# 01 — Models

Every LangChain app rests on one primitive: a **model**. This folder covers both kinds you'll
ever call — **chat models** (text → text) and **embedding models** (text → vectors) — across
every provider actually available to us: OpenAI (paid), Gemini (free), Groq (free), Anthropic
(reference only, no key), and Hugging Face (free/open-source).

## Notebooks

| # | Notebook | What it covers |
|---|---|---|
| 1 | [`01_chat_models.ipynb`](./01_chat_models.ipynb) | The chat model interface (`.invoke`/`.stream`/`.batch`), messages, all five providers side by side, generation parameters (`temperature`, `reasoning_effort`, `max_tokens`), a provider-agnostic factory function, and a capstone: a multi-provider support assistant with automatic fallback |
| 2 | [`02_embedding_models.ipynb`](./02_embedding_models.ipynb) | What embeddings actually are, `embed_query` vs. `embed_documents`, which providers support embeddings and which don't, cosine similarity from scratch, and a capstone: a semantic support-ticket router |

## Why this order

Chat models first, embeddings second — deliberately:

- **Chat models** are the more intuitive entry point: you send a message, you get a message back.
  There's an immediate, visible result, which makes the *provider* differences (speed, cost, free
  tier limits) easy to feel rather than just read about.
- **Embedding models** are a different mental model — text goes in, a list of numbers comes out,
  and the "result" is invisible until you do something with it (like measure similarity). Seeing
  chat models work first gives you a reference point for "normal" model behavior before this
  notebook asks you to trust a black-box vector.
- Both notebooks build toward the same destination: `06_Document_Loaders/` through
  `09_Retriever/` need embeddings to exist, and `10_Tools/`/`11_Tool_Calling/` need chat models
  that can reason about when to call something. This folder is the prerequisite for both branches.

## Provider cheat sheet

| Provider | Chat models | Embeddings | Your access | Notes |
|---|---|---|---|---|
| **OpenAI** | ✅ | ✅ | Paid | Most reliable, best docs — your fallback of last resort (costs money) |
| **Google Gemini** | ✅ | ✅ | Free (Flash-tier only) | Generous free quota, huge context window |
| **Groq** | ✅ | ❌ | Free | Fastest inference by far — no embeddings endpoint exists |
| **Anthropic** | ✅ | ❌ | None — code shown as reference | No native embeddings API; Anthropic points to Voyage AI instead |
| **Hugging Face** | ✅ | ✅ | Free | Fully free, runs open models — best for learning without spending anything |

## Prerequisites

```bash
pip install langchain langchain-core python-dotenv
pip install langchain-openai langchain-google-genai langchain-groq langchain-huggingface
pip install langchain-anthropic huggingface_hub sentence-transformers numpy
```

Create a `.env` file in this folder (or the repo root — see the [repo root README](../README.md)):

```bash
OPENAI_API_KEY=sk-...
GOOGLE_API_KEY=...
GROQ_API_KEY=gsk_...
HUGGINGFACEHUB_API_TOKEN=hf_...
# ANTHROPIC_API_KEY=...   # not required — Anthropic cells are reference-only in this folder
```

## Running

Open either notebook and run cells top to bottom — each one is self-contained and picks up
whatever keys are present in your `.env`. Missing a key for a provider? Skip that section; the
rest of the notebook doesn't depend on it, except the fallback capstone in
`01_chat_models.ipynb`, which is *designed* to keep working even when a provider is missing.

```bash
jupyter notebook 01_chat_models.ipynb
jupyter notebook 02_embedding_models.ipynb
```

## What you should be able to do after this folder

- Call any of the five providers with the exact same code shape, and explain *why* that
  consistency is LangChain's actual value proposition.
- Explain the difference between `temperature` and `reasoning_effort`, and know when GPT-5 ignores
  the one you'd expect.
- Write a function that falls back across providers when one fails or is rate-limited.
- Explain, in one sentence, why embeddings turn "find similar text" from a keyword problem into a
  meaning problem.
- Compute cosine similarity between two vectors without importing a library that does it for you.

## Next

[`02_Prompts/`](../02_Prompts) — turning the hardcoded `SystemMessage`/`HumanMessage` pairs from
this folder into reusable, parameterized templates.