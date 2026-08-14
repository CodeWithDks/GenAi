# 🚀 Learning Generative AI using LangChain

This repository is my hands-on learning journey into **Generative AI** with **LangChain**. It's a collection of small, focused scripts — each one exploring a single LangChain concept — rather than one big application. Together they build up to the core skills needed to build real LLM-powered apps: chatbots, document Q&A, RAG pipelines, agents with tools, and structured-output extraction.

---

## 📚 Topics Covered

- Chat models (OpenAI & Gemini)
- Prompt templates & chat prompt templates
- Message history / `MessagesPlaceholder`
- Chains — simple, sequential, parallel, conditional (`RunnableBranch`)
- The custom Runnable interface (building LangChain's `Runnable` pattern from scratch)
- Document loaders (Text, CSV, PDF, Web)
- Text splitters (character-based & recursive/structure-based)
- Structured output (`TypedDict`, Pydantic, `with_structured_output`)
- Vector stores (FAISS, Chroma)
- Retrievers (similarity, MMR, multi-query, contextual compression, Wikipedia)
- Retrieval-Augmented Generation (RAG) with `RetrievalQA`
- Tools — `@tool`, `StructuredTool`, `BaseTool`, and toolkits
- Tool calling with an LLM (`bind_tools`)
- Built-in tools (DuckDuckGo search, Shell)
- Streamlit mini-apps (Gemini chatbot, AI website builder)

---

## 📂 Project Structure

```
.
├── Chains/                          # Simple, sequential, parallel & conditional chains
│   ├── simple_chain.py
│   ├── sequential_chain.py
│   ├── parallel_chain.py
│   ├── conditional_chain.py
│   └── Text.txt
│
├── Documents_Loader/                 # Loading docs: text, CSV, PDF, web pages
│   ├── simple-text.py
│   ├── doc-csv.py
│   ├── doc-pdf.py
│   └── web-scrip.py
│
├── Models/
│   └── ChatModels/                   # Chat model examples
│       ├── openai-chatbot.py
│       └── gemini-chatbot.py         # Streamlit chatbot using Gemini
│
├── Prompts/                          # Prompt templates & message handling
│   ├── message.py
│   ├── chatbot.py                    # CLI chatbot with running chat history
│   ├── chat_prompt_template.py
│   ├── message_placeholder.py
│   └── website.py                    # Streamlit "AI Website Builder"
│
├── Retriever/
│   ├── based_on_document_search/
│   │   ├── vector_store_retriever.py
│   │   └── wikipedia_retriever.py
│   └── based_on_retrievers/
│       ├── mmr.py                          # Max Marginal Relevance retriever
│       ├── multi_query_retriever.py
│       └── contextual_compression_retriever.py
│
├── Runnables/                        # Hand-built Runnable/Chain/PromptTemplate/LLM,
│   ├── dummy_prompt.py               # to understand what LangChain does internally
│   ├── dummy_llms.py
│   ├── dummy_chain.py
│   ├── app.py
│   ├── pdf_reader.py                 # RetrievalQA over a PDF using FAISS
│   └── simple.txt
│
├── Structured_Output/                # Getting structured data out of an LLM
│   ├── pydantic_demo.py              # Plain Pydantic model validation (no LLM)
│   ├── typeddict_output.py           # with_structured_output + TypedDict
│   └── pytandict_output.py           # with_structured_output + Pydantic
│
├── Text_Spliter/                     # Splitting documents into chunks
│   ├── lenght_based.py               # CharacterTextSplitter
│   ├── text_structured_based.py      # RecursiveCharacterTextSplitter
│   └── docs-text-splitter.py         # Splitting a loaded PDF
│
├── Tool-Calling/
│   └── first_tool_calling.py         # bind_tools + manual tool execution loop
│
├── Tools/
│   ├── custom_tools/
│   │   ├── my_first_custom_tool.py   # @tool decorator basics
│   │   ├── using_basetool.py         # BaseTool subclass
│   │   └── using_pydatic_tool.py     # StructuredTool.from_function
│   ├── Built_in_tools/
│   │   ├── duckduckgo_search_tool.py
│   │   └── shell_tool.py
│   └── Toolkit/
│       └── custom_toolkit.py         # Grouping tools into a toolkit
│
├── Vector_Store/                     # Embeddings + vector databases
│   ├── vectore_store_faiss.py
│   └── vectore_store_chroma.py
│
├── .gitignore
└── README.md
```

---

## 📖 Folder Guide

| Folder                  | What it covers                                                            |
| ------------------------ | -------------------------------------------------------------------------- |
| `Chains`                 | Composing `prompt \| model \| parser` pipelines — simple, sequential, parallel (`RunnableParallel`), and conditional (`RunnableBranch`) |
| `Documents_Loader`       | Loading raw content into LangChain `Document` objects from `.txt`, `.csv`, `.pdf`, and web pages |
| `Models/ChatModels`      | Talking to chat models directly — OpenAI and Google Gemini, including a Streamlit chatbot UI |
| `Prompts`                | `PromptTemplate`, `ChatPromptTemplate`, message types (`SystemMessage`/`HumanMessage`/`AIMessage`), and `MessagesPlaceholder` for chat history |
| `Retriever`              | Turning vector stores into retrievers — similarity search, MMR, multi-query, contextual compression, and Wikipedia as a retriever |
| `Runnables`              | A from-scratch mini implementation of a prompt template, LLM wrapper, and chain — for understanding what LangChain's `Runnable`/LCEL abstraction is really doing under the hood; also includes a full RAG example over a PDF |
| `Structured_Output`      | Getting typed/structured data back from an LLM using `TypedDict` and Pydantic with `with_structured_output` |
| `Text_Spliter`           | Breaking large documents into chunks with `CharacterTextSplitter` and `RecursiveCharacterTextSplitter` |
| `Tool-Calling`           | Binding tools to a chat model with `bind_tools` and manually running the tool-call → `ToolMessage` → final-answer loop |
| `Tools`                  | Three ways to define a tool (`@tool`, `StructuredTool`, `BaseTool`), plus built-in tools (DuckDuckGo, Shell) and grouping tools into a toolkit |
| `Vector_Store`           | Creating embeddings and storing them in FAISS and Chroma for semantic search |

---

## 🛠 Technologies Used

- Python
- [LangChain](https://python.langchain.com/) (`langchain-core`, `langchain-community`, `langchain-classic`, `langchain-text-splitters`)
- OpenAI (`langchain-openai`)
- Google Gemini (`langchain-google-genai`)
- FAISS (`langchain-community` vector store)
- Chroma (`langchain-chroma`, `chromadb`)
- Pydantic
- Streamlit
- python-dotenv

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/CodeWithDks/GenAi.git
cd GenAi
```

Create a virtual environment

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

Install the core dependencies used across these scripts:

```bash
pip install langchain langchain-openai langchain-community langchain-classic \
            langchain-google-genai langchain-chroma langchain-text-splitters \
            chromadb faiss-cpu pydantic python-dotenv streamlit \
            pypdf duckduckgo-search
```

> 💡 A pinned `requirements.txt` isn't checked into the repo yet — install the packages above, or generate one with `pip freeze > requirements.txt` once your environment is set up.

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

`OPENAI_API_KEY` is required for most scripts (chat models, embeddings, structured output). `GOOGLE_API_KEY` is only needed for `Models/ChatModels/gemini-chatbot.py`.

> ⚠️ Several scripts currently use hardcoded Windows file paths (e.g. `D:\Gen Ai\...`). Update these to relative paths or your own local paths before running them.

---

## ▶ Running Examples

Run any standalone script directly:

```bash
python Chains/simple_chain.py
python Retriever/based_on_retrievers/mmr.py
python Tool-Calling/first_tool_calling.py
```

Run the Streamlit apps:

```bash
streamlit run Prompts/website.py
streamlit run Models/ChatModels/gemini-chatbot.py
```

---

## 🎯 Learning Roadmap

- [x] LangChain installation & basics
- [x] Prompt templates & message types
- [x] A hand-built Runnable/Chain (understanding LCEL internals)
- [x] Chains (simple, sequential, parallel, conditional)
- [x] Document loaders & text splitters
- [x] Structured output (TypedDict & Pydantic)
- [x] Vector stores (FAISS, Chroma)
- [x] Retrievers (similarity, MMR, multi-query, contextual compression)
- [x] Retrieval-Augmented Generation (RAG)
- [x] Tools & toolkits
- [x] Tool calling with LLMs
- [ ] Memory
- [ ] Agents
- [ ] LangGraph
- [ ] Multi-agent systems
- [ ] End-to-end AI projects

---

## 📌 Repository Purpose

This repository exists to:

- Learn LangChain from the ground up, one concept at a time
- Practice core Generative AI building blocks before combining them into full apps
- Keep reusable, well-commented reference code for future projects
- Track learning progress toward building production-ready AI applications

---

## 🤝 Contributions

This is primarily a personal learning repository, but suggestions and improvements are always welcome — feel free to open an issue or PR.

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Acknowledgements

- [LangChain Documentation](https://python.langchain.com/)
- OpenAI
- Google Gemini
- FAISS & Chroma
- Python community