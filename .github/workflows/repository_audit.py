from __future__ import annotations
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
required = [
    "backend/app", "frontend/src", "tests", "scripts", "docs", ".github/workflows",
    "docker-compose.yml", "README.md", ".env.example"
]
missing = [item for item in required if not (root / item).exists()]
archives = list(root.rglob("*.zip"))

if missing:
    print("Missing required paths:")
    for item in missing:
        print(f" - {item}")
    sys.exit(1)

if archives:
    print("Archives inside repository:")
    for archive in archives:
        print(f" - {archive.relative_to(root)}")
    sys.exit(1)

print("Repository foundation audit passed.")
