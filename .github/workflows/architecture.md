# NOX v1.0 — Architecture

## Purpose
NOX is structured as an AI Operating System with a modular API layer, agent orchestration,
persistent memory, research, workforce capabilities, autonomous execution, and a web client.

## Bounded contexts
- Agents: Supervisor, Planner, Reviewer and agent coordination.
- Memory: persistent, permission-aware semantic memory.
- Research: evidence-oriented research workflows.
- Workforce: specialist agents and skill routing.
- Execution: tasks, scheduling, retries and execution state.
- Missions: long-running objectives composed of tasks.
- Workspaces: isolated user/project working contexts.
- Artifacts: durable outputs and references.
- Providers: external AI, vector, database and cache integrations.

## Infrastructure
FastAPI serves the application API. Supabase provides managed PostgreSQL/backend services.
Qdrant provides vector retrieval. Upstash Redis provides managed Redis access. Next.js
provides the web application. Docker supplies reproducible local/container packaging.
