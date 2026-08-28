# Asset scout agent — state

## 2026-08-28 — second run (revised brief: regenerative medicine, earlier stage, asset-level Gate 3, near-miss tier)

**Scope this run:** Per the operator's revised brief — regenerative medicine only (exosomes/EVs, MSC and other stem-cell therapies, secretome, cell-free products); Phase I/II and Phase II prioritised over Phase III; academic holders (university hospitals, TLOs, spinouts with no commercial arm) prioritised; Gate 3 re-scoped to asset-level; Gate 1 loosened to include recruiting-with-interim-readout and biomarker endpoints; near misses now recorded in the longlist itself, not just in state.

**jRCT retry, as instructed:** Tried again before falling back to UMIN, per the revised brief.

- **jrct.niph.go.jp direct**, including the English-interface URL (`/en-search`) — still fails at the TLS handshake stage (`SSLV3_ALERT_HANDSHAKE_FAILURE`), confirmed via both `curl` (with a browser user-agent and forced HTTP/1.1) and the browser tool's own navigation. Immediate failure (~0.04s), consistent with a hard block rather than a slow/overloaded server.
- **JPRN portal** (rctportal.mhlw.go.jp/s), simple free-word search this time (not the advanced/detailed search that failed last run) — same failure mode as last run: the request either returns a CakePHP HTTP 500 or, this time, a CloudFront 504 Gateway Timeout confirmed by title/page-text after a wait. This was tried with slower pacing (explicit waits between fill and submit) and still failed. This reads as a broad origin-server problem across the whole portal, not specific to the detailed-search request shape tested last run.

**Conclusion: jRCT is still unreachable by any route tried across two runs.** Per the brief's own instruction, this is noted and the run proceeded with UMIN-CTR. If a third run hits the same wall, it's probably worth treating jRCT as unavailable to this agent's tooling for now rather than re-spending time on it every run — flagging that judgment call for the operator rather than making it unilaterally.

**What was searched:** UMIN-CTR advanced search, Study type = Interventional, Region = Japan, keyword searches (title field) for "exosome," "extracellular vesicle," "mesenchymal stem cell," and "secretome" — deliberately not filtered by phase or recruitment status this time, per the revised scope (Phase I/II and Phase II prioritised, and Gate 1 now allows recruiting trials with an interim readout). "Exosome" and "extracellular vesicle" searches returned almost entirely diagnostic/biomarker studies (liquid biopsy for cancer), not therapeutic products — none of these are in scope (this agent scouts therapeutic assets, not diagnostics). "Mesenchymal stem cell" returned 27 interventional trials in Japan, most academic and small — this is where the real candidates came from. "Secretome" returned one trial, which was already in the MSC set.

**One asset passed all five gates — the longlist's first real entry:**

- **MSC-CM (Nagoya University, PI Wataru Katagiri)** — secretome/cell-free bone regeneration ahead of dental implant placement. Full reasoning and dossier are in [`artifacts/japan-asset-longlist.md`](../artifacts/japan-asset-longlist.md) and [`artifacts/dossiers/msc-cm-nagoya-bone-regeneration.md`](../artifacts/dossiers/msc-cm-nagoya-bone-regeneration.md) — not repeated here. Short version: two published human studies over ~10 years (2016, 2017), sole funding is a Japanese government academic grant (KAKENHI), no company found anywhere in the technology's history, and Gate 4 (patent) is recorded as genuinely open rather than assumed either way — no patent was found, which is not the same as confirming none exists.

**Four near misses — each failing exactly one gate — went into the longlist's Near miss section** rather than being dropped outright, per the revised brief:

| Asset | Failed gate | Confidence |
|---|---|---|
| KOI2 (Osaka University, epidermolysis bullosa) | Gate 3 | Genuinely uncertain — Shionogi & Co. is a named funding source alongside AMED, but the record doesn't distinguish translational co-funding from an exclusive license, and this agent isn't in a position to resolve that from public registry data alone. |
| LS-ABMSC1 (Yamaguchi University, decompensated liver cirrhosis) | Gate 2 | Genuinely uncertain — "No longer recruiting," results marked "Unpublished"/"Results Delayed" on the registry, no interim readout found. Dual-registered as jRCT2063200014, which this agent still can't reach directly — that jRCT entry might carry more than the UMIN mirror does. |
| iPS-cell-derived dopaminergic progenitors / AMCHEPRY (Kyoto University CiRA / Sumitomo Pharma) | Gate 3 | High confidence, essentially dead — carried forward from the first run, re-confirmed in scope since it's a cell therapy. Included only because it technically fails one gate. |
| TEC scaffold-free construct (Osaka University / Twocells / Chugai) | Gate 3 | High confidence, essentially dead — already Phase III with pharma backing (Osaka University's own Dec. 2017 press release). Included only because it technically fails one gate. |

**A false lead worth recording so it isn't re-chased:** a ClinicalTrials.gov search surfaced NCT00420134, a similarly-named autologous MSC liver-cirrhosis trial, which looked at first like it might be an earlier US registration of Takami's work. Checked directly — it's an unrelated trial at Shahid Beheshti University of Medical Sciences, Tehran, Iran. Not connected to LS-ABMSC1 or Yamaguchi University at all. No US registration was found for the actual LS-ABMSC1 program.

**Assets found but ruled out of scope (not screened against the gates) under the revised regenerative-medicine-only domain:** KP-100IT (recombinant HGF drug, not a cell/EV/secretome product), ITK-1 (peptide vaccine), SI-657 (chondroitinase enzyme), and NPC-18/FBG-18/Retympa (recombinant single growth factor + scaffold — judged closer to a standard biologic-device combination than a secretome/cell-free regenerative product as the revised brief defines it, though this is an edge call the operator may want to revisit). All four were screened in depth on the *previous* run under the old, broader domain; none are re-litigated here since they're out of this run's scope regardless of gate outcome.

**Not yet screened:** UMIN-CTR keyword searches for "iPS," "induced pluripotent," "cell-free," and Japanese-language equivalents (エクソソーム, 間葉系幹細胞, 再生医療) — English-only title-field search this run likely misses Japanese-only-titled entries. PMDA's ASRM (再生医療等安全性確保法) committee filings and provisional-plan notifications, specifically called out in the revised brief, were not reached this run — this is the single biggest gap against the revised brief's own stated priorities and should be first on the next run. University TLO sites were not checked directly.

**Open questions carried forward:**

- Whether jRCT should be treated as unreachable going forward, or retried a third time, is an operator call — noted above rather than decided here.
- KOI2's Shionogi relationship and LS-ABMSC1's jRCT-only result status are both answerable with one more piece of information each — worth prioritizing over fresh keyword searches on the next run.
- PMDA ASRM filings are unreached and were the revised brief's most specific new source — next run should start there, not repeat the UMIN keyword sweep.
- Japanese-language keyword search on UMIN-CTR (and jRCT, if it becomes reachable) has not been tried and may surface academic trials that never got an English title worth indexing well in search engines — exactly the kind of stalled asset this agent exists to find.
