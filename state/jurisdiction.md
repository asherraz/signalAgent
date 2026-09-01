# Jurisdiction agent — state

## 2026-09-01 — site re-check: SB 1768 citation withdrawn

**Trigger:** operator report that the product site no longer cites SB 1768 as its legal basis. Verified directly against the live page (now `sgl001.signal.clinic` — `spray.signal.clinic` redirects here) before editing the artifact, rather than taking the report on trust — this repo's primary-sources-only rule applies to the operator's own claims about the site the same way it applies to any other source.

**What changed:** the §05 "Launching in Florida" section and the footer both previously named "Florida SB 1768" verbatim (fetched 2026-08-27); as of this check, neither does. The footer now carries a general development-stage disclaimer instead. This resolves the specific conflict this artifact recorded — a statute cited for a use its own text doesn't cover — because the citation is gone, not because the underlying scope question was answered. Moved the finding to a new `## Resolved` section and kept the statutory-scope analysis (indication scope, product-type/HCT/P exclusion) as a standing reference under its own heading, since that analysis is about Florida law generally and doesn't depend on whether Signal's site currently cites the statute.

**What stayed open:** the site still makes no mention of federal law, IND status, or FDA review anywhere — unchanged, still the live Conflicts entry. The underlying statute and FDA guidance were not re-fetched this run; only the site text was checked, so the Map table's "Last checked" dates are unchanged.

## 2026-08-27 — first run

**Jurisdictions checked:** Florida, US federal (in full, per brief's first-run instruction).

**What changed:** Both rows created from scratch; `artifacts/jurisdiction-map.md` did not exist before this run.

**What was found:**

- Florida SB 1768 (enacted as Fla. Stat. §§458.3245 / 459.0127, eff. 7/1/2025) authorizes unapproved stem cell therapy **only** for orthopedics, wound care, or pain management. Cognitive/neuro is not in the enumerated list — the statute is silent on it, not permissive.
- SB 1768's own definition of covered products excludes "secreted or extracted human products" (§458.3245(2)(a)3.), language drawn near-verbatim from 21 CFR 1271.3(d)(3). FDA has already construed the identical federal exclusion to put secreted products (in that case, amniotic fluid) outside HCT/P status entirely, requiring full drug/biologic review instead (Kimera Labs warning letter, 9/1/2023, footnote 1). Exosomes are secreted vesicles. Whether Florida's Board of Medicine would read its parallel language the same way is untested — recorded as an open ambiguity, not resolved in Signal's favor.
- Federally: no exosome product is FDA-approved for any indication. FDA's Dec. 2019 Public Safety Notification and July 2020 Consumer Alert both state exosome products intended to treat disease/conditions require premarket review under PHS Act §351 / FD&C Act; the Consumer Alert names neurological disorders (Alzheimer's, Parkinson's, ALS, MS, epilepsy, stroke) explicitly among indications with zero approved products.
- Checked spray.signal.clinic directly (fetched 2026-08-27, resolves fine over HTTP/1.1 — HTTP/2 connection hung, noted for future runs). Site cites "Florida SB 1768" as its stated legal basis for launch while marketing exclusively cognitive/neuro claims (brain repair, cognitive clarity, focus, working memory, mood, drive). This contradicts the statute's enumerated scope and, independently, may not even involve a product SB 1768's definition reaches. Written up in full in the artifact's `## Conflicts` section — that section should not be softened in future runs without a new primary source that changes the analysis.
- Site makes no reference to federal law, IND, or FDA status anywhere.

**Open questions carried forward:**

- No Signal X/Twitter account was located to check for the same "SB 1768" claim the brief flags as a risk. Need a handle from the operator or a search pass next run.
- No Florida Board of Medicine advisory opinion, disciplinary action, or rule (the statute authorizes the Board to adopt implementing rules — §458.3245(10)) was found addressing exosomes specifically. Worth a recheck — rules could be adopted at any time and would directly resolve the scope ambiguity noted above, in either direction.
- Whether Signal (or Kimera Labs, or any other FL exosome manufacturer) has an IND on file was not checked — that's a company-specific compliance question, arguably out of scope for this map, but worth flagging to the operator since it's the single fact that would change the federal row's "Status" from prohibited to conditional-under-IND.
- Texas is next per the brief's jurisdiction list; not started this run.

**Sources fetched this run (primary only):**

- SB 1768, Enrolled (2025), flsenate.gov — full text pulled and parsed directly, not summarized from a secondary source.
- FDA Public Safety Notification on Exosome Products (12/6/2019)
- FDA Public Safety Alert (MedWatch mirror of the above, posted 12/9/2019)
- FDA Consumer Alert on Regenerative Medicine Products Including Stem Cells and Exosomes (dated 7/22/2020, content current as of 4/9/2024)
- FDA Warning Letter, Kimera Labs Inc., MARCS-CMS 649343 (9/1/2023, content current as of 1/4/2024)

Note: FDA pages 404 through the standard WebFetch tool (blocked on user-agent); direct curl with a browser UA succeeded at 200. Future runs on fda.gov should go straight to curl rather than losing a round-trip to WebFetch first.
