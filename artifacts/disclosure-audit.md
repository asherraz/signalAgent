---
slug: disclosure-audit
title: Disclosure Audit
description: What exosome vendors publish about their product, field by field, from public pages only — source, passage, isolation method, particle count and its measurement method, markers, sterility, traceability, storage, and COA availability.
updated: 2026-08-28
status: in-progress
---

# Disclosure audit

Eight vendors, eleven fields, one row each. Every cell records what the
vendor's own public pages state, or `not disclosed`. Non-disclosure is
not evidence of a bad product and is not written here as if it were —
this records what a buyer can and cannot learn before purchase, nothing
more.

Signal is audited first, on the same fields, from its own public pages.

## Conflicts

`spray.signal.clinic` publishes a per-dose particle count
(5×10⁹ particles/dose), a size range (30–150 nm), a marker panel
(CD9, CD63, CD81), and a filtration step (0.22 µm), and publishes no
source cell type, no isolation method, no measurement method behind the
particle count, no sterility or endotoxin result, no lot or traceability
reference, no storage or shipping condition, and no COA offer. The
0.22 µm figure is a process step, not a sterility test result, and is
recorded in the sterility field as filtration only.

This repo's own `cdmo-readiness.md` (2026-08-27) records the same
parameters — cell source, isolation method, particle-count method,
release testing — as questions Signal cannot currently answer in full.
The public pages and the internal readiness record are consistent with
each other on those fields: both say the information does not exist
publicly. The published figures above are the exception, and
`sgl-001-spec.md` (2026-08-27) already records that the bottle
arithmetic behind them does not close. That unresolved point is not
re-litigated here; it is noted so this audit's Signal row is not read as
independent confirmation of those numbers.

## The table

| Vendor | Source cell type / line | Passage no. | Isolation method | Particle count per dose (method) | Size distribution | Marker panel | Sterility / endotoxin | Lot no. / traceability | Storage / shipping | COA to buyers | Date checked |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Signal** | not disclosed | not disclosed | not disclosed | 5×10⁹ particles/dose; 100 doses/bottle (method not disclosed) | 30–150 nm | CD9, CD63, CD81 | 0.22 µm sterile filtration stated; no sterility or endotoxin result disclosed | not disclosed | not disclosed | not disclosed | 2026-08-28 |
| **Kimera Labs** | "perinatal mesenchymal stem cell (MSC)-derived"; "single-donor pre-COVID MSC cell bank"; no line identifier | not disclosed | not disclosed | not disclosed | not disclosed | not disclosed | not disclosed | not disclosed | not disclosed | not disclosed | 2026-08-28 |
| **Direct Biologics** | not disclosed | not disclosed | not disclosed | not disclosed | not disclosed | not disclosed | not disclosed | not disclosed | not disclosed | not disclosed | 2026-08-28 |
| **Vitti Labs** | not disclosed | not disclosed | not disclosed | not disclosed | not disclosed | not disclosed | not disclosed | product-tracking form linked; no lot format or record disclosed | not disclosed | not disclosed | 2026-08-28 |
| **EriVan Bio** | "Umbilical Cord Derived"; no line identifier | not disclosed | not disclosed | 1×10⁹/mL (method not disclosed) | not disclosed | not disclosed | not disclosed | not disclosed | "shipped on dry ice"; storage temperature not disclosed | not disclosed | 2026-08-28 |
| **Stem Nova Network** | not disclosed for the exosome line | not disclosed | not disclosed | 12, 60 and 150 billion per vial, by SKU (NTA, stated per production lot) | not disclosed | not disclosed | sterility, mycoplasma, endotoxin and viral screening stated as covered on the lot COA; no values published | "lot-specific Certificate of Analysis" with every shipment | "overnight on dry ice with cold-chain logging" | yes — lot-specific, stated as in-house plus third-party | 2026-08-28 |
| **BioRegenEx** | "Umbilical cord-derived MSCs" from "Wharton's jelly"; no line identifier | not disclosed | not disclosed | not disclosed | not disclosed | not disclosed | not disclosed | not disclosed | not disclosed | stated as included in a physician-portal documentation package; no COA or sample published | 2026-08-28 |
| **Exocel Bio** | "placental stem cell–derived"; no line identifier | not disclosed | not disclosed | 5, 12, 25 billion and 5 trillion (skin SKUs); 7, 15, 30 billion (hair SKUs); 75, 100, 450 billion (research SKUs) — method not disclosed | not disclosed | not disclosed | donor "infectious disease panel screened" and "sterile C-section collection" stated; no product sterility or endotoxin result disclosed | not disclosed | not disclosed | not disclosed | 2026-08-28 |

### Aggregate, this run

Counts over the eight rows above. These are arithmetic on the table, not
a ranking.

| Field | Vendors disclosing | of |
|---|---|---|
| Source cell type | 4 | 8 |
| Cell line identifier | 0 | 8 |
| Passage number | 0 | 8 |
| Isolation method | 0 | 8 |
| Particle count per dose or per vial | 4 | 8 |
| Measurement method behind that count | 1 | 8 |
| Size distribution | 1 | 8 |
| Marker panel | 1 | 8 |
| Sterility and endotoxin (any statement) | 1 | 8 |
| Lot number / traceability | 1 | 8 |
| Storage and shipping | 2 | 8 |
| COA available to buyers | 2 | 8 |

Four vendors publish a number of particles. One publishes how that
number was measured.

## Sources

One entry per row. Pages fetched 2026-08-28; field values above are
taken from these pages only.

- **Signal** — <https://spray.signal.clinic/> and
  <https://spray.signal.clinic/science>. Homepage carries
  "5×10⁹ particles / dose", "100 µL", "10 mL · METERED SPRAY",
  "0.22 µm". Science page carries "5×10⁹ particles per dose, 100 doses
  per bottle", "30-150 nm vesicles", "tetraspanins CD9, CD63, CD81".
  Neither page carries a source cell type, isolation method, storage
  condition, or COA offer.
- **Kimera Labs** — <https://kimeralabs.com/products/>. Carries
  "perinatal mesenchymal stem cell (MSC)-derived exosome products",
  "fully characterized, single-donor pre-COVID MSC cell bank", and
  "used for cosmetic and research purposes". No characterisation values.
  (`kimeralabs.com/` root returned a connection reset on first attempt;
  the products page fetched normally.)
- **Direct Biologics** — <https://www.directbiologics.com/pipeline>
  (`/exoflo` 301-redirects here). Page is pipeline-level: products "are
  being evaluated in clinical trials conducted under active
  Investigational New Drug applications" and "All Direct Biologics
  programs are investigational and have not been approved by the U.S.
  Food and Drug Administration." No product characterisation data on
  the public page.
- **Vitti Labs** — <https://vittilabs.com/>. Company-level page:
  "an industry leading manufacturer of human cellular and tissue-based
  products (HCT/Ps)", with AATB, GMP and FDA-registration claims. A
  "Product Tracking" form is linked. No product specification page was
  located on the public site this run.
- **EriVan Bio** — <https://www.erivanbio.com/product-page/uc-msc-exosomes-umbilical-cord-derived>.
  Carries "Umbilical Cord Derived", "Exosome Concentration: 1 x 10⁹ / mL",
  "shipped on dry ice", "$995 per vial (1 mL)".
- **Stem Nova Network** — <https://www.stemnovanetwork.com/pages/exosome-biologics-for-medspas>
  and <https://www.stemnovanetwork.com/>. Carries "60 billion
  NTA-verified extracellular vesicles" (also 12B and 150B SKUs),
  "Nanoparticle Tracking Analysis confirms exosome particle count on
  every production lot", "Every lot ships with a lot-specific
  Certificate of Analysis covering particle count, sterility,
  mycoplasma, endotoxin, and viral screening", "overnight on dry ice
  with cold-chain logging". Labelled "for topical cosmetic use only —
  they are not for injection or therapeutic use". The landing page
  describes "Wharton's jelly sourced" UCT-MSCs as a separate stem cell
  line and does not state the source cell type of the exosome line.
- **BioRegenEx** — <https://bioregenex.com/what-are-msc-derived-exosomes-physician-guide/>.
  Carries "Umbilical cord-derived MSCs", "Wharton's jelly", "Supplied
  for Research Use Only", and "BioRegenEx provides complete
  documentation in all five areas as part of the standard physician
  portal package". The page's own list of what a COA should contain
  (including CD63, CD81, HSP70) describes supplier requirements, not
  disclosed values for this vendor's product; it is not recorded as a
  marker-panel disclosure.
- **Exocel Bio** — <https://exocelbio.com/> and
  <https://exocelbio.com/exovex/>. Homepage carries per-SKU particle
  counts ("5 TRILLION", "5 BILLION", "12 BILLION", "25 BILLION" for
  exovex+ Skin; "7 BILLION", "15 BILLION", "30 BILLION" for exovex+
  Hair; "100 BILLION", "75 BILLION", "450 BILLION" for research
  products), "Ethically sourced placental stem cell–derived exosomes",
  "Infectious disease panel screened, exceeding FDA requirements /
  transplant grade", "Sterile C-section collection", "our team produces
  exosomes under rigorous cGMP and ISO standards", "FOR PROFESSIONAL USE
  ONLY", and "This product is not intended to diagnose, treat, cure, or
  prevent any disease". The exovex product page itself carries no
  particle count, no method, and no COA offer.

## Provenance

- First run of this agent. Eight vendors is the starting set, not the
  category — it was assembled from public search for exosome suppliers
  selling to clinics and practitioners, plus vendors already named
  elsewhere in this repo. It is not a census and should not be read as
  one; the denominator in the aggregate table is eight audited pages.
- **Not checked this run:** Zeo ScientifiX (formerly Organicell —
  `organicell.com` 301-redirects to `zeoscientifix.com`, which returned
  HTTP 403 to automated fetch). No row was created rather than filling
  one with `not disclosed` values that were never actually verified. Also
  not reached: Rion/Purexo, Predictive Biotech, Regenerative Labs, and
  the Korean supplier segment.
- Every value above comes from a page a prospective buyer can reach
  without a login. Nothing gated was fetched, no account was created,
  and no vendor was contacted. Where a vendor states that a document
  exists behind a portal or on request (BioRegenEx, Stem Nova), the row
  records the statement, not the document — the document itself was not
  seen.
- Field values are recorded from the specific pages listed above.
  A vendor may disclose more in a product insert, a portal, or on
  request. This audit measures what is published, which is the field a
  buyer can check before committing.
- Signal's row was compiled independently from the site this run and not
  copied from `sgl-001-spec.md`, so the two are separate readings of the
  same public pages rather than one reading cited twice.
