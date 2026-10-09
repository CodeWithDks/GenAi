# 09 — Retriever

`08_Vector_Store/` ended with `.as_retriever()` — the bridge from "a store I can search" into "a
`Runnable` that fits in a chain." Plain similarity search, the default behind that bridge, is the
simplest way to query a vector store. It isn't the only way, and for several real failure modes,
not the best one. This folder covers the retrieval strategies that actually fix those failures.

This closes out the retrieval arc that started in `06_Document_Loaders` — load, split, store,
retrieve. `10_RAG_Project` wires all four into one working app.

## Notebook

| # | Notebook | What it covers |
|---|---|---|
| 1 | [`01_retrievers.ipynb`](./01_retrievers.ipynb) | MMR, `MultiQueryRetriever`, `EnsembleRetriever` (hybrid vector + BM25 search), `ContextualCompressionRetriever`, and `ParentDocumentRetriever`, each framed around the specific failure it fixes, with an honest cost comparison. Capstone: a tuned hybrid-search support retriever feeding a real answer chain |

## A real migration worth knowing about

In LangChain's 1.0 restructure, `MultiQueryRetriever`, `EnsembleRetriever`,
`ContextualCompressionRetriever`, and `ParentDocumentRetriever` all moved out of core LangChain into
a separate `langchain-classic` package — imported from `langchain_classic.retrievers` instead of
the old `langchain.retrievers`. "Classic" here means "pre-1.0 API, still fully supported," not
"deprecated." Every import in this notebook was checked against the actual installed package before
being written — this isn't guessed from older tutorials, several of which are now wrong about this
exact thing. `BM25Retriever` is the odd one out: it stayed in `langchain_community` (the sunset
package from `06_Document_Loaders`) rather than moving to `langchain-classic`.

## Why five retrieval strategies, framed as "which failure does this fix"

It would be easy to turn this into a list of five classes with one example each. Instead, every
section opens with a specific way plain similarity search falls short — near-duplicate results,
narrow phrasing, missed exact terms, noisy chunks, context-starved small chunks — and introduces the
retriever that fixes *that specific thing*. The comparison table at the end is deliberately blunt
about cost: two of these five techniques make an extra LLM call (one of them *per retrieved
document*), and the right default is "start with MMR, which is free, and add the others only once
your own failure analysis justifies the cost" — not "use all five because they exist."

## What you should be able to do after this folder

- Explain what MMR optimizes for that plain similarity search doesn't, and why that matters for
  broad or generic queries.
- Identify when a retrieval failure is a *phrasing* problem (fixed by `MultiQueryRetriever`) versus
  an *exact-term* problem (fixed by `EnsembleRetriever`/BM25) — they look similar from the outside
  and have different fixes.
- Explain the specific cost `ContextualCompressionRetriever` adds, and decide whether a given use
  case justifies it.
- Explain what `ParentDocumentRetriever` solves about the small-chunk-vs-context tension from
  `07_Text_Splitters`.
- Look at a retrieval problem and pick the cheapest technique that actually fixes it, instead of
  reaching for the most sophisticated one by default.

## Prerequisites

Same as earlier folders — see the [repo root README](../README.md). New for this notebook:

```bash
pip install langchain-classic rank_bm25
```

## Running

```bash
jupyter notebook 01_retrievers.ipynb
```

## Next

[`10_RAG_Project/`](../10_RAG_Project) — every piece from `06` through this notebook, wired into one
real, working "chat with your documents" application with conversational memory.
