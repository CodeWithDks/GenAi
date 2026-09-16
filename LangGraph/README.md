# LangGraph

Stateful, graph-based agent workflows — building on everything in
[`../LangChain/`](../LangChain/). Where LangChain composes a linear
`prompt | model | parser` pipeline, LangGraph models a workflow as a graph
of nodes and edges, with shared state that persists and evolves as
execution moves between them — which is what makes loops, branching,
human approval steps, and multi-agent coordination possible.

Each numbered folder is one concept, roughly in the order the ideas build
on each other: control flow first, then safety/architecture patterns, then
advanced multi-agent systems.

## Folders

| # | Folder | What it covers |
|---|---|---|
| 01 | [`Sequential_Workflows`](./01_Sequential_Workflows) | The simplest graph shape — nodes run one after another in a fixed order. Starting point for understanding LangGraph's state object and how nodes read/write it. |
| 02 | [`Conditional_Workflows`](./02_Conditional_Workflows) | Branching — the graph decides which node runs next based on the current state, instead of a fixed sequence. |
| 03 | [`Parallel_Workflows`](./03_Parallel_Workflows) | Multiple nodes running independently on the same input, with their results combined afterward. |
| 04 | [`Iterative`](./04_Iterative) | Loops — a node (or set of nodes) runs repeatedly until some condition is met, e.g. an optimizer that revises its own output, or a self-healing agent that retries after a failure. |
| 05 | [`Tool_Calling`](./05_Tool_Calling) | Agents that call external tools from within a graph — the LangGraph equivalent of LangChain's `bind_tools`, wired into a stateful flow. |
| 06 | [`Subgraphs`](./06_Subgraphs) | Composing a graph out of smaller graphs — with either isolated per-subgraph state (`Custom-State`) or state shared across the parent and its subgraphs (`Shared-State`). |
| 07 | [`Middleware`](./07_Middleware) | Code that runs around a tool call — observing it (logging) or actually gating it (blocking a specific tool outright before it executes). |
| 08 | [`HITL`](./08_HITL) | Human-in-the-loop — a graph that pauses mid-execution for a human decision (e.g. approve/reject) before continuing, using LangGraph's checkpointing to persist state across that pause. |
| 09 | [`Memory_Persistence`](./09_Memory_Persistence) | Giving an agent memory across turns/sessions using LangGraph checkpointers, rather than relying on the entire conversation being replayed every time. |
| 10 | [`Multiagent`](./10_Multiagent) | A supervisor agent coordinating multiple specialized agents (writer, reviewer, editor), routing between them based on shared state rather than a fixed pipeline. |
| 11 | [`Orchestrator`](./11_Orchestrator) | A higher-level orchestrator coordinating a full multi-step task (e.g. generating a research report) end to end. |

## Why this order

- **01–03** cover the three basic graph shapes — sequence, branch, and
  parallel — before anything gets more advanced.
- **04** introduces loops, which is where LangGraph starts to do things a
  plain LangChain chain can't.
- **05** brings tool-calling (already covered in LangChain) into a
  stateful graph context.
- **06–07** are architecture and safety concerns that matter once a graph
  is complex enough to need decomposing (subgraphs) or gating (middleware).
- **08–09** deal with the graph pausing or persisting across
  time — human approval, or memory across sessions.
- **10–11** are the payoff: multiple agents and a supervising layer
  coordinating a real multi-step task, built on every pattern above.

## Running an example

Each notebook is self-contained. Open it in Jupyter and run cell by cell,
or convert and run as a script:

```bash
jupyter notebook LangGraph/03_Parallel_Workflows/StartupScan.ipynb
```

Most notebooks expect an `OPENAI_API_KEY` in a local `.env` file in the
same folder — see each subfolder's own README where one exists
(`06_Subgraphs`, `07_Middleware`, `10_Multiagent`) for specifics, or the
[repo root README](../README.md) for general setup.

## Coming from LangChain?

Start at [`../LangChain/`](../LangChain/) first if you haven't — this
section assumes familiarity with prompts, chains, structured output, and
tool calling, and builds directly on top of those ideas rather than
re-explaining them.