# SalesWon AI POC Runtime — Developer Guide

Implements: [ADR-006](../../architecture/DECISIONS.md), [ADR-007](../../architecture/DECISIONS.md)

## Prerequisites

- Python 3.11+
- Node.js 18+
- Azure OpenAI credentials recommended for unscripted demo (falls back to rule_based without them)

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
| `LLM_PROVIDER` | `azure_openai` | `azure_openai` or `rule_based` (fallback) |
| `AZURE_OPENAI_*` | empty | Required for unscripted Azure planning |
| `CONNECTOR` | `servicenow` | Connector implementation |
| `SERVICENOW_*` | empty | Activates live connector when set |

## Unscripted Demo Prompts

Try natural language — no scripted keywords required when Azure is configured:

- "What deals are closing this quarter?"
- "Which accounts have overdue activities?"
- "Move my Acme follow-up to Friday."
- "Mark the Acme call complete."

## Tests

```bash
cd apps/poc-runtime/backend
pytest -q
```

16 tests: 11 connector-ready plumbing + 5 unscripted plan scenarios (mocked LLM).

## Related Docs

- [architecture.md](architecture.md)
- [agent-runtime.md](agent-runtime.md)
- [saleswon-mapping.md](saleswon-mapping.md)
- [connector-contract.md](connector-contract.md)
- [audit-format.md](audit-format.md)
- [scope-enforcement.md](scope-enforcement.md)
