# Azure Infrastructure

## Scope

- Compute (Functions, Container Apps, App Service)
- Azure OpenAI deployment
- Azure SQL for long memory and audit
- Key Vault, Managed Identity, RBAC
- AI Search / vector storage
- Observability (App Insights, Log Analytics)

## Key Questions

- Single-tenant vs. multi-tenant Azure layout?
- Region and data residency requirements?
- Dev/staging/prod subscription strategy?

## Related

- [specifications/governance-spec.md](../../specifications/governance-spec.md)
- [runtime/SECURITY.md](../../runtime/SECURITY.md)
- [platform/observability.md](../../platform/observability.md)

## Decisions Pending

- Hosting model for runtime SDK
- SQL schema for memory tiers (see runtime/MEMORY_MODEL.md)
