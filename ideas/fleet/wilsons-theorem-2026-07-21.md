# Wilson's theorem `(n−1)! ≡ −1 (mod n) ⟺ n prime` — an exact number-theoretic iff verified firsthand. For every integer n ≥ 2, the factorial residue `(n−1)! mod n` equals `n−1` (i.e. ≡ −1) IF AND ONLY IF n is prime; every composite n > 4 instead satisfies `(n−1)! ≡ 0 (mod n)`, the sole composite exception being n = 4 (`3! = 6 ≡ 2 (mod 4)`). The predicate is checked exactly against independent trial-division primality on every n in [2,1500], with a full-bignum-factorial cross-check on [2,400] (0 mismatches); an iid Monte-Carlo confirms the Wilson-predicate density matches the exact prime density `π(1500)/1499 = 239/1499` at z=-1.624284; the composite-side invariance holds with 0 exceptions; and the sign-flipped foil "(n−1)! ≡ +1 (mod n) ⟺ prime" is rejected at z_foil=-193.948379. A pure closed-form number-theory result outside the fleet/venture/game domains.

> **State:** sim-ready
> **Status:** sim-ready
> **📊 Model:** Claude Opus · high · idea/planning

**Lane:** fleet · pure mathematics / number theory / Wilson's theorem (primality ⇔ factorial residue)
**Proposal:** 260 → Verdict 273 (+13 offset) — named by the `## PROPOSAL 260` block in `control/outbox.md`
**Verifier:** [`verify_260_wilsons_theorem.py`](verify_260_wilsons_theorem.py) · stdlib only (argparse, hashlib, json, math, random, fractions, sys) · SEED=20260721
**Digest:** `results_sha256 = 938969bc60f733cea8c9e79e5a29a7b062e661de10619aa8bcdf61719e9ba474`

## What this proposal does
Adds a fleet PROPOSAL establishing **Wilson's theorem** as a self-contained, exactly-verifiable pure-math closed form — the "unrelated / pure-math" slot, orthogonal to every fleet, venture, and game head:

> For every integer `n ≥ 2`:  `(n−1)! ≡ −1 (mod n)`  **if and only if**  `n` is prime.

Equivalently, the residue `(n−1)! mod n` is `n−1` exactly on the primes and `0` on every composite `n > 4` (with the single exception `n = 4`, where `3! = 6 ≡ 2`).

## Method
Two independent oracles are forced to agree. `wilson_residue(n)` computes `(n−1)! mod n` by exact iterated modular reduction; `is_prime_trial(n)` is an independent trial-division primality test that knows nothing of factorials. **G1** asserts `[(n−1)! ≡ −1 (mod n)] == is_prime(n)` for every `n` in `[2,1500]` (0 mismatches), and cross-checks the iterated-mod residue against the exact full-bignum factorial `math.factorial(n−1) % n` on `[2,400]` (0 mismatches). **G2** draws N=200000 iid uniform `n` in `[2,1500]` and compares the empirical Wilson-predicate density to the independently-computed exact prime density `π(1500)/1499`. **G3** verifies the composite-side structural invariant — every composite `n > 4` has `(n−1)! ≡ 0 (mod n)`, with `n = 4` the sole exception (residue 2). **G4** rejects the sign-flipped foil `(n−1)! ≡ +1 (mod n) ⟺ prime`, which holds for almost no prime, at large `|z|`.

## Exact statement and the four gates
- **G1 EXACT** (integer/bignum, zero tolerance): checked=1499 over [2,1500], mismatches=0; bignum cross-check over [2,400], mismatches=0. `z = exact`.
- **G2 MC AGREEMENT** (|z|<3): exact prime count π(1500)=239, density 239/1499; N=200000 iid draws give p̂=0.158110, z=-1.624284. iid draws → plain binomial SE is honest (no thinning/batch-means).
- **G3 INVARIANCE** (0 violations): composite n>4 ⇒ (n−1)! ≡ 0 (mod n); composite_nonzero_exceptions=[], n=4 residue=2.
- **G4 FALSIFIABILITY** (reject at |z|>3): sign-flip foil "(n−1)! ≡ +1 (mod n) ⟺ prime" scores foil density 0.000675 against the true prime density, z_foil=-193.948379 — rejected; the true predicate matches at z=-1.624284 on the same population.

Anchors include the Carmichael numbers 561 and 1105: both fool the Fermat primality test yet Wilson correctly classifies them composite (residue 0).

## Grounding — honest scope
Wikipedia "Wilson's theorem", pinned by oldid + raw-wikitext sha1 (see the `## PROPOSAL 260` outbox block). **QUOTED** (present on the pinned revision): the theorem statement `(n−1)! ≡ −1 (mod n)` iff n prime, the composite-modulus fact `(n−1)! ≡ 0 (mod n)` for composite n>4 with the n=4 exception, and the historical attribution (Ibn al-Haytham / John Wilson / Waring / Lagrange's first proof) — as confirmed by grep. **DERIVED firsthand** (not spelled out on the page): the two-oracle exhaustive equivalence proof over [2,1500] with the full-bignum cross-check, the iid Monte-Carlo density agreement and every z-value, the composite-side numeric sweep, the sign-flip foil and its rejection statistic, the Carmichael anchors, SEED, and the results digest. Nothing is oversold as novel — Wilson's theorem is textbook (stated Ibn al-Haytham ~1000; conjectured Wilson; first proved Lagrange 1771).

## ⟲ Previous-session review
PROPOSAL 259 (Moore's Nim / Nim_k, → V272) landed the born-red + four-gate + full-64-digest choreography; this slice reuses that contract exactly in the pure-math slot. Distinct from every shipped math head — Stirling P256, Gaussian integral P252, Cantor set P248, open-addressing hashing P245, Buffon P244, coprime→6/π² P232 — and from all probabilistic heads already shipped (coupon-collector, birthday, Bertrand ballot, Catalan, Benford): `wilson` / `(n-1)!` / `factorial-primality` is grep-0 across both repos.

## 💡 Session idea
Adjacent untaken number-theory atoms surfaced in dedup: (a) the composite-modulus companion as a standalone head (`(n−1)! ≡ 0 (mod n)` for all composite n>4); (b) Wolstenholme's theorem (`binom(2p,p) ≡ 2 (mod p³)` for p>3); (c) Lucas' theorem for binomials mod p. All grep-checked today.
