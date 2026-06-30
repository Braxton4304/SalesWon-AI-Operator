# Testing & Deployment

## Scope

- Unit, integration, and agent evaluation tests
- QUALITY.md / METRICS.md automation
- CI/CD pipeline (GitHub Actions, Azure DevOps)
- Environment promotion (dev → staging → prod)

## Key Questions

- Golden datasets for agent eval?
- How to test ServiceNow integration without prod?
- Contract validation in CI (spec YAML/JSON blocks)?

## Related

- [specifications/agent-spec.md](../../specifications/agent-spec.md)
- [agents/_template/QUALITY.md](../../agents/_template/QUALITY.md)
- [docs/architecture/contract-evolution.md](../../docs/architecture/contract-evolution.md)

## Decisions Pending

- Eval harness design (OUTPUT_SCHEMA validation)
- Staging ServiceNow instance strategy
