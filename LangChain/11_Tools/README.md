# 11 — Tools

Every notebook so far did one thing: text in, text out. A **tool** is how a model gets to *do*
something — look up an order, run a calculation, search the web, hand a case to a human. This folder
is about building tools well, before the next folder (`12_Tool_Calling`) lets a model start using them.

## Notebook

| # | Notebook | What it covers |
|---|---|---|
| 1 | [`01_tools.ipynb`](./01_tools.ipynb) | The anatomy of a tool; the three ways to build one (`@tool`, `StructuredTool`, `BaseTool`) and when to pick each; `parse_docstring`; error handling with `ToolException`; async tools; what the model actually sees; `return_direct` and artifacts; the built-in `DuckDuckGoSearchResults` and `ShellTool` (with a safety section); `create_retriever_tool`; `BaseToolkit`. Capstone: a support-desk toolbox, exercised by a hand-written "dry run" of model tool calls |

## The mental model

A tool works like a restaurant. The **menu** is the tool's name, description and input schema. The
**customer** is the model: it reads the menu and places an order, but never cooks. The **kitchen** is
your Python function, which *your* code runs. Two consequences run through the whole notebook: the model
never executes your function, and the description you write matters as much as the code behind it.

## Things in your original scripts worth knowing about

None of these stopped your scripts from running; they are the kind of thing that bites later.

- **Import path.** `from langchain_community.tools import tool` works (it is the same object as the core
  one, re-exported), but it goes through the sunset `langchain-community` package. Use
  `from langchain_core.tools import tool`.
- **A return hint that doesn't match the return.** `multiply` was annotated `-> int` but returned an
  f-string. Python doesn't check this, so nothing complains; the notebook shows it.
- **A name that hides the decorator.** In `custom_toolkit.py`, `for tool in tools:` reuses the name `tool`,
  which shadows the imported `@tool` decorator. Harmless there, because the decorator had already been
  used, but a trap if you add a tool below that loop.
- **`Divide` raised a plain `ValueError`** with no error handling, so inside an agent a divide-by-zero would
  end the whole run. Section 6 shows `ToolException` and `handle_tool_error`.
- **`ShellTool` needs `langchain-experimental`.** It moved out of `langchain-community`, so
  `ShellTool()` raises an `ImportError` unless that package is installed. It also has no safeguards, and
  `ls` won't work on Windows (the command goes through `cmd.exe`; use `dir`).

## What was verified, and what wasn't

Verified by running it, against `langchain-core 1.6.7`: all 25 code cells execute without errors. The
specific behaviors the notebook states — the `parse_docstring` difference, `ValueError` escaping
`handle_tool_error` while `ToolException` doesn't, async-only tools refusing sync calls, `Literal`
becoming an allow-list, `ask_human_input` skipping a declined command — were each checked directly.

Not verified, because the build sandbox had no internet and ran Linux:

- **The web search itself.** `DuckDuckGoSearchResults` needs the `ddgs` package and a connection; the
  cell is written to skip cleanly without them, and that skip path is what was exercised.
- **Real retrieval quality in Section 11.** A stand-in embedding model was used, which doesn't understand
  meaning, so the retrieved text in the build run wasn't a meaningful answer. Run it with the real
  Hugging Face model and check that "how long do refunds take?" returns the refund-timing chunk.
- **`ShellTool` on Windows.** The `cmd.exe` behavior is inferred from `shell=True` in the library source,
  not tested on a Windows machine.

## What you should be able to do after this folder

- Name the four parts of a tool and say which one the model reads versus which one your code runs.
- Choose between `@tool`, `StructuredTool` and `BaseTool` for a given job, defaulting to
  `@tool(parse_docstring=True)`.
- Explain why a tool should turn expected failures into messages, and why a plain `ValueError` doesn't
  get that treatment by default.
- Explain why you wouldn't hand a model an unrestricted shell, and what a narrow tool with a `Literal`
  input looks like instead.
- Turn a retriever into a tool, and say what changes compared with always retrieving, as in
  `10_RAG_Project`.

## Prerequisites

Same as earlier folders; see the [repo root README](../README.md). Most of this notebook needs no API key.

```bash
pip install langchain-core pydantic
pip install langchain-huggingface sentence-transformers            # Section 11 only
pip install "langchain-community==0.4.2" ddgs "langchain-experimental==0.4.2"   # Section 10 only
```

## Running

```bash
jupyter notebook 01_tools.ipynb
```

## Next

[`12_Tool_Calling/`](../12_Tool_Calling) — everything here was the menu and the kitchen. Next the model
arrives: `bind_tools` lets it read the menu and write the tool calls you wrote by hand in this folder's
dry run, and you'll run the full loop yourself — call, execute, return the result, get the final answer.
