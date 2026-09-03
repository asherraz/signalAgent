#!/usr/bin/env python3
"""Decide whether artifacts/synthesis.md needs a refresh.

Compares the last commit that touched artifacts/synthesis.md against
every commit since then that touched anything else under artifacts/
(excluding synthesis.md itself and its dated trail in
artifacts/synthesis/, which synthesize writes on its own runs). Prints
GitHub-Actions `key=value` output to stdout (`due`) so a workflow step
can capture it via `>> "$GITHUB_OUTPUT"`. Status messages go to stderr.

Usage: scripts/check_synthesis_due.py
"""

import subprocess
import sys


def git(*args):
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, check=True
    ).stdout.strip()


def main():
    last = git("log", "-1", "--format=%H", "--", "artifacts/synthesis.md")

    if not last:
        print("due=true")
        print("synthesis.md has no commit history yet, treating as due", file=sys.stderr)
        return

    changed = git(
        "log",
        f"{last}..HEAD",
        "--oneline",
        "--",
        "artifacts/",
        ":!artifacts/synthesis.md",
        ":!artifacts/synthesis",
    )

    if changed:
        print("due=true")
        print(f"artifacts changed since last synthesis ({last[:8]})", file=sys.stderr)
    else:
        print("due=false")
        print("nothing new to synthesize, skipped", file=sys.stderr)


if __name__ == "__main__":
    main()
