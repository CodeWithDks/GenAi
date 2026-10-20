# 14 — Error Handling & Resilience

Everything before this folder assumed the happy path. Real systems meet rate limits, provider outages,
answers that don't match your schema, and tools that fail halfway. The goal isn't to prevent failure; it
is to **fail gracefully, cheaply, and visibly**: recover when recovery is possible, give up fast when it
isn't, and never hide what happened. This is the last notebook in the LangChain track.

## Notebook

| # | Notebook | What it covers |
|---|---|---|
| 1 | [`01_error_handling.ipynb`](./01_error_handling.ipynb) | Which failures deserve a retry; `.with_retry()` and its three traps; `.with_fallbacks()` (order, `exceptions_to_handle`, `exception_key`, retry-vs-fallback ordering, logging fallbacks); `InMemoryRateLimiter`; batch failures and `max_concurrency`; unparseable model output (`include_raw`, `OutputFixingParser`); idempotency for side effects; `ModelFallbackMiddleware` in an agent. Capstone: a ticket-triage pipeline with retry, fallback, and per-item failure handling |

## How the notebook is tested: a fake provider you control

Almost nothing here can be demonstrated against a real provider, because you can't make Groq fail on
cue. So the notebook puts the **real `ChatGroq` client** on top of a fake HTTP server (`FakeServer`) that
you script to return `429`, `500`, `401`, malformed answers and so on, and it **counts every request**.
That means the retry logic, exceptions and request counts are the real library's behavior; only the
server is simulated. It also means the whole notebook runs offline with no API key, and you can reproduce
every number below yourself.

## Findings worth knowing

Each was measured by running it (`langchain-core 1.6.7`, `langchain-groq 1.1.3`, `langchain 1.4.4`).

- **`.with_retry()` retries every exception by default**, including a wrong API key, which can never
  succeed. Narrow it with `retry_if_exception_type`, ideally a function that looks at the HTTP status.
- **The model client already retries.** `ChatGroq` defaults to `max_retries=2`, retrying `429` and `5xx` but
  not `400`/`401`. Stack `.with_retry(3)` on top and one failing call made **9 HTTP requests**, not 3. Pick
  one layer, or set the client's `max_retries=0`.
- **`wait_exponential_jitter=False` means no waiting at all.** Four attempts took 0.01 seconds. It is not
  "plain backoff", and against a rate-limited API it is a retry stampede. The notebook uses it in demos
  only for speed and says so each time.
- **Order matters when you compose:** retry-then-fallback exhausts the primary's retries before using the
  backup; fallback-then-retry switches immediately.
- **Retrying a bad answer only helps if the answer can change.** A model that repeats the same invalid
  output just costs you three calls. `OutputFixingParser` instead shows the model its own mistake.
- **Never retry a side effect blindly.** A timeout *after* a refund succeeded makes a naive retry refund
  twice. The fix is an idempotent operation (the `issue_refund` tool in `12` and `13` already is one).
- **`.with_retry()` + `.batch()` is order-dependent, and can destroy good results.** This one surfaced
  because an assertion in the capstone failed. In a batch, the retry decision is made from the *first*
  exception in input order. If it isn't retryable, nothing is retried and **every slot** — including items
  that succeeded — is overwritten with that one exception (mechanism read from `RunnableRetry._batch`). If
  it is retryable, items with *non*-retryable errors are retried too. The fix is to batch over a plain
  wrapper that retries one item at a time. `.with_fallbacks().batch()` does not have this problem.
- **It can be silent.** In the first version of the capstone, with the garbage ticket first, the answers
  looked identical, but the rate-limited tickets were never retried, so *every* ticket was answered by the
  backup (6 backup requests instead of 3). Only the request counts exposed it, which is why the notebook
  counts requests, and ends by running the pipeline forwards and backwards and asserting identical results.

## What was verified, and what wasn't

**Verified by running:** all 28 code cells execute without errors, and every number above was observed.
The final capstone counts (8 primary requests, 3 backup, 3 fallbacks, 1 failure) are pinned by an assertion
and identical in both ticket orders.

**Not verified:**
- **Any real provider.** The sandbox had no network. Real servers choose their own `Retry-After` timing,
  error bodies and failure patterns; the fake server sends a tiny `retry-after-ms` so demos run fast.
- **Timeouts.** `ChatGroq` has a `request_timeout` setting, but timeout behavior isn't exercised anywhere
  in the notebook.
- **The Gemini/OpenAI fallback snippet** after the capstone is shown but not run (it needs live keys).
- **`OutputFixingParser` with a real model.** The demo's "fixer" is a stand-in that always returns a
  corrected answer, so it shows the mechanism, not how well a real model repairs bad output.
- **`InMemoryRateLimiter` across processes.** It lives in one process's memory; that is by design, and not
  something the notebook tests.

## What you should be able to do after this folder

- Sort a failure into transient, permanent, bad-output, or your-own-bug, and say which are worth retrying.
- Explain why `.with_retry()` on top of a model client can multiply requests, and how to avoid it.
- Choose between retry-then-fallback and fallback-then-retry for a rate limit versus an outage.
- Explain why a fallback must be logged, and what a silently-used fallback costs.
- Explain why `.with_retry()` and `.batch()` need a per-item wrapper, and how request counts reveal the
  problem when results look fine.
- Make a side-effecting operation safe to retry.

## Prerequisites

Same as earlier folders; see the [repo root README](../README.md). No API key is needed for this notebook.

```bash
pip install -U langchain langchain-core langchain-groq langchain-classic python-dotenv pydantic
```

## Running

```bash
jupyter notebook 01_error_handling.ipynb
```

## Next

This closes the LangChain track. Your `LangGraph/` folders pick up from here: stateful graphs, subgraphs,
multi-agent systems and persistence, all built on these fourteen.
