# Take the good bet and repeat, go broke: a repeated multiplicative wager with STRICTLY POSITIVE expected value (ensemble mean multiplier 1.05 per round, +5% EV) drives the TYPICAL investor almost surely toward ruin, because the TIME-AVERAGE (geometric) growth rate is NEGATIVE (√(1.5·0.6)=0.94868, −5.27%/round) — the ensemble's gains are carried by a vanishing fraction of ever-luckier paths while the median wealth collapses

> **State:** sim-ready
> **Class:** venture / markets / risk
> **Target:** sim-lab (VERDICT 203, +13 offset)
> **Grounding:** https://github.com/elemer1/elemer1.github.io/blob/def46918c26483bdd11580bc0851956536306c56/_markdown/The%20Barrier%20that%20Moved.md@def46918c26483bdd11580bc0851956536306c56 · fetched 2026-07-20T00:52:17Z
> **Reference (external, reachable):** Ergodicity economics — the multiplicative coin-toss result that a wager with positive expected value can have negative time-average growth, so the ensemble average and the time average diverge (broken ergodicity). https://en.wikipedia.org/wiki/Ergodicity_economics — verified live HTTP 200 this session ("over time, with probability one, wealth decreases by about 5% per round, in contrast to the increase by 5% per round of the expected value"). GitHub source file also verified live HTTP 200 this session: https://raw.githubusercontent.com/elemer1/elemer1.github.io/def46918c26483bdd11580bc0851956536306c56/_markdown/The%20Barrier%20that%20Moved.md
> **Harvest source (firsthand):** the Peters coin-flip / Kelly practice — heads +50% (×1.5) / tails −40% (×0.6), played repeatedly on one's own wealth; encoded in ideas/venture-lab/positive-ev-time-average-ruin.py + its recorded double-run (this branch).

## The phenomenon (one line)
Start with wealth 1.0 and repeatedly multiply it by 1.5 (prob 0.5) or 0.6 (prob 0.5): the per-round expected multiplier is 0.5·1.5+0.5·0.6 = 1.05 (a genuine +5% EV, and the ensemble mean wealth grows like 1.05^T), yet the per-round GEOMETRIC multiplier is √(1.5·0.6) = √0.9 = 0.94868 (< 1), so almost every individual trajectory decays at −5.27%/round and the typical (median) investor is driven toward ruin.

## The folk belief
"Positive expected value means it's a good bet — so take it, and if it's good once it's better repeated: compounding a positive-EV edge is how fortunes are built." The folk rule reads a positive ensemble/arithmetic average as a promise about the money in *your* account over time, and treats "repeat the +EV bet" as monotonically wealth-increasing.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
The trap is that the ensemble average and the time average are two DIFFERENT averages of a multiplicative process, and they answer two different questions. The ensemble (arithmetic) average E[m] = 1.05 answers "average the round multiplier across infinitely many parallel investors at a fixed time" — it is dominated by the additive contribution of a vanishingly small set of extremely lucky paths whose wealth is astronomically large, so E[W_T] = 1.05^T → ∞. The time average answers "what rate does ONE investor's wealth compound at as rounds accumulate for them" — and because wealth compounds multiplicatively, the relevant quantity is E[ln m] = 0.5·ln 1.5 + 0.5·ln 0.6 = −0.05268 < 0, i.e. the geometric mean √(1.5·0.6) = 0.94868 < 1. By the strong law of large numbers applied to the log-wealth (a sum of i.i.d. mean-negative increments), (1/T)·ln(W_T/W0) → E[ln m] < 0 almost surely, so W_T → 0 almost surely. The process is NON-ERGODIC: time average ≠ ensemble average, and the folk belief silently substitutes the ensemble average (a statement about a crowd) for the time average (a statement about you).

The load-bearing structural fact is that a single up-then-down round is not a wash: 1.5·0.6 = 0.9, a 10% loss per pair, even though the arithmetic mean of +50% and −40% is +5%. That gap between the arithmetic mean (+5%) and the geometric mean (−5.27%) is the volatility drag: for a log-normal-ish multiplicative process the drag is ≈ σ²/2 of the log-returns, and here the log-return variance is large enough (the ±50%/−40% swings) that the drag (≈ +10.1%) overwhelms the +5% arithmetic engine and bends the lived growth rate below zero. The correct decision-theoretic response is NOT "take the +EV bet full-size and repeat" but to size the bet so the TIME-AVERAGE growth rate is maximised (the Kelly prescription): betting a fraction of wealth rather than the whole stake can restore a positive geometric growth rate on the same +EV edge. The folk "take it and repeat at full size" is exactly the strategy the compounding dynamics punish.

## Pinned world (committed constants, SEED=20260717)
SEED = 20260717 · W0 = 1.0 · T = 100 rounds/path · P = 20000 paths · z_gate = 3.0 · ROUND_DP = 10 (fixed float serialization precision). Base world: up multiplier U = 1.5, down D = 0.6, each with probability 0.5 (ensemble expected multiplier 1.05, geometric 0.94868). Shifted robustness world: U = 1.6, D = 0.55 (ensemble expected multiplier 1.075 — still positive EV; geometric √0.88 = 0.93808 < 1 — still negative time-average). A fresh `random.Random(SEED)` is created at the start of EACH full run, so an in-process double-run and separate cross-invocation both reproduce byte-identical output. Digest posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY — the compact-canonical results dict's own sha256 IS the digest (not a field), printed to stdout.

## Gate criteria
Run `python3 ideas/venture-lab/positive-ev-time-average-ruin.py`; it must exit 0, print `all_pass=true`, and print `RESULTS_SHA256=<64hex>` byte-identical across two invocations. The four pre-registered gates (z_gate = 3.0):
- **G1 — time-average growth NEGATIVE (base):** z = −mean_time_avg_growth / SE(time_avg_growth across paths). Pass if mean_time_avg_growth < 0 AND z ≥ 3.
- **G2 — arithmetic EV POSITIVE (base):** z = mean_per_round_simple_return / SE(per_round_simple_return across all path-rounds). Pass if mean_per_round_simple_return > 0 AND z ≥ 3.
- **G3 — typical investor RUINED (base):** p̂ = frac_below_start; z = (p̂ − 0.5)/√(0.25/P). Pass if p̂ > 0.5 AND z ≥ 3.
- **G4 — ROBUSTNESS / SHIFT gate:** re-run the whole simulation with the SHIFTED world U = 1.6, D = 0.55 (EV = 1.075 > 1 still positive; geometric √0.88 = 0.93808 < 1 still negative). The paradox SIGN structure must persist: time-avg growth < 0 (z ≥ 3) AND per-round return > 0 (z ≥ 3) AND frac_below_start > 0.5 (z ≥ 3). Pass if all three signs hold at ≥ 3σ.
- all_pass = G1 AND G2 AND G3 AND G4.

## Measured results (this run)
Results-dict sha256 = `8d04b241d3589e2e49337c087da623d73c47dbe84074eaf5596bfa39db3c5336` (byte-identical across two separate invocations AND an in-process double-run). all_pass = **true**, first_failing_gate = null.

Base world (U=1.5, D=0.6):
- ensemble_expected_multiplier = 1.05 (positive EV confirmed); geometric_per_round_multiplier = 0.9486832981.
- mean_final_wealth = 55.6049183908 (ensemble grows — the +EV crowd looks rich) vs median_final_wealth = 0.0051537752 (the typical investor is near-ruined).
- mean_time_avg_growth = −0.0527741776 (negative, ≈ −5.27%/round).
- mean_per_round_simple_return = 0.0499077500 (positive, ≈ +5%/round).
- frac_below_start = 0.8623 · frac_ruined_10pct = 0.75635.
- **G1** z_time_avg_negative = 163.2077618449 (≥ 3 ✓, mean < 0 ✓).
- **G2** z_ev_positive = 156.8448905713 (≥ 3 ✓, mean > 0 ✓).
- **G3** z_frac_below_start = 102.4739147296 (≥ 3 ✓, p̂ = 0.8623 > 0.5 ✓).

Shifted world (U=1.6, D=0.55) — **G4**:
- ensemble_expected_multiplier = 1.075; geometric_per_round_multiplier = 0.938083152.
- mean_final_wealth = 296.2018051143 · median_final_wealth = 0.0016754582.
- mean_time_avg_growth = −0.0632973382 (z = 169.6825537139 ≥ 3 ✓).
- mean_per_round_simple_return = 0.075609 (z = 203.6710827592 ≥ 3 ✓).
- frac_below_start = 0.8627 (z = 102.5870518145 ≥ 3 ✓).
- **G4** all three signs hold at ≥ 3σ ✓.

## Caveats & crossovers (honest disclosure)
- **The bet is a well-known textbook object, not a novel discovery.** This is the Ole Peters / ergodicity-economics multiplicative coin toss (heads +50%, tails −40%), equivalently the Kelly / volatility-drag result. The head's contribution is the pinned, gate-verified reproduction and the venture/markets framing, not the mathematics, which is standard and disclosed.
- **Kelly-fractional sizing dissolves the "paradox".** The negative time-average is a property of betting the WHOLE stake every round. A rational investor sizing the bet as a fraction f of wealth can restore a positive geometric growth rate on the same +EV edge; the head is a claim about the naive "full-size, repeat" strategy the folk rule endorses, not a claim that the edge is unusable.
- **Mean vs sample-mean of final wealth.** The theoretical E[W_T] = 1.05^100 ≈ 131, but the measured sample mean_final_wealth is 55.60 because with only P=20000 paths the astronomically-lucky tail that carries the ensemble expectation is under-sampled — the sample mean is itself a high-variance, downward-biased estimator here. This is disclosed on purpose: it is the same non-ergodicity showing up as estimator instability, and it does NOT affect any gate (the gates test signs and ≥3σ, not the magnitude of the mean).
- **z-scores are enormous because the effect is structural, not marginal.** The ≥100σ values reflect a genuinely large, sign-definite effect (a −5.27% vs +5% gap) against a tiny standard error at P=20000, T=100 — not a knife-edge that a larger sample was needed to clear. A null (additive, non-compounding) world would put time-avg growth at exactly the arithmetic mean with no sign split.
- **Crossover with existing heads.** This is a time-average-vs-ensemble / volatility-drag result on a compounding wager, distinct from the venture-lab order-statistics/selection heads (term-sheet winner's curse, follow-on reserve starvation) which hold no multiplicative-compounding-of-one-agent's-wealth mechanism; and distinct from the survivorship-mirage retention head (which is a selection-on-survivors artefact, not a geometric-vs-arithmetic identity). No overlap detected in a venture-lab inventory scan.
- **Constants are illustrative but not tuned to a pass margin.** U/D are the canonical Peters values; the direction (geometric < 1 < arithmetic) holds for any two-outcome multiplicative bet with U·D < 1 < 0.5(U+D), a wide region, and the shift gate (U=1.6, D=0.55) confirms the signs are not an artefact of the specific pair.

## Probe report
**1. Is this just "geometric mean < arithmetic mean", i.e. a trivial AM-GM restatement?** The AM-GM inequality guarantees the geometric mean is ≤ the arithmetic mean, but the CONTENT here is that the gap straddles 1: the arithmetic mean of the multiplier is > 1 (a real +EV bet) while the geometric mean is < 1 (almost-sure ruin). AM-GM alone does not force that straddle — a lower-variance +EV bet keeps both above 1. The head is the straddle plus its consequence (median → 0 while mean → ∞), which G1∧G2∧G3 measure jointly, not the inequality.

**2. Are the ≥100σ z-scores just an artefact of a huge P·T sample?** No — the effect size is structural: mean_time_avg_growth = −0.0528 is ~5% per round away from zero, and a null non-compounding world would sit at +0.05 (the arithmetic mean) with the SAME sample size. The z is large because the sign is definite and the SE is small, not because a marginal effect needed a big N to reach significance; frac_below_start = 0.8623 (not ~0.5+ε) is a majority-ruin result, not a hair over the 0.5 threshold.

**3. Could the result be a coding artefact of how "ruin" or the median is computed?** The three ruin-adjacent statistics are independent constructions and mutually corroborate: median_final_wealth = 0.00515 (a rank statistic), frac_below_start = 0.8623 (a threshold count at W0), and frac_ruined_10pct = 0.75635 (a threshold count at 0.1·W0) all point the same way, while mean_final_wealth = 55.6 (an arithmetic sum) points the opposite way — exactly the ensemble/time split the head predicts, so no single metric carries the claim.

**4. Does the paradox survive a different world, or is it tuned to U=1.5/D=0.6?** G4 re-runs the entire simulation at U=1.6, D=0.55 (a higher +7.5% EV) and every sign persists at ≥3σ: time-avg −0.0633 (z=169.7), per-round +0.0756 (z=203.7), frac_below_start 0.8627 (z=102.6). The straddle (geometric 0.938 < 1 < arithmetic 1.075) is what carries it, and that region is wide, so the specific base pair is not load-bearing.

**5. Is "almost-sure ruin" honestly stated given the ensemble mean is huge and rising?** Yes, and both are true simultaneously — that is the whole point. E[W_T] = 1.05^T → ∞ (measured sample mean 55.6, an under-estimate of the true ≈131) AND W_T → 0 almost surely (measured median 0.00515, 86% of paths below start). The caveats section discloses that the sample mean under-samples the tail; neither statement is hidden or softened.

**6. Is determinism real and is the digest the whole dict?** SEED=20260717 is pinned with a fresh `random.Random(SEED)` at the top of every full run; compute() is called twice in-process and asserted canonical-identical before hashing; the compact-canonical (sort_keys, no-whitespace) results dict's own sha256 (8d04b241…c5336) is the digest, contains no self-field, and reproduced byte-identically across two separate invocations and the in-process double-run (all three confirmed this session).

**Recommendation: sim-ready**
