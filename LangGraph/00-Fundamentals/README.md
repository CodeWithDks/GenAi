# 00 — Foundations

LangChain runs steps in a line. LangGraph describes a workflow as a **graph**, so it can branch, loop, run
things in parallel, pause for a human and remember. This folder teaches the vocabulary and the mechanics that
every later `LangGraph/` folder relies on: **state, nodes, edges, reducers, messages, schemas and runtime
context**. Read it first.

## Notebooks

| # | Notebook | What it covers | Capstone |
|---|---|---|---|
| 1 | [`01_state_nodes_edges.ipynb`](./01_state_nodes_edges.ipynb) | The whiteboard model; state, nodes, edges, `compile`, `invoke`; watching a run with `stream`; `add_sequence`; reading a graph; **super-steps** and parallel branches; joining branches safely; seven common mistakes, shown on purpose | A support-ticket intake pipeline (language, priority and queue checks in parallel, then a deadline) |
| 2 | [`02_reducers_and_messages.ipynb`](./02_reducers_and_messages.ipynb) | What happens when a field is written more than once; overwrite vs `operator.add` vs custom reducers; parallel writes and the conflict error; `add_messages`, `MessagesState`, `RemoveMessage`; two ways to trim a long chat | A support chatbot whose memory stays bounded (with a built-in stand-in model, so no key is needed) |
| 3 | [`03_schemas_validation_and_context.ipynb`](./03_schemas_validation_and_context.ipynb) | `TypedDict` vs dataclass vs Pydantic state and what each really validates; `output_schema`; node arguments (`config`, `runtime`); runtime context with `context_schema` | A "Ticket API": validated input, private internals, and a different tone and deadline table per customer |

## Why this order

1. **Part 1** builds the mental model with nothing that can collide: each node writes its own field. You see
   the whole cycle (declare, wire, compile, run, inspect) before anything gets subtle.
2. **Part 2** introduces the first real subtlety: two writers, one field. That is the moment a graph stops
   being a pipeline, and it is the foundation for every parallel and looping pattern later.
3. **Part 3** is about design: choosing what your state *is*, who may see it, and where settings go. It
   comes last because those choices only make sense once you know how state behaves.

## Findings worth knowing

Everything below was observed by running it on `langgraph 1.2.17`, and most of it is **silent**, which is why
it's worth knowing.

- **A node must return its changes.** Modifying the state in place does nothing.
- **A misspelled key in a node's return is dropped without an error**, with `TypedDict` and with Pydantic.
- **Compile catches some wiring mistakes and misses others.** A missing `START` edge or an edge to an unknown
  node raises `ValueError`. An orphan node, or a missing edge to `END`, compiles quietly.
- **A join can run twice.** When one parallel branch is longer than the other, separate `add_edge` calls make
  the join node run once per arrival. The list form `add_edge([...], "node")` waits for all of them.
- **Parallel writes to one field without a reducer fail loudly** with `InvalidUpdateError`, and the message
  tells you the fix.
- **Reducers also run on the starting value**, where `old` is the empty value of the type (`''`, `0`, `[]`,
  `{}`). A first draft of notebook 2 had a reducer that crashed on `''`, so the notebook now teaches this
  directly.
- **Only a Pydantic *state* rejects bad input**, and only on the way in. Values nodes write aren't checked,
  and a Pydantic `input_schema` alone did not validate.
- **Count-based chat trimming can leave the history starting with an AI reply.** Notebook 2 handles it.
- **Older tutorials use APIs that have moved:** `MessageGraph` and `config_schema` are deprecated since
  LangGraph 1.0 (use `StateGraph` with `messages`, and `context_schema`), and `create_react_agent` is deprecated
  in favour of `langchain.agents.create_agent`.

## What was verified, and what wasn't

**Verified by running:** every code cell of all three notebooks executes, including the assertions that pin
the lesson's expected results. They ran against **five LangGraph releases: 1.0.0, 1.1.0, 1.2.0, 1.2.17 and
1.2.19** (the newest available when written), not just the newest. Everything outside the chatbot capstone is
fully deterministic and needs no API key.

**Not verified:**
- **A real model in notebook 2's capstone.** It was run with the built-in `LLM=fake` stand-in. I confirmed that
  `init_chat_model` builds a `ChatOpenAI` for `openai:...` and a `ChatGroq` for `groq:...` and that a missing key
  gives a clear error, but I made no live call. Model names change fast (Groq shut down several in August
  2026), so if you get a `404 model_not_found`, pick a current name and set `LLM`.
- **Whether `openai:gpt-4o-mini`, the default, is still available on your account.** One setting, `LLM`, fixes
  it.
- **How `context_schema` behaves with subgraphs and checkpointers.** Those belong to later folders and will be
  checked when they're written.

## What you should be able to do after this folder

- Explain state, nodes, edges and compile using the whiteboard model, and draw the graph you built.
- Say what a super-step is, and predict which nodes run together.
- Wire a join correctly, and explain why separate edges can run a node twice.
- Choose a reducer for a field and explain what happens without one.
- Explain what a reducer receives the first time it runs.
- Manage a chat's messages with `MessagesState`, and keep its length bounded safely.
- Choose between `TypedDict`, dataclass and Pydantic state, and say exactly what each validates.
- Expose a public result while keeping working fields private, and pass settings through runtime context
  instead of state.

## Prerequisites

Python 3.10 or newer (required by LangGraph).

```bash
pip install -U langgraph pydantic python-dotenv langchain
pip install grandalf            # optional: text-art drawing in notebook 1
pip install langchain-openai    # for the default LLM=openai:...   (notebook 2 capstone, real model)
pip install langchain-groq      # or this, for LLM=groq:...
```

Notebooks 1 and 3 need no key. For notebook 2's capstone, add one of these to a `.env` file in the repo root:

```
LLM=openai:gpt-4o-mini          # needs OPENAI_API_KEY
# LLM=groq:openai/gpt-oss-120b  # free; needs GROQ_API_KEY
# LLM=fake                      # no key: a built-in stand-in replies with fixed text
```

## Running

```bash
jupyter notebook 01_state_nodes_edges.ipynb
```

Run each notebook top to bottom, in order.

## Next

[`01_Sequential_Workflows/`](../01_Sequential_Workflows): the first of the workflow patterns, now with all of
this vocabulary in place.
