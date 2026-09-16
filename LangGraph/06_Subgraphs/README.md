# LangGraph Subgraphs

A **subgraph** is a graph inside another LangGraph workflow.

Subgraphs are useful when a part of a workflow becomes a separate, logical workflow that can be developed, tested, and maintained independently.

---

## Create the File

Create the following structure:

```text
subgraphs/
└── README.md
```

Copy the content below into `subgraphs/README.md`.

---

# Why Use Subgraphs?

Instead of putting every node into one large graph:

```text
START
  ↓
Node A
  ↓
Node B
  ↓
Node C
  ↓
Node D
  ↓
Node E
  ↓
END
```

we can group related nodes into a subgraph:

```text
START
  ↓
Node A
  ↓
┌──────────────────────┐
│      Subgraph        │
│                      │
│  Node B → Node C     │
│          ↓           │
│        Node D        │
└──────────┬───────────┘
           ↓
        Node E
           ↓
          END
```

The parent graph treats the subgraph as a workflow component.

---

# Two Important Subgraph Patterns

LangGraph commonly uses two approaches depending on how the parent and child graphs communicate state:

1. **Different-State / Custom-State Subgraph**
2. **Shared-State Subgraph**

---

# 1. Different-State / Custom-State Subgraph

In this pattern, the parent and child graphs use **different state schemas**.

The parent does not directly share its state with the child.

Instead, a **wrapper node** passes the required data to the child graph and receives the result back.

## Structure

```text
Parent Graph

START
  ↓
Parent Node
  ↓
Wrapper Node
  ↓
┌──────────────────────┐
│    Child Subgraph    │
│                      │
│  Node A → Node B     │
│          ↓           │
│        Node C        │
└──────────┬───────────┘
           ↓
      Parent continues
```

## Integration

```python
def run_child_graph(state):

    result = child_graph.invoke({
        "question": state["question"]
    })

    return {
        "category": result["category"]
    }


parent_builder.add_node(
    "analysis",
    run_child_graph
)
```

Here, the wrapper controls:

* What data enters the child graph
* What data comes back from the child graph
* How parent and child state are mapped

## When to Use

Use this pattern when:

* Parent and child have different state schemas
* The child has private or internal state
* You want to isolate a module
* You are integrating an independent workflow
* You are building multi-agent systems where each agent has its own state

## Example Use Case: AI Customer Support

The parent workflow might have:

```python
class SupportState(TypedDict):
    question: str
    response: str
```

The child analysis workflow might have:

```python
class AnalysisState(TypedDict):
    question: str
    category: str
    priority: str
    sentiment: str
```

The child performs detailed analysis and returns only what the parent needs.

```text
Support Graph
      ↓
Analysis Wrapper
      ↓
Analysis Subgraph
      ↓
category + priority
      ↓
Support Graph
```

This keeps the analysis workflow isolated from the parent.

---

# 2. Shared-State Subgraph

In this pattern, the parent and child graphs **share state keys**.

The child graph can directly operate on state that belongs to the parent workflow.

The subgraph can be added directly as a node:

```python
parent_builder.add_node(
    "analysis",
    child_graph
)
```

No wrapper function is required.

## Structure

```text
Parent Graph
     ↓
┌──────────────────────┐
│    Child Subgraph    │
│                      │
│  Node A              │
│    ↓                 │
│  Node B              │
│    ↓                 │
│  Node C              │
└──────────┬───────────┘
           ↓
Parent Graph
```

## Example State

```python
class SupportState(TypedDict):
    ticket: str
    category: str
    priority: str
    customer_name: str
    response: str
```

The child subgraph can update:

```text
category
priority
customer_name
```

The parent can then use those values.

```text
Parent
  ↓
Ticket Analysis Subgraph
  ↓
category
priority
customer_name
  ↓
Parent
  ↓
Generate Response
```

## Integration

```python
parent_builder.add_node(
    "analysis",
    analysis_subgraph
)
```

The important point is that the parent and child have **compatible/shared state keys**.

---

# Shared State vs Different State

| Aspect          | Shared State           | Different / Custom State |
| --------------- | ---------------------- | ------------------------ |
| State           | Share one or more keys | Independent schemas      |
| Integration     | Direct `add_node()`    | Wrapper function         |
| Data mapping    | Minimal                | Explicit mapping         |
| Child isolation | Lower                  | Higher                   |
| Best for        | Integrated workflows   | Independent modules      |
| Example         | Ticket analysis        | Separate agent workflow  |

## Simple Rule

```text
Do parent and child share state keys?
            │
       ┌────┴────┐
       │         │
      YES       NO
       ↓         ↓
 Shared State   Custom State
       ↓         ↓
 add_node()     Wrapper
                  ↓
          child_graph.invoke()
```

---

# Real-World Use Cases

## Shared-State Subgraph

Shared-state subgraphs are useful when different stages of a workflow work on the **same information**.

Examples:

* Customer support ticket analysis
* Document processing
* Content analysis
* Resume analysis
* Order processing
* Data processing pipelines

Example:

```text
Customer Support
      ↓
Ticket Analysis Subgraph
      ↓
category
priority
sentiment
      ↓
Response Generation
```

---

## Different-State / Custom-State Subgraph

Custom-state subgraphs are useful for **isolated workflows** that have their own internal state.

Examples:

* Multi-agent systems
* Independent research agents
* Specialized analysis modules
* Third-party workflow integration
* Complex reusable components

Example:

```text
Main Agent
    ↓
Research Wrapper
    ↓
Research Subgraph
    ↓
Research Result
    ↓
Main Agent
```

The research subgraph can have its own internal workflow and state without exposing everything to the parent.

---

# Key Takeaway

A subgraph is useful when a workflow contains a **logical group of steps that should behave as an independent workflow**.

The main decision is how the parent and child communicate:

```text
Shared State
→ Directly connect the child graph.

Different State
→ Use a wrapper to transform and pass data.
```

The goal is **not** to create subgraphs everywhere.

Use them when they make the workflow:

* Easier to understand
* Easier to test
* Easier to reuse
* Better organized
* More isolated when necessary
