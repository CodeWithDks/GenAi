# 05 — Structured Output

`04_Chains/` used a minimal `PydanticOutputParser` just to make one `RunnableBranch` condition
reliable. This folder is the full treatment: every way LangChain turns a model's answer into
program-usable data instead of a paragraph you'd have to parse yourself.

## Notebook

| # | Notebook | What it covers |
|---|---|---|
| 1 | [`01_structured_output.ipynb`](./01_structured_output.ipynb) | A Pydantic primer, `with_structured_output()` with both `TypedDict` and `BaseModel`, a comparison table against `PydanticOutputParser`, nested models for structured lists, and `method="json_mode"`. Capstone: batch review analysis with real aggregate statistics computed in plain Python |

## Why this topic exists

Everything before this folder produced text. Text is fine for a human to read and useless for a
program to act on — `"sentiment was mostly negative"` isn't something you can write an `if`
statement against. This folder is the bridge: the point where a model's output stops being
something you print and starts being something your code can compute on.

## Why `with_structured_output()` before `PydanticOutputParser`

`04_Chains` already showed `PydanticOutputParser` — prompt-instruction-based, works with any model,
but relies on the model *following instructions* to format its output correctly. This folder leads
with `with_structured_output()` instead, because it's what you should reach for by default: most
providers implement it via native function/tool-calling, which means the *provider* enforces the
shape rather than hoping the model gets the formatting right. `PydanticOutputParser` stays in the
toolkit as the fallback for providers or models that don't support the native method — a deliberate
downgrade, not a first choice.

## What you should be able to do after this folder

- Explain, in one sentence, why `TypedDict` and Pydantic give you different guarantees even when
  the extracted data looks identical when printed.
- Choose `with_structured_output()` over `PydanticOutputParser` by default, and explain the one
  situation where you'd reach for the parser instead.
- Write a nested Pydantic schema (a list of sub-models inside a parent model) for an extraction
  task that isn't flat.
- Run `.batch()` across several inputs and compute a real aggregate statistic (a count, a
  percentage, a filtered list) on the structured results — not just print each one individually.

## Prerequisites

Same as earlier folders — see the [repo root README](../README.md). No new packages beyond
`pydantic`, already introduced in `04_Chains`.

## Running

```bash
jupyter notebook 01_structured_output.ipynb
```

## Next

[`06_Document_Loaders/`](../06_Document_Loaders) — a shift in direction: instead of shaping a
model's *output*, you start feeding it real external content (files, web pages, PDFs) as *input*.
This is where the retrieval-augmented half of the curriculum begins.
