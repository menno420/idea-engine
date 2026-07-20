# 100 prisoners each open half the boxes; naive independent guessing saves the group once in 10³⁰, yet a strategy that leaks zero information — just follow the chain — saves all 100 about 31% of the time, exactly 1 − (H₁₀₀ − H₅₀)

> **State:** sim-ready
> **Class:** probability · random-permutation cycle structure · counterintuitive
> **Target:** sim-lab (VERDICT 205, +13 offset)
> 📊 Model: Claude Opus · high · idea/planning
> **Grounding:** https://en.wikipedia.org/wiki/100_prisoners_problem@5e5ca1c63092d2bf6748d449a4826c91330c5a92 · fetched 2026-07-20
> **Reference (external, reachable):** [100 prisoners problem — Wikipedia](https://en.wikipedia.org/w/index.php?title=100_prisoners_problem&oldid=1355965864) — rendered article verified reachable 2026-07-20 via WebFetch (HTTP 200), stating "using the cycle-following strategy the prisoners survive in a surprising 31% of cases" and the closed form "1 − (H₁₀₀ − H₅₀) ≈ 0.31183"; source revision pinned by sha1 5e5ca1c63092d2bf6748d449a4826c91330c5a92 of the raw wikitext at oldid 1355965864 (29277 bytes, fetched live 2026-07-20). The strategy and harmonic closed form are on the page; the exhaustive-enumeration exact-match gate below is firsthand.
> **Verifier (firsthand):** ideas/fleet/hundred_prisoners.py · results-dict sha256 ebc266644b5e21cb3c3c52415abd30e907c279fed74aa8f1c7151d5be895fdcf

## The phenomenon (one line)
Give 100 prisoners one shared rule for which boxes to open — no communication, no marks, no shared randomness — and their all-or-nothing survival probability jumps from 2⁻¹⁰⁰ ≈ 8×10⁻³¹ to ≈ 0.312.

## Domain
Probability / combinatorics of random permutations — specifically the cycle-length distribution of a uniform random permutation. Outside fleet-ops, venture, and game-theory.

## The folk belief
Each prisoner opens 50 of 100 boxes, so each individually has a 1/2 chance. The events look independent, so the group's chance "must" be (1/2)¹⁰⁰ — astronomically close to zero. Adding a strategy can't help, because every prisoner still sees only 50 boxes and carries no information out of the room.

## The thesis (reasoned to its fuller form — Q-0254 duty)
The folk multiplication is wrong because the 100 survival events are massively positively correlated, and one shared convention couples them all to a single global fact about the permutation. Number prisoners and boxes 1..100; the boxes hold a uniformly random permutation π. Each prisoner starts at the box with their own number and follows the chain (open box i → it names j → open box j → …). This traces exactly the cycle of π that contains i. A prisoner finds their number within 50 opens iff the cycle they are on has length ≤ 50. Therefore **all 100 prisoners succeed together iff π has no cycle longer than 50** — one event about π, not 100 independent ones.

The probability that a uniform random permutation of 2n elements has a cycle longer than n is exactly H₂ₙ − Hₙ: the expected number of cycles longer than n is that sum, and a permutation can contain at most one cycle longer than half its length, so expectation equals probability. Hence survival = 1 − (H₁₀₀ − H₅₀) ≈ 0.31183. As n → ∞ this tends to 1 − ln 2 ≈ 0.30685 and never drops below it — the strategy keeps the whole group alive at least ~31% of the time no matter how many prisoners you add. The naive bound is not merely loose; it is wrong by ~30 orders of magnitude.

## The formal model / Pinned world (committed constants)
- N_MAIN = 100 prisoners/boxes, OPEN_MAIN = 50 opens each.
- Boxes hold a uniform random permutation π ∈ S₁₀₀ (random.Random(SEED).shuffle).
- Survival(π) ⇔ longest cycle of π ≤ 50.
- Closed form: P = 1 − (H₁₀₀ − H₅₀), Hₙ exact rational (fractions.Fraction).
- SEED = 20260717; M_TRIALS = 200000; Z_GATE = 3.0.
- Exact-enumeration probe: N_ENUM = 8, opens 4, all 8! = 40320 permutations.
- Shift sweep: N ∈ {100, 300, 1000, 3000, 10000}.

## Pre-registered gates
- **G1 — Monte-Carlo matches the closed form (≥3σ).** Simulate M=200000 permutations of S₁₀₀; survival rate p̂ must agree with p* = 1−(H₁₀₀−H₅₀) within 3 binomial σ: z = |p̂ − p*| / √(p*(1−p*)/M) < 3.0. Confirms the simulation implements the strategy; the reduction to "longest cycle ≤ 50" is what is under test.
- **G2 — Exactly-true (exhaustive enumeration ≡ closed form).** For N=8, opens 4, enumerate all 40320 permutations, count those with longest cycle ≤ 4, and assert the exact rational equals 1−(H₈−H₄). Not a sampling test: exact-fraction identity 307/840.
- **G3 — Robustness / shift.** Closed-form survival over N ∈ {100,…,10000} must stay within a band of width < 0.01, remain strictly above the 1−ln2 ≈ 0.30685 floor, below 0.32, and beat the naive 2⁻ᴺ survival by > 25 orders of magnitude. Shows the effect is not a small-N artifact: it persists and stays bounded away from zero.

## Pre-registered decision rule
sim-ready iff G1 ∧ G2 ∧ G3 all pass under SEED=20260717 with a byte-identical results-dict sha256 across an in-process double-run and a separate cross-invocation. Any gate failing, or any digest drift, blocks.

## Dry-sim results (SEED=20260717, verbatim from ideas/fleet/hundred_prisoners.py)
- G1: p_closed_form = 0.311828, p̂ = 0.311315, std_error = 0.001036, **z = 0.495079** → pass.
- G2: enumeration 307/840, closed form 307/840, **exact_match = true** (value 0.365476) → pass.
- G3: sweep {100: 0.311828, 300: 0.308517, 1000: 0.307353, 3000: 0.307019, 10000: 0.306903}, spread = 0.004925, ln2_floor = 0.306853, log10 advantage over naive = 29.596914 → pass.
- all_pass = true. Results-dict sha256 `ebc266644b5e21cb3c3c52415abd30e907c279fed74aa8f1c7151d5be895fdcf` (byte-identical across a second process).

## Reproduce
```
python3 ideas/fleet/hundred_prisoners.py
```
Prints the pretty results dict then `Results-JSON sha256: ebc266644b5e21cb3c3c52415abd30e907c279fed74aa8f1c7151d5be895fdcf`; exits 0 iff all_pass.

## Verifier
`ideas/fleet/hundred_prisoners.py`, stdlib only (hashlib, json, math, random, fractions, itertools). Digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY: the compact-canonical sha256 over the results dict is the digest, the dict carries no self field, floats rounded 6 dp, no on-disk JSON, in-process double-run asserts byte-identical.

## Why it matters
The trap is treating positively-correlated events as independent and multiplying. One shared convention can convert 100 "independent" coin-flips into a single draw from a permutation's cycle structure — collapsing a 10⁻³⁰ event into a 1-in-3. The fleet analogue: shared deterministic conventions (routing keys, hash-partitioning, retry schedules) couple per-node success into one global structural event, and the naive product-of-independents both wildly understates the good case and, symmetrically, misreads correlated failure. When agents coordinate by convention rather than by messaging, correlation is the resource — and the quantity to reason about is a structural distribution, not a product of marginals.

## Dedup
No 100-prisoners / cycle-following / permutation-cycle head exists in ideas/ (grepped monty/goat/prisoner/cycle/loop-following on origin/main; only Monty Hall and Buffon's needle were the other unoccupied classics, both distinct). Distinct mechanism from the shipped counterintuitive-probability heads: birthday and coupon-collector concern random maps/collisions, inspection and arcsine concern renewal/paths, Berkson and Simpson concern conditioning, giant-component concerns graph thresholds. This is uniquely the cycle-length distribution of a uniform random permutation and the H₂ₙ − Hₙ long-cycle law.

## Model basis (declared model-dependence — the P024 discipline)
Depends on: (a) boxes holding a uniform random permutation — adversarial placement breaks it, the result is for random, not worst-case, filling; (b) each prisoner allowed exactly N/2 opens; (c) the shared cycle-following convention, applied by every prisoner. Relax any and the number moves: fewer than N/2 opens pushes survival toward 0; adversarial placement can force 0. The claim is the exact random-permutation value, not a worst-case guarantee.

## Probe report (v0, 2026-07-20)
**1. Is the head crisp and falsifiable?** Yes — a single number (≈0.31183) with an exact closed form 1−(H₁₀₀−H₅₀) and a byte-pinned verifier; any gate failure or digest drift falsifies it.
**2. Is it counterintuitive-but-true?** Yes — the naive independent-events answer 2⁻¹⁰⁰ is wrong by ~30 orders of magnitude; the true value is ≈31%, and the coupling mechanism (one shared convention ties all survivals to a single permutation fact) is exactly true.
**3. Is the model clean and fully pinned?** Yes — uniform permutation of S₁₀₀, N/2 opens, the longest-cycle ≤ 50 reduction, SEED=20260717, all constants committed; nothing tunable post-hoc.
**4. Is there an exactly-true gate?** Yes — G2 exhaustively enumerates all 8! permutations, yielding the exact rational 307/840 identical to the closed form; no sampling is involved.
**5. Is it deterministic and reproducible?** Yes — results-dict sha256 ebc266644b5e21cb3c3c52415abd30e907c279fed74aa8f1c7151d5be895fdcf is byte-identical across an in-process double-run and a separate process invocation.
**6. Is the grounding real and external?** Yes — Wikipedia "100 prisoners problem" raw wikitext pinned by sha1 at oldid 1355965864, fetched live 2026-07-20, states the 31% result and the harmonic closed form; the enumeration gate is firsthand.
**7. Could it collide with a shipped proposal?** No — no permutation-cycle / prisoners head exists, and the mechanism is distinct from every shipped counterintuitive-probability head (see Dedup).
**8. What would make sim-lab reject it?** A non-reproducible digest, a gate that fails under an independent reimplementation, or the closed form disagreeing with enumeration at a second small N — the natural sim-lab generalization is to re-derive H₂ₙ − Hₙ and confirm the exact-match gate at N ∈ {6, 8, 10}.

**Recommendation: sim-ready**
