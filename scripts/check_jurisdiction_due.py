#!/usr/bin/env python3
"""Decide whether the jurisdiction agent's weekly refresh is due.

Jurisdiction runs on its own dedicated weekly cron, separate from the
daily cadence rota (see check_due.py) — it doesn't compete with other
agents for a slot. This just guards the manual workflow_dispatch path so
a manual trigger the day after a real run doesn't force an off-cycle
refresh: due if at least 6 days have passed since the last commit that
touched state/jurisdictions.json, or if it has no commit history yet.

Prints GitHub-Actions `key=value` output to stdout (`due`). Status
messages go to stderr.

Usage: scripts/check_jurisdiction_due.py
"""

import subprocess
import sys
from datetime import datetime, timezone

MIN_DAYS = 6


def git(*args):
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, check=True
    ).stdout.strip()


def main():
    last_date = git("log", "-1", "--format=%cI", "--", "state/jurisdictions.json")

    if not last_date:
        print("due=true")
        print("state/jurisdictions.json has no commit history yet, treating as due", file=sys.stderr)
        return

    last = datetime.fromisoformat(last_date)
    days_since = (datetime.now(timezone.utc) - last).days

    if days_since >= MIN_DAYS:
        print("due=true")
        print(f"{days_since} day(s) since last jurisdiction refresh", file=sys.stderr)
    else:
        print("due=false")
        print(f"only {days_since} day(s) since last refresh, skipped", file=sys.stderr)


if __name__ == "__main__":
    main()
