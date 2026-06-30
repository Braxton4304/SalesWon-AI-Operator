# Technical Roadmap

Implements: [specifications/platform-spec.md](../specifications/platform-spec.md)

## Phase 1 — Operating System & Digital Workforce v1 (Current)

- [x] Platform scaffold (specs, runtime, platform, shared)
- [x] 7-spec architecture freeze (ADR-005)
- [x] `policies/` enterprise policy layer
- [x] Digital Workforce v1 — 5 employees × 22 files
- [x] Workforce Manager spec (Phase 2 runtime)
- [x] Shared playbooks + organizational memory
- [ ] Azure + ServiceNow stack ADRs
- [ ] Runtime SDK (Phase 2)

## Phase 2 — Runtime SDK

- Prompt builder (RUNTIME_CONTEXT)
- Decision engine + priority score calculator
- Workforce Manager orchestration
- ServiceNow connector
- Accountability learning loops (feedback → MEMORY_LONG)

## Phase 3 — Customer Deployment

- Layer 4 configuration per customer
- Phase 2 `execute` authority level (approved workflows)

## Digital Workforce v1 Status

| Component | Status |
|-----------|--------|
| customer-service | Complete (22 files) |
| sales-rep | Complete (22 files) |
| sales-manager | Complete (22 files) |
| account-research | Complete (22 files) |
| follow-up | Complete (22 files) |
| workforce-manager | Spec complete (22 files) |
