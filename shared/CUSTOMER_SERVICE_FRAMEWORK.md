# Customer Service Framework

Standards for case handling, SLA awareness, and customer sentiment.

## Principles

1. Resolve at lowest appropriate tier before escalation
2. Acknowledge sentiment before procedural response
3. Ground every status update in case record (data-spec)
4. Draft-only case updates unless workflow approved

## SLA Tiers (TBD — Layer 4)

| Tier | Response Target | Resolution Target |
|------|-----------------|-------------------|
| Critical | TBD | TBD |
| High | TBD | TBD |
| Standard | TBD | TBD |

## Sentiment Handling

- Detect from message tone + case history
- Low sentiment + open cases → escalate per escalation-framework
- **TBD:** Sentiment scoring model

## Cross-References

- [escalation-framework.md](escalation-framework.md)
- [platform/DATA_DICTIONARY.md](../platform/DATA_DICTIONARY.md) — Case object
