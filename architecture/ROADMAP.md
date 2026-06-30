# Technical Roadmap

**Status:** Phase 1 — Specification and scaffold (this repo)

Implements: [specifications/platform-spec.md](../specifications/platform-spec.md)

## Phase 1 — Specification & Scaffold (Current)

- [x] `/specifications` contract layer
- [x] Runtime, agent, platform, shared folder structure
- [x] Agent template with OUTPUT_SCHEMA
- [ ] Architecture decisions for Azure + ServiceNow stack
- [ ] First production agent (TBD: Customer Service or Sales Rep)

## Phase 2 — Runtime SDK (Planned)

- Prompt builder (RUNTIME_CONTEXT assembly)
- Decision engine implementation
- Memory engine (short + long, Azure SQL)
- Governance middleware (audit, confidence, escalation)
- ServiceNow connector

## Phase 3 — Agent Deployment (Planned)

- Customer Service Agent
- Sales Rep Agent
- Sales Manager Agent

## Phase 4 — Customer Layer (Planned)

- Layer 4 configuration per deployment
- ServiceNow instance mapping
- Stage definitions, approval rules, escalation contacts

## Decisions Pending

| Decision | Options | Target |
|----------|---------|--------|
| Primary LLM provider | Azure OpenAI, Anthropic via Azure | TBD |
| Vector store | Azure AI Search, pgvector | TBD |
| App hosting | Azure Functions, Container Apps | TBD |
| Frontend framework | Next.js, React SPA | TBD |

Record decisions in [DECISIONS.md](DECISIONS.md).
