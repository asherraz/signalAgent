# Manufacturing agent — state

## 2026-08-27 — first run

**Scope this run:** Readiness direction only, per instruction — the
CDMO-asks-Signal side. Vendor landscape (`artifacts/cdmo-landscape.md`)
not started.

**What changed:** `artifacts/cdmo-readiness.md` created from scratch —
did not exist before this run.

**What was found:**

- Signal has no public product specification anywhere found. The only
  source is spray.signal.clinic (already fetched by the jurisdiction
  agent, 2026-08-27; not re-fetched independently this run) — it states
  the route (intranasal) and delivery format (spray), and nothing else a
  CDMO would need: no cell source, particle count/dose, analytics,
  batch size, device manufacturer, or stability data.
- Built the readiness question set from two grounded sources rather than
  assumption: a peer-reviewed review of clinical-grade EV manufacturing
  requirements (PMC11863704) and a 2024 regulatory-challenges review of
  exosome medicines (Wang et al., *Clin Transl Sci*), cross-checked
  against general biologics CDMO tech-transfer/RFQ practice
  (Drug Discovery News tech-transfer guide, PharmaSource RFQ checklist).
- Checked Lonza and Esco Aster's own EV/CDMO pages directly for a
  published client intake questionnaire — neither publishes one. Lonza
  blocked automated fetch (403); Esco Aster's page is capability
  marketing only. No CDMO appears to publish its actual RFQ form; the
  question set had to be reconstructed from manufacturing-requirements
  literature instead, and is recorded as reconstructed, not copied from
  a primary CDMO intake form.
- Result: of the 7 questions in the brief (target particle count, source
  cell line/provenance, required analytics, batch size, container/device,
  stability, market/regulatory pathway), Signal can answer 0 fully and 1
  partially (route of administration, from the device claim only — not
  the device itself). The regulatory-pathway row is worse than blank:
  the one public claim (Florida SB 1768) doesn't hold up per
  `jurisdiction-map.md`'s existing Conflicts section.

**Open questions carried forward:**

- Whether any of these seven answers exist in a Signal-internal document
  outside this repo is unknown to this agent — flagged to the operator
  rather than assumed either way.
- `artifacts/cdmo-landscape.md` (the vendor-facing side) is still not
  started. Next manufacturing slot per the rota should pick that up
  unless the readiness gaps get closed first, since landscape work
  without known specs risks recording vendors against requirements that
  don't exist yet.
- No RFI/RFQ forms have been received from any CDMO (none contacted yet),
  so nothing kept in a local gitignored file this run.

**Sources consulted this run:**

- [Global requirements for manufacturing and validation of clinical grade extracellular vesicles, PMC11863704](https://pmc.ncbi.nlm.nih.gov/articles/PMC11863704/)
- [Wang et al., "Regulation of exosomes as biologic medicines," Clinical and Translational Science, 2024](https://ascpt.onlinelibrary.wiley.com/doi/10.1111/cts.13904)
- [Drug Discovery News — CDMO tech transfer and quality agreements guide](https://www.drugdiscoverynews.com/negotiating-tech-transfer-and-quality-agreements-with-your-cdmo-17316)
- [PharmaSource — CDMO RFQ checklist](https://pharmasource.global/content/cdmo-rfq/)
- Lonza exosomes/CDMO page (fetch blocked, HTTP 403 — noted for future runs, may need a browser-UA fetch like the jurisdiction agent found for fda.gov)
- Esco Aster extracellular vesicles page (fetched successfully, no intake questionnaire found)
- `spray.signal.clinic` — not re-fetched; reused the 2026-08-27 fetch already on record in `state/jurisdiction.md` and `artifacts/jurisdiction-map.md`
