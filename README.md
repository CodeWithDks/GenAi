# 🚀 GenAi — Learning Generative AI with LangChain & LangGraph

A structured, hands-on learning repository covering **LangChain**
fundamentals through **LangGraph** agent workflows. Each folder is one
concept, numbered in the order it makes sense to learn — this isn't one
big application, it's a growing set of focused, working examples that
build on each other.

> 👉 **New here?** Start with [`LangChain/README.md`](./LangChain/README.md) —
> a 14-step path from "call a model" to "run a tool-using agent that survives
> a bad day", with a notebook and a small project for every step.

---

## 📂 Repository Structure

```
.
├── LangChain/          # Fundamentals — models, prompts, chains, RAG, tools, agents
│   ├── 01_Models
│   ├── 02_Prompts
│   ├── 03_Runnables
│   ├── 04_Chains
│   ├── 05_Structured_Output
│   ├── 06_Document_Loaders
│   ├── 07_Text_Splitters
│   ├── 08_Vector_Store
│   ├── 09_Retriever
│   ├── 10_RAG_Project
│   ├── 11_Tools
│   ├── 12_Tool_Calling
│   ├── 13_Agents
│   ├── 14_Error_Handling
│   └── README.md
│
├── LangGraph/           # Stateful agent workflows, built on LangChain
│   ├── 01_Sequential_Workflows
│   ├── 02_Conditional_Workflows
│   ├── 03_Parallel_Workflows
│   ├── 04_Iterative
│   ├── 05_Tool_Calling
│   ├── 06_Subgraphs
│   ├── 07_Middleware
│   ├── 08_HITL
│   ├── 09_Memory_Persistence
│   ├── 10_Multiagent
│   ├── 11_Orchestrator
│   ├── 12_Long_Term_Memory
│   ├── 13_Streaming
│   └── README.md
│
├── LICENSE
├── .gitignore
└── README.md
```

Each section has its own README with the full folder-by-folder breakdown
and the reasoning behind the order:

- 📘 **[`LangChain/README.md`](./LangChain/README.md)** — models → prompts
  → the Runnable abstraction → chains → structured output → documents →
  splitting → vector stores → retrieval → a full RAG project → tools →
  tool calling → agents → error handling
- 📗 **[`LangGraph/README.md`](./LangGraph/README.md)** — sequential →
  conditional → parallel → iterative workflows → tool calling in a graph
  → subgraphs → middleware → human-in-the-loop → memory → multi-agent →
  orchestration → long-term memory → streaming

## 🧠 Why two sections

**LangChain** covers the fundamentals: talking to a model, structuring
prompts, chaining calls together, grounding responses in real documents,
giving a model tools, and keeping it all running when things fail.
**LangGraph** takes those same building blocks and orchestrates them into
*stateful graphs* — workflows that can branch, loop, pause for human
approval, persist memory across sessions, and coordinate multiple agents.
Learning them in this order means every LangGraph example builds on a
LangChain concept already covered, instead of introducing everything at
once.

---

## 🛠 Technologies Used

- Python 3.10+
- [LangChain](https://python.langchain.com/) (`langchain`, `langchain-core`,
  `langchain-text-splitters`, `langchain-classic`)
- [LangGraph](https://langchain-ai.github.io/langgraph/)
- Groq (`langchain-groq`) — free tier; used by the `LangChain/` notebooks
- OpenAI (`langchain-openai`) — used by the `LangGraph/` notebooks
- Google Gemini (`langchain-google-genai`)
- Hugging Face (`langchain-huggingface`, `sentence-transformers`) — free,
  local embeddings
- FAISS (`faiss-cpu`) and Chroma (`langchain-chroma`, `chromadb`)
- BM25 hybrid search (`rank_bm25`)
- Pydantic
- python-dotenv
- Jupyter

> ⚠️ `langchain-community` and `langchain-experimental` are being sunset by
> LangChain (no new features, limited maintenance). A few notebooks still
> use them (document loaders, FAISS, BM25, the shell tool, semantic
> chunking), so they are pinned — see `LangChain/README.md` →
> *Package status*.

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/CodeWithDks/GenAi.git
cd GenAi
```

Create a virtual environment (Python 3.10 or newer):

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies for the section you want to run.

**For `LangChain/`** (everything at once; each notebook also has its own
`%pip install` line at the top if you'd rather install per notebook):

```bash
pip install -U langchain langchain-core langchain-text-splitters langchain-classic langgraph \
            langchain-groq langchain-openai langchain-google-genai langchain-huggingface \
            huggingface_hub sentence-transformers tiktoken \
            langchain-chroma chromadb faiss-cpu rank_bm25 \
            pypdf beautifulsoup4 ddgs grandalf \
            python-dotenv "pydantic[email]" numpy jupyter

# Pinned on purpose — both are being sunset
pip install "langchain-community==0.4.2" "langchain-experimental==0.4.2"
```

**For `LangGraph/`:**

```bash
pip install -U langgraph langchain langchain-core langchain-openai pydantic python-dotenv jupyter
```

`LangGraph/04_Iterative/Self-Healing-SQL-Agent.ipynb` additionally needs
`psycopg2-binary` and a PostgreSQL database.

> 💡 A pinned `requirements.txt` isn't checked into the repo yet — install
> the packages above, or generate one with `pip freeze > requirements.txt`
> once your environment is set up.

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```

Which key you need depends on the section:

| Key | Needed for |
|---|---|
| `GROQ_API_KEY` | Most `LangChain/` notebooks (free tier). `08_Vector_Store`, `11_Tools` and `14_Error_Handling` need no key |
| `OPENAI_API_KEY` | The `LangGraph/` notebooks (they use `ChatOpenAI`). Optional in `LangChain/` |
| `GOOGLE_API_KEY` | Optional — `LangChain/01_Models` only |
| `HUGGINGFACEHUB_API_TOKEN` | Optional — `LangChain/01_Models` only (the hosted-endpoint cell) |

`LangChain/` is designed to run on free tiers; `LangGraph/` assumes an
OpenAI key. `LangChain/README.md` has a notebook-by-notebook table of
what each one needs.

Some `LangGraph/` notebooks may need their own local `.env` in the same
folder — check that subfolder's README where one exists.

---

## ▶ Running Examples

Open any notebook in Jupyter and run it top to bottom:

```bash
jupyter notebook LangChain/01_Models/01_chat_models.ipynb
jupyter notebook LangChain/10_RAG_Project/01_rag_chatbot.ipynb
jupyter notebook LangChain/13_Agents/01_agents.ipynb
jupyter notebook LangGraph/10_Multiagent/multiagent-content-team.ipynb
```

Notebooks that need sample files create their own in a `sample_docs/`
folder next to them. A few folders also keep their original standalone
scripts, which run directly (this one uses OpenAI, so it needs
`OPENAI_API_KEY`):

```bash
python LangChain/12_Tool_Calling/first_tool_calling.py
```

---

## 🎯 Learning Roadmap

- [x] LangChain fundamentals — models, prompts, Runnables, chains
- [x] Structured output, document loaders, text splitters
- [x] Vector stores & retrievers, and a full RAG project
- [x] Tools, tool calling, agents & error handling
- [x] LangGraph — sequential, conditional, parallel & iterative workflows
- [x] LangGraph tool calling
- [x] Subgraphs & middleware
- [x] Human-in-the-loop (HITL)
- [x] Memory & persistence, including long-term memory
- [x] Multi-agent systems & orchestration
- [x] Streaming
- [ ] Model Context Protocol (MCP) — see my separate
      [`mcp`](https://github.com/CodeWithDks/mcp) repo
- [ ] End-to-end, production-style AI projects

---

## 📌 Repository Purpose

This repository exists to:

- Learn LangChain and LangGraph from the ground up, one concept at a time
- Practice core Generative AI building blocks before combining them into
  full applications
- Keep reusable, well-documented reference code for future projects
- Track learning progress toward building production-ready AI systems

---

## 🤝 Contributions

This is primarily a personal learning repository, but suggestions and
improvements are always welcome — feel free to open an issue or PR.

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE).

---

## ⭐ Acknowledgements

- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- Groq
- OpenAI
- Google Gemini
- Hugging Face
- FAISS & Chroma
- Python community

---

## 👨‍💻 Author

Built by [Deepak Kumar Singh](https://github.com/CodeWithDks) as a
hands-on Generative AI learning project.
