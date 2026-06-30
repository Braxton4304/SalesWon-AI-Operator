# Governance

Implements: [specifications/governance-spec.md](../specifications/governance-spec.md)

## Governed AI Checklist

Every response MUST satisfy:

- [ ] Audit log entry written
- [ ] Confidence score computed and recorded
- [ ] Sources cited in `source_references`
- [ ] Escalation path defined if below threshold
- [ ] Tenant scope validated
- [ ] Policy check passed (capabilities + limitations + data-spec)

## Confidence Bands

| Band | Range | Default Action |
|------|-------|----------------|
| High | ≥ 0.85 | answer / recommend |
| Medium | 0.60–0.84 | answer with caveat; human review for writes |
| Low | < 0.60 | ask / retrieve / escalate |

Configure in [CONFIG.yaml](CONFIG.yaml). Normative defaults in governance-spec.

## Audit Record Schema

```yaml
tenant_id: string
correlation_id: uuid
actor: string          # user_id or agent_id
timestamp: datetime    # UTC
decision_action: string
confidence_score: float
source_references: array
outcome: string        # success | escalated | refused | error
agent_id: string
request_summary: string  # no PII in logs unless policy allows
```

## Cross-References

- [shared/confidence-scoring.md](../shared/confidence-scoring.md)
- [shared/escalation-framework.md](../shared/escalation-framework.md)
- [DECISION_ENGINE.md](DECISION_ENGINE.md)
