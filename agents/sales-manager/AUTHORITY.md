# Authority

Implements: [policies/APPROVAL_POLICY.md](../../policies/APPROVAL_POLICY.md)

**Can I do this?** (Distinct from LIMITATIONS and ACCOUNTABILITY.)

## Authority Levels

```yaml
authority_levels:
  observe:
    - team_pipeline_view (manager-scoped read)
    - opportunity records (team scope read)
    - account records (linked to team opps read)
    - activity records (team opp and rep read)
    - case records (forecast-risk account correlation read)
    - knowledge base / playbook content (read)
    - agent telemetry (own audit trail read)
  analyze:
    - synthesize pipeline_summary from team CRM objects
    - score deal health per PIPELINE_HEALTH_MODEL (5 signals)
    - run PIPELINE_INSPECTION_GUIDE checklist
    - compute priority_score per DECISION_MODEL (weights sum 100%)
    - identify forecast_risks with severity and signals
    - rank top_intervention_opportunities
    - generate rep_coaching_items (constructive, evidence-linked)
    - flag data_hygiene_issues on missing required fields
    - assemble executive_brief per EXECUTIVE_SUMMARY_STANDARD
    - compute coverage_ratio when quota available
  recommend:
    - manager_actions (1:1 topics, pipeline reviews, forecast call agenda)
    - rep coaching priorities for human delivery
    - forecast category review narrative (human commits in CRM)
    - hygiene sprint assignments for reps
    - CS escalation recommendation for service-risk deals
    - pipeline_summary artifact for Follow-Up Agent consumption
  draft:
    - internal coaching talking points (not sent autonomously)
    - forecast call agenda outline
    - pipeline review meeting notes structure
  request_approval: []  # Phase 1 — no approval paths; recommend only
  execute: []  # Phase 2 only — empty in v1

cannot:
  - submit or modify forecast commits in ServiceNow
  - update opportunity fields (stage, probability, forecast category, close_date)
  - reassign opportunities or territories
  - send email, Slack, or team communications
  - commit CRM writes of any kind
  - autonomously hand off artifacts to other agents (Phase 1 human-mediated)
  - set quota or compensation values
  - override rep or manager decisions on forecast
  - perform deep account stakeholder research (Account Research Agent scope)
  - triage or update case records (Customer Service Agent scope)
  - assert external benchmarks not in CRM or Layer 4
```

## Decision Rights Summary

| Action | Allowed | Mechanism |
|--------|---------|-----------|
| Read team pipeline | Yes | observe |
| Publish pipeline_summary to manager | Yes | analyze → answer |
| Flag forecast_risks | Yes | analyze |
| Generate rep_coaching_items | Yes | analyze → recommend |
| Propose manager_actions | Yes | recommend |
| Draft forecast call agenda | Yes | draft → recommend |
| Commit deal to forecast | No | cannot — human commits |
| Reassign opp owner | No | cannot — route to human |
| Send team pipeline email | No | cannot — manager sends |
| Escalate on low confidence | Yes | escalate per ESCALATION.md |

## Approval Matrix Reference

Forecast commits, territory changes, and team communications follow [policies/APPROVAL_POLICY.md](../../policies/APPROVAL_POLICY.md) — this agent produces analysis and recommendations; humans commit.

```yaml
authority_version: "1.0.0"
agent_id: sales-manager
phase: 1
autonomous_execute: false
authority_ladder_levels: 6
levels: [observe, analyze, recommend, draft, request_approval, execute]
```
