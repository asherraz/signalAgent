---
slug: challenges
title: Challenges
description: The opposing-view pass — the day's new or updated artifact, attacked for claims that don't trace to a primary source, "missing" fields that were never actually exhausted, and a named lead that may rest on assumption rather than evidence.
updated: 2026-09-01
status: in-progress
domain: challenge
---

# Challenges

A running, newest-first log of this agent's adversarial pass on each day's new or changed artifact. See [`agents/challenge.md`](../agents/challenge.md) for what this agent does and does not do — it has no write access to any artifact but this one.

## 2026-09-01 — formulation's `active-candidates.md`

Target: the same-day rewrite naming intranasal insulin as the current lead under the new four-axis criterion (mechanism, human-relevant evidence, manufacturability, regulatory tractability), per [`agents/formulation.md`](../agents/formulation.md).

**Traced.** The evidence-axis claims for every candidate trace cleanly to primary sources already cited in the artifact's own Sources section from the first run (2026-08-28): NCT01767909 (SNIFF), NCT04388982 / Xie et al. 2023, the NEJM 2021 Sikich et al. oxytocin RCT, the Syntocinon regulatory history, the NAD⁺ trials. These are stable facts (a trial's design and result don't change between runs) and re-using them without re-fetching is not the kind of "prior inference" the brief's fresh-instance-reset rule is aimed at.

The mechanism, manufacturability, and regulatory-tractability scores for the three pharmacological candidates (insulin, oxytocin, NAD⁺ precursors) do **not** trace to any source, primary or secondary, fetched in either run. The artifact's own Sources section admits this directly — it says these three axes "draw on established receptor pharmacology and each product's public approval history... rather than a fresh primary-source search." That disclosure is honest, but it means three of insulin's four axis-scores, including two of the three that separate it from oxytocin (regulatory tractability, and a large part of manufacturability), are unchecked claims this run, not traced findings. This is exactly the gap the brief's own new fresh-instance-reset clause exists to catch, on the same run it was added.

**Missing vs. premature.** `formulation-design.md` and `presentation-and-device.md` still don't exist — both required by the brief's "What it produces." This is disclosed, not hidden, and matches the first run's own stated scope-narrowing rather than a new stopped-early search, so it's not counted as a fresh gap. But it does mean "current lead" is being named before the axis (manufacturability, in the formulation-specific sense of excipient/device interaction) that would most directly threaten insulin's lead — nasal-specific permeation-enhancer formulation for a large-enough insulin dose is flagged as "a separate, real question" in the artifact's own Comparison table and then not actually assessed anywhere.

**Lead check.** The core move — ranking insulin above naive EVs because EVs fail the mechanism gate the new brief installs — is well-supported: EVs' mechanism score rests on `mirna-cargo.md`'s documented stoichiometry problem, which is a real, already-verified finding in this repo. But the EV mechanism verdict ("weak/undefined") is argued **only** from the miRNA-cargo pathway. EV cargo also includes protein and lipid content, and surface-marker-mediated signaling — neither addressed anywhere in this repo. The directional conclusion (no demonstrated single mechanism connecting EV administration to a cognitive outcome in humans) is still likely defensible — there is no dose-response biomarker or target-engagement study for any EV product cited anywhere in this repo either — but the artifact argues it from a narrower base than the confidence of the verdict implies, and doesn't say so.

Insulin's lead over oxytocin — the other mechanistically-strong candidate — turns on evidence quality and regulatory tractability, both real distinctions in the artifact's own comparison table (a null RCT for oxytocin vs. a positive controlled trial for insulin; a currently-unmarketed-in-the-US precedent for oxytocin vs. a currently-marketed drug for insulin). That comparison holds up on what's actually cited.

**Verdict.** Holds with corrections. The direction — insulin outranks EVs once mechanism is a gate — is sound and traceable. The specific axis-scores that make insulin the clear leader over the field's second-strongest mechanistic candidate (oxytocin) rest partly on undisclosed-until-challenged, unverified general knowledge rather than a checked source. And the EV mechanism score, while probably right in conclusion, is argued from one pathway (miRNA transfer) rather than the mechanism space as a whole. Neither correction changes the "current lead" call, but both should be closed — with an actual primary-source pass on insulin/oxytocin/NAD⁺ regulatory and manufacturing history, and a broader look at non-miRNA EV mechanism literature — before this artifact's verdict is treated as settled rather than provisional.
