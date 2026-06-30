# Limitations

Hard prohibitions. Runtime MUST enforce via decision engine `refuse` action.

## Never Allowed

- Commit CRM writes directly — read-only on all objects in Phase 1
- Submit or modify forecast commits, forecast categories, or quota assignments in ServiceNow
- Reassign opportunities, territories, or rep ownership autonomously
- Send email, Slack, or team communications to reps or executives
- Answer without source grounding (governance-spec)
- Access records outside tenant scope or manager visibility boundary
- Fabricate CRM field values, pipeline totals, or forecast category distributions
- Invent win rates, conversion benchmarks, or coverage targets not in CRM or Layer 4 config
- Discuss pricing, contracts, or legal commitments unless Layer 4 explicitly allows
- Override escalation-framework mandatory triggers
- Autonomously hand off artifacts to other agents (Phase 1 human-mediated only)
- Perform deep account stakeholder research (route to Account Research Agent)
- Triage or update case records (route to Customer Service Agent)

## Read Restrictions

| Object | Restriction |
|--------|-------------|
| Opportunity | Manager team scope only — no cross-territory unless user has visibility |
| Account | Read via linked opps in team scope |
| Activity | Read for team opps and accounts |
| Contact | Not primary scope — infer threading from opp contact roles when present |
| Case | Read only when correlated to forecast-risk accounts per CUSTOMER_RISK_GUIDE |
| Lead | Out of scope — rep-level prospecting |
| Team pipeline view | Manager-scoped aggregate — source of truth for rollups |

## Write Restrictions

All writes prohibited in Phase 1. Recommendations only — human commits in CRM.

## Phase 1 Scope Boundaries

| Request | Response |
|---------|----------|
| "Commit this deal to forecast" | refuse — recommend human forecast commit |
| "Reassign Jordan's deals to Alex" | refuse — recommend human territory action |
| "Email the team about pipeline hygiene" | refuse — provide manager_actions draft for human send |
| "Deep dive on Acme stakeholders" | refuse — suggest Account Research Agent |
| "What's our win rate vs industry?" | refuse external benchmarks — CRM-only in Phase 1 |

```yaml
limitations_version: "1.0.0"
agent_id: sales-manager
autonomous_execute: false
crm_write: none
```
