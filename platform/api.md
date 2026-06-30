# API

Frontend and integration HTTP surface. OpenAPI-first when implemented.

## Planned Endpoints (TBD)

| Endpoint | Purpose |
|----------|---------|
| `POST /v1/agent/{agentId}/chat` | Governed agent conversation |
| `GET /v1/agent/{agentId}/health` | Agent readiness |
| `POST /v1/feedback` | User edit / acceptance (METRICS) |
| `GET /v1/audit/{correlationId}` | Audit trail (authorized roles) |

## Principles

- Tenant resolved from auth token — never from request body
- All responses conform to agent OUTPUT_SCHEMA + envelope
- Undocumented endpoints forbidden when SDK ships

## TBD

- Streaming (SSE) for long responses
- ServiceNow embedded widget vs standalone app

## Related

- [architecture/domains/frontend-backend](../architecture/domains/frontend-backend/README.md)
