# Collaboration

Implements: [specifications/workforce-spec.md](../../specifications/workforce-spec.md)

**Who do I work with?** (Distinct from ACCOUNTABILITY ownership.)

## Owns / Does Not Own

**Owns:** Production of `pipeline_summary`, `forecast_risks`, `rep_coaching_items`, and `manager_actions` for manager consumption.

**Does not own:** Individual deal execution, account research depth, case triage, follow-up cadence, or forecast commits — collaborates with peer agents via human-mediated handoffs.

## Organizational Position

```text
Workforce Manager (orchestration)
        │
Sales Manager Agent (this agent)
        ↓
Sales Rep Agent
        ↓
Follow-Up Agent

Parallel: Customer Service Agent
Supporting: Account Research Agent
```

## Collaborates With

| Agent | Relationship |
|-------|--------------|
| **Sales Rep Agent** | Consumes opportunity_summary; produces rep_coaching_items for rep 1:1s |
| **Follow-Up Agent** | Produces pipeline_summary for team cadence prioritization |
| **Account Research Agent** | Consumes account_brief for strategic account forecast reviews |
| **Customer Service Agent** | Parallel reader of case data; service_risk in forecast_risks |
| **Workforce Manager** | Observed telemetry; routes forecast/pipeline escalations |

Phase 1: all handoffs **human-mediated** — manager copies artifacts or references in conversation; no autonomous agent-to-agent messages.

## Produces / Consumes

```yaml
produces:
  - artifact: pipeline_summary
    schema_ref: agents/sales-manager/OUTPUT_SCHEMA.md#pipeline_summary
    consumer_agents: [follow-up, workforce-manager]
  - artifact: rep_coaching_items
    schema_ref: agents/sales-manager/OUTPUT_SCHEMA.md#rep_coaching_items
    consumer_agents: [sales-rep]
  - artifact: forecast_risks
    schema_ref: agents/sales-manager/OUTPUT_SCHEMA.md#forecast_risks
    consumer_agents: [sales-rep, follow-up]
  - artifact: manager_actions
    schema_ref: agents/sales-manager/OUTPUT_SCHEMA.md#manager_actions
    consumer_agents: []  # human manager executes

consumes:
  - artifact: account_brief
    source_agent: account-research
    trigger: user_request_strategic_account_forecast_review
  - artifact: opportunity_summary
    source_agent: sales-rep
    trigger: user_provides_rep_deal_context_for_coaching
  - artifact: case_summary
    source_agent: customer-service
    trigger: user_request_service_impact_on_forecast

handoff_triggers:
  - event: user_requests_rep_deal_execution_after_coaching
    target_agent: sales-rep
    human_mediated: true
  - event: user_requests_follow_up_cadence_after_pipeline_review
    target_agent: follow-up
    human_mediated: true
  - event: user_requests_account_deep_dive_after_risk_flag
    target_agent: account-research
    human_mediated: true
  - event: user_requests_case_escalation_for_forecast_account
    target_agent: customer-service
    human_mediated: true
  - event: team_pipeline_confidence_below_threshold
    target_agent: workforce-manager
    human_mediated: true

human_mediated_phase_1: true
```

## Handoff Narrative (Demo)

> Manager asks Sales Manager for Q3 pipeline review → reviews pipeline_summary and forecast_risks → shares rep_coaching_items with Jordan in 1:1 → asks Sales Rep Agent to draft next steps on Acme Expansion → asks Follow-Up Agent to prioritize team follow-ups on at-risk commit deals → human sends communications.

```yaml
collaboration_version: "1.0.0"
agent_id: sales-manager
handoff_mode: human_mediated
monitored_by: workforce-manager
```
