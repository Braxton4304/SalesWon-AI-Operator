# Observability

Logging, metrics, and tracing for governed AI operations.

## Requirements (from governance-spec)

Every request traceable by `correlation_id` across:

- API gateway
- Runtime / decision engine
- ServiceNow calls
- LLM invocations
- Audit write

## Metrics

From agent [METRICS.md](../agents/_template/METRICS.md):

- Schema compliance, source grounding, escalation rate, average confidence
- Business metrics (ROI, SLA) — TBD per deployment

## Stack (Planned)

- Azure Application Insights
- Log Analytics workspace
- Structured JSON logs (no secrets, PII per SECURITY.md)

## Alerts (TBD)

- Escalation rate spike
- Confidence drop below baseline
- ServiceNow API errors
- LLM latency / error rate

## Related

- [runtime/GOVERNANCE.md](../runtime/GOVERNANCE.md)
