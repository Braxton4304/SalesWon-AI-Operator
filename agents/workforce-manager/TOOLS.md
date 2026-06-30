# Tools

## query_workforce_telemetry

Aggregate session counts, mean confidence, escalation rates, and latency per Digital Employee.

**Returns:** per-agent metrics keyed by `agent_id`

## query_audit_log

Filter agent decision events by time window, agent_id, decision_action, record_id, confidence range.

**Required for:** audit oversight, conflict evidence, KPI freshness validation

## query_handoff_queue

List pending produces/consumes per COLLABORATION.md contracts across all five employees.

**Phase 1:** human_mediated status only  
**Phase 2:** completion timestamps and retry counts

## classify_work_item

Map inbound work descriptor (artifact type, record type, urgency) to target employee per DIGITAL_WORKFORCE.

**Inputs:** work_type, record_refs, urgency, source_channel

## detect_conflicts

Compare agent outputs sharing record_id or account_id within time window; flag contradictions.

**Returns:** conflict_id, agents_involved, severity, source_refs

## compute_workforce_kpis

Roll up operational metrics from all employee METRICS.md definitions plus workforce-spec aggregates.

**Includes:** mean workforce confidence, cross-agent escalation rate, handoff completion rate

## recommend_routing

Produce routing directive with target agent_id or human role, rationale, and authority check result.

**Output:** draft_only until Phase 2 execute path approved

## recommend_workload_balance

Given capacity thresholds, propose defer/reroute plan across employees.

## query_organizational_memory

Read workforce-wide context per [shared/ORGANIZATIONAL_MEMORY.md](../../shared/ORGANIZATIONAL_MEMORY.md) — routing policies, terminology, approval matrix summary.

## Rules

1. query_audit_log before asserting conflict or violation
2. classify_work_item must check target employee LIMITATIONS.md
3. No tool invokes end-user-facing employee chat directly in Phase 1
4. KPI rollups label missing employee telemetry as `stale` or `unavailable`
5. recommend_routing never sets decision_action `execute` in Phase 1 spec

```yaml
tools_version: "1.0.0"
phase_1_execute: false
primary_domain: workforce_observability
```
