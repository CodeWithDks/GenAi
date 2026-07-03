# 🚀 Learning Generative AI using LangChain

This repository contains my hands-on learning journey in **Generative AI** using **LangChain**. It includes practical examples, experiments, and mini-projects covering the core concepts required to build AI-powered applications.

The goal of this repository is to understand how Large Language Models (LLMs) work with LangChain and how to build applications such as chatbots, document question answering systems, Retrieval-Augmented Generation (RAG), and structured output pipelines.

---

## 📚 Topics Covered

- Prompt Engineering
- LLM Models
- LangChain Basics
- Prompt Templates
- Output Parsers
- Chains
- Runnables
- Document Loaders
- Text Splitters
- Embedding Models
- Vector Databases (FAISS)
- Retrieval-Augmented Generation (RAG)
- Structured Output
- Environment Variables
- Building AI Applications

---

## 📂 Project Structure

```
.
├── Chains/
├── Documents_Loader/
├── faiss_index/
├── Models/
├── Prompts/
├── Rag/
├── Runnables/
├── Structured_Output/
├── Text_Splitter/
├── .env
├── .gitignore
├── pdf_reader.py
├── dummy_llms.py
├── dummy_prompt.py
├── requirements.txt
├── study_guide.md
├── test.py
└── README.md
```

---

## 📖 Folder Description

| Folder | Description |
|---------|-------------|
| Chains | Learning different types of LangChain chains |
| Documents_Loader | Loading documents like PDF, TXT, DOCX, etc. |
| Models | Working with different LLM providers |
| Prompts | Prompt Templates and Prompt Engineering |
| Rag | Retrieval-Augmented Generation examples |
| Runnables | LangChain Runnable Interface examples |
| Structured_Output | Returning structured responses from LLMs |
| Text_Splitter | Splitting large documents into chunks |
| faiss_index | FAISS vector database for semantic search |

---

## 🛠 Technologies Used

- Python
- LangChain
- OpenAI
- FAISS
- Hugging Face
- Pydantic
- Python-dotenv

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git
```

Move into the project directory

```bash
cd <repository-name>
```

Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

Example

```env
OPENAI_API_KEY=your_api_key_here
```

Depending on the examples, additional API keys may be required.

---

## ▶ Running Examples

Run any Python file

```bash
python filename.py
```

Example

```bash
python pdf_reader.py
```

---

## 🎯 Learning Roadmap

- [x] LangChain Installation
- [x] Prompt Templates
- [x] Dummy LLM
- [x] Chains
- [ ] Output Parsers
- [ ] Memory
- [ ] Agents
- [ ] Tools
- [ ] Embedding Models
- [ ] Vector Databases
- [ ] RAG
- [ ] Chatbots
- [ ] LangGraph
- [ ] Multi-Agent Systems
- [ ] AI Projects

---

## 📌 Repository Purpose

This repository is created for:

- Learning LangChain from scratch
- Practicing Generative AI concepts
- Building production-ready AI applications
- Maintaining notes and reusable code examples
- Tracking my learning progress

---

## 🤝 Contributions

This repository is primarily for learning purposes. Suggestions and improvements are always welcome.

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Acknowledgements

- LangChain Documentation
- OpenAI
- Hugging Face
- FAISS
- Python Community