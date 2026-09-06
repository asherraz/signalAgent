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

The Signal Disclosure Standard (SDS-1), copied verbatim from `artifacts/signal-standard.md` so nothing is lost if that artifact changes shape. `version`, `date`, `title`, `intro`, `audit_headline`, and `fields` — an array of 11 `{n, name, tier, definition, absence_means}` objects, `tier` being `"minimum"` (5 fields) or `"complete"` (6 fields).

**`artifacts/signal-standard.md` is re-scored on every disclosure-audit run** (see `agents/disclosure-audit.md`), so this copy goes stale the moment that happens. Run `python3 scripts/sync_airb_standard.py` to regenerate this key from the current `signal-standard.md` — it parses the title, the version/date line, the first paragraph under "What this is", the bolded headline sentence at the top of the Compliance table section, and all 11 fields (with their tier from the Tiers section), and rewrites only the `standard` key, leaving `board` and `reviews` untouched. It prints what changed, or "no change" if the copy was already current. **Required step after any disclosure-audit run that touches `signal-standard.md`** — not yet wired into the GitHub Actions workflow, so it must be run by hand until it is.

## `reviews`

Append-only array of aiRB deliberations, newest-first once populated. Empty until the board runs its first review; the aiRB page shows "coming online" for the feed until this has entries.
