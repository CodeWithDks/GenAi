# 🦜 LangChain — A 14-Step Learning Path

A practice-first walk through LangChain 1.x, from "call a model" to "run a tool-using agent that
survives a bad day". Every topic is a Jupyter notebook that explains the idea in plain language, builds
it from scratch where that helps, and ends with a small real-world project (mostly one running example:
a **customer-support assistant**).

**Status:** complete — 14 topics, 15 notebooks, each folder with its own README.

---

## 🗺 The path

```
 FOUNDATIONS                     RETRIEVAL (RAG)                          AGENTS & TOOLS
 ───────────                     ───────────────                          ──────────────
 01 Models ──► 02 Prompts        06 Document Loaders ──► 07 Text          11 Tools ──► 12 Tool Calling
      │              │                                      Splitters            │              │
      ▼              ▼                       │                  │               ▼              ▼
 03 Runnables ──► 04 Chains                  ▼                  ▼          13 Agents ──► 14 Error Handling
      │                                08 Vector Store ──► 09 Retriever
      ▼                                                         │
 05 Structured Output                                           ▼
                                                        10 RAG Project (capstone)
```

| Phase | Folders | The question it answers |
|---|---|---|
| **Foundations** | `01`–`05` | How do I talk to a model, shape what I send, compose steps, and get usable data back? |
| **Retrieval** | `06`–`10` | How do I let a model answer from *my* documents instead of guessing? |
| **Agents & tools** | `11`–`14` | How do I let a model *do* things — and keep it safe and standing when things fail? |

---

## 📚 Curriculum

| # | Folder | Notebook(s) | What you'll learn | Capstone |
|---|---|---|---|---|
| 01 | [`01_Models`](./01_Models) | [`01_chat_models`](./01_Models/01_chat_models.ipynb), [`02_embedding_models`](./01_Models/02_embedding_models.ipynb) | Chat models (text → text) across OpenAI, Gemini, Groq and Hugging Face, with Anthropic as a reference example; embedding models (text → vectors); the shared `invoke`/`stream`/`batch` interface | Multi-provider support assistant with automatic fallback; a semantic ticket router |
| 02 | [`02_Prompts`](./02_Prompts) | [`01_prompt_templates`](./02_Prompts/01_prompt_templates.ipynb) | `PromptTemplate` vs `ChatPromptTemplate`, `MessagesPlaceholder` (`optional`, `n_messages`), few-shot prompting, `.partial()`, composition, the prompt-caching trap | Support chatbot with consistent tone and bounded memory |
| 03 | [`03_Runnables`](./03_Runnables) | [`01_runnables_from_scratch`](./03_Runnables/01_runnables_from_scratch.ipynb) | What `\|` really does — you build a tiny `Runnable` first, then use `RunnableLambda`, `Parallel`, `Passthrough`, `Branch` | Ticket-triage pipeline (parallel + branching) |
| 04 | [`04_Chains`](./04_Chains) | [`01_chains`](./04_Chains/01_chains.ipynb) | Simple, sequential, parallel (+ merge) and conditional chains; drawing a chain with `get_graph()` | Study-guide generator with translation |
| 05 | [`05_Structured_Output`](./05_Structured_Output) | [`01_structured_output`](./05_Structured_Output/01_structured_output.ipynb) | Pydantic primer; `with_structured_output` with `TypedDict` vs `BaseModel`; nested schemas; the parser fallback | Batch review analysis with aggregate statistics |
| 06 | [`06_Document_Loaders`](./06_Document_Loaders) | [`01_document_loaders`](./06_Document_Loaders/01_document_loaders.ipynb) | The `Document` object; Text, CSV, PDF, Web and Directory loaders; `lazy_load`; metadata | Ingestion pipeline + the three walls of "paste everything into the prompt" |
| 07 | [`07_Text_Splitters`](./07_Text_Splitters) | [`01_text_splitters`](./07_Text_Splitters/01_text_splitters.ipynb) | Character vs recursive splitting, overlap, token-based sizing, Markdown and code splitters, semantic chunking, contextual retrieval | Chunking a knowledge base, with a measured contextual-retrieval comparison |
| 08 | [`08_Vector_Store`](./08_Vector_Store) | [`01_vector_stores`](./08_Vector_Store/01_vector_stores.ipynb) | FAISS vs Chroma, persistence, metadata filtering, incremental updates | A knowledge base that survives a restart with zero re-embedding |
| 09 | [`09_Retriever`](./09_Retriever) | [`01_retrievers`](./09_Retriever/01_retrievers.ipynb) | MMR, multi-query, hybrid (BM25 + vector) search, contextual compression, parent-document retrieval — each framed by the failure it fixes | Tuned support retriever feeding an answer chain |
| 10 | [`10_RAG_Project`](./10_RAG_Project) | [`01_rag_chatbot`](./10_RAG_Project/01_rag_chatbot.ipynb) | Wiring `06`–`09` together; history-aware retrieval so follow-ups like "how long does *that* take?" work; per-session memory | **Chat with your documents**, as a terminal chatbot |
| 11 | [`11_Tools`](./11_Tools) | [`01_tools`](./11_Tools/01_tools.ipynb) | Three ways to build a tool, `parse_docstring`, error handling, async, built-in tools, retriever-as-a-tool, toolkits | A support-desk toolbox, exercised by a hand-written dry run |
| 12 | [`12_Tool_Calling`](./12_Tool_Calling) | [`01_tool_calling`](./12_Tool_Calling/01_tool_calling.ipynb) | `bind_tools`, the call → execute → return loop, parallel calls, failure handling, streaming, `tool_choice`, guardrails | Support assistant whose refund tool enforces its own rules |
| 13 | [`13_Agents`](./13_Agents) | [`01_agents`](./13_Agents/01_agents.ipynb) | `create_agent`; how it maps to the loop you wrote; middleware for limits, retries, tool errors and human approval; thread memory | The support agent, assembled with approvals and memory |
| 14 | [`14_Error_Handling`](./14_Error_Handling) | [`01_error_handling`](./14_Error_Handling/01_error_handling.ipynb) | `.with_retry()`, `.with_fallbacks()`, rate limiting, batch failures, bad model output, idempotency | Ticket triage that survives rate limits, outages and garbage input |

---

## 🧭 Why this order

- **Models → Prompts → Runnables → Chains → Structured output.** Each step is a prerequisite for the
  next. `03` is deliberately "build it yourself": `prompt | model` stops being magic before you lean on it
  for the rest of the track.
- **Loaders → Splitters → Vector store → Retriever → RAG project.** The four pieces of retrieval, in the
  order data flows through them. `06` ends by *measuring* why pasting whole documents into a prompt
  stops working, so the next four notebooks have a reason to exist. `10` is where they become one app.
- **Tools → Tool calling → Agents → Error handling.** `11` builds the menu and the kitchen; `12` has the
  model order from it, via a loop you write by hand; `13` shows the same loop packaged as an agent (and
  which of your protections it quietly *doesn't* give you); `14` is how you keep all of it standing.

---

## ⚙ Setup

**Python 3.10 or newer** (required by the LangChain 1.x packages, and used by the notebooks' type
hints).

### Install

Each notebook has its own `%pip install` line at the top listing exactly what it needs. To install
everything for the whole track at once:

```bash
pip install -U langchain langchain-core langchain-text-splitters langchain-classic langgraph \
  langchain-groq langchain-openai langchain-google-genai langchain-huggingface \
  huggingface_hub sentence-transformers tiktoken \
  langchain-chroma faiss-cpu rank_bm25 \
  pypdf beautifulsoup4 ddgs grandalf \
  python-dotenv "pydantic[email]" numpy jupyter

# Pinned on purpose: both packages are being sunset (see "Package status" below)
pip install "langchain-community==0.4.2" "langchain-experimental==0.4.2"

# Optional: only to run the Anthropic example cell in 01_Models, which also needs a paid key
pip install langchain-anthropic
```

### API keys

Create a `.env` file in the repo root (python-dotenv searches upward from where the notebook runs):

```bash
GROQ_API_KEY=gsk_...              # free — used by most notebooks
OPENAI_API_KEY=sk-...             # optional (paid) — 01_Models, and as a drop-in elsewhere
GOOGLE_API_KEY=...                # optional (free tier) — 01_Models only
HUGGINGFACEHUB_API_TOKEN=hf_...   # optional (free) — 01_Models only (the hosted-endpoint cell)
```

Which notebook needs what:

| Notebooks | Needs |
|---|---|
| `01_Models` | Any providers you want to try; each section is independent, so skip the ones you have no key for. Embeddings can run fully locally |
| `02`–`07`, `09`, `10`, `12`, `13` | `GROQ_API_KEY` for the live cells. `07`, `09` and `10` also download a small local embedding model on first use |
| `08_Vector_Store`, `11_Tools` | No key. Local embeddings only (`11`'s web-search cell also needs internet) |
| `14_Error_Handling` | No key. It runs the real client against a built-in fake server |

Everything runs on free tiers: Groq and Gemini are free, embeddings run locally, and OpenAI is
optional throughout.

### Run

```bash
jupyter notebook
```

Open a folder, read its `README.md`, then run the notebook top to bottom. Notebooks that need sample
files create their own in a `sample_docs/` folder next to them. If a folder still holds older standalone
`.py` scripts from the first pass of this repo, the notebook is the version to follow.

---

## 🧩 How each notebook is built

Every notebook follows the same shape, so you always know where you are:

1. **A short intro** — the idea in plain language, plus a "worth knowing" box with anything that
   changed recently or commonly goes wrong.
2. **Concepts in small steps** — each a short explanation followed by a runnable cell.
3. **A real-world capstone** — usually the customer-support scenario, so ideas accumulate instead of
   restarting from scratch each time.
4. **Try it yourself** — a few exercises, some of them deliberately breaking something.
5. **Next** — what the following notebook builds on.

---

## ⚠ Gotchas this track covers

Each of these was confirmed by running it, and each fails *quietly* rather than loudly.

| Gotcha | Where |
|---|---|
| `chain.get_graph().print_ascii()` needs the `grandalf` package, or it raises `ImportError` | `04` |
| A Pydantic `EmailStr` field needs `pydantic[email]` (the `email-validator` package) | `05` |
| `PyPDFLoader`'s `metadata["page"]` is zero-based; `page_label` is the number a human sees | `06` |
| `tiktoken` downloads its encoding file on first use, which some networks block | `07` |
| Chroma rejects collection names shorter than 3 characters | `08` |
| `MultiQuery`, `Ensemble`, `ContextualCompression` and `ParentDocument` retrievers moved to `langchain-classic` | `09` |
| `@tool` drops docstring parameter descriptions unless `parse_docstring=True` | `11` |
| `handle_tool_error=True` only catches `ToolException`, not a plain `ValueError` | `11` |
| A malformed tool call can arrive as an *empty* `tool_calls`, which looks like "the model is done" | `12` |
| A truncated *streamed* tool call is silently repaired into one that looks valid but is missing an argument | `12` |
| An agent's default step limit is 10007 — effectively none | `13` |
| In an agent, a tool raising `ToolException` crashes the run unless you opt in to handling it | `13` |
| `.with_retry()` retries *every* exception by default, including a bad API key | `14` |
| Stacking `.with_retry(3)` on a client that already retries made 9 requests, not 3 | `14` |
| `wait_exponential_jitter=False` means *no waiting at all*, not plain backoff | `14` |
| `.with_retry()` plus `.batch()` is order-dependent and can overwrite good results with one error | `14` |

---

## 📦 Package status

- **`langchain-community`** — LangChain has announced its sunset (see issue #674 in the
  `langchain-community` repository): no new integrations or features, limited maintenance, and a
  direction of one standalone package per provider. The loaders (`06`), FAISS (`08`), BM25 (`09`) and
  the built-in tools (`11`) still come from it, so it is pinned to `0.4.2`. The notebooks keep these
  calls behind small functions so that moving to a standalone package later touches one place.
- **`langchain-experimental`** — also being sunset (it prints a deprecation notice on import). It is only
  needed for `SemanticChunker` (`07`) and `ShellTool` (`11`).
- **`langchain-classic`** — not deprecated. It holds the pre-1.0 APIs LangChain still supports,
  including several retrievers (`09`), `create_history_aware_retriever` (`10`), and `OutputFixingParser`
  (`14`). `AgentExecutor` also lives only here now; new code should use `create_agent` (`13`).

---

## 🧪 How this was tested

Honest notes on what "tested" means, so you know where to look first if something differs on your
machine. The final checks used `langchain 1.4.x`, `langchain-core 1.6.x`, `langgraph 1.2.x`,
`langchain-groq 1.1.x`, `langchain-classic 1.0.x`, `langchain-community 0.4.2` and
`langchain-experimental 0.4.2`.

| Folders | What was run |
|---|---|
| `01`–`05` | Every code cell executed against **stand-in models and embeddings**. This confirms the code runs, not what a real model replies |
| `06`, `07`, `09` | Cells that need no network or live chat model were executed (loaders on real files, splitters, retrievers; stand-in embeddings where a retriever needed them). Cells calling Groq, downloading a real embedding model, or fetching a web page were not |
| `08`, `10`, `11` | Every cell executed with stand-in embeddings (and, for `10`, a stand-in chat model), against real FAISS, Chroma and chain code. The web-search cell in `11` was not |
| `12`, `13` | Every cell executed against stand-in models. In `13` the agent, middleware, checkpointer and approval flow are the real `create_agent` |
| `14` | Every cell executed. The real `ChatGroq` client, retry, fallback and rate-limiter code run against a fake HTTP server |

**Also not tested:** the all-in-one install command under *Setup*. It was assembled from the notebooks' own
`%pip` lines and imports, but never run as a single command in a clean environment. If pip reports a
conflict, install per notebook using the line at the top of each one.

**What was never tested:** any live provider. Real servers choose their own `Retry-After` timing, error
bodies and failure patterns, and no one has yet seen, in these notebooks, what a real model chooses to do
on these questions. Treat your first live run as the real test — each folder's README lists exactly what
its notebook does and doesn't rest on.

---

## ➡ After LangChain

This track is the foundation for the [`../LangGraph`](../LangGraph) folder. It picks up exactly where
`13_Agents` leaves off: `05_Tool_Calling`, `07_Middleware`, `08_HITL`, `09_Memory_Persistence`,
`12_Long_Term_Memory` and `13_Streaming` are the graph-level versions of what `13` declares in a line each.