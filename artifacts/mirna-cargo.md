---
slug: mirna-cargo
title: miRNA Cargo in Regenerative EVs
description: A two-tier synthesis of the miRNAs most reported in MSC-EV and pluripotent-EV cargo — recurring pathways, the chassis-matching implication, the Chevillet stoichiometry controversy, and the caveats that come with a secondary synthesis.
updated: 2026-08-31
status: v1
domain: route
agent: literature
---

# miRNA cargo in regenerative EVs

Structured data: [`artifacts/data/mirna-cargo.json`](data/mirna-cargo.json) — 24 miRNAs, one object per entry, machine-readable. This document is the narrative read of that data, not a duplicate of it — field-level detail (targets, sources, exact citations) lives in the JSON.

## The two-tier split

The 24 miRNAs split into two tiers by what kind of source cell produces them, and what kind of regenerative effect they're reported for:

**Tier A — MSC-EV workhorse (19 entries).** miRNAs reported in mesenchymal-stem-cell-derived EV cargo, across bone-marrow, adipose, and umbilical-cord MSC sources: miR-21, -126, -132, -146a, -125b, -29, let-7, -210, -221/222, -133b, -17-92, -486-5p, -22-3p, -100-5p, -181, plus an engineered subgroup (miR-24, -19a, -410, -214-3p) that appears in the literature as deliberately loaded or genetically-induced cargo rather than native MSC-EV content. These are the miRNAs doing the work in the tissue-repair, anti-inflammatory, and pro-angiogenic literature — cardiac, wound, kidney, bone, CNS recovery.

**Tier B — pluripotency/rejuvenation (5 entries).** miRNAs from embryonic and induced-pluripotent stem cells: the miR-302 cluster, miR-371-373, the mouse-specific miR-290-295 cluster, miR-9-5p, and miR-296-5p. These skew toward cell-cycle control and self-renewal rather than tissue repair — the literature here is closer to reprogramming biology and stemness maintenance than to wound healing, with the exception of miR-296-5p, whose regenerative-vascularization relevance is borrowed from a tumor-angiogenesis literature that wasn't written with regenerative medicine in mind.

The split matters for sourcing decisions: Tier A cargo comes from adult, clinically-accessible cell sources already used in cell-therapy manufacturing; Tier B cargo comes from cell types (ESC, iPSC) that carry a different regulatory and manufacturing burden entirely. A product built on Tier B cargo is not a manufacturing variant of a Tier A product — it's a different regulatory conversation.

## The recurring pathways

Five pathway nodes recur across this cargo set. Tallied directly from the 24 entries in the JSON:

| Pathway | Count | miRNAs |
|---|---|---|
| PTEN/PI3K-Akt | 9 | miR-21, -126, -132, -17-92, -486-5p, -181, -24, -19a, -296-5p |
| Cell-cycle/senescence | 8 | miR-125b, let-7, -221/222, -100-5p, -302, -371-373, -290-295, -9-5p |
| TGF-β/SMAD | 2 | miR-29, -133b |
| Wnt/β-catenin | 2 | miR-410, -214-3p |
| NF-κB | 2 | miR-146a, -22-3p |

That's 23 of 24 entries converging on one of five nodes. The one outlier is miR-210, which sits on a hypoxia/HIF axis distinct from all five — worth flagging precisely because it's the exception, not folded into the nearest category to make the table cleaner.

Two things follow from this concentration. First, **PTEN/PI3K-Akt and cell-cycle/senescence together account for 17 of 24 entries (71%)** — the literature isn't reporting 24 independent mechanisms, it's reporting the same two or three regulatory nodes hit by different miRNAs in different tissue contexts. Second, **TGF-β/SMAD, Wnt/β-catenin, and NF-κB are each hit by only two miRNAs apiece** in this set — thin enough that a single new paper on any of those three axes would meaningfully shift the picture, whereas the PTEN/PI3K-Akt node is dense enough that individual papers don't move it much.

## The chassis-matching implication

If the effective mechanism space is really three or four pathway nodes rather than 24 independent miRNA identities, then the miRNA identity itself is partly a proxy for *which node the source cell's secretory profile happens to hit* — and the more consequential design decision is which chassis (source cell type, culture condition, engineering strategy) reliably produces cargo on the node you want, not which single miRNA to chase.

The engineered subgroup in Tier A makes this concrete. GATA-4 overexpression in the parental MSC line enriches both miR-24 and miR-19a simultaneously — two different miRNA identities, same PTEN/PI3K-Akt node, same engineering intervention, same paper. Hypoxic preconditioning enriches miR-210 specifically, on a node (hypoxia/HIF) no other cargo in this set reaches. The osteogenic application of miR-214-3p requires the *opposite* cargo (an antagomiR against the native, bone-suppressive form) from what the parental cell produces natively — the chassis has to be engineered against its own default output, not just harvested.

Read this way, "which miRNA" is close to the wrong question for a chassis-design decision. The better question is which source-cell condition (donor MSC subtype, hypoxic vs. normoxic culture, genetic modification, direct loading) reliably produces cargo on the pathway node the indication calls for — and the pathway tally above is the closest thing this synthesis offers to a map of which nodes are well-served by existing chassis strategies (PTEN/PI3K-Akt, cell-cycle/senescence) versus thin (TGF-β/SMAD, Wnt/β-catenin, NF-κB, and the single-entry hypoxia axis).

## The Chevillet stoichiometry controversy

Chevillet et al. (2014, *PNAS*) quantified both exosome number and miRNA-molecule number across five sources (plasma, seminal fluid, dendritic cells, mast cells, an ovarian cancer line) and found, on average, far less than one copy of a given miRNA per exosome — even for the most abundant miRNAs, ranging roughly 10⁻⁵ to 10⁻¹ molecules per vesicle, averaging around one copy per 121 exosomes across all samples tested. Taken at face value, this is a serious problem for the entire cargo-transfer narrative above: if a typical vesicle in a typical preparation carries less than one copy of a given miRNA, a single recipient cell taking up a single vesicle cannot receive a functionally meaningful dose of that miRNA from it, regardless of what the target/pathway/effect columns in the JSON claim.

The controversy hasn't resolved cleanly in either direction:

- **Chevillet's own paper offers an escape hatch it doesn't fully resolve.** The data are consistent with two different models producing the same low average: either (a) most vesicles carry a little miRNA each, or (b) a small subpopulation of vesicles carries a lot, and the rest carry none. Both average out to "less than one copy per vesicle," but only model (b) preserves the possibility of a functionally loaded vesicle reaching a target cell.
- **Selective sorting machinery has since been characterized.** hnRNPA2B1 was shown to recognize specific sequence motifs ("EXOmotifs") and actively sort particular miRNAs into exosomes (Villarroya-Beltri et al., 2013, *Nat Commun*); YBX1 was independently shown to be required for miRNA sorting into exosomes in both cellular and cell-free reconstitution systems (Shurtleff et al., 2016, *eLife*). Neither paper directly refutes Chevillet's bulk numbers, but both are evidence against the assumption that cargo loading is uniform and random across the vesicle population — which is the assumption model (b) above would violate in the direction that matters for functional transfer.
- **Functional-transfer studies exist alongside the stoichiometry problem, not as a rebuttal of it.** Studies like the miR-133b stroke work (Xin et al., 2013) report real biological effects following EV administration. This doesn't resolve the stoichiometry question — a demonstrated downstream effect is consistent with functionally-loaded subpopulations (model b), with cumulative effects across many vesicles and repeated dosing, or with EV cargo other than the named miRNA (protein, lipid, other RNA species) driving some or all of the observed effect. The field has not converged on which of these explains any specific functional-transfer result.

**The practical upshot for this document:** every "effect" field in the JSON describes what was observed downstream of EV administration, not a demonstrated single-vesicle delivery mechanism for the named miRNA. That gap is real, unresolved in the literature, and inherited by every entry in this file rather than being specific to one or two of them.

## Caveats

- **Loaded vs. native cargo.** Four entries (miR-24, -19a, -410, -214-3p) are engineered or genetically-induced cargo, not native MSC-EV content. Per the literature agent's standing rule, an indication demonstrated with engineered cargo does not transfer to an unloaded product — these four are flagged individually in the JSON's `caveat` field for this reason, but it bears restating here since it's easy to lose when scanning the pathway table above.
- **Family and cluster bundling.** Several entries (let-7, miR-17-92, miR-181, miR-221/222, miR-302, miR-371-373, miR-290-295) represent families or co-transcribed clusters, not single sequences. Isoform-level heterogeneity is real and, in at least two cases in this set (let-7b, miR-92a within miR-17-92), is exactly where the documented context-dependent reversals live — see below.
- **Context-dependent direction of effect.** Four entries are flagged `contextDependent: true` in the JSON: miR-146a, miR-125b, let-7 (specifically the let-7b isoform), and miR-17-92 (specifically its miR-92a member). For these, "effect" in the JSON is the commonly-cited default, not a guarantee — documented reversals exist and the deciding factor (dose, target-cell type, disease model) varies by study.
- **Species and model heterogeneity.** Several foundational citations in the JSON are not MSC-EV papers at all — they're the underlying target-validation biology (e.g., Fish et al. on miR-126 in endothelial cells, van Rooij et al. on miR-29 in cardiac tissue) that the MSC-EV literature later built on. The JSON's `caveat` field flags each of these individually; in aggregate, roughly a third of the 24 entries lean on a foundational non-MSC citation rather than an MSC-EV-specific one.
- **Mouse-only biology.** miR-290-295 is a mouse-specific cluster with no direct human ortholog (miR-371-373 is the human functional analogue, not the same sequence). Any claim built on miR-290-295 data does not transfer to a human-cell product without that substitution already having been made in the source study.

## Provenance

This is a **secondary synthesis**, assembled from general domain knowledge of the MSC-EV and pluripotent-EV miRNA literature, not from a fresh primary-source search of each of the 24 entries this run. Several `keyCitation` values in the JSON are foundational or adjacent papers rather than MSC-EV-specific ones (flagged individually where relevant), and one entry (miR-410) carries a citation that was not confidently recalled at all and is marked as such.

**Every citation in this document and in `data/mirna-cargo.json` requires verification against primary sources (PubMed, the original journal) before any claim here is used externally, cited in a public-facing document, or relied on for a formulation or regulatory decision.** This applies to the well-established foundational citations as well as the lower-confidence ones — none of them were re-checked against the primary literature this run. This is a deliberate departure from the literature agent's standing "primary sources only" rule, made explicit here rather than silently: the value of this document is the structure (tiers, pathway convergence, the chassis-matching read, the stoichiometry framing), not unverified citation precision. A follow-up primary-source pass should confirm or correct each `keyCitation` field individually before this document's status moves past v1.
