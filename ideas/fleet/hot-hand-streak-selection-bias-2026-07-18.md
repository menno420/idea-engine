# The hot-hand streak-selection bias — a fair, memoryless coin looks anti-streaky when you measure "what happens after a streak" in a finite sequence

> **State:** sim-ready
> **Class:** unrelated-domain (round-33 unrelated slot) · finite-sample selection bias / law of small numbers · PROPOSAL 144
> **Target:** sim-lab (VERDICT 157, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@9678a2b4be285f7ddb9c89d430ae7a0a208ca713 · fetched 2026-07-18T19:39:36Z
> **Source basis:** Miller & Sanjurjo, "Surprised by the Hot Hand Fallacy? A Truth in the Law of Small Numbers", *Econometrica* 86(6):2019-2047, 2018; Gilovich, Vallone & Tversky, "The Hot Hand in Basketball", *Cognitive Psychology* 17(3):295-314, 1985 (the original null this result overturns). Standard published result; external reference https://en.wikipedia.org/wiki/Hot_hand (verified reachable 2026-07-18 via WebFetch). No external repo fetched.
> **Verifier (firsthand):** committed stdlib-only `ideas/fleet/hot_hand_streak_selection_bias.py`, SEED=20260717, results-dict sha256 `1c262684265b51e714365a29aa1209ff646b13975d554a404aaf144927b2dac3` (deterministic double-run, exit 0).

## Domain

Finite-sample statistics / the law of small numbers — outside the fleet, venture, and game-mechanics domains. The object is the humblest possible one: a run of **fair, independent coin flips**. The question is the one every "streakiness" audit implicitly asks: *after a streak of successes, is the next trial more, less, or equally likely to be a success?* This is the exact estimator that the famous 1985 Gilovich–Vallone–Tversky study used to declare the basketball "hot hand" a cognitive illusion — and the exact estimator Miller & Sanjurjo (2018) showed is silently biased.

## The folk belief

"A fair coin is memoryless. So if I look at every flip that comes right after a run of `k` heads and ask what fraction of *those* flips are heads, the answer must be exactly 0.5 — the coin cannot 'know' it just came off a streak." Under this belief, an empirical fraction below 0.5 is read as evidence of **negative** autocorrelation (an anti-streak, a "gambler's-fallacy" mechanism, a mean-reverting process). The 1985 hot-hand study made precisely this move: shooters' post-hit hit-rate was ≈ their base rate (even slightly below), so "no hot hand."

## The thesis (reasoned to its fuller form)

The expected value of that fraction is **strictly below 0.5** for a fair memoryless coin — with no autocorrelation anywhere in the process. The 0.5 baseline is *wrong*, so the correct null the 1985 study should have compared against was already below the base rate, and a hit-rate *at* the base rate is actually evidence *for* a hot hand.

The mechanism is a **selection/sampling bias inside each finite sequence**, not memory in the coin:

- Fix a single finite sequence of `N` flips. Define its estimator as (heads among flips that immediately follow a run of `k` heads) ÷ (number of such selected flips), computed only when the sequence has ≥1 such flip.
- Within that one sequence, the *act of selecting* a flip because its `k` predecessors were heads is negatively correlated with that flip being a head. A head at position `j` tends to *extend* the current run and be consumed as a predecessor of later selections; a tail *ends* the run. Conditioning on "the `k` flips before `j` are heads" and then averaging the **ratio** across sequences (equal weight per sequence, not pooled) pulls the expected ratio below 0.5.
- It is the finite, per-sequence **ratio averaging** that does it — the same reversal that makes the average of per-group rates differ from the pooled rate. Pooling all selected flips across infinitely many sequences would give 0.5; averaging each finite sequence's own fraction does not.

This is a **law-of-small-numbers** effect: it vanishes as `N → ∞` and grows as `k` grows or `N` shrinks. It has an exact closed form — the finite-sequence expectation is a deterministic combinatorial quantity, computable by summing the per-sequence fraction over all `2^N` equally likely sequences.

## The trap

Any "streakiness" audit that (a) works on **finite** runs and (b) compares the post-streak success rate against a **0.5 / base-rate** null is measuring the bias, not the phenomenon. It will (i) declare a genuinely memoryless process "mean-reverting / anti-streaky," and (ii) *hide* real positive streakiness of magnitude smaller than the bias. The correct null is the **exact finite-sequence expectation**, which sits below the base rate by an amount that depends on `N` and `k`.

## Formal model (committed constants)

`N` fair i.i.d. coin flips (heads = 1, p = 1/2). A position `j ∈ [k, N-1]` is *selected* iff flips `j-k … j-1` are all heads (overlapping windows allowed — the Miller–Sanjurjo convention). Per-sequence estimator = (selected flips that are heads) ÷ (selected flips), defined iff ≥1 selected flip. Pinned: SEED=20260717, N=15, K=3, M=400000 Monte-Carlo sequences, SIGMA_GATE=3.0. The **exact** Miller–Sanjurjo expectation is computed by exhaustive enumeration of all `2^15 = 32768` sequences (deterministic, no RNG) and used as the closed-form reference the Monte-Carlo run is gated against.

## Pre-registered gates (ordered; each on the /se margin, one pinned SEED)

| Gate | Statistic | Claim | Pass rule |
|---|---|---|---|
| **G1** estimator-agreement | z = (mean_firsthalf − mean_secondhalf) / se_diff | the two independent halves of the M per-sequence fractions do not disagree (the estimate is stable, not a split artifact) | \|z\| < 3 |
| **G2** closed-form agreement | z = (mc_mean − e_exact) / mc_se | the Monte-Carlo mean is not significantly different from the exact enumerated Miller–Sanjurjo expectation (the sim measures the right quantity) | \|z\| < 3 |
| **G3** head (below one-half) | z = (0.5 − mc_mean) / mc_se | the post-streak head fraction is significantly BELOW 0.5 for a fair memoryless coin | z ≥ 3 |

## Pre-registered decision rule

sim-ready iff G1 ∧ G2 ∧ G3 all pass, in order, at the pinned SEED, with a deterministic double-run reproducing the disclosed results-dict sha256.

## Dry-sim results (firsthand, verbatim)

```
{
  "all_pass": true,
  "exact": {
    "bias_vs_half": -0.14711,
    "defined_sequences": 21232,
    "e_exact": 0.35289,
    "total_sequences": 32768
  },
  "first_failing_gate": null,
  "gates": {
    "G1_estimator_agreement": {
      "mean_first_half": 0.353071,
      "mean_second_half": 0.353576,
      "pass": true,
      "rule": "|z| < sigma_gate",
      "stat": "z = (mean_firsthalf - mean_secondhalf) / se_diff",
      "z": -0.384486
    },
    "G2_closed_form_agreement": {
      "e_exact": 0.35289,
      "mc_mean": 0.353323,
      "pass": true,
      "rule": "|z| < sigma_gate",
      "stat": "z = (mc_mean - e_exact) / mc_se",
      "z": 0.660242
    },
    "G3_head_below_half": {
      "mc_mean": 0.353323,
      "pass": true,
      "rule": "z >= sigma_gate",
      "stat": "z = (0.5 - mc_mean) / mc_se",
      "z": 223.601743
    }
  },
  "mc": {
    "mc_bias_vs_half": -0.146677,
    "mc_mean": 0.353323,
    "mc_se": 0.000656,
    "n_defined": 259246,
    "undefined_dropped": 140754
  },
  "params": {
    "k_streak": 3,
    "m_sequences": 400000,
    "n_flips": 15,
    "seed": 20260717,
    "sigma_gate": 3.0
  },
  "phenomenon": "hot-hand streak-selection bias (Miller-Sanjurjo finite-sequence selection bias)",
  "proposal": 144
}
Results-JSON sha256: 1c262684265b51e714365a29aa1209ff646b13975d554a404aaf144927b2dac3
```

All three gates PASS in order; exit 0; the second run reproduces the identical sha256. The exact finite-sequence expectation is **0.35289** — a fair memoryless coin's post-(3-head)-streak head fraction is expected ≈ 14.7 points BELOW 0.5 at N=15 — and the Monte-Carlo mean (0.353323) lands on it (G2 z=0.66) while sitting 224σ below 0.5 (G3).

## Verify

```
python3 ideas/fleet/hot_hand_streak_selection_bias.py
```

Deterministic: same SEED → identical results dict → identical sha256; exit 0 iff all three gates pass in order.

## Fleet relevance

The fleet routinely measures "streaks" of success/failure in ops metrics: retry-after-retry success, "green builds after a green build," an agent's post-win-run win rate, "does a lane keep passing once it starts passing." Any such audit that works on a **finite** window and benchmarks the post-streak rate against the unconditional base rate is running the Gilovich-1985 estimator — and will read a memoryless lane as *anti-streaky*, or bury a real positive streak smaller than the built-in bias. The transferable rule: **when you condition on "the last k trials succeeded" inside finite windows, the correct null is the exact finite-sequence expectation, which is strictly below the base rate — never benchmark a post-streak rate against the base rate directly.** Compute the enumerated null (cheap: `2^N` for the window length) and compare against that.

## Model basis (declared model-dependence — the P024 discipline)

The result is a theorem about i.i.d. fair Bernoulli sequences under (a) the overlapping-window streak-selection convention, (b) per-sequence **ratio** averaging conditioned on ≥1 selected flip, and (c) a finite `N`. It is model-dependent on all three: pooling selected flips across sequences (rather than averaging ratios) removes the bias; `N → ∞` removes it; a biased or autocorrelated coin shifts the null but does not remove the finite-sample term. The magnitude scales UP with `k` and DOWN with `N`. These are disclosed, not hidden — the closed-form null is the whole point, and its dependence on `N` and `k` is exactly what an audit must compute rather than assume.

## Dedup

Distinct from every prior fleet/unrelated head. The unrelated-domain lane has spanned social choice (P017), congestion routing (P024 Braess / two-choices P113), tournament seeding (P028), pattern races (Penney P032), the secretary problem (P039-family), German-tank estimation, Benford, Stein shrinkage, gambler's ruin, birthday collisions, arcsine, coupon-collector, inspection paradox, PPV/base-rate collapse, Simpson's paradox, friendship paradox, regression to the mean, series-MTBF — none of them is a finite-sequence streak-selection bias on i.i.d. fair coins. Nearest rhymes, disclosed: **regression-to-the-mean** (`regression-to-mean-2026-07-18`) is about extreme selection on a noisy score reverting, not conditioning on a run inside one finite sequence; **Penney's game** (`penney-game-responder-edge-decay`) is about which *pattern* wins a race, not the post-streak rate of a single symbol; **arcsine lead illusion** is about lead-duration distribution, not conditional next-flip rate. The hot-hand was explicitly a named runner-up "weighed and dropped on merit" in `secretary-rule-cardinal-regret-2026-07-13.md` — it has never been proposed. This head takes exactly that open slot.

## Probe report (v0, 2026-07-18)

**1. Real or a coding artifact?** Real — it is the Miller & Sanjurjo (2018) theorem, published in *Econometrica*. The exact enumerated expectation (0.35289 at N=15, k=3) is computed independently of the Monte-Carlo run and the MC lands on it (G2).
**2. Could the sub-0.5 result be a seed fluke?** No — 259,246 defined sequences, per-sequence fractions, the head gate clears at z=223.6; and the estimate is split-half stable (G1 z=−0.38).
**3. Is this just negative autocorrelation dressed up?** No — the coin is provably i.i.d. fair (`rng.random() < 0.5`, independent per flip). The bias is in the finite-sample *estimator*, not the process. That is the entire surprise.
**4. Why average ratios instead of pooling?** Because that is the estimator the folk audit (and the 1985 study) actually uses — "each shooter/sequence gets one post-streak rate, then average." Pooling across sequences would give 0.5; the bias is a property of the per-sequence conditional estimator, exactly the one people compute.
**5. Why k=3, N=15?** k=3 makes the bias large and unmistakable (~0.147) while N=15 keeps the exact `2^15` enumeration instant and the per-sequence selected-flip counts non-trivial; larger k or smaller N widen the bias, larger N shrinks it toward 0 (disclosed as the law-of-small-numbers scaling).
**6. What about sequences with no streak?** Dropped as undefined (140,754 of 400,000), exactly as the enumeration conditions on ≥1 selected flip — the MC and the exact reference condition identically, which is why G2 passes.
**7. What breaks it?** Pooling instead of ratio-averaging, or N→∞; both are disclosed model-dependence. A biased/autocorrelated coin moves the null but the finite-sample selection term persists.
**8. Actionable?** Yes — any finite-window "streakiness" audit in the fleet must benchmark post-streak rates against the enumerated finite-sequence null (strictly below base rate), not against the base rate itself.

Ship to sim-lab for VERDICT 157 (P144 → V157, +13). One counterintuitive result (a fair memoryless coin reads anti-streaky under the natural estimator), one published anchor (Miller–Sanjurjo 2018), an exact enumerated closed-form null, three ordered ≥3σ gates, a deterministic committed verifier.

**Recommendation: sim-ready**
