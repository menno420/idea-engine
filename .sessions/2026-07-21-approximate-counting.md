# PROPOSAL 261 — Morris approximate counting: unbiased estimator E[2^C−1]=n, Var=n(n−1)/2

> **Status:** in-progress

> **📊 Model:** Claude Opus · high · idea/planning
started: 2026-07-21T16:21:19Z

💓 Heartbeat:
- round/slot: round-71 UNRELATED slot · probabilistic streaming / sketch algorithms · Morris approximate counting closed form
- lane: P261 → V274 (+13 offset)
- branch: claude/proposal-261-approximate-counting
- verifier: ideas/fleet/verify_261_approximate_counting.py (stdlib only: argparse, hashlib, json, math, random, fractions, sys)
- claim: A base-2 Morris counter C starts at 0; to process one increment draw u ~ Uniform(0,1) and set C := C+1 iff u < 2^(−C), else leave C unchanged; after n increments N̂ = 2^C − 1. It is EXACTLY unbiased — E[2^C] = n+1, so E[N̂] = n — with EXACT variance Var[N̂] = Var[2^C] = n(n−1)/2, from E[4^C] = 1 + 3n(n+1)/2.
- SEED: 20260721 · results_sha256: ade24bf035bcc213d144494660998ed207ddae62b00e0a36879643b5a98239e6
- verifier file sha256: fdc06e07bbce31a877e56e00ddc78cb5232142656878a7fd1b1a09b82765f71e
- determinism: in-process double-run IDENTICAL · --selfcheck byte-identical · separate re-invocation byte-identical
- G1 EXACT (fractions.Fraction, 0 tolerance) — full-pmf rational DP over n=0..80; per-n assert E[2^C]==n+1, E[N̂]==n, E[4^C]==1+3n(n+1)/2, Var[N̂]==n(n−1)/2, and Σ pmf==1; checked=405, mismatches=0 · pass
- G2 MC agreement (|z|<3) — n=63, M=300000 iid replicas; mean=62.945547, honest iid SE=0.080218, z=−0.6788; sample variance 1930.5012 within 0.9885× the exact 1953 · pass
- G3 invariance (0 violations + second scale) — martingale increment E[2^{C_{n+1}}]−E[2^{C_n}]==1 over n=0..79, martingale_violations=0; second scale n=31, M=300000, mean2=30.958720, z2=−1.0545 · pass
- G4 falsifiability (reject at |z|>3, same n=63 sample) — primary foil "forgot the −1" est=2^C rejected at z_foil=11.7871 (mean 63.945547 = 62.945547 + 1 exactly); secondary foil raw counter est=C rejected at z=−36771.5913 (mean 5.737313 ≈ log2 63); true estimator accepted at z=−0.6788 · pass
- all_pass: true · first_failing_gate: null · decision: PASS

⏳ Flip note (born-red): this card commits FIRST with Status: in-progress to hold the PR red behind the substrate-gate born-red HOLD; it flips to complete as the deliberate LAST commit, after the idea doc (ideas/fleet/approximate-counting-2026-07-21.md), the verifier, the ## PROPOSAL 261 outbox block, the Approximate-counting grounding pin, the full-64 digest ade24bf035bcc213d144494660998ed207ddae62b00e0a36879643b5a98239e6, and all four gates landed. The flip clears the born-red HOLD and releases native squash auto-merge. NO control/status.md heartbeat edit, NO ## VERDICT block, NO verdict / proposal high-water advance from this worker; NO merge API calls (merge-on-green automation lands the PR once the HOLD is released).

## What this proposal does
Adds a fleet PROPOSAL establishing **Morris's approximate counting algorithm** (the base-2 Morris counter) as a self-contained, exactly-verifiable streaming/sketch closed form in the unrelated/probabilistic-algorithm slot. Although the counter is an approximation of the count, its first two moments are EXACT: the estimator N̂ = 2^C − 1 is exactly unbiased (E[N̂] = n) with exact variance Var[N̂] = n(n−1)/2. Ships a stdlib-only firsthand verifier that proves both by computing the full rational pmf of C_n in fractions.Fraction, then confirms them by an iid Monte-Carlo at two scales, exhibits the martingale-increment structure, and rejects two naive foils.

## Method
`exact_pmf_sequence(nmax)` builds the full pmf of C_n by the rational-DP transition P_{k+1}(c) = P_k(c)(1 − 2^{−c}) + P_k(c−1) 2^{−(c−1)}; `moment_2c`/`moment_4c` read off E[2^C] and E[4^C] as exact Fractions. G1 asserts the four exact identities plus Σ pmf == 1 per n over n=0..80 (checked=405, mismatches=0). `morris_batch(n_inc, replicas)` re-seeds random.seed(SEED) and runs iid replicas, accumulating exact-integer sufficient statistics (Σ est, Σ est², Σ C, Σ C²) so the digest is float-order-independent; G2 (n=63) confirms the mean, G3(b) a second scale (n=31), G4 reuses G2's sample to reject the two foils. G3(a) checks the martingale increment on the exact pmf moments.

## ⟲ Previous-session review
PROPOSAL 260 (Wilson's theorem, → V273) landed the born-red + four-gate + full-64-digest choreography; this slice reuses that contract exactly and opens the streaming/sketch head **Morris approximate counting**, grep-0 across both repos ("approximate counting"/"approximate counter"/"probabilistic counting" = 0/0) and distinct from every shipped math head (Wilson P260, Stirling P256, Gaussian P252, Cantor P248, hashing P245, Buffon P244, coprime→6/π² P232). Carries the grounding-honesty discipline: the page states the increment rule, the 2^c estimator, and qualitative unbiasedness verbatim, so the firsthand contribution is the exact-moment apparatus (E[2^C]=n+1, Var=n(n−1)/2), and the off-page −1 correction is disclosed and pinned as the G4 primary foil rather than glossed.

## 💡 Session idea
Adjacent untaken atoms: the **relative-error / concentration** leg of the Morris counter (the (1+ε,δ) guarantee via averaging M independent counters, Var of the mean = n(n−1)/(2M)); the **Morris+ / Morris++** base-b variant (increment probability (1+a)^{−c}, tunable variance n(n−1)/(2·(1/a))); and **HyperLogLog** (the distinct-count sketch listed under the page's "See also"). All grep-checked today (grep-0).
