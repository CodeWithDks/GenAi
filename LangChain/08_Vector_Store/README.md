# 08 — Vector Store

`01_Models/02_embedding_models.ipynb` found the best-matching chunk by hand — a Python list, a
for-loop, `cosine_similarity` called once per chunk. Fine for 6 tickets, not fine for 60,000 of
them. A vector store is a database purpose-built to answer "which stored vectors are closest to
this one?" without scanning everything, and to keep that data around between runs instead of
re-embedding it every single time your app starts.

## Notebook

| # | Notebook | What it covers |
|---|---|---|
| 1 | [`01_vector_stores.ipynb`](./01_vector_stores.ipynb) | FAISS (in-memory, manual persistence, `similarity_search_with_score`) and Chroma (auto-persisting, first-class metadata filtering), a comparison table, incremental document adds, and the `.as_retriever()` bridge to the next notebook. Capstone: a knowledge base that survives a simulated restart with zero re-embedding |

## A real bug this notebook catches

Your original `vectore_store_chroma.py` calls `vectore_store.aadd_documents(text_splitted)` —
that's the **async** method, called without `await`. It doesn't raise an error; it silently returns
an unfinished coroutine and adds nothing to the collection. The notebook calls this out explicitly
in Section 2, right where the correct, synchronous `add_documents()` is introduced, because "my
collection count is 0 and nothing errored" is exactly the kind of bug that wastes an afternoon.

## Why this notebook was tested harder than most

Every code cell in this notebook was actually **executed** against real FAISS and Chroma instances
during development — not just checked for valid syntax. That's what caught the `aadd_documents` bug
above being worth flagging, and a second, unrelated bug in an early draft of the capstone: Chroma
rejects collection names under 3 characters, and `"kb"` was two characters short. Both were fixed
before you ever saw the notebook.

## Why FAISS and Chroma, and why Chroma by default

| | FAISS | Chroma |
|---|---|---|
| Persistence | Manual (`save_local` / `load_local`) | Automatic, as you add documents |
| Metadata filtering | Supported, less ergonomic | First-class — a `filter` dict on every search |
| Best for | Fast prototyping, research, read-mostly workloads | Apps with ongoing writes, filtering, multiple sessions |
| Package status | Lives in the unmaintained `langchain_community` (see `06_Document_Loaders`) | Actively maintained, own package |

The notebook leads with FAISS because it's the simpler mental model (a file, not a client/server
collection), then moves to Chroma and makes the case — with a real before/after filtered-search
comparison — for why Chroma is the better default once an app needs more than "store some vectors
and search them."

## What you should be able to do after this folder

- Explain why a vector store scales where a Python-list-plus-loop approach doesn't.
- Build, query, and persist both a FAISS index and a Chroma collection.
- Use Chroma's `filter` argument to narrow a search to a metadata subset (e.g. one department),
  and explain why that matters for result quality, not just convenience.
- Add new documents to an existing store without rebuilding it from scratch.
- Explain, concretely, what "persistence" buys you — that re-opening a store doesn't cost an
  embedding call for data that's already in it.

## Prerequisites

Same as earlier folders — see the [repo root README](../README.md). New for this notebook:

```bash
pip install langchain-chroma
pip install "langchain-community==0.4.2" faiss-cpu   # FAISS — see the sunset note in 06/07
```

## Running

```bash
jupyter notebook 01_vector_stores.ipynb
```

## Next

[`09_Retriever/`](../09_Retriever) — plain similarity search is the simplest way to query a vector
store, not the only one. MMR, multi-query expansion, and re-ranking all build directly on the
`chroma_store` and `faiss_store` created in this notebook.
