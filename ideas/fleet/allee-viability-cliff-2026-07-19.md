# The strong Allee effect makes population viability a cliff, not a slope: below a critical density A the population deterministically drains to extinction, above A it climbs to carrying capacity

> **State:** sim-ready
> **Class:** counterintuitive-dynamics / population-ecology (unrelated slot)
> **Slot:** round-36 unrelated
> **Target:** sim-lab (VERDICT 169, +13 offset)
> **Grounding:** https://en.wikipedia.org/wiki/Allee_effect@854835807f66e5b253350b8a3e79e9408b466b9e · fetched 2026-07-19T04:56:46Z
> **Reference (external, reachable):** Wikipedia "Allee effect" — original: W. C. Allee (1931), *Animal Aggregations: A Study in General Sociology*; modern synthesis: F. Courchamp, L. Berec & J. Gascoigne (2008), *Allee Effects in Ecology and Conservation* (Oxford University Press).
> **Harvest source (firsthand):** ideas/fleet/allee_viability_cliff.py + its recorded double-run (this branch).

## The phenomenon (one line)
Under a *strong* Allee effect a population has a critical density A: start with even slightly fewer individuals than A and the population is deterministically doomed to extinction; start with slightly more and it climbs to carrying capacity — survival is a sharp cliff at N = A, not a gentle dose-response.

## The folk belief
"More of a resource is always at least a little better than less; a small population is just a slow-growing large one — give it time and it recovers." Conservation intuition says a remnant of 25 is only modestly worse off than a remnant of 35. The strong Allee effect says the first is doomed and the second is safe: below A the per-capita growth rate is *negative*, so the population does not grow slowly — it shrinks to zero.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
At low density, cooperative processes fail — mates cannot find each other, group defence and cooperative feeding collapse, inbreeding rises — so the per-capita growth rate turns *negative* below a threshold A. The canonical strong-Allee growth law encodes exactly this:
    dN = r · N · (1 − N/K) · (N/A − 1),   N_{t+1} = N_t + dt·dN.
The extra factor (N/A − 1) is negative for N < A and positive for A < N < K. The map has THREE fixed points:
    N = 0   — STABLE (extinction well)
    N = A   — UNSTABLE (the Allee threshold / separatrix)
    N = K   — STABLE (persistence well).
Because A is unstable, the deterministic flow is monotone away from it: any N0 < A drains to 0, any N0 > A climbs to K. A is therefore the *basin boundary* between the two wells. This is directly testable without noise: bisect the initial density that separates "drains to 0" from "climbs to K" and it must land on A — and it must do so for *every* (r, K) pair sharing the same A, because A is set only by the cooperation threshold, not by r or K (invariance probe). Adding demographic noise (fluctuation scaling with √N, the standard population-size term) turns the deterministic cliff into a stochastic one: seeded below A the extinction fraction is ≈ 1; seeded above A it is ≈ 0. Allee's original aggregation studies (1931) and the Courchamp, Berec & Gascoigne (2008) synthesis document the mechanism across mammals, birds, insects, and plants.

## Pinned world (committed constants — the verifier is the contract)
SEED=20260717 · main world r=0.6, K=100, A=30, dt=0.02 · deterministic invariance probe over (r,K) ∈ {(0.6,100), (0.3,150), (0.9,80)}, all A=30, DET_STEPS=6000, DET_TOL=1e-6 · stochastic layer R_TRIALS=400, T_STEPS=2000, EXT_EPS=0.5, DELTA=0.15 (below N0=A(1−DELTA)=25.5, above N0=A(1+DELTA)=34.5), baseline SIGMA_LO=0.25, shifted SIGMA_HI=0.55 · proportion se=√(0.25/400)=0.025, gap se=√(2·0.25/400)=0.035355, GAP_MIN=0.6, z_gate=3.0.

## Pre-registered gates (evaluation order G1 → G2 → G3; APPROVE iff ALL hold)
- **G1 — doomed below the threshold.** From N0 = A(1−DELTA)=25.5, extinction fraction p_below against conservative null H0=0.5: z1 = (p_below − 0.5)/se ≥ 3. Observed p_below = **1.000000**, z1 = **+20.000000**. (p_above from N0=34.5 recorded alongside: **0.000000**.)
- **G2 — safe above the threshold (leak-ceiling NEGATION).** From N0 = A(1+DELTA)=34.5, the extinction fraction p_above must sit UNDER the 0.5 ceiling: z2 = (0.5 − p_above)/se ≥ 3. Observed p_above = **0.000000**, z2 = **+20.000000**.
- **G3 — robust to a shift to heavier demographic noise.** Raise sigma to SIGMA_HI=0.55; gap′ = p_below_hi − p_above_hi against null GAP_MIN=0.6: z3 = (gap′ − 0.6)/se_gap ≥ 3. Observed p_below_hi = **0.912500**, p_above_hi = **0.090000**, gap′ = **0.822500**, z3 = **+6.293250**.

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 ∧ G3 all hold on a clean-room re-run (SEED=20260717) with the results-dict sha256 matching. Any gate false → REJECT naming first_failing_gate. Observed all_pass = **true**, first_failing_gate = **null**. Independent-check handles for a VERDICT 169 session: SEED=20260717, z_gate=3.0, the three gate definitions and their nulls above, and the results-dict sha256 below (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture — no `results_sha256` key inside the dict).

## Disclosed verifier (the sim-lab spec)
`ideas/fleet/allee_viability_cliff.py` — stdlib only (hashlib, json, math, random). Posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY. Builds a fresh `random.Random(SEED)` inside `run()` (so in-process and cross-invocation streams coincide), runs the deterministic basin-boundary bisection (no rng consumed), then the four stochastic experiments in fixed order (below/above at SIGMA_LO, below/above at SIGMA_HI), assembles the ordered results dict, asserts an in-process double run is identical, and prints the pretty dict and its sha256 (all floats round()-ed to 6 dp before hashing). Expected results-dict sha256:
    bbc42b796c1dab6fae0b4be5da91e277a737cfdd5fd61246700fe826600b9471
Re-run twice cross-invocation; both must print IDENTICAL output and the sha256 above; exit 0 iff all_pass. Deterministic basin boundaries observed: **[30.0, 30.0, 30.0]** — all three (r,K) pairs land on A=30 (invariance).

## Why it matters
The strong Allee effect is the load-bearing counterexample to "a small population is just a slow one." It sets a hard extinction floor: conservation of an endangered species, reintroduction of a locally-extinct one, or biological pest control all live or die on whether the seeded density clears A. The same threshold-with-an-unstable-middle structure recurs wherever a system needs a critical mass to self-sustain — an ignition below which output decays and above which it runs. It is a clean, quantitative instance of a *bistable* system whose separatrix is a real, measurable density, grounded in a century of field ecology.

## Dedup (contrast vs prior lane heads)
- vs **Braess's paradox (P155-era)** — a strategic-equilibrium routing artifact (added capacity, worse equilibrium); this is a single-population *bistable dynamical* threshold. No network, no equilibrium of agents.
- vs **Will Rogers stage migration (P148)** — a classification / relabelling artifact on a conserved population; this is a genuine *dynamical* extinction/persistence split, no reclassification.
- vs **epidemic overshoot / SIR, regression to the mean, Simpson's, friendship paradox** — none is a strong-Allee bistability with an unstable interior fixed point acting as a basin boundary.
- Crossover honesty: the "critical-mass adoption" reading — a venture/fleet needs a minimum active base or it decays, above which it self-sustains — is a CROSSOVER ANALOGY, not the verified claim. The verified claim is strictly population-ecology (the strong-Allee growth law). Distinct mechanism from every prior head.

## Model basis (declared model-dependence — the P024 discipline)
Exact given the model: the cubic strong-Allee map dN = rN(1−N/K)(N/A−1) with 0 < A < K, small-dt explicit Euler integration, and √N demographic noise. The three fixed points and the fact that A is the unstable separatrix are structural — they do not depend on the specific r, K, dt (the invariance probe confirms the boundary is A for all three (r,K) pairs). Dependence disclosed honestly: (i) explicit Euler with too large a dt would distort magnitudes near K — dt=0.02 is small enough that the deterministic boundary lands on A to 1e-6; (ii) the noise term is demographic (√N) not environmental (∝N) — a different noise law would shift the exact p_below_hi/p_above_hi but not the sign of the cliff; (iii) EXT_EPS=0.5 is a small absorbing floor standing in for "last individual" — a continuous state, not integer counts. NOT a claim about one named species; the claim is that this documented mechanism is real, sign-correct, sharp at N=A, and robust to a noise-distribution shift.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed stat | z | Verdict |
|------|------|-----------|---------------|---|---------|
| G1 | sign (below doomed) | p_below > 0.5, z≥3 | 1.000000 | +20.000000 | PASS |
| G2 | ceiling (above safe) | p_above < 0.5, z≥3 | 0.000000 | +20.000000 | PASS |
| G3 | robustness (shifted noise) | gap′ > 0.60, z≥3 | 0.822500 | +6.293250 | PASS |

## Probe report (v0, self-adversarial)
**1. Is the object real or a rigged toy?** Real — the strong-Allee growth law is textbook population ecology (Allee 1931; Courchamp, Berec & Gascoigne 2008). N0=25.5 and 34.5 straddle A=30 by ±15%; no free parameter is tuned to force the split — the split IS the strong-Allee bistability.
**2. Is A=30 really the basin boundary, or picked to match?** The deterministic bisection finds the drain/climb separatrix with NO knowledge of A and lands on 30.000000 for all three (r,K) pairs — invariance. A is where the per-capita rate crosses zero, structural, not fitted.
**3. Is the null conservative enough?** Yes — G1/G2 gate proportions against H0=0.5 with se=√(0.25/400), the most conservative proportion variance. z1 and z2 are +20 because p_below and p_above are pinned at the 0/1 corners over 400 trials, not because the se was shrunk.
**4. Is the method sound (integration + noise)?** Explicit Euler at dt=0.02 keeps the deterministic boundary on A to 1e-6 (no overshoot: the map is monotone away from A). Demographic noise σ√N√dt·ε is the standard population-size fluctuation term; extinction is an absorbing hit of EXT_EPS=0.5 within T_STEPS=2000.
**5. Are the gates actually ordered and independent handles?** Yes — G1 (below doomed) and G2 (above safe) are two *different* seedings; G2 uses the leak-ceiling NEGATION form (0.5 − p_above)/se so "must stay under a ceiling" reads as a positive z. G3 is a *third* experiment at heavier noise. all_pass = G1 ∧ G2 ∧ G3, first_failing_gate names the first false.
**6. Does the cliff survive a noise-distribution shift?** Yes — at SIGMA_HI=0.55 the below/above extinction gap is still 0.8225 (p_below_hi 0.9125, p_above_hi 0.09), clearing GAP_MIN=0.6 at z3=+6.29. Heavier noise blurs the corners but does not erase the cliff.
**7. What breaks it / what is the honest caveat?** Where the noise is large enough or the offset DELTA small enough, corners fatten (p_above_hi rose from 0 to 0.09 under SIGMA_HI) — disclosed, not hidden. The "critical-mass adoption" fleet/venture reading is a CROSSOVER analogy only; the verified claim is population-ecology. A different noise law (environmental ∝N) or a much larger dt would move magnitudes, not the sign.
**8. How do we know it worked (determinism)?** SEED=20260717 pinned; a fresh `random.Random(SEED)` is built inside `run()`; the in-process double run is asserted identical; the cross-invocation double run printed IDENTICAL output with results-dict sha256 bbc42b796c1dab6fae0b4be5da91e277a737cfdd5fd61246700fe826600b9471. A verdict re-run must reproduce that digest.

**Recommendation: sim-ready**
