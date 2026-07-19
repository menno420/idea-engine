# The pay-to-play cramdown cliff: in a down round, the marginal pro-rata dollar is the highest-return dollar on the cap table

> **State:** sim-ready
> **Class:** venture / startup-economics — down-round mechanics, pay-to-play, liquidation preference
> **Target:** sim-lab (VERDICT 195, +13 offset)
> **Grounding:** https://www.fenwick.com/insights/publications/what-is-a-pay-to-play-financing@8552d3db117ccbbb2c4dd7014b987834666bb971 · fetched 2026-07-19T19:57:35Z
> **Reference (external, reachable):** https://www.fenwick.com/insights/publications/what-is-a-pay-to-play-financing — verified live HTTP 200 this session.
> **Harvest source (firsthand):** Fenwick, "What is a 'Pay-to-Play' Financing?": "All current preferred stock is converted to common stock at a 1:1 ratio."

## The phenomenon (one line)

Under a pay-to-play provision, an existing preferred investor who declines to write its (small) pro-rata check in a down round has its preferred **converted to common** — the liquidation preference is wiped — so conditional on a modest exit the pro-rata dollar preserves several times its own value, and the conversion penalty, not the dilution, is what does it.

## The folk belief

"Pay-to-play just dilutes investors who don't follow their money — it's a dilution stick," and "your liquidation preference is a safe downside floor regardless." The intuition treats non-participation as a linear dilution cost and the preference as a floor that survives.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

A pay-to-play (or "pull-up" / "cram-down") provision makes participating in the down round a *condition* for keeping preferred status. Miss the pro-rata and the shares convert to common. Two things happen at once, and they are not the same size:

1. **Dilution.** You skip the round, so your fully-diluted ownership falls (here 25% → 12.5%). Linear and modest.
2. **Conversion.** Your preferred becomes common: the liquidation preference is erased and you drop *behind* every remaining preference in the waterfall.

The counterintuitive part is that (2) dominates (1) exactly in the outcomes where a preference is supposed to matter — modest and down-market exits, where the company sells near or below the aggregate preference stack. There, a still-preferred holder recovers its capital off the top; a crammed-down (now common) holder recovers little or nothing because the participating investors' preference sits senior. So the marginal pro-rata dollar is not buying ownership — it is buying back a *senior claim* the provision would otherwise destroy. That makes it the highest-return dollar on the cap table in the danger band, and it is worth the most in cold markets, where exits cluster near the preference stack. The provision thereby manufactures rational over-participation in weak companies: even a skeptical investor writes the check, because the alternative is a discontinuous wipeout.

## Pinned world (committed constants, SEED=20260717)

- Existing investor A: prior $4M at a 1× non-participating preference; 25% fully-diluted ownership entering the down round.
- Down round: $5M new money at $5M pre-money (post $10M); new investors take 50%.
- A's pro-rata of the new round: $1.25M (the marginal check under test).
- Waterfall convention: a single pari-passu tranche of 1× non-participating preferred; each preferred holder takes the greater of its pref-share or its as-converted value; common splits the residual; senior preferred convert above the exit where converting beats their preference ($10M here).
- Three A-payoffs per exit V: **participate** (holds 25%, $5.25M pref), **keep / no-pay-to-play counterfactual** (skips pro-rata, keeps the prior $4M pref, diluted to 12.5%), **crammed** (converted to common at 12.5%, no preference, junior to the $5M senior stack).
- Exit V ~ lognormal. Base market: median $18M, σ=0.95. Cold market (robustness): median $11M, σ=1.20 (common random numbers shared with base). Danger band: V ≤ $15M. TRIALS = 200,000.

## Gate criteria

- **G1 — the marginal dollar (in-band).** Conditional on a danger-band exit, the expected value A preserves by participating per dollar of pro-rata check `(A_participate − A_crammed)/1.25` is ≥ **2.0** at ≥ **3σ**.
- **G2 — conversion, not dilution, is the driver (in-band).** Conditional on a danger-band exit, the value from avoiding the conversion `(A_keep − A_crammed)` is ≥ **1.5×** the value from avoiding the dilution `(A_participate − A_keep)`, at ≥ **3σ** (per-trial premium `conv − 1.5·dil`, mean > 0).
- **G3 — cold-market amplification.** The danger-band probability is strictly higher under the cold market than the base at ≥ **3σ** (two-proportion z), and the in-band conversion-dominance (ratio ≥ 1.5) still holds under the cold market.

`all_pass = G1 ∧ G2 ∧ G3`

Digest posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY (P127+ twist) — the compact-canonical results dict's own sha256 IS the digest; the stdout dump is the pretty (indent=2, sort_keys) render; nothing is written to disk.

## Measured results (this run)

```
{
  "all_pass": true,
  "base_median_exit": 18.0,
  "cold_median_exit": 11.0,
  "danger_band": 15.0,
  "gate_G1_pass": true,
  "gate_G1_ratio_gate": 2.0,
  "gate_G1_ret_band_mean": 2.674407,
  "gate_G1_ret_band_z": 308.093567,
  "gate_G2_conv_gate": 1.5,
  "gate_G2_conv_mean": 2.348806,
  "gate_G2_conv_over_dil": 2.362501,
  "gate_G2_dil_mean": 0.994203,
  "gate_G2_pass": true,
  "gate_G2_z": 848.320658,
  "gate_G3_band_prob_z": 112.415006,
  "gate_G3_base_band_prob": 0.42401,
  "gate_G3_cold_band_prob": 0.601695,
  "gate_G3_cold_conv_over_dil": 2.516596,
  "gate_G3_pass": true,
  "head": "pay-to-play cramdown cliff: conditional on a modest exit the marginal pro-rata dollar is the highest-return dollar, driven by the preferred->common conversion (not dilution), and it sharpens in cold markets",
  "pro_rata_check": 1.25,
  "proposal": 182,
  "seed": 20260717,
  "trials": 200000
}
Results-JSON sha256 ed8a081bb104683d1ee8c0c2ec9b90e2a1212100495d9d44b5e484016a75b243
```

## Caveats & crossovers (honest disclosure)

- **Conditioning is the head, not a cherry-pick.** The cliff is a *modest-exit* phenomenon; in a home-run exit ownership dilution dominates and the preference is irrelevant, so G1/G2 are explicitly conditioned on the danger band. That conditioning is the claim, disclosed, not hidden.
- **Conservative conversion.** A 1:1 conversion to common is modeled; real pay-to-play "pull-up" provisions often convert on punitive terms, which would only deepen the cliff. The head holds under the mildest conversion.
- **Waterfall simplification.** A single pari-passu 1× non-participating tranche with the standard per-security "greater-of" rule and residual-to-common; a stacked multi-series stack or participating preferred would change magnitudes but not the sign.
- **Crossovers.** Shares the "preference in a modest exit" surface with `founder-dilution-waterfall` and `full-ratchet-convexity`, but the mechanism here is the *pay-to-play conversion* of a non-participant — a distinct provision none of those heads model. Distinct from `post-money-safe-stacking` and the retention/LTV cluster.
- **Distributional load.** G3's amplification is driven by the median shift (more mass below the pref stack); the σ change is disclosed and the two-proportion test isolates band membership.

## Probe report (v0, self-adversarial)

**1. Does the danger-band conditioning honestly scope the head, or does it cherry-pick the region where the effect exists?**
The head *is* that preferences matter in modest exits; the conditioning is disclosed and is the claim, not a hidden filter. Unconditionally, the fat upper tail lets ordinary dilution dominate — which the doc states.

**2. Is the single-pari-passu-tranche waterfall a fair simplification, or does it bias the cliff?**
It is the standard per-security greater-of rule with residual-to-common; a real stacked stack would deepen the senior overhang, so the simplification is conservative on the cliff, not inflationary.

**3. Is the 1:1 conversion assumption conservative, and would a punitive pull-up only strengthen the head?**
Yes — modeling a mild 1:1 conversion understates real pull-up haircuts; a punitive conversion lowers `A_crammed`, raising every gate margin.

**4. Does G2 genuinely isolate the conversion penalty from ordinary dilution?**
The keep / no-pay-to-play counterfactual holds ownership fixed at 12.5% and differs from the crammed case only by keeping the preference, so `conv = A_keep − A_crammed` is the pure conversion term and `dil = A_participate − A_keep` the pure dilution term.

**5. Is the cold-market amplification an artifact of the σ change rather than the median shift?**
The two-proportion z tests danger-band membership, which the median shift drives; the doc discloses the σ change and G3 also confirms the conversion-dominance persists under cold.

**6. Would a participating preferred or a stacked multi-tranche stack flip the head?**
Participating preferred raises both participate and crammed payoffs, but the crammed holder still loses seniority; a deeper stack raises the senior overhang, deepening the cliff. Neither flips the sign.

**7. Is the lognormal doing load-bearing work, or does the cliff survive a different exit family?**
The cliff is a waterfall property (senior pref vs common in modest exits), not a distributional one; lognormal only sets how much mass lands in the band. A verdict session may re-run under a different family to confirm.

**8. Does the results-dict digest reproduce bit-identically across a fresh interpreter invocation?**
Yes — a local `random.Random(SEED)`, common random numbers, no wall-clock or external input; the in-process double-run asserts identical dicts and the CLI is deterministic across invocations.

**Recommendation: sim-ready**
