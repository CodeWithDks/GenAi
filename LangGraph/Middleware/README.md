# LangGraph / LangChain Middleware

Examples of **middleware** in LangChain's agent framework — code that runs
*around* a tool call (before, after, or instead of it) without changing
the tool itself. Same idea as middleware in a web framework like Flask or
Express: a wrapper that observes or controls execution without being part
of the core logic it's wrapping.

This folder builds up in two steps: first a middleware that only
**observes** a tool call (logging), then one that actually **enforces** a
rule and can **block** a call outright.

## Files

| Notebook | What it does |
|---|---|
| [`customer-support-guard.ipynb`](./customer-support-guard.ipynb) | Logs a tool call's name and arguments before it runs, and confirms completion after. Observes only — does not block anything. |
| [`tool-security-guard.ipynb`](./tool-security-guard.ipynb) | Inspects every tool call and **blocks** a specific dangerous one (`delete_customer`) before it ever executes, returning a rejection message instead. |

---

## `customer-support-guard.ipynb` — Tool-call logging middleware

**What it demonstrates:** the basic shape of `@wrap_tool_call` — a
decorator that wraps around any tool an agent calls.

1. **A tool**, `get_customer`, that looks up a customer by ID from a small
   hardcoded dictionary (a stand-in for a real customer database).
2. **A middleware function**, `logging_middleware`. Before the wrapped
   tool runs, it prints the tool's name and arguments; the actual tool
   call happens via `handler(request)`; after it finishes, it prints a
   completion message.
3. **An agent** (`gpt-4o-mini`) is built with the tool and middleware
   attached, then asked to "Get information about customer 101" — the
   middleware's logs print around that one tool call.

This notebook is a **logging** example, not access control — it observes
a call, it doesn't stop one. (Despite the filename — see the next
notebook for the version that actually guards something.)

---

## `tool-security-guard.ipynb` — Tool-call blocking middleware

**What it demonstrates:** middleware that inspects a tool call *before*
deciding whether to let it run at all — the pattern an access-control or
safety layer would actually use.

1. **Two tools**: `get_customer` (safe, read-only) and `delete_customer`
   (destructive — deletes an account).
2. **A middleware function**, `security_middleware`, that checks the name
   of every tool call the agent tries to make:
   - If it's `delete_customer` → the middleware **blocks it**. It never
     calls `handler(request)` at all, so the tool never actually runs.
     Instead it returns a `ToolMessage` telling the agent the action was
     blocked.
   - For anything else → the middleware allows it through by calling
     `handler(request)` as normal.
3. **An agent** is built with both tools and this middleware, then asked
   to "Delete customer 101." The middleware intercepts that request and
   blocks it — the agent's final answer reflects the rejection, not a
   successful delete.

**Why this matters:** the tool itself (`delete_customer`) has no idea it
was blocked — it's never called. The safety check lives entirely in the
middleware, so the same rule (block deletes) can be applied to any agent
that uses this middleware, without touching the tool's own code.

---

## Where middleware sits in the agent's flow

```
User: "Delete customer 101"
        │
        ▼
   Agent decides to call delete_customer
        │
        ▼
┌───────────────────────────────────────────┐
│  security_middleware receives the request   │
│                                             │
│  Is it "delete_customer"?                   │
│    ├── YES → 🛡️ BLOCKED                     │
│    │         return rejection ToolMessage   │
│    │         (handler() is never called —   │
│    │          the real tool never runs)     │
│    │                                        │
│    └── NO  → ✅ ALLOWED                     │
│              handler(request) runs the      │
│              real tool normally             │
└───────────────────────────────────────────┘
        │
        ▼
Result (real or blocked) returned to the agent → final answer
```

## Running either notebook

```bash
pip install langchain langchain-openai python-dotenv
```

Create a `.env` file in this folder with your OpenAI key:

```
OPENAI_API_KEY=your_key_here
```

Then run the notebook cell by cell. For `tool-security-guard.ipynb`,
watch the console output around the final `agent.invoke(...)` call — the
`[MIDDLEWARE]` log lines will show the delete request being intercepted
and blocked, followed by the agent's final message reflecting the
rejection rather than a successful deletion.

## Why this folder exists

These two notebooks aren't meant to grow into a bigger project — they're
reference examples, written to understand **what middleware is, where it
sits in an agent's execution, and how to write one**, using the smallest
possible code that makes the idea concrete:

- `customer-support-guard.ipynb` → middleware that **observes** a call
- `tool-security-guard.ipynb` → middleware that **decides** whether a
  call is even allowed to happen

Between the two, that covers the core pattern: a middleware function
receives the request and a `handler`, and it's entirely up to that
function whether `handler(request)` gets called at all. Once that clicks,
the same `@wrap_tool_call` pattern applies directly to real agent
projects — logging, permission checks, rate limiting, redaction, retries
— without needing a separate example for each one.