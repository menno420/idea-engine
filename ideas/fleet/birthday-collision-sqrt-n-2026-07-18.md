# A random collision arrives after √N draws, NOT N/2 — drawing uniformly with replacement from N equally-likely outcomes, the first value that repeats one already seen shows up after only about √N draws: the waiting time to the first collision has mean E[T_N]→√(πN/2)=1.2533√N, and a collision is more-likely-than-not after m*≈1.1774√N draws — a VANISHING fraction m*/(N/2)=2.3548/√N→0 of the space. Doubling the space buys only √2≈1.41× more safe draws, not 2×. The danger line for any random-ID / token / nonce / hash-key scheme is the SQUARE ROOT of the space, not half of it.

> **State:** sim-ready
> **Class:** fleet (unrelated / cross-cutting) · probability / combinatorics · the birthday problem's √N first-collision scaling law
> **Target:** sim-lab (VERDICT 145, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@5ee597a · fetched 2026-07-18T10:48:42Z
> **Reference (external, reachable):** https://en.wikipedia.org/wiki/Birthday_problem — the √N scaling (n≈√(2d·p(n))), the 50%-collision threshold n(d)=⌈√(2d ln 2)⌉ (=√(2 ln 2)·√d≈1.1774√d), and the expected number of draws to the first collision "1 + Q(M) ≈ 24.61659" for M=365 (Ramanujan's Q-function, E[T_N]→√(πN/2)); verified reachable 2026-07-18 (WebFetch, confirms the √N scaling, the ⌈√(2d ln 2)⌉ 50%-threshold, and the 1+Q(M)≈24.61659 exact expectation).

## The phenomenon (one line)
Draw values one at a time, uniformly at random with replacement, from a space of N equally-likely outcomes. The number of draws T until the first REPEAT is **not** on the order of N/2 — its mean is about **√(πN/2)=1.2533√N**, and a collision is **more-likely-than-not after only m*≈1.1774√N draws**. On the pinned world the exact expected waiting time at N=16384 is **161.091690** draws (vs the folk-belief ~N/2=8192), the simulated mean is **161.135750**, and a collision is already more-likely-than-not by draw **m*=151** — a fraction **0.018433** of N/2.

## The folk belief
"A collision is rare until you've sampled a large fraction of the space. To get two draws to coincide out of N possible values you need on the order of N/2 draws — half the space — because each new draw only has a `(number already seen)/N` chance of hitting a prior one, and that stays small until you've seen a big chunk of N. So a random-ID or token scheme over N values is safe for roughly N/2 uses, and doubling the space doubles the safe budget." The intuition prices the collision hazard of a SINGLE draw (small, ≈k/N after k draws) but forgets that the number of PAIRS grows like k², so the cumulative hazard crosses 1 far sooner — at √N, not N/2.

## The probabilistic thesis (reasoned to its fuller form — Q-0254 duty)
The intuition confuses the per-draw collision probability with the cumulative one. After k distinct draws the next draw collides with probability k/N — small — but there are `C(k,2)=k(k−1)/2` PAIRS of draws, and the probability that ALL k are distinct is the exact product

    P(all k distinct) = ∏_{i=0}^{k-1} (N−i)/N ≈ exp(−k(k−1)/(2N)),

so the collision probability `1 − P(all k distinct)` is governed by `k²/2N`, not `k/N`. It crosses ½ when `k²/2N ≈ ln 2`, i.e. at

    m*(N) ≈ √(2 ln 2 · N) = 1.1774·√N,

and the WAITING TIME to the first collision, `T`, has mean given exactly by the tail-sum

    E[T_N] = Σ_{k≥0} P(T > k) = Σ_{k=0}^{N} P(first k draws all distinct) = 1 + Q(N),

where `Q(N) = Σ_{k≥1} N!/((N−k)! N^k)` is **Ramanujan's Q-function**, with the asymptotics

    E[T_N] = √(πN/2) + 2/3 + (1/12)√(π/(2N)) − … → 1.2533·√N.

Both landmarks scale as the **square root of N**. Two consequences the folk belief misses. **(1) √N, not N/2 — a quadratic gap.** At N=16384 the collision danger line is ~128–161 draws, not ~8192; the intuition overstates the safe budget by a factor of ~√N. **(2) Doubling the space buys only √2×.** Because both E[T_N] and m*(N) scale as √N, doubling N multiplies the safe draw budget by only √2≈1.41×, not 2× — to HALVE collision risk you must QUADRUPLE the space. This is exactly why random-ID / session-token / nonce / cache-key / short-hash schemes have a birthday bound: a space of N values is safe only to ~√N uses, and ID width must grow ~2 bits per doubling of usage, not linearly. The honest reading: √N is the design threshold for collision resistance, and a linear "half the space" budget silently over-provisions safety by a quadratic factor.

## The formal model (committed constants — sim-lab must reproduce exactly)
- A "trial" draws values `x = rng.randrange(N)` one at a time, uniformly with replacement, keeping a set of seen values; `T` = the index of the first draw whose value is already in the set (so `T ≥ 2`).
- Per grid cell `N ∈ N_GRID` run `TRIALS` independent trials off a single pinned RNG stream, in fixed `N_GRID` order; record the mean and unbiased sample variance of `T`, and (at `N_HI` only) the fraction of trials with `T ≤ m*`.
- `m*(N) = ` smallest `m` with `P(collision within m draws) = 1 − P(all m distinct) ≥ 0.5` — computed exactly, deterministically, no RNG.
- Exact anchors (no RNG): `P(all k distinct) = ∏_{i=0}^{k-1}(N−i)/N`; `E[T_N] = Σ_{k=0}^{N} P(all k distinct)` (Ramanujan Q+1); the 50%-threshold `m*` above.
- A statistic's standard error is `se = sample-sd / √TRIALS` (the P104…P128 /se convention: z on an estimated statistic).

## Pinned world (committed constants)
- SEED = 20260717 (proposal-owned; SEEDLESS discipline)
- TRIALS = 120000 first-collision waiting times per grid cell
- N_GRID = (365, 1024, 4096, 16384) — 365 is the classic birthday space; N_LO = 1024, N_HI = 16384 so √(N_HI/N_LO) = √16 = 4.0 exactly
- SIGMA_GATE = 3.0
- Leading coefficients: C_mean = √(π/2) = 1.2533141…; C_half = √(2 ln 2) = 1.1774100…
- Exact anchors at the pinned N: E[T_365] = 24.616586 (= 1+Q(365), matching the Wikipedia value 24.61659), E[T_1024] = 40.775954, E[T_4096] = 80.880396, E[T_16384] = 161.091690; m*(16384) = 151 with exact P(collision by m*) = 0.500101.

## Pre-registered gates (APPROVE iff ALL hold, in order G1 → G2 → G3)
- **G1 — sim correct:** at N_HI the Monte-Carlo mean waiting time matches the EXACT finite-N anchor `E[T_N] = Σ_k P(first k draws distinct)` within z < 3σ (standard error of the mean). The sim reproduces the exact Ramanujan-Q expectation, not just the √N asymptotic.
- **G2 — √N scaling law:** the mean waiting time scales like √N, NOT like N. The MC ratio `mean(T@N_HI)/mean(T@N_LO)` matches the EXACT-mean ratio `E[T_16384]/E[T_1024]` within z < 3σ (delta method), and that exact ratio is a √N-law value (≈3.95 ≈ √16 = 4.0) decisively far from the linear-N folk prediction `N_HI/N_LO = 16.0`. Doubling×4 the space multiplies the budget by √16=4, not 16.
- **G3 — inversion (folk belief reversed):** a collision is more-likely-than-not after only `m* ≈ 1.1774√N` draws — a vanishing fraction of the space, NOT ~N/2. At N_HI the MC fraction of trials collided by draw `m*` EXCEEDS 0.5 AND matches the exact anchor `1 − P(all m* distinct)` within z < 3σ, with `m*/(N/2) ≪ 1`. The "need half the space" belief is reversed.

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 ∧ G3 hold at their stated thresholds on the pinned world with SEED=20260717 and the committed reference verifier (the verifier's `all_pass` field encodes exactly `G1 ∧ G2 ∧ G3`). Any gate failing → REJECT (the √N-collision-scaling claim is falsified for these constants). No post-hoc threshold moves; SEED is not changed; margins reported in σ on the standard error of the estimated statistic.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
- exact E[T_N] = {365: 24.616586, 1024: 40.775954, 4096: 80.880396, 16384: 161.091690}
- MC mean waiting time = {365: 24.582992, 1024: 40.823367, 4096: 80.736133, 16384: 161.135750}
- MC mean / √N = {365: 1.286733, 1024: 1.275730, 4096: 1.261502, 16384: 1.258873} → C_mean = √(π/2) = 1.253314 (approached from above as N grows, the +2/3/√N correction)
- m*(16384) = **151**; exact P(collision by m*) = **0.500101**; MC fraction collided by m* = **0.500183**; m*/(N/2) = **0.018433** (a vanishing fraction of half the space)
- **G1 sim-correct:** MC mean 161.135750 vs exact 161.091690 at z = **+0.183** — PASS (|z| < 3)
- **G2 √N law:** ratio_mc 3.947145 vs exact ratio 3.950637 (≈ √16 = 4.0) at z = **−0.425** — PASS; the exact ratio is nearer the √N-law value 4.0 than the linear-folk value 16.0 (sqrt_not_linear = true)
- **G3 inversion:** MC frac collided by m* = 0.500183 > 0.5 (majority) and matches anchor 0.500101 at z = **+0.057** — PASS; m*/(N/2) = 0.018433 ≪ 1 (tiny fraction)
- all_pass = true; **exit 0**
- Two runs byte-identical (deterministic under SEED).
- **Disclosed results-dict sha256 = 838bee178afb150de05ebeaf65f4d712eedb39d1fd861f311a4f2b1c4f710c51**
  (this is the sha256 of `json.dumps(results, sort_keys=True, separators=(",",":"))` over the whole results dict — the compact canonical serialization the verifier prints as `Results-JSON sha256:`. WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture — the dict never carries a self-referential sha field, and the stdout DUMP is pretty `indent=2` while the hashed preimage is compact; the P105/P109/P114/P118/P122/P123/P126/P127/P128/P129/P130/P131 family. No `.json` artifact is committed.)

## Verifier
Stdlib-only python3 (`random, math, json, hashlib` — no numpy), committed alongside this idea as `ideas/fleet/birthday_collision_sqrt_n.py`. Seeds once with SEED=20260717, computes the exact deterministic anchors (E[T_N] via the tail-sum, m* via the exact threshold scan), then for each N in N_GRID simulates TRIALS=120000 first-collision waiting times off the single pinned stream, recording the mean, unbiased sample variance, and (at N_HI) the fraction collided by m*; it evaluates G1/G2/G3 on the /se margin and emits a canonical (sorted-keys, comma/colon-separated) results JSON with its sha256. Exit 0 iff all three gates pass.

Reproduce:

```
python3 ideas/fleet/birthday_collision_sqrt_n.py
```

Expected: all_pass=true, exit 0, G1 z=+0.183, G2 z=−0.425, G3 z=+0.057, m*=151, results-dict sha256 = 838bee178afb150de05ebeaf65f4d712eedb39d1fd861f311a4f2b1c4f710c51.

## Why it matters (cross-cutting)
Any system that mints or samples from a finite ID / key / token / nonce / hash space with replacement inherits the √N collision bound. Decision rule for an operator/architect: (1) size a random-ID space by the SQUARE of the number of draws you expect plus a safety margin — the danger line is ~√N draws (more precisely, a collision is more-likely-than-not by ~1.1774√N), NOT ~N/2, so a scheme over N values is safe only to ~√N uses; (2) doubling the space buys only √2≈1.41× more safe draws, so ID/token WIDTH must grow ~2 bits per doubling of expected usage, never linearly — to halve collision risk, quadruple the space; (3) this is the birthday bound behind cryptographic collision resistance (a b-bit hash resists collisions only to ~2^(b/2) queries), hash-table load thresholds, and random short-URL / request-ID exhaustion. A capacity plan that treats a random-ID space as "half-full is fine" silently ships a quadratic collision risk.

## Dedup
Distinct from the nearby unrelated / probability priors:
- **Prior UNRELATED closers** — **kelly-overbet-ruin** (P100, information theory — growth-optimal bet fraction), **epidemic-overshoot** (P104, SIR final size), **regression-to-mean** (P108, conditional-mean shrinkage), **series-reliability-collapse** (P112, reliability — min-of-exponentials MTBF), **arcsine-lead-illusion** (P116, the sojourn-time DISTRIBUTION of a fair walk), **german-tank-mvue** (P120, point estimation of a discrete-uniform maximum), **benford-multiplicative-growth** (P124, the leading-digit law), **stein-shrinkage-dominance** (P128, estimator admissibility): different domains and different objects (a bet fraction, an epidemic size, a conditional mean, an MTBF, a sojourn distribution, a point estimate, a leading-digit law, an estimator-dominance result). None is the first-collision WAITING TIME of uniform draws with replacement, and none uses the `∏(N−i)/N` / Ramanujan-Q `E[T_N]=√(πN/2)` mechanism or the `m*≈1.1774√N` threshold.
- **coupon-collector-tail** (fleet, occupancy/collection): the OPPOSITE problem — coupon-collector counts draws to collect ALL N distinct values (a completion COST, mean ~N ln N, the tail of a MAX of geometrics); this head counts draws to the FIRST collision (a first-repeat waiting time, mean ~√N). Complementary ends of the occupancy spectrum (first-collision vs full-coverage) with different scaling laws (√N vs N ln N), different anchors, and different gates — no shared metric.
- **inspection-paradox-wait-inflation** (fleet — length-biased renewal waiting time), **secretary-rule-cardinal-regret** (fleet — optimal stopping), **variance-blind-provisioning-trap** (fleet — M/M/1 queueing tail), **simpsons-paradox-aggregation-reversal** (fleet — aggregation reversal): different objects (a length-biased wait, a stopping rule, a queueing tail, an aggregation reversal) — none is a first-collision / occupancy waiting-time claim.
- The birthday-collision head was "set aside by a prior sweep as fully closed-form, nothing a sim settles" — that referred to the STATIC one-line collision PROBABILITY (a single combinatorial fact `1−∏(N−i)/N`). This proposal is the DYNAMICAL emergence: a Monte-Carlo of the first-collision WAITING-TIME DISTRIBUTION that reproduces the exact Ramanujan-Q expectation `E[T_N]` AND the √N scaling law AND isolates the mechanism with a dose-response (√N-not-linear scaling) and an inversion control (collision by ~√N, not ~N/2) — the same sim-reproduces-closed-form posture as P104/P108/P112/P116/P124, not a one-line probability. (Precedent: the Benford card P124 made exactly this static→dynamical move.)

## Model basis (declared model-dependence — the P024 discipline)
The exact anchor `E[T_N]=Σ_k P(first k distinct)=1+Q(N)` and the threshold `m*≈√(2 ln 2 · N)` are the classical birthday-problem results for uniform draws with replacement — no distributional assumption beyond uniformity, which the model pins exactly (`rng.randrange(N)`). The √N scaling (`E[T_N]→√(πN/2)`, `m*→1.1774√N`) is a theorem, not a fitted curve; the constants merely make the anchor exact and the seed reproducible. Scoping: the √N law is specific to the UNIFORM space with replacement — a non-uniform draw law makes collisions arrive EVEN SOONER (any imbalance only raises collision probability, by convexity / the rearrangement inequality), so the uniform case is the best case and the √N danger line is if anything optimistic; the QUALITATIVE claim (first collision at ~√N, doubling the space buys only √2×) holds for any fixed distribution, demonstrated on the pinned uniform constants and mechanism-explained (pairs grow like k², so cumulative hazard ~k²/2N crosses 1 at √N).

## Probe report (v0, 2026-07-18)

**1. What is this really?** A waiting-time claim: for uniform draws with replacement from N cells, the number of draws to the FIRST repeat has mean `E[T_N]→√(πN/2)=1.2533√N` and is more-likely-than-not by `m*≈1.1774√N` — the √N scaling of the birthday problem, NOT the folk ~N/2. Controls: the exact ratio of means at N_HI vs N_LO is a √N-law value (≈4.0=√16), decisively not linear (16.0); and a collision is already majority-likely by a tiny fraction `m*/(N/2)=0.0184` of half the space.
**2. What would make it false?** If the MC mean waiting time at N_HI did NOT match the exact `E[T_N]` within 3σ (G1 — sim doesn't reproduce the Ramanujan-Q expectation), or the MC ratio did NOT match the exact-mean ratio within 3σ / the exact ratio were a linear-N not √N value (G2 — no √N scaling), or the MC fraction collided by `m*` were NOT a majority matching `1−P(all m* distinct)` within 3σ (G3 — collision needs more than ~√N draws). Any → REJECT.
**3. Simplest version that still bites?** SEED=20260717, 120000 trials per N∈{365,1024,4096,16384}; each trial draws `randrange(N)` into a set until a repeat, recording the draw count T; report mean(T) vs exact `Σ_k P(all k distinct)`, the ratio mean(16384)/mean(1024) vs √16=4, and the fraction with T≤m*(16384)=151 vs 0.5.
**4. What is the counterintuitive core?** "You need ~N/2 draws for a collision" is wrong by a quadratic factor — the first collision arrives at ~√N (at N=16384: ~128–161 draws, not ~8192), and doubling the space buys only √2≈1.41× more safe draws, not 2×. The number of PAIRS grows like k², so the cumulative collision hazard crosses ½ at √N.
**5. Where could I be fooling myself?** G1 anchors to the EXACT finite-N `E[T_N]` (the Ramanujan-Q tail-sum), not the √N asymptotic, so the gate is a genuine finite-N reproduction — and the exact E[T_365]=24.616586 matches the independently-published Wikipedia value 24.61659. G2 anchors the ratio to the EXACT-mean ratio (3.9506), not the bare √16=4.0 (which the +2/3 correction shifts), so a naive-asymptotic anchor would falsely fail; the sqrt_not_linear structural check separately confirms it is a √N not linear-N ratio. G3's anchor is the exact `1−P(all m* distinct)`, and m* is the exact deterministic threshold.
**6. What is the honest calibration?** Dry-sim margins at SEED=20260717: G1 |z|=0.183, G2 |z|=0.425, G3 |z|=0.057 — all comfortably inside the 3σ match band (these are AGREEMENT gates: small |z| = the sim reproduces the closed form); the structural separations are decisive (exact ratio 3.95 vs linear 16.0; m*/(N/2)=0.0184≪1). exit 0; results-dict sha256 838bee17…f710c51.
**7. What decision does it change?** When sizing a random-ID / token / nonce / cache-key / short-hash space, treat ~√N (more precisely ~1.1774√N) as the collision danger line, NOT ~N/2; grow ID width ~2 bits per doubling of expected usage (quadruple the space to halve risk); and read the birthday bound into any collision-resistance or hash-load capacity plan.
**8. How will we know it worked?** The committed stdlib verifier reproduces the birthday √N collision scaling under SEED=20260717 with all three gates holding (G1 MC mean = exact E[T_N] within 3σ, G2 MC ratio = exact √N-law ratio within 3σ and not linear, G3 majority-collided-by-m* matching `1−P(all m* distinct)` within 3σ with m*/(N/2)≪1), and the results-dict sha256 matching 838bee178afb150de05ebeaf65f4d712eedb39d1fd861f311a4f2b1c4f710c51.

## One-line correction
The first random collision arrives after ~√N draws (more precisely, more-likely-than-not by ~1.1774√N), NOT ~N/2 — the birthday bound — so a random-ID/token/nonce/hash space of N values is safe only to ~√N uses, and to halve collision risk you must QUADRUPLE the space, not double it.

**Recommendation: sim-ready**
