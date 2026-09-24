# 02 — Prompts

`01_Models/` hardcoded a `SystemMessage`/`HumanMessage` list. That's fine for a one-off script, but
breaks the moment you need the same conversation *shape* with different inputs. This folder covers
**prompt templates** — how you turn a hardcoded conversation into something reusable, parameterized,
and (once you scale up) cheaper to run.

## Notebook

| # | Notebook | What it covers |
|---|---|---|
| 1 | [`01_prompt_templates.ipynb`](./01_prompt_templates.ipynb) | `PromptTemplate` vs. `ChatPromptTemplate`, `MessagesPlaceholder` (including `optional=True` and `n_messages=` truncation), few-shot prompting, `.partial()`, prompt composition, and a production-grade section on the prompt-caching trap with Anthropic's tuple shorthand. Capstone: a support chatbot with consistent tone (few-shot) and bounded memory (`n_messages`) |

## Why this order, and why one notebook this time

`01_Models` split into two notebooks because chat models and embedding models are genuinely
different primitives — different input, different output, different mental model. Prompts aren't
that: everything here is one continuous idea (turning static messages into reusable templates), so
splitting it would have meant arbitrary breaks rather than real ones.

Inside the notebook, the order matters more than usual:

1. **`PromptTemplate` → `ChatPromptTemplate`** — see the plain-string version first so the
   chat-message version doesn't feel like magic; it's the same idea with a list of messages instead
   of one string.
2. **`MessagesPlaceholder`** — the piece that makes a template handle a *growing* conversation
   instead of a fixed one. This is the direct upgrade path from the manual chat-history list you
   built in `01_Models`.
3. **Few-shot prompting** — once you can template a conversation, the next real problem is
   *consistency* — description alone often isn't enough; examples usually are.
4. **`.partial()` and composition** — small conveniences, but the kind you'll use constantly once
   you're building more than one assistant that shares parts of a system prompt.
5. **Prompt caching (reference)** — placed last and marked as reference material because it needs
   an Anthropic key you don't have yet. Included anyway because it's a real production cost lever,
   and the failure mode (silently paying full price) is invisible unless you know to look for it.

## What you should be able to do after this folder

- Explain what `ChatPromptTemplate.from_messages([("system", ...), ...])` is actually shorthand for.
- Use `MessagesPlaceholder` to inject a variable-length chat history into a template, and cap it
  with `n_messages` so a long conversation doesn't silently inflate cost and context length.
- Write a few-shot prompt that locks in a tone or output format the system prompt alone couldn't
  reliably enforce.
- Explain why `("system", big_prompt)` defeats Claude's prompt caching, and what the fix looks like.
- Build a chatbot function that takes a query and a history list, and returns a reply — with the
  actual prompt logic living in one reusable template, not scattered through the function.

## Prerequisites

Same as `01_Models/` — see the [repo root README](../README.md) for install commands and `.env`
setup. This notebook uses Groq (free) for its live calls; no new packages beyond what `01_Models`
already installed.

## Running

```bash
jupyter notebook 01_prompt_templates.ipynb
```

## Next

[`03_Runnables/`](../03_Runnables) — this notebook piped `template | model` throughout without
explaining what that `|` operator actually does. Time to build a minimal version of LangChain's
Runnable interface from scratch, so the abstraction stops being a black box before you start
relying on it everywhere.