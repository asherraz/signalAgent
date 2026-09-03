# Agent brief format

Each file in this directory is one agent's job description. An agent reads
its own brief to know who it is, then reads its state file in
[`../state/`](../state/) to know what it already found, before doing any
work.

## Format

```markdown
---
name: agent-slug
description: One-line summary of what this agent is responsible for.
schedule: How often / when this agent runs, e.g. "daily" or "on new data"
---

## What it reads

- Inputs this agent needs before it can run: state files, artifacts from
  other agents, external sources.

## What it produces

- The artifact(s) or post(s) this agent is responsible for creating or
  updating, and where they go.

## Rules

- Constraints, tone, scope boundaries, and anything the agent must never
  do (e.g. never publish without human review, never claim results not
  in the source data).
```

## Conventions

- `name` matches the filename (without `.md`) and the corresponding state
  file in `state/<name>.md`.
- Keep briefs short enough to read in one pass — if an agent needs a long
  reference doc, put that doc in `artifacts/` and link to it.
- Update a brief when an agent's job changes; the commit history of the
  brief itself is part of the development record.

## Rota

The scheduled workflow ([`.github/workflows/agents.yml`](../.github/workflows/agents.yml))
runs Monday/Wednesday/Friday at 06:00 UTC, plus on manual dispatch. Each
run is capped to a single cadence agent, to keep per-run cost down:

1. Before invoking Claude at all, [`scripts/check_due.py`](../scripts/check_due.py)
   reads every agent's cadence from `artifacts/rota.json` and its
   last-run date from the newest dated heading in `state/<name>.md`, and
   picks whichever due agent is most overdue relative to its own
   cadence. An agent with no state file yet counts as maximally overdue.
2. If nothing is due, the run stops there — no Claude invocation, no
   cost, just a "nothing due, skipped" log line.
3. Otherwise the picked agent's brief runs in full — reads its state,
   does the work, and commits, or commits nothing if there was nothing
   material to add — capped at 30 turns.
4. If that run changed a file in `artifacts/`, the [challenge](challenge.md)
   agent runs once against that one artifact, then the workflow stops.
   `synthesize` is not part of this automatic run; run it manually
   (`workflow_dispatch` with its own prompt, or locally) when the
   standing summary needs updating.

There is no per-weekday agent assignment anymore — the schedule just
picks the single most-overdue agent among all agents whose `schedule`
field says they're due, every time it runs. Fortnightly and monthly
agents are simply not due, and get skipped over, until their cadence
elapses. A skipped slot means no commit — silence is a valid outcome and
is preferable to a run that manufactures a finding to justify itself.

## Rules that apply to every agent

- Primary sources only. A summary is a pointer, never a substitute.
- Regenerate `artifacts/index.json` in the same commit as any artifact change.
- Record uncertainty as uncertainty. Never resolve an ambiguity in Signal's favour.
- Conflicts between an artifact and Signal's public materials go in a
  `## Conflicts` section at the top of that artifact, unsoftened.
- Input-status and provenance notes go at the bottom of an artifact,
  under a `## Provenance` heading — never at the top. The document leads
  with its content. (This does not change where `## Conflicts` goes —
  that stays at the top.)
- Post drafts are category-level only. Never draft a post that names or
  implies Signal's own regulatory, commercial, or supplier position.
- Nothing confidential in the repo. Quotes, pricing, correspondence, and
  named prospects stay in local gitignored files.
