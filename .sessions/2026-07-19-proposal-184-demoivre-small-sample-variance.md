# PROPOSAL 184 — de Moivre's small-sample variance artifact (round-43 UNRELATED)

> **Status:** `in-progress`
> **Slot:** round-43 UNRELATED (rotation fleet→venture→game→unrelated)
> **Target:** sim-lab VERDICT 197 (+13 offset)
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card lands first as `in-progress` to hold substrate-gate red; the final commit flips it to `complete` after the content, verifier double-run, and outbox append are in place.

## Objective
Author round-43 UNRELATED PROPOSAL 184: **de Moivre's equation — "the most dangerous equation"** (Wainer 2007). When many units share ONE true rate but differ in sample size n, ranking by the *observed* rate surfaces the small-n units at BOTH extremes of the leaderboard, because SD(observed) = sqrt(p(1-p)/n) inflates as n shrinks. The top and bottom of the ranking are a sample-size illusion, not a quality signal. Stdlib-only deterministic verifier (SEED=20260717), ordered ≥3σ gates plus a shifted-distribution robustness gate, for future VERDICT 197 (+13).

## Gate plan (pre-registered; APPROVE iff G1∧G2∧G3 in order, z_gate=3.0)
- **G1** — extremes are small-n dominated: among the top+bottom EXT=10% of units ranked by observed rate, the fraction that are small-n units exceeds the 0.5 population share at ≥3σ.
- **G2** — the spread is a de Moivre artifact: the ratio of observed-rate variance in the small-n class to the large-n class exceeds 1 at ≥3σ and matches the predicted n_large/n_small within tolerance.
- **G3** — robust under a shifted distribution: the small-n-dominates-extremes effect persists at ≥3σ both under a skewed rate (p=0.1) and under continuous sample sizes n~U{n_small..n_large} split at the median.

## Outcome
_(filled at flip)_ Verifier proven twice byte-identical, all_pass=true, first_failing_gate=null; results-dict sha256 recorded; outbox PROPOSAL 184 appended (sim-ready), proposal high-water P183→P184, targeting VERDICT 197.
