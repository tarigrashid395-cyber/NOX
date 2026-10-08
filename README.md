# NOX v1.0

NOX is a production-oriented AI Operating System foundation for multi-agent intelligence,
persistent semantic memory, autonomous research, workforce routing, execution workflows,
missions, workspaces, and durable artifacts.

## Repository Structure

```text
backend/       FastAPI domain and provider boundary
frontend/      Next.js web application
tests/         Unit, integration, E2E, performance, security
scripts/       Environment and repository validation
docs/          Architecture and operations documentation
.github/       CI/CD workflows
docker-compose.yml
.env.example
```

## Architecture

```text
Next.js
   |
FastAPI API
   |
   +-- Supervisor / Planner / Reviewer
   +-- Research / Memory / Workforce
   +-- Execution / Missions / Workspaces / Artifacts
   |
   +-- Supabase / PostgreSQL
   +-- Qdrant
   +-- Upstash Redis
   +-- OpenRouter / OpenAI-compatible models
```

## Installation

1. Copy `.env.example` to `.env`.
2. Populate secrets from the actual managed services.
3. Install backend dependencies:
   `pip install -r backend/requirements.txt`
4. Install frontend dependencies:
   `cd frontend && npm install`
5. Validate the repository:
   `python scripts/repository_audit.py`

## Deployment

Docker images are defined independently for backend and frontend.
Docker Compose provides the local orchestration boundary and health checks.

Production deployments must supply real managed-service credentials and must pass the
repository's CI, security, container, and provider-runtime validation gates.

## Environment Variables

The committed `.env.example` contains only the requested NOX provider variables and no
real credentials. Never commit `.env`.

## Development Workflow

- Keep domain logic isolated by bounded context.
- Add schemas, services, repositories, provider contracts, tests, and documentation together.
- Do not introduce demo implementations into production modules.
- Run backend tests and frontend builds before opening a production pull request.
- Use Playwright for browser-level validation.
- Treat provider connectivity as a runtime concern and validate it with real credentials.

## Quality Gate

A production release is not implied by repository creation. Release status must be based
on executed evidence from tests, builds, container validation, security checks, and live
provider connectivity.
