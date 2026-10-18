# 13 — Agents

In `12_Tool_Calling` you wrote the agent loop yourself: call the model, run its tool requests, feed the
results back, repeat — with a step limit, retries, error handling and an approval gate. An **agent** is
that same loop, packaged. This folder uses `create_agent`, shows that it *is* your loop, and shows which
of your protections it provides automatically and which it quietly doesn't.

## Notebook

| # | Notebook | What it covers |
|---|---|---|
| 1 | [`01_agents.ipynb`](./01_agents.ipynb) | `create_agent`; the two-node graph it builds; a table mapping each protection in your `12` loop to its agent equivalent; a scripted stand-in model so failures happen on demand; error handling, step limits, retries, approval gates (approve / reject / edit) and per-thread memory; and a capstone support agent assembled from all of it |

## The graph it builds

```
 __start__ ──► model ──── no tool calls ────► __end__
                 ▲  │
                 │  └── tool calls ──► tools ─┐
                 └──────────────────────────────┘
```

That is read straight from `agent.get_graph()`, and it is the loop from `12`.

## Findings worth knowing

Each was checked by running it, against `langchain 1.4.4` and `langgraph 1.2.14`. Several are the
opposite of what you'd assume.

- **The default step limit is effectively none.** LangGraph's default recursion limit is **10007**. An
  agent you don't cap can run for thousands of steps, and you pay for each model call. Set
  `ModelCallLimitMiddleware` or a `recursion_limit` yourself.
- **Mistakes by the model are handled; exceptions in your tool are not.** A missing argument or an
  unknown tool name becomes an error message the model reads and recovers from. A `ToolException` raised
  *inside your tool* — for example "no such order" — **crashes the whole run** unless you add
  `ToolErrorMiddleware` or `handle_tool_error=True`. Your hand-written loop handled both, so the agent is
  less forgiving out of the box.
- **An approval pause really pauses.** While waiting, the tool had not run. Rejecting carries the
  reviewer's reason back to the model. *Editing* runs the **reviewer's** arguments (in the test, the
  refund went to a different order than the model asked for), which is why the tool must still enforce
  its own rules.
- **Resuming needs one decision per paused action.** A mismatch raises `ValueError`. The capstone's
  `decide` helper counts the pending actions rather than assuming one.
- **Old tutorials use moved APIs.** `create_react_agent` still imports but is deprecated in favour of
  `create_agent`. `AgentExecutor` is no longer importable from `langchain.agents` and lives only in
  `langchain_classic.agents`.
- **A bug that was in my own test model:** returning the *same* `AIMessage` object twice makes the
  agent's history stop growing, because the second one looks like an update to the first. The notebook's
  `ScriptedModel` returns a fresh copy each time, with a comment explaining why.

## How this fits with your `LangGraph/` folder

`create_agent` builds a LangGraph graph, so this notebook is the bridge. Your existing folders go deeper
on exactly the pieces introduced here: `07_Middleware` (writing your own with `@wrap_tool_call`),
`08_HITL` (interrupts at the graph level), `09_Memory_Persistence` and `12_Long_Term_Memory` (checkpointers
and stores), and `13_Streaming`. The notebook doesn't re-teach those; it points at them.

## What was verified, and what wasn't

**Verified by running:** all 20 code cells execute without errors, and the behaviors above were each
observed directly. The agent, the middleware, the checkpointer and the approval flow in Sections 4–8 are
all real `create_agent` behavior, driven by a scripted model built inside the notebook.

**Not verified:** any real model's behavior. The build sandbox couldn't reach Groq, so the cells that call
`llama-3.3-70b-versatile` (Section 2 and the capstone conversations) ran against a rule-based stand-in.
That means no one has yet seen what the real model chooses to do on those questions, or whether it writes
valid tool calls reliably. Also not exercised: the `respond` decision that the approval prompt lists;
`SummarizationMiddleware`, `ModelFallbackMiddleware`, `PIIMiddleware`, `TodoListMiddleware` and
`ContextEditingMiddleware` (the notebook names them as present in the installed package, nothing more);
and `create_agent`'s `response_format`, `store` and `context_schema` parameters (named from its signature
only). Treat your first real run as the test.

## What you should be able to do after this folder

- Explain what `create_agent` builds, and relate each part of it to the loop you wrote in `12`.
- Say which protections an agent gives you by default (bad arguments, unknown tools) and which you must
  add (tool exceptions, step limits, retries, approvals, memory).
- Explain why leaving the default recursion limit alone is a cost risk.
- Pause an agent for approval, then approve, reject or edit the pending action, and explain why an edit
  makes it even more important that the tool enforces its own rules.
- Explain what a `thread_id` is and why two threads don't share history.
- Choose between a hand-written loop, `create_agent`, and a full LangGraph graph.

## Prerequisites

Same as earlier folders; see the [repo root README](../README.md). You need `GROQ_API_KEY` in your `.env`.

```bash
pip install -U langchain langgraph langchain-groq python-dotenv
```

`create_agent` needs `langchain` 1.x, so the `-U` matters if you have an older install.

## Running

```bash
jupyter notebook 01_agents.ipynb
```

Sections 4–8 are fully offline. The live cells are Section 2 and the capstone conversations.

## Next

Your `LangGraph/` folders pick up exactly here. Back in `LangChain/`, `14_Error_Handling` covers the
non-agent equivalents: retrying and falling back around any ordinary chain.
