# Collaboration

Implements: [specifications/workforce-spec.md](../../specifications/workforce-spec.md)

**Who do I work with?** (Distinct from ACCOUNTABILITY ownership.)

## Owns / Does Not Own

**Owns:** Production of `case_summary`, ITIL triage assessments, `suggested_customer_response` drafts, and escalation recommendations for CS rep consumption.

**Does not own:** Pipeline analysis, account research depth, follow-up cadence execution, case commits, or customer send — collaborates with peer agents via human-mediated handoffs.

## Organizational Position

```text
Workforce Manager (orchestration)
        │
Customer Service Agent (this agent)
        ↓
CS Rep (human executes drafts and commits)

Parallel: Sales Manager Agent (reads case data for forecast risk)
Supporting: Sales Rep Agent, Account Research Agent, Follow-Up Agent
```

## Collaborates With

| Agent | Relationship |
|-------|--------------|
| **Sales Manager Agent** | Produces case_summary consumed for service_risk in forecast_risks |
| **Sales Rep Agent** | Parallel — CS handles service cases; sales handles opportunities |
| **Account Research Agent** | Consumes account_brief when strategic account escalation context needed |
| **Follow-Up Agent** | Service follow-up tasks may overlap; CS owns case drafts |
| **Workforce Manager** | Observed telemetry; routes CS escalations and low-confidence cases |

Phase 1: all handoffs **human-mediated** — rep copies artifacts or references in conversation; no autonomous agent-to-agent messages.

## Produces / Consumes

```yaml
produces:
  - artifact: case_summary
    schema_ref: agents/customer-service/OUTPUT_SCHEMA.md#case_summary
    consumer_agents: [sales-manager, workforce-manager]
  - artifact: suggested_customer_response
    schema_ref: agents/customer-service/OUTPUT_SCHEMA.md#suggested_customer_response
    consumer_agents: []  # human rep sends
  - artifact: escalation_assessment
    schema_ref: agents/customer-service/OUTPUT_SCHEMA.md#escalation_required
    consumer_agents: [workforce-manager]

consumes:
  - artifact: account_brief
    source_agent: account-research
    trigger: user_request_strategic_account_case_context
  - artifact: pipeline_summary
    source_agent: sales-manager
    trigger: user_request_revenue_context_for_vip_case

handoff_triggers:
  - event: user_requests_sales_context_on_service_case
    target_agent: sales-rep
    human_mediated: true
  - event: user_requests_forecast_impact_from_open_cases
    target_agent: sales-manager
    human_mediated: true
  - event: user_requests_account_deep_dive_for_escalation
    target_agent: account-research
    human_mediated: true
  - event: user_requests_follow_up_cadence_on_case_task
    target_agent: follow-up
    human_mediated: true
  - event: case_confidence_below_threshold_or_mandatory_escalation
    target_agent: workforce-manager
    human_mediated: true

human_mediated_phase_1: true
```

## Handoff Narrative (Demo)

> Rep asks Customer Service Agent to summarize INC0012345 on VIP account Acme → reviews case_summary and severity → drafts suggested_customer_response → human sends email → asks Sales Manager Agent how open P1 cases affect Acme forecast → asks Account Research Agent for stakeholder map before executive escalation → Workforce Manager notified on mandatory escalation.

```yaml
collaboration_version: "1.0.0"
agent_id: customer-service
handoff_mode: human_mediated
monitored_by: workforce-manager
primary_produces: [case_summary, suggested_customer_response]
```
