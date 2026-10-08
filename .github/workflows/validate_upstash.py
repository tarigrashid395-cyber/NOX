from __future__ import annotations
import os
import sys
import httpx

url = os.getenv("UPSTASH_REDIS_REST_URL")
token = os.getenv("UPSTASH_REDIS_REST_TOKEN")
if not url or not token:
    print("UPSTASH_REDIS_REST_URL and UPSTASH_REDIS_REST_TOKEN are required.")
    sys.exit(1)

response = httpx.post(
    url.rstrip("/") + "/ping",
    headers={"Authorization": f"Bearer {token}"},
    timeout=10.0,
)
response.raise_for_status()
print("Upstash Redis REST endpoint responded successfully.")
