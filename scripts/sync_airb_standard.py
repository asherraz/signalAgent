#!/usr/bin/env python3
"""Regenerate state/aiRB.json's "standard" key from artifacts/signal-standard.md.

artifacts/signal-standard.md is re-scored on every disclosure-audit run (see
agents/disclosure-audit.md). state/aiRB.json carries a copy of its title,
version, date, intro, audit headline, and eleven fields for the aiRB page to
read without depending on markdown parsing at request time. This script is
the re-sync step: run it after any disclosure-audit run that touches
signal-standard.md, so the copy doesn't silently drift.

Leaves aiRB.json's "board" and "reviews" keys untouched. Prints a summary of
what changed (or "no change") to stdout.

Usage: scripts/sync_airb_standard.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STANDARD_PATH = ROOT / "artifacts" / "signal-standard.md"
AIRB_PATH = ROOT / "state" / "aiRB.json"

TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
VERSION_RE = re.compile(r"\*\*(v\d+)\*\*\s+—\s+(\d{4}-\d{2}-\d{2})")
FIELD_HEADING_RE = re.compile(r"^###\s+(\d+)\.\s+(.+?)\s*$", re.MULTILINE)
WHAT_IT_IS_RE = re.compile(r"^\*\*What it is:\*\*\s*(.+?)\s*$", re.MULTILINE)
ABSENCE_RE = re.compile(r"^\*\*What its absence means:\*\*\s*(.+?)\s*$", re.MULTILINE)
TIER_ITEM_RE = re.compile(r"^-\s+Field\s+(\d+)\b")


def section(text, heading, next_headings):
    """Text of the section starting at `## {heading}` up to the next heading
    at the same or higher level found in `next_headings` (or end of file)."""
    start_match = re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.MULTILINE)
    if not start_match:
        raise ValueError(f"section {heading!r} not found in {STANDARD_PATH}")
    start = start_match.end()
    end = len(text)
    for other in next_headings:
        m = re.search(rf"^##\s+{re.escape(other)}\s*$", text[start:], re.MULTILINE)
        if m:
            end = min(end, start + m.start())
    return text[start:end]


def parse_tiers(tiers_section):
    tier_of = {}
    current_tier = None
    for line in tiers_section.splitlines():
        stripped = line.strip()
        if stripped.startswith("**Minimum disclosure**"):
            current_tier = "minimum"
        elif stripped.startswith("**Complete disclosure**"):
            current_tier = "complete"
        else:
            m = TIER_ITEM_RE.match(stripped)
            if m and current_tier:
                tier_of[int(m.group(1))] = current_tier
    return tier_of


def parse_fields(fields_section, tier_of):
    headings = list(FIELD_HEADING_RE.finditer(fields_section))
    fields = []
    for i, m in enumerate(headings):
        n = int(m.group(1))
        name = m.group(2).strip()
        block_start = m.end()
        block_end = headings[i + 1].start() if i + 1 < len(headings) else len(fields_section)
        block = fields_section[block_start:block_end]

        what_it_is = WHAT_IT_IS_RE.search(block)
        absence = ABSENCE_RE.search(block)
        if not what_it_is or not absence:
            raise ValueError(f"field {n} ({name!r}) missing 'What it is' or 'What its absence means'")
        if n not in tier_of:
            raise ValueError(f"field {n} ({name!r}) has no tier assignment in the Tiers section")

        fields.append({
            "n": n,
            "name": name,
            "tier": tier_of[n],
            "definition": what_it_is.group(1),
            "absence_means": absence.group(1),
        })
    return fields


def parse_audit_headline(compliance_section):
    m = re.search(r"^\*\*(.+?)\*\*", compliance_section, re.MULTILINE)
    if not m:
        raise ValueError("no bold audit headline found in the Compliance table section")
    return m.group(1)


def build_standard():
    text = STANDARD_PATH.read_text()

    title_match = TITLE_RE.search(text)
    if not title_match:
        raise ValueError("no H1 title found")
    title = title_match.group(1)

    what_this_is = section(text, "What this is", ["The fields"])
    intro = what_this_is.strip().split("\n\n")[0].replace("\n", " ").strip()

    version_match = VERSION_RE.search(section(text, "Version and date", []))
    if not version_match:
        raise ValueError("no version/date line found in the Version and date section")
    version, date = version_match.group(1), version_match.group(2)

    compliance = section(text, "Compliance table", ["This table will be re-scored", "Version and date"])
    audit_headline = parse_audit_headline(compliance)

    tier_of = parse_tiers(section(text, "Tiers", ["How to use it"]))
    fields = parse_fields(section(text, "The fields", ["Tiers"]), tier_of)

    if len(fields) != 11:
        raise ValueError(f"expected 11 fields, found {len(fields)}")

    return {
        "version": version,
        "date": date,
        "title": title,
        "intro": intro,
        "audit_headline": audit_headline,
        "fields": fields,
    }


def main():
    new_standard = build_standard()

    aiRB = json.loads(AIRB_PATH.read_text())
    old_standard = aiRB.get("standard")

    if old_standard == new_standard:
        print("no change — state/aiRB.json's \"standard\" key already matches artifacts/signal-standard.md")
        return

    aiRB["standard"] = new_standard
    AIRB_PATH.write_text(json.dumps(aiRB, indent=2, ensure_ascii=False) + "\n")

    if old_standard is None:
        print("wrote a new \"standard\" key to state/aiRB.json")
    else:
        old_fields = {f["n"]: f for f in old_standard.get("fields", [])}
        new_fields = {f["n"]: f for f in new_standard["fields"]}
        changed_fields = [n for n in new_fields if old_fields.get(n) != new_fields[n]]
        print("updated state/aiRB.json's \"standard\" key:")
        for key in ("version", "date", "title", "intro", "audit_headline"):
            if old_standard.get(key) != new_standard[key]:
                print(f"  {key}: {old_standard.get(key)!r} -> {new_standard[key]!r}")
        if changed_fields:
            print(f"  fields changed: {sorted(changed_fields)}")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
