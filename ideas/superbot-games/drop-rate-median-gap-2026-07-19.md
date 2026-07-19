# PROPOSAL 159 — drop-rate median gap: the "expected N kills" loot anchor is the ~63rd percentile and the typical grind is ~69% of it

> **State:** sim-ready
> **Class:** superbot-games · loot / drop-rate economics · geometric distribution (mean–median–percentile skew)
> **Slot:** round-37 GAME
> **Anchor:** the geometric/exponential mean-vs-median skew — for T ~ Geometric(p), mean = 1/p but median = ⌈ln2 / −ln(1−p)⌉ ≈ 0.693/p and mode = 1; the CDF at the mean → 1 − 1/e ≈ 0.632. Feller, *An Introduction to Probability Theory and Its Applications*, Vol. 1 (1968).
> **Target:** sim-lab (VERDICT 172, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine/blob/b8a631d29dad72d2238134bca882067b4feb1701/ideas/superbot-games/drop_rate_median_gap.py@fe602dda5c0f0924c386423b7d7ca451fc965370 · fetched 2026-07-19T06:30:31Z
> **Reference (external, reachable):** Wikipedia "Geometric distribution" https://en.wikipedia.org/wiki/Geometric_distribution — mean 1/p, median ⌈−1/log2(1−p)⌉; Wikipedia "Exponential distribution" https://en.wikipedia.org/wiki/Exponential_distribution — CDF at the mean = 1 − 1/e ≈ 0.632.
> **Verifier (firsthand):** `ideas/superbot-games/drop_rate_median_gap.py` · results-dict sha256 `ff22cf37b81fb96bb36a1aeb1a4484479d31e1232b637efb0faf297bb852fb19`
> 📊 Model: Claude Opus · high · idea/planning

## The phenomenon (one line)
For an i.i.d. loot roll at per-attempt drop probability p, the attempts-until-first-drop T is Geometric(p): mean 1/p, but median ≈ 0.693/p and mode 1 — so the "expected N tries" players anchor on is the ~63rd percentile, not the typical grind.

## The folk belief
"The drop is 1%, so it's about 100 kills on average; if I've done 100 with nothing, I'm exactly average and due for it." Both halves are wrong: 100 is not the typical grind (the median is ~69), and nothing is "due" — the rolls are memoryless.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Attempts-until-first-success with a constant per-roll probability p is Geometric(p), a heavily right-skewed law. Its mean 1/p is not its centre of mass in the sense players imagine: the **median** is ⌈ln2 / −ln(1−p)⌉ ≈ 0.693/p, so the typical player finishes in about **69% of the advertised mean**. Because the distribution is skewed right, the mean sits well above the median — at the mean itself a solid **majority** have already succeeded: P(T ≤ 1/p) = 1 − (1−p)^⌊1/p⌋ → **1 − 1/e ≈ 0.632** as p → 0, i.e. the "expected N kills" is really the ~63rd percentile. What drags the mean up is a fixed heavy tail: P(T > 3/p) → **e⁻³ ≈ 0.0498**, so about 5% of players grind past *triple* the expected count regardless of how the rate is tuned — and it is those unlucky tails, not the median player, who dominate the forums. Crucially all three landmarks — median/mean = ln2, mean-percentile = 1 − 1/e, tail = e⁻ᵏ — are **scale-free in p**: halving the drop rate doubles every count but leaves every ratio identical. (Crossover, not the head: the same law is *memoryless* — k prior misses never raise the next roll above p, so "due" is a fallacy; and PRD ramps / pity counters deliberately break the constant-p assumption to compress this very skew. Both disclosed below, neither is this claim.)

## The formal model (committed constants — sim-lab must reproduce exactly)
T ~ Geometric(p) on {1,2,…}, P(T=k) = (1−p)^(k−1)·p.
- true_mean(p)    = 1/p
- exact_median(p) = ⌈ ln2 / −ln(1−p) ⌉   (integer)
- P(T ≤ m)        = 1 − (1−p)^m           with m = ⌊1/p⌋
- Limits as p → 0: median/mean → ln2 = 0.6931…, P(T ≤ mean) → 1 − 1/e = 0.6321…, P(T > 3/p) → e⁻³ = 0.0498…

Draws use the inverse-CDF map k = ⌈ ln U / ln(1−p) ⌉ for U ~ Uniform(0,1).

## Pinned world (committed constants)
SEED=20260717 · P_MAIN=0.01 · P_SHIFT=0.005 · TRIALS=200000 · R=30 replications · SIGMA_GATE=3.0 · CEILING=0.05 (relative-error). Main measure draws from `random.Random(SEED)`; the shifted-rate measure draws from `random.Random(SEED+1)`. Per replication the verifier records median/mean, the right-skew gap (mean−median)/mean, and the fraction of draws ≤ the true mean 1/p; z-scores are on the /se margin across the R replications.

## Pre-registered gates (APPROVE iff ALL hold, in order G1 → G2 → G3)
- **G1 median-below-mean** — the right-skew gap (mean−median)/mean exceeds the symmetric null 0 at ≥3σ, and the measured median/mean ratio matches the exact closed form within the 0.05 relative-error ceiling. Measured: gap 0.305865, z_skew **+369.741566**; ratio 0.694135 vs exact 0.69, relerr 0.005993. PASS. Head: the typical grind is ~69% of the advertised mean.
- **G2 mean-is-majority-percentile** — the fraction of grinds finishing by the true mean 1/p exceeds the 0.5 null at ≥3σ, and matches the exact P(T ≤ ⌊1/p⌋) within the ceiling. Measured: frac 0.634140, z_majority **+761.720583**; exact 0.633968, relerr 0.000272 (asymptote 1 − 1/e = 0.632121). PASS. Head: the "expected" count is already the ~63rd percentile.
- **G3 scale-free robustness** — under the rarer shifted rate p′=0.005 both landmarks still hold at ≥3σ. Measured: gap z_skew **+802.499080**, majority z **+706.081134**; ratio 0.693966 (relerr 0.001487), frac 0.632729 vs exact 0.633042 (relerr 0.000494). PASS. Head: the skew is a property of the geometric law, not of one tuned rate.

## Pre-registered decision rule
APPROVE iff sim-lab reproduces `ideas/superbot-games/drop_rate_median_gap.py` byte-for-byte under SEED=20260717, the results-dict sha256 equals `ff22cf37b81fb96bb36a1aeb1a4484479d31e1232b637efb0faf297bb852fb19` exactly, and all three gates PASS in order (all_pass=true, first_failing_gate=null, exit 0). Any digest mismatch, gate failure, or non-deterministic double-run ⇒ REJECT (or QUALIFY on a disclosed environment difference).

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```json
{
  "all_pass": true,
  "ceiling": 0.05,
  "first_failing_gate": null,
  "g1_median_below_mean": {
    "pass": true,
    "relerr_ratio": 0.005993,
    "z_skew": 369.741566
  },
  "g2_mean_majority_percentile": {
    "pass": true,
    "relerr_frac": 0.000272,
    "z_majority": 761.720583
  },
  "g3_scale_free_robustness": {
    "pass": true,
    "relerr_frac": 0.000494,
    "relerr_ratio": 0.001487,
    "z_majority": 706.081134,
    "z_skew": 802.49908
  },
  "gates": [
    {
      "id": "G1",
      "name": "median_below_mean",
      "pass": true,
      "z": 369.741566
    },
    {
      "id": "G2",
      "name": "mean_is_majority_percentile",
      "pass": true,
      "z": 761.720583
    },
    {
      "id": "G3",
      "name": "scale_free_robustness",
      "pass": true,
      "z": 706.081134
    }
  ],
  "limits": {
    "median_over_mean_ln2": 0.693147,
    "p_le_mean_1_minus_inv_e": 0.632121,
    "tail_3_over_p_inv_e3": 0.049787
  },
  "main": {
    "exact_median": 69,
    "exact_median_over_mean": 0.69,
    "exact_p_le_mean": 0.633968,
    "frac_le_mean_mc": 0.63414,
    "frac_le_mean_se": 0.000176,
    "gap_mc": 0.305865,
    "gap_se": 0.000827,
    "p": 0.01,
    "ratio_med_mean_mc": 0.694135,
    "ratio_med_mean_se": 0.000827,
    "true_mean": 100.0
  },
  "params": {
    "p_main": 0.01,
    "p_shift": 0.005,
    "replications": 30,
    "trials": 200000
  },
  "proposal": 159,
  "seed": 20260717,
  "shift": {
    "exact_median": 139,
    "exact_median_over_mean": 0.695,
    "exact_p_le_mean": 0.633042,
    "frac_le_mean_mc": 0.632729,
    "frac_le_mean_se": 0.000188,
    "gap_mc": 0.306034,
    "gap_se": 0.000381,
    "p": 0.005,
    "ratio_med_mean_mc": 0.693966,
    "ratio_med_mean_se": 0.000381,
    "true_mean": 200.0
  },
  "sigma_gate": 3.0,
  "slot": "round-37 GAME"
}
Results-JSON sha256: ff22cf37b81fb96bb36a1aeb1a4484479d31e1232b637efb0faf297bb852fb19
```

## Verifier
`ideas/superbot-games/drop_rate_median_gap.py` — stdlib-only (`math`, `json`, `hashlib`, `random`). Draws R=30 replications × 200000 Geometric(p) samples at p=0.01 and p=0.005, measures the median/mean ratio, the right-skew gap, and the mean-percentile, and gates each against its exact closed form and null at ≥3σ. WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest posture: the results dict carries no digest field; `main()` runs `run()` twice, asserts the two compact-canonical (sorted-keys, 6-dp-rounded) digests are identical, prints the indent=2 dump, then the `Results-JSON sha256:` line. No JSON is written to disk.

## Reproduce
```
python3 ideas/superbot-games/drop_rate_median_gap.py
```
Expected tail:
```
  "all_pass": true,
  ...
Results-JSON sha256: ff22cf37b81fb96bb36a1aeb1a4484479d31e1232b637efb0faf297bb852fb19
```
Exit 0; a second invocation is byte-identical.

## Why it matters (game design + player analytics)
Drop rates are almost always communicated as a rate ("1%") or an implied mean ("~100 kills"). Players then read the mean as the typical experience and feel cheated at the 60th–90th percentile of an ordinary distribution — the complaint volume is manufactured by publishing the wrong summary statistic. The honest number to publish is the **median** (0.693/p, the coin-flip grind) and the **unlucky-tail count** (3/p, where ~5% still sit) — or to change the distribution itself. PRD ramps and pity counters exist precisely because designers learned this skew is a retention hazard: they trade a lower jackpot ceiling for a tighter grind whose median and mean sit close together. The mechanism also inoculates against the "due" fallacy in balance discussions: memorylessness means a bad-luck streak carries no stored credit, so bad-luck protection has to be engineered, not waited for.

## Dedup (contrast vs prior lane heads)
- **prd-proc-compression** and **pity-anticipation-collapse** are the *engineered cures* — a Warcraft-III-style ramping probability, or a hard pity cap, deliberately break the constant-p assumption to compress exactly this median/mean gap and clip the e⁻³ tail. This proposal is the untreated **plain-geometric disease** they cure; it makes no claim about ramped or capped systems.
- **coupon-collector-tail** (fleet) is the *sum* of many geometrics (collecting all N items, ~N·ln N); this is a *single* geometric's internal skew.
- **speedrun-record-drought** (P155) is the harmonic record law (a different distribution and statistic — record counts, not first-success time).
- **shop-reroll-ruin** is a gambler's-ruin bankroll process; this is a single-item first-hit distribution. No prior head states the median/mean/percentile skew of one geometric grind.

## Model basis (declared model-dependence — the P024 discipline)
The head is an exact property of the geometric/exponential law and holds for *any* constant-p i.i.d. roll — the SIGN (median < mean, mean-percentile > 0.5) and the scale-free ratios are not modelling choices. Declared model-dependence: (1) the finite-rate correction — at p=0.01 the exact mean-percentile is 0.633968, not the p→0 limit 0.632121; G2 gates the MC against the **exact finite-p** closed form and reports the limit only as the asymptote. (2) The MC sample median of a discrete law sits a hair above the integer exact_median (ties), which is why the measured ratio 0.6941 exceeds 69/100 — still inside the 0.05 ceiling. (3) Constant-p only: PRD, pity, bad-luck-protection, and diminishing/increasing drop rates break the geometric assumption and are out of scope (named as the cures, not tested here).

## Probe report (v0, self-adversarial)
**1.** Is the median really below the mean, or MC noise? — Exact: mean 1/p=100, median ⌈ln2/−ln0.99⌉=69. G1 measures gap (mean−median)/mean=0.3059 at z=+369.7 vs null 0; not noise.
**2.** Is "63rd percentile" cherry-picked at p=0.01? — No; it is the p→0 limit 1−1/e and is gated against the exact finite-p value 0.633968 (relerr 0.000272), and re-confirmed at p=0.005 (0.632729). Scale-free.
**3.** Could a different draw method change the result? — The inverse-CDF map is the standard geometric sampler; the claim is distributional, not sampler-specific. Determinism is asserted across a double-run (identical digests).
**4.** Is this just the exponential-distribution fact dressed up? — It is the discrete geometric, which limits to the exponential; the exponential's CDF-at-the-mean = 1−1/e is the continuous shadow of G2. Disclosed as the anchor, not hidden.
**5.** Does the tail claim (e⁻³) get gated? — Not gated (kept to two head gates + one robustness gate for a clean ≥3σ story); it is stated as a limit and is directly checkable from the same draws. Named as a caveat, not a verified gate.
**6.** Memorylessness / "due" — is that the claim? — No; it is disclosed as a crossover. The verified head is the median/mean/percentile skew.
**7.** Overlap with the PRD/pity heads? — Explicit dedup: those are the cures that break constant-p; this is the untreated law. No shared gate or number.
**8.** What would falsify it? — A reproduction where median ≥ mean, or the mean-percentile ≤ 0.5, or the ratios drift with p beyond the ceiling. None occur; all three gates pass at ≥3σ across two rates.

## One-line design fix
Publish the median grind (~0.693/p) and the unlucky-tail count (~3/p, where ~5% still sit) alongside the drop rate — or ramp p (PRD) / add a pity cap to pull the median and mean together.

**Recommendation: sim-ready**
