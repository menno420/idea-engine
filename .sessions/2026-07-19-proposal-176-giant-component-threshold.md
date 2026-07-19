# PROPOSAL 176 — giant-component phase transition: the largest cluster snaps from vanishing to macroscopic as average degree crosses 1 (P176 → V189, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD (active).** This card lands first as `in-progress` to hold the substrate-gate red while the proposal is authored and the verifier proven; the final commit flips it to `complete`, releasing merge-on-green.

## Objective

Author PROPOSAL 176 (round-42 UNRELATED slot): a fresh, counterintuitive, quantifiable mechanism grounded in a real documented phenomenon (the Erdős–Rényi random-graph phase transition), with a stdlib-only deterministic verifier (SEED=20260717, ordered ≥3σ gates including a robustness gate under a scale shift) and a full proposal doc, then land it on green for a future VERDICT 189 (+13 offset).

## Constraints honored

- UNRELATED slot: network-science / statistical-physics phenomenon, outside fleet ops, venture econ, and games.
- Dedup: distinct from the shipped Stein/shrinkage head (P128 → V141) and the friendship-paradox size-bias head; disclosed in the doc's dedup section.
- Stdlib-only verifier; SEED=20260717 pinned; in-process double-run determinism assert.
- Digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY (compact-canonical sha256, pretty indent=2 stdout dump).
- Pre-registered ordered gates G1 → G2 → G3 at z_gate = 3.0; the gate plan matches the shipped verifier.
- Grounding URL verified reachable (HTTP 200) and documents the specific c = 1 threshold head.
- Timestamps from `date -u`; no model version identifiers.

## GROUNDING (verified at HEAD)

Erdős–Rényi random-graph evolution: in G(n, m = round(c·n/2)) the largest connected component undergoes a sharp phase transition at average degree c = 1 — order log n below, a constant fraction ρ(c) above, with ρ = 1 − exp(−c·ρ). Grounding pinned in the proposal doc: https://en.wikipedia.org/wiki/Giant_component (HTTP 200), documenting the giant component's emergence at the threshold.

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

_in-progress — filled on flip to complete._

## ⟲ Previous-session review

_filled on flip._

## 💡 Session idea

_filled on flip._
