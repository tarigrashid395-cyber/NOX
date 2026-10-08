from __future__ import annotations
import os
import sys

REQUIRED = (
    "SUPABASE_URL", "SUPABASE_ANON_KEY", "SUPABASE_SERVICE_ROLE_KEY",
    "UPSTASH_REDIS_REST_URL", "UPSTASH_REDIS_REST_TOKEN",
    "QDRANT_URL", "QDRANT_API_KEY", "OPENROUTER_API_KEY"
)

missing = [name for name in REQUIRED if not os.getenv(name)]
if missing:
    print("Missing required environment variables:")
    for name in missing:
        print(f" - {name}")
    sys.exit(1)

print("Environment variables required by NOX are present.")
