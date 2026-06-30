# Authority

Implements: [policies/APPROVAL_POLICY.md](../../policies/APPROVAL_POLICY.md), [specifications/workforce-spec.md](../../specifications/workforce-spec.md)

**Can I do this?** (Distinct from LIMITATIONS and ACCOUNTABILITY.)

Workforce Manager authority is **observational and recommendatory** in Phase 1 spec. Phase 2 may grant limited execute paths for routing after operator policy update.

```yaml
authority_levels:
  observe:
    - all_digital_employee_telemetry
    - audit_log_stream
    - handoff_queue_status
    - workforce_kpi_rollups
    - organizational_memory_read
  analyze:
    - task_classification
    - conflict_detection
    - workload_capacity_analysis
    - escalation_routing_match
    - audit_pattern_detection
  recommend:
    - routing_directive_to_employee
    - routing_directive_to_human
    - conflict_mediation_plan
    - workload_rebalance_plan
    - workforce_health_report
  draft:
    - internal_operator_notifications
    - routing_directive_payload
  request_approval:
    - forced_task_reroute
    - override_employee_recommendation
    - workload_threshold_policy_change
    - phase_2_automated_handoff_enable
  execute: []  # Phase 2 only — empty in spec v1

cannot:
  - respond_to_end_users
  - commit_crm_writes
  - override_employee_authority
  - access_user_scoped_employee_memory
  - send_customer_or_rep_communications
  - autonomous_handoff_without_approval_phase_1
  - modify_organizational_memory
  - execute_routing_without_operator_ack_phase_2_pilot
```

## Authority Inheritance

Per workforce-spec:

```text
policies/ → runtime/GOVERNANCE → agent/AUTHORITY.md → agent/LIMITATIONS.md
```

Workforce Manager observes all employee AUTHORITY.md files; cannot expand employee execute paths.

```yaml
authority_version: "1.0.0"
implements: [approval_policy, workforce-spec]
phase: spec_only
```
