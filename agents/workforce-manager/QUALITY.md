# Quality

## Correctness

- [ ] Routing target matches DIGITAL_WORKFORCE division of labor and handoff matrix
- [ ] affected_agents lists only valid employee agent_ids
- [ ] KPI values sourced from employee telemetry or audit — not invented
- [ ] Conflict alerts cite sources from both involved agents
- [ ] Authority check references target employee AUTHORITY.md outcome

## Completeness

- [ ] workforce_health label supported by per-agent capacity and confidence data
- [ ] kpi_rollup includes telemetry_freshness per employee
- [ ] routing_recommendation includes rationale and human_mediated flag
- [ ] Escalation routing names human role from Layer 4 or escalation-framework

## Scope Compliance

- [ ] Summary text is operator-facing — no customer/rep coaching language
- [ ] No domain answers that belong to employee agents
- [ ] Phase 1 outputs marked recommend-only; no execute claims

## Hallucination Avoidance

- [ ] No CRM facts unless present in audit sources
- [ ] Missing telemetry explicitly labeled stale or unavailable

## Demo Scenarios (Phase 2 Spec Validation)

1. Healthy workforce KPI rollup — all employees within capacity
2. Routing recommendation — account_brief request → account-research
3. Conflict detection — contradictory opp updates from sales-rep and follow-up
4. Workload rebalance — follow-up overloaded → defer plan
5. Employee escalation → human manager routing suggestion
6. Audit summary — refuse and sub-confidence cluster by agent

```yaml
quality_version: "1.0.0"
```
