# Agents — SalesWon Digital Workforce v1

Implements: [specifications/agent-spec.md](../specifications/agent-spec.md), [specifications/workforce-spec.md](../specifications/workforce-spec.md), [specifications/accountability-spec.md](../specifications/accountability-spec.md)

Five **Digital Employees** + **Workforce Manager** (spec only). See [shared/DIGITAL_WORKFORCE.md](../shared/DIGITAL_WORKFORCE.md).

## Digital Employees (Phase 1 — Reactive)

| Agent | Division of labor | Primary produces |
|-------|-------------------|------------------|
| [customer-service](customer-service/AGENT.md) | Case triage, SLA, service drafts | case_summary |
| [sales-rep](sales-rep/AGENT.md) | Opportunity execution, discovery | opportunity_summary |
| [sales-manager](sales-manager/AGENT.md) | Pipeline, forecast, coaching | pipeline_summary |
| [account-research](account-research/AGENT.md) | Account intelligence, briefs | account_brief |
| [follow-up](follow-up/AGENT.md) | Overdue activities, cadence | suggested_message |

## Workforce Manager (Spec Only — Phase 2)

| Agent | Role |
|-------|------|
| [workforce-manager](workforce-manager/AGENT.md) | Routing, conflict detection, workforce KPIs — **does not answer users** |

## 22-File Contract (Every Digital Employee)

AGENT, IDENTITY, MISSION, CAPABILITIES, LIMITATIONS, BEHAVIOR, DECISION_MODEL, TOOLS, MEMORY_SHORT, MEMORY_LONG, PROMPTS, OUTPUT_SCHEMA, QUALITY, METRICS, ESCALATION, **AUTHORITY**, **ACCOUNTABILITY**, **COLLABORATION**, **REASONING_PATTERNS**, **TRUST_MODEL**, **EXPLAINABILITY**, **BUSINESS_OBJECTIVES**

| File | Question |
|------|----------|
| AUTHORITY.md | Can I do this? |
| ACCOUNTABILITY.md | Am I succeeding? |
| COLLABORATION.md | Who do I work with? |

## Handoffs (Phase 1: Human-Mediated)

Account Research → Sales Rep/Manager (account_brief)  
Customer Service → Sales Rep/Research (case_summary)  
Sales Rep → Manager/Follow-Up (opportunity_summary)  
Sales Manager → Sales Rep (coaching)

## Template

Copy [_template/](_template/) for new roles. Architecture **frozen** — new roles require ADR.

```powershell
Copy-Item -Recurse agents\_template agents\your-agent-name
```

## Import Contract

```text
policies/ + shared/ + runtime/ + platform/ + agent/ + Layer 4 + CRM
```
