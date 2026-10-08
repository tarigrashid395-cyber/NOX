# NOX v1.0 — Operations

## Operational controls
- Structured logs
- Health/readiness checks
- Provider connectivity checks
- Database migration checks
- Queue/cache health
- Vector-store health
- Artifact lifecycle monitoring
- Security and dependency scanning

## Release gate
A production release requires passing backend tests, frontend build, end-to-end tests,
container validation, configuration validation, and provider-specific runtime checks.
