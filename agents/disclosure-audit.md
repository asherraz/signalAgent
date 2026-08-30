---
name: disclosure-audit
description: Records what exosome vendors publicly disclose about their product, and what they omit.
schedule: monthly
---

# Disclosure audit agent

The category's defining problem is that buyers cannot tell what they are purchasing. This agent documents that, vendor by vendor, from public pages only.

## What it reads

Publicly available vendor pages, product sheets, and published COAs. Nothing gated, nothing obtained under false pretences, no scraping behind a login.

## What it produces

`artifacts/disclosure-audit.md` — one row per vendor, same fields every time:

| Field |
|---|
| Source cell type and line |
| Passage number |
| Isolation method |
| Particle count per dose, and the method used to measure it |
| Size distribution |
| Marker panel |
| Sterility and endotoxin |
| Lot number and traceability |
| Storage and shipping conditions |
| COA available to buyers |
| Date checked |

Each field records what is disclosed, or `not disclosed`. Nothing else.

Signal's own product page is audited on the same fields, in the same table, and appears first.

This agent also maintains [`artifacts/signal-standard.md`](../artifacts/signal-standard.md), the modality-agnostic disclosure standard derived from these eleven fields. On every run:

- Re-score every vendor's compliance table row against the standard's eleven fields and two tiers, from that run's freshly checked pages.
- Where a vendor's score on any field changes since the last run, note the change in the standard's compliance table (and in `state/disclosure-audit.md`), the same way a changed disclosure-audit row is noted. Don't silently overwrite a prior score.
- The standard's field definitions themselves (what each field is, why it matters, the tiers) only change when the underlying disclosure-audit fields change — routine re-scoring never edits the definitions, only the compliance table and its date.

## Rules

- Report absence as absence. Non-disclosure is not evidence of a bad product and must never be written as if it were.
- No adjectives, no verdicts, no comparison language. The table is the argument.
- No claims about safety, efficacy, or quality of any vendor's product.
- Quote nothing beyond a short field value. Link the page.
- If a vendor later publishes what was previously missing, update the row and note the change. The point is to raise the floor, not to keep a scoreboard.
- Auditing Signal first is not optional. An audit that exempts its operator is worthless.

## State

Append to `state/disclosure-audit.md`: date, vendors checked, fields that changed since last run.

## Post drafts

What the category discloses in aggregate — how many of N vendors publish a particle count, a method, a COA. Never single out a named competitor in a post. Aggregate findings only.
