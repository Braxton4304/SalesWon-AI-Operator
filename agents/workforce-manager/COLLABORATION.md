# Collaboration

Implements: [specifications/workforce-spec.md](../../specifications/workforce-spec.md)

**Who do I work with?** (Distinct from ACCOUNTABILITY ownership.)

The Workforce Manager **supervises collaboration** among all five Digital Employees. It does not produce domain artifacts (case summaries, opportunity briefs, etc.) — it orchestrates handoffs, monitors completion, and resolves conflicts.

## Owns / Does Not Own

**Owns (orchestration layer):**

- Routing directives between employees and to humans
- Conflict mediation recommendations
- Handoff queue health monitoring
- Cross-agent escalation routing

**Does Not Own (employee domain):**

- account_brief, case_summary, opportunity_summary, pipeline_summary, rep_coaching_items, suggested_message — produced by employees per handoff matrix

## Organizational Hierarchy

```text
Workforce Manager (this agent)
        │
Sales Manager Agent
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
| [customer-service](../customer-service/AGENT.md) | Observe telemetry; route CS work; mediate CS ↔ sales conflicts |
| [sales-rep](../sales-rep/AGENT.md) | Observe telemetry; route opp/activity work; sales chain coordination |
| [sales-manager](../sales-manager/AGENT.md) | Observe telemetry; route forecast/pipeline escalations |
| [account-research](../account-research/AGENT.md) | Observe telemetry; route research requests; feed handoff monitoring |
| [follow-up](../follow-up/AGENT.md) | Observe telemetry; route cadence work; balance follow-up load |

## Employee Handoff Matrix (Monitored)

Per [shared/DIGITAL_WORKFORCE.md](../../shared/DIGITAL_WORKFORCE.md):

| Producer | Artifact | Consumer |
|----------|----------|----------|
| account-research | account_brief | sales-rep, sales-manager |
| customer-service | case_summary | sales-rep, account-research |
| sales-rep | opportunity_summary | sales-manager, follow-up |
| sales-manager | rep_coaching_items | sales-rep |
| sales-manager | pipeline_summary | follow-up |
| follow-up | suggested_message | sales-rep |

Phase 1: all handoffs **human_mediated**. Workforce Manager logs and recommends; does not auto-complete.

## Produces / Consumes

```yaml
produces:
  - artifact: routing_directive
    schema_ref: agents/workforce-manager/OUTPUT_SCHEMA.md#routing_recommendation
    consumer_agents: [customer-service, sales-rep, sales-manager, account-research, follow-up]
  - artifact: conflict_report
    schema_ref: agents/workforce-manager/OUTPUT_SCHEMA.md#conflict_alert
    consumer_agents: [customer-service, sales-rep, sales-manager, account-research, follow-up]
  - artifact: workforce_kpi_rollup
    schema_ref: agents/workforce-manager/OUTPUT_SCHEMA.md#kpi_rollup
    consumer_agents: []  # platform ops / admin UI
  - artifact: audit_summary
    schema_ref: agents/workforce-manager/OUTPUT_SCHEMA.md#audit_summary
    consumer_agents: []  # governance / platform ops
  - artifact: workload_balance_plan
    schema_ref: agents/workforce-manager/OUTPUT_SCHEMA.md#workload_balance_plan
    consumer_agents: [customer-service, sales-rep, sales-manager, account-research, follow-up]

consumes:
  - artifact: agent_output
    source_agent: customer-service
    trigger: audit_log_event
  - artifact: agent_output
    source_agent: sales-rep
    trigger: audit_log_event
  - artifact: agent_output
    source_agent: sales-manager
    trigger: audit_log_event
  - artifact: agent_output
    source_agent: account-research
    trigger: audit_log_event
  - artifact: agent_output
    source_agent: follow-up
    trigger: audit_log_event
  - artifact: escalation_event
    source_agent: customer-service
    trigger: decision_action_escalate
  - artifact: escalation_event
    source_agent: sales-rep
    trigger: decision_action_escalate
  - artifact: escalation_event
    source_agent: sales-manager
    trigger: decision_action_escalate
  - artifact: escalation_event
    source_agent: account-research
    trigger: decision_action_escalate
  - artifact: escalation_event
    source_agent: follow-up
    trigger: decision_action_escalate
  - artifact: account_brief
    source_agent: account-research
    trigger: handoff_initiated
  - artifact: case_summary
    source_agent: customer-service
    trigger: handoff_initiated
  - artifact: opportunity_summary
    source_agent: sales-rep
    trigger: handoff_initiated
  - artifact: pipeline_summary
    source_agent: sales-manager
    trigger: handoff_initiated
  - artifact: rep_coaching_items
    source_agent: sales-manager
    trigger: handoff_initiated
  - artifact: suggested_message
    source_agent: follow-up
    trigger: handoff_initiated

handoff_triggers:
  - event: employee_escalation
    target_agent: workforce-manager
    human_mediated: true
  - event: cross_agent_conflict_detected
    target_agent: workforce-manager
    human_mediated: true
  - event: handoff_stalled_beyond_sla
    target_agent: workforce-manager
    human_mediated: true
  - event: workload_threshold_exceeded
    target_agent: workforce-manager
    human_mediated: true
  - event: inbound_work_unclassified
    target_agent: workforce-manager
    human_mediated: true
  - event: routing_directive_issued
    target_agent: customer-service
    human_mediated: true
  - event: routing_directive_issued
    target_agent: sales-rep
    human_mediated: true
  - event: routing_directive_issued
    target_agent: sales-manager
    human_mediated: true
  - event: routing_directive_issued
    target_agent: account-research
    human_mediated: true
  - event: routing_directive_issued
    target_agent: follow-up
    human_mediated: true

human_mediated_phase_1: true
```

## Conflict Scenarios (Cross-Employee)

| Scenario | Mediation |
|----------|-----------|
| CS case_summary vs sales-rep opp context on same account | Surface both; recommend human account team review |
| account-research brief stale vs sales-rep active opp changes | Recommend refresh handoff to account-research |
| sales-manager coaching vs sales-rep next_best_action conflict | Defer to sales-manager hierarchy; flag in conflict_report |
| follow-up suggested_message vs sales-rep draft email | sales-rep owns send decision; follow-up supports |

```yaml
collaboration_version: "1.0.0"
implements: workforce-spec
managed_employees: [customer-service, sales-rep, sales-manager, account-research, follow-up]
handoff_mode_phase_1: human_mediated
```
