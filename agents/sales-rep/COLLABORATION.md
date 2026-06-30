# Collaboration

Implements: [specifications/workforce-spec.md](../../specifications/workforce-spec.md)

**Who do I work with?** (Distinct from ACCOUNTABILITY ownership.)

## Owns / Does Not Own

**Owns:** Production of `opportunity_summary`, `deal_health`, `qualification_gaps`, `next_best_action`, `recommended_questions`, and `suggested_follow_up` for rep consumption.

**Does not own:** Team pipeline rollups, account research depth, case triage, follow-up cadence orchestration, or forecast commits — collaborates with peer agents via human-mediated handoffs.

## Organizational Position

```text
Workforce Manager (orchestration)
        │
Sales Manager Agent
        ↓
Sales Rep Agent (this agent)
        ↓
Follow-Up Agent

Parallel: Customer Service Agent
Supporting: Account Research Agent
```

## Collaborates With

| Agent | Relationship |
|-------|--------------|
| **Sales Manager Agent** | Consumes rep_coaching_items (human-mediated); produces opportunity_summary for manager deal reviews |
| **Account Research Agent** | Consumes account_brief for meeting prep and discovery context |
| **Follow-Up Agent** | Produces opportunity_summary + suggested_follow_up for cadence prioritization |
| **Customer Service Agent** | Parallel reader of case data; service risk context on active deal accounts |
| **Workforce Manager** | Observed telemetry; routes opp/activity escalations |

Phase 1: all handoffs **human-mediated** — rep copies artifacts or references in conversation; no autonomous agent-to-agent messages.

## Produces / Consumes

```yaml
produces:
  - artifact: opportunity_summary
    schema_ref: agents/sales-rep/OUTPUT_SCHEMA.md#opportunity_summary
    consumer_agents: [sales-manager, follow-up, workforce-manager]
  - artifact: next_best_action
    schema_ref: agents/sales-rep/OUTPUT_SCHEMA.md#next_best_action
    consumer_agents: [follow-up]
  - artifact: qualification_gaps
    schema_ref: agents/sales-rep/OUTPUT_SCHEMA.md#qualification_gaps
    consumer_agents: [sales-manager]
  - artifact: suggested_follow_up
    schema_ref: agents/sales-rep/OUTPUT_SCHEMA.md#suggested_follow_up
    consumer_agents: [follow-up]

consumes:
  - artifact: account_brief
    source_agent: account-research
    trigger: user_request_meeting_prep_or_discovery_context
  - artifact: rep_coaching_items
    source_agent: sales-manager
    trigger: user_references_manager_1_1_coaching
  - artifact: case_summary
    source_agent: customer-service
    trigger: user_request_service_impact_on_deal
  - artifact: pipeline_summary
    source_agent: sales-manager
    trigger: user_request_team_context_for_own_deal

handoff_triggers:
  - event: user_requests_account_deep_dive
    target_agent: account-research
    human_mediated: true
  - event: user_requests_manager_pricing_approval
    target_agent: sales-manager
    human_mediated: true
  - event: user_requests_follow_up_cadence_after_deal_review
    target_agent: follow-up
    human_mediated: true
  - event: user_requests_case_escalation_for_deal_account
    target_agent: customer-service
    human_mediated: true
  - event: deal_confidence_below_threshold_after_retrieves
    target_agent: workforce-manager
    human_mediated: true
  - event: user_requests_team_pipeline_rollup
    target_agent: sales-manager
    human_mediated: true

human_mediated_phase_1: true
```

## Handoff Narrative (Demo)

> Rep asks Account Research for Acme brief → reviews account_brief → asks Sales Rep Agent to qualify Acme Expansion → receives opportunity_summary, qualification_gaps (MEDDIC), and next_best_action → drafts email via suggested_follow_up → asks Follow-Up Agent to schedule cadence → manager shares rep_coaching_items from Sales Manager Agent in 1:1 → rep updates CRM and sends email.

## Conflict Resolution

| Conflict | Resolution |
|----------|------------|
| sales-manager coaching vs next_best_action | Defer to manager hierarchy; note in summary |
| account-research brief stale vs active opp changes | Recommend refresh handoff to account-research |
| follow-up suggested_message vs sales-rep draft email | sales-rep owns send decision; follow-up supports |
| CS case_summary vs opp context on same account | Surface both; recommend human account team review |

```yaml
collaboration_version: "1.1.0"
agent_id: sales-rep
handoff_mode: human_mediated
monitored_by: workforce-manager
```
