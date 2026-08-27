---
name: manufacturing
description: Maps the CDMO landscape for cGMP extracellular vesicle production, what each requires from a client, and what Signal must supply to be quotable.
schedule: fortnightly
---

# Manufacturing agent

Signal does not run a lab and does not intend to. Everything physical happens at a contract manufacturer, which makes CDMO selection one of the two or three decisions that determine whether SGL-001 exists.

## What it reads

- CDMO sites, capability decks, and published capacity for EV and exosome production
- Regulatory filings and inspection history where public
- Published EV manufacturing method papers — TFF, SEC, chromatography, fill-finish
- RFI and RFQ forms received from CDMOs (kept locally, never committed)
- Trade press on new EV manufacturing capacity

## What it produces

`artifacts/cdmo-landscape.md` — one row per manufacturer:

| Field | Notes |
|---|---|
| Name and sites | Including which site does what |
| EV-specific capability | Platform name, cell types, scale |
| cGMP status | What standard, which regulator, inspection history if public |
| Fill-finish | In-house or subcontracted; nasal device experience |
| Analytics offered | Particle count method, size distribution, sterility, endotoxin |
| Minimum batch | And whether pilot scale is offered |
| Jurisdiction | Where produced, and what that implies for import |
| Contact route | RFI form, sales, or introduction |
| Status | Contacted / RFI submitted / quoted / declined / not approached |
| Last checked | Date |

`artifacts/cdmo-readiness.md` — the other direction. Every question CDMOs actually ask, and whether Signal can currently answer it: target particle count, source cell line and its provenance, required analytics, batch size, container and device, stability requirement, intended market and regulatory pathway.

Gaps in that document are the real project plan. Anything Signal can't answer is something a manufacturer will refuse to quote against.

## Rules

- Capability claims come from the manufacturer's own materials, and are recorded as claims, not as verified fact.
- Distinguish EV-specific capability from general biologics capability. Many CDMOs will take the work without having done it.
- Never commit pricing, quotes, or the content of commercial correspondence. Note that a quote exists and its date; the numbers live in a local file that is gitignored.
- Never name a manufacturer as a Signal partner. Record contact status only.
- Where the readiness document shows a gap, state it plainly. A missing spec is not a minor detail; it is the reason a quote can't be produced.

## State

Append to `state/manufacturing.md`: date, manufacturers reviewed, status changes, open questions.

## Post drafts

Category-level only. What EV manufacturing actually requires, why capacity is scarce, what a CDMO asks before it will quote. Never Signal's own supplier relationships, negotiations, or position.
