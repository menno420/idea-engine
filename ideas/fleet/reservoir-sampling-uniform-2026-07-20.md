# Reservoir sampling is exactly fair — one streaming pass under Algorithm R leaves every one of n items in the size-k reservoir with probability exactly k/n, whatever the arrival order

> **State:** sim-ready
> **Class:** counterintuitive-but-exactly-true · streaming algorithms / combinatorial probability (round-53 FLEET slot)
> **Target:** sim-lab (VERDICT 234, +13 offset)
> **Grounding:** https://en.wikipedia.org/w/index.php?oldid=1365118921@daf21f648c352d230e4640de6a7574aaf9ac83fc · fetched 2026-07-20
> **Verifier (firsthand):** stdlib-only, SEED=20260717; results-dict sha256 721cabd10d50672c6ddae8a893c0cc773c727fdb9f6d789e27aa8e7ad7dd0190

## The phenomenon (one line)
Stream n distinct items past a reservoir that holds only k of them — fill the first k slots, then for each later arrival i (i>k) draw j uniform in [1,i] and, if j≤k, overwrite slot j with the new item. When the stream ends, EVERY one of the n items — the first arrival and the last alike — sits in the reservoir with probability exactly k/n, and every k-subset of the n items is equally likely, with no second pass and no knowledge of n in advance.

## The folk belief
"Whatever you keep from a stream you saw earliest is over-represented — the first items had many chances to be evicted, and the last items barely had a chance to be considered, so a single online pass must be biased toward the tail (or, if you only replace rarely, toward the head)." The intuition treats 'survived many eviction rounds' and 'only just arrived' as obviously unequal fates. They are not: the shrinking acceptance probability k/i for later arrivals exactly cancels the accumulating eviction risk on earlier ones, and the net inclusion probability is the same flat k/n for all n positions.

## The thesis (reasoned to fuller form — Q-0254 duty)
Algorithm R balances two opposing forces so precisely that they annihilate. A late item i>k enters the reservoir only with probability k/i (it is accepted iff its uniform draw j lands in [1,k]); that acceptance probability shrinks toward the end of the stream. An early item, once in the reservoir, must SURVIVE every subsequent arrival: at step i it is evicted only if the new item is accepted (prob k/i) AND that new item targets this specific slot (prob 1/k), i.e. with probability 1/i, so it survives step i with probability 1−1/i = (i−1)/i. Chain the survivals: an item present after step k survives to the end with probability ∏_{i=k+1}^{n} (i−1)/i = k/n by telescoping. Multiplying an item's entry probability by its survival probability gives, for EVERY item, exactly k/n — the newest arrival (entry k/n, survives trivially) and the oldest (entry 1, survival k/n) included at the same rate. The result is order-free because the argument never used which item arrived when, only its index in the stream; permuting arrivals permutes the bookkeeping but not the k/n conclusion. Sharper still, the algorithm is uniform over k-SUBSETS, not merely over marginal inclusion: all C(n,k) subsets are equiprobable, which is the property a correct sample must have and which marginal k/n alone would not guarantee.

## The formal model (committed constants, exact)
- Stream = the ordered sequence of n distinct items (labelled by arrival index 1..n); reservoir = k slots. Algorithm R: for i≤k place item i in slot i; for i>k draw j = uniform integer in [1,i], and if j≤k set slot j ← item i (else discard item i).
- Exact core identity (looped `fractions.Fraction`, NOT hardcoded to k/n): for each item index i, form its inclusion probability as the literal product of its entry factor and per-step survival factors — entry = 1 for i≤k else Fraction(k,i); survival across steps t=max(i,k)+1..n = ∏ (1 − Fraction(1,t)) for an item already resident, with the i≤k and i>k cases assembled from the per-step Fraction factors. Claim: this looped product == Fraction(k,n) for every i in 1..n and every config (n,k).
- Subset-uniformity object: over all C(n,k) k-subsets, the empirical selection frequency is uniform; tested exactly by frequency count and χ² for the small config (6,3), where C(6,3)=20 subsets must all appear with equal expected frequency.
- Configs committed: (n,k) = (40,8) and (25,5) for the exact/inclusion legs (both have k/n = 1/5), and (6,3) for exhaustive subset-uniformity.
- G1's exact leg uses `fractions.Fraction` — no floating point enters the inclusion identity; G2/G3/G4's Monte-Carlo legs are seeded sampling cross-checks of the flat-k/n law and the subset-uniformity property.

## Pinned world (committed constants)
SEED=20260717 · all randomness from `random.Random(20260717)` · exact inclusion identity on configs (40,8) and (25,5) · Monte-Carlo 80000 trials/config, probes at item indices {1, k, k+1, n} · shuffled-arrival robustness on (40,8) · exhaustive subset-uniformity on (6,3), C(6,3)=20, χ² df=19, critical value 43.8 (α≈0.001) · falsifiability bug = unconditional-replace (drop the j≤i / j≤k acceptance gate) and the analytic first-k naive model {1 for i≤k, 0 for i>k}.

## Pre-registered gates (sim-ready iff ALL hold, in order)
**G1 — Exact inclusion identity (Fraction ==).** For every item i in 1..n across configs (40,8) and (25,5), the looped `Fraction` inclusion product equals `Fraction(k,n)` (= 1/5) exactly. *Direction:* any analytic inclusion probability ≠ k/n ⇒ FAIL. **PASS** (all items equal 1/5, both configs).
**G2 — Monte-Carlo agreement (≥3σ).** For probes {1, k, k+1, n}, 80000 trials/config, the empirical inclusion frequency lands within 3·SE of k/n. *Direction:* max |z| ≥ 3 ⇒ FAIL. **PASS** (max |z| = 0.760140 for (40,8), 1.175565 for (25,5) — all < 3).
**G3 — Robustness (order-invariance + subset-uniformity).** (a) Under a shuffled arrival order on (40,8) the probe inclusion frequencies still match k/n: probe z = {1.122532, 0.919239, −1.210920, −2.306936}, max |z| = 2.306936 < 3. (b) On (6,3) all C(6,3)=20 subsets are observed and the selection is uniform: χ² = 15.0832 < 43.8 (df=19). *Direction:* stream-order dependence OR non-uniform k-subsets ⇒ FAIL. **PASS**.
**G4 — Falsifiability (the gate must REJECT wrong models).** The unconditional-replace bug (drop the acceptance gate so every arrival overwrites a random slot) deviates from k/n at max |z| = 400.0 — the last item then always occupies a slot (freq 1.0) while early items collapse to ≈0.014 — so it is marked REJECTED. The analytic first-k naive model {1 for i≤k, 0 for i>k} is a second rejected alternative. *Direction:* PASS iff the wrong model is REJECTED at max |z| ≥ 6. **PASS** (both wrong models rejected).

## Pre-registered decision rule
sim-ready iff G1 ∧ G2 ∧ G3 ∧ G4 all hold in their stated directions, AND determinism holds (both the in-process double-run and separate-process byte-identical stdout), AND both deliberately-wrong models (unconditional-replace bug; first-k naive) are REJECTED.

## Dry-sim results
```json
{
  "proposal": 221,
  "seed": 20260717,
  "configs": [[40, 8], [25, 5]],
  "target_k_over_n": "1/5",
  "g1_exact_inclusion": {
    "40,8": {
      "n": 40,
      "k": 8,
      "target": "1/5",
      "all_items_equal_k_over_n": true,
      "distinct_inclusion_values": ["1/5"],
      "hardcoded_to_k_over_n": false,
      "sample_items": {"1": "1/5", "8": "1/5", "9": "1/5", "40": "1/5"}
    },
    "25,5": {
      "n": 25,
      "k": 5,
      "target": "1/5",
      "all_items_equal_k_over_n": true,
      "distinct_inclusion_values": ["1/5"],
      "hardcoded_to_k_over_n": false,
      "sample_items": {"1": "1/5", "5": "1/5", "6": "1/5", "25": "1/5"}
    }
  },
  "g2_montecarlo": {
    "trials_per_config": 80000,
    "probe_indices": [1, "k", "k+1", "n"],
    "40,8": {"max_abs_z": 0.760140, "within_3sigma": true},
    "25,5": {"max_abs_z": 1.175565, "within_3sigma": true}
  },
  "g3_robustness": {
    "shuffled_order_40_8": {
      "probe_indices": [1, "k", "k+1", "n"],
      "z": [1.122532, 0.919239, -1.210920, -2.306936],
      "max_abs_z": 2.306936,
      "within_3sigma": true
    },
    "subset_uniformity_6_3": {
      "n": 6,
      "k": 3,
      "subsets_observed": 20,
      "subsets_total": 20,
      "chi_square": 15.0832,
      "df": 19,
      "critical_0p001": 43.8,
      "uniform": true
    }
  },
  "g4_falsifiability": {
    "unconditional_replace_bug": {
      "max_abs_z": 400.0,
      "late_item_freq": 1.0,
      "early_item_freq_approx": 0.014,
      "rejected": true
    },
    "first_k_naive_model": {
      "model": "{1 for i<=k, 0 for i>k}",
      "rejected": true
    },
    "both_wrong_models_rejected": true
  },
  "determinism": {
    "determinism_double_run": true,
    "two_process_byte_identical": true,
    "stdout_sha256": "703f6048dd5e4a775ea8cb79fede6b11c00ce52db4bbc82e0cc54e856121afe7"
  },
  "gates": {
    "G1": true,
    "G2": true,
    "G3": true,
    "G4": true
  },
  "sim_ready": true
}
```
results_sha256=721cabd10d50672c6ddae8a893c0cc773c727fdb9f6d789e27aa8e7ad7dd0190

**Disclosed results-dict sha256 = `721cabd10d50672c6ddae8a893c0cc773c727fdb9f6d789e27aa8e7ad7dd0190`** — every item is included with probability exactly k/n (G1: the looped `Fraction` product == 1/5 for all items in both (40,8) and (25,5), never hardcoded to the telescoped k/n); Monte-Carlo agrees at max |z| = 0.760140 and 1.175565; all C(6,3)=20 subsets are uniform (χ² = 15.0832 < 43.8); and the unconditional-replace bug is rejected at z = 400.0. In-process `determinism_double_run=True`; two separate processes print byte-identical stdout (sha256 703f6048dd5e4a775ea8cb79fede6b11c00ce52db4bbc82e0cc54e856121afe7).

## Verifier
`sims/verdict-234-reservoir-sampling/reservoir-sampling-uniform.py` (menno420/sim-lab, PR #313, merge SHA 872a84763f1aed1e0a56a6a9a47ddee148976c59) — stdlib only (`fractions`, `itertools`, `math`, `random`, `hashlib`, `json`, `sys`), SEED=20260717, all randomness from `random.Random(20260717)`; the results dict is built twice and both canonical dumps are asserted identical before exit.
```reproduce
python3 sims/verdict-234-reservoir-sampling/reservoir-sampling-uniform.py
# prints the results JSON, then results_sha256=721cabd10d50672c6ddae8a893c0cc773c727fdb9f6d789e27aa8e7ad7dd0190, then determinism_double_run=True; exits 0
# each process's stdout sha256 = 703f6048dd5e4a775ea8cb79fede6b11c00ce52db4bbc82e0cc54e856121afe7 (two processes byte-identical)
```

## Why it matters
Reservoir sampling is the canonical fixed-memory answer to "keep a uniform sample from a stream of unknown length" — log sampling, A/B bucketing, telemetry down-sampling, database SAMPLE clauses, and any single-pass draw from data too large to store all rely on the exact k/n guarantee. The counterintuitive part is that it is EXACTLY fair with one pass, no rewind, and no advance knowledge of n: the shrinking acceptance rate k/i for late arrivals cancels the accumulating eviction risk on early ones to the last bit, so there is no head/tail bias to correct for. It is also the base case for the weighted (A-Res/A-ExpJ) and sublinear (Algorithm L) variants — get the uniform inclusion law right and the weighted generalizations inherit its correctness proof.

## Dedup
Grepped all lanes (`ideas/**`) at boot: no reservoir-sampling / Algorithm-R / streaming-uniform card exists (`grep -rilE 'reservoir|algorithm.r|waterman|vitter' ideas/` returned nothing; no slug collision on `reservoir-sampling-uniform`). Distinct from the three nearest neighbours: **coupon-collector-tail** (P052 — the n·H_n *time to collect all* coupons, a completion-time sum, not a per-item inclusion probability under bounded memory); **consistent-hashing-max-gap-harmonic** (P217 — the maximum of n uniform circular *spacings* = H_n/n, a geometric max-of-gaps, not a streaming sample); **two-choices-routing-cliff** (P113 — power-of-two-choices load balancing, a placement-variance result, unrelated to sampling). This card's object is the exact k/n inclusion law (and C(n,k)-subset uniformity) of Algorithm R over an ordered stream — no existing card computes it.

## Model basis (declared model-dependence — the P024 discipline)
The result is exact GIVEN the model: n distinct items, a size-k reservoir, and Algorithm R with a uniform integer draw in [1,i] at each arrival i>k. It assumes distinct items (so 'inclusion of item i' is unambiguous) and a true uniform RNG; a biased RNG or non-distinct items shift the accounting. G1's exact leg carries no probabilistic assumption (a `Fraction` identity over the per-step entry/survival factors); G2/G3/G4's Monte-Carlo legs are seeded sampling cross-checks of the flat-k/n law and subset-uniformity, not the proof.

Grounding caveat (accurate to the pinned revision): Pinned to English Wikipedia "Reservoir sampling", revision oldid 1365118921 (fetched 2026-07-20). This revision describes Algorithm R and attributes it to Alan G. Waterman, with references to Knuth's TAOCP (pp. 138–139) and Vitter (1985); it proves the uniform-sampling property by induction, showing each new input is retained with probability k/(i+1) and each prior item survives with probability (k/i)·(1−1/(i+1)) = k/(i+1), which yields the standard k/n inclusion result at the end of the stream. Note the article states this as step-wise k/i and k/(i+1) probabilities rather than the literal phrase "k/n". The same revision also covers weighted reservoir sampling (A-Res/A-ExpJ, Efraimidis–Spirakis) and the unweighted sublinear Algorithm L (Kim-Hung Li).

## One-line design fix
When a stream sample looks tail-heavy in practice, the bug is almost never Algorithm R itself but a broken acceptance gate — dropping the `j≤k` test (unconditional replace) makes the newest item always resident (freq 1.0) and starves the head to ≈0.014; keep the gate and the sample is exactly k/n uniform with fixed k-slot memory.

## Probe report (v0, 2026-07-20)
**1. Is the headline claim exactly true or only statistically likely?** Exactly true for the identity: G1 computes each item's inclusion probability as a looped `Fraction` product (entry × per-step survival) and asserts it equals `Fraction(k,n)` = 1/5 for every item i in 1..n across (40,8) and (25,5); the Monte-Carlo gates (G2/G3) only cross-check the closed form by sampling, they do not establish it.
**2. Is the sampling model unambiguously defined?** Yes: n distinct items arrive in order, the reservoir has exactly k slots, the first k items fill slots 1..k, and each later arrival i draws j uniform in [1,i] and overwrites slot j iff j≤k — the acceptance rate is k/i and the object of study is each item's end-of-stream inclusion probability, committed as constants in the model section.
**3. Does the exact identity actually telescope to k/n, or is that asserted?** It is computed, not asserted: G1 evaluates the entry×survival product ∏(1−1/t) factor-by-factor as `Fraction`s (never substituting the closed form) and asserts equality with `Fraction(k,n)`; G4 further shows that dropping the acceptance gate breaks the identity (z=400.0), so the gate structure is load-bearing.
**4. Could the k/n result be an artifact of the two chosen configs?** No: G1 holds item-by-item on two independent configs (40,8) and (25,5), G3(b) exhaustively enumerates all C(6,3)=20 subsets of a third config and requires uniform selection (χ²=15.0832<43.8), and G3(a) reruns under a shuffled arrival order — a config-specific coincidence would fail one of these rather than pass quietly.
**5. Is the ≥3σ gate a real check or a tautology given the exact identity?** It is an independent seeded sampling cross-check: G2 draws 80000 fresh streams per config from `random.Random(20260717)` and tests the empirical inclusion frequency at probes {1,k,k+1,n} against k/n (max |z| = 0.760140 and 1.175565, both < 3); it would flag any mismatch between the sampler and the flat-k/n law.
**6. Is the result invariant to arrival order / does position sneak in?** Yes and checked: G3(a) reruns the Monte-Carlo on a SHUFFLED arrival order for (40,8) and reproduces k/n at every probe (max |z| = 2.306936 < 3), while the telescoping proof never referenced arrival time — inclusion is k/n for the first and last item alike, so no head/tail bias exists.
**7. Is the grounding an external citation and is its caveat accurate to the pinned revision?** The grounding pins Wikipedia "Reservoir sampling" oldid 1365118921 (sha1 daf21f648c352d230e4640de6a7574aaf9ac83fc). That revision describes Algorithm R (attributed to Waterman; Knuth TAOCP pp. 138–139, Vitter 1985) and proves uniformity by induction via the step-wise k/i and k/(i+1) probabilities, yielding the k/n result — but it states the step-wise probabilities rather than the literal phrase "k/n", and it also covers weighted (A-Res/A-ExpJ) and Algorithm L. Our verifier's looped-`Fraction` inclusion identity, the subset-uniformity χ², the seeded significance tests, and the falsifiability rejections are its OWN firsthand computations; the caveat is honest — neither oversold nor undersold.
**8. Is the verifier deterministic and reproducible cross-invocation?** Yes: no wall-clock or OS entropy; all randomness comes from `random.Random(20260717)` consumed in a fixed order, the results dict is built twice and both canonical dumps asserted identical (determinism_double_run=True), and two separate invocations printed the byte-identical stdout digest 703f6048dd5e4a775ea8cb79fede6b11c00ce52db4bbc82e0cc54e856121afe7 (results-dict sha256 721cabd10d50672c6ddae8a893c0cc773c727fdb9f6d789e27aa8e7ad7dd0190).

**Recommendation: sim-ready**
