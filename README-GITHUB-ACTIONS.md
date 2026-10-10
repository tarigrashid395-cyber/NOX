# NOX GitHub Actions files

## Files
- `.github/workflows/ci.yml`: routine CI for pull requests and pushes. It does not require API keys or cloud secrets.
- `.github/workflows/staging-runtime-validation.yml`: optional manual validation against configured external staging services. It requires GitHub Actions secrets and should use staging credentials only.

## Install
Copy the two files into the same paths in the repository, then commit and push them.

## CI secrets
No custom GitHub secrets are required for `ci.yml`. GitHub supplies `GITHUB_TOKEN` automatically; this workflow only needs read access to repository contents.

## Optional staging secrets
Configure these only if you intend to run `staging-runtime-validation.yml`:
- `SUPABASE_URL`
- `SUPABASE_ANON_KEY`
- `DATABASE_URL`
- `UPSTASH_REDIS_REST_URL`
- `UPSTASH_REDIS_REST_TOKEN`
- `QDRANT_URL`
- `QDRANT_API_KEY`
- `SUPABASE_SERVICE_ROLE_KEY` is passed through but is not part of the required-secret preflight; do not add it unless the validator genuinely requires it. If needed, use a dedicated staging key with minimal scope.

Do not put secrets in source files, workflow literals, artifacts, logs, or `NEXT_PUBLIC_*` variables.

## Important limitation from the supplied archive
The existing `frontend/package-lock.json` has only the root package entry and is not a complete dependency lockfile. The CI file temporarily uses `npm install` so dependency resolution can happen on the runner. For deterministic CI, regenerate and commit a full lockfile locally, then change both frontend install steps from `npm install --no-audit --no-fund` to `npm ci`.

The workflow files are prepared against the uploaded `NOX_v1_0_REMEDIATED.zip` structure, but a successful GitHub run has not been performed here. Build, tests, and service compatibility must be confirmed by the Actions run.
