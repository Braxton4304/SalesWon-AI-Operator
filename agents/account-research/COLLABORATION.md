# Collaboration

Implements: [specifications/workforce-spec.md](../../specifications/workforce-spec.md)

**Who do I work with?** (Distinct from ACCOUNTABILITY ownership.)

## Owns / Does Not Own

**Owns:** Production of `account_brief` and supporting intelligence fields (relationship_map, buying_signals, service_context, research questions).

**Does not own:** Deal execution, case triage, forecast rollups, or follow-up cadence — consumes CRM alongside peer agents without autonomous routing.

## Collaborates With

| Agent | Relationship |
|-------|--------------|
| **Sales Rep Agent** | Primary consumer of account_brief for meeting prep and discovery |
| **Sales Manager Agent** | Consumes briefs for strategic account reviews and coaching |
| **Customer Service Agent** | Parallel reader of case data; may produce case_summary consumed indirectly |
| **Follow-Up Agent** | Indirect — rep may action research tasks after brief review |

Phase 1: all handoffs **human-mediated** — user copies brief or references artifact; no autonomous agent-to-agent messages.

## Produces / Consumes

```yaml
produces:
  - artifact: account_brief
    schema_ref: agents/account-research/OUTPUT_SCHEMA.md
    consumer_agents: [sales-rep, sales-manager]
  - artifact: relationship_map
    schema_ref: agents/account-research/OUTPUT_SCHEMA.md#relationship_map
    consumer_agents: [sales-rep, sales-manager]
  - artifact: recommended_research_questions
    schema_ref: agents/account-research/OUTPUT_SCHEMA.md#recommended_research_questions
    consumer_agents: [sales-rep]

consumes:
  - artifact: case_summary
    source_agent: customer-service
    trigger: user_request_with_service_focus
  - artifact: opportunity_summary
    source_agent: sales-rep
    trigger: user_provides_opp_context_for_research

handoff_triggers:
  - event: user_requests_deal_execution_after_brief
    target_agent: sales-rep
    human_mediated: true
  - event: user_requests_team_rollup_after_brief
    target_agent: sales-manager
    human_mediated: true
  - event: user_requests_case_triage_after_brief
    target_agent: customer-service
    human_mediated: true
  - event: strategic_account_low_confidence
    target_agent: sales-manager
    human_mediated: true

human_mediated_phase_1: true
```

## Handoff Narrative (Demo)

> Rep asks Account Research for Acme brief → reviews account_brief → asks Sales Rep Agent to draft follow-up email using brief context → human sends email.

```yaml
collaboration_version: "1.0.0"
agent_id: account-research
handoff_mode: human_mediated
```
