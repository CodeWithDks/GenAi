# Sequential Workflows

The simplest possible LangGraph shape: a fixed chain of nodes, each
running exactly once, in a fixed order — `START → node → node → END`,
with no branching, no loops, no conditions. This is the starting point
for understanding LangGraph's core idea (a typed, shared **state** object
that nodes read from and write back to) before anything more advanced
gets layered on top of it.

## `bmi_workflow.ipynb` — BMI Calculator

A two-node graph with no LLM involved at all — deliberately, so the
graph mechanics are the only thing being demonstrated:

```
START → calculate_bmi → label_bmi → END
```

- **State** (`BMIState`): `weight_kg`, `height_m`, `bmi`, `category`
- **`calculate_bmi`** — computes BMI from weight and height, writes it
  back into state
- **`label_bmi`** — reads the computed BMI and classifies it
  (Underweight / Normal / Overweight / Obese)

Each node takes the *whole* state dict in, and returns the *whole* state
dict back out — a plain Python function, no decorators, no magic. That's
the entire mental model this notebook is teaching: a node is a function
`(state) -> state`, and the graph just decides the order they run in.

## `simle_chat_workflow.ipynb` — Minimal Chat Node

A one-node graph that wraps a single LLM call:

```
START → chat → END
```

- **State** (`ChatState`): `question`, `answer`
- **`chat`** — takes `question` from state, calls `ChatOpenAI`, writes
  the response into `answer`

This is the smallest possible graph that still does something useful —
the point isn't the chat itself, it's seeing that an LLM call is just
another node like `calculate_bmi` was: read from state, do work, write
back to state. Everything more complex later (conditional routing,
parallel branches, multi-agent supervisors) is this same pattern,
repeated and combined.

## Running either notebook

```bash
pip install langgraph langchain-openai python-dotenv
```

`simle_chat_workflow.ipynb` needs a `.env` file in this folder:

```
OPENAI_API_KEY=your_key_here
```

`bmi_workflow.ipynb` needs no API key — it's pure Python logic wrapped
in a graph, useful for seeing LangGraph's structure without an LLM call
in the way.

Both notebooks end with a Mermaid graph visualization
(`workflow.get_graph().draw_mermaid_png()`) — a good habit to keep for
any graph you build, since seeing the shape of a workflow makes it much
easier to reason about than reading the `add_node`/`add_edge` calls alone.