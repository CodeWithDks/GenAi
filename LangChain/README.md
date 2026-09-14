# LangChain

A structured, numbered walkthrough of LangChain — each folder is one
concept, in the order it actually makes sense to learn them: start by
talking to a model directly, then layer on prompts, the Runnable
abstraction, chains, structured output, documents, retrieval, and
finally tools. By the end, `LangChain/` covers everything needed before
moving on to [`../LangGraph/`](../LangGraph/) for stateful, multi-step
agent workflows.

## Folders

| # | Folder | What it covers |
|---|---|---|
| 01 | [`Models`](./01_Models) | Talking to chat models directly — OpenAI and Google Gemini |
| 02 | [`Prompts`](./02_Prompts) | `PromptTemplate`, `ChatPromptTemplate`, message types (`SystemMessage`/`HumanMessage`/`AIMessage`), and `MessagesPlaceholder` for chat history |
| 03 | [`Runnables`](./03_Runnables) | A from-scratch mini implementation of a prompt template, LLM wrapper, and chain — for understanding what LangChain's `Runnable`/LCEL abstraction is actually doing under the hood |
| 04 | [`Chains`](./04_Chains) | Composing `prompt \| model \| parser` pipelines — simple, sequential, parallel (`RunnableParallel`), and conditional (`RunnableBranch`) |
| 05 | [`Structured_Output`](./05_Structured_Output) | Getting typed/structured data back from an LLM using `TypedDict` and Pydantic with `with_structured_output` |
| 06 | [`Document_Loaders`](./06_Document_Loaders) | Loading raw content into LangChain `Document` objects from `.txt`, `.csv`, `.pdf`, and web pages |
| 07 | [`Text_Splitters`](./07_Text_Splitters) | Breaking large documents into chunks with `CharacterTextSplitter` and `RecursiveCharacterTextSplitter` |
| 08 | [`Vector_Store`](./08_Vector_Store) | Creating embeddings and storing them in FAISS and Chroma for semantic search |
| 09 | [`Retriever`](./09_Retriever) | Turning vector stores into retrievers — similarity search, MMR, multi-query, contextual compression, and Wikipedia as a retriever |
| 10 | [`Tools`](./10_Tools) | Three ways to define a tool (`@tool`, `StructuredTool`, `BaseTool`), plus built-in tools (DuckDuckGo, Shell) and grouping tools into a toolkit |
| 11 | [`Tool_Calling`](./11_Tool_Calling) | Binding tools to a chat model with `bind_tools` and manually running the tool-call → `ToolMessage` → final-answer loop |

## Why this order

Each numbered step depends on the ideas before it:

- **01–02** get a model responding to a well-structured prompt — the
  foundation everything else sits on.
- **03** pulls back the curtain on *how* LangChain actually chains things
  together, before relying on that abstraction in **04**.
- **05** adds structure to what comes *out* of the model, which matters
  once real applications need to act on a response, not just display it.
- **06–07** shift from "talking to a model" to "grounding a model in real
  content" — the prerequisite for any retrieval-based application.
- **08–09** turn that content into something searchable.
- **10–11** give the model the ability to *act*, not just answer — the
  natural last step before LangGraph, where those actions get orchestrated
  into multi-step, stateful workflows.

## Running an example

Each script is standalone — run any file directly:

```bash
python LangChain/04_Chains/simple_chain.py
python LangChain/09_Retriever/based_on_retrievers/mmr.py
python LangChain/11_Tool_Calling/first_tool_calling.py
```

A few are Streamlit apps:

```bash
streamlit run LangChain/02_Prompts/website.py
streamlit run LangChain/01_Models/gemini-chatbot.py
```

See the [repo root README](../README.md) for environment variables
(`OPENAI_API_KEY`, `GOOGLE_API_KEY`) and full dependency installation.

## Next step

Once this section feels solid, [`../LangGraph/`](../LangGraph/) picks up
where it leaves off — the same building blocks, orchestrated into
stateful graphs: conditional and parallel workflows, human-in-the-loop
approval, subgraphs, middleware, multi-agent systems, and memory
persistence.