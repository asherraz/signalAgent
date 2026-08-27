---
slug: sgl-001-spec
title: SGL-001 Specification
description: Every SGL-001 parameter with its value, the evidence behind it, a confidence rating, and the question still open — including where the published numbers do not reconcile.
updated: 2026-08-27
status: in-progress
---

# SGL-001 specification

Every number here carries its basis. "5×10⁹ particles per dose" is an
assertion; "5×10⁹ per dose, published without a stated basis, 6.25× the
highest dose ever given intranasally to a human in a registered trial,
confidence low" is a specification. Where a parameter cannot yet be
fixed, it is recorded as open. An open parameter is a task. A guessed
one is a future recall.

## Conflicts

**spray.signal.clinic (fetched 2026-08-27) now publishes four
product numbers. Two of them do not reconcile with each other, and the
dose does not reconcile with the only human evidence that exists.**

Site text, verbatim: `5×10⁹ Particles / dose`, `100 Doses / bottle`,
`0.22 µm Sterile filtration`, `10 mL · METERED SPRAY`, and
`Dose 5×10⁹ particles / 100 µL`.

**1. The container arithmetic leaves nothing for priming or dead
volume.** 100 doses × 100 µL = 10.0 mL, exactly the stated fill. A
non-pressurised multiple-dose metered nasal spray cannot deliver 100%
of its fill: it requires initial priming and re-priming actuations, and
it retains unrecoverable dead volume in the dip tube and pump chamber.
The EMA/Health Canada harmonised quality guideline treats both as
mandatory development work for this exact dosage form — Table 4.2.2
lists "Minimum fill justification" and "Initial & re-priming
requirements" as required for non-pressurised multiple-use metered dose
sprays — and sets the release requirement plainly at §4.5.1.13: "The
number of actuations per container should be demonstrated to be no less
than the labelled number of actuations." As published, 10 mL will not
yield 100 × 100 µL delivered doses. Either the fill is larger than
10 mL, the delivered dose is smaller than 100 µL, or the container
delivers fewer than 100 doses. All three cannot hold.

**2. The dose is 6.25× the highest dose ever administered intranasally
in a registered human exosome trial, and 62.5× its concentration.** The
only such trial found is NCT04388982 (Ruijin Hospital), published as
Xie et al. 2023: nine patients, three arms, **2×10⁸, 4×10⁸ and 8×10⁸
particles per administration in 1 mL of saline**, twice weekly for 12
weeks. SGL-001's published 5×10⁹ per dose is 6.25× that top arm, and
12.5× the ≥4×10⁸ the trial's own authors proposed carrying forward. On
concentration the gap is wider: 5×10⁹ in 100 µL is 5×10¹⁰ particles/mL
against that trial's 8×10⁸ particles/mL — a 62.5-fold difference. A
single published SGL-001 dose contains 26% of the cumulative particles
that trial's highest arm received across all 24 administrations; one
100-dose bottle contains 26× that entire 12-week course.

This is not an argument that 5×10⁹ is wrong. It is the observation that
it sits two orders of magnitude off the only human anchor available,
and no basis for it has been published. A dose that far above precedent
is a claim requiring evidence, and none is on the site.

**3. "0.22 µm sterile filtration" is a process step presented as a
quality attribute.** Sterile filtration is how a batch is made; sterility
(a pharmacopoeial test on the finished product) is what a release
specification records. The two are not interchangeable, and filtration
through a 0.2 µm membrane of a 30–160 nm particle population is itself
a yield-loss step that must be quantified, not a guarantee. Nothing on
the site states a sterility test, an endotoxin limit, a mycoplasma
result, a particle-count method, or any other release assay.

**4. No storage temperature and no shelf life are published anywhere,
for a product format that makes both unusually hard.** See the storage
and shelf-life rows below: the consensus storage condition for EVs is
−80°C, a single freeze-thaw cycle costs 23–36% of particles, and the
one human trial's batches were valid for 30 days. A 100-dose
multi-dose bottle is difficult to reconcile with any of that. Silence
on this point is not a neutral omission; it is the parameter most
likely to decide whether the product works at the point of
administration.

Per the map's standing rule, none of this is resolved in Signal's
favour, and none of it is softened. What Signal does about its own site
is the operator's call.

## Specification

Confidence key: **high** = direct human evidence for this product;
**moderate** = human evidence for the class, or a hard regulatory/physical
constraint; **low** = derived, scaled, or inferred; **none** = no basis
found.

| Parameter | Value | Basis | Confidence | Open question |
|---|---|---|---|---|
| **Particle count per dose** | 5×10⁹ particles / dose *(as published; not adopted here)* | Published on spray.signal.clinic with no stated derivation. The only human intranasal anchor is Xie et al. 2023 / NCT04388982: 2×10⁸, 4×10⁸, 8×10⁸ particles per administration, n=3 per arm, open-label, no control; authors concluded "a dose of at least 4×10⁸ particles could be selected for further clinical trials." 5×10⁹ is 6.25× the top arm. | **low** — the published figure has no basis; the class anchor it exceeds is itself n=9 and unblinded | On what evidence was 5×10⁹ selected? If it was scaled from a rodent study, from which one, at what body-weight assumption? Allometric scaling from a 25–30 g mouse is not arithmetic, and no intranasal EV dose-ranging study in humans has been run above 8×10⁸. |
| **Particle concentration** | 5×10¹⁰ particles/mL *(derived from 5×10⁹ / 100 µL)* | Arithmetic on the two published figures. Comparator: 8×10⁸/mL in the Xie trial — 62.5× lower. | **low** | EV preparations aggregate at high concentration; trehalose is used specifically because it "narrows the particle size distribution" and prevents freeze-induced aggregation (Bosch et al. 2016). Has aggregation been measured at 5×10¹⁰/mL, and does the size distribution still meet a 30–150 nm claim at that concentration? |
| **Doses per container** | 100 doses / 10 mL bottle *(as published; does not reconcile — see Conflicts §1)* | Published. 100 × 100 µL = 10.0 mL = the entire stated fill, leaving zero priming and dead volume. EMA/CHMP/QWP/49313/2005 §4.5.1.13 requires actuations per container ≥ label; Table 4.2.2 requires minimum-fill justification and priming/re-priming studies for this dosage form. | **none** — the arithmetic is self-contradicting | Which of the three published numbers (fill volume, dose volume, dose count) is the one that moves? |
| **Dose volume per nostril** | Open. Published as "100 µL" per dose, without stating whether that is per nostril or per administration. | 100 µL is squarely inside normal metered nasal pump range (Aptar UDS: metered dose "up to 100 µL"; Bidose: 100 µL per actuation, 200 µL per device). Clinical ceiling: ENA Clinical Practice Guideline on Intranasal Medication Administration — "The ideal volume for intranasal medication administration is 0.2–0.3 mL per nare," and "volumes greater than 1 mL per nare are not reliably absorbed and often result in medication runoff." Xie et al. used 1 mL per administration, sprayed "about once a minute for 10 min" alternating nostrils — a slow split instillation, not a single bolus. | **moderate** on the ceiling, **none** on which convention the published figure uses | Is 100 µL one actuation into one nostril, or the total across both? The two readings differ 2× in delivered dose. Separately: the volume ceiling is *why* the concentration has to be extreme — you cannot buy particle count with volume here, only with concentration, and concentration is where aggregation lives. |
| **Fraction reaching the olfactory region** | Open — and the constraint the "nose to brain" framing rests on. | Xi et al. 2016, four nasal spray pumps in an MRI-based sectional adult nasal cast: "the majority of nasal spray droplets deposited in the anterior nose while only a small fraction (less than 4.6%) reached the olfactory region," concluding "standard nasal devices are inadequate to deliver clinically significant olfactory dosages." Seifelnasr et al. 2023 reached 22.7 ± 3.7% olfactory deposition only under optimised conditions: head tilted 45–60°, nozzle 5–10°, two doses, no inhalation flow. | **moderate** (in vitro casts, not in vivo human imaging) | With a standard metered spray and no positioning protocol, the delivered olfactory dose may be under 5% of the labelled dose. Is there an administration protocol (head position, nozzle angle, breath-hold) attached to the product, and is it in the physician instructions? Positioning is part of the dose. |
| **Source cell line and passage** | Open. | Not published. Class precedent: Xie et al. used allogeneic human adipose MSCs from "healthy young adult donors'" liposuction tissue, manufactured in cGMP-compliant labs. Passage limits are not specified in that trial, and the EV-manufacturing review cited in [`cdmo-readiness.md`](cdmo-readiness.md) (Thakur & Rai 2024) does not give numerical passage thresholds either — it states only that engineered cell lines "provide a better opportunity for scale up and reproducibility." | **none** | Cell type, tissue source, donor traceability, master/working cell bank status, and a passage ceiling with a stated senescence justification. This is question 1 on the CDMO readiness list and remains unanswered. |
| **Isolation method** | Open. | Not published. Xie et al. used "precipitation and ultracentrifugation... with polyethylene glycol applied for the enrichment," reporting a yield of **3×10¹⁰–5×10¹⁰ nanoparticles from 500 mL conditioned medium**. | **none** | Which method, and what is the yield per litre of conditioned medium? At the trial's yield, one published 100-dose bottle (5×10¹¹ particles) requires **5.0–8.3 L of conditioned medium at 100% downstream recovery** — before any loss to filtration, concentration or fill. Real recovery is well below 100%, so the true figure is higher. This number, not the dose, is what sets batch cost. |
| **Filtration** | 0.22 µm sterile filtration *(published as an attribute; see Conflicts §3)* | Published. Standard for EV preparations, since most EVs are 20–150 nm and pass a 0.2 µm membrane. But sterilising-grade membranes are rated at 0.2 µm against a particle population overlapping that rating, so loss is expected and must be quantified. | **low** | What is the measured particle recovery across the sterile filtration step? A filtration step with unmeasured loss makes every upstream particle-count figure unverifiable at the point of fill. |
| **Excipients and buffer** | Open. | Not published. Xie et al. used saline, composition unstated. Evidence for doing better: 25 mM trehalose in the isolation and storage buffer "narrows the particle size distribution and increases the number of individual particles per microgram of protein," and prevents the freeze-thaw–induced aggregation seen in PBS alone (Bosch et al. 2016, *Sci Rep* 6:36162). A 50-study systematic review found "no variations... in EV concentration following storage for up to one year at −80 °C supplemented with trehalose." | **low** (class evidence is good; nothing is fixed for this product) | Is there a cryoprotectant/stabiliser in the formulation at all? For a multi-dose container there is a second, separate question: an antimicrobial preservative. EMA Table 4.5.2.1 makes preservative content a release test for multiple-use metered nasal sprays where a preservative is present — and preservatives are membrane-active, which is a direct formulation risk for lipid vesicles. |
| **Storage temperature** | Open. Evidence supports −80°C; no published value. | Systematic review of 50 studies (Ahmadian et al. 2024, *Stem Cell Res Ther* 15:453): −80°C is the consensus long-term condition; −20°C showed up to "90% loss" over 26 weeks in one report; 4°C is viable "up to 1 week"; at 37°C EVs lose "all their bioactivity after just four days." Xie et al. shipped on dry ice and stored at −80°C, thawing at room temperature before use. | **moderate** for the class, **none** for this product | −80°C storage and a 100-dose in-clinic bottle are hard to hold simultaneously. What is the actual storage condition, and what is the in-use condition once a bottle is thawed and opened? |
| **Shelf life** | Open. No published value. | Only human anchor: Xie et al. report their batches "remained valid for 30 days." Freeze-thaw is the dominant destructive variable — a single cycle costs **23–36% of particles**, three cycles 37–43% (Ahmadian et al. 2024). | **low** | Shelf life at the storage condition, *and* in-use shelf life after first actuation, are two different numbers and neither is published. For a 100-dose container the in-use number is the binding one: it determines how many of the 100 labelled doses are still on-specification when given. Stability, not potency, is what decides whether this format is viable. |
| **Container and device** | Open beyond format. Published: "10 mL · METERED SPRAY", intranasal. | Published format only; no device manufacturer, actuation volume tolerance, pump type, spray pattern, or plume geometry. Comparable qualified platforms exist (Aptar UDS unidose, up to 100 µL; Aptar Bidose, 2 × 100 µL with 25 µL/shot overfill) but these are single- and two-dose devices — the opposite architecture to a 100-dose bottle. | **low** | A multi-dose metered nasal spray is a single-patient device; a 100-dose bottle used across a clinic's patients is a cross-contamination question before it is a stability question. Is one bottle one patient? At the Xie schedule (2×/week, 12 weeks = 24 administrations) a 100-dose bottle is roughly four full courses. |
| **Analytics on every lot** | Open. Nothing published. | The applicable release set is the union of two regimes. (a) *Nasal dosage form* — EMA Table 4.5.2.1 for non-pressurised multiple-use metered dose sprays: description, assay, mean delivered dose, delivered dose uniformity, microbial/microbiological limits, sterility (if sterile), preservative content (if present), **number of actuations per container**, and particle/droplet size distribution — with the guideline requiring that "the vast majority of the particles / droplets are larger than 10 microns" to show deposition is localised in the nasal cavity. (b) *EV product* — the only human-trial precedent, Xie et al.: TEM morphology, NTA with ">80% of the particles... between 30 and 160 nm", CD63⁺/CD81⁺/CD9⁺/TSG101⁺ and calnexin⁻ by western blot, sterility negative, **endotoxin < 100 EU/mL**, mycoplasma negative. Reporting conventions follow MISEV2023 (Welsh et al. 2024, *J Extracell Vesicles* 13:e12404). | **moderate** — the required *set* is well defined by primary regulator guidance; **none** for what SGL-001 actually runs | Two distinct droplet populations are in tension: the nasal guideline wants droplets >10 µm to keep deposition nasal rather than pulmonary, while the EV specification is about 30–160 nm vesicles inside those droplets. Both must be measured; they are not the same test. And there is still no potency assay in either regime — the "Signal Index" is a marketed cognitive score, not a lot-release measurement. |

## Derived figures

Stated separately because they are arithmetic on published numbers, not
measurements, and each carries an explicit assumption.

| Figure | Value | Working | Assumption |
|---|---|---|---|
| Particles per bottle | 5×10¹¹ | 100 doses × 5×10⁹ | Both published figures hold |
| Bottle vs. the full published human course | **26×** | 5×10¹¹ ÷ (24 administrations × 8×10⁸) | Compared against the highest arm of NCT04388982 across all 24 administrations |
| One dose vs. that full course | **26%** | 5×10⁹ ÷ 1.92×10¹⁰ | As above |
| Conditioned medium per bottle | **5.0–8.3 L** | 5×10¹¹ ÷ (3–5×10¹⁰ per 500 mL) | Xie et al.'s reported yield; **100% downstream recovery**, which is not achievable — treat as a floor |
| Delivered olfactory dose per 5×10⁹ dose, standard spray | **< 2.3×10⁸ particles** | 5×10⁹ × <4.6% | Xi et al. 2016 cast data with standard spray pumps and no positioning protocol; in vitro, not in vivo |

That last row is the one worth sitting with: under standard
administration, the fraction of a labelled dose that reaches the
olfactory region may be smaller than the *entire labelled dose* of the
lowest arm of the only registered human trial.

## Sources consulted

Primary sources, fetched or extracted directly this run.

- [NCT04388982, ClinicalTrials.gov registry record](https://clinicaltrials.gov/study/NCT04388982) — Ruijin Hospital, phase I/II, intranasal allogeneic adipose MSC exosomes in mild-to-moderate Alzheimer's disease. Registry lists doses as 5/10/20 µg in 1 mL; the publication reports the same arms in particles (2/4/8 ×10⁸). The unit mismatch between a registry entry and its own publication is itself worth noting.
- Xie X, et al. "Clinical safety and efficacy of allogenic human adipose mesenchymal stromal cells-derived exosomes in patients with mild to moderate Alzheimer's disease: a phase I/II clinical trial." *Gen Psychiatr*. 2023;36(5):e101143. [PMC10582850](https://pmc.ncbi.nlm.nih.gov/articles/PMC10582850/). n=9, open-label, no control arm; authors' own stated limitations include small sample size, absence of blinding, and that the maximum tolerated dose was not determined.
- [EMA/CHMP/QWP/49313/2005 Corr, "Guideline on the pharmaceutical quality of inhalation and nasal products"](https://www.ema.europa.eu/en/documents/scientific-guideline/guideline-pharmaceutical-quality-inhalation-and-nasal-products_en.pdf) — CHMP, adopted 23 March 2006, in effect 1 October 2006, harmonised with Health Canada. PDF pulled and parsed directly; Tables 4.2.2 and 4.5.2.1 and §§4.5.1.13, 4.5.2.1 quoted above.
- Xi J, Yuan JE, Zhang Y, Nevorski D, Wang Z, Zhou Y. "Visualization and Quantification of Nasal and Olfactory Deposition in a Sectional Adult Nasal Airway Cast." *Pharm Res*. 2016;33(6):1527–41. doi:10.1007/s11095-016-1896-2 (abstract retrieved via NCBI E-utilities).
- Seifelnasr A, Si XA, Xi J. "Visualization and Estimation of Nasal Spray Delivery to Olfactory Mucosa in an Image-Based Transparent Nasal Model." *Pharmaceutics*. 2023;15(6):1657. doi:10.3390/pharmaceutics15061657.
- Ahmadian S, et al. "Different storage and freezing protocols for extracellular vesicles: a systematic review." *Stem Cell Res Ther*. 2024;15:453. doi:10.1186/s13287-024-04005-7 (50 studies).
- Bosch S, et al. "Trehalose prevents aggregation of exosomes and cryodamage." *Sci Rep*. 2016;6:36162. doi:10.1038/srep36162.
- Gänger S, Schindowski K. "Tailoring Formulations for Intranasal Nose-to-Brain Delivery." *Pharmaceutics*. 2018;10(3):116. doi:10.3390/pharmaceutics10030116 — "On average nasal mucus is cleared every 10 to 20 min."
- Emergency Nurses Association, *Clinical Practice Guideline: Intranasal Medication Administration* (PDF parsed directly) — volume-per-nare limits quoted above.
- Welsh JA, et al. "Minimal information for studies of extracellular vesicles (MISEV2023)." *J Extracell Vesicles*. 2024;13:e12404. doi:10.1002/jev2.12404 — cited for reporting convention. The publisher's full text returned HTTP 403 and the PMC copy did not surface the marker-category tables; the specific category numbering was **not** verified this run and is not relied on above.
- [Aptar Unidose (UDS)](https://aptar.com/en-us/products/pharmaceutical-uds-unidose-liquid-nasal-spray-system) and [Bidose (BDS)](https://aptar.com/en-us/products/pharmaceutical-bds-bidose-nasal-spray-system-manufacturer) nasal spray system product pages — device volumes, as a reference point only; no device is specified for SGL-001.
- `spray.signal.clinic`, fetched independently 2026-08-27 over HTTP/1.1. Published product figures quoted verbatim in the Conflicts section.

## Provenance

**Input status.** This agent's brief directs it to read
`artifacts/evidence-base.md` and `artifacts/dose-landscape.md`. Neither
exists — the literature agent has not run. Every dose figure below was
therefore sourced directly from the trial registry and the primary
publication by this agent, and should be re-checked against the dose
landscape once it exists. That is a gap in the inputs, not a substitute
for them.
