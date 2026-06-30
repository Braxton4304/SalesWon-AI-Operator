# POC Runtime Architecture

Implements: [ADR-006](../../architecture/DECISIONS.md)

## Layer Mapping

| Spec Layer | POC Location |
|------------|--------------|
| runtime-spec | `apps/poc-runtime/backend/app/runtime/` |
| governance-spec | `apps/poc-runtime/backend/app/audit/`, `security/` |
| data-spec | `apps/poc-runtime/backend/app/connectors/saleswon/` |
| platform/api.md | `apps/poc-runtime/backend/app/api/` |

## Request Flow

```text
User message
  → POST /chat
  → CurrentUserContext (X-User-Id header)
  → ShortTermMemory (session history)
  → IntentRouter (LLMProvider)
  → DecisionEngine (6 actions)
  → ScopeEnforcer (every connector call)
  → SalesWonConnector → ServiceNowAdapter
  → AuditLogger (JSONL)
  → Governed response envelope
```

## Decision Action Semantics

| Action | POC Trigger |
|--------|-------------|
| `answer` | Data returned, confidence ≥ threshold |
| `ask` | Missing required fields |
| `retrieve` | Connector path valid but credentials pending |
| `escalate` | Retrieval exhausted or write error |
| `refuse` | `scope_denied`, `unsupported_action`, `unsafe_write`, `missing_authority` only |
| `recommend` | Draft activity update awaiting confirmation |

## Pluggable Surfaces

- **LLMProvider:** `RuleBasedLLMProvider` (default) | `AzureOpenAIProvider`
- **SalesWonConnector:** `ServiceNowSalesWonConnector` (stub until creds)

No fake CRM data is ever returned. Unconfigured connectors produce `retrieve` + `connector_pending_credentials`.
