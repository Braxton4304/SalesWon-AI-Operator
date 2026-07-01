# POC Runtime Architecture

Implements: [ADR-006](../../architecture/DECISIONS.md), [ADR-007](../../architecture/DECISIONS.md)

## Core rule

```text
LLM plans.
Backend validates.
Connector executes.
User confirms writes.
```

## Layer Mapping

| Spec Layer | POC Location |
|------------|--------------|
| runtime-spec | `apps/poc-runtime/backend/app/runtime/` |
| agent-spec | `apps/poc-runtime/backend/app/agent/` |
| governance-spec | `apps/poc-runtime/backend/app/audit/`, `security/` |
| data-spec | `apps/poc-runtime/backend/app/connectors/saleswon/`, `config/saleswon_mapping.yaml` |
| platform/api.md | `apps/poc-runtime/backend/app/api/` |

## Request Flow (Unscripted Agent v1)

```text
User message
  → POST /chat
  → CurrentUserContext (X-User-Id header)
  → PromptCompiler (agent specs + policies + mapping + session)
  → AzureOpenAIProvider.plan() → ActionPlan JSON
  → PlanValidator
  → PlanExecutor → ScopeEnforcer → SalesWonConnector
  → ConfirmationStore (writes only)
  → LLM generate_response (narrative)
  → AuditLogger (JSONL)
```

## Decision Action Semantics

| Action | POC Trigger |
|--------|-------------|
| `answer` | Data returned, confidence ≥ threshold |
| `ask` | Missing required fields in ActionPlan |
| `retrieve` | Connector path valid but credentials pending |
| `escalate` | Retrieval exhausted or write error |
| `refuse` | `scope_denied`, `unsupported_action`, `unsafe_write`, `missing_authority` only |
| `recommend` | Draft activity update awaiting confirmation |

## Pluggable Surfaces

- **LLMProvider:** `AzureOpenAIProvider` (default) | `RuleBasedLLMProvider` (fallback)
- **SalesWonConnector:** `ServiceNowSalesWonConnector` (mapping-driven, stub until creds)
- **Agent contracts:** loaded from `/agents/` via `poc_agent_manifest.yaml`

No fake CRM data is ever returned. Unconfigured connectors produce `retrieve` + `connector_pending_credentials`.

See [agent-runtime.md](agent-runtime.md) for ActionPlan and manifest details.
