# 🚀 GenAi — Learning Generative AI with LangChain & LangGraph

A structured, hands-on learning repository covering **LangChain**
fundamentals through **LangGraph** agent workflows. Each folder is one
concept, numbered in the order it makes sense to learn — this isn't one
big application, it's a growing set of focused, working examples that
build on each other.

---

## 📂 Repository Structure

```
.
├── LangChain/          # Fundamentals — models, prompts, chains, RAG, tools
│   ├── 01_Models
│   ├── 02_Prompts
│   ├── 03_Runnables
│   ├── 04_Chains
│   ├── 05_Structured_Output
│   ├── 06_Document_Loaders
│   ├── 07_Text_Splitters
│   ├── 08_Vector_Store
│   ├── 09_Retriever
│   ├── 10_Tools
│   ├── 11_Tool_Calling
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
  splitting → vector stores → retrieval → tools → tool calling
- 📗 **[`LangGraph/README.md`](./LangGraph/README.md)** — sequential →
  conditional → parallel → iterative workflows → tool calling in a graph
  → subgraphs → middleware → human-in-the-loop → memory → multi-agent →
  orchestration

## 🧠 Why two sections

**LangChain** covers the fundamentals: talking to a model, structuring
prompts, chaining calls together, grounding responses in real documents,
and giving a model tools. **LangGraph** takes those same building blocks
and orchestrates them into *stateful graphs* — workflows that can branch,
loop, pause for human approval, persist memory across sessions, and
coordinate multiple agents. Learning them in this order means every
LangGraph example builds on a LangChain concept already covered, instead
of introducing everything at once.

---

## 🛠 Technologies Used

- Python
- [LangChain](https://python.langchain.com/) (`langchain-core`,
  `langchain-community`, `langchain-classic`, `langchain-text-splitters`)
- [LangGraph](https://langchain-ai.github.io/langgraph/)
- OpenAI (`langchain-openai`)
- Google Gemini (`langchain-google-genai`)
- FAISS (`langchain-community` vector store)
- Chroma (`langchain-chroma`, `chromadb`)
- Pydantic
- Streamlit
- python-dotenv

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/CodeWithDks/GenAi.git
cd GenAi
```

Create a virtual environment:

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

Install the core dependencies used across these examples:

```bash
pip install langchain langchain-openai langchain-community langchain-classic \
            langchain-google-genai langchain-chroma langchain-text-splitters \
            langgraph chromadb faiss-cpu pydantic python-dotenv streamlit \
            pypdf duckduckgo-search
```

> 💡 A pinned `requirements.txt` isn't checked into the repo yet — install
> the packages above, or generate one with `pip freeze > requirements.txt`
> once your environment is set up.

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

`OPENAI_API_KEY` is required for most examples across both `LangChain/`
and `LangGraph/`. `GOOGLE_API_KEY` is only needed for
`LangChain/01_Models/gemini-chatbot.py`.

Some `LangGraph/` notebooks may need their own local `.env` in the same
folder — check that subfolder's README where one exists.

---

## ▶ Running Examples

Run any standalone LangChain script directly:

```bash
python LangChain/04_Chains/simple_chain.py
python LangChain/09_Retriever/based_on_retrievers/mmr.py
python LangChain/11_Tool_Calling/first_tool_calling.py
```

Run the Streamlit apps:

```bash
streamlit run LangChain/02_Prompts/website.py
streamlit run LangChain/01_Models/gemini-chatbot.py
```

Open any LangGraph notebook in Jupyter:

```bash
jupyter notebook LangGraph/10_Multiagent/multiagent-content-team.ipynb
```

---

## 🎯 Learning Roadmap

- [x] LangChain fundamentals — models, prompts, Runnables, chains
- [x] Structured output, document loaders, text splitters
- [x] Vector stores & retrievers
- [x] Tools & tool calling
- [x] LangGraph — sequential, conditional, parallel & iterative workflows
- [x] LangGraph tool calling
- [x] Subgraphs & middleware
- [x] Human-in-the-loop (HITL)
- [x] Memory & persistence
- [x] Multi-agent systems & orchestration
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
- OpenAI
- Google Gemini
- FAISS & Chroma
- Python community

---

## 👨‍💻 Author

Built by [Deepak Kumar Singh](https://github.com/CodeWithDks) as a
hands-on Generative AI learning project.