# 10 — RAG Project: Chat With Your Documents

Folders `06` through `09` built four separate pieces: loaders, splitters, a vector store, and
retrievers. This folder wires all four into one working application, plus the one piece none of them
covered on their own: **conversational memory**, so a follow-up like *"How long does that take?"*
resolves against the previous turn instead of searching for the meaningless word "that."

## Notebook

| # | Notebook | What it covers |
|---|---|---|
| 1 | [`01_rag_chatbot.ipynb`](./01_rag_chatbot.ipynb) | The full pipeline in seven steps: load → split → store → retrieve → make the retriever history-aware → answer → wrap with per-session memory. Ends with a terminal chat loop, a second independent session, and a look at which chunks each answer was built from |

## The one new idea

A plain retriever takes one string and searches for it. In a multi-turn conversation that breaks:
searching the vector store for the literal text "How long does that take?" finds nothing useful.
`create_history_aware_retriever` fixes this by asking the model to rewrite the follow-up into a
standalone question using the chat history, and only then searching. `RunnableWithMessageHistory`
keeps one history per `session_id`, so two users never see each other's conversation.

`create_history_aware_retriever`, `create_retrieval_chain`, and `create_stuff_documents_chain` live
in `langchain_classic.chains`, the same `langchain-classic` package introduced in `09_Retriever`.

## What was verified, and what wasn't

This notebook was built in a sandbox with no access to Groq or Hugging Face, so the verification has
a clear boundary:

- **Verified by running it:** every cell executes without errors; the real Chroma index is built and
  queried; the chain assembles correctly; session memory is isolated (in the test, one session ended
  with 4 messages after two turns and a second session with only its own 2).
- **Not verified:** whether the Groq model actually rewrites "that" into a useful standalone question,
  and how good the final answers are. A fake chat model and fake embeddings stood in for those parts.

So treat your first real run as the actual test: ask the refund question, then the vague follow-up,
and check that the turn-2 answer is about refund timing. If it isn't, the `contextualize_prompt` in
Step 5 is the first thing to tune.

## What you should be able to do after this folder

- Explain why a plain retriever fails on follow-up questions, and what the history-aware step does
  about it.
- Name the pieces of the pipeline in order and say which earlier folder each one came from.
- Explain what `session_id` is for, and why a plain Python dict is fine for learning but not for a
  deployed app (history is lost on restart; use Redis or a database).
- Swap one stage (for example the `mmr` or `EnsembleRetriever` from `09`) without touching the rest.
- Use `response["context"]` to see which chunks an answer came from.

## Prerequisites

Same as earlier folders — see the [repo root README](../README.md). This notebook uses:

```bash
pip install langchain-classic langchain-chroma langchain-huggingface langchain-groq
pip install "langchain-community==0.4.2"   # DirectoryLoader/TextLoader — see the sunset note in 06
```

You need a `GROQ_API_KEY` in your `.env`. Embeddings run locally and need no key.

## Running

```bash
jupyter notebook 01_rag_chatbot.ipynb
```

The notebook creates its own `sample_docs/` folder and rebuilds the Chroma index on every run, so it
works with no setup. For a real app, build the index once and reopen it on start (the persistence
pattern from `08_Vector_Store`).

## Next

[`11_Tools/`](../11_Tools) — this project answers from what it already knows. Next, the model learns
to *act*: call a function, look something up, or take an action, starting with how to define a tool.
