# Balls into bins: the expected number of collisions is exactly m(m−1)/(2n) — quadratic in the balls, not linear, which is why hash / shard / nonce collisions arrive far sooner than a per-ball 1/n intuition predicts

> **State:** sim-ready
> **Class:** counterintuitive-but-exactly-true · combinatorial probability / hashing (round-54 FLEET slot)
> **Target:** sim-lab (VERDICT 238, +13 offset)
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Birthday_problem&action=raw&oldid=1357361405@d876b4f46b64278277ad0cf4b4bdf2ea0f271be1 · fetched 2026-07-20
> **Verifier (firsthand):** stdlib-only, SEED=20260717; results-dict sha256 874a5b611f327149714d07b841bb4285481bbb223086823a5980b5ae6a31a57a

## The phenomenon (one line)
Throw m balls independently and uniformly into n bins — equivalently, hash m keys into a table of n buckets, or draw m values from a discrete-uniform space of size n. Count one COLLISION for every unordered PAIR of balls that land in the same bin (X = Σ over bins of C(load, 2)). The expected number of colliding pairs is EXACTLY **E[X] = C(m,2)/n = m(m−1)/(2n)** — a closed-form rational with no approximation, for every (m, n).

## The folk belief
"A collision is a per-ball event: each new ball has about (balls already placed)/n chance of landing on an occupied bin, so with m balls in n bins you expect roughly m·(m/n)/something — order m²/(2n) — collisions. And since each ball 'competes' against all m placed balls, m²/2 pairs feels right." The intuition is nearly correct in shape (it IS quadratic) but wrong in the constant: it counts m²/2 ordered/self-inclusive pairs instead of the C(m,2) = m(m−1)/2 genuine unordered pairs, overstating the exact answer by exactly m/(2n). The deeper error the phrase "per-ball event" invites is treating collisions as linear in m; they are quadratic, because it is the PAIRS that collide, and pairs grow like m².

## The thesis (reasoned to fuller form — Q-0254 duty)
Fix any two balls i ≠ j. They land in the same bin with probability exactly 1/n: sum over the n bins of P(both in bin b) = n · (1/n)(1/n) = 1/n, independent of every other ball. Let 1_{ij} indicate that pair {i, j} collides. The total collision count is X = Σ_{i<j} 1_{ij}, a sum over the C(m,2) unordered pairs. By **linearity of expectation** — which needs NO independence between the pair-indicators, and they are indeed not independent —

    E[X] = Σ_{i<j} E[1_{ij}] = C(m,2) · (1/n) = m(m−1)/(2n).

Three things make this sharp. (1) It is EXACT, not asymptotic: no Poisson limit, no n→∞. (2) It is quadratic in m: doubling the balls nearly quadruples the collisions (ratio (2m)(2m−1)/(m(m−1)) → 4), whereas a naive per-ball reading predicts linear growth. (3) The self-collision correction is real: the −1 in m(m−1) removes the m "pairs" a ball would form with itself; dropping it gives m²/(2n), which is wrong by m/(2n) — small in relative terms but a genuine, rejectable bias. The same C(m,2)/n rate is exactly the mean of the Poisson that the birthday-attack analysis uses to approximate the collision DISTRIBUTION; here we assert only the mean, which is exact.

## The formal model (committed constants, exact)
- m balls thrown independently, each uniform over n bins (`rng.randrange(n)`); load B_k = #balls in bin k; collision count X = Σ_k C(B_k, 2) = # unordered colliding pairs.
- Exact core identity, computed THREE independent ways and asserted equal (no route hardcoded to the closed form):
  - **(a) literal pair-sum**: Σ over all C(m,2) unordered pairs of `Fraction(1, n)`, added out in a double loop.
  - **(b) per-bin linearity**: n · [C(m,2)/n²] as `n * (Fraction(m(m−1)/2) / Fraction(n·n))`.
  - **(c) closed form**: `Fraction(m·(m−1), 2·n)`.
  - Claim: (a) == (b) == (c) exactly for every config.
- Configs committed: (n, m) = (365, 23) [canonical birthday], (256, 64) [64 keys into a 256-bucket table], (1000, 100) [100 items over 1000 shards] for the exact/MC legs; a robustness sweep (365, 30) / (128, 40) / (500, 50) / (64, 16); and (256, 64) for falsifiability.
- G1's exact leg uses `fractions.Fraction` — no float enters the identity; G2/G3/G4's Monte-Carlo legs are seeded sampling cross-checks of the m(m−1)/(2n) law.

## Pinned world (committed constants)
SEED=20260717 · all randomness from `random.Random(20260717)` · exact three-route identity on (365,23), (256,64), (1000,100) · Monte-Carlo 200000 trials/config, sample mean vs exact E with z = (mean − E)/(sample_sd/√T) · robustness sweep 120000 trials each on (365,30),(128,40),(500,50),(64,16) plus an exact-scaling `Fraction` ratio E(2m)/E(m) · falsifiability = the naive shortcut m²/(2n) and the ordered-pair count m(m−1)/n, both on the same (256,64) sample · Z_AGREE=3.0, Z_REJECT=6.0.

## Pre-registered gates (sim-ready iff ALL hold, in order)
**G1 — Exact identity (three routes, Fraction ==).** For every config the expected colliding-pair count is built as (a) a literal Σ Fraction(1,n) over all C(m,2) pairs, (b) the per-bin linearity route, and (c) the closed form m(m−1)/(2n), and all three are asserted exactly equal. *Direction:* any route ≠ the others ⇒ FAIL. **PASS** ((365,23)→253/365, (256,64)→63/8, (1000,100)→99/20, all three routes equal).
**G2 — Monte-Carlo agreement (<3σ).** For each config the sample mean of X over 200000 trials lands within 3·SE of the exact E. *Direction:* |z| ≥ 3 ⇒ FAIL. **PASS** (z = −0.745423 (365,23), −0.988399 (256,64), −1.509722 (1000,100) — all < 3).
**G3 — Robustness (sweep + exact scaling).** (a) Over four further configs (365,30)/(128,40)/(500,50)/(64,16) each sample mean agrees within |z| < 3 (z = 0.281804, −0.687537, −0.830305, 1.261990). (b) The exact scaling ratio E(n, 2m)/E(n, m) equals (2m)(2m−1)/(m(m−1)) as identical Fractions, independent of n ((365,23)→45/11, (256,64)→254/63). *Direction:* any swept config disagrees OR the scaling identity fails ⇒ FAIL. **PASS**.
**G4 — Falsifiability (the gate must REJECT wrong models).** On the (256,64) sample whose mean AGREES with the exact 63/8 at z = −0.576503, the naive shortcut E ≈ m²/(2n) = 8.0 is REJECTED at z = −20.566187, its overstatement exactly m/(2n) = 1/8; the ordered-pair count m(m−1)/n = 15.75 is REJECTED at z = −1259.926656. *Direction:* PASS iff each wrong model is REJECTED at |z| ≥ 6. **PASS** (both rejected).

## Pre-registered decision rule
sim-ready iff G1 ∧ G2 ∧ G3 ∧ G4 all hold in their stated directions, AND determinism holds (both the in-process double-run and separate-process byte-identical stdout), AND both deliberately-wrong models (m²/(2n) shortcut; ordered-pair m(m−1)/n) are REJECTED.

## Dry-sim results
```json
{
  "proposal": "PROPOSAL 225",
  "verdict": 238,
  "theorem": "Balls-into-bins expected collision count = m(m-1)/(2n)",
  "identity": "E[colliding pairs] = C(m,2)/n = m(m-1)/(2n) exactly",
  "seed": 20260717,
  "configs": [[365, 23], [256, 64], [1000, 100]],
  "g1_exact_identity": {
    "365,23": {"n": 365, "m": 23, "pairs_C_m_2": 253, "route_a_pairsum": "253/365", "route_b_perbin": "253/365", "route_c_closed": "253/365", "three_routes_equal": true, "E_float": 0.693150685},
    "256,64": {"n": 256, "m": 64, "pairs_C_m_2": 2016, "route_a_pairsum": "63/8", "route_b_perbin": "63/8", "route_c_closed": "63/8", "three_routes_equal": true, "E_float": 7.875},
    "1000,100": {"n": 1000, "m": 100, "pairs_C_m_2": 4950, "route_a_pairsum": "99/20", "route_b_perbin": "99/20", "route_c_closed": "99/20", "three_routes_equal": true, "E_float": 4.95}
  },
  "g2_montecarlo": {
    "365,23": {"E_exact": 0.693150685, "sample_mean": 0.691765, "z": -0.745423, "within_3sigma": true},
    "256,64": {"E_exact": 7.875, "sample_mean": 7.86881, "z": -0.988399, "within_3sigma": true},
    "1000,100": {"E_exact": 4.95, "sample_mean": 4.94247, "z": -1.509722, "within_3sigma": true}
  },
  "g3_robustness": {
    "sweep": {
      "365,30": {"E_exact": 1.191780822, "sample_mean": 1.192666667, "z": 0.281804, "within_3sigma": true},
      "128,40": {"E_exact": 6.09375, "sample_mean": 6.088858333, "z": -0.687537, "within_3sigma": true},
      "500,50": {"E_exact": 2.45, "sample_mean": 2.446266667, "z": -0.830305, "within_3sigma": true},
      "64,16": {"E_exact": 1.875, "sample_mean": 1.87995, "z": 1.261990, "within_3sigma": true}
    },
    "exact_scaling": {
      "365,23": {"ratio_E2m_over_Em": "45/11", "predicted_ratio": "45/11", "n_independent_equal": true},
      "256,64": {"ratio_E2m_over_Em": "254/63", "predicted_ratio": "254/63", "n_independent_equal": true}
    },
    "both_hold": true
  },
  "g4_falsifiability": {
    "config": [256, 64],
    "E_true_m_m_minus_1_over_2n": 7.875,
    "E_naive_m_squared_over_2n": 8.0,
    "E_ordered_m_m_minus_1_over_n": 15.75,
    "sample_mean": 7.871395,
    "z_true_agree": -0.576503,
    "z_naive_reject": -20.566187,
    "z_ordered_reject": -1259.926656,
    "naive_overstatement_exact": "1/8",
    "both_wrong_models_rejected": true
  },
  "gates": {"G1": true, "G2": true, "G3": true, "G4": true},
  "sim_ready": true
}
```
results_sha256=874a5b611f327149714d07b841bb4285481bbb223086823a5980b5ae6a31a57a

**Disclosed results-dict sha256 = `874a5b611f327149714d07b841bb4285481bbb223086823a5980b5ae6a31a57a`** — the expected collision count is exactly m(m−1)/(2n) (G1: all three exact routes agree — literal Σ Fraction(1,n) over C(m,2) pairs, per-bin linearity, and the closed form — for (365,23)→253/365, (256,64)→63/8, (1000,100)→99/20); Monte-Carlo agrees at z = −0.745423 / −0.988399 / −1.509722; a four-config sweep all agrees (|z| < 1.27) with the exact-scaling Fraction identity holding; and the naive m²/(2n) shortcut is rejected at z = −20.566187 (overstatement exactly m/(2n) = 1/8) with the ordered-pair impostor rejected at z = −1259.926656. In-process `determinism_double_run=True`; two separate processes print byte-identical stdout (sha256 df886c2d1102774119b971fe56c55edc62c282f6c1dba7ebf512ad95d9e48279).

## Verifier
`sims/verdict-238-balls-into-bins-collisions/balls-into-bins-collision-count.py` (menno420/sim-lab, branch `claude/p225-balls-in-bins`) — stdlib only (`hashlib`, `json`, `math`, `random`, `fractions.Fraction`), SEED=20260717, all randomness from `random.Random(20260717)` consumed in a fixed order; the results dict is built twice and both canonical dumps are asserted identical before exit.
```reproduce
python3 sims/verdict-238-balls-into-bins-collisions/balls-into-bins-collision-count.py
# prints the results JSON, then results_sha256=874a5b611f327149714d07b841bb4285481bbb223086823a5980b5ae6a31a57a, then determinism_double_run=True; exits 0
# each process's stdout sha256 = df886c2d1102774119b971fe56c55edc62c282f6c1dba7ebf512ad95d9e48279 (separate processes byte-identical)
```

## Why it matters
The expected-collision-count is the load-planning number behind every hash table, sharding scheme, dedup pass, random-ID / nonce / token allocator, and Bloom-filter sizing: with m items over n slots you should expect m(m−1)/(2n) collisions BEFORE you observe any, and that number is quadratic in m — halving the item count cuts expected collisions roughly fourfold, and doubling the table size only halves them. The counterintuitive part is that collisions are a PAIR phenomenon, not a per-ball one: a table that is only 25% full (m = n/4) already expects ≈ n/32 colliding pairs. The exact m(m−1)/(2n) is also the mean of the Poisson that governs the birthday-attack collision probability — get the mean right (and notice the −1 that the naive m²/(2n) drops) and the whole security-margin calculation for hash-collision resistance follows.

## Dedup
Grepped all lanes (`ideas/**`) at boot (`rg -i 'balls.into.bins|collision|birthday|occupancy|coupon|hash.table'`, bootstrap.py/.substrate excluded). Two nearest neighbours exist and are DISTINCT objects:
- **coupon-collector-tail** (P052, `coupon-collector-tail-2026-07-14.md`) — the n·H_n expected time to COLLECT ALL n bins (full cover time, a sum of geometric stage-waits). This head is the expected COLLISION COUNT at a fixed number of throws — a linearity-over-pairs result, not a cover-time sum. Disjoint machinery (no harmonic-number kernel here; no pair-count kernel there).
- **birthday-collision-sqrt-n** (`birthday-collision-sqrt-n-2026-07-18.md`) — the √N waiting time to the FIRST collision and the 1.1774√N 50%-threshold (a first-repeat hitting time). This head prices the EXPECTED NUMBER of colliding pairs at a fixed m (a count, not a waiting time); it uses the same C(m,2) pair-count observation the birthday doc mentions in passing but computes a different object (E[#pairs] = C(m,2)/n, exact) at a fixed throw budget rather than a stopping time.
No existing card computes the expected collision COUNT m(m−1)/(2n); the slug `balls-into-bins-collision-count` is un-collided.

## Model basis (declared model-dependence — the P024 discipline)
The result is exact GIVEN the model: m independent balls, each uniform over n bins, and "collision" defined as an unordered PAIR sharing a bin (X = Σ C(B_k,2)). It assumes a true uniform RNG and independence across balls; a biased or correlated hash shifts the per-pair probability off 1/n and changes the constant (any load imbalance can only RAISE E[X] by convexity, so uniform is the best case — the minimum expected collisions). G1's exact leg carries no probabilistic assumption (a `Fraction` identity over the C(m,2) pairs); G2/G3/G4's Monte-Carlo legs are seeded sampling cross-checks of the m(m−1)/(2n) law, not the proof.

Grounding caveat (accurate to the pinned revision): Pinned to English Wikipedia "Birthday problem", revision oldid 1357361405 (raw wikitext, sha1 d876b4f46b64278277ad0cf4b4bdf2ea0f271be1, 52676 bytes; local sha1sum and the MediaWiki API `rvprop=sha1` agree — a 3-way match). ON-PAGE (confirmed by grep): the C(m,2) = m(m−1)/2 pair count, literally "the birthday comparisons will be made between every possible pair of individuals. With 23 individuals, there are 23×22/2 = 253 pairs"; the Poisson mean `Poi(C(23,2)/365) = Poi(253/365) ≈ Poi(0.6932)` used to approximate the collision distribution — 253/365 being exactly this head's E at (m=23, n=365); the linearity-of-indicator-variables method (used on-page for the expected number of people with a shared birthday); and the hash-table / hash-collision framing. The general exact closed form **E = m(m−1)/(2n) is DERIVED here**, not quoted: the page supplies the pair count C(m,2), the per-pair probability 1/d, the linearity method, and the single numeric rate 253/365 — but presents 253/365 as the mean of an APPROXIMATING Poisson, and never states the general m(m−1)/(2n) as a labeled exact expected-collision-count formula. (A separate on-page quantity — the "number of people who repeat a birthday", Σ q(k−1;d) = n − d + d((d−1)/d)ⁿ — is the expected count of balls landing in an OCCUPIED bin, NOT the colliding-pair count; distinct object, and one of this verifier's rejected impostors is kin to it.) The page also names the Coupon collector's problem (n·H_n) as the DISTINCT cover-time neighbour. The SEED, the (n,m) configs, the three-route Fraction identity, the Monte-Carlo z-scores, the exact-scaling ratio, and the m²/(2n) falsifiability rejection are the verifier's OWN firsthand computations. The caveat is honest — the pair count and the 253/365 rate are quoted; the general exact formula is attributed as derived.

## One-line design fix
When a hash table or shard map shows more collisions than "m/n per slot" suggested, the estimate was linear-in-m; the right expectation is the quadratic m(m−1)/(2n) (pairs, not balls) — and if a calculation used m²/(2n), it silently over-provisioned by exactly m/(2n) collisions per the dropped self-pair term.

## Probe report (v0, 2026-07-20)
**1. Is the headline claim exactly true or only statistically likely?** Exactly true for the identity: G1 computes E[X] three independent exact ways — a literal Σ `Fraction(1,n)` over all C(m,2) pairs, the per-bin linearity route n·C(m,2)/n², and the closed form `Fraction(m(m−1), 2n)` — and asserts all three equal (253/365, 63/8, 99/20 across the three configs). The Monte-Carlo gates (G2/G3) only cross-check the closed form by sampling; they do not establish it.
**2. Is the model unambiguously defined?** Yes: m balls each thrown uniformly and independently over n bins (`rng.randrange(n)`), and a collision is an unordered PAIR of balls sharing a bin, so the collision count is X = Σ_bins C(load, 2) — committed as constants in the model section, with the three (n,m) configs and the sweep fixed.
**3. Does the exact identity actually come from linearity, or is it asserted?** It is computed, not asserted: route (a) sums `Fraction(1,n)` term-by-term over every one of the C(m,2) pairs (never substituting the closed form), route (b) sums the per-bin C(m,2)/n² contribution over n bins, and route (c) is the closed form — all three are compared for exact `Fraction` equality. Linearity is exercised, not taken on faith.
**4. Could the result be an artifact of the chosen configs?** No: G1 holds on three independent configs spanning a full table (365,23), a quarter-full table (256,64), and a sparse shard map (1000,100); G3 adds four more (365,30)/(128,40)/(500,50)/(64,16) all agreeing under Monte-Carlo, plus an exact-scaling Fraction identity E(2m)/E(m) that is config-independent — a coincidence would fail one of these rather than pass quietly.
**5. Is the ≥3σ gate a real check or a tautology given the exact identity?** It is an independent seeded sampling cross-check: G2 draws 200000 fresh balls-into-bins trials per config from `random.Random(20260717)`, counts colliding pairs, and tests the sample mean against the exact E with z = (mean − E)/(sample_sd/√T) — z = −0.745423 / −0.988399 / −1.509722, all < 3. It would flag any mismatch between the sampler and the m(m−1)/(2n) law.
**6. Does the gate battery actually reject a plausible wrong answer?** Yes, and that is G4's whole job: on the SAME (256,64) sample whose mean agrees with the exact 63/8 at z = −0.576503, the naive engineering shortcut m²/(2n) = 8.0 (which forgets the self-pair −1) is REJECTED at z = −20.566187 — its overstatement is exactly m/(2n) = 1/8 — and the ordered-pair count m(m−1)/n = 15.75 is REJECTED at z = −1259.926656. Both wrong models fail at |z| ≥ 6, opposite polarity to the G2/G3 agreement.
**7. Is the grounding an external citation and is its caveat accurate to the pinned revision?** The grounding pins Wikipedia "Birthday problem" oldid 1357361405 (raw-wikitext sha1 d876b4f46b64278277ad0cf4b4bdf2ea0f271be1, 3-way match: local sha1sum = MediaWiki API sha1). That revision literally states the C(m,2) pair count (23×22/2 = 253), the Poisson mean C(23,2)/365 = 253/365 ≈ 0.6932 for the number of coincidences, and the linearity-of-indicator-variables method, in a hash-collision context — but it presents 253/365 as an approximating Poisson's mean and does NOT state the general exact m(m−1)/(2n) as a labeled expected-collision-count formula. The caveat therefore attributes the pair count and the 253/365 rate as QUOTED and the general exact closed form as DERIVED; the SEED, the configs, the three-route Fraction identity, the z-scores, and the falsifiability rejection are the verifier's OWN firsthand computations — neither oversold nor undersold.
**8. Is the verifier deterministic and reproducible cross-invocation?** Yes: no wall-clock or OS entropy; all randomness comes from `random.Random(20260717)` consumed in a fixed, documented order (G2 configs, then the G3 sweep, then G4), the results dict is built twice and both canonical dumps asserted identical (determinism_double_run=True), and separate invocations printed the byte-identical stdout digest df886c2d1102774119b971fe56c55edc62c282f6c1dba7ebf512ad95d9e48279 (results-dict sha256 874a5b611f327149714d07b841bb4285481bbb223086823a5980b5ae6a31a57a).

**Recommendation: sim-ready**
