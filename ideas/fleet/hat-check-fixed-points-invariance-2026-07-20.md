# Hat-check invariance: when n patrons each grab a coat at random, the expected number who get their own coat back is exactly 1 — for every n — and the chance nobody does converges to 1/e ≈ 36.8%

> **State:** sim-ready
> **Class:** unrelated (round-48 UNRELATED slot)
> **Target:** sim-lab (VERDICT 217, +13 offset)
> 📊 Model: Claude Opus · high · idea/planning
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Rencontres_numbers&oldid=1340506236@256b0417a6785bd9d1e50a6aa9766175ee329dc5 · fetched 2026-07-20
> **Reference (external, reachable):** [Rencontres_numbers — Wikipedia](https://en.wikipedia.org/w/index.php?title=Rencontres_numbers&oldid=1340506236) — supports the head firsthand: "For n ≥ 1, the expected number of fixed points is 1 (a fact that follows from linearity of expectation).". Byte-pinned to the raw-wikitext sha1 of the cited revision.
> **Verifier (firsthand):** ideas/fleet/hat-check-fixed-points-invariance.py · results-dict sha256 7b99e6504b7cfa776ce871b7756b2ff71ed5bcd025e9dd6134d0f8d8e246dfb0

## The phenomenon (one line)
Shuffle who-walks-off-with-whose-coat uniformly at random: on average exactly one patron — out of any number — gets their own coat back, and the probability that nobody does settles at 1/e no matter how large the crowd.

## Domain
Probability / combinatorics of random permutations — fixed points, derangements, rencontres numbers. Outside fleet-ops, venture, and game: an everyday-life counterintuitive fact (the coat-check / hat-check problem).

## The folk belief
Two intuitions, both wrong: (a) "the bigger the crowd, the more people will, by luck, get their own coat back" — people expect the number of self-matches to grow with n; (b) "with a big enough crowd, surely at least one person always ends up with their own coat" — people expect the no-match probability to shrink toward 0.

## The thesis (reasoned to its fuller form — Q-0254 duty)
Model who-gets-whose-coat as one uniform random permutation π of {0..n−1}; a *fixed point* (π(i)=i) is a patron who got their own coat.

1. **The mean is pinned at 1, forever.** By linearity of expectation E[fixed points] = Σ_i P(π(i)=i) = Σ_i (1/n) = n·(1/n) = 1, for *every* n≥1. Crowd size cancels exactly — not "about 1 for large n" but exactly 1 at n=2 and at n=5,000,000 alike.
2. **The variance is also exactly 1** (n≥2): E[X(X−1)] = n(n−1)·1/(n(n−1)) = 1, so Var = E[X(X−1)] + E[X] − E[X]² = 1 + 1 − 1 = 1. Mean = variance = 1 is the fingerprint of Poisson(1).
3. **The no-match probability → 1/e, not 0.** The number of ways nobody matches is the derangement count D_n = n!·Σ_{k=0}^n (−1)^k/k!, so P(nobody matches) = Σ_{k=0}^n (−1)^k/k! → e^{−1} = 0.3678794… The second folk intuition is inverted: ~37% of the time *nobody* gets their own coat, and that floor never erodes.
4. **The whole count converges to Poisson(1).** P(exactly k self-matches) = (1/k!)·Σ_{j=0}^{n−k}(−1)^j/j! → e^{−1}/k!, so the entire distribution — not just its mean — is n-invariant in the limit.

Fuller form, one sentence: *the fixed-point count of a uniform random permutation is Poisson(1) in the limit, with mean and variance exactly 1 at every finite n≥2, and derangements are just its k=0 atom, ≈1/e.*

## The formal model / Pinned world (committed constants)
- Object: uniform random permutation of {0,…,n−1} via Fisher–Yates (`random.Random(SEED).shuffle`).
- Fixed points: |{i : π(i)=i}|. Derangement: zero fixed points.
- SEED = 20260717; one `random.Random(SEED)` consumed in gate order G2→G3→G4.
- Exact arithmetic via `fractions.Fraction`; exhaustive `itertools.permutations` for n=1..8.
- Committed constants: G2 n=200, M=80000, folk floor 0.30; G3 n∈{10,100,1000,2000} with M∈{80000,80000,40000,25000}; G4 n=100, M=80000, buckets k∈{0,1,2,3,≥4}, Poisson(1) expected, χ² df=4, α=0.001 critical value 18.467.

## Pre-registered gates
- **G1 — exactly true (Fraction, exhaustive enumeration, n=1..8).** For every n: E[fixed points] = 1 exactly; Var = 1 exactly for n≥2; and the brute derangement count equals BOTH the inclusion–exclusion closed form n!·Σ(−1)^k/k! AND the recurrence D_n=(n−1)(D_{n−1}+D_{n−2}). *Direction:* every identity exact; any single mismatch fails.
- **G2 — derangement floor at ≥3σ (n=200).** Empirical P(no fixed point) exceeds the folk "essentially never" floor 0.30 by z_floor ≥ 3, and is simultaneously within 3σ of 1/e. *Direction:* one-sided up past the floor (the counterintuitive signal) + two-sided consistency with e^{−1}.
- **G3 — n-invariance / robustness–shift (n∈{10,100,1000,2000}).** The mean fixed-point count does not move with crowd size: range across the four scales < 0.05, and every mean within 0.05 of 1. *Direction:* invariance under the n-shift; a growing (folk) mean would blow the range.
- **G4 — Poisson(1) shape (n=100).** Empirical fixed-point histogram matches Poisson(1): Pearson χ² (df=4) below the α=0.001 critical value 18.467 ⇒ fit not rejected. *Direction:* χ² below critical ⇒ limiting shape holds.

## Pre-registered decision rule
`sim-ready` iff G1 ∧ G2 ∧ G3 ∧ G4 all pass on a deterministic double-run (in-process rerun and a separate cross-invocation reproduce the identical results-dict sha256). Any gate fail ⇒ `needs-more-grooming`.

## Dry-sim results (SEED=20260717, verbatim from hat-check-fixed-points-invariance.py)
```
{
  "G1_exact_enumeration": {
    "1": {
      "D_all_agree": true,
      "D_n_brute": 0,
      "D_n_incexc": 0,
      "D_n_recur": 0,
      "E": "1",
      "E_eq_1": true,
      "Var": "0",
      "Var_ok": true,
      "p_derange": "0"
    },
    "2": {
      "D_all_agree": true,
      "D_n_brute": 1,
      "D_n_incexc": 1,
      "D_n_recur": 1,
      "E": "1",
      "E_eq_1": true,
      "Var": "1",
      "Var_ok": true,
      "p_derange": "1/2"
    },
    "3": {
      "D_all_agree": true,
      "D_n_brute": 2,
      "D_n_incexc": 2,
      "D_n_recur": 2,
      "E": "1",
      "E_eq_1": true,
      "Var": "1",
      "Var_ok": true,
      "p_derange": "1/3"
    },
    "4": {
      "D_all_agree": true,
      "D_n_brute": 9,
      "D_n_incexc": 9,
      "D_n_recur": 9,
      "E": "1",
      "E_eq_1": true,
      "Var": "1",
      "Var_ok": true,
      "p_derange": "3/8"
    },
    "5": {
      "D_all_agree": true,
      "D_n_brute": 44,
      "D_n_incexc": 44,
      "D_n_recur": 44,
      "E": "1",
      "E_eq_1": true,
      "Var": "1",
      "Var_ok": true,
      "p_derange": "11/30"
    },
    "6": {
      "D_all_agree": true,
      "D_n_brute": 265,
      "D_n_incexc": 265,
      "D_n_recur": 265,
      "E": "1",
      "E_eq_1": true,
      "Var": "1",
      "Var_ok": true,
      "p_derange": "53/144"
    },
    "7": {
      "D_all_agree": true,
      "D_n_brute": 1854,
      "D_n_incexc": 1854,
      "D_n_recur": 1854,
      "E": "1",
      "E_eq_1": true,
      "Var": "1",
      "Var_ok": true,
      "p_derange": "103/280"
    },
    "8": {
      "D_all_agree": true,
      "D_n_brute": 14833,
      "D_n_incexc": 14833,
      "D_n_recur": 14833,
      "E": "1",
      "E_eq_1": true,
      "Var": "1",
      "Var_ok": true,
      "p_derange": "2119/5760"
    }
  },
  "G2_derangement_floor": {
    "M": 80000,
    "folk_floor": 0.3,
    "inv_e": 0.3678794412,
    "n": 200,
    "p_derange": 0.369875,
    "pass": true,
    "z_floor": 40.937939,
    "z_inv_e": 1.169146
  },
  "G3_n_invariance": {
    "means": {
      "10": 1.004275,
      "100": 1.0002125,
      "1000": 1.000425,
      "2000": 0.9824
    },
    "pass": true,
    "plan": [
      [
        10,
        80000
      ],
      [
        100,
        80000
      ],
      [
        1000,
        40000
      ],
      [
        2000,
        25000
      ]
    ],
    "range": 0.021875,
    "z_vs_1": {
      "10": 1.209153,
      "100": 0.060104,
      "1000": 0.085,
      "2000": -2.782804
    }
  },
  "G4_poisson1_shape": {
    "M": 80000,
    "buckets": "k=0,1,2,3,>=4",
    "chi2": 1.36372,
    "counts": [
      29316,
      29462,
      14767,
      4954,
      1501
    ],
    "crit_0p001": 18.467,
    "df": 4,
    "expected": [
      29430.3553,
      29430.3553,
      14715.1776,
      4905.0592,
      1519.0526
    ],
    "n": 100,
    "pass": true
  },
  "decision": "sim-ready",
  "gates": {
    "G1": true,
    "G2": true,
    "G3": true,
    "G4": true
  },
  "seed": 20260717
}

in_process_double_run: IDENTICAL
results_sha256: 7b99e6504b7cfa776ce871b7756b2ff71ed5bcd025e9dd6134d0f8d8e246dfb0
decision: sim-ready
```
results-dict sha256: `7b99e6504b7cfa776ce871b7756b2ff71ed5bcd025e9dd6134d0f8d8e246dfb0`

## Honest nuance (disclosed)
- Mean/variance = 1 are *exact at every finite n≥2* (G1, Fraction-exact); the Poisson(1) *shape* (G4) and the 1/e derangement value (G2) are limits — at finite n they differ from the limit by O(1/(n−k)!) terms, astronomically small at n=100/200 but not literally zero. G4 tests "indistinguishable from Poisson(1) at this n," not "equals Poisson(1)."
- G2's ≥3σ signal is framed against a folk floor of 0.30 (well below the true ≈0.3679) so the gate reports the *direction* people get wrong (derangements are common, not vanishing), plus a two-sided check against 1/e itself.
- G3 uses per-scale M, so each single mean's σ shrinks with sample size; the hard condition is the cross-scale *range*, which is the invariance claim.

## Dedup
No prior idea keys on fixed points, derangements, or rencontres numbers (grep `derangement`, `rencontres`, `hat-check`, `1/e`, `random permutation` → zero collisions on this mechanism). Two shipped heads use a uniform random permutation as their *object* but key on a **different invariant** — cycle-length structure: `ideas/fleet/hundred-prisoners-2026-07-20.md` (no cycle exceeds n/2) and `ideas/fleet/cycle-following-coupling-lever-2026-07-16.md` (cycle-skeleton coupling). This proposal keys on the **fixed-point count** (cycles of length 1) and derangements — a distinct invariant, distinct number (E=1, not the H₂ₙ−Hₙ long-cycle law), distinct verifier. Disclosed adjacency, no overlap.

## Reproduce
```
python3 ideas/fleet/hat-check-fixed-points-invariance.py
```
Deterministic: SEED=20260717, stdlib-only. Prints the results dict and its sha256; the same 64-hex digest appears here, in the session card, and in control/outbox.md's P204 block.

## Verifier
`ideas/fleet/hat-check-fixed-points-invariance.py` — stdlib-only (`fractions`, `itertools`, `random`, `math`, `hashlib`, `json`). Enumerates n=1..8 exactly (G1) and runs the three Monte-Carlo gates from one seeded RNG (G2–G4); asserts an in-process double-run reproduces the identical results-dict before emitting the digest.

## Why it matters
"An average exactly invariant to system size while individuals fluctuate wildly" is the shape behind load-balancing self-collisions, hash-table self-mappings, and retry-storm self-hits: the *expected* number of self-collisions under a full permutation-style remap is a size-independent constant (≈1), and the tail that actually bites — the ≈37% chance of a total reshuffle with zero survivors — is exactly what capacity math misses when it assumes "more slots ⇒ more survivors." A clean, exactly-provable anchor for that intuition is worth pinning.

## Model basis (declared model-dependence)
The result depends only on "uniform random permutation" (every reassignment equally likely, Fisher–Yates). Under biased shuffles (patrons grab nearby coats) the mean can shift; the claim is scoped to the uniform model — the standard idealization of the hat-check problem.

## Probe report (v0, 2026-07-20)
**1. What is the precise claim, and which parts are exact vs asymptotic?** Mean = 1 and variance = 1 are EXACT for all n≥2, proven by exhaustive Fraction enumeration in G1; the derangement value 1/e (G2) and the Poisson(1) shape (G4) are limits, tested as "indistinguishable at n=200/100."
**2. Is it counterintuitive in a defensible way?** Yes — two common intuitions (self-matches grow with the crowd; someone always matches in a big crowd) are both wrong: the mean is pinned at 1 and ~37% of the time nobody matches.
**3. Is it deterministic and stdlib-only?** Yes — SEED=20260717; `fractions/itertools/random/math/hashlib/json`; an in-process double-run and a separate cross-invocation both reproduce one 64-hex digest.
**4. Can an independent re-implementation reproduce it?** Yes — the model is fully specified (uniform permutation via Fisher–Yates, fixed gate constants and seed); sim-lab reproduces the digest byte-for-byte.
**5. What is the strongest disconfirming check?** G1's exact enumeration: if E≠1, or Var≠1 for any n≥2, or the three derangement counts disagree for any n∈1..8, the head is false — these are Fraction-exact with zero tolerance.
**6. Where could it silently pass while being wrong?** If the RNG were reseeded or reused out of order, or floats formatted platform-dependently — mitigated by one seeded RNG consumed in fixed gate order and rounding every Monte-Carlo output to fixed decimals before hashing.
**7. Is the grounding external and does it support THIS head?** Yes — Rencontres_numbers (Wikipedia, byte-pinned revision 1340506236) states the fixed-point mean/variance and derangement facts firsthand; caveat: the page *states* the facts, the verifier *proves* them (phenomenon-on-page vs firsthand-witness), and the pin is to raw wikitext, not the rendered page.
**8. What is the dedup status?** Clear on mechanism (fixed points / derangements / rencontres); the only adjacency is two shipped heads that use permutations for CYCLE-LENGTH structure, not fixed points — disclosed in the Dedup section.

**Recommendation: sim-ready**
