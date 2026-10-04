# 07 — Text Splitters

`06_Document_Loaders/` ended with a number: a 200-page handbook costs roughly 130,000 tokens *per
question* if you send the whole thing every time. The fix isn't sending less of the document — it's
sending only the few paragraphs that actually answer the question. Before you can retrieve the right
piece, you need pieces. That's what a text splitter makes.

## Notebook

| # | Notebook | What it covers |
|---|---|---|
| 1 | [`01_text_splitters.ipynb`](./01_text_splitters.ipynb) | `CharacterTextSplitter` (naive baseline), `RecursiveCharacterTextSplitter` with `chunk_size`/`chunk_overlap`, token-based vs. character-based sizing, `MarkdownHeaderTextSplitter`, language-aware code splitting, and semantic chunking. Capstone: implementing a lightweight version of Anthropic's contextual retrieval technique and measuring the improvement with cosine similarity |

## What the research actually says (and why this notebook leans on it)

This folder isn't just "here are the splitter classes." Current 2026 benchmarks (Vectara/NAACL,
Chroma, FloTorch) converge on specific, actionable numbers — chunking configuration affects
retrieval quality as much as the embedding model choice, 400–512 tokens with 10–20% overlap is the
practical default, and Anthropic's own contextual retrieval research found a 49% reduction in
retrieval failures (67% combined with reranking) from prepending a short context sentence to each
chunk before embedding it. The capstone doesn't just cite that last number — it implements a small
version of the technique and reproduces the effect on six chunks with cosine similarity, the same
measurement from `01_Models/02_embedding_models.ipynb`.

## A second sunset notice

`langchain_experimental` — home to `SemanticChunker`, used in Section 5 — is **also** sunset and
unmaintained, same situation as `langchain-community` in the previous folder. It still works (tested
against `langchain-experimental==0.3.4`), and semantic chunking is a concept worth knowing regardless
of which package eventually implements it. Treat Section 5 as a concept you understand, not a
dependency to build production code on without checking its status first.

## A QA note worth knowing

Testing this notebook's `from_tiktoken_encoder()` cell surfaced a real issue: tiktoken downloads its
encoding file from Microsoft's blob storage on first use, and that download is blocked on some
networks (it failed in the sandbox this notebook was built in). The cell now catches that failure and
falls back to the ~4-characters-per-token estimate used elsewhere in the notebook, with an explanation
of why — rather than a cell that just breaks with no context on some machines and not others.

## What you should be able to do after this folder

- Explain why `CharacterTextSplitter` cuts words in half and what `RecursiveCharacterTextSplitter`
  does differently to avoid it.
- Choose a `chunk_size` and `chunk_overlap` using the 2026 benchmark numbers as a starting point,
  not a guess.
- Explain why chunk size should sometimes be measured in tokens instead of characters, and what can
  go wrong with the tiktoken-based approach on a restricted network.
- Pick the right splitter for structured content — `MarkdownHeaderTextSplitter` for Markdown,
  language-aware splitting for source code — instead of defaulting to the generic recursive splitter
  for everything.
- Explain what semantic chunking trades off against recursive splitting, and why it's a targeted
  upgrade rather than a default.
- Explain, in your own words, why prepending context to a chunk before embedding it improves
  retrieval — and demonstrate it with a similarity-score comparison, not just a claim.

## Prerequisites

Same as earlier folders — see the [repo root README](../README.md). New for this notebook:

```bash
pip install langchain-text-splitters tiktoken
pip install "langchain-experimental==0.3.4"   # optional — Section 5 only, see the sunset note above
```

## Running

```bash
jupyter notebook 01_text_splitters.ipynb
```

## Next

[`08_Vector_Store/`](../08_Vector_Store) — these chunks need somewhere to live that supports fast
similarity search over thousands, or millions, of them — not the Python list used in this notebook's
cosine-similarity capstone.
