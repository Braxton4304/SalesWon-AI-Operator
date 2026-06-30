# Reasoning Patterns

Implements: [runtime/DECISION_ENGINE.md](../../runtime/DECISION_ENGINE.md)

## Routing Evaluation Chain

```text
Inbound work / telemetry event
  → Step 1: Classify work type (classify_work_item)
  → Step 2: Match handoff matrix + employee division of labor
  → Step 3: Check target employee AUTHORITY + LIMITATIONS
  → Step 4: Assess employee capacity (query_workforce_telemetry)
  → Step 5: Compute routing confidence
  → Step 6: Escalate to human if ambiguous OR recommend route
```

## Conflict Detection Chain

```text
Audit events on shared record_id / account_id
  → Step 1: Group outputs by record within time window
  → Step 2: Compare decision_action + recommended_action payloads
  → Step 3: detect_conflicts — severity scoring
  → Step 4: Gather sources from both agents
  → Step 5: Confidence on conflict validity
  → Step 6: recommend mediation OR escalate if critical
```

## KPI Rollup Chain

```text
Scheduled or on-demand poll
  → Step 1: query_workforce_telemetry per employee
  → Step 2: Validate telemetry_freshness
  → Step 3: compute_workforce_kpis (aggregate + per-agent)
  → Step 4: Assign workforce_health label
  → Step 5: Flag anomalies vs thresholds
  → Step 6: answer (internal dashboard) OR recommend action if strained/critical
```

## Escalation Routing Chain

```text
Employee escalation event (decision_action: escalate)
  → Step 1: Parse employee ESCALATION.md trigger
  → Step 2: Match escalation-framework + Layer 4 contacts
  → Step 3: Check for cross-agent context (same record conflicts)
  → Step 4: Confidence on human role assignment
  → Step 5: recommend human_escalation with payload
```

## Workload Balance Chain

```text
Capacity threshold breach
  → Step 1: Identify overloaded + underloaded employees
  → Step 2: Classify deferrable vs urgent work in queue
  → Step 3: recommend_workload_balance
  → Step 4: request_approval if forced reroute required
  → Step 6: Escalate to human ops if all saturated
```

Each step maps to DECISION_ENGINE actions: retrieve → analyze → recommend → escalate.

```yaml
reasoning_patterns_version: "1.0.0"
chains: [routing_evaluation, conflict_detection, kpi_rollup, escalation_routing, workload_balance]
```
