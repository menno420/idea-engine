# PROPOSAL 184 — de Moivre's small-sample variance artifact (round-43 UNRELATED)

> **Status:** `complete`
> **Slot:** round-43 UNRELATED (rotation fleet→venture→game→unrelated)
> **Target:** sim-lab VERDICT 197 (+13 offset)
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD cleared: this card landed first as `in-progress`; this final commit flips it to `complete` after the verifier double-run, proposal doc, and outbox append are in place.

## Objective
Round-43 UNRELATED PROPOSAL 184: **de Moivre's √n law — the standard error of a proportion is √(p(1−p)/n)**, popularly "the most dangerous equation" (Wainer 2007). When many units share ONE true rate but differ in sample size n, ranking by the *observed* rate surfaces the small-n units at BOTH extremes of the leaderboard, because SD(observed) inflates as n shrinks. The top and bottom of the ranking are a sample-size illusion, not a quality signal. Stdlib-only deterministic verifier (SEED=20260717), ordered ≥3σ gates plus shifted-distribution robustness, for future VERDICT 197 (+13).

## Gate plan (pre-registered; APPROVE iff G1∧G2∧G3 in order, z_gate=3.0) — matches the shipped verifier
- **G1 — the √n scaling law holds:** across M=800 units, Pearson corr(|r̂−p|, 1/√n) > 0 at ≥3σ. Observed mean r = 0.570449, z = 238.774053.
- **G2 — the ranking extremes are small-n:** top+bottom EXT=10% by observed rate have a smaller mean sample size than the population; pop_mean_n − extreme_mean_n > 0 at ≥3σ. Observed delta = 147.021788, z = 213.047828.
- **G3 — robust under shifted rate and size range:** under skewed p=0.1 the G1 correlation stays > 0 at ≥3σ (r = 0.570124, z = 219.519762) and under range [25,250] the G2 delta stays > 0 at ≥3σ (delta = 38.443275, z = 129.55551).

## Outcome
Complete. Verifier `ideas/fleet/demoivre_small_sample_variance.py` proven twice byte-identical, all_pass=true, first_failing_gate=null; results-dict sha256 `8b9506d1182b6c5f3121ff8b585dfb7032d47a337013e30d4f7fbfc1e0968871`. Grounding confirmed live: Wikipedia "Standard error" oldid 1362665393 (SE = σ/√n; the de Moivre attribution and Wainer's small-schools / kidney-cancer illustrations are cited but were not independently fetchable in-env). Outbox PROPOSAL 184 appended (sim-ready), proposal high-water P183→P184, targeting VERDICT 197. Previous-session frontier reviewed: PROPOSAL 183 (kingmaker skill-inversion, round-43 GAME) shipped and V195 mirrored P182. Loop idea: an empirical-Bayes shrinkage leaderboard companion quantifying how much a min-n gate reorders a fleet ranking.
