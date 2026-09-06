---
name: aiRB
description: Documents the shape of state/aiRB.json, the single source the aiRB page reads.
stage: none
---

# aiRB dataset

`state/aiRB.json` is the single source the aiRB page reads. Three top-level keys.

## `board`

The aiRB's self-description — static, not regenerated per run.

- `name` — `"aiRB"`
- `definition` — one line: an internal adversarial multi-agent review layer that audits Signal's own data artifacts before they reach the public site. Not an institutional review board in the legal/human-subjects sense; carries no regulatory authority; a bias-and-accuracy check.
- `roles` — array of `{name, mandate, sees, isolated_from}`, one per role: Proposer, Verifier, Adversary, Chair. Isolation between roles is the mechanism the board relies on — a role's `isolated_from` is load-bearing, not incidental.
- `rules` — the three disposition rules: dissent is recorded rather than resolved away; no record ships on agent consensus alone if the Verifier flagged an overclaim (routes to a human instead); the board convenes only on changes to a record, never on static records.

## `standard`

The Signal Disclosure Standard (SDS-1), copied verbatim from `artifacts/signal-standard.md` so nothing is lost if that artifact changes shape. `version`, `date`, `title`, `intro`, `audit_headline`, and `fields` — an array of 11 `{n, name, tier, definition, absence_means}` objects, `tier` being `"minimum"` (5 fields) or `"complete"` (6 fields). If `artifacts/signal-standard.md` is revised, re-sync this object from it — don't let the two drift.

## `reviews`

Append-only array of aiRB deliberations, newest-first once populated. Empty until the board runs its first review; the aiRB page shows "coming online" for the feed until this has entries.
