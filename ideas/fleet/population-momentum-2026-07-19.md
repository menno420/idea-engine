# Population momentum — replacement-level fertility still grows a population for a generation

> **State:** sim-ready
> **Class:** demography · age-structured population dynamics · counterintuitive
> **Target:** sim-lab (VERDICT 201, +13 offset)
> 📊 Model: Claude Opus · high · idea/planning
> **Grounding:** https://github.com/menno420/idea-engine@6da9ac5 · fetched 2026-07-19
> **Reference (external, reachable):** [Population momentum — Wikipedia](https://en.wikipedia.org/wiki/Population_momentum) — verified reachable 2026-07-19 via WebFetch ("Population momentum explains why a population will continue to grow even if the fertility rate declines... a current increase in fertility rates causes an increase in the number of women of childbearing age roughly twenty-to-forty years later"). Historical origin conventionally Keyfitz (1971), "On the momentum of population growth," Demography 8(1):71–80 — that attribution is NOT on the Wikipedia page and is unverified from this source.
> **Verifier (firsthand):** ideas/fleet/population_momentum.py · results-dict sha256 fb74854ebd92a08fe48770136cf4e5645b47176394d1b04a70c2a0cc6ef36f33

## The phenomenon (one line)

A growing population whose fertility drops instantly to exact replacement (NRR = 1.000) does not stop growing — it keeps growing for roughly a generation, ending ~29% larger, purely because its age structure is young.

## Domain

Demography / age-structured population dynamics. Outside fleet ops, venture econ, and games — the round-44 UNRELATED slot.

## The folk belief

"If every woman has just enough daughters to replace herself (net reproduction rate = 1), the population holds steady." Replacement fertility is widely read as the switch that stops growth. It is not — not for decades.

## The thesis (reasoned to its fuller form — Q-0254 duty)

Under a Leslie model the long-run growth rate is the dominant eigenvalue λ, and λ = 1 exactly when NRR = 1 (the Euler–Lotka equation at λ = 1 reduces to Σ l(x)m(x) = NRR). So NRR = 1 does fix the *asymptotic* rate at zero. But the *level* it converges to depends on the age structure the population carries at the moment of the switch. A population that was growing (NRR = 1.5) has a young stable structure — an over-representation of children and young adults relative to the stationary structure the new regime will settle into. Those young cohorts have not yet had their (replacement-level) children. As they pass through the childbearing ages, births exceed deaths and the total keeps climbing, until the young bulge ages out and the structure relaxes to the new stationary form. The ratio of the ultimate stationary size to the size at the switch is the *momentum* M > 1. Individual-level replacement does not buy population-level stationarity for about one generation.

## The formal model / Pinned world (committed constants)

- 17 five-year age classes (ages 0–84); childbearing in classes 3–8 (ages 15–44).
- Per-step (5-year) survival s = 0.96 for classes 0–15; class 16 terminal.
- Base fertility shape F_base (classes 0–8) = [0, 0, 0, 0.30, 0.90, 1.00, 0.70, 0.35, 0.10], rescaled to NRR = 1.50 (growth regime) and NRR = 1.00 (replacement regime).
- Initial total N0 = 300000; the initial age structure is the stable (dominant-eigenvector) structure of the growth-regime Leslie matrix.
- Stochastic projection: births ~ Poisson, survival ~ Binomial (Gaussian-approximated for large counts); K = 1500 replicates; horizon T = 50 five-year steps (250 years).
- Robustness: childbearing shape shifted +1 class later (delayed childbearing), NRR re-pinned 1.50 → 1.00.
- SEED = 20260717; null band = 0.02; z_gate = 3.0.

## Pre-registered gates

- **G1 — momentum is real.** From the growth-regime structure under replacement fertility, mean momentum M over K replicates gives z1 = (mean_M − 1)/SE ≥ 3.0 with mean_M > 1.
- **G2 — age structure is the sole cause (null contrast).** A control starting from the replacement-regime stationary structure, same replacement fertility, shows no material growth: |mean_M_null − 1| < 0.02; and z_contrast = (mean_M − mean_M_null)/√(SE1² + SE_null²) ≥ 3.0.
- **G3 — robustness under a shifted vital-rate distribution.** Under delayed childbearing, momentum from the growth-regime structure still gives z3 = (mean_M_shift − 1)/SE ≥ 3.0.

## Pre-registered decision rule

sim-ready iff the verifier reproduces byte-identical results-dict sha256 with all_pass = true and G1 ∧ G2 ∧ G3 holding in order.

## Dry-sim results (SEED=20260717, verbatim from ideas/fleet/population_momentum.py)

- nrr_repl_check = 1.000000 (post-switch fertility is exact replacement).
- deterministic_momentum M_det = 1.291976 (ultimate population 29.2% above the switch level).
- G1: mean_M = 1.291456, SE = 0.000234, **z = 1246.79** → PASS.
- G2: mean_M_null = 1.000409 (within the 0.02 band), z_contrast = 949.02, z_null = 2.06 → PASS.
- G3: mean_M_shift = 1.219339, SE = 0.000197, **z = 1115.58** → PASS.
- all_pass = true; results-dict sha256 = fb74854ebd92a08fe48770136cf4e5645b47176394d1b04a70c2a0cc6ef36f33 (byte-identical across two fresh invocations).

## Reproduce

```
python3 ideas/fleet/population_momentum.py
```

## Verifier

ideas/fleet/population_momentum.py — stdlib-only; deterministic in-process double-run with an equality assert; digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY.

## Why it matters

The failure mode is general: a system's asymptotic rate and its transient trajectory are set by different things. Fixing the per-unit rate (fertility → replacement, per-node arrival → service, per-account churn → retention) does not fix the aggregate until the built-up structure drains. A fleet that halts new spawns still grows its backlog while in-flight work matures; a lane that hits break-even per-cohort still expands while a young-cohort bulge ages in. Momentum quantifies the overshoot and its ~one-generation timescale — useful whenever someone reads a per-unit equilibrium as an aggregate one.

## Dedup

Checked `git grep -il` across ideas/ and control/outbox.md for the mechanism terms. "Leslie" and demographic population momentum: no prior head. "momentum" DOES appear — exclusively in the trading-strategy lane (cross-sectional price/factor momentum: assets that rose keep rising) and in unrelated senses (epidemic-overshoot, tournament-seeding). That is a different mechanism entirely (return autocorrelation vs. age-structure renewal) sharing only the English word. Distinct from shipped counterintuitive-statistics heads (Stein, friendship paradox, Berkson, Will Rogers, Allee cliff, de Moivre, arcsine, Benford, coupon-collector): none is age-structured population renewal. No near-duplicate.

## Model basis (declared model-dependence — the P024 discipline)

The result is model-dependent on the Leslie discrete-renewal convention (top-row fertility, subdiagonal survival) and the pinned vital-rate schedule. The DIRECTION (M > 1 when a growing population switches to replacement) is theory-guaranteed for any young→stationary transition and is confirmed to survive the shifted schedule (G3). The MAGNITUDE (≈1.29) is specific to the pinned NRR-1.5 growth regime, survival 0.96, and fertility shape; a milder prior growth regime yields a smaller M. Disclosed, not hidden.

## Probe report (v0, 2026-07-19)

**1. Is the growth a coding artifact of the Leslie convention, or a real renewal-equation consequence?** Real. λ = 1 exactly at NRR = 1 (Euler–Lotka), so the asymptotic rate is genuinely zero; the growth is the transient of a young initial structure relaxing to stationary, and the deterministic projection (no RNG) already shows M_det = 1.291976.

**2. Would a seed change or a different N0 flip the sign?** No. The direction is deterministic (M_det computed RNG-free); the stochastic replicates land z ≈ 1250 above the null, far beyond seed noise. A larger N0 only tightens SE.

**3. What is the simplest version that still bites — does the null isolate the cause?** Yes. G2 holds fertility fixed at replacement and changes only the starting structure: the young (growth) structure grows 29%, the stationary structure stays flat (mean 1.000409, inside a 2% band). Age structure is the whole story.

**4. How large is the momentum, and does it match the Keyfitz direction?** M ≈ 1.292 — the population ends ~29% larger. Direction M > 1 matches Keyfitz and the Wikipedia worked example (700 → 1200 as fertility drops to replacement).

**5. Where could I be fooling myself — is NRR truly 1.000000 post-switch?** nrr_repl_check = 1.000000 in the results dict: replacement fertility is rescaled to exact replacement, so no residual per-cohort surplus is hiding. The growth is age structure, not leftover fertility.

**6. Does the effect survive a shifted childbearing schedule?** Yes. G3 delays childbearing by one class and re-pins NRR; momentum is still 1.219339 at z ≈ 1116. Robust to the vital-rate distribution.

**7. What decision does it change?** It warns against reading a per-unit equilibrium (replacement fertility, break-even churn, arrival = service) as an aggregate equilibrium: the aggregate overshoots for about one generation while built-up structure drains.

**8. How will we know it worked?** Byte-identical results-dict sha256 fb74854ebd92a08fe48770136cf4e5645b47176394d1b04a70c2a0cc6ef36f33 across fresh runs, all_pass = true, and G1 → G2 → G3 passing in order.

**Recommendation: sim-ready**
