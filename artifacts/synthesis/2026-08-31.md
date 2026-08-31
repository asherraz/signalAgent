---
slug: synthesis
title: Synthesis
description: The standing four-section summary of what Signal knows about developing SGL-001, rebuilt from every public artifact and the run log on each run.
updated: 2026-08-31
status: standing
domain: synthesis
---

# Synthesis

## What changed recently

First synthesis — no prior version to diff against, so this covers everything on record in [`runs.json`](runs.json), 2026-08-27 through 2026-08-31: jurisdiction and CDMO-readiness findings, the spec's internal conflicts, formulation's first active-candidate comparison, two disclosure-audit passes plus the new Signal Disclosure Standard, two private asset-screening passes and a private commercial-targeting pass (shape only — see `runs.json`), and the miRNA cargo reference.

## What we know

The published SGL-001 spec does not reconcile with itself or precedent: the 100-dose, 10 mL bottle leaves no room for priming or dead volume; the stated 5×10⁹-particle dose is 6.25× the top arm of the only registered human intranasal EV trial (n=9, open-label, uncontrolled) and 62.5× its concentration; "0.22 µm filtration" is stated as a quality attribute though it is a process step, not a sterility result ([`sgl-001-spec.md`](sgl-001-spec.md)) — the same gap the disclosure standard records as category-wide at field 7 ([`signal-standard.md`](signal-standard.md)).

The cited legal basis does not cover the marketed use: Florida SB 1768 authorizes orthopedics, wound-care, and pain-management only, not cognitive claims, and may exclude secreted vesicles like exosomes entirely; federal law, which governs regardless, is never mentioned on the site, and no FDA-approved exosome product exists for any indication ([`jurisdiction-map.md`](jurisdiction-map.md)).

None of the seven questions a CDMO needs answered before quoting cGMP production — cell line, dose basis, analytics, batch volume, device, stability, regulatory pathway — is answerable from public materials ([`cdmo-readiness.md`](cdmo-readiness.md)).

No audited vendor, Signal included, meets the disclosure standard's minimum tier ([`signal-standard.md`](signal-standard.md), [`disclosure-audit.md`](disclosure-audit.md)).

EVs are one of eight compared actives, not a default: strongest cognitive-specific human precedent (the same n=9 trial above), weakest stability profile, no approved regulatory comparator ([`active-candidates.md`](active-candidates.md)).

24 miRNAs are catalogued as MSC-EV and pluripotent-EV cargo, converging on a few pathway nodes, but the reference is an unverified secondary synthesis pending primary-source checks, with an unresolved stoichiometry controversy attached to every entry ([`mirna-cargo.md`](mirna-cargo.md)).

## What we don't know

Source cell line, dose basis, release analytics, storage condition, shelf life, device, and federal regulatory pathway are all open ([`cdmo-readiness.md`](cdmo-readiness.md), [`sgl-001-spec.md`](sgl-001-spec.md)). Whether SB 1768 covers exosomes at all, independent of indication, is unresolved either way ([`jurisdiction-map.md`](jurisdiction-map.md)). Whether any EV-cargo miRNA reaches a target cell in a functional dose is an open literature controversy, not settled by any entry in the cargo reference ([`mirna-cargo.md`](mirna-cargo.md)).

## What it means for the product

The published product page describes numbers that do not reconcile, a legal basis that does not cover its marketed use, and a manufacturing process no CDMO can yet quote. None of this is evaluated here as good or bad — it is the state of the record. The items above are what would need to close before SGL-001 has an answerable specification.
