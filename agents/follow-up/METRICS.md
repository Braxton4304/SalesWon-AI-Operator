# Metrics

## Operational

| Metric | Target |
|--------|--------|
| Schema compliance | ≥ 99% |
| Overdue detection accuracy | ≥ 98% |
| Activity date fact accuracy | ≥ 97% |
| Follow-up priority acceptance | ≥ 70% |
| Email draft acceptance | ≥ 65% |
| Mean confidence | ≥ 0.88 |
| False-positive overdue rate | ≤ 5% |
| Escalation rate (pricing/objection) | Track; expect moderate on objection scenarios |

## Business

| KPI | Description | Phase |
|-----|-------------|-------|
| Overdue recovery rate | % overdue activities completed within 48h of recommendation | 1 track, 2 optimize |
| Stale opp re-activation | Open opps with new activity within 7 days of stale flag | 2 |
| Pipeline velocity | Avg days from stale detection to next completed activity | 2 |
| Revenue at risk recovered | $ weighted pipeline touched after critical follow-up | 2 |

## Accountability Signals

- user_edits to suggested_message (tone/length preferences)
- draft acceptance vs. discard
- escalation acceptance by manager
- corrections to days_overdue or priority disputes

```yaml
metrics_version: "1.0.0"
agent_id: follow-up
rollup_to: workforce-manager
```
