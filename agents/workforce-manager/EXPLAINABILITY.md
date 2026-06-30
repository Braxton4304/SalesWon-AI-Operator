# Explainability

When an operator asks **"Why did you route this?"** or **"Why is workforce health strained?"** respond with:

1. **Recommendation restated** — target agent_id or human role and work type
2. **Priority score breakdown** — policy/SLA, revenue impact, handoff match, capacity, confidence per [DECISION_MODEL.md](DECISION_MODEL.md)
3. **Evidence** — audit log IDs, telemetry snapshots, handoff queue entries (sources array)
4. **Authority check** — target employee AUTHORITY.md / LIMITATIONS.md pass or fail
5. **What would change the recommendation** — e.g., "If follow-up capacity drops below 100%, defer action would not trigger"

## Conflict Explainability

When asked **"Why is this a conflict?"**:

1. Agents involved and record_id
2. Side-by-side contradiction summary from each agent's sources
3. Severity rationale (customer impact, revenue, policy)
4. Recommended mediation path

## KPI Explainability

When asked **"Why is mean workforce confidence X?"**:

1. Per-employee confidence breakdown with telemetry_freshness
2. Employees pulling aggregate down
3. Recent escalation or refuse events contributing
4. Stale or missing data caveats

All explainability output is **internal operator-facing** — never formatted as end-user coaching or customer communication.

```yaml
explainability_version: "1.0.0"
audience: platform_operators
```
