# LangGraph / Multi-Agent Systems

A supervisor-orchestrated multi-agent workflow — multiple specialized
agents working on the same task, coordinated by a supervisor that decides
who goes next, rather than a fixed, hardcoded sequence.

## `multiagent-content-team.ipynb` — LinkedIn Content Team

**What it builds:** a three-agent content pipeline (Writer, Reviewer,
Final Editor) that drafts, critiques, and polishes a LinkedIn post on a
given topic — supervised by a fourth agent that decides which one runs
next, based on the current state.

### The agents

| Agent | Role |
|---|---|
| **Supervisor** | Looks at the current state (is there a draft? was it approved? how many revisions so far?) and decides what happens next: `writer`, `reviewer`, `final`, or `end`. Uses `with_structured_output` so its decision is always a validated `SupervisorDecision` object, not a plain-text guess. |
| **Writer** | Drafts the post from scratch, or rewrites it using the reviewer's feedback if a revision was requested. |
| **Reviewer** | Reads the draft and returns a structured `STATUS: APPROVED` or `STATUS: NEEDS_REVISION` verdict with 1–2 concrete feedback points. |
| **Final** | Only runs once a draft is approved — polishes it into publish-ready copy, stripped of any commentary. |

### How the routing works

Unlike a fixed pipeline (`writer → reviewer → done`), every agent here
reports back **to the supervisor**, not to the next agent directly. The
supervisor re-evaluates the whole state after each step and decides where
to go next — so a "needs revision" verdict naturally loops back to the
writer instead of needing special-case logic wired into the reviewer
itself.

```
                 ┌──────────────┐
        ┌───────▶│  Supervisor  │◀───────┐
        │        └──────┬───────┘        │
        │               │                │
        │      decides next_agent        │
        │               │                │
   ┌────┴────┐    ┌─────┴─────┐    ┌─────┴────┐
   │  writer  │    │ reviewer  │    │  final   │
   └────┬────┘    └─────┬─────┘    └─────┬────┘
        │               │                │
        └───────────────┴────────────────┘
              (every agent reports back
                 to the supervisor)
                        │
                        ▼
                    END (once
                  final_post is set)
```

### Safety guardrails (this is the part worth noticing)

Multi-agent loops can run forever if nothing stops them — this notebook
builds in two independent limits rather than trusting the LLM to just
"know" when to stop:

- **`MAX_REVISIONS = 3`** — if the writer/reviewer loop hits 3 revisions
  without approval, the supervisor is hard-coded to force a `final`
  routing regardless of what the LLM would otherwise decide. The model
  never gets a chance to loop forever chasing an approval.
- **`recursion_limit: 8`** on the graph execution itself — a second,
  independent circuit breaker at the LangGraph level, in case the first
  guard is ever bypassed or misbehaves.

Both guards are enforced in code, not left to prompting — the kind of
detail that separates a working demo from a workflow that quietly runs
away on you in production.

### Shared state

```python
class ContentState(TypedDict):
    topic: str
    draft: str
    review: str
    review_status: str   # "APPROVED" or "NEEDS_REVISION"
    final_post: str
    next_agent: str
    revision_count: int
```

Every agent reads from and writes back to this one shared state object —
this is what lets the supervisor make an informed routing decision every
time, without needing to pass a full conversation history around.

## Running it

```bash
pip install langgraph langchain-openai pydantic python-dotenv
```

Create a `.env` file in this folder:

```
OPENAI_API_KEY=your_key_here
```

Then run the notebook cell by cell. The last cell streams each node's
execution as it happens (`--- Executed Node: writer ---`, etc.), then
prints the final, publish-ready post. The topic used in the example is
hardcoded (`initial_state["topic"]`) — change it to try the pipeline on a
different subject.

## Why this pattern is worth knowing

A single-prompt "write me a LinkedIn post" call has no self-correction —
whatever the model outputs first is what you get. This pipeline forces a
review step with a real pass/fail gate before anything is considered
"final," and bounds how long that back-and-forth is allowed to run. That
combination — specialized agents, a supervisor making routing decisions
from shared state, and hard limits on the loop — is the core pattern
behind most real multi-agent systems, not just content generation.