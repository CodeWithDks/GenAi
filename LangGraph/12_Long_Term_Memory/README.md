Here is a complete, well-structured **`README.md`** file for your **`llm-long-term-memory`** project, following standard open-source documentation practices.

```markdown
# 🧠 LLM Long-Term Memory with LangGraph

A production-ready, multi-agent framework demonstrating **long-term memory persistence, CRUD operations, and constraint-aware decision making** using **LangGraph** and **LangChain**.

This project showcases how an AI assistant can recall user preferences, physical limitations, dietary restrictions, or learning goals across independent conversational sessions without needing them repeated in prompt inputs.

---

## 📸 Key Architecture


```

User Input (New Session)
│
▼
┌──────────────────┐
│ Memory Extraction│ ──► Extracts persistent facts (Injuries, Goals, Diet, etc.)
└─────────┬────────┘
│
▼
┌──────────────────┐
│ Long-Term Store  │ ──► Saves / Updates / Retrieves user profile namespace
└─────────┬────────┘
│
▼
┌──────────────────┐
│ Multi-Agent Graph│ ──► Planner + Safety Reviewer enforce memory constraints
└─────────┬────────┘
│
▼
Personalized Output (Constraint-Compliant)

```

---

## ✨ Key Features

- **Automated Memory Extraction:** Dynamically parses incoming conversational turns to extract long-term facts using Pydantic structured output.
- **Full Memory CRUD Operations:** Supports **C**reate, **R**ead, **U**pdate, and **D**elete for persistent state keys using `InMemoryStore`.
- **Multi-Agent Supervisor Pattern:** Routes workflow execution across specialized worker agents (`planner`, `safety_reviewer`, `final`).
- **Safety Boundaries & Circuit Breakers:** Bounded loop iterations (`MAX_REVISIONS = 3`) and recursion limit guards to eliminate infinite agent revision loops.
- **Cross-Session Persistence Simulation:** Retrieves namespace facts dynamically even when the user query contains zero explicit context.

---

## 🛠️ Real-World Example: AI Fitness & Health Coach ("Coach Flex")

In the provided implementation, the system acts as a personalized fitness coach:

1. **Session 1 (Stored Memory):** User reveals they have a **broken right knee** (cannot squat/jump) and follow a **strict lactose-free vegan diet**.
2. **Session 2 (New Request):** User asks: *"Give me a quick 20-minute leg workout and a post-workout recovery snack."*
3. **Execution Outcome:**
   - **Leg Workout:** Automatically excludes barbell squats and jumping plyometrics, selecting low-impact exercises (*Wall Sits*, *Glute Bridges*, *Seated Leg Extensions*).
   - **Recovery Snack:** Excludes dairy and animal products, proposing high-protein vegan options (*Chickpea Salad*, *Pea Protein Smoothie*, *Edamame*).

---

## 📂 Repository Structure


```

llm-long-term-memory/
│
├── learning_assistant.ipynb   # Complete step-by-step Jupyter Notebook
├── README.md                  # Project documentation
├── .env.example               # Environment variables template
└── requirements.txt           # Python dependencies

```

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR-USERNAME/llm-long-term-memory.git](https://github.com/YOUR-USERNAME/llm-long-term-memory.git)
cd llm-long-term-memory

```

### 2. Set Up Virtual Environment & Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt

```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here

```

### 4. Run the Notebook

Launch Jupyter Notebook and execute `learning_assistant.ipynb`:

```bash
jupyter notebook learning_assistant.ipynb

```

---

## 📦 Required Dependencies (`requirements.txt`)

```text
langchain-openai>=0.1.0
langgraph>=0.2.0
langchain-core>=0.2.0
pydantic>=2.0.0
python-dotenv>=1.0.0

```

---

## 🔒 Safety & Production Controls

| Feature | Implementation | Purpose |
| --- | --- | --- |
| **Revision Safety Limit** | `MAX_REVISIONS = 3` | Prevents endless loop execution between reviewer and planner agents. |
| **Token Capping** | `max_tokens = 500` | Limits generation length, reduces API costs, and accelerates responses. |
| **Recursion Circuit Breaker** | `config={"recursion_limit": 8}` | LangGraph graph-level execution protection against unforeseen state locks. |

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE&utm_source=gemini) file for details.

```

```