from __future__ import annotations
import os
import sys
import httpx

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_ANON_KEY")
if not url or not key:
    print("SUPABASE_URL and SUPABASE_ANON_KEY are required.")
    sys.exit(1)

response = httpx.get(
    f"{url.rstrip('/')}/rest/v1/",
    headers={"apikey": key, "Authorization": f"Bearer {key}"},
    timeout=10.0,
)
response.raise_for_status()
print("Supabase REST endpoint responded successfully.")
