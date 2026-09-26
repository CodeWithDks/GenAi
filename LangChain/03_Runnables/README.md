# 03 — Runnables (LCEL, from the ground up)

Every notebook so far has quietly used `prompt | model`. This folder exists for one reason: to
stop that `|` from being magic before you start relying on it everywhere. You build a minimal
version of LangChain's Runnable protocol yourself, then use the real thing.

## Notebook

| # | Notebook | What it covers |
|---|---|---|
| 1 | [`01_runnables_from_scratch.ipynb`](./01_runnables_from_scratch.ipynb) | A hand-built `MiniRunnable`/`MiniRunnableSequence` showing exactly what `__or__` does, then the real `RunnableLambda`, `RunnableSequence`, `RunnableParallel`, `RunnablePassthrough`, and `RunnableBranch`. Capstone: a support-ticket triage pipeline combining all five |

## Why build it from scratch first

It would be faster to just list the five Runnable types and show one example each. That's also how
you end up able to use LangChain but not really understand it — the moment something doesn't work
the way the docs implied, there's no mental model to fall back on.

Building `MiniRunnable` first means the rest of the notebook isn't "here are five new classes to
memorize" — it's "here's the same one idea (a class with `invoke()`, chainable via `|`) showing up
five times with different shapes." `RunnableParallel` isn't a new concept; it's a Runnable whose
`invoke()` happens to run several other Runnables concurrently instead of one after another.
`RunnableBranch` isn't a new concept either; it's a Runnable whose `invoke()` picks which child
Runnable to call based on a condition. Once that clicks, the whole Runnable ecosystem stops being
a list of API surface to memorize.

## What you should be able to do after this folder

- Explain, without looking it up, what Python actually does when it evaluates `a | b` on two
  Runnables, and why that's what makes `prompt | model | parser` work at all.
- Choose `RunnableParallel` over a sequential chain when two steps don't depend on each other's
  output, and explain why that's faster, not just different.
- Explain what problem `RunnablePassthrough.assign()` solves — specifically, why a plain
  `RunnableSequence` loses the original input by the time it reaches a later step.
- Build a `RunnableBranch` that routes different inputs to different sub-chains based on a
  condition, with a required default.
- Call `.batch()` and `.stream()` on a multi-step chain, not just a raw model call, and explain why
  that works for free once every step speaks the same interface.

## Prerequisites

Same as `01_Models/` and `02_Prompts/` — see the [repo root README](../README.md). This notebook
uses Groq (free) for its live calls; no new packages beyond what earlier folders already installed.

## Running

```bash
jupyter notebook 01_runnables_from_scratch.ipynb
```

## Next

[`04_Chains/`](../04_Chains) — the same sequential/parallel/conditional patterns from this folder,
now as first-class LangChain concepts you reach for directly, instead of assembling from Runnable
primitives every time.