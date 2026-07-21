# PROPOSAL 236 — counting necklaces of n beads in k colours under rotation (cyclic group C_n): the exact orbit count is N_k(n) = (1/n)·Σ_{d|n} φ(d)·k^(n/d), refuting the naive "divide by the group order" rule N = k^n/n

> **Status:** in-progress

> **📊 Model:** Claude Opus · high · idea/planning
started: 2026-07-21T00:17:50Z

💓 Heartbeat:
- round/slot: fleet · combinatorics / group-action orbit count (necklaces, Burnside/Pólya)
- lane: P236 → V249 (+13 offset)
- branch: claude/proposal-236-necklace-burnside
- verifier: ideas/fleet/verify_236_necklace_burnside.py (stdlib only)
- SEED: 20260717 · results_sha256: 4ce987eb3da551811389d54d5d70f72ec27cadcd8600efc73320ad9860938ece
- determinism: in-process double-run IDENTICAL · separate re-invocation byte-identical
- G1 EXACT orbit count via fractions.Fraction — 5-instance panel (6,3)=130,(4,2)=6,(5,2)=8,(6,2)=14,(4,3)=24: Burnside Fraction (denominator==1) == brute min-rotation enumeration == expected on every row; headline Fraction(130, 1) · pass
- G2 MC agreement — 400000 uniform colourings of (6,3), unbiased estimator N_hat = k^n·mean(1/orbit_size)=129.934834 vs exact N=130, z=−0.842145, |z|<3.0 · pass
- G3 invariance — orbit count invariant to a colour relabel (cyclic +1 mod k on every bead), reproduced for (6,3) and (5,2) · pass
- G4 falsifiability — naive "N == k^n/n = 121.5" (divide by group order, ignores non-free orbits) rejected at z_reject=109.003526, |z|≥6.0 · pass
- all_pass: true · first_failing_gate: null · decision: PASS

⏳ Flip note (born-red): this card commits FIRST with Status: in-progress to hold the PR red behind the substrate-gate; it flips to complete as the deliberate LAST commit, only after the idea doc, verifier, the full-64 digest match, and all four gates land. The flip clears the born-red HOLD and releases native squash auto-merge.

## What this proposal does
Adds a fleet PROPOSAL establishing the number of distinct necklaces of n beads in k colours (rotations equivalent, the cyclic group C_n acting on bead positions) as an exact, machine-checked closed-form identity — Burnside's lemma specialised to C_n, N_k(n) = (1/n)·Σ_{d|n} φ(d)·k^(n/d) — and ships a stdlib-only firsthand verifier. Fills a confirmed gap: necklace / Burnside / Pólya cyclic-group orbit counting is untaken across both repos (grep count 0 for necklace / Burnside; the only "polya" hits are the distinct Pólya-URN reinforcement head P208 and Pólya's random-walk recurrence theorem — neither is the enumeration/orbit-count result).

## Method
Exact orbit counting over `fractions.Fraction`. For the headline (n=6, k=3): (1/6)[φ(1)·3^6 + φ(2)·3^3 + φ(3)·3^2 + φ(6)·3^1] = (1/6)[729+27+18+6] = 780/6 = 130. G1 cross-checks the closed form against a brute-force orbit count (enumerate every k^n colouring, bucket by the minimum over its n rotations) over a 5-instance panel and confirms the Fraction reduces to an integer (denominator 1); a Monte-Carlo agreement gate draws uniform colourings and estimates N via the unbiased N_hat = k^n·mean(1/orbit_size); an invariance gate confirms the orbit count is unchanged under a colour relabel; a falsifiability gate rejects the naive "divide by the group order" rule N = k^n/n = 121.5 on the same MC sample.

## ⟲ Previous-session review
PROPOSAL 235 (2×2 zero-sum minimax value, → V248) landed with the born-red + four-gate + full-64-digest choreography; this slice reuses that contract exactly and extends the shipped set into combinatorial group-action enumeration, an atom distinct from the shipped probability/combinatorics heads (Pólya urn P208, random-walk recurrence, Kaprekar, coupon collector, Efron dice).

## 💡 Session idea
Next untaken group-action / orbit-count atoms surfaced in dedup: (a) k-ary bracelets under the dihedral group D_n (rotations + reflections), B_n(k) with its even/odd split; (b) Moreau's aperiodic-necklace / Lyndon-word count M_k(n) = (1/n)·Σ_{d|n} μ(d)·k^(n/d) via Möbius inversion; (c) the colour-restricted multiset necklace count via the multinomial refinement. All grep-checked today.
