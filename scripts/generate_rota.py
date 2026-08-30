#!/usr/bin/env python3
"""Regenerate artifacts/rota.json from frontmatter in agents/*.md.

Usage: scripts/generate_rota.py
"""

import json
import re
import sys
from pathlib import Path

AGENTS_DIR = Path(__file__).resolve().parent.parent / "agents"
ROTA_PATH = AGENTS_DIR.parent / "artifacts" / "rota.json"
FIELDS = ["name", "description", "schedule", "domain"]

# Not an agent brief.
EXCLUDE = {"README.md"}

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(text):
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    fields = {}
    for line in match.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def main():
    entries = []
    missing = []

    for path in sorted(AGENTS_DIR.glob("*.md")):
        if path.name in EXCLUDE:
            continue
        text = path.read_text()
        fields = parse_frontmatter(text)
        if fields is None:
            missing.append(path.name)
            continue

        entry = {"file": path.name}
        for field in FIELDS:
            entry[field] = fields.get(field, "")
        entry["private"] = fields.get("private", "false").lower() == "true"
        entries.append(entry)

    if missing:
        print(
            "warning: skipped files with no frontmatter: " + ", ".join(missing),
            file=sys.stderr,
        )

    ROTA_PATH.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {len(entries)} entries to {ROTA_PATH}")


if __name__ == "__main__":
    main()
