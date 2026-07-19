# PROPOSAL 155 — speedrun record drought: in any i.i.d. sequence of attempt times the k-th attempt sets a new personal-best (a strictly-new running minimum, lower=better) with probability EXACTLY 1/k, so lifetime PB records grow only as the harmonic number H_N ≈ ln N + γ — squaring the attempt count (×100) multiplies PB records by only ~1.887, and the cadence is distribution-free

> **State:** sim-ready
> **Class:** superbot-games · leaderboard / speedrun telemetry · theory of records (running minima of i.i.d. sequences)
> **Slot:** round-37 GAME
> **Anchor:** theory of records — in an i.i.d. (exchangeable) continuous sequence the k-th term is a record with probability 1/k independently of the value distribution (Rényi 1962), so the expected record count after N terms is the harmonic number H_N and records accumulate only logarithmically
> **Target:** sim-lab (VERDICT 168, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine/blob/claude/proposal-155-speedrun-record-drought/ideas/superbot-games/speedrun_record_drought.py@add649478c0d2c95616c591551db5c8b10a7a9b4 · fetched 2026-07-19T04:38:21Z
> **Reference (external, reachable):** Rényi, A. (1962) "Théorie des éléments saillants d'une suite d'observations" — the record-indicator independence and the 1/k record probability; Glick, N. (1978) "Breaking Records and Breaking Boards," *American Mathematical Monthly* 85(1):2–26 — expository proof that E[records after N] = H_N and records are logarithmically rare; Arnold, Balakrishnan & Nagaraja (1998) *Records* (Wiley) — the standard monograph on record statistics.
> **Verifier (firsthand):** `ideas/superbot-games/speedrun_record_drought.py` · results-dict sha256 `fa31d28495ab63c8ff9f1c502031da475bfa334c918fb29173fab26e8e489f26`
> 📊 Model: Claude Opus · high · idea/planning

## The phenomenon (one line)
Log a speedrunner's attempt times as i.i.d. draws from ANY continuous distribution; the k-th attempt is a new personal best (a strictly-new running minimum) with probability exactly 1/k, so the expected number of lifetime PB records after N attempts is the harmonic number H_N = Σ_{k=1}^N 1/k ≈ ln N + γ — records accumulate only LOGARITHMICALLY, so squaring the attempt count (×100) multiplies PB records by only ~H(N²)/H(N) ≈ 1.887, not by 100, and the cadence does not depend on the runner's time distribution.

## The folk belief
"My PBs dried up because I plateaued, the game got harder, or I lost my touch." A drought of new records feels like a signal about the RUNNER. Under the i.i.d.-stationary null it is not: even a perfectly stationary runner — skill and variance never changing — sees records arrive at rate 1/k, because the k-th attempt has only a 1/k chance of beating all k−1 attempts before it. The drought is the DEFAULT behaviour of running minima of exchangeable draws, and the naive baseline "more attempts → proportionally more PBs" over-predicts records by orders of magnitude.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Model an attempt log as N i.i.d. draws from any continuous base time distribution (lower = better). A PB is a strictly-new running minimum; attempt 1 is the first PB by definition. The indicator I_k = "attempt k is a record" has P(I_k = 1) = **1/k**, and the indicators are **independent** across k (Rényi 1962): whether the minimum of the first k draws lands in position k is a statement about the RANK of an exchangeable sequence and ignores the values entirely — every ordering of k distinct draws is equally likely, so the smallest is last with probability 1/k. Hence the record COUNT after N,

    C_N = Σ_{k=1}^N I_k,  with  E[C_N] = Σ_{k=1}^N 1/k = H_N,  Var[C_N] = H_N − Σ_{k=1}^N 1/k².

Two consequences a leaderboard / telemetry designer must price in. **(1) Logarithmic cadence.** To double a runner's lifetime PB count they must roughly SQUARE their attempts (H_{N²} ≈ 2H_N for large N); a "records per week" metric decays like 1/t, so a drought is the expected trajectory, not an alarm. **(2) Distribution-free.** The record law depends only on ranks, so a heavy-tailed grind (Pareto) and a light-tailed one (Exponential) produce the SAME expected record count H_N — a PB-rate baseline needs no fit to the runner's time distribution. The right way to detect a genuinely improving player is as a DEVIATION ABOVE this stationary harmonic null, never against a linear "attempts → PBs" expectation.

Concretely (SEED = 20260717, committed constants): with N1 = 100 and N2 = 10000 = N1², the Monte-Carlo mean record count at N2 is **9.773** (harmonic law H(N2) = **9.787606**), while a linear-accumulation null calibrated at N1 predicts **520.15** records at N2. The observed count is **>11000 σ** below that linear prediction, and the observed record ratio C_{N2}/C_{N1} = **1.878881** matches H(N2)/H(N1) = **1.886812** to within |z| = 0.98. A ×100 attempt count buys ~1.887× the records, not 100×.

## The formal model (committed constants — sim-lab must reproduce exactly)
- Per Monte-Carlo trial, draw **N2** i.i.d. attempt times from a base distribution under one `random.Random(SEED)` stream; a record is a **strictly-new running minimum** (x < current min), attempt 1 always counts as the first record.
- Capture the record count at checkpoint **k = N1** and at **k = N2** within the SAME sequence (no extra draws): C_{N1} and (C_{N2} − C_{N1}) count records in DISJOINT index ranges and are therefore INDEPENDENT, so Cov(C_{N1}, C_{N2}) = Var(C_{N1}).
- Harmonic anchor: **H(n) = exact Σ_{k=1}^n 1/k** (accumulated as a float sum).
- Base distributions: G1/G2 use **Exponential** (`rng.expovariate(1.0)`); G3 uses a heavy-tailed **Pareto** (`rng.paretovariate(2.5)`) — a genuinely different shape, identical running-min record logic.
- Standard error from the sample variance across TRIALS; z on the /se convention (se = sample_sd / √TRIALS).
- **Model note (declared):** the head is an objective identity of record statistics (record probability 1/k, mean H_N, independence of indicators) for any CONTINUOUS base distribution. The single declared modelling choice is the i.i.d.-STATIONARY null (attempt times exchangeable, no drift); a real improving runner is measured as a deviation ABOVE this null. Discrete-clock ties make the exact-1/k law an approximation (continuous base ⇒ ties have probability 0).

## Pinned world (committed constants)
- SEED = 20260717
- SIGMA_GATE = 3.0
- N1 = 100, N2 = 10000 (= N1²), TRIALS = 4000
- G1/G2 base: Exponential(1.0); G3 base: Pareto(2.5)
- H(N1) = 5.187378, H(N2) = 9.787606, H(N2)/H(N1) = 1.886812

## Pre-registered gates (APPROVE iff ALL hold, in order G1 → G2 → G3)
- **G1 — harmonic law.** mean(count@N2) matches H(N2) within |z| < 3, where z = (mean − H(N2)) / (sample_sd / √TRIALS). The expected lifetime PB count is the harmonic number, not the attempt count. (Measured z = **−0.325727**.)
- **G2 — log-slowdown (HEADLINE).** The linear-accumulation null calibrated at N1 predicts mean(count@N1) · (N2/N1) records at N2. PASS iff **(a)** observed mean(count@N2) is ≥ 3 σ BELOW that linear prediction (z_linear = (linear_pred − mean@N2)/se(mean@N2) ≥ 3), AND **(b)** the observed ratio mean(count@N2)/mean(count@N1) matches H(N2)/H(N1) within |z| < 3 via the delta method (Cov(count@N1, count@N2) = Var(count@N1), disjoint ranges). Headline: squaring attempts (×100) multiplies records by only ~H(N2)/H(N1) ≈ 1.887. (Measured z_linear = **11381.841906**, z_ratio = **−0.981196**.)
- **G3 — distribution-free.** mean(count@N2) under the Pareto base matches the SAME H(N2) within |z| < 3. The cadence does not depend on the time distribution. (Measured z = **−1.285293**.)

## Pre-registered decision rule
APPROVE (sim-ready confirmed) iff G1 AND G2 AND G3 all hold in order and the verifier exits 0 with a reproducible results-dict sha256 across a deterministic double-run. Any gate failing ⇒ REJECT/REVISE naming first_failing_gate. Observed all_pass = **true**, first_failing_gate = **null**.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```
{
  "all_pass": true,
  "exp_pass": {
    "cov_count_N1_N2": 3.562131,
    "mean_count_N1": 5.2015,
    "mean_count_N2": 9.773,
    "sd_count_N1": 1.875174,
    "sd_count_N2": 2.836015,
    "se_count_N1": 0.029649,
    "se_count_N2": 0.044841,
    "var_count_N1_identity": 3.516277
  },
  "first_failing_gate": null,
  "g1_harmonic_law": {
    "H_N2": 9.787606,
    "mean_count_N2": 9.773,
    "pass": true,
    "se": 0.044841,
    "z": -0.325727
  },
  "g2_log_slowdown": {
    "headline_x100_attempts_multiplies_records_by": 1.886812,
    "linear_pred_count_N2": 520.15,
    "mean_count_N2": 9.773,
    "pass": true,
    "ratio_null_H_N2_over_H_N1": 1.886812,
    "ratio_observed": 1.878881,
    "se_ratio": 0.008083,
    "z_linear": 11381.841906,
    "z_ratio": -0.981196
  },
  "g3_distribution_free": {
    "H_N2": 9.787606,
    "dist": "pareto(2.5)",
    "mean_count_N2": 9.73,
    "pass": true,
    "se": 0.044819,
    "z": -1.285293
  },
  "gates": [
    {
      "id": "G1",
      "name": "harmonic_law",
      "pass": true,
      "z": -0.325727
    },
    {
      "id": "G2",
      "name": "log_slowdown",
      "pass": true,
      "z": 11381.841906
    },
    {
      "id": "G3",
      "name": "distribution_free",
      "pass": true,
      "z": -1.285293
    }
  ],
  "harmonic": {
    "H_N1": 5.187378,
    "H_N2": 9.787606,
    "ratio_H_N2_over_H_N1": 1.886812
  },
  "params": {
    "N1": 100,
    "N2": 10000,
    "dist_g1g2": "exponential(1.0)",
    "dist_g3": "pareto(2.5)",
    "seed": 20260717,
    "sigma_gate": 3.0,
    "trials": 4000
  }
}
Results-JSON sha256: fa31d28495ab63c8ff9f1c502031da475bfa334c918fb29173fab26e8e489f26
```
Results-dict sha256: `fa31d28495ab63c8ff9f1c502031da475bfa334c918fb29173fab26e8e489f26` (deterministic double-run, exit 0 both times, two cross-invocation stdouts byte-identical).

## Verifier
`ideas/superbot-games/speedrun_record_drought.py` — stdlib only (`random, math, json, hashlib`). Runs TRIALS=4000 Monte-Carlo trials under one seeded stream for an Exponential base and a Pareto base; each trial draws N2 i.i.d. attempt times, counts strictly-new running minima, and captures the record count at k=N1 and k=N2 in the SAME sequence. Computes the exact harmonic anchors H(N1)/H(N2), the sample means/variances/covariance, and runs the three ordered z-gates (harmonic-law anchor at N2, the log-slowdown headline vs the linear-accumulation null plus the delta-method ratio anchor, and the Pareto distribution-free anchor). Emits the whole results dict (no self-referential sha field; every float rounded to 6 decimals; the compact-canonical serialization's sha256 IS the disclosed digest; stdout dumps the pretty indent=2 view — the WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture, P127+ twist). Writes no JSON to disk; asserts the in-process double-run digests are identical before printing.

## Reproduce
```
python3 ideas/superbot-games/speedrun_record_drought.py
```
Expected: prints the results JSON, `Results-JSON sha256: fa31d28495ab63c8ff9f1c502031da475bfa334c918fb29173fab26e8e489f26`, exit 0 (all_pass=true).

## Why it matters (game design / analytics)
A leaderboard, a "personal best" tracker, a speedrun telemetry pipeline, any "am I still improving?" dashboard — all sit on top of running minima of an attempt log, and all inherit the record law. Two design consequences invert intuition: (1) PB cadence is LOGARITHMIC, so a "records this week" metric that trends toward zero is the EXPECTED behaviour of a stationary runner, not a churn signal or a plateau — punishing the drought (or celebrating a "record spree" that is really just early low-k luck) mis-reads pure rank statistics as skill; (2) the law is DISTRIBUTION-FREE, so a PB-rate baseline needs no per-runner fit — the same H_N applies to a twitch grinder and a marathon router. The right instrument for genuine improvement is a DEVIATION-ABOVE-H_N test: a runner whose record count outruns the harmonic null is actually getting faster; one who tracks it is stationary and their drought is arithmetic, not a slump. Price the harmonic law, not the linear fantasy.

## Dedup (contrast vs prior lane heads)
- vs **st-petersburg-cap-collapse (P151)** — that is a divergent-EV lottery whose fair price grows with the LOG of a payout CAP; this is running-minima record COUNTS growing with the harmonic number of the ATTEMPT count. Both are "log-slow" laws, but one is a bounded-bankroll pricing collapse and the other is order-statistics of exchangeable draws — no jackpot, no cap, no EV.
- vs **matchmaking-winrate-mirage (P111)** — Elo win-rate compression via a rating fixed point; no records, no running minima, no harmonic law.
- vs **streak-shield-regression / rank-decay-churn-cliff / pity-anticipation-collapse** — regression to the mean, loss-aversion decay, and gacha timing respectively; none models the 1/k record probability or the H_N accumulation of running minima.
- Crossover honesty: adjacent to any prior "it feels like a plateau but it's just statistics" framing, but no prior game head models the theory of records, the 1/k record indicator, or the logarithmic PB-count law. This is the FIRST record-statistics / running-minimum card in any lane.

## Model basis (declared model-dependence — the P024 discipline)
The head is an **objective identity of record statistics**, not a behavioural claim: for any CONTINUOUS i.i.d. sequence the k-th term is a record with probability exactly 1/k, the indicators are independent, and E[C_N] = H_N — all exact and confirmed by Monte-Carlo to the σ margin. The **one declared modelling choice** (flagged, not hidden): the attempt log is i.i.d.-STATIONARY (exchangeable, no drift in the runner's skill or variance) — this is the NULL against which a real improving player's drought is measured, not a claim that runners never improve. Dependence disclosed: (a) discrete-clock ties (e.g. centisecond timers) make the exact-1/k law an approximation, since ties have positive probability on a discrete grid — the continuous base here sets ties to probability 0; (b) the distribution-free property holds for any CONTINUOUS base, verified across Exponential and Pareto(2.5) shapes in G3. The magnitudes (H(N2) = 9.79, ratio 1.887, linear-null 520) are pinned to (N1, N2, TRIALS); the SIGN and the logarithmic scaling are structural to running minima of exchangeable sequences.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed | z | Verdict |
|------|------|-----------|----------|---|---------|
| G1 | anchor | |z| < 3 vs H(N2) | mean 9.773 vs 9.787606 | −0.325727 | PASS |
| G2 | headline + anchor | z_linear ≥ 3 AND |z_ratio| < 3 | 9.773 vs linear 520.15; ratio 1.878881 vs 1.886812 | z_lin +11381.841906 / z_ratio −0.981196 | PASS |
| G3 | robustness | |z| < 3 vs H(N2), Pareto | mean 9.730 vs 9.787606 | −1.285293 | PASS |

## Probe report (v0, self-adversarial)
**1. What is this really?** A logarithmic-cadence law for personal-best records. In an i.i.d. attempt log the k-th attempt beats all before it with probability 1/k, so lifetime PB records grow as H_N ≈ ln N + γ. A ×100 attempt count buys only ~1.887× the records; the linear "attempts → PBs" intuition over-predicts by two orders of magnitude.
**2. What would make it false?** If mean(count@N2) did NOT match H(N2) (G1 — the harmonic law is wrong), or if the observed count were NOT ≥3σ below the linear prediction and the ratio did NOT match H(N2)/H(N1) (G2 — the slowdown is not logarithmic), or if the Pareto base gave a DIFFERENT mean record count (G3 — the law is distribution-dependent). Any of G1/G2/G3 failing → REJECT.
**3. Simplest version that still bites?** SEED = 20260717; 100 → 10000 attempts (a ×100 grind) lifts the expected PB count only from 5.19 to 9.77 — under 2×. The 10000th attempt has a 1-in-10000 chance of being a PB.
**4. What is the counterintuitive core?** "PBs should keep coming if I keep grinding, and a drought means I've plateaued" is inverted. A stationary runner's records arrive at rate 1/k regardless of the value distribution, so the drought is arithmetic — the record count SQUARES its input to double its output.
**5. Where could I be fooling myself?** The z on G1/G3 is a TWO-SIDED anchor (small |z| = MC matches theory), so it cannot be inflated by large N into a false pass — a wrong mean would show up as |z| ≫ 3. G2's headline z_linear is huge because the effect is huge (the linear null is ~53× the true count), not statistical over-precision; the load-bearing test in G2 is the two-sided ratio anchor (z_ratio = −0.98). The delta-method ratio variance uses the disjoint-range identity Cov(C_{N1},C_{N2}) = Var(C_{N1}), sanity-checked against the sample covariance (3.562131 vs var 3.516277 — agree to Monte-Carlo error).
**6. Determinism?** SEED = 20260717 pinned; in-process double run asserted byte-identical before hashing; cross-invocation double run printed IDENTICAL stdout with sha256 fa31d284…489f26. All dict floats round()-ed to 6 dp; trial sums in fixed order; compact JSON with sort_keys; no set/dict-ordering nondeterminism.
**7. Real or toy?** The theory of records is a century-old, empirically load-bearing result (Rényi 1962; Glick 1978; Arnold-Balakrishnan-Nagaraja 1998) used to model athletic-record breaking and extreme events; the speedrun leaderboard is exactly a running-minimum process, so the harmonic law is the correct stationary baseline, not a toy.
**8. How will we know it worked?** The committed stdlib verifier reproduces, under SEED = 20260717, the harmonic-law anchor (G1), the logarithmic-slowdown headline plus ratio anchor (G2), and the Pareto distribution-free anchor (G3) at their SIGMA_GATE = 3.0 bars, with the results-dict sha256 matching fa31d28495ab63c8ff9f1c502031da475bfa334c918fb29173fab26e8e489f26 across a deterministic double-run.

## One-line design fix
Baseline personal-best cadence against the harmonic law H_N ≈ ln N + γ (records grow only logarithmically in the attempt count, distribution-free) — not against a linear "more attempts → proportionally more PBs" expectation — and flag genuine improvement as a runner whose record count runs ABOVE the stationary harmonic null.

**Recommendation: sim-ready**
