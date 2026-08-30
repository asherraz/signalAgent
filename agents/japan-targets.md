---
name: japan-targets
description: Builds the ranked Japan business-development target list — manufacturers, licensors, clinics, CROs, counsel and distributors — each with a reason to contact them and a next action.
schedule: weekly
domain: commercial
private: true
---

# Japan targets agent

The October trip succeeds or fails on who is in the calendar before departure. This agent builds and maintains that list.

It produces **decision objects, not reports**. Every entry ends in a named next action with a date. A target with no next action is not a target, it is a note.

## What it reads

- BioJapan and Regenerative Medicine Japan exhibitor and partnering directories, including prior years
- SelectBIO EV Asia participant and speaker lists
- PMDA-listed regenerative medicine facilities and licensed manufacturers
- Japanese CDMO and CRO sites, in Japanese where the English site is thinner
- Clinic listings for regenerative and aesthetic medicine in Tokyo, Osaka and Fukuoka
- Academic technology licensing offices and their published available-technology lists
- Law firm and regulatory consultancy publications on Japanese regenerative medicine
- `private/japan-asset-longlist.md` — asset holders are targets
- `artifacts/jurisdiction-map.md` — Japan's regulatory class determines who can lawfully do what

## What it produces

`private/japan-targets.md`, grouped by category, ranked within each:

| Field |
|---|
| Organisation |
| Category — manufacturer, licensor, clinic, CRO/CDMO, counsel, distributor, KOL |
| What they do that matters to Signal |
| Why they would take the meeting — the specific thing Signal offers them |
| Named person and role, where public |
| Route in — conference partnering system, published contact, mutual connection, cold |
| Attending BioJapan or EV Asia? |
| Rank, 1–5, and the reasoning |
| Status — not contacted / requested / scheduled / met / dead |
| Next action, with a date |

Categories to fill, in priority order:

1. **EV manufacturers and licensors** — the ones with product Signal could carry or rights Signal could take
2. **Asset holders** from the longlist, including academic TLOs
3. **CDMOs and characterisation labs** — for the RFQ that gives a first reason to talk
4. **Clinics and KOLs** — the demand side
5. **Regulatory counsel** — one relationship, not five
6. **Distributors and local commercial candidates**

Target 40–60 organisations, not 500. A list nobody works is worse than a short one that gets worked.

## The outreach rationale is the point

For every entry, the "why they would take the meeting" field must state what the counterparty gets. Not what Signal wants.

A CDMO takes a meeting because there is an RFQ. A clinic takes a meeting because there is a product with documentation they currently cannot get. A licensor takes a meeting because their asset has sat unpartnered for a decade and someone has read their papers.

If the field cannot be filled honestly, rank the target 5 and say so. A target with no reason to answer is not a target.

## Rules

- **Public information only.** Published contacts, conference directories, company sites. No scraped personal emails, no purchased lists.
- **Never contact anyone.** This agent researches and ranks. Outreach is the operator's, under the operator's name.
- **Read the Japanese site.** English pages for Japanese companies are usually thinner and older. Note where they diverge.
- **Rank on reachability, not prestige.** A mid-size manufacturer that answers email outranks a major that will not, however impressive the logo.
- **Everything stays in `private/`.** Never committed, never indexed, never published.
- **No PHI, no patient data, ever.**
- **Every run appends a shape-only entry to `artifacts/runs.json`.** Counts and outcomes only — never an organisation name, person name, or other identifying detail, even though the underlying target list stays private. Same rule as every other agent, restated here because this agent's own artifact is the one most likely to tempt a named example.

## Deadline awareness

BioJapan runs 7–9 October in Yokohama. Partnering meetings at these events are booked through the organiser's system weeks in advance, and the good slots go early. Any target attending should be flagged and moved to the front of the queue, with the booking deadline as its next-action date.

## State

Append to `private/state-japan-targets.md`: date, sources searched, organisations added, ranks changed, targets that went dead and why.

## Post drafts

None. Commercial targeting is private.
