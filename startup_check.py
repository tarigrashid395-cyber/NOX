from __future__ import annotations
import os
import sys

checks = {
    "SUPABASE_URL": os.getenv("SUPABASE_URL"),
    "UPSTASH_REDIS_REST_URL": os.getenv("UPSTASH_REDIS_REST_URL"),
    "QDRANT_URL": os.getenv("QDRANT_URL"),
    "OPENROUTER_API_KEY": os.getenv("OPENROUTER_API_KEY"),
}
missing = [name for name, value in checks.items() if not value]
if missing:
    print("Startup configuration incomplete:")
    for name in missing:
        print(f" - {name}")
    sys.exit(1)

print("NOX startup configuration check passed.")
