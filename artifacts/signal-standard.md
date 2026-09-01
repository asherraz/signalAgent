---
slug: signal-standard
title: The Signal Disclosure Standard
description: The minimum a buyer of a biological product needs disclosed before they can evaluate it, and the seed of a common language for approval across the category — eleven fields, two tiers, a buyer's checklist, and every disclosure-audit vendor scored against it.
updated: 2026-09-01
status: v1
domain: market
agent: disclosure-audit
---

# The Signal Disclosure Standard (SDS-1)

## What this is

A buyer of a biological product — a clinic, a distributor, a practitioner — cannot inspect the product itself before purchase. They can only read what the supplier publishes. In regenerative medicine broadly (exosomes and other extracellular vesicles, mesenchymal and other stem-cell therapies, secretome, cell-free products), that published information is routinely incomplete, and the category has no shared floor for what "incomplete" means. [`artifacts/disclosure-audit.md`](disclosure-audit.md) documented this for eight exosome vendors and found that most of the eleven fields a buyer would need are absent across most of the market.

This standard generalizes that finding into something usable beyond exosomes: the fields a buyer of *any* biological product needs disclosed before they can evaluate it, independent of modality. A cell-therapy supplier, a secretome supplier, and an exosome supplier are all being asked the same eleven questions here, phrased generically enough to apply to all three.

Read at the category level, this standard is the seed of something larger: **a common language for approval** — a shared way to characterise and reproduce a biological product well enough that a regulator, a CDMO, and a buyer can all evaluate the same claim the same way. Manufacturing consistency (can two lots, batches, or production years be shown to be the same product) and a defined mechanism (can the product's activity be tied to a specific, testable cause) are the two problems this standard's eleven fields point toward. They are not side considerations to a disclosure checklist; they are the actual bottleneck a disclosure standard is a first step toward closing.

The standard does not set pass/fail thresholds on quality, safety, or efficacy, and it makes no claim about any product's suitability. It sets a floor for disclosure — what must be stated for a buyer to make an informed decision at all. Non-disclosure is not evidence of a bad product. It is evidence that the buyer cannot currently evaluate the product, which is a different problem and the one this standard addresses.

This is a **living document** — see [Version and date](#version-and-date). It is maintained and re-scored by the disclosure-audit agent on the same schedule as the underlying audit.

## The fields

Eleven fields, generalized from the eleven fields already used in `disclosure-audit.md`. Each is stated modality-agnostically: "source material" rather than "cell line," "potency or quantity metric" rather than "particle count," so the same field applies whether the product is exosomes, a cell suspension, or a cell-free secretome fraction.

### 1. Source material and line identifier
**What it is:** The biological starting material (cell type, tissue origin, donor category) and a specific line or bank identifier — not just a category description.
**Why a buyer needs it:** "Umbilical cord-derived" or "placental stem cell-derived" describes a category, not a product. Two suppliers naming the same source category can be manufacturing from entirely different starting material with different consistency and risk profiles. A line identifier is what makes the product traceable back to a specific, characterized source.
**What its absence means:** The buyer cannot confirm that what they receive today is the same starting material as what they received last time, or as what any published data was generated from.

### 2. Passage number (or equivalent culture/processing history)
**What it is:** How many times the source material was expanded or passaged before the product was derived from it, or the equivalent processing-history marker for a non-cultured modality.
**Why a buyer needs it:** Cultured cells and cell-derived products drift with passage — phenotype, potency, and yield all change over expansion. A product's characteristics are only meaningful in the context of where in that drift it was made.
**What its absence means:** Two lots described identically on every other field could still differ meaningfully if drawn from different points in the culture history, and the buyer has no way to know.

### 3. Isolation or production method
**What it is:** The specific technique used to derive or isolate the product from its source material (e.g. ultracentrifugation, size-exclusion, tangential-flow filtration for EVs; expansion and harvest protocol for cells).
**Why a buyer needs it:** Different isolation methods yield materially different products from the same starting source — different purity, different co-isolated contaminants, different yield. The method is part of the product's identity, not an implementation detail.
**What its absence means:** Two products claiming the same source and the same potency number can still be different products if isolated differently, and nothing in the rest of the disclosure would reveal that.

### 4. Potency or quantity metric, and its measurement method
**What it is:** The quantitative measure appropriate to the modality (particle count for EVs, viable cell count for cell therapy, protein concentration for secretome) per dose or per unit, **and** the method used to measure it.
**Why a buyer needs it:** A number without a method is not a specification, it's a claim. Nanoparticle tracking analysis, flow cytometry, and other counting methods produce different numbers from the same sample. Without the method, the number cannot be verified or compared against another supplier's number.
**What its absence means:** The buyer cannot verify the quantity claim independently, and cannot compare it meaningfully to a competitor's claim even when both publish a number.

### 5. Size or physical characterization
**What it is:** The physical characterization appropriate to the modality — size distribution for particles, morphology and viability for cells.
**Why a buyer needs it:** Confirms the product is physically consistent with what it's claimed to be (e.g. a particle-size range consistent with extracellular vesicles rather than larger cellular debris or aggregates).
**What its absence means:** The buyer has no independent physical confirmation that the product matches its own description.

### 6. Identity markers
**What it is:** The panel of markers (surface markers, proteins, or other identity confirmation) used to confirm what the product actually is, distinct from what it's claimed to be.
**Why a buyer needs it:** A stated source and isolation method are claims about process; identity markers are evidence about the actual output. They are the closest thing to independent confirmation a public disclosure can offer.
**What its absence means:** The product's identity rests entirely on the supplier's description of their process, with no output-level confirmation.

### 7. Sterility and endotoxin testing
**What it is:** Results (not just the existence of a testing step) confirming the product is sterile and within an endotoxin limit appropriate to its route of administration.
**Why a buyer needs it:** This is a direct patient-safety field. A process step described as contributing to sterility (e.g. a filtration step) is not the same as a sterility test result, and buyers need to be able to tell the two apart.
**What its absence means:** The buyer has no confirmation the product is safe to administer by its intended route, regardless of anything else disclosed.

### 8. Lot number and traceability
**What it is:** A lot or batch identifier tying a specific unit of product to its manufacturing record, and a mechanism for the buyer to reference it.
**Why a buyer needs it:** If a safety issue or a quality deviation is later identified, traceability is what allows the buyer to know whether the units they hold are affected.
**What its absence means:** In a recall or adverse-event scenario, the buyer has no way to determine whether their inventory is implicated.

### 9. Storage and shipping conditions
**What it is:** The temperature and handling conditions required in transit and storage, stated specifically (a temperature or a defined condition, not just "cold chain").
**Why a buyer needs it:** Biological products can lose potency or become unsafe if mishandled. The buyer needs to know the actual required conditions to verify their own handling was correct, and to know what they're responsible for once the product arrives.
**What its absence means:** The buyer cannot confirm the product they received was maintained correctly, and has no defined standard to hold their own handling to.

### 10. Certificate of Analysis (COA) availability
**What it is:** Whether a lot-specific or batch-specific COA is offered to buyers, and how (automatically with shipment, on request, or not at all).
**Why a buyer needs it:** A COA is where fields 4, 6, and 7 above should actually appear with values, per lot. Its availability is a proxy for whether the supplier's quality system produces buyer-facing documentation at all.
**What its absence means:** Everything else on this list may exist internally at the supplier, but the buyer has no route to see it for the specific lot they are purchasing.

### 11. Documentation currency
**What it is:** A stated date on the supplier's product documentation (spec sheet, product page, or COA) indicating when it was last confirmed accurate or revised.
**Why a buyer needs it:** Published specifications can go stale without the buyer knowing — a process change, a supplier switch, or a reformulation can happen without the public page being updated. A dated document lets a buyer judge how current what they're reading actually is.
**What its absence means:** The buyer cannot tell whether the disclosed information reflects the current product or an earlier version of it. As of this version of the standard, no audited vendor's public documentation states a currency date at all — this is a category-wide gap, not one supplier's gap.

## Tiers

**Minimum disclosure** — the floor below which a buyer cannot responsibly evaluate the product at all:

- Field 1 — Source material and line identifier
- Field 4 — Potency/quantity metric and measurement method
- Field 6 — Identity markers
- Field 7 — Sterility and endotoxin testing
- Field 10 — COA availability

**Complete disclosure** — minimum, plus the fields needed for ongoing quality assurance and audit trail once a buying relationship exists:

- Field 2 — Passage number
- Field 3 — Isolation or production method
- Field 5 — Size or physical characterization
- Field 8 — Lot number and traceability
- Field 9 — Storage and shipping conditions
- Field 11 — Documentation currency

A supplier can be a reasonable purchase candidate without meeting Complete disclosure. A supplier that does not meet Minimum disclosure cannot currently be evaluated on the published record — the buyer would be purchasing on trust in the supplier's private assurances, which this standard does not attempt to score.

## How to use it — a buyer's checklist

Hand this section, unmodified, to any supplier. It is written to be sent as-is.

> Before we can evaluate your product, please confirm the following in writing, with reference to a public page, product sheet, or COA where possible:
>
> **Minimum disclosure**
> 1. What is the source material, and what is the specific line or bank identifier?
> 2. What is the potency or quantity metric per dose or per unit, and what method was used to measure it?
> 3. What identity markers confirm the product is what it is claimed to be?
> 4. What are the sterility and endotoxin test results for this product (not just the process steps intended to achieve sterility)?
> 5. Is a lot-specific Certificate of Analysis available for the lot we would receive, and how do we obtain it?
>
> **Complete disclosure**
> 6. What is the passage number or equivalent processing history of the material used?
> 7. What isolation or production method was used to derive the product from its source?
> 8. What is the size distribution or physical characterization of the product?
> 9. What lot number will this shipment carry, and how can we reference it later?
> 10. What are the required storage and shipping conditions, stated as a specific temperature or condition?
> 11. What is the date this documentation was last confirmed accurate?
>
> A supplier that cannot answer the first five has not met the minimum for evaluation. A supplier that answers all eleven has met complete disclosure as defined by the Signal Disclosure Standard (SDS-1).

## Compliance table

Every vendor audited in `disclosure-audit.md`, scored against the eleven fields above, Signal first. Legend: **✓** fully disclosed, **~** partially disclosed (something stated, but not enough to satisfy the field as defined), **—** not disclosed. Scored from the same public pages and dates recorded in the audit; see that document for sources and exact quoted language.

| Vendor | 1. Source & line | 2. Passage | 3. Isolation method | 4. Potency & method | 5. Size/physical | 6. Identity markers | 7. Sterility/endotoxin | 8. Lot/traceability | 9. Storage/shipping | 10. COA | 11. Documentation date |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Signal** | — | — | — | ~ (count only, no method) | ✓ | ✓ | ~ (filtration step stated, not a test result) | — | — | — | — |
| **Kimera Labs** | ~ (type stated, no line ID) | — | — | — | — | — | — | — | — | — | — |
| **Direct Biologics** | — | — | — | — | — | — | — | — | — | — | — |
| **Vitti Labs** | — | — | — | — | — | — | — | ~ (tracking form linked, no lot record shown) | — | — | — |
| **EriVan Bio** | ~ (type stated, no line ID) | — | — | ~ (count only, no method) | — | — | — | — | ~ ("dry ice" stated, no temperature) | — | — |
| **Stem Nova Network** | — | — | — | ✓ (per-SKU counts, NTA stated) | — | — | ~ (categories named, no values published) | ✓ | ✓ | ✓ | — |
| **BioRegenEx** | ~ (type stated, no line ID) | — | — | — | — | — | — | — | — | ~ (stated as included in a portal package, not published) | — |
| **Exocel Bio** | ~ (type stated, no line ID) | — | — | ~ (SKU counts, no method) | — | — | ~ (donor screening stated, not a product sterility/endotoxin result) | — | — | — | — |

### Scores

| Vendor | Minimum tier — fields fully met (of 5) | Complete tier — fields fully met (of 11) | Fields partially disclosed (of 11) | Fields not disclosed (of 11) |
|---|---|---|---|---|
| **Signal** | 1 | 2 | 2 | 7 |
| **Kimera Labs** | 0 | 0 | 1 | 10 |
| **Direct Biologics** | 0 | 0 | 0 | 11 |
| **Vitti Labs** | 0 | 0 | 1 | 10 |
| **EriVan Bio** | 0 | 0 | 3 | 8 |
| **Stem Nova Network** | 2 | 4 | 1 | 6 |
| **BioRegenEx** | 0 | 0 | 2 | 9 |
| **Exocel Bio** | 0 | 0 | 3 | 8 |

**No vendor in this run, Signal included, fully meets the Minimum disclosure tier.** Stem Nova Network meets the most fields overall (4 of 11 fully, 2 of 5 minimum-tier), driven by its lot-specific COA and stated storage/shipping conditions. No vendor discloses a source line identifier, a passage number, an isolation method, a size/physical characterization independent of Signal's own particle-size figure, or a documentation currency date — these five fields are unmet category-wide, not just by any one supplier.

This table will be re-scored on each disclosure-audit run. Where a vendor's disclosure changes, that change is noted in the run's entry rather than silently overwriting the prior score.

## Version and date

**v1** — 2026-08-30. First version, derived from the eight-vendor, eleven-field audit of 2026-08-28. Maintained by the disclosure-audit agent; see [`agents/disclosure-audit.md`](../agents/disclosure-audit.md). 2026-09-01: added the common-language-for-approval framing above — mission context, not a change to the eleven fields, the tiers, or the compliance table, so the version stays v1.
