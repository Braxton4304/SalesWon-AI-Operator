# Trust Model

**Why trust this routing or workforce assessment?**

## Evidence Sources

| Source | Use |
|--------|-----|
| Agent audit log | decision_action, confidence, sources per employee output |
| Workforce telemetry | Capacity, latency, session counts per agent_id |
| Handoff queue | Producer/consumer status, SLA timestamps |
| Employee METRICS.md rollups | Per-agent operational KPIs |
| policies/ + runtime/GOVERNANCE | Authority and violation detection |
| shared/DIGITAL_WORKFORCE.md | Division of labor ground truth |
| shared/ORGANIZATIONAL_MEMORY.md | Process standards — supplements, never overrides audit facts |

## Confidence Calculation

Per [shared/confidence-scoring.md](../../shared/confidence-scoring.md):

- **Routing recommendations:** Base confidence from handoff matrix match (0.4) + authority check pass (0.3) + capacity headroom (0.2) + corroborating telemetry (0.1)
- **Conflict alerts:** Minimum of involved agents' output confidences, penalized if sources incomplete
- **KPI rollups:** Mean of fresh employee metrics; cap at 0.5 if any employee telemetry stale > 15 min
- **Mean workforce confidence:** Arithmetic mean of five employee mean_confidence values with available telemetry

## Missing Data / Assumptions

| Condition | Handling |
|-----------|----------|
| Employee telemetry unavailable | Label `telemetry_freshness: unavailable`; do not infer capacity |
| Partial audit log | Reduce conflict detection confidence; recommend retrieve |
| Layer 4 routing contacts missing | Escalate to platform ops; do not invent assignee |
| Handoff matrix ambiguity | decision_action: ask operator for classification |

Label assumptions separately from audit-verified facts in summary text.

```yaml
trust_model_version: "1.0.0"
primary_evidence: [audit_log, workforce_telemetry, handoff_queue]
```
