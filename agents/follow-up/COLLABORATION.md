# Collaboration

Implements: [specifications/workforce-spec.md](../../specifications/workforce-spec.md)

**Who do I work with?** (Distinct from ACCOUNTABILITY ownership.)

## Owns / Does Not Own

**Owns:** Overdue activity surfacing, cadence recommendations, follow-up email drafts, stale opportunity hygiene alerts.

**Does not own:** Deal qualification coaching, forecast commits, account dossiers, case SLA triage, autonomous send execution.

## Collaborates With

| Agent | Relationship |
|-------|--------------|
| **Sales Rep Agent** | Receives deal-context requests; hands off when user needs MEDDIC gaps or next-best-action beyond follow-up |
| **Sales Manager Agent** | Escalations for team coverage, repeated overdue patterns, strategic account critical items |
| **Account Research Agent** | Consumes account briefs when re-engagement needs fresh intel |
| **Customer Service Agent** | Coordinates when follow-up tied to open case affecting sales opp |
| **Workforce Manager** (Phase 2) | Workload and overdue KPI rollup |

## Produces / Consumes

```yaml
produces:
  - artifact: overdue_activity_ranked_list
    schema_ref: agents/follow-up/OUTPUT_SCHEMA.md
    consumer_agents: [sales-rep, sales-manager]
  - artifact: follow_up_email_draft
    schema_ref: agents/follow-up/OUTPUT_SCHEMA.md#recommended_action
    consumer_agents: [sales-rep]
  - artifact: stale_opportunity_alert
    schema_ref: agents/follow-up/OUTPUT_SCHEMA.md
    consumer_agents: [sales-rep, sales-manager]
  - artifact: cadence_recommendation
    schema_ref: agents/follow-up/OUTPUT_SCHEMA.md
    consumer_agents: [sales-rep]

consumes:
  - artifact: opportunity_context
    source_agent: sales-rep
    trigger: user names opp already coached by Sales Rep Agent
  - artifact: account_brief
    source_agent: account-research
    trigger: re-engagement on strategic account needing fresh context
  - artifact: team_coverage_gap
    source_agent: sales-manager
    trigger: manager assigns overdue recovery to rep

handoff_triggers:
  - event: user_requests_qualification_audit
    target_agent: sales-rep
    human_mediated: true
  - event: pricing_discount_needed_in_draft
    target_agent: sales-manager
    human_mediated: true
  - event: account_dossier_requested
    target_agent: account-research
    human_mediated: true
  - event: case_sla_blocking_follow_up
    target_agent: customer-service
    human_mediated: true
  - event: repeated_overdue_same_opp
    target_agent: sales-manager
    human_mediated: true

human_mediated_phase_1: true
```

## Hierarchy Note

Per workforce-spec, Follow-Up Agent sits under Sales Rep Agent in the sales execution chain. Phase 1: all cross-agent artifacts require human initiation — no automatic routing.
