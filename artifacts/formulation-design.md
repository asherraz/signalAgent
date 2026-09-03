---
slug: formulation-design
title: Formulation Design
description: The excipient system for an intranasal exosome preparation, each component traced to an approved nasal product or to the FDA Inactive Ingredient Database. The published EV-stabilisation buffer has no nasal precedent at all, and the one approved nasal permeation enhancer is a detergent that dissolves lipid vesicles.
updated: 2026-09-03
status: in-progress
domain: product
---

# Formulation design

**This is a design document. Nothing here has been formulated, made, filled,
or tested by Signal.** Every component below is a selection between published
options, with the precedent that justifies it and the confidence that
precedent supports. No entry is a measured result, and none of it substitutes
for bench compatibility and stability work.

Per [`agents/formulation.md`](../agents/formulation.md), Signal's declared
development focus is an intranasal exosome therapeutic, and this document
designs against exosomes as the active. That is a business decision recorded
as scope, not a conclusion of the four-axis comparison in
[`active-candidates.md`](active-candidates.md) — which still scores naive EVs
weakest of any candidate on three of four axes, and is unaffected by anything
here.

## Conflicts

**sgl001.signal.clinic describes the product as "a shelf-stable intranasal
exosome biologic" while publishing no storage condition, no shelf life, and
no formulation.** Fetched 2026-09-03; the phrase appears once, in the page's
meta description. Every other stability-related word — "storage",
"refrigerated", "frozen", "cold chain" — is absent from the page.

"Shelf-stable" is a stability claim, not a format description, and it is the
one claim on the site that this document's entire subject matter exists to
support or refute. Nothing published supports it, and the class evidence runs
the other way:

- −80 °C is the consensus long-term storage condition for EV preparations,
  and one freeze-thaw cycle costs 23–36% of particles (Ahmadian et al. 2024,
  already recorded in [`sgl-001-spec.md`](sgl-001-spec.md)).
- EVs held or diluted in plain PBS lose recoverable particles **within
  minutes**, not months — Görgens et al. 2022 found "using PBS as diluent was
  found to result in severely reduced EV recovery rates already within
  minutes," and drastically reduced recovery on storage "starting already
  within days" at every temperature tested.
- The only excipient systems shown to hold EVs stable at or above room
  temperature are lyophilised ones (Trenkenschuh et al. 2022;
  Charoenviriyakul et al. 2018), not the aqueous 10 mL metered spray the site
  publishes.

This is recorded here unsoftened, per the map's standing rule. It is a newer
and narrower point than the storage/shelf-life gap
[`sgl-001-spec.md`](sgl-001-spec.md) already records: that artifact noted the
*absence* of a published storage condition, and did not catch that the site
simultaneously makes an affirmative stability claim in its meta description.
The spec artifact owns the product-parameter record, so this is flagged for
that agent rather than edited into it here. What Signal does about its own
site is the operator's call.

## Scope and method

The brief requires every excipient to cite an approved intranasal product or
the FDA Inactive Ingredient Database (IID) as precedent, and treats an
excipient with no intranasal precedent as a regulatory problem rather than a
formulation choice. Three primary sources were queried directly this run:

1. **The FDA Inactive Ingredient Database, July 2026 release**, downloaded in
   full and filtered locally. Of 9,071 rows across all routes, **132 are
   route `NASAL`.** That whole 132-row list is the US nasal excipient
   precedent universe as FDA records it, and it is reproduced in the sections
   below wherever it bears on a decision.
2. **The openFDA drug-label index, filtered to `openfda.route:"NASAL"`** —
   694 labels — used to find which named products actually use a given
   excipient and at what stated level.
3. **The labels themselves** for the products relied on as precedent, read
   directly rather than through a formulary summary.

**Two structural findings came out of the method itself, before any
individual excipient was chosen.**

**There is no approved nasal biologic in the United States.** Of the
nasal-route labels indexed with an application number, 74 are NDAs, 238 are
ANDAs, and 278 are OTC monograph entries. **Zero are BLAs.** The nearest
things to a precedent are peptides and small proteins approved as *drugs* —
calcitonin-salmon (NDA 020313, 32 amino acids) and glucagon (BAQSIMI,
NDA 210134, 29 amino acids). SGL-001 sits on a BLA pathway
([`jurisdiction-map.md`](jurisdiction-map.md)), and no product on that
pathway has ever been approved for this route.

**The IID does not contain biologic excipients at all.** FDA's own guidance
says so: "Excipients used in approved Biologics License Applications (BLAs)
are not entered into the IID" (*Using the Inactive Ingredient Database*,
Guidance for Industry, CDER, July 2019 draft, footnote 4). So the 132-row
nasal list is drawn entirely from small-molecule and peptide NDA/ANDA
products. It is the right precedent database to check — the guidance is
explicit that "if an excipient is used in approved drug products for a
particular route of administration, the excipient generally is not
considered new and may warrant less extensive review" — but for a
vesicle-based biologic it is precedent from a neighbouring field, not the
same one. Both facts are recorded because they set the ceiling on how strong
*any* precedent claim in this document can be.

## The core constraint: the EV stabiliser set has no nasal precedent

The published buffer systems that keep extracellular vesicles intact were
developed for frozen bulk storage in laboratory plastics, not for a nasal
dosage form. Checking each of them against the IID, by route:

| Stabiliser | Why it is in the EV literature | IID routes with precedent | Nasal precedent |
|---|---|---|---|
| **Trehalose** (25 mM) | Bosch et al. 2016 — narrows particle size distribution, prevents freeze-thaw aggregation. Görgens et al. 2022 — a component of PBS-HAT, the lead buffer. Charoenviriyakul et al. 2018 — prevents aggregation on lyophilisation. | Intradermal, subcutaneous (3 rows) | **None** |
| **Human serum albumin** (0.2%) | Görgens et al. 2022 — the other PBS-HAT component; suppresses the plastic-surface adsorption that loses EVs within minutes | Intravenous, oral (2 rows) | **None** |
| **HEPES** (25 mM) | Görgens et al. 2022 — buffer base of PBS-HAT | **Not in the IID at all, by any route** | **None** |
| **Sucrose** (5%) | Trenkenschuh et al. 2022 — improved colloidal stability on freeze-thaw; part of the lyophilisate stable 6 months at 40 °C | 10 routes incl. IV, ophthalmic, oral, transmucosal (73 rows) | **None** |
| **Poloxamer 188** (0.02%) | Trenkenschuh et al. 2022 — "EVs colloidal stability can be most effectively preserved by addition of low amounts of poloxamer 188" | 7 routes incl. IV, ophthalmic, intratympanic (45 rows) | **None** |

**Every single component of the best-evidenced EV stabilisation buffer has
zero nasal precedent.** Not one of the five appears in the nasal IID. Three
of them (sucrose, poloxamer 188, albumin) have substantial precedent by other
routes, which helps a safety argument but does not supply the route-specific
prior use FDA's guidance describes. HEPES has no US excipient precedent by
any route.

This is the single most consequential finding of this run, and it is not a
gap that can be closed by choosing more carefully. It means one of three
things has to happen, and the choice is a development-strategy decision, not
a formulation one:

- **Qualify the excipients for the nasal route.** Trehalose in particular is
  well characterised, orally ubiquitous, and has parenteral precedent; a
  nasal-route safety qualification is a real but tractable package. It is
  also work, cost, and time that a formulation with only precedented
  excipients would not incur.
- **Substitute within the nasal-precedented set** and accept whatever
  stability that costs. Section *Stabilisers* below identifies the only two
  plausible substitutes.
- **Move the stabiliser out of the dosage form** by lyophilising, so the
  sugar is in a cake reconstituted at the point of use rather than in a
  standing aqueous nasal spray. This changes the presentation decision, which
  is [`presentation-and-device.md`](presentation-and-device.md)'s territory
  and does not exist yet.

## Buffer and target pH

**The nasal mucosa's actual pH is higher than the formulation literature
usually says, and that is good news here.** Secondary reviews of nasal
delivery routinely give the tolerated range as 5.0–6.5. The primary in-vivo
measurement does not say that. Washington et al. 2000 (*Int J Pharm*
198:139–146, PMID 10767563) placed miniature pH electrodes 3 cm apart in the
nasal cavities of twelve healthy volunteers and recorded a 30-minute
stabilised baseline: **anterior nasal pH 6.40 (+0.11, −0.15 SD), posterior
6.27 (+0.13, −0.18 SD)**, with considerable inter- and intra-subject
variation. The same study sprayed 100 µL of buffered isotonic solutions and
found nasal anterior pH could be pulled down only by buffers at 0.13 M and
above — i.e. a low-molarity buffer does not override the nose.

**The active wants neutral.** Trenkenschuh et al. 2022 found "less
aggregation and/or vesicle fusion occurred at neutral pH compared to slightly
acidic or alkaline pH," and specifically that **potassium phosphate buffer
outperformed sodium phosphate buffer and PBS** for EV colloidal stability on
freeze-thaw.

**Those two do not actually conflict, which is worth stating plainly rather
than dramatising.** The brief asks what to do when the mucosa's tolerated
range and the active's stability optimum disagree. Here they nearly meet:
measured mucosal pH is 6.3–6.4, the active prefers neutral, and the gap is
under a pH unit. It is also already bridged by approved practice — **SPRIX
(ketorolac tromethamine nasal spray, NDA 022382) is formulated at pH 7.2**,
stated on its own label. An approved nasal spray sits at pH 7.2 today.

**Proposed: 10 mM potassium phosphate, target pH 7.0–7.2.**

| Element | Choice | Precedent | Confidence |
|---|---|---|---|
| Buffer species | Monobasic potassium phosphate / dibasic sodium phosphate | IID nasal: `MONOBASIC POTASSIUM PHOSPHATE` (SOLUTION, 680 mg; SPRAY), `SODIUM PHOSPHATE, DIBASIC, ANHYDROUS` (SPRAY, SPRAY METERED). In approved products: TOSYMRA (NDA 210884) uses potassium phosphate monobasic + sodium phosphate dibasic anhydrous; SPRIX (NDA 022382) uses monobasic potassium phosphate | **moderate** — strong nasal precedent, and independently the buffer EV freeze-thaw work favours |
| Molarity | 10 mM | Trenkenschuh et al. 2022 used 10 mM K- or Na-phosphate in the lyophilisate stable 6 months at 40 °C. Washington et al. 2000 shows ≥0.13 M is where a buffer starts overriding nasal pH — 10 mM stays well below that, which is the intent | **low** — the number is transferred from a lyophilisate study, not derived for this product |
| Target pH | 7.0–7.2 | SPRIX label, pH 7.2, approved. Trenkenschuh et al. 2022 for the neutral-pH optimum | **moderate** on acceptability, **low** on optimum for *this* preparation |
| Ruled out | Citrate | Nasal precedent is good (IID: anhydrous citric acid, citric acid monohydrate, trisodium citrate dihydrate; TOSYMRA uses citric acid monohydrate) but citrate buffers to pH 5–6, the acidic region Trenkenschuh associates with aggregation and fusion. Precedent is not a reason to buffer an active into its worst pH | **moderate** |
| Ruled out | Plain PBS | Görgens et al. 2022: severe EV recovery loss in PBS within days on storage and within minutes on dilution. Trenkenschuh et al. 2022 ranked PBS below potassium phosphate. It is also the buffer the only human intranasal EV trial's "saline, composition unstated" most likely was | **moderate** |

## Tonicity and osmolality

**Target 270–330 mOsm/kg**, taken directly from an approved label rather than
from a textbook: TOSYMRA states its osmolality is "between 270 to 330
mOsmol." That is the same actuation volume (100 µL) as SGL-001's published
dose figure, which makes it the closest available anchor.

Tonicity agent: **sodium chloride**, the most heavily precedented nasal
excipient there is (IID nasal: SOLUTION 330 mg, LIQUID 7.4 mg/mL, plus SPRAY
and SPRAY METERED entries; 224 of 694 nasal labels mention it; used in both
TOSYMRA and calcitonin-salmon nasal spray). Confidence **moderate**.

Two cautions that are not resolved here:

- **The stabiliser is also a tonicity contributor.** 25 mM trehalose adds
  roughly 25 mOsm; 5% sucrose adds roughly 150 mOsm. Whatever stabiliser
  survives the precedent problem above has to be costed into the osmolality
  budget before the NaCl level is fixed. Fixing an NaCl number now would be
  filling in a plausible figure ahead of the decision it depends on, so it is
  recorded open.
- **Ionic strength is not neutral for vesicles.** Sodium chloride is the
  precedented tonicity agent, but Görgens' PBS findings are about a
  salt-buffered system, and Trenkenschuh's preference for potassium over
  sodium phosphate suggests counter-ion identity matters more than a tonicity
  calculation captures. Whether NaCl at isotonic levels is itself a
  destabiliser for this preparation is an open bench question.

## Viscosity and mucoadhesion

The nasal-precedented viscosity and mucoadhesive agents, from the IID:

| Agent | IID nasal entry | Seen in |
|---|---|---|
| Microcrystalline cellulose / carboxymethylcellulose sodium | `CELLULOSE MICROCRYSTALLINE/CARBOXYMETHYLCELLULOSE SODIUM` — SPRAY, SPRAY METERED (no max potency listed) | Nasonex (NDA 215712), fluticasone propionate ANDAs |
| Carboxymethylcellulose sodium alone | — (listed via the co-processed entry above) | ENBUMYST (NDA 219500), labelled "viscosity control agent" |
| Hypromellose 2910 (5 mPa·s) | SPRAY and SPRAY METERED, **1 mg/1 mL** | azelastine ANDAs |
| Hypromellose 2910 (4000 mPa·s) | SPRAY, SPRAY METERED (no max potency listed) | — |
| Hydroxyethyl cellulose (2000 mPa·s at 1%) | SPRAY, 0.1 mg/0.2 mL | — |
| Pectin | SPRAY, 10 mg | — |

**Recommendation: no viscosity or mucoadhesive agent in the initial design.**
Recorded as a deliberate choice, not an omission, on three grounds:

1. **The trade-off the brief asks about is real and cuts against inclusion
   here.** Increasing viscosity coarsens the plume and shifts droplet size
   upward. For a conventional nasal product that is acceptable or even
   desirable — the EMA guideline wants "the vast majority of the particles /
   droplets ... larger than 10 microns" to keep deposition nasal rather than
   pulmonary. But SGL-001's whole premise is olfactory-region deposition, and
   [`sgl-001-spec.md`](sgl-001-spec.md) already records the primary finding
   that standard spray pumps put **under 4.6%** of dose in the olfactory
   region (Xi et al. 2016). Anything that further coarsens the plume attacks
   the one deposition number the product cannot afford to lose.
2. **No data exists on cellulose-polymer/EV compatibility.** Adsorption of
   vesicles onto a polymer network is exactly the loss mechanism Görgens
   found for plastic surfaces. Whether CMC or hypromellose does the same
   thing is unstudied as far as this search found.
3. **It is an additive, not a subtractive, decision.** A mucoadhesive can be
   added later against measured residence-time data. Removing one after a
   deposition study has been run on it is more expensive.

Confidence **low** — this is a reasoned deferral, not a tested conclusion.
Every one of the six agents above stays available with real nasal precedent
if residence time turns out to be the binding constraint.

## Permeation strategy — and why the one approved option is disqualified

**There is exactly one permeation enhancer with US nasal precedent, and it is
a detergent that dissolves lipid bilayers.**

The IID nasal list contains a single permeation-enhancing excipient:
`N-DODECYL .BETA.-D-MALTOSIDE` (SPRAY), maximum potency listed as `NA`. Its
precedent is TOSYMRA (NDA 210884), which contains **0.2% w/v** DDM — marketed
as Intravail — and reaches blood levels comparable to a 4 mg subcutaneous
sumatriptan injection because of it.

DDM is also a standard laboratory reagent for solubilising membranes. Its
critical micelle concentration is **0.17 mM**. At MW 510.6, TOSYMRA's 0.2%
w/v is 3.92 mM — **about 23× its CMC**. Above the CMC, DDM solubilises lipid
bilayers by the classical three-stage mechanism, with the lamellar-to-micellar
transition beginning at a detergent/phospholipid ratio of about
R<sub>sat</sub> = 1 mol/mol and completing at R<sub>sol</sub> ≈ 1.6 mol/mol
(dodecyl maltoside–lipid solubilisation studies, *Biophys J* 1998, PMID
9533703).

**An order-of-magnitude check against SGL-001's own published target dose.**
At the site's stated 5×10⁹ particles per 100 µL — i.e. 5×10¹⁰ particles/mL —
and taking a 100 nm vesicle with a lipid headgroup area of ~0.65 nm², a
vesicle carries roughly 9×10⁴ lipids across both leaflets, giving on the
order of **7 µM total lipid**. Against 3.92 mM DDM that is roughly **500 mol
detergent per mol lipid** — some two and a half orders of magnitude past
R<sub>sol</sub>.

Every input to that estimate is approximate and the vesicle-lipid figure is a
geometric estimate, not a measurement. It does not need to be precise. The
margin is so large that no plausible correction to particle size, lipid
packing, or particle count brings the ratio anywhere near the solubilisation
threshold. **DDM at its precedented nasal use level would be expected to
dissolve the active.**

**Decision: no permeation enhancer.** Confidence **moderate** on the
exclusion — the calculation is an inference from established detergent
physics and needs bench confirmation, but the direction is not in doubt, and
the alternative is a formulation whose enhancer and whose active are
mechanistically incompatible.

That leaves the permeation problem unsolved rather than solved, and this
document should not pretend otherwise. The consequence is that whatever
crosses the nasal epithelium has to do so unaided — which puts more weight,
not less, on the deposition question [`sgl-001-spec.md`](sgl-001-spec.md)
records as open, since with no enhancer the delivered olfactory fraction is
the entire lever.

Alternative enhancers were checked and none has nasal precedent: **chitosan
does not appear in the nasal IID and no nasal-route label mentions it**; the
only other surfactants in the nasal IID are polysorbate 80 (max 0.1 mg/mL in
metered spray), polysorbate 20, and sorbitan monolaurate, all present as
solubilisers at levels far below an enhancing dose — and all of them
surfactants, carrying the same class question against a lipid vesicle at
whatever level would actually enhance permeation.

## Preservative, or a preservative-free presentation

**The published presentation — a 10 mL multi-dose aqueous metered spray —
forces this question, and every answer to it is bad for a lipid vesicle.**

Under EMA/CHMP/QWP/49313/2005 (verified directly this run), a non-pressurised
multiple-use metered dose nasal spray requires a preservative
effectiveness/efficacy development study (Table 4.2.2, row t) and a
preservative content release test (Table 4.5.2.1, row l) — both conditional
on "if a preservative is present." Section 4.5.1.13 separately requires that
"the number of actuations per container should be demonstrated to be no less
than the labelled number of actuations."

**The precedented preservatives are all membrane-active.** The nasal IID
lists benzalkonium chloride, benzyl alcohol (5 mg/mL, metered spray),
chlorobutanol, phenylethyl alcohol, methyl- and propylparaben, potassium
sorbate, thimerosal, and phenylmercuric acetate/nitrate. BAC dominates in
practice: **535 of 694 nasal-route labels mention it.**

BAC is a quaternary ammonium cationic surfactant. Its documented nasal
toxicity is a primary finding, not an inference — Riechelmann et al. 2004
(*Am J Rhinol* 18:291–299, PMID 15586800) tested isolated human nasal
epithelia from 15 donors and 0.05% BAC in 16 healthy volunteers over 8 days
in a randomised double-blind crossover: **"In vitro, BAC was ciliotoxic
(p < 0.0001)"**, concluding that **"BAC in concentrations used in nasal
preparations is ciliotoxic."** In vivo it did not change saccharin transport
time (p > 0.8) but did cause nasal irritation (p = 0.001), burning
(p = 0.0003), hypersecretion (p = 0.006), and persistent irritation
(p < 0.01). The IID's own nasal levels — 40.46 mg/100 mL (0.04%) for
solutions, 0.2 mg/mL (0.02%) for liquids — sit inside the range that study
calls ciliotoxic.

For SGL-001 there is a second, independent problem on top of the mucosal one:
a cationic surfactant at ~0.02% is a membrane-disrupting agent placed in
continuous contact with a lipid-vesicle active for the whole in-use life of
the bottle. No study of BAC against EV preparations was found in this search,
so this is recorded as a class inference requiring bench work, not as a
measured incompatibility — but it is the same physics as the DDM finding
above, applied to an agent whose entire mode of action is membrane
disruption.

**Recommendation: preservative-free, and this is a presentation decision
before it is a formulation one.** Three approved products show the three ways
it is actually done, and none of them is a 10 mL multi-dose bottle:

| Product | How it avoids a preservative | Format | Storage |
|---|---|---|---|
| **TOSYMRA** (NDA 210884) | Single-dose disposable unit | 100 µL, one dose | 20–25 °C, excursions 15–30 °C; "Do not store in the refrigerator or freezer" |
| **ENBUMYST** (NDA 219500) | Unit-dose spray, blister-packed | 0.1 mL, one dose (12-pack carton) | 15–25 °C, excursions 4–40 °C, do not freeze |
| **SPRIX** (NDA 022382) | Multi-dose bottle with a 24-hour in-use limit — "Bottles of SPRIX should be discarded within 24 hours of priming" | 8 sprays of 100 µL per bottle | Unopened 2–8 °C; in use 15–30 °C |

**SPRIX is the closest structural analogue and the most instructive.** It is a
genuinely multi-dose, 100 µL metered, preservative-free nasal spray of a
fragile-enough active, and it buys that by refrigerating the unopened bottle
and discarding the opened one **within 24 hours**. Eight doses, one day. That
is the shape of the trade a preservative-free multi-dose nasal spray actually
makes.

**Compare with what SGL-001 publishes: a 10 mL bottle, "multiple metered
doses," and the word "shelf-stable."** For reference on how much of a nasal
bottle is even deliverable, the calcitonin-salmon label states a 2 mL fill
yields "at least 14 doses" of 0.09 mL — 1.26 mL delivered, about 63% of fill
— and a 3.7 mL fill yields 30 doses, about 73%. Applied to a 10 mL fill at
100 µL per actuation that implies roughly 63–73 deliverable doses, not 100 —
which is consistent with, and independent primary support for, the arithmetic
[`sgl-001-spec.md`](sgl-001-spec.md) used to retire the site's withdrawn
"100 doses" figure.

Confidence **moderate** on preservative-free as the right call; **none** on
the in-use period, which cannot be set without stability data.

## Stabilisers, cryoprotectants and bulking agents

This is where the precedent problem in the section above becomes a concrete
choice. Two positions, both honest, and this run does not have the data to
pick between them:

**Position A — formulate on the evidence, qualify the excipient.** Use
trehalose. It has the deepest EV-specific evidence base of any excipient
considered here: Bosch et al. 2016 (*Sci Rep* 6:36162) found 25 mM trehalose
in the isolation and storage buffer "narrows the particle size distribution
and increases the number of individual particles per microgram of protein",
with significantly reduced mean particle size (p = 0.0005) and freeze-thaw
protection across four cycles; Görgens et al. 2022 (*J Extracell Vesicles*
11:e12238) made it a component of PBS-HAT, the lead buffer of a two-year
comparison, with stability "throughout several freeze-thaw cycles";
Charoenviriyakul et al. 2018 (*Int J Pharm* 553:1–7) found "lyophilization
without cryoprotectant resulted in the aggregation" of exosomes "while the
addition of trehalose ... prevented aggregation," with retained activity for
about 4 weeks at 25 °C. The cost is a nasal-route safety qualification for an
excipient with intradermal and subcutaneous IID precedent only.

**Position B — formulate inside the precedent set.** The nasal IID contains
exactly two candidates with any stabiliser function:

- **Mannitol** — `MANNITOL | SPRAY | 41.5 mg`. The only sugar or polyol with
  nasal precedent and a stated maximum potency. A standard lyophilisation
  bulking agent, but a crystallising one, which makes it a weaker
  lyoprotectant for a membrane-bearing particle than an amorphous
  disaccharide like trehalose or sucrose. No EV-specific data was found.
- **Polysorbate 80** — `POLYSORBATE 80 | SPRAY, METERED | 0.1 mg/1 mL`
  (0.01% w/v). The nasal-precedented stand-in for the poloxamer 188 that
  Trenkenschuh found most effective. But polysorbate 80's CMC is in the low
  micromolar range, so even 0.01% is above it, which is precisely the
  property that made DDM disqualifying — at a hundredth the concentration and
  with a different head group, but not obviously safe for a vesicle. This
  needs measurement, not reasoning.

**Recorded as open, with a stated preference.** Position A is better
supported by the evidence that actually exists about this active, and
excipient qualification is a known, bounded regulatory activity. Position B
is cheaper and faster and rests on nothing EV-specific at all. Choosing
Position B to avoid a qualification package, and then discovering mannitol
does not protect the vesicles, is the more expensive mistake. But this
document is not going to assert 25 mM trehalose as the answer when the
decision that governs it — aqueous spray versus lyophilised cake, which
determines whether the sugar is a cryoprotectant or just an osmolality
contributor — has not been made.

Confidence **none** on a final stabiliser selection.

## Excipients explicitly ruled out

| Excipient | Nasal precedent | Why ruled out |
|---|---|---|
| **n-Dodecyl β-D-maltoside (Intravail)** | Yes — IID nasal SPRAY; TOSYMRA at 0.2% | ~23× its own CMC and ~500 mol/mol lipid against this product's target particle concentration; a lipid-bilayer solubilising detergent placed in a lipid-vesicle product |
| **Benzalkonium chloride** | Yes — the dominant nasal preservative, 535/694 labels | Ciliotoxic at nasal use concentrations (Riechelmann et al. 2004, p < 0.0001); separately, a cationic surfactant in continuous contact with a vesicle active |
| **Plain PBS as the vehicle** | Sodium chloride and sodium phosphate both precedented | Görgens et al. 2022 — severe EV recovery loss within days on storage and within minutes on dilution; Trenkenschuh et al. 2022 ranked it below potassium phosphate |
| **Citrate buffer** | Yes — three citrate entries in the nasal IID; TOSYMRA | Buffers to pH 5–6, the acidic region associated with EV aggregation and vesicle fusion (Trenkenschuh et al. 2022). Good precedent for the wrong pH |
| **Edetate disodium (EDTA)** | Yes — 352 nasal labels; SPRIX contains it | Not excluded on toxicity — excluded as unjustified. Its usual nasal role is potentiating a preservative that this design does not have. An excipient with no function is a leachables and compatibility question with no upside |
| **Chitosan** | **No** — absent from the nasal IID and from all 694 nasal labels | Frequently proposed as a nasal permeation enhancer in the delivery literature; has no US nasal precedent whatsoever. Its cationic, mucoadhesive, membrane-interacting mode of action also raises the same vesicle question as every other enhancer here |
| **Ethanol** | Yes — IID nasal, several dosage forms | Standard EV-lysis solvent class; no plausible role in an aqueous vesicle formulation |
| **Phenylmercuric acetate / nitrate, thimerosal** | Yes — legacy IID nasal entries | Organomercurial preservatives; legacy precedent is not a reason to use one in a new product |

## The design, assembled

Nothing below has been made. Confidence key follows
[`sgl-001-spec.md`](sgl-001-spec.md): **high** = direct evidence for this
product; **moderate** = evidence for the class or a hard regulatory
constraint; **low** = derived or inferred; **none** = no basis found.

| Component | Function | Proposed | Precedent | Confidence |
|---|---|---|---|---|
| Buffer | pH control | 10 mM potassium phosphate | IID nasal `MONOBASIC POTASSIUM PHOSPHATE`; TOSYMRA (NDA 210884); SPRIX (NDA 022382); Trenkenschuh et al. 2022 | **moderate** |
| pH | — | 7.0–7.2 | SPRIX label, pH 7.2; measured nasal pH 6.27–6.40 (Washington et al. 2000); neutral-pH EV optimum (Trenkenschuh et al. 2022) | **moderate** |
| Tonicity agent | Osmolality | Sodium chloride, level **open** pending the stabiliser decision | IID nasal SOLUTION 330 mg / LIQUID 7.4 mg/mL; TOSYMRA; calcitonin-salmon nasal spray | **moderate** on the agent, **none** on the level |
| Osmolality | — | 270–330 mOsm/kg | TOSYMRA label, same 100 µL actuation volume | **moderate** |
| Viscosity / mucoadhesive | Residence time | **None** in the initial design | Deliberate deferral — plume-quality trade-off against a <4.6% olfactory deposition fraction (Xi et al. 2016, via [`sgl-001-spec.md`](sgl-001-spec.md)) | **low** |
| Permeation enhancer | Absorption | **None** | Exclusion of the only precedented option (DDM) on detergent grounds | **moderate** on the exclusion, **none** on what replaces the function |
| Preservative | Microbial control | **None** — preservative-free presentation required | TOSYMRA and ENBUMYST (unit dose); SPRIX (multi-dose, 24 h in-use); BAC ciliotoxicity (Riechelmann et al. 2004) | **moderate** |
| In-use period | — | **Open** | SPRIX's 24 hours is the closest precedent; no stability data exists for this product | **none** |
| Stabiliser / cryoprotectant | Aggregation, freeze-thaw, storage | **Open** — 25 mM trehalose on the evidence, mannitol as the only nasal-precedented substitute | Bosch et al. 2016; Görgens et al. 2022; Charoenviriyakul et al. 2018; IID nasal `MANNITOL` 41.5 mg | **none** on selection, **moderate** on trehalose's effect in the class |
| Surface-adsorption control | Recovery from container | **Open** — 0.2% HSA has the EV evidence and no nasal precedent; polysorbate 80 has nasal precedent and no EV evidence | Görgens et al. 2022; IID nasal `POLYSORBATE 80` 0.1 mg/mL | **none** |
| Bulking agent | Lyophilisate only | **Not applicable until the presentation is decided** | — | **none** |

## What needs a formulation scientist

Laboratory questions, recorded as design intent with verification marked
required, per the brief:

1. **DDM and BAC compatibility with the actual preparation.** Both exclusions
   above are physics-based inferences. A simple NTA particle-count and
   size-distribution readout before and after exposure would confirm or
   refute each in a day, and would convert the two strongest recommendations
   in this document from reasoned to measured.
2. **Polysorbate 80 at 0.01% against the vesicles.** The same test. This one
   matters more than it looks, because polysorbate 80 is the only
   nasal-precedented surfactant available for surface-adsorption control.
3. **Cellulose-polymer adsorption.** Whether CMC-Na or hypromellose strips
   vesicles from solution the way plastic surfaces do (Görgens et al. 2022).
   If they do, the mucoadhesive option is closed permanently, not deferred.
4. **Buffer screen at the product's actual concentration.** Potassium
   phosphate vs. sodium phosphate vs. PBS, at 5×10¹⁰ particles/mL — a
   concentration two orders of magnitude above anything in the cited
   stability literature, where aggregation behaviour is least predictable.
5. **pH stability window.** "Neutral is better than acidic or alkaline"
   (Trenkenschuh) is a direction, not a specification. The width of the
   acceptable window around pH 7.0–7.2 has to be measured before a release
   specification can be written.
6. **Device–formulation interaction.** Whether shear through a metered pump
   orifice damages vesicles at all is unaddressed here and unaddressed in the
   literature found. It belongs to
   [`presentation-and-device.md`](presentation-and-device.md), and it could
   invalidate the entire spray format independently of anything in this
   document.

## What this run did not do

- **[`presentation-and-device.md`](presentation-and-device.md) still does not
  exist.** The liquid/lyophilised/frozen comparison and the device
  specification were not attempted. Three findings gathered this run feed
  directly into it and are recorded so the next run starts from them rather
  than from scratch: TOSYMRA and ENBUMYST as room-temperature unit-dose
  precedents; SPRIX as the multi-dose preservative-free precedent with a
  24-hour in-use limit; and Trenkenschuh et al. 2022's lyophilisate holding
  particle size and concentration for 6 months at 40 °C. That last is the
  only published route to anything resembling "shelf-stable" for this active,
  and it is a lyophilisate, not a spray.
- **No excipient supplier, grade, or compendial status was checked.** USP-NF
  vs. multicompendial grade, and whether a supplier will provide a
  parenteral-grade material with a DMF, is a real gating question not
  addressed here.
- **No extractables or leachables assessment.** Required by
  EMA/CHMP/QWP/49313/2005 §4.5.1.11 and unaddressed.
- **The IID's `NA` and blank maximum-potency fields were not chased.** Several
  nasal entries relied on above (the MCC/CMC-Na co-processed entry,
  hypromellose 4000 mPa·s, DDM) carry no maximum potency in the database.
  Precedent of use exists; a precedented *level* does not, and for those
  excipients the level would have to be justified independently.

## Sources

Primary sources fetched or downloaded directly this run:

- [FDA Inactive Ingredient Database, July 2026 release](https://www.fda.gov/drugs/drug-approvals-and-databases/inactive-ingredients-database-download) — downloaded in full (`IIR_OCOMM.csv`, 9,071 rows) and filtered locally to the 132 route-`NASAL` entries
- [Using the Inactive Ingredient Database, Guidance for Industry, CDER, July 2019 (draft)](https://www.fda.gov/media/128687/download) — for the route-precedent principle and the BLA-exclusion footnote
- [openFDA drug label API](https://api.fda.gov/drug/label.json), `openfda.route:"NASAL"` — 694 labels; counts by excipient and by application type
- [TOSYMRA (sumatriptan) nasal spray label, NDA 210884](https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=7260d567-3824-230d-836d-8065302baaec)
- [Calcitonin salmon nasal spray label (Miacalcin, NDA 020313)](https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=c82eb602-12e1-692b-d660-f8d5b5736b54)
- SPRIX (ketorolac tromethamine) nasal spray label, NDA 022382 — via openFDA label record
- ENBUMYST (bumetanide) nasal spray label, NDA 219500 — via openFDA label record
- BAQSIMI (glucagon) nasal powder label, NDA 210134 — via openFDA label record
- [EMEA/CHMP/QWP/49313/2005 Corr, Guideline on the Pharmaceutical Quality of Inhalation and Nasal Products](https://www.ema.europa.eu/en/documents/scientific-guideline/guideline-pharmaceutical-quality-inhalation-and-nasal-products_en.pdf) — Tables 4.2.2 and 4.5.2.1, §4.5.1.11, §4.5.1.13, §4.2.1.20, read directly
- `sgl001.signal.clinic`, fetched 2026-09-03

Primary literature (abstracts and, where accessible, full text):

- Washington N, Steele RJ, Jackson SJ, et al. "Determination of baseline human nasal pH and the effect of intranasally administered buffers." *Int J Pharm* 2000;198:139–146. [PMID 10767563](https://europepmc.org/abstract/MED/10767563)
- Riechelmann H, Deutschle T, Stuhlmiller A, Gronau S, Bürner H. "Nasal toxicity of benzalkonium chloride." *Am J Rhinol* 2004;18:291–299. [PMID 15586800](https://europepmc.org/abstract/MED/15586800)
- Görgens A, Corso G, Hagey DW, et al. "Identification of storage conditions stabilizing extracellular vesicles preparations." *J Extracell Vesicles* 2022;11:e12238. [PMC9206228](https://pmc.ncbi.nlm.nih.gov/articles/PMC9206228/)
- Trenkenschuh E, Richter M, Heinrich E, Koch M, Fuhrmann G, Friess W. "Enhancing the stabilization potential of lyophilization for extracellular vesicles." *Adv Healthc Mater* 2022;11:e2100538. [PMID 34310074](https://europepmc.org/abstract/MED/34310074)
- Charoenviriyakul C, Takahashi Y, Nishikawa M, Takakura Y. "Preservation of exosomes at room temperature using lyophilization." *Int J Pharm* 2018;553:1–7. [PMID 30316791](https://europepmc.org/abstract/MED/30316791)
- Bosch S, de Beaurepaire L, Allard M, et al. "Trehalose prevents aggregation of exosomes and cryodamage." *Sci Rep* 2016;6:36162. [PMC5099918](https://pmc.ncbi.nlm.nih.gov/articles/PMC5099918/)
- Dodecyl maltoside–lipid solubilisation and the R<sub>sat</sub>/R<sub>sol</sub> transition: *Biophys J* 1998, [PMID 9533703](https://pubmed.ncbi.nlm.nih.gov/9533703/)

## Provenance

**Input status.** This document was built this run from the primary sources
listed above. The IID and the EMA guideline were downloaded and parsed
locally rather than read through a summary. The five product labels were read
as labels. `sgl001.signal.clinic` was fetched directly on 2026-09-03 for the
Conflicts section rather than relied on from
[`sgl-001-spec.md`](sgl-001-spec.md)'s 2026-09-01 check.

**Not independently re-verified this run.** Two figures are carried in from
[`sgl-001-spec.md`](sgl-001-spec.md) and were not re-fetched from their own
primary sources: the Ahmadian et al. 2024 freeze-thaw loss figures (23–36%
per cycle) and the Xi et al. 2016 olfactory deposition fraction (<4.6%). Both
are load-bearing here — the first for the Conflicts section, the second for
the decision to omit a mucoadhesive — and both should be re-checked against
their own publications if either becomes contested.

**Read only as an abstract.** Trenkenschuh et al. 2022 and Charoenviriyakul
et al. 2018 were read as abstracts via Europe PMC, not full text. The
Trenkenschuh abstract's statements about potassium versus sodium phosphate,
neutral pH, and poloxamer 188 are quoted from it directly, but the underlying
concentrations, EV sources, and effect sizes were not examined. The buffer
recommendation in this document rests substantially on that abstract, so this
matters.

**Computed here, not cited.** The ~500 mol DDM per mol lipid ratio and the
~7 µM lipid concentration are this run's arithmetic from the site's published
target dose and standard bilayer geometry, not values from any source. The
inputs are stated in the text so the calculation can be checked or discarded.

**Not found rather than absent.** No study of benzalkonium chloride, or of
any nasal preservative, against extracellular vesicle preparations was found
in this search. That is a negative search result, not evidence that no such
study exists.
