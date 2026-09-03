#!/usr/bin/env python3
"""Decide whether any cadence agent is overdue, and if so, which one.

Reads each agent's cadence from artifacts/rota.json and its last-run date
from the newest dated heading in state/<name>.md. Prints GitHub-Actions
`key=value` output lines to stdout (`due` and, when due, `agent`) so a
workflow step can capture them via `>> "$GITHUB_OUTPUT"`. Status messages
go to stderr so they show up in the job log without polluting the
captured output.

Usage: scripts/check_due.py
"""

import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROTA_PATH = ROOT / "artifacts" / "rota.json"
STATE_DIR = ROOT / "state"

CADENCE_DAYS = {"weekly": 7, "fortnightly": 14, "monthly": 30}
NEVER_RUN = 10**6  # sorts before any real overdue-by value

DATE_RE = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2})\b", re.MULTILINE)


def cadence_days(schedule):
    schedule = (schedule or "").lower()
    for key, days in CADENCE_DAYS.items():
        if key in schedule:
            return days
    return None  # not a cadence agent (e.g. challenge, synthesize)


def last_run_date(name):
    path = STATE_DIR / f"{name}.md"
    if not path.exists():
        return None
    match = DATE_RE.search(path.read_text())
    if not match:
        return None
    return datetime.strptime(match.group(1), "%Y-%m-%d").date()


def main():
    today = date.today()
    rota = json.loads(ROTA_PATH.read_text())

    due = []
    for entry in rota:
        days = cadence_days(entry.get("schedule"))
        if days is None:
            continue
        name = entry["name"]
        last = last_run_date(name)
        if last is None:
            due.append((NEVER_RUN, name))
            continue
        days_since = (today - last).days
        if days_since < days:
            continue
        due.append((days_since - days, name))

    if not due:
        print("due=false")
        print("nothing due, skipped", file=sys.stderr)
        return

    due.sort(key=lambda pair: (-pair[0], pair[1]))
    chosen = due[0][1]
    print("due=true")
    print(f"agent={chosen}")
    print(f"picked {chosen} as most overdue ({len(due)} agent(s) due)", file=sys.stderr)


if __name__ == "__main__":
    main()
