# Runtime Interfaces

Implements: [specifications/runtime-spec.md](../specifications/runtime-spec.md)

Defines platform-level agent I/O contract template. Each agent extends this in its own folder via `agents/{name}/` and registers in the orchestrator (future SDK).

## Machine-Readable Contract

```json
{
  "inputs": [
    "user_request",
    "tenant_context",
    "customer_configuration",
    "crm_context",
    "knowledge_context",
    "user_behavior_signals",
    "conversation_history"
  ],
  "outputs": [
    "response_payload",
    "decision_action",
    "confidence_score",
    "source_references",
    "audit_record"
  ],
  "depends_on": [
    "governance-spec",
    "data-spec",
    "shared",
    "runtime"
  ]
}
```

## Input Definitions

| Input | Source | Required |
|-------|--------|----------|
| `user_request` | Current message | Yes |
| `tenant_context` | Auth / tenancy resolver | Yes |
| `customer_configuration` | Layer 4 | Yes |
| `crm_context` | ServiceNow via data-spec | When CRM-relevant |
| `knowledge_context` | RAG | When KB-relevant |
| `user_behavior_signals` | platform/user-behavior.md | No |
| `conversation_history` | Short memory | Yes |

## Output Definitions

| Output | Description |
|--------|-------------|
| `response_payload` | Must conform to agent OUTPUT_SCHEMA |
| `decision_action` | One of: answer, ask, retrieve, escalate, refuse, recommend |
| `confidence_score` | 0.0–1.0 per governance-spec |
| `source_references` | CRM IDs, KB doc IDs, policy refs |
| `audit_record` | Full audit per governance-spec |
