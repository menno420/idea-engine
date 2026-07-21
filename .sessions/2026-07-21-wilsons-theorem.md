# PROPOSAL 260 — Wilson's theorem: (n−1)! ≡ −1 (mod n) ⟺ n prime

> **Status:** complete

> **📊 Model:** Claude Opus · high · idea/planning
started: 2026-07-21T15:49:08Z

💓 Heartbeat:
- round/slot: round-70 UNRELATED slot · pure mathematics / number theory · Wilson's theorem closed form
- lane: P260 → V273 (+13 offset)
- branch: claude/proposal-260-wilsons-theorem
- verifier: ideas/fleet/verify_260_wilsons_theorem.py (stdlib only: argparse, hashlib, json, math, random, fractions, sys)
- claim: For every integer n ≥ 2, (n−1)! ≡ −1 (mod n) IF AND ONLY IF n is prime. Equivalently the residue (n−1)! mod n is n−1 on primes and 0 on every composite n > 4 (sole exception n=4, 3!=6≡2 mod 4).
- SEED: 20260721 · results_sha256: 938969bc60f733cea8c9e79e5a29a7b062e661de10619aa8bcdf61719e9ba474
- determinism: in-process double-run IDENTICAL · separate re-invocation byte-identical
- G1 EXACT (integer/bignum, 0 tolerance) — Wilson predicate == independent trial-division primality over [2,1500] (checked=1499, mismatches=0) + iterated-mod == full-bignum residue over [2,400] (mismatches=0) · pass
- G2 MC agreement (|z|<3) — N=200000 iid draws of n in [2,1500]; empirical Wilson-predicate density vs exact prime density π(1500)/1499=239/1499 (π==239); p̂=0.158110, z=-1.624284 · pass
- G3 invariance/robustness (0 violations) — composite n>4 ⇒ (n−1)!≡0 (mod n); composite_nonzero_exceptions=[], n=4 residue=2 · pass
- G4 falsifiability (reject at |z|>3) — sign-flip foil "(n−1)!≡+1 (mod n) ⟺ prime" rejected at z_foil=-193.948379; true predicate matches at z=-1.624284 on the same population · pass
- all_pass: true · first_failing_gate: null · decision: PASS

⏳ Flip note (born-red): this card commits FIRST with Status: in-progress to hold the PR red behind the substrate-gate born-red HOLD; it flips to complete as the deliberate LAST commit, after the idea doc (ideas/fleet/wilsons-theorem-2026-07-21.md), the verifier, the ## PROPOSAL 260 outbox block, the Wilson's-theorem grounding pin, the full-64 digest 938969bc60f733cea8c9e79e5a29a7b062e661de10619aa8bcdf61719e9ba474, and all four gates landed. The flip clears the born-red HOLD and releases native squash auto-merge.

## What this proposal does
Adds a fleet PROPOSAL establishing **Wilson's theorem** — for every integer n ≥ 2, (n−1)! ≡ −1 (mod n) iff n is prime — as a self-contained, exactly-verifiable pure-math closed form in the unrelated/pure-math slot. Ships a stdlib-only firsthand verifier that forces two independent oracles (exact factorial-residue vs trial-division primality) to agree through four gates.

## Method
`wilson_residue(n)` computes (n−1)! mod n by exact iterated modular reduction; `is_prime_trial(n)` is an independent trial-division test. G1 asserts the Wilson predicate equals primality on every n in [2,1500] (0 mismatches) plus a full-bignum-factorial residue cross-check on [2,400]. G2 compares the iid Monte-Carlo Wilson-predicate density to the exact prime density. G3 verifies the composite-side invariant ((n−1)!≡0 mod n for composite n>4, n=4 the sole exception). G4 rejects the sign-flipped foil.

## ⟲ Previous-session review
PROPOSAL 259 (Moore's Nim, → V272) landed the born-red + four-gate + full-64-digest choreography; this slice reuses that contract exactly and opens the number-theory head **Wilson's theorem**, grep-0 across both repos and distinct from every shipped math head (Stirling P256, Gaussian P252, Cantor P248, hashing P245, Buffon P244, coprime→6/π² P232).

## 💡 Session idea
Adjacent untaken atoms: the composite-modulus companion ((n−1)!≡0 mod n, composite n>4) as a standalone head; Wolstenholme's theorem (binom(2p,p)≡2 mod p³); Lucas' theorem for binomials mod p. All grep-checked today.
