#!/usr/bin/env python3
"""Regenerate artifacts/index.json from frontmatter in artifacts/*.md.

Also appends fixed entries for structured state/ files that carry no
frontmatter of their own but are registered in the index by operator
instruction — currently the jurisdiction agent's state/jurisdictions.json
and state/changelog.json (see agents/jurisdiction.md). Their "updated"
field is computed from the file's own content, not hardcoded, so it stays
accurate as those files change; everything else about them is static.

Usage: scripts/generate_artifacts_index.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTIFACTS_DIR = ROOT / "artifacts"
STATE_DIR = ROOT / "state"
INDEX_PATH = ARTIFACTS_DIR / "index.json"
FIELDS = ["slug", "title", "description", "updated", "status"]

EXTRA_ENTRIES = [
    {
        "file": "../state/jurisdictions.json",
        "slug": "jurisdictions",
        "title": "Jurisdictions",
        "description": "Structured jurisdiction-by-jurisdiction legal status for intranasal exosome products — classification, legal basis, permitted/grey/prohibited lists, cell-source rules, enforcement, and route-in, one record per jurisdiction.",
        "status": "standing",
        "updated_from": ("jurisdictions", "last_verified"),
    },
    {
        "file": "../state/changelog.json",
        "slug": "jurisdictions-changelog",
        "title": "Jurisdictions Changelog",
        "description": "Append-only log of every field-level change to state/jurisdictions.json, newest first — date, jurisdiction, field, old value, new value, source URL, and whether the change was material (a verdict change).",
        "status": "standing",
        "updated_from": ("changelog", "date"),
    },
]

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


def newest_value(state_filename, key):
    """Latest value of `key` across a state/*.json array, or '' if absent/empty."""
    path = STATE_DIR / f"{state_filename}.json"
    if not path.exists():
        return ""
    try:
        records = json.loads(path.read_text())
    except json.JSONDecodeError:
        return ""
    values = [r.get(key, "") for r in records if isinstance(r, dict) and r.get(key)]
    return max(values) if values else ""


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

    for extra in EXTRA_ENTRIES:
        state_filename, key = extra["updated_from"]
        entry = {
            "file": extra["file"],
            "slug": extra["slug"],
            "title": extra["title"],
            "description": extra["description"],
            "updated": newest_value(state_filename, key),
            "status": extra["status"],
        }
        entries.append(entry)

    INDEX_PATH.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {len(entries)} entries to {INDEX_PATH}")


if __name__ == "__main__":
    main()
