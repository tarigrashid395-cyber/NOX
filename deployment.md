# NOX v1.0 — Deployment

## Required infrastructure
- Supabase project
- Upstash Redis database
- Qdrant Cloud or compatible Qdrant endpoint
- OpenRouter API access
- Container runtime for Docker deployment

## Deployment principles
1. Store secrets outside source control.
2. Validate provider connectivity before application startup.
3. Build backend and frontend images from their respective Dockerfiles.
4. Run health checks before exposing traffic.
5. Promote immutable builds through environments.
6. Keep database migrations versioned and reviewable.

## Local composition
`docker compose config` validates Compose syntax and interpolation.
`docker compose build` validates container builds when Docker is available.
