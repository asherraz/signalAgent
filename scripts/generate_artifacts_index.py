#!/usr/bin/env python3
"""Regenerate artifacts/index.json from frontmatter in artifacts/*.md.

Usage: scripts/generate_artifacts_index.py
"""

import json
import re
import sys
from pathlib import Path

ARTIFACTS_DIR = Path(__file__).resolve().parent.parent / "artifacts"
INDEX_PATH = ARTIFACTS_DIR / "index.json"
FIELDS = ["slug", "title", "description", "updated", "status"]

# Paths relative to ARTIFACTS_DIR excluded from the index regardless of
# frontmatter. Two different reasons live in one set:
# - japan-asset-longlist.md, dossiers: private working documents that must
#   never reach the published index.
# - synthesis: dated snapshots (synthesis/YYYY-MM-DD.md) are a trail, not
#   separate artifacts — only the current artifacts/synthesis.md itself
#   (a sibling file, not under this directory, so unaffected by this
#   exclusion) belongs in the index.
EXCLUDE = {
    "japan-asset-longlist.md",
    "dossiers",
    "synthesis",
}

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def is_excluded(path):
    relative = path.relative_to(ARTIFACTS_DIR)
    return relative.parts[0] in EXCLUDE


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

    for path in sorted(ARTIFACTS_DIR.rglob("*.md")):
        if is_excluded(path):
            continue
        text = path.read_text()
        fields = parse_frontmatter(text)
        if fields is None:
            missing.append(path.relative_to(ARTIFACTS_DIR).as_posix())
            continue

        entry = {"file": path.relative_to(ARTIFACTS_DIR).as_posix()}
        for field in FIELDS:
            entry[field] = fields.get(field, "")
        entries.append(entry)

    if missing:
        print(
            "warning: skipped files with no frontmatter: " + ", ".join(missing),
            file=sys.stderr,
        )

    INDEX_PATH.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {len(entries)} entries to {INDEX_PATH}")


if __name__ == "__main__":
    main()
