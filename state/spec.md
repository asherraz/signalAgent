# Spec agent — state

## 2026-08-27 — first run

**Parameters changed:** all of them — `artifacts/sgl-001-spec.md` did not
exist before this run. Eleven parameters from the brief plus two added
(particle concentration, olfactory deposition fraction) now carry a
value, basis, confidence and open question.

**Inputs missing.** The brief directs this agent to read
`artifacts/evidence-base.md` and `artifacts/dose-landscape.md`. Neither
exists; the literature agent has not run yet. Every dose figure in the
spec was therefore sourced first-hand from the registry and the primary
publication by this agent. When `dose-landscape.md` appears, the
particle-count and concentration rows should be re-derived against it
rather than trusted as-is.

**What evidence moved the parameters:**

- `spray.signal.clinic` now publishes four hard product numbers that no
  artifact in this repo had recorded: **5×10⁹ particles/dose**,
  **5×10⁹ particles / 100 µL**, **100 doses/bottle**, **10 mL metered
  spray**, **0.22 µm sterile filtration**. The jurisdiction agent's
  2026-08-27 fetch captured the legal claims, not these; the
  `cdmo-readiness.md` table records dose and particle count as "No,"
  which was accurate to what that run recorded but is now superseded by
  the site's own figures. Flagging rather than editing another agent's
  artifact.
- **The container arithmetic does not close.** 100 × 100 µL = 10.0 mL,
  exactly the stated fill, leaving nothing for priming or pump dead
  volume. EMA/CHMP/QWP/49313/2005 §4.5.1.13 requires actuations per
  container to be no fewer than labelled, and Table 4.2.2 makes
  minimum-fill justification and priming/re-priming studies mandatory
  development items for non-pressurised multiple-use metered dose
  sprays. One of the three published numbers has to move. Written up
  unsoftened in the artifact's Conflicts section.
- **The dose sits two orders of magnitude off the only human anchor.**
  NCT04388982 / Xie et al. 2023 (*Gen Psychiatr* 36:e101143) is the only
  registered human intranasal exosome trial found: n=9, open-label, no
  control, 2/4/8 ×10⁸ particles in 1 mL saline, twice weekly, 12 weeks.
  5×10⁹ is 6.25× its top arm and 12.5× the ≥4×10⁸ the authors proposed
  carrying forward; at 5×10¹⁰ particles/mL the concentration gap is
  62.5×. Derived: one bottle = 26× that trial's full 12-week
  highest-dose course.
- **Yield is the number that sets cost, not dose.** Xie et al. report
  3–5×10¹⁰ particles from 500 mL conditioned medium. One 100-dose bottle
  (5×10¹¹ particles) therefore needs **5.0–8.3 L of conditioned medium at
  100% downstream recovery** — a floor, not an estimate.
- **Olfactory deposition is the constraint the whole "nose to brain"
  framing rests on and nobody had costed it.** Xi et al. 2016 (*Pharm
  Res* 33:1527), four spray pumps in an MRI-based adult nasal cast:
  "<4.6%" reaches the olfactory region, concluding standard nasal
  devices are inadequate for clinically significant olfactory dosing.
  22.7 ± 3.7% was reached only under optimised head position (45–60°),
  nozzle angle (5–10°), two doses, no inhalation flow (Seifelnasr et al.
  2023). Implication recorded in the artifact: under standard
  administration the delivered olfactory dose from 5×10⁹ may be
  <2.3×10⁸ particles — less than the entire labelled dose of Xie's
  lowest arm. Positioning is part of the dose.
- **Stability decides more than potency here.** 50-study systematic
  review (Ahmadian et al. 2024): −80°C is consensus, one freeze-thaw
  cycle costs 23–36% of particles, three cost 37–43%. Xie's batches were
  valid 30 days. Signal publishes no storage temperature and no shelf
  life. A 100-dose multi-dose bottle is hard to reconcile with any of
  it, and in-use shelf life after first actuation is the binding number,
  not shelf life in storage.

**What remains open:**

- Every basis question in the artifact's "Open question" column. The
  three that would move the most: what 5×10⁹ was derived from; whether
  100 µL is per nostril or per administration (a 2× difference in
  delivered dose); and whether one bottle is one patient.
- No potency / mechanism-of-action release assay exists in either the
  nasal-dosage-form regime or the EV regime. The "Signal Index" is a
  cognitive score, not a lot-release measurement, and nothing indicates
  it maps to a particle-level attribute.
- Two droplet-size populations must both be specified and are in
  tension: EMA wants "the vast majority of the particles / droplets...
  larger than 10 microns" so deposition stays nasal rather than
  pulmonary, while the EV attribute is a 30–160 nm vesicle inside those
  droplets. Different tests; neither is published.
- Sterile filtration recovery across the 0.22 µm step is unmeasured. Any
  upstream particle count is unverifiable at the point of fill until it
  is.
- MISEV2023 marker-category numbering could not be verified: the Wiley
  full text returned HTTP 403 and the PMC copy did not surface the
  category tables. The artifact cites MISEV2023 for reporting convention
  only and does not rely on the category scheme. Worth a retry next run.

**Notes for other agents:**

- **fda.gov was unreachable from this runner today** — every URL tried
  returned HTTP 404 with a 10-byte body, including the exosome safety
  notification page the jurisdiction agent successfully fetched with a
  browser UA earlier the same day. Not a user-agent problem this time.
  The Wayback snapshot of the FDA nasal spray CMC guidance
  (fda.gov/media/70857) also failed — archive.org returned 503, and
  WebFetch refuses web.archive.org outright. The EMA/Health Canada
  harmonised guideline was used instead and is a fully adequate primary
  source for nasal dosage form quality; the FDA 2002 CMC guidance is
  still worth retrieving next run for the US-specific release set.
- Thakur & Rai 2024 (PMC11863704), cited five times in
  `cdmo-readiness.md`, contains no numerical limits — no passage
  thresholds, no endotoxin limits, no storage parameters, no release
  assay list. It supports the *shape* of the questions in that artifact,
  not any figure. The manufacturing agent should know this before
  leaning on it further.

**Post drafted:** `posts/2026-08-27-olfactory-deposition-fraction.md` —
the Xi et al. 2016 <4.6% figure. Category-level, no reference to Signal.

**Sources fetched this run (primary only):**

- ClinicalTrials.gov API v2 record for NCT04388982
- Xie X, et al., *Gen Psychiatr* 2023;36(5):e101143 (PMC10582850)
- EMA/CHMP/QWP/49313/2005 Corr — PDF downloaded and parsed page by page
- Xi J, et al., *Pharm Res* 2016;33(6):1527–41 — abstract via NCBI E-utilities
- Seifelnasr A, et al., *Pharmaceutics* 2023;15(6):1657
- Ahmadian S, et al., *Stem Cell Res Ther* 2024;15:453
- Bosch S, et al., *Sci Rep* 2016;6:36162
- Gänger S & Schindowski K, *Pharmaceutics* 2018;10(3):116
- Emergency Nurses Association, *Clinical Practice Guideline: Intranasal
  Medication Administration* — PDF parsed directly
- Wang Y, et al., *Front Med* 2025;12:1625787 — MSC-EV trial dose survey
- Aptar UDS and Bidose product pages
- `spray.signal.clinic`, fetched independently 2026-08-27 over HTTP/1.1
  (HTTP/2 still hangs, as the jurisdiction agent recorded)
