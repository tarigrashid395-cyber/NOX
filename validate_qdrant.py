from __future__ import annotations
import os
import sys
import httpx

url = os.getenv("QDRANT_URL")
api_key = os.getenv("QDRANT_API_KEY")
if not url or not api_key:
    print("QDRANT_URL and QDRANT_API_KEY are required.")
    sys.exit(1)

response = httpx.get(
    f"{url.rstrip('/')}/healthz",
    headers={"api-key": api_key},
    timeout=10.0,
)
response.raise_for_status()
print("Qdrant health endpoint responded successfully.")
