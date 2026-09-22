# Streaming — Incident Response Assistant

Three ways to stream output from a LangGraph application, demonstrated
side by side on the same simple graph: a sequential incident-response
workflow that analyzes an alert, investigates root causes, and drafts a
resolution report.

## Why streaming matters here

Without streaming, a multi-node graph like this one is silent until the
*entire* pipeline finishes — the user waits for analysis, investigation,
and report generation to all complete before seeing anything. For an
incident-response tool specifically, that's a bad experience: an
on-call engineer wants to see *something* moving immediately, not stare
at a blank screen during an outage. This notebook shows the three
different granularities LangGraph offers for fixing that.

## The graph

A plain three-node sequential graph — deliberately simple, so the focus
stays on the three streaming modes rather than the workflow itself:

```
START → analyze → investigate → generate_report → END
```

- **`analyze`** — extracts core symptoms from the raw incident alert
- **`investigate`** — proposes 3 potential root causes based on that analysis
- **`generate_report`** — turns both into an actionable report for the
  engineering team

## The three streaming modes

**1. Node-level updates — `stream_mode="updates"`**
Yields a complete update the moment each node finishes, rather than
waiting for the whole graph:
```python
for event in app.stream({"incident_data": sample_incident}, stream_mode="updates"):
    for node_name, state_update in event.items():
        print(f"✅ [Completed Node: {node_name}]")
```
Good for showing high-level progress — "analysis done," "investigation
done" — without needing to see inside any one node's LLM call.

**2. Pure token streaming — `llm.stream(...)`**
Not LangGraph-specific at all — this is the plain LangChain chat model
interface, streaming individual tokens as the model generates them:
```python
for chunk in llm.stream([HumanMessage(content=prompt)]):
    print(chunk.content, end="", flush=True)
```
Included deliberately as a contrast case: this is what streaming looks
like *outside* a graph, so the next mode's value is obvious by comparison.

**3. Combined graph + token streaming — `stream_mode="messages"`**
The most granular mode: streams individual LLM tokens as they're
generated *from inside a specific node* of the graph, rather than
waiting for that node to fully complete:
```python
for msg, metadata in app.stream({"incident_data": sample_incident}, stream_mode="messages"):
    if metadata.get("langgraph_node") == "generate_report" and msg.content:
        print(msg.content, end="", flush=True)
```
The `metadata["langgraph_node"]` check is the key detail — it's what
lets you filter token streams down to *one particular node* (here,
`generate_report`) in a graph that has several LLM-calling nodes, rather
than getting an undifferentiated stream of every node's output mixed
together.

## Running it

```bash
pip install langgraph langchain-openai langchain-core python-dotenv
```

Create a `.env` file in this folder:

```
OPENAI_API_KEY=your_key_here
```

Run the notebook cell by cell. The last three cells are the three
streaming demos — run them in order to see the progression from
coarse (node-level) to fine-grained (token-level, scoped to one node).

## Takeaway

Pick the mode based on what the user actually needs to see:
`"updates"` for coarse progress indicators, plain `llm.stream()` when
there's no graph at all, and `"messages"` (filtered by
`langgraph_node`) when you want a specific node's response to feel
like it's typing in real time, inside a larger multi-step workflow.