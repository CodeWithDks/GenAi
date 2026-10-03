# 06 — Document Loaders

Every notebook up to this point used text you typed directly into the notebook. Real applications
pull knowledge from PDFs, spreadsheets, web pages, and folders of files. A **document loader** goes
and gets that content and hands it back in one standard shape — a `Document`, with `page_content`
and `metadata` — so nothing downstream cares whether the text came from a PDF or a website.

This folder is also where the curriculum turns toward retrieval: `06` through `09` build the four
pieces a real RAG pipeline needs (load → split → embed → retrieve), and `10_RAG_Project` wires them
into one working app.

## Notebook

| # | Notebook | What it covers |
|---|---|---|
| 1 | [`01_document_loaders.ipynb`](./01_document_loaders.ipynb) | The `Document` object, `TextLoader`, `CSVLoader`, `PyPDFLoader`, `WebBaseLoader` (with `SoupStrainer` to strip navigation junk), `DirectoryLoader`, and `.lazy_load()` for large corpora. Capstone: a knowledge-base ingestion function, followed by a deliberate demonstration of the three walls that "just paste everything into the prompt" hits as data grows |

## A note on `langchain-community`

Anthropic's own research while building this notebook turned up something worth knowing:
**`langchain-community`, the package every loader in this notebook comes from, was sunset in May
2026** — frozen, unmaintained, repository archived. LangChain's direction going forward is one
package per provider (`langchain-openai`, `langchain-chroma`, and so on).

Nothing in the notebook is wrong because of this — every loader was tested and runs correctly
against `langchain-community==0.4.2`, and the *concepts* (a `Document`, metadata, lazy loading)
don't change regardless of which package implements them. But it's the reason the capstone wraps
every loader call inside one function (`ingest_knowledge_base`) instead of scattering
`from langchain_community...` imports through the rest of the codebase — if a loader needs to move
to a maintained standalone package later, there's exactly one place to change it.

## Why the "three walls" section exists

Your original loader scripts filtered a CSV with `"favorite season" in doc.page_content.lower()` —
plain keyword matching. That's a completely reasonable thing to try first, and the notebook doesn't
skip past it: it demonstrates the approach working, then demonstrates it failing the moment a
customer phrases the same question differently ("money back" vs. "refund"), then shows a model
succeeding anyway because it understands the *meaning*, then calculates what it costs to send an
entire knowledge base on every single question once that knowledge base is a real size. That
calculation is the actual reason `07_Text_Splitters` through `09_Retriever` exist — not "because
that's the next chapter," but because you just watched the alternative break.

## What you should be able to do after this folder

- Explain what a `Document` is and why every loader, regardless of source, returns the same shape.
- Choose the right loader for a `.txt` file, a `.csv` file, a PDF, and a web page — and know that
  `metadata["page"]` from a PDF loader is a zero-based index, not the number printed on the page.
- Use a `SoupStrainer` to keep a scraped web page from being mostly navigation and footer text.
- Explain when to reach for `.lazy_load()` instead of `.load()`.
- Explain, with a number attached, why sending an entire knowledge base as context on every question
  stops working once that knowledge base is bigger than a few pages.

## Prerequisites

Same as earlier folders — see the [repo root README](../README.md). New for this notebook:

```bash
pip install "langchain-community==0.4.2" pypdf beautifulsoup4
```

The version pin is deliberate — see the note above.

## Running

```bash
jupyter notebook 01_document_loaders.ipynb
```

The notebook creates its own `sample_docs/` folder on first run, so it works immediately with no
files to hunt down. Drop a real PDF into that folder before running the PDF section if you want to
see it work on something other than the generated sample.

## Next

[`07_Text_Splitters/`](../07_Text_Splitters) — a `Document` is often too large to embed or search
usefully. Learn how to cut it into chunks without cutting a sentence, or an idea, in half.
