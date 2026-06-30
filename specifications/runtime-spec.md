---
spec_version: "1.0.0"
spec_id: runtime-spec
title: SalesWon AI Runtime Specification
---

# Runtime Specification

Defines how the platform assembles context, makes decisions, applies business reasoning, and manages memory before and after every LLM call.

## Scope

This spec governs:

- Context assembly order (`RUNTIME_CONTEXT.md`)
- Decision engine actions (`DECISION_ENGINE.md`)
- Business optimization targets (`BUSINESS_REASONING.md`)
- Memory tiers short vs. long (`MEMORY_MODEL.md`)
- Agent I/O interfaces (`INTERFACES.md`)
- Runtime defaults (`CONFIG.yaml`)

Agents import runtime; they do not redefine it.

## Context Assembly Order

Every LLM invocation MUST assemble context in this order:

1. System prompt (platform + governance)
2. Agent prompt (role-specific)
3. Customer configuration (Layer 4)
4. ServiceNow / CRM data (Layer 5, retrieved)
5. Knowledge retrieval (RAG)
6. User behavior signals
7. Conversation history (short memory)
8. Current user request

See implementation: [runtime/RUNTIME_CONTEXT.md](../runtime/RUNTIME_CONTEXT.md).

## Decision Engine Actions

The runtime MUST support exactly these decision outcomes:

| Action | Description |
|--------|-------------|
| `answer` | Respond with grounded output matching OUTPUT_SCHEMA |
| `ask` | Clarify missing required fields or ambiguous intent |
| `retrieve` | Fetch additional CRM or knowledge data |
| `escalate` | Route to human per escalation-framework |
| `refuse` | Decline when policy, permissions, or confidence block action |
| `recommend` | Propose action without executing (draft-only writes) |

See implementation: [runtime/DECISION_ENGINE.md](../runtime/DECISION_ENGINE.md).

## Memory Tiers

| Tier | Scope | Storage (future) |
|------|-------|------------------|
| Short | Current conversation, current task | Session / ephemeral |
| Long | User preferences, historical decisions, org memory | Azure SQL |

See implementation: [runtime/MEMORY_MODEL.md](../runtime/MEMORY_MODEL.md).

## Machine-Readable Contract

```yaml
spec_version: "1.0.0"
spec_id: runtime-spec
context_assembly_order:
  - system_prompt
  - agent_prompt
  - customer_configuration
  - crm_data
  - knowledge_retrieval
  - user_behavior
  - conversation_history
  - current_request
decision_actions:
  - answer
  - ask
  - retrieve
  - escalate
  - refuse
  - recommend
memory_tiers:
  short:
    scope: [conversation, current_task]
  long:
    scope: [user_preferences, historical_decisions, learned_behavior, organization_memory]
config_required_keys:
  - agent
  - execution
  - evidence
  - governance
interfaces_required_keys:
  inputs: array
  outputs: array
  depends_on: array
```

## References

- Implements: [governance-spec.md](governance-spec.md), [data-spec.md](data-spec.md)
- Implemented by: [runtime/](../runtime/)
