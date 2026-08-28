# Disclosure audit agent — state

## 2026-08-28 — first run

**Vendors checked (8):** Signal (`spray.signal.clinic`, homepage +
`/science`), Kimera Labs, Direct Biologics, Vitti Labs, EriVan Bio,
Stem Nova Network, BioRegenEx, Exocel Bio.

**What changed:** `artifacts/disclosure-audit.md` created from scratch —
did not exist before this run. All eleven brief fields populated for all
eight vendors. No prior rows, so nothing to compare against; the
"fields that changed since last run" column starts being meaningful on
the second run.

**What the audit found, field by field (denominator 8, not the category):**

- **Passage number: 0 of 8. Isolation method: 0 of 8. Cell line
  identifier: 0 of 8.** Not one vendor publishes any of the three. These
  are the fields that determine what is actually in the vial, and they
  are uniformly absent — including from vendors that publish a lot COA.
- **Particle count: 4 of 8** (Signal, EriVan Bio, Stem Nova, Exocel Bio).
  **Measurement method behind that count: 1 of 8** (Stem Nova, NTA, and
  it is the only vendor stating the method is run per production lot).
  A particle number with no method behind it is the single most common
  disclosure pattern in the set.
- **Sterility and endotoxin: 1 of 8** state anything, and that one
  (Stem Nova) states the tests are *covered on the lot COA* without
  publishing values. Exocel Bio's "infectious disease panel screened" and
  "sterile C-section collection" are donor and collection statements, not
  product release testing — recorded as such rather than counted.
  Signal's "0.22 µm" is a filtration step, not a sterility result, and is
  recorded the same way.
- **Storage/shipping: 2 of 8. Lot traceability: 1 of 8. COA to buyers:
  2 of 8** (Stem Nova, with every shipment; BioRegenEx, stated as part of
  a physician-portal package — the statement was recorded, the document
  was not seen).
- **Stem Nova is the only vendor in the set that discloses at the level
  the brief's field list asks for**, and it is also the only one labelled
  "topical cosmetic use only — not for injection or therapeutic use."
  Recorded as an observation about who discloses, not a claim about
  product quality either way, and not a comparison the artifact makes.

**Signal's own row:** four fields disclosed (particle count per dose,
30–150 nm, CD9/CD63/CD81, 0.22 µm filtration), seven `not disclosed`.
Signal is the only vendor in the set publishing a marker panel and a size
distribution, and one of four publishing no storage condition for a
product presented as a 100-dose multi-dose bottle. The
`## Conflicts` section records that the four published figures are the
same ones `sgl-001-spec.md` already found do not reconcile
arithmetically — this audit does not independently confirm them, and the
Conflicts section should not be dropped on a future run just because the
audit table itself looks fuller than most rows.

**Access problems, recorded for the next run:**

- `organicell.com` 301-redirects to `zeoscientifix.com` (the company
  appears to have rebranded); `zeoscientifix.com` returns **HTTP 403** to
  automated fetch. No row created — an unverified row of `not disclosed`
  would be a fabricated finding, not a cautious one. Retry; if it 403s
  again, the row may need a manual read.
- `kimeralabs.com/` root returned `ECONNRESET` on first attempt;
  `/products/` fetched fine on retry. Go straight to `/products/`.
- `directbiologics.com/exoflo` 301-redirects to `/pipeline`. There is no
  public ExoFlo product-specification page; the pipeline page is
  pipeline-level only. Cite `/pipeline`.
- `vittilabs.com` has no product-specification page reachable from the
  public nav. Its row is company-level pages only, which is why every
  characterisation field is `not disclosed` — that is a fact about the
  site's structure as much as about its disclosure.

**Open questions carried forward:**

- **The set is eight, assembled by public search plus vendors already
  named in this repo.** It is not a census and the aggregate counts must
  never be published as if it were. If the count row is ever used in a
  post, the denominator goes with it. Expand the set before the ratios
  are treated as a category-level fact.
- Not reached this run: Zeo ScientifiX (403, above), Rion/Purexo,
  Predictive Biotech, Regenerative Labs, and the Korean supplier segment
  that turned up repeatedly in search and appears to be a large part of
  the aesthetics-side market.
- Several vendors state a COA exists behind a portal or on request. The
  brief bars anything gated or obtained under false pretences, so those
  documents will stay unseen. That is a permanent ceiling on this
  audit — the artifact says so, and the row records the *statement* that
  a COA exists, never the contents. Worth telling the operator directly
  that "COA available" and "COA contents verified" are different
  columns and only the first is reachable from here.
- The brief's rule about updating a row when a vendor later publishes
  what was missing needs a diff to work against. From next run, record
  per-vendor field changes explicitly, including a vendor going the other
  way and removing a figure.
- Signal's `/diagnostic` page and `agent.signal.clinic` were not audited
  — both are linked from the homepage and neither looked product-facing,
  but that was a judgement made without fetching them. Check next run.
