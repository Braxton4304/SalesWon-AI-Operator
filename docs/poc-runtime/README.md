# SalesWon AI POC Runtime — Developer Guide

Implements: [ADR-006](../../architecture/DECISIONS.md), [runtime-spec](../../specifications/runtime-spec.md)

## Prerequisites

- Python 3.11+
- Node.js 18+
- No ServiceNow or Azure OpenAI credentials required for local demo

## Setup

### Backend

```bash
cd apps/poc-runtime/backend
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -e ".[dev]"
copy .env.example .env
uvicorn app.main:app --reload --port 8001
```

### Frontend

```bash
cd apps/poc-runtime/frontend
npm install
npm run dev
```

Open http://localhost:5173

## Environment Variables

See [backend/.env.example](../backend/.env.example).

| Variable | Default | Purpose |
|----------|---------|---------|
| `LLM_PROVIDER` | `rule_based` | `rule_based` or `azure_openai` |
| `CONNECTOR` | `servicenow` | Connector implementation |
| `AUDIT_LOG_PATH` | `./audit/events.jsonl` | Local audit trail |
| `SERVICENOW_*` | empty | Activates live connector when set |

## Demo Flows

1. **Read (connector pending):** "show my open opportunities" → `retrieve` + `connector_pending_credentials`
2. **Update with clarification:** "update my call activity for ACME" → `ask` for status
3. **Update with confirmation:** "update my call activity for ACME to done" → `recommend` → Confirm → `retrieve` + `connector_pending_credentials`
4. **Scope denied:** Set user to `alice`, use configured mock in tests with record owned by `bob`

## Tests

```bash
cd apps/poc-runtime/backend
pytest -v
```

## Related Docs

- [architecture.md](architecture.md)
- [connector-contract.md](connector-contract.md)
- [audit-format.md](audit-format.md)
- [scope-enforcement.md](scope-enforcement.md)
