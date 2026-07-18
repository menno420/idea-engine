# Selecting the extreme-low tail of a noisy repeated measure and doing NOTHING manufactures a large, hundred-sigma "improvement" of exactly (rho−1)·E[X|X<c] — pure regression to the mean, mistaken for a treatment effect: at rho=0.5 and a −1 SD cutoff, the underperformers "improve" by +0.76 SD while the whole population does not move at all.

> **State:** sim-ready
> **Class:** UNRELATED-domain (round-24 closer) · statistics / experimental design / measurement — Galton's regression to the mean · fleet-external pure-mechanism head
> **Target:** sim-lab (VERDICT 121, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@a2c7162 · fetched 2026-07-18T01:30:00Z
> **Source basis:** F. Galton, "Regression towards Mediocrity in Hereditary Stature," J. Anthropol. Inst. 15 (1886) 246–263 — the regression coefficient E[Y|X=x]=rho·x for a bivariate normal, and the inverse-Mills-ratio mean of a truncated normal E[X|X<c]=−phi(c)/Phi(c) (standard textbook results; the Kahneman flight-instructor example is the same mechanism; no external repo fetched).
> **Verifier (firsthand):** committed stdlib-only reference sim `ideas/fleet/regression_to_mean.py` (random, math, json, hashlib) — dry-sim exit 0, all gates PASS, results-dict sha256 35d65a50…85ed8aed (see Verifier + Dry-sim below).

## The phenomenon (one line)
When a measurement is noisy (test-retest reliability rho<1) and you SELECT the units that scored at an extreme — say the underperformers with pre score X below a cutoff c<0 — then re-measure the SAME units (Y) after doing NOTHING, their mean moves back toward the population mean by exactly Delta* = (rho−1)·E[X|X<c] > 0. It looks like the selected group improved; nobody changed. At rho=0.5 and c=−1 SD, E[X|X<c]=−1.525135 and the spurious improvement is +0.762568 SD, while the whole population's before/after change is exactly zero.

## The folk belief
"We identified the worst performers, gave them the intervention, and re-measured — they improved, so the intervention works." The before/after change of the treated group is read as the treatment effect. The selection ("worst performers") and the noise (any measure has some) are treated as innocuous bookkeeping. The folk error is judging a selected-because-extreme group by its own before/after delta, with no randomized control and no correction for the regression the selection guarantees.

## The thesis (reasoned to its fuller form — Q-0254 duty)
A noisy measure of a fixed latent quantity is latent + independent error. Two reads of the same unit (X pre, Y post) are therefore a bivariate normal with correlation rho equal to the reliability (the shared-latent fraction), and E[Y | X=x] = rho·x for standardized scores: the conditional expectation of the second read is the first read SHRUNK toward the mean by the factor rho. That shrinkage is regression to the mean, and it is a theorem, not a tendency — it happens for every rho<1 whether or not anything is done between the reads.

Now select on the extreme. Conditioning on X<c (the underperformers) pulls the selected group's mean pre score to E[X | X<c] = −phi(c)/Phi(c), the inverse Mills ratio — a number strictly below c, and well below the population mean 0 (at c=−1 it is −1.525135). Their post scores, by the conditional-expectation law, average rho·E[X | X<c] — pulled a (1−rho) fraction of the way back to the mean. The group's apparent improvement is the gap:

  Delta* = E[Y | X<c] − E[X | X<c] = rho·E[X|X<c] − E[X|X<c] = (rho−1)·E[X|X<c].

Because E[X|X<c] < 0 and rho < 1, this is strictly POSITIVE: the underperformers "improve" by (1−rho)·|E[X|X<c]| with zero intervention. The same algebra run on the over-performers (X > −c) gives a symmetric spurious DECLINE (rho−1)·E[X|X>−c] < 0 — the "winners" appear to get worse. And the whole population, selected on nothing, has E[Y] − E[X] = 0: there is no time trend. The counterintuitive core: an INERT intervention applied to a selected-because-extreme group produces a large, statistically overwhelming, perfectly replicable effect, and the effect's size is fixed in advance by the reliability and the selection cutoff — Delta* = (rho−1)·E[X|X<c] — nothing about the intervention enters it. The illusion is not sampling error (it does not shrink with n; it grows in significance) and not a global trend (the population is flat); it is entirely manufactured by selecting on the extreme of a noisy measure and re-measuring.

## The formal model (committed constants — sim-lab must reproduce exactly)
- Standard bivariate normal repeated measure. Per unit: pre score X ~ N(0,1); post score Y = rho·X + sqrt(1−rho^2)·Z with Z ~ N(0,1) independent — so (X,Y) is standard bivariate normal with correlation rho and NO real change between reads (the "intervention" is inert).
- Selection: the underperformers are the units with X < C_THRESH. The control is the WHOLE population (no selection). Descriptive: the over-performers are the units with X > −C_THRESH.
- Per trial (N_UNITS units): delta_sel = mean(Y)−mean(X) over the selected underperformers; delta_pop = mean(Y)−mean(X) over the whole population; delta_top = mean(Y)−mean(X) over the over-performers. Averaged over TRIALS independent experiments; gate z on the estimated mean via its standard error se = std/sqrt(TRIALS).
- Analytic anchors (Galton; standard-normal truncation):
  - Selection gap: E[X | X<c] = −phi(c)/Phi(c) (inverse Mills ratio), with phi the standard-normal pdf and Phi its CDF (computed via math.erf).
  - Spurious improvement: Delta* = (rho−1)·E[X | X<c] > 0 for rho<1, c<0.
  - Over-performer gap E[X | X>−c] = phi(−c)/(1−Phi(−c)); spurious decline Delta_top* = (rho−1)·E[X | X>−c] < 0.

## Pinned world (committed constants)
- SEED = 20260717 (proposal-owned; SEEDLESS discipline)
- RHO = 0.5 (test-retest reliability; correlation of the two noisy reads of one fixed latent ability)
- C_THRESH = −1.0 (selection cutoff: "underperformers" more than 1 SD below the mean)
- N_UNITS = 20000 (units per trial)
- TRIALS = 400 (independent experiments; the /se convention averages over these)
- SIGMA_GATE = 3.0 (pre-registered gate threshold in σ)
- IMPROVE_MIN = 0.50 (G1 floor on the spurious improvement, SD units)
- Derived: m_sel = E[X|X<c] = −1.525135, Delta* = (rho−1)·m_sel = 0.762568, top-tail Delta_top* = −0.762568.

## Pre-registered gates (all on the /se margin; APPROVE iff ALL hold)
- **G1 — spurious-improvement headline:** the selected underperformers' mean improvement Delta_sel exceeds IMPROVE_MIN=0.50 by ≥3σ: (Delta_sel − 0.50)/se ≥ 3 AND Delta_sel > 0. An inert intervention on the bottom tail shows a large, significant "effect".
- **G2 — selection-necessity control:** the WHOLE-population before/after change Delta_pop is within 3σ of 0: |Delta_pop|/se < 3. There is no global time trend, so G1's effect is 100% selection-on-extremes + regression, not drift.
- **G3 — closed-form anchor MATCH:** Delta_sel matches the exact regression prediction Delta* = (rho−1)·E[X|X<c] within 3σ: |Delta_sel − Delta*|/se < 3. Reproduces Galton's regression coefficient, so the effect IS the RTM mechanism (not some other quantity).

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 ∧ G3 all hold at their stated thresholds on the pinned world with SEED=20260717 and the committed reference verifier. Any gate failing → REJECT (the regression-to-the-mean claim is falsified for these constants). No post-hoc threshold moves; SEED is not changed; margins reported in σ.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
- Anchors: m_sel = −1.525135 · Delta* = 0.762568 · top-tail Delta_top* = −0.762568
- delta_sel (selected underperformers) = 0.762986 (se 0.000842) — the spurious improvement
- delta_pop (whole-population control) = 4.5e-05 (se 0.000372) — no time trend
- delta_top (over-performers, descriptive) = −0.764375 (se 0.000738) — the symmetric spurious decline
- **G1 spurious improvement:** z = 312.4059 — PASS (delta_sel=0.762986 ≥ 0.50, > 0)
- **G2 population control:** |z| = 0.1204 — PASS (< 3σ; the whole population does not move)
- **G3 anchor-match:** |z| = 0.4969 — PASS (< 3σ; delta_sel=0.762986 vs closed Delta*=0.762568)
- **all_pass = true; exit 0**
- **Disclosed results-dict sha256 = 35d65a5060d0582a5fd0d041c2d72635657c7f8c62ac024d4ee004b285ed8aed**

## Verifier
Stdlib-only python3 (`random, math, json, hashlib` — no numpy/scipy), committed alongside this idea as `ideas/fleet/regression_to_mean.py`. Seed once with SEED=20260717. It computes the closed-form selection gap E[X|X<c]=−phi(c)/Phi(c) (Phi via math.erf) and the anchor Delta*=(rho−1)·E[X|X<c], then runs TRIALS=400 independent experiments of N_UNITS=20000 standard bivariate-normal repeated measures (Y=rho·X+sqrt(1−rho^2)·Z), selects the underperformers X<C_THRESH with NO intervention applied, records per-trial delta_sel/delta_pop/delta_top, computes means and standard errors, evaluates G1/G2/G3 on the /se margin, and emits a canonical (sorted-keys, comma/colon-separated) results JSON with its sha256. Exit 0 iff all gates pass.

Reproduce:

```
python3 ideas/fleet/regression_to_mean.py
```

Expected: all_pass=true, exit 0, m_sel=−1.525135, Delta*=0.762568, results-dict sha256 = 35d65a5060d0582a5fd0d041c2d72635657c7f8c62ac024d4ee004b285ed8aed.

## Why it matters (transferable mechanism)
Any before/after comparison whose group was chosen BECAUSE it was extreme on a noisy measure carries a built-in spurious effect of exactly (rho−1)·E[X|selected]: part of the group's extremeness was luck that does not repeat, so it regresses toward the mean by the (1−rho) fraction, manufacturing an "improvement" (bottom tail) or "decline" (top tail) with zero real change. The correct read requires a randomized control (or the unselected population) as the counterfactual, or an explicit RTM correction that subtracts the regression prediction before crediting the intervention. The transferable audit: whenever an intervention is applied to a selected-because-extreme cohort and judged by its own before/after delta, ask "what would a randomized control — or the whole unselected population — have done?" — and if the measure is noisy and the selection was on the measure itself, the answer is (rho−1)·E[X|selected], which must be netted out. As a fleet-external pure-mechanism head there is NO lane build here; the deliverable is a citable measured verdict plus the "a selected-because-extreme group regresses by (1−rho); use a control or subtract the regression prediction, never the naked before/after delta" correction.

## Dedup
Distinct from the nearby priors:
- **kelly-overbet-ruin** (P100, the round-22 UNRELATED closer): a repeated-MULTIPLICATIVE-betting interior-optimum / ensemble-vs-time-average trap in information theory / mathematical finance. This head is a statistics/measurement selection illusion — a different domain (Galton regression / experimental design), a different object (a conditional-expectation regression coefficient (rho−1)·E[X|X<c], not a log-growth argmax), and a different counterintuition (an inert intervention manufacturing a spurious effect via selection-on-extremes, not an arithmetic-vs-geometric mean gap).
- **epidemic-overshoot** (P104, the round-23 UNRELATED closer): a self-limiting SIR cascade whose settling point overshoots a growth-stops threshold (epidemiology / Kermack–McKendrick final-size theory). This head prices no epidemic and no final-size fixed point — it is a regression coefficient under truncated-normal selection. This is the mandated NEW unrelated domain, distinct from BOTH prior closers, not a re-skin.
- **berkson-admission-collider** (P-era): a collider / selection-bias illusion, but Berkson's paradox is a spurious CORRELATION induced by conditioning on a common effect (admission), not a regression-to-the-mean shift under selection on ONE extreme tail of a repeated measure. Different mechanism (collider vs RTM), different object (an induced negative correlation vs a (rho−1) mean shift).
- **simpsons-paradox-aggregation-reversal** (P-era): an aggregation-reversal illusion (a trend reverses when groups are pooled), not a regression toward the mean under selection; no truncated-normal selection gap, no reliability coefficient.
- **inspection-paradox-wait-inflation** / **friendship-paradox-sensor**: size-biased-sampling illusions (long intervals / high-degree nodes over-sampled), a different sampling bias than regressing a noisy re-measure of a selected extreme; the "spurious effect from how the group was selected" template names them as cousins, distinct from this measured RTM verdict.
- No prior idea in the tree models regression to the mean, a test-retest reliability coefficient rho, or a truncated-normal selection gap E[X|X<c]; grep of the full ideas/ tree + outbox history returns no RTM / regression-to-the-mean / inverse-Mills-ratio head.

## Model basis (declared model-dependence — the P024 discipline)
The exact anchor Delta*=(rho−1)·E[X|X<c] depends on structural assumptions: (a) a standard bivariate-normal repeated measure (Gaussian latent + Gaussian independent error), so E[Y|X=x] is exactly linear (rho·x) and the truncated mean is the inverse Mills ratio; (b) the "intervention" is inert (no real effect), isolating the RTM component; (c) selection is on the pre score X itself (selection-on-the-measure). Under a non-normal measure the conditional expectation E[Y|X] is no longer exactly linear, so the numeric anchor shifts (the truncated mean and the regression function change), and if the intervention has a REAL effect it adds to the RTM shift (the point is precisely that the naked before/after delta confounds the two). But the qualitative result — a selected-because-extreme group regresses toward the mean by a positive (1−rho)-scaled amount whenever the measure is noisy and monotonically related across reads — is robust wherever reliability is below 1. The claim is scoped: under the standard bivariate-normal model with rho<1 and selection on X<c, the selected group's spurious before/after improvement is exactly (rho−1)·E[X|X<c]>0, demonstrated on the pinned constants, mechanism-explained, not asserted as a universal numeric law.

## Probe report (v0, 2026-07-18)

**1. What is this really?** A Galton regression-to-the-mean claim: select the underperformers (pre score X below a −1 SD cutoff) of a noisy repeated measure with reliability rho=0.5, apply an INERT intervention, and re-measure — the selected group's mean rises by exactly Delta*=(rho−1)·E[X|X<c]=+0.762568 SD, purely because their extreme-low score was partly luck that does not repeat, while the whole population does not move.
**2. What would make it false?** If the selected group's before/after change settled at 0 rather than at Delta*≈0.76 (no regression), or failed to match the closed-form (rho−1)·E[X|X<c], or if the whole-population control ALSO moved by a comparable amount (a real time trend rather than a selection artifact). Any of G1/G2/G3 failing → REJECT.
**3. Simplest version that still bites?** SEED=20260717, rho=0.5, c=−1.0, 20000 units × 400 trials of standard bivariate-normal (X,Y); compare the selected underperformers' mean improvement to a 0.50 floor (G1) and to the closed-form (rho−1)·E[X|X<c] (G3), and check the whole-population change is ~0 (G2).
**4. What is the counterintuitive core?** An intervention that does LITERALLY NOTHING produces a large, hundred-sigma, perfectly replicable "improvement" — and its size is fixed in advance by the reliability and the cutoff, (rho−1)·E[X|X<c], with nothing about the intervention entering it. The effect does not shrink with n (it grows in significance) and is not a global trend (the population is flat); it is manufactured entirely by selecting on the extreme of a noisy measure and re-measuring.
**5. Where could I be fooling myself?** A finite-N selection bias could in principle trip the anchor match — but the sim reproduces Delta* to |z|=0.4969σ (well inside G3's 3σ), and the whole-population control sits at |z|=0.1204σ from 0, confirming there is no drift to confound the signal. The gauss draws are deterministic under SEED (two runs byte-identical), and the anchor E[X|X<c]=−phi(c)/Phi(c) is computed in-verifier via math.erf, not hard-coded.
**6. What is the honest calibration?** Dry-sim margins at SEED=20260717: G1 spurious-improvement z=312.4059σ (delta_sel=0.762986 vs floor 0.50), G2 population-control |z|=0.1204σ (delta_pop=4.5e-05 vs 0), G3 anchor-match |z|=0.4969σ (delta_sel=0.762986 vs closed Delta*=0.762568) — all clear the ≥3σ / <3σ bars; exit 0; results-dict sha256 35d65a50…85ed8aed. m_sel=−1.525135, Delta*=0.762568, symmetric top-tail decline delta_top=−0.764375.
**7. What decision does it change?** Never credit an intervention by the before/after delta of a group that was selected for being extreme on a noisy measure: use a randomized control (or the unselected population) as the counterfactual, or subtract the regression prediction (rho−1)·E[X|selected] before attributing any effect. "We fixed the worst-performing X and it improved" is, by default, regression to the mean — not the fix.
**8. How will we know it worked?** The committed stdlib verifier reproduces delta_sel ≈ Delta* within 3σ, delta_sel ≥ 0.50 by ≥3σ, and a whole-population control within 3σ of 0, with the results-dict sha256 matching 35d65a5060d0582a5fd0d041c2d72635657c7f8c62ac024d4ee004b285ed8aed.

**Recommendation: sim-ready**
