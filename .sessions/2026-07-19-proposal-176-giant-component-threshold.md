# PROPOSAL 176 — giant-component phase transition: the largest cluster snaps from vanishing to macroscopic as average degree crosses 1 (P176 → V189, +13)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD (cleared).** This card landed first as `in-progress` to hold the substrate-gate red while the proposal was authored and the verifier proven; this final commit flips it to `complete`, releasing merge-on-green.

## Objective

Author PROPOSAL 176 (round-42 UNRELATED slot): a fresh, counterintuitive, quantifiable mechanism grounded in a real documented phenomenon (the Erdős–Rényi random-graph phase transition), with a stdlib-only deterministic verifier (SEED=20260717, ordered ≥3σ gates including a robustness gate under a scale shift) and a full proposal doc, then land it on green for a future VERDICT 189 (+13 offset).

## Constraints honored

- UNRELATED slot: network-science / statistical-physics phenomenon, outside fleet ops, venture econ, and games.
- Dedup: distinct from the shipped Stein/shrinkage head (P128 → V141) and the friendship-paradox size-bias head; the sole `giant component` grep hit is P105's random-mapping governance head (a different object — a fixed asymptotic constant, no phase transition), disclosed in the doc's dedup section.
- Stdlib-only verifier; SEED=20260717 pinned; in-process double-run determinism assert.
- Digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY (compact-canonical sha256, pretty indent=2 stdout dump).
- Pre-registered ordered gates G1 → G2 → G3 at z_gate = 3.0; the gate plan matches the shipped verifier.
- Grounding URL verified reachable (HTTP 200) and documents the specific c = 1 threshold head.
- Timestamps from `date -u`; no model version identifiers.

## GROUNDING (verified at HEAD)

Erdős–Rényi random-graph evolution: in G(n, m = round(c·n/2)) the largest connected component undergoes a sharp phase transition at average degree c = 1 — order log n below, a constant fraction ρ(c) above, with ρ = 1 − exp(−c·ρ). Grounding pinned in the proposal doc: https://en.wikipedia.org/wiki/Giant_component (HTTP 200, oldid 1340194064, content hash 66da05b6…) — documents the giant component's emergence at the threshold.

## Gate plan (pre-registered — matches the shipped verifier)

z_gate = 3.0, SEED = 20260717, TRIALS = 40 graphs per condition, in-process double-run byte-identical.

- **G1 — existence.** Supercritical (c=1.4, n=4000) largest-component fraction ≥ 0.30 AND subcritical (c=0.7, n=4000) fraction ≤ 0.08 AND z of the difference ≥ 3.
- **G2 — robustness (4× scale shift).** Under n: 4000 → 16000 the supercritical giant fraction stays ≥ 0.30 with z vs the 0.30 floor ≥ 3, is size-invariant (|ρ(16000) − ρ(4000)| ≤ 0.05), and the subcritical fraction shrinks with n (order log n / n → 0).
- **G3 — sharpness (placebo).** The near-threshold jump frac(1.1) − frac(0.9) exceeds the far-subcritical jump frac(0.7) − frac(0.5) by ≥ 3σ, with all sub-threshold fractions ≤ 0.15 — growth is concentrated at c ≈ 1, not linear in c.

## Probe questions

**1.** Does the supercritical giant fraction hold its value under a 4× scale-up while the subcritical fraction vanishes — an intensive phase transition, not a finite-size artifact?
**2.** Is the growth of the largest component concentrated at the c ≈ 1 threshold (a sharp jump) rather than smooth and linear in average degree?
**3.** Does the measured ρ(1.4) match the mean-field fixed point ρ = 1 − exp(−c·ρ) ≈ 0.51?

## Outcome

Complete. Verifier proven twice cross-invocation (byte-identical), `all_pass=true`, `first_failing_gate=null`, results-dict sha256 `14875022bef41594dbc8d19bd2960724d2f86f6dedcadf1b339f228915469537`. Gates: G1 z=263.375801 (sup 0.507138 vs sub 0.008025), G2 z=204.254546 vs the 0.30 floor (giant 0.511348 at n=16000, size-gap 0.004211, subcritical shrinks 0.008025 → 0.002861), G3 z=33.80426 (near-jump 0.159642 ≫ far-jump 0.001612). Grounding HTTP 200 (Wikipedia "Giant component", oldid 1340194064) — documents the c=1 threshold. Outbox PROPOSAL 176 appended (sim-ready), proposal high-water advances P175 → P176, targeting VERDICT 189 (+13). Landed on green via merge-on-green, PR #668.

## ⟲ Previous-session review

P175 (pie-rule opening trap, GAME slot, sim-ready) reads sound: clean +13 offset, pinned Wikipedia grounding (oldid + content hash), deterministic digest, 8-question probe battery. This session mirrored its outbox-block grammar, frontmatter, and born-red flow. No correction needed.

## 💡 Session idea

A companion UNRELATED head worth a future slot: "the epidemic threshold R₀=1 is the same phase transition" — on a contact network the fraction ever-infected jumps from ~0 to a constant epidemic size exactly as the basic reproduction number crosses 1, and the critical vaccination fraction is 1 − 1/R₀ (herd immunity as a percolation threshold). Distinct from this head by being about dynamic spread on a graph, not static connectivity, but the same branching-process criticality.
