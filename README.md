# signalAgent

This repo is the development record for **SGL-001**, an intranasal exosome
biologic. It is not source code for the product — it is the working memory
and audit trail for the team of agents developing and communicating about it.

## How this works

Agents run on a rota. Each agent:

1. Reads its own state file in [`state/`](state/) to see what it already
   knows and what it did last time.
2. Does its job (research, analysis, drafting, review).
3. Produces or updates an artifact in [`artifacts/`](artifacts/) —
   maps, audits, spec sheets, and other published outputs — or a draft
   post in [`posts/`](posts/).
4. Appends what it learned back to its state file.
5. Commits the result.

The **commit history is the development record.** Anyone should be able to
reconstruct how SGL-001's development progressed, what each agent found,
and why an artifact or post looks the way it does, by reading commits in
order.

## Layout

- `agents/` — one markdown brief per agent job: what it is, what it reads,
  what it produces, and the rules it operates under. See
  [`agents/README.md`](agents/README.md) for the brief format.
- `state/` — one file per agent, holding what that agent has already found
  or decided. Read at the start of a run, appended to at the end.
- `artifacts/` — published outputs: maps, audits, spec sheets, and other
  finished documents that other agents or humans consume.
- `posts/` — draft social posts, one file per day.
- `scripts/` — utilities used by agents or maintainers.

## Conventions

- Every agent run that changes state or produces an artifact should end in
  a commit, with a message describing what was found or produced.
- State files are append-only logs, not scratch space — don't rewrite
  history in them, add to it.
- Artifacts are the source of truth for anything published externally;
  posts should cite the artifact they draw from.
