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
