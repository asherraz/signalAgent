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
runs weekdays at 06:00 UTC, plus on manual dispatch. Each run:

1. Checks the table below for today's assigned agent.
2. If that slot is empty, or the assigned agent has already run today,
   falls back to whichever agent has gone longest since its last run (per
   `state/<name>.md`), restricted to agents whose brief's own `schedule`
   says they're due.
3. Reads that agent's brief in full, does the work, and commits — or
   commits nothing if there was nothing material to add.

| Day | Agent | Cadence |
|---|---|---|
| Monday | [literature](literature.md) | weekly |
| Tuesday | [jurisdiction](jurisdiction.md) | weekly |
| Wednesday | [manufacturing](manufacturing.md) | fortnightly |
| Thursday | [spec](spec.md) | fortnightly |
| Friday | [disclosure-audit](disclosure-audit.md) / [clinics](clinics.md) | monthly, alternating |

Fortnightly and monthly agents skip their slot when they ran inside their
cadence. A skipped slot means no commit — silence is a valid outcome and
is preferable to a run that manufactures a finding to justify itself.

An empty slot isn't idle time — the fallback rule in step 2 fills it from
whichever agent is most overdue. Give a new agent its own row when its
brief is created; until then it still runs via the fallback whenever it's
due and nothing else has priority.

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
