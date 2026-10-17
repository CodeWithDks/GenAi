# 12 — Tool Calling

In `11_Tools` you built the menu and the kitchen, then played the model by hand. This folder is where
the real model arrives and the loop connects everything: the model *asks* for a tool, your code *runs*
it, the result goes back, and the model either asks again or answers. An agent (`13_Agents`) is that
loop, packaged. Writing it yourself first means the agent won't be a black box.

## Notebook

| # | Notebook | What it covers |
|---|---|---|
| 1 | [`01_tool_calling.ipynb`](./01_tool_calling.ipynb) | `bind_tools` and reading an `AIMessage`'s `tool_calls`; one full round by hand; parallel calls; a hardened multi-round loop (max steps, errors as messages, retries, a default-deny approval gate); a scripted stand-in model that reproduces failures on demand; streaming tool calls; `tool_choice`; guardrails. Capstone: a support assistant whose refund tool enforces the rules itself |

## The loop

```
Human message → MODEL (tools bound) → AI message with tool_calls
                                            ↓  your code runs each tool
                                      Tool messages (one per call, same id)
                                            ↓
                                      MODEL again → more tool calls, or the final answer
```

## What your original script did, and what this adds

Your `first_tool_calling.py` is a correct single round: bind, ask, run the requested tool, send the
`ToolMessage` back, get the answer. Three things to know about it:

- **`ChatOpenAI()` named no model**, so which model ran depended on whatever default your installed
  version picks. The notebook always names the model.
- **It handles exactly one round.** "Add 20 and 20, then multiply the result by 3" needs a second round
  because the second call depends on the first answer. That is what the loop is for.
- **It assumes nothing goes wrong.** No unknown tool names, bad arguments, or runaway loops. The
  notebook's loop handles each, and its scripted stand-in model lets you watch it do so.

## Findings worth knowing

These were checked while building the notebook, and each one is a silent failure rather than a loud one.

- **A malformed tool call can look like "the model finished."** With `.invoke`, unparseable arguments land
  in `invalid_tool_calls` and `tool_calls` comes back **empty**. The obvious loop condition
  (`if not ai.tool_calls`) then returns a blank answer with no error.
- **A truncated *streamed* call can look valid.** `{"a": 20, "b": ` is repaired into `{"a": 20}` — a
  plausible call missing an argument, with nothing flagged. Act only after the stream ends, and let your
  tools validate their inputs: here the tool's own validation caught it.
- **`bind_tools` options differ by provider.** Read from the installed packages: `ChatGroq` takes a tool
  name, `"auto"`, `"any"` (sent to Groq as `"required"`) or a dict; `ChatOpenAI` adds `"none"`,
  `"required"`, `strict` and `parallel_tool_calls`.
- **Groq can reject a bad tool call with `400 tool_use_failed`.** The reports (forum threads and issue
  trackers, not an official Groq statement) say it is most common on `llama-3.1-8b-instant` and Llama 4
  models and least common on `llama-3.3-70b-versatile`, which is the model the notebook uses.

## What was verified, and what wasn't

**Verified by running:** all 22 code cells execute without errors. The in-notebook failure demos
(a provider error then success, unparseable arguments, an unknown tool, a missing argument, a runaway
model hitting `max_steps`) behave as described. The approval gate declines by default and the declined
refund never reaches the `REFUNDED` list. The refund tool refuses an out-of-window order when called
directly, with no model involved. `tool_choice` binding was tested against the real `ChatGroq` class.

**Not verified: any real model's behavior.** The build sandbox couldn't reach Groq, so the live cells ran
against a rule-based stand-in. That means nobody has yet seen, in this notebook, what
`llama-3.3-70b-versatile` actually chooses on these questions; whether it writes valid calls reliably
(that claim rests on community reports, not on a test I ran); whether Groq honors `tool_choice="none"`;
or how the live streaming cell behaves. Treat your first real run as the test, and expect model wording
and tool choices to vary.

## What you should be able to do after this folder

- Describe the call → execute → return → answer loop and write it without looking.
- Explain why every tool call needs its own `ToolMessage` with a matching `tool_call_id`.
- Name the two ways a malformed tool call shows up, and why the naive loop condition misses one.
- Explain why `max_steps` exists, and why a forced `tool_choice` inside a loop defeats the loop.
- Explain why business rules belong inside the tool, not just in the prompt, and what default-deny
  means for an approval gate.

## Prerequisites

Same as earlier folders; see the [repo root README](../README.md). You need `GROQ_API_KEY` in your `.env`.

```bash
pip install langchain-core langchain-groq python-dotenv pydantic
pip install langchain-openai    # optional, only to swap in OpenAI
```

## Running

```bash
jupyter notebook 01_tool_calling.ipynb
```

Run it top to bottom. Sections 4 and 5 run offline; the live cells are the ones that call `llm_with_tools`
or `support_llm`.

## Next

[`13_Agents/`](../13_Agents) — you now know what an agent does on every turn. The next notebook hands
the loop to LangChain's agent runtime and looks at what you gain and what you give up.
