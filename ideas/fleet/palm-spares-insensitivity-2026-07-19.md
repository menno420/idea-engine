# An M/G/∞ repair pipeline holds a Poisson number of units — λ·E[S], insensitive to repair-time variance: spares depend on the mean, not the spread

> **State:** sim-ready
> **Class:** counterintuitive-invariant / fleet-ops (spares + maintenance pipeline)
> **Slot:** round-38 fleet
> **Anchor:** cutting repair-time variability at a fixed mean buys zero reduction in spares — the units-in-repair count is Poisson(λ·E[S]), fixed by the mean repair time and the failure rate alone, for any repair-time distribution.
> **Target:** sim-lab (VERDICT 174, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine/blob/56fe7d210f9d2df03dbebbb3803c2b146350a4f2/ideas/fleet/palm_spares_insensitivity.py@da7466ec6c75c22993344dc1caf983babee2cccf · fetched 2026-07-19T07:58:32Z
> **Reference (external, reachable):** the M/G/∞ (infinite-server) queue / Palm's theorem — the stationary number in system is Poisson with mean λ·E[S], independent of the service-time distribution beyond its mean. Wikipedia "M/M/∞ queue" https://en.wikipedia.org/wiki/M/M/infinity_queue (states "The stationary distribution of the M/G/∞ queue is the same as that of the M/M/∞ queue"); foundational to C. C. Sherbrooke, "METRIC: A Multi-Echelon Technique for Recoverable Item Control," Operations Research 16(1):122-141 (1968).
> **Verifier (firsthand):** `ideas/fleet/palm_spares_insensitivity.py` · results-dict sha256 `9bbe2171bd7678fc7efa03c550f0afbcec438498b0553a1723ee078bf5ec13ef`
> 📊 Model: Claude Opus · high · idea/planning

## The phenomenon (one line)
In an M/G/∞ repair pipeline — Poisson unit-failure arrivals at rate λ, each failed unit independently in repair for an i.i.d. time S — the stationary number of units in repair N is Poisson with mean λ·E[S] for ANY repair-time distribution, so its dispersion is fixed by the mean repair time alone; halving the variability of repair while holding E[S] fixed does not move the pipeline, and does not reduce the spares you must hold.

## The folk belief
"Erratic, high-variance repair times force you to carry more spares — smooth the repair process and you can stock fewer." For a WAITING line (finite repair bays, M/G/1) that reflex is right: the Pollaczek-Khinchine wait scales with (1+CV²)/2, so variance taxes you. But for the ample-server REPAIR PIPELINE the reflex is simply false — the number in repair is Poisson(λ·E[S]) regardless of shape, so a deterministic, an exponential, and a heavy-tailed lognormal repair time of equal mean all demand the same spares.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
The pipeline count is not a queueing-delay quantity — nothing waits, every failed unit enters repair immediately (ample servers). So the relevant object is the number of "in-flight" repairs at a random instant. Model failures as a Poisson process of rate λ; mark each arrival u with its i.i.d. repair duration S_u. A unit is in repair at time t iff it arrived in the window (t−S_u, t], i.e. iff u ≤ t < u+S_u. By the **marking / displacement theorem for Poisson processes**, the set {(u, S_u)} is a Poisson process on the plane with intensity λ·du × dF(s), and the count of its points falling in the region {u ≤ t < u+s} is itself **Poisson**, with mean λ·∫₀^∞ P(S > x) dx = λ·E[S]. Two consequences drop out and neither carries a distribution-shape term: (1) the mean pipeline is E[N] = λ·E[S] — Little's law for the M/G/∞ system, W = E[S], L = λW; (2) because N is Poisson, its **index of dispersion Var(N)/E[N] = 1 exactly**, for every repair law with a finite mean — deterministic (CV=0), exponential (CV=1), or lognormal (CV=3) alike. The variance of repair time cancels out of the count entirely. This is Palm's theorem (1938) and the invariance at the heart of Sherbrooke's METRIC spares model: the recoverable-item pipeline is Poisson(demand-rate × mean-resupply-time), so you provision against the mean, not the spread. (Crossover, not the head: for a WAITING line with finite servers (M/G/1, M/G/c) repair-time variance DOES inflate wait via Pollaczek-Khinchine (1+CV²)/2; and if the mean repair time E[S] or the failure rate λ moves, the pipeline moves proportionally. Both disclosed below; neither is this claim.)

## The formal model (committed constants — sim-lab must reproduce exactly)
Failures arrive as a Poisson process of rate λ (exponential interarrivals, mean 1/λ). Each failed unit is in repair for an i.i.d. time S drawn from a repair law of mean E[S]; the number in repair N(t) is sampled at integer instants after a warm-up.
- pipeline mean:            E[N] = λ·E[S]  (Little's law for M/G/∞)
- pipeline distribution:    N ~ **Poisson(λ·E[S])** for any repair law ⇒ index of dispersion Var(N)/E[N] = 1
- repair laws (all mean E[S] = 10): deterministic S=10 (CV=0); exponential rate 1/10 (CV=1); lognormal μ,σ with σ² = ln(1+CV²), μ = ln(10) − σ²/2 (CV=3)
- M/G/1 contrast (readout, not gated): the same CV=3 would impose a wait multiplier (1+CV²)/2 = 5× on a single-server WAITING line

## Pinned world (committed constants)
SEED=20260717 · Z_GATE=3.0 · R=30 replications · LAM=1.0 · MEAN_S=10.0 (⇒ LOAD = λ·E[S] = 10.0) · HORIZON=60000 integer instants · WARMUP=8000 discarded · CV_HI=3.0 (the high-variance lognormal) · relerr ceiling CEIL=0.05. A single `random.Random(SEED + rep*101 + k)` stream per (replication, repair-law) feeds each run in fixed order; N is accumulated by a difference-array prefix sum over integer instants and summarized post-warmup as (mean, variance, dispersion). `run()` is executed twice in-process and the two results dicts are asserted identical.

## Pre-registered gates (APPROVE iff ALL hold, in order G1 → G2 → G3)
- **G1 pipeline-is-load** — the exponential-repair pipeline mean E[N] matches the offered load λ·E[S] within the 0.05 relative-error ceiling at ≥3σ. Measured: load_relerr_mean 0.004443, z **+68.279173** (ceiling 0.05). PASS. Head: the pipeline fills to Little's-law load, E[N] ≈ 10.0.
- **G2 variance-insensitivity** — under a HIGH-variance lognormal repair law (CV=3), the pipeline's index of dispersion Var(N)/E[N] stays at the Poisson value 1.0 within the 0.05 ceiling at ≥3σ. Measured: disp_relerr_mean 0.021783, z **+12.870661** (ceiling 0.05). PASS. Head: repair variability does NOT inflate the pipeline — a CV=3 repair time yields a dispersion-1 Poisson count, while the same CV would impose a 5× wait tax on a WAITING line (readout mg1_wait_tax_multiplier = 5.0, not gated).
- **G3 distribution-free** — across three repair laws of IDENTICAL mean (deterministic CV=0, exponential CV=1, lognormal CV=3) the pipeline mean AND dispersion index agree within the 0.05 ceiling at ≥3σ. Measured: spread_mean 0.031331, z **+10.750843** (ceiling 0.05). PASS. Head: the same Poisson(10) pipeline serves all three — the spares requirement is a property of the mean, not the shape.

## Pre-registered decision rule
APPROVE iff sim-lab reproduces `ideas/fleet/palm_spares_insensitivity.py` byte-for-byte under SEED=20260717, the results-dict sha256 equals `9bbe2171bd7678fc7efa03c550f0afbcec438498b0553a1723ee078bf5ec13ef` exactly, and all three gates PASS in order (all_pass=true, first_failing_gate=null, exit 0). Any digest mismatch, gate failure, or non-deterministic double-run ⇒ REJECT (or QUALIFY on a disclosed environment difference).

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```json
{
  "all_pass": true,
  "first_failing_gate": null,
  "g1_pipeline_is_load": {
    "ceiling": 0.05,
    "load_relerr_mean": 0.004443,
    "pass": true,
    "se": 0.000667,
    "z": 68.279173
  },
  "g2_variance_insensitive": {
    "ceiling": 0.05,
    "disp_relerr_mean": 0.021783,
    "pass": true,
    "se": 0.002192,
    "z": 12.870661
  },
  "g3_distribution_free": {
    "ceiling": 0.05,
    "pass": true,
    "se": 0.001736,
    "spread_mean": 0.031331,
    "z": 10.750843
  },
  "gates": [
    true,
    true,
    true
  ],
  "params": {
    "R": 30,
    "ceiling": 0.05,
    "cv_hi": 3.0,
    "horizon": 60000,
    "lam": 1.0,
    "load": 10.0,
    "mean_s": 10.0,
    "warmup": 8000
  },
  "proposal": 161,
  "readout": {
    "mg1_wait_tax_multiplier": 5.0
  },
  "seed": 20260717,
  "sigma_gate": 3.0,
  "slot": "round-38 FLEET (fleet-ops spares / maintenance pipeline)"
}
Results-JSON sha256: 9bbe2171bd7678fc7efa03c550f0afbcec438498b0553a1723ee078bf5ec13ef
```

## Verifier
`ideas/fleet/palm_spares_insensitivity.py` — stdlib-only (`math`, `json`, `hashlib`, `random`). Simulates an M/G/∞ repair pipeline (Poisson arrivals rate λ=1, i.i.d. repair time of mean 10) over 60000 integer instants, samples the number in repair post-warmup via a difference-array prefix sum, and over R=30 replications z-tests: the exponential pipeline mean against λ·E[S] (G1), the lognormal-CV3 dispersion index against the Poisson value 1.0 (G2), and the cross-law spread of mean and dispersion against 0 (G3). WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest posture: the results dict carries no digest field; `main()` runs `run()` twice, asserts the two dicts are identical, prints a human-readable header, the indent=2 dump, then the `Results-JSON sha256:` line. No JSON is written to disk.

## Reproduce
```
python3 ideas/fleet/palm_spares_insensitivity.py
```
Expected tail:
```
  "all_pass": true,
  ...
Results-JSON sha256: 9bbe2171bd7678fc7efa03c550f0afbcec438498b0553a1723ee078bf5ec13ef
```
Exit 0; a second invocation is byte-identical.

## Why it matters (spares + maintenance provisioning)
Every recoverable-item stocking decision — depot spares, line-replaceable units, loaner pools, repairable-tool cribs, even standby compute a fleet keeps warm to cover units out for maintenance — is a bet on how many units are simultaneously in the repair pipeline. The counterintuitive, load-bearing fact is that this number is Poisson(failure-rate × mean-repair-time) and **nothing else about the repair process matters**: a maintenance program that halves the *variance* of turnaround time while leaving the *mean* unchanged does not let you carry one fewer spare. The levers that actually shrink the pipeline are the two that move its mean — cut the mean repair/turnaround time E[S] (faster diagnosis, pre-kitted parts, parallel repair), or cut the failure rate λ (reliability, condition-based maintenance). This is exactly the invariance METRIC is built on, and it is the opposite of the queueing-wait intuition, where variance is the dominant tax — so the same "reduce variability" program pays off richly at a congested repair bay (finite servers) and not at all in the ample-server pipeline count. Misreading which regime you are in is how spares budgets get spent on the wrong lever.

## Dedup (contrast vs prior lane heads)
- vs **service-variance-wait-tax / kleinrock-conservation-zero-sum / erlang-b-trunking** — those are WAITING-line results (service variance or scheduling moving WAIT / blocking at a congested server). This is the ample-server (M/G/∞) PIPELINE COUNT, where by Palm's theorem service-time variance is exactly irrelevant — the deliberate inversion of the wait-tax head, not a restatement of it.
- vs **correlated-fleet-variance-floor / variance-blind-provisioning-trap** — those raise a variance FLOOR via cross-unit correlation or ignored variance. Here variance is genuinely immaterial to the pipeline count for INDEPENDENT repairs; the point is insensitivity, not a hidden floor.
- vs **bullwhip-order-variance-amplification** — that is a temporal control-loop amplifying ORDER variance across periods. This is a static, instantaneous COUNT distribution (units currently in repair); no forecasting loop, no amplification, an exact Poisson invariance.
- vs **inspection-paradox-wait-inflation / regression-to-mean** — sampling/observation biases. This is a genuine distributional invariance of an unbiased count, not a measurement artifact.
- No prior fleet head states the M/G/∞ Poisson(λ·E[S]) service-distribution insensitivity for the spares pipeline. Distinct.

## Model basis (declared model-dependence — the P024 discipline)
Exact given the model: Poisson (memoryless) failure arrivals, ample repair capacity (M/G/∞, no queueing for a bay), independent i.i.d. repair times with finite mean. The insensitivity — N ~ Poisson(λ·E[S]), dispersion 1 for any repair law — is a theorem, not a modelling choice, so G2 (dispersion ≈ 1 at CV=3) and G3 (three laws agree) do not depend on the repair distribution or on the scale. Declared model-dependence, disclosed honestly: (1) **ample servers.** If repair bays are finite and units QUEUE, the system is M/G/1 or M/G/c and repair-time variance re-enters through the wait (Pollaczek-Khinchine (1+CV²)/2) — the readout reports that 5× tax for CV=3 as the crossover, not the head. (2) **independent repairs.** Correlated failures or shared repair resources add covariance and break the pure Poisson; independence is the pinned assumption. (3) **the mean is the lever.** The pipeline is invariant to variance but strictly proportional to λ and E[S]; moving either moves the spares — verified implicitly by G1 (E[N]=λ·E[S]). The SIGN and the invariance are structural for the ample-server pipeline; the pinned constants (λ=1, E[S]=10, CV∈{0,1,3}) are the reproduced instance.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed | z | Verdict |
|------|------|-----------|----------|---|---------|
| G1 | pipeline = load | relerr < 0.05, z≥3 | 0.004443 | +68.279173 | PASS |
| G2 | variance-insensitive | disp relerr < 0.05, z≥3 | 0.021783 | +12.870661 | PASS |
| G3 | distribution-free | spread < 0.05, z≥3 | 0.031331 | +10.750843 | PASS |

## Probe report (v0, self-adversarial)
**1. Is the pipeline count really Poisson, or an artifact of the integer-instant sampler?** — M/G/∞ insensitivity is an exact result (the Poisson marking/displacement theorem): the count of arrivals present at any instant is a Poisson thinning with mean λ·E[S]. G1 gates E[N] against λ·E[S]=10 (z=+68.3) and G2 gates the index of dispersion against the Poisson value 1.0 (z=+12.9); both hug the theorem, not sampler noise.
**2. Does repair-time VARIANCE genuinely not matter, or is CV=3 too tame?** — CV=3 is a heavy lognormal (variance 9× the squared mean); the same CV imposes a 5× Pollaczek-Khinchine wait tax on a WAITING line, reported as the readout. The pipeline's dispersion still sits at 1.0 within 0.05 (z=+12.9) — the variance cancels, as the theorem says.
**3. Is the insensitivity distribution-free or a one-law artifact?** — G3 runs deterministic (CV=0), exponential (CV=1), and lognormal (CV=3) repair laws of identical mean and confirms the pipeline mean AND dispersion index agree across all three within 0.05 at ≥3σ (spread 0.031, z=+10.8). Three very different shapes, one Poisson(10) pipeline.
**4. Could the difference-array binning bias Var(N)?** — N is sampled at integer instants and the marginal (mean, variance) are estimated across ~52000 post-warmup samples per replication; the deterministic law (exact bins) and the continuous laws all land on dispersion ≈ 1, so binning does not manufacture or hide the result.
**5. Are the z's inflated by the long horizon?** — No; the z's come from R=30 replications (n=30 per z-test), not from the 52000 within-run samples. Each replication is an independent seeded pipeline, and the ratio lands near its target every time with small cross-replication spread.
**6. Is this just "the count is Poisson" restated?** — The verified, non-obvious content is the SERVICE-DISTRIBUTION INSENSITIVITY: the dispersion stays 1 and the mean stays λ·E[S] as CV sweeps 0→1→3, so the spares requirement is a function of the mean alone — the actionable inversion of the wait-tax intuition, quantified at ≥3σ.
**7. Does it overlap the wait-tax / queueing heads?** — Explicit dedup and crossover: those are finite-server WAIT results where variance dominates; this is the ample-server COUNT where variance is exactly irrelevant. Opposite regime, opposite lever; no shared gate or number.
**8. What would falsify it?** — A reproduction where the CV=3 pipeline's dispersion drifts above 1 (variance leaking into the count), or the three laws' means/dispersions failing to agree within the ceiling, or a non-deterministic double-run. None occur; all three gates pass at ≥3σ and the double-run is byte-identical.

## One-line design fix
Size recoverable-item spares against the pipeline mean λ·E[S] (failure rate × mean repair time) and treat repair-time *variability* as irrelevant to the count — spend variance-reduction effort where units QUEUE for a scarce repair bay, and spend spares-reduction effort on the MEAN (faster turnaround or fewer failures), not on smoothing.

**Recommendation: sim-ready**
