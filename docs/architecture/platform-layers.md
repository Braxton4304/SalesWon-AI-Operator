# Platform Layers

SalesWon AI operating system — layer model and future SDK.

## Layers

```text
/specifications          Layer 0 — Contracts (ISO-style)
/shared                  Layer 1 — Business standards
/runtime                 Layer 2 — Platform runtime
/agents                  Layer 3 — Agent specifications
/platform                Integrations (implements data-spec)
/architecture            Blueprint workspace
Layer 4                  Customer configuration (per deployment)
Layer 5                  Customer CRM data (never in repo)
```

## Governed Response Pipeline

```text
Business Standards → Runtime → Agent → Customer Config → CRM Context → LLM → Governed Response
```

## Context Assembly

See [runtime/RUNTIME_CONTEXT.md](../runtime/RUNTIME_CONTEXT.md):

```text
System Prompt → Agent Prompt → Customer Config → ServiceNow Data →
Knowledge Retrieval → User Behavior → Conversation History → Current Request
```

## SalesWon AI SDK (Planned)

| Module | Spec / Implementation |
|--------|----------------------|
| Runtime | runtime-spec, runtime/ |
| Agent Specification | agent-spec, agents/ |
| Governance | governance-spec, runtime/GOVERNANCE.md |
| Memory Engine | MEMORY_MODEL, MEMORY_SHORT/LONG |
| Prompt Builder | RUNTIME_CONTEXT |
| Decision Engine | DECISION_ENGINE |
| Business Reasoning | BUSINESS_REASONING |
| ServiceNow Connector | platform/servicenow, DATA_DICTIONARY |
| Tool Definitions | agents/TOOLS |
| Behavior Engine | platform/user-behavior |
| Feedback Engine | platform/feedback |
| Evaluation Engine | QUALITY, METRICS |

Phase 1 delivers contracts. SDK implementation is Phase 2.

## Cross-Product Reuse

| Product | Imports |
|---------|---------|
| SalesWon Operator | Full implementation |
| Cohort | specifications/* + customer layers |
| Axiom | specifications/* + customer layers |
| AI Council | governance-spec, runtime-spec (orchestration) |

## Extension

- New agent: copy `agents/_template/`
- New CRM object: update `data-spec.md` → `DATA_DICTIONARY.md`
- New domain: top-level README charter only

See [architecture/ROADMAP.md](../architecture/ROADMAP.md).
