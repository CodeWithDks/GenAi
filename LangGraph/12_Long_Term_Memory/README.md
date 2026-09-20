# Long-Term Memory — AI Fitness & Health Coach

A multi-agent LangGraph workflow demonstrating **long-term, cross-session
memory** — an AI fitness coach that remembers a user's injuries, dietary
restrictions, and goals across separate conversations, without the user
ever having to repeat them.

## How this differs from `../09_Memory_Persistence`

`09_Memory_Persistence` covers LangGraph's **checkpointer** — memory of
*this specific conversation's* message history, so an agent doesn't
forget what was just said. This notebook covers something different:
LangGraph's **`InMemoryStore`**, a namespaced key-value store for facts
that should persist *across* sessions entirely — a user's fitness profile
doesn't belong to any one conversation; it should be available the next
time they show up, days later, with no memory of the earlier chat baked
into a message history at all.

## What it demonstrates

**1. Memory extraction** — `extract_fitness_memory()` reads a user
message and pulls out only the facts worth remembering long-term
(injuries, dietary restrictions, goals, equipment/training preferences),
returning `NONE` if there's nothing persistent to store.

**2. Memory storage & retrieval** — facts are saved into `InMemoryStore`
under a per-user namespace (`(user_id, "fitness_profile")`) and retrieved
with `get_fitness_profile()` / `build_fitness_context()` — the same
pattern a real app would use, just with an in-memory store standing in
for a persistent one.

**3. A supervisor-routed multi-agent workflow** (the same pattern as
[`../10_Multiagent`](../10_Multiagent)) built on top of that memory:

- **`supervisor`** — decides what runs next based on current state,
  using structured output (`SupervisorDecision`) rather than parsing text
- **`fitness_planner_agent`** — drafts a workout/meal plan, given the
  user's request *and* their stored long-term profile
- **`safety_reviewer_agent`** — checks the draft against the stored
  constraints (does it actually avoid the user's bad knee? is it
  actually dairy-free?) and returns `APPROVED` or `NEEDS_REVISION`
- **`final_agent`** — polishes the approved plan into the final response

**4. The same safety guardrails as `10_Multiagent`** — `MAX_REVISIONS = 3`
hard-stops the planner/reviewer loop regardless of what the supervisor's
LLM call would otherwise decide, plus an independent `recursion_limit: 8`
at the graph level as a second circuit breaker.

## The example walkthrough

The notebook's demo cell simulates two *prior* sessions storing memory,
then a *new* session that never repeats that context:

1. **Session 1:** *"I broke my right knee last year and cannot do heavy
   barbell squats or jumping exercises."* → stored.
2. **Session 2:** *"I recently went strict lactose-free vegan and want
   high protein meals."* → stored.
3. **Session 3 (new conversation):** *"Give me a quick 20-minute leg
   workout and a post-workout recovery snack."* — no mention of the knee
   or the diet.

The agent pulls both stored facts from memory and produces a plan that
automatically avoids barbell squats/jumping (low-impact alternatives
instead) and avoids dairy/animal products in the snack suggestion — all
without the user restating either constraint.

## Running it

```bash
pip install langchain-openai langgraph langchain-core pydantic python-dotenv
```

Create a `.env` file in this folder:

```
OPENAI_API_KEY=your_key_here
```

Then run the notebook cell by cell. The final cell streams each node's
execution (`--- Executed Node: supervisor ---`, etc.) so you can watch
the supervisor route between planner and reviewer before producing the
final, memory-compliant plan.

## Note on `InMemoryStore`

As the name says, this store is in-memory — it resets when the notebook
process ends. That's the right choice for demonstrating the *pattern*;
a real application would swap it for a persistent backend (LangGraph
supports Postgres-backed stores, for instance) without changing anything
about how the agents read or write memory — the store's interface stays
the same either way.