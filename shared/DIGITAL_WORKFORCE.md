# Digital Workforce

Implements: [specifications/workforce-spec.md](../specifications/workforce-spec.md)

Five **Digital Employees** + **Workforce Manager** (spec only) = SalesWon Digital Workforce v1.

## Organizational Chart

```text
                    [Workforce Manager — Phase 2 spec]
                              │
                    Sales Manager Agent
                              │
                    Sales Rep Agent
                              │
                    Follow-Up Agent

        Parallel: Customer Service Agent

        Supporting: Account Research Agent
                     (feeds Rep + Manager)
```

## Division of Labor

| Agent | Owns |
|-------|------|
| customer-service | Case triage, SLA, service communication drafts |
| sales-rep | Opportunity execution, discovery, rep coaching |
| sales-manager | Pipeline, forecast risk, rep coaching, exec briefs |
| account-research | Account briefs, relationship maps, buying signals |
| follow-up | Overdue activities, cadence, follow-up drafts |
| workforce-manager | Routing, conflict detection, workforce KPIs (spec) |

## Handoff Matrix

| Producer | Artifact | Consumer |
|----------|----------|----------|
| account-research | account_brief | sales-rep, sales-manager |
| customer-service | case_summary | sales-rep, account-research |
| sales-rep | opportunity_summary | sales-manager, follow-up |
| sales-manager | rep_coaching_items | sales-rep |
| sales-manager | pipeline_summary | follow-up |
| follow-up | suggested_message | sales-rep |

Phase 1: all handoffs **human-mediated**.

## Client Narrative

> These are not five disconnected chatbots. They are five governed members of a digital sales and service organization — accountable for outcomes, bounded by authority, operating inside the SalesWon AI Operating System.

```yaml
workforce_version: "1.0.0"
employees: [customer-service, sales-rep, sales-manager, account-research, follow-up]
manager: workforce-manager
handoff_mode: human_mediated
phase: 1
```
