---
slug: cdmo-readiness
title: CDMO Readiness
description: The questions a contract manufacturer asks before it will quote cGMP extracellular vesicle production, and whether Signal can currently answer each one.
updated: 2026-08-27
status: in-progress
domain: product
---

# CDMO readiness

The other direction from a vendor landscape: not which CDMOs exist, but
what any of them needs from Signal before a quote is possible. A CDMO
does not price a project from a product idea — it prices a defined
process against a defined material. Everything below is a question that
process definition requires an answer to.

Signal's only public materials are spray.signal.clinic (fetched
2026-08-27, per [`jurisdiction-map.md`](jurisdiction-map.md)) — in-clinic,
physician-directed, a nasal spray device, cognitive/neuro marketing
claims, a proprietary "Signal Index" score. No local file in this repo
holds a product spec, and none was found publicly. Where a row below says
"not publicly documented," that is a search result, not an assumption —
if Signal has these answers in an internal document, this artifact does
not know about it, and the gap should be closed by the operator supplying
it, not by this agent guessing.

## Questions

| # | Question | Why a CDMO asks it | Can Signal answer it today | Source |
|---|---|---|---|---|
| 1 | **Source cell line and its provenance** — what cell type, tissue origin (e.g. bone-marrow, adipose, endometrial MSC; HEK293; iPSC), donor/vendor traceability, passage number, and master/working cell bank status | Exosomes are not a homogeneous class — cell source determines vesicle content and is the first branch point in any process design; a CDMO needs a "reliable and traceable source" and cell-bank characterization before it will scope work | **No.** Not stated anywhere on spray.signal.clinic or found elsewhere. | [Global requirements for manufacturing and validation of clinical grade EVs, PMC11863704](https://pmc.ncbi.nlm.nih.gov/articles/PMC11863704/); [Wang et al. 2024, Clin Transl Sci](https://ascpt.onlinelibrary.wiley.com/doi/10.1111/cts.13904) |
| 2 | **Target particle count / dose** — particles per unit dose, and the basis for that number (particles per µg protein, per mL, per administration) | Sets batch size, yield targets, and whether the CDMO's platform scale is even compatible with the ask | **No.** No dose or particle-count figure published. | Wang et al. 2024 (above) — particle count and "particles per microgram of protein" as the standard reporting basis |
| 3 | **Required analytics** — size distribution method (DLS, NTA, TRPS), particle count method, molecular cargo characterization (protein/miRNA/mRNA), sterility, endotoxin, potency/mechanism-of-action assay, batch-to-batch consistency vs. a reference standard | A CDMO quotes the analytics package as its own line item and needs to know whether methods already exist (transfer) or must be developed from scratch (much more expensive) | **No.** Nothing published about analytical methods; "Signal Index" is a marketed cognitive score, not a release assay, and there's no indication it maps to any particle-level measurement. | Wang et al. 2024; general biologics tech-transfer requirement of 15–20 analytical methods per product, [Drug Discovery News, CDMO tech transfer guide](https://www.drugdiscoverynews.com/negotiating-tech-transfer-and-quality-agreements-with-your-cdmo-17316) |
| 4 | **Batch size and annual demand** — clinical vs. commercial scale, pilot-batch availability, forecasted batches/year | Determines which CDMOs even have compatible capacity, and is a direct input to price | **No.** No production volume, cohort size, or manufacturing cadence has been published; "limited cohort of licensed physicians for the initial rollout" (site language) gives no number. | spray.signal.clinic (fetched 2026-08-27); [PharmaSource CDMO RFQ checklist](https://pharmasource.global/content/cdmo-rfq/) |
| 5 | **Container and device** — final container-closure system, and specifically nasal spray device compatibility (device supplier, actuation volume, fill-finish approach, whether device fill happens at the CDMO or downstream) | Nasal delivery is not a standard biologics fill-finish path; most EV CDMOs are set up for vial/syringe fill, not device assembly, so this alone can eliminate candidates | **Partially.** The route is known — intranasal — from the site's own framing ("Nose to brain"). The device itself (manufacturer, fill volume, actuation mechanism) is not disclosed anywhere found. | spray.signal.clinic (fetched 2026-08-27) |
| 6 | **Stability requirement** — storage condition (frozen, refrigerated, ambient), shelf-life target, freeze/thaw tolerance, in-use stability after device fill | Directly shapes formulation and packaging choices, and stability data is typically the longest lead-time item in a program | **No.** No stability data, target shelf life, or storage condition has been published. | PMC11863704 (above) — storage condition and shelf-life among core clinical-grade EV requirements |
| 7 | **Intended market and regulatory pathway** — which jurisdiction(s), and under what legal theory (IND-backed biologic, a state-law carve-out, or something else) | A CDMO's own quality system and documentation burden depend entirely on what regulatory status the batch is being made to support — cGMP-for-IND is a different (and pricier) scope than anything less | **No, and the public claim conflicts with itself.** [`jurisdiction-map.md`](jurisdiction-map.md) documents that spray.signal.clinic cites Florida SB 1768 as its legal basis while marketing exclusively cognitive/neuro claims — a combination the statute's own text does not cover, and federal law is not mentioned on the site at all. There is no public statement of an IND, a BLA, or any federal regulatory posture. | [`jurisdiction-map.md` § Conflicts](jurisdiction-map.md) |

## What this means

Every question above is answerable in principle — none require original research, only a decision or a document Signal should already have if a product exists. The pattern is not "hard questions," it's an absence of any published product specification at all. A CDMO cannot open a scoping conversation, let alone quote, from marketing copy and a legal citation. Rows 1–4 and 6 are pure gaps: no CDMO will price against them as they stand. Row 5 is half-answered — route only. Row 7 is worse than unanswered: the one regulatory claim that is public [doesn't hold up on its own terms](jurisdiction-map.md), which is a liability in an RFQ conversation, not a neutral blank.

None of this is resolved by this agent; it isn't Signal's internal information to have and doesn't appear in this repo. The next move belongs to the operator: either these seven answers exist in a document this repo doesn't have access to, or they don't exist yet, in which case this table is the actual pre-manufacturing punch list.

## Sources consulted

- [Global requirements for manufacturing and validation of clinical grade extracellular vesicles, PMC11863704](https://pmc.ncbi.nlm.nih.gov/articles/PMC11863704/)
- [Wang et al., "Regulation of exosomes as biologic medicines," Clinical and Translational Science, 2024](https://ascpt.onlinelibrary.wiley.com/doi/10.1111/cts.13904)
- [Drug Discovery News — CDMO tech transfer and quality agreements guide](https://www.drugdiscoverynews.com/negotiating-tech-transfer-and-quality-agreements-with-your-cdmo-17316)
- [PharmaSource — CDMO RFQ checklist](https://pharmasource.global/content/cdmo-rfq/)
- `spray.signal.clinic`, fetched 2026-08-27 (via [`jurisdiction-map.md`](jurisdiction-map.md), not re-fetched independently this run)
- Lonza and Esco Aster EV/CDMO service pages were checked directly for a published intake questionnaire; neither publishes one (Lonza returned HTTP 403 to automated fetch; Esco Aster's page describes capabilities only, no client-facing checklist).
