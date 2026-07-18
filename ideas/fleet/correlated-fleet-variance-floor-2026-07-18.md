# The correlated-fleet variance floor — shared errors cap a fleet's wisdom at N_eff → 1/ρ

> **State:** sim-ready
> **Class:** FLEET-domain (round-25 opener) · multi-agent estimation — equicorrelated-error aggregation / wisdom-of-crowds diversification limit · PROPOSAL 109
> **Target:** sim-lab (VERDICT 122, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@d20e881 · fetched 2026-07-18T01:42:17Z
> **Source basis:** the equicorrelation (equicorrelated / exchangeable) variance identity — for N unit-variance errors with common pairwise correlation ρ, Var(mean) = ρ + (1−ρ)/N → ρ; standard textbook result (portfolio diversification limit; "effective sample size" / design-effect N_eff = 1/[ρ+(1−ρ)/N] → 1/ρ). No external repo fetched; every constant is invented-but-pinned in this file.
> **Verifier (firsthand):** committed stdlib-only reference sim `ideas/fleet/correlated_fleet_variance_floor.py` (random, math, json, hashlib) — dry-sim exit 0, all gates PASS, results-dict sha256 77ab05b0…60513903 (see Verify below).

## Domain
FLEET — multi-agent estimation / coordination economics. Distinct from prior fleet slots (winner's-curse common-value auction P101, liquid-democracy random mapping P105, sequential information cascades P064): a *parallel* correlated-aggregation mechanism — many agents estimating one truth with a shared error component, and what that correlation does to the wisdom of the crowd.

## The mechanism
A fleet of N agents each estimates a common truth θ (WLOG θ=0). Agent i's error is a shared common-mode draw plus an idiosyncratic draw:

`ε_i = √ρ · C + √(1−ρ) · Z_i`, with `C ~ N(0, σ²)` (identical for every agent) and `Z_i ~ N(0, σ²)` iid.

Then every agent's error has variance σ² and every pair has correlation ρ. The fleet aggregates by the plain mean, so the fleet-mean error is `E = √ρ·C + √(1−ρ)·mean(Z)`. The common-mode term `C` does **not** average away — it is the same in every estimate.

## The trap (counterintuitive)
"Wisdom of crowds" says averaging N estimates cuts the error variance to σ²/N → 0, so a big fleet is an arbitrarily accurate fleet. The equicorrelation identity says otherwise:

`MSE_N(ρ) = ρ·σ² + (1−ρ)·σ²/N  →  ρ·σ²`  as N → ∞.

- **Variance floor.** The aggregate mean-squared error bottoms out at ρσ² and never goes lower, no matter how many agents you add. Only the `(1−ρ)/N` idiosyncratic slice is diversifiable.
- **Effective count saturates.** `N_eff = σ²/MSE_N = 1/[ρ + (1−ρ)/N] → 1/ρ`. On the pinned world (ρ=0.25, N=400) the floor is 0.251875 while independence predicts 0.0025 — **a fleet of 400 correlated agents is worth only ~3.97 independent ones** (asymptote 1/ρ = 4), and ~99% of the promised variance reduction never materializes.
- **Scaling is futile past N ≈ 1/ρ.** Going from N=25 to N=400 to N=∞ moves MSE from 0.2725 → 0.2519 → 0.2500: 16× more agents cuts the error by under 1%. The bottleneck is the shared component, not the fleet size.

Nothing here is adversarial or a modelling artifact: it is the plain covariance algebra of a shared error term. Any fleet whose members share a common config, upstream, prior, or dataset inherits the floor.

## Gates (each ≥3σ on the /se margin; SEED=20260717, N=400, ρ=0.25, 400 trials × 200 batch)
| gate | statistic | claim |
|---|---|---|
| G1 correlated floor (headline) | mean(MSE_corr) | ≥ 0.10 |
| G2 correlation-necessity (control) | mean(MSE_indep) vs σ²/N | \|z\| < 3 |
| G3 closed-form anchor | mean(MSE_corr) vs ρσ²+(1−ρ)σ²/N | \|z\| < 3 |

G2 is the isolating control: with ρ=0 (no shared component) the **same** fleet size collapses to σ²/N=0.0025, so the floor in G1 is 100% the common-mode correlation, not fleet size or a sim artifact.

## Verify
```
python3 ideas/fleet/correlated_fleet_variance_floor.py   # exit 0; prints canonical results + sha256
```
Deterministic: pinned seed, canonical `json.dumps(sort_keys, separators)` → sha256 reproduces byte-for-byte on a double run. Expected results-dict sha256 disclosed in the outbox block after the dry run: `77ab05b0c61ce782d90f51a747cd4a96f5445f4df10f982a506f346a60513903`.

## Fleet relevance
Any fleet that averages/votes over many agents to beat noise inherits this floor when the agents share an error source: replicas reading the same stale cache, monitors on the same upstream, model ensembles sharing a training prior or a feature, retries hitting the same failing dependency, pollers with a common clock skew. Mitigation for sim-lab to explore: measure the *residual* correlation ρ and report N_eff = 1/ρ (not N) as the real precision budget; decorrelate the shared component (independent inputs/configs/priors) before scaling the count — adding agents past N ≈ 1/ρ is spend without precision.

## Model basis (declared model-dependence — the P024 discipline)
The floor depends on structural assumptions: (a) a single scalar common-mode component shared identically by all agents plus iid idiosyncratic noise, giving exact equicorrelation ρ (an exchangeable-error model; heterogeneous or block-correlation structures shift the constant but not the floor's existence); (b) Gaussian errors, used only so the idiosyncratic fleet-mean has a clean sampling distribution — the variance identity Var(mean)=ρσ²+(1−ρ)σ²/N holds for ANY finite-variance equicorrelated errors, Gaussian or not (the mechanism is second-moment, not distributional); (c) equal-weight averaging as the aggregation rule (optimal-weight or shrinkage aggregation cannot beat the ρσ² floor either — the common-mode term is common to every estimate). The verifier draws the N idiosyncratic errors **explicitly** and averages them, so the 1/N reduction emerges from the fleet rather than being asserted; ρ enters through the shared draw C. The claim is scoped: under a shared-common-mode equicorrelated error model with equal-weight aggregation, the fleet MSE floors at ρσ² and N_eff saturates at 1/ρ — mechanism-explained, not asserted as a universal law.

## Dedup
Distinct from prior fleet slots: winner's-curse task auction (P101, common-value auction/valuation economics), liquid-democracy random mapping (P105, functional-graph governance), Braess selfish routing (P092, congestion equilibrium), and sequential information cascades (P064, Bikhchandani–Hirshleifer–Welch observational herding). Those are auction, graph, routing, and *sequential* learning mechanisms; this is *parallel* correlated aggregation — an equicorrelation-covariance variance floor, a second-moment estimation result, not a Bayesian herd, an auction, or a graph collapse. No prior fleet idea models a shared-common-mode estimator fleet or the N_eff = 1/ρ diversification limit.

## Probe report (v0, 2026-07-18)

**1. What is this really?** An equicorrelation-variance claim: N=400 agents each estimate a common truth with error ε_i=√ρ·C+√(1−ρ)·Z_i (shared common-mode C, idiosyncratic Z_i), so pairwise correlation is ρ=0.25. The fleet mean's error variance is the exact ρσ²+(1−ρ)σ²/N=0.251875, which floors at ρσ²=0.25 as N→∞. The effective independent count N_eff=σ²/MSE→1/ρ=4: a 400-agent fleet is worth ~3.97 independent agents, and ~99% of the variance reduction independence predicts never appears.
**2. What would make it false?** If a simulation showed the correlated-fleet MSE at N=400 collapsing toward σ²/N=0.0025 (the floor does NOT bind), or the ρ=0 control NOT collapsing to σ²/N (the effect is not the shared component), or the correlated MSE not matching the equicorrelation formula ρσ²+(1−ρ)σ²/N. Any of G1/G2/G3 failing → REJECT.
**3. Simplest version that still bites?** SEED=20260717, N=400 agents, ρ=0.25, 400 trials each averaging 200 fleet realizations; each realization draws one shared C and N idiosyncratic Z_i, forms the fleet-mean error E, records E²; compare the mean MSE to the 0.10 floor (G1), the ρ=0 control MSE to σ²/N (G2), and the correlated MSE to the closed form (G3).
**4. What is the counterintuitive core?** Averaging "feels" like it should drive error to zero — more agents, less noise, σ²/N → 0. But a shared error component is identical in every estimate, so it survives the average untouched: the fleet mean's error variance floors at ρσ² and N_eff caps at 1/ρ. Four hundred agents buy the accuracy of four. No adversary, no bias, no non-stationarity — pure covariance of a common term.
**5. Where could I be fooling myself?** Finite-batch noise in the MSE estimate: E² is heavy-tailed (∝χ²₁), so the gate correctly tests the ESTIMATED MEAN via its standard error (se=std/√400), not the per-realization spread. The Gaussian choice is not load-bearing — the variance identity is second-moment and holds for any finite-variance equicorrelated errors; Gaussian only gives a clean draw. Drawing the N idiosyncratic errors explicitly (not sampling the mean from N(0,σ²/N)) keeps the 1/N reduction empirical, so G3's match is a genuine confirmation of the formula, not a tautology.
**6. What is the honest calibration?** Dry-sim margins at SEED=20260717: G1 mean_mse_corr=0.250281 (se 0.001198) z=125.4097σ (≥0.10); G2 mean_mse_indep=0.002502 (se 1.3e-05) vs anchor 0.0025 |z|=0.1469 (<3); G3 mean_mse_corr=0.250281 vs anchor 0.251875 |z|=1.3306 (<3) — G1 clears the ≥3σ bar, G2/G3 sit inside 3σ; N_eff(sim)=3.995517 (asymptote 1/ρ=4.0); exit 0; results-dict sha256 77ab05b0…60513903.
**7. What decision does it change?** Any fleet that averages/votes over many agents to beat noise — replica reads, monitor quorums, model ensembles, retry fan-out, poller pools — should budget precision by N_eff=1/ρ (the residual shared-error correlation), not by the raw count N. Measure ρ; decorrelate the shared input/config/prior before scaling; and stop adding agents once N ≈ 1/ρ, because past that the count grows and the precision does not.
**8. How will we know it worked?** The committed stdlib verifier reproduces mean_mse_corr ≥ 0.10 at ≥3σ (G1), the ρ=0 control MSE within 3σ of σ²/N (G2), and the correlated MSE within 3σ of ρσ²+(1−ρ)σ²/N (G3), with the results-dict sha256 matching 77ab05b0c61ce782d90f51a747cd4a96f5445f4df10f982a506f346a60513903.

**Recommendation: sim-ready**
