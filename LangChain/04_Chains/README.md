# 04 — Chains

`03_Runnables/` built the raw mechanics by hand. This folder uses those same pieces as **named,
recognized patterns** — simple, sequential, parallel, conditional — that you reach for directly
when designing a real pipeline, instead of assembling from primitives every time.

## Notebook

| # | Notebook | What it covers |
|---|---|---|
| 1 | [`01_chains.ipynb`](./01_chains.ipynb) | Simple chains (+ `get_graph().print_ascii()` as a debugging habit), sequential chains (output-as-input across prompts), parallel chains with a merge step, and conditional chains routed on a `PydanticOutputParser`-backed structured signal instead of raw text. Capstone: a study-guide generator (notes + quiz, merged, conditionally translated) |

## Why this doesn't just repeat 03_Runnables

The mechanics — `RunnableSequence`, `RunnableParallel`, `RunnableBranch` — don't change here. What
changes is the question you're asking. Last folder: *"what does `|` actually do?"* This folder:
*"given a real problem, which of these four shapes fits it?"* That's a design-judgment skill, not
a syntax one, and it only makes sense to practice once the syntax is no longer the hard part.

One deliberate addition worth calling out: routing a `RunnableBranch` on **raw model text**
("the language is definitely Hindi!") is fragile — model output isn't consistent enough to be a
safe `if` condition. The conditional-chain section fixes this with a minimal `PydanticOutputParser`,
explicitly flagged as a preview — full structured-output coverage is next, in `05_Structured_Output/`.
This is the right amount of new material for this folder: just enough to make branching reliable,
not a full parser deep-dive that would duplicate the next topic.

## What you should be able to do after this folder

- Look at a new problem and identify which of the four chain shapes (simple / sequential / parallel
  / conditional) fits it, before writing any code.
- Explain why a sequential chain's steps can't run out of order, while a parallel chain's branches
  genuinely can run at the same time.
- Merge the results of a `RunnableParallel` into one final output with a third prompt.
- Explain why routing a `RunnableBranch` on raw text output is risky, and what a structured parser
  fixes about that.
- Use `chain.get_graph().print_ascii()` to confirm a multi-step pipeline is wired the way you
  intended, before spending API calls debugging it blind.

## Prerequisites

Same as earlier folders — see the [repo root README](../README.md). This notebook adds `pydantic`
to the install list (used for the structured language-detection step); everything else is already
covered by `01_Models`' setup.

## Running

```bash
jupyter notebook 01_chains.ipynb
```

## Next

[`05_Structured_Output/`](../05_Structured_Output) — the `PydanticOutputParser` used here to make
one branch condition reliable gets the full treatment: every parser type, `TypedDict` vs. Pydantic,
when to use which, and the more modern `.with_structured_output()` method.