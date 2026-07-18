# Reaching herd immunity does NOT stop an epidemic: infections already in flight keep transmitting, so the final attack rate z* solves z=1−e^{−R0·z} and strictly OVERSHOOTS the herd-immunity threshold h*=1−1/R0 — at R0=2.5, h*=0.60 but z*≈0.893, so ~29% of the population is infected UNNECESSARILY past the threshold.

> **State:** sim-ready
> **Class:** UNRELATED-domain (round-23 closer) · epidemiology — Kermack–McKendrick SIR final-size theory · fleet-external pure-mechanism head
> **Target:** sim-lab (VERDICT 117, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@1423b26 · fetched 2026-07-17T23:51:55Z
> **Source basis:** W. O. Kermack & A. G. McKendrick, "A Contribution to the Mathematical Theory of Epidemics," Proc. R. Soc. Lond. A 115 (1927) 700–721 — the SIR final-size equation and the epidemic threshold (standard textbook result; no external repo fetched).
> **Verifier (firsthand):** committed stdlib-only reference sim `ideas/fleet/epidemic_overshoot.py` (random, math, json, hashlib) — dry-sim exit 0, all gates PASS, results-dict sha256 2ecda33c…d4340c3f (see Verifier + Dry-sim below).

## The phenomenon (one line)
In an SIR epidemic with basic reproduction number R0>1, the herd-immunity threshold h*=1−1/R0 is the susceptible fraction at which transmission stops GROWING (the effective reproduction number R_eff=R0·S falls to 1) — but the epidemic does not stop there: the infections already in flight at that moment keep transmitting, driving the final attack rate to z*, the nonzero root of the Kermack–McKendrick final-size equation z=1−e^{−R0·z}, which strictly exceeds h* for every R0>1. At R0=2.5, h*=0.60 while z*≈0.893, so the epidemic OVERSHOOTS the threshold by ≈0.29 — nearly a third of the population is infected past the point where the disease was already dying out.

## The folk belief
"Once enough people are immune to reach herd immunity, the epidemic stops — so the final fraction infected is about the herd-immunity threshold, 1−1/R0." The threshold is real and widely cited, and it is genuinely the point where new cases stop RISING (the epidemic peak). The folk error is reading "cases stop rising" as "the epidemic ends here": planners size a vaccination target or a lockdown-release point at h*=1−1/R0 and expect the outbreak to fizzle at that attack rate.

## The thesis (reasoned to its fuller form — Q-0254 duty)
The herd-immunity threshold h*=1−1/R0 marks where the epidemic's GROWTH turns negative, not where its STATE settles — and for a cascade with in-flight momentum those two points are different. At the moment S first falls to 1/R0, the effective reproduction number R_eff=R0·S equals 1, so prevalence is at its PEAK: there is still a large, maximal pool of currently-infectious individuals. Each of them goes on to infect (on average) fewer than one further person, but "fewer than one each, from a peak-sized infectious pool" is still an enormous number of additional infections. Those post-threshold infections drive S well below 1/R0 before the infectious pool finally empties. Formally, the SIR dynamics conserve a quantity that yields the final-size equation: letting z be the total fraction ever infected, mass balance gives z = 1 − e^{−R0·z} (equivalently S_∞ = S_0·e^{−R0·z}). This transcendental equation has the trivial root z=0 and a nonzero root z*>h* whenever R0>1 — and z* is what the population actually reaches. The overshoot Δ = z* − h* is the fraction infected UNNECESSARILY, purely because transmission cannot be switched off the instant the threshold is crossed; the in-flight infectives carry the system past its own stopping line. The counterintuitive core: the threshold where growth stops (h*) and the level where the epidemic settles (z*) are strictly different, and the gap between them is large — at R0=2.5 the overshoot (0.29) is nearly as big as the "necessary" herd fraction minus its complement. Sizing an intervention at h* leaves the overshoot on the table.

## The formal model (committed constants — sim-lab must reproduce exactly)
- Stochastic Reed–Frost chain-binomial SIR on a homogeneously-mixing population of N=N_POP. Per-pair per-generation transmission probability q=R0/N; infectives are infectious for exactly one generation, then recover.
- Each generation with S susceptibles and I infectives: each susceptible independently escapes all I infectives with probability (1−q)^I, so is infected with probability p_inf = 1 − (1−q)^I; new infectives next generation ~ Binomial(S, p_inf); S decreases by that count; the epidemic ends when I=0.
- Seeded with I0 index cases. Epidemics are classified MAJOR (a real outbreak) vs MINOR (early stochastic fade-out) by a final-size cutoff MAJOR_CUTOFF; the closed-form final-size limit conditions on a major outbreak, so the gates use major outbreaks only.
- Analytic anchors (Kermack–McKendrick, large-N limit):
  - Herd-immunity threshold h* = 1 − 1/R0 (S=1/R0 ⇒ R_eff=1 ⇒ epidemic peak).
  - Final attack rate z* = nonzero root of z = 1 − e^{−R0·z} (equivalently z* = 1 + (1/R0)·W(−R0·e^{−R0}) via the Lambert W function; computed here by bisection).
  - Overshoot Δ = z* − h* > 0 for all R0 > 1.

## Pinned world (committed constants)
- SEED = 20260717 (proposal-owned; SEEDLESS discipline)
- R0 = 2.5 (basic reproduction number; favorable-epidemic regime R0>1)
- N_POP = 5000 (homogeneously-mixing population per epidemic)
- I0 = 1 (initial infectives / index cases)
- N_EPIDEMICS = 4000 (independent stochastic epidemics simulated)
- MAJOR_CUTOFF = 0.10 (final-size fraction separating major from minor outbreaks)
- SIGMA_GATE = 3.0 (pre-registered gate threshold in σ)
- Derived: h* = 1−1/R0 = 0.60, z* = 0.892645 (final-size root), overshoot Δ = z*−h* = 0.292645.

## Pre-registered gates (all ≥ 3σ; APPROVE iff ALL hold)
- **G1 — overshoot headline:** the measured final attack rate z_sim (mean over major outbreaks) exceeds the herd-immunity threshold h*=1−1/R0 by ≥ 3σ: (z_sim − h*)/se ≥ 3 AND z_sim > h*. The epidemic does NOT stop at herd immunity.
- **G2 — final-size anchor MATCH:** z_sim matches the closed-form final-size solution z* (nonzero root of z=1−e^{−R0·z}) within 3σ: |z_sim − z*|/se < 3. Confirms the stochastic sim reproduces the Kermack–McKendrick anchor (it is not measuring some other quantity).
- **G3 — post-threshold burn:** the mean fraction infected AFTER the susceptible pool first drops below 1/R0 (the herd threshold crossing) is ≥ 3σ above zero: burn_mean/se ≥ 3 AND burn_mean > 0. Demonstrates the MECHANISM — in-flight transmission past the threshold — not merely the magnitude.

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 ∧ G3 all hold at their stated thresholds on the pinned world with SEED=20260717 and the committed reference verifier. Any gate failing → REJECT (the overshoot / final-size claim is falsified for these constants). No post-hoc threshold moves; SEED is not changed; margins reported in σ.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
- Anchors: h_star = 0.6 · z_star = 0.892645 · overshoot_star = 0.292645
- Outbreak split: n_major = 3574, n_minor = 426 (major_frac = 0.8935 — matches the branching-process major-outbreak probability for R0=2.5, distinct from the naive 1−1/R0)
- z_sim (final attack rate, major outbreaks) = 0.892632 (se 0.000101) · overshoot_sim = z_sim − h* = 0.292632 (matches overshoot_star 0.292645 to 4 decimals)
- burn_post_threshold = 0.194675 (se 0.000869) — post-threshold burn measured from the DISCRETE crossing generation (whose end-of-generation cumulative already sits above h*, so this is a conservative lower bound on the continuous overshoot; the full overshoot is the z_sim−h* headline)
- **G1 overshoot:** z = 2883.28 — PASS (z_sim=0.892632 ≫ h*=0.6)
- **G2 anchor-match:** |z| = 0.13 — PASS (< 3σ; z_sim=0.892632 vs closed z*=0.892645)
- **G3 post-threshold burn:** z = 224.07 — PASS (burn=0.194675 > 0, ≥3σ)
- **all_pass = true; exit 0**
- **Disclosed results-dict sha256 = 2ecda33ccab80be04904c973478093bb50a51cde8e5964da9d35e1ca4d340c3f**

## Verifier
Stdlib-only python3 (`random, math, json, hashlib` — no numpy/scipy), committed alongside this idea as `ideas/fleet/epidemic_overshoot.py`. Seed once with SEED=20260717. It computes h*=1−1/R0 and the closed-form final size z* by bisection on z=1−e^{−R0·z}, then runs N_EPIDEMICS=4000 independent stochastic Reed–Frost chain-binomial SIR epidemics on N_POP=5000 (Binomial draws by an exact geometric-gap sampler — no third-party RNG), records each epidemic's final attack rate and its cumulative infected fraction at the first generation past the herd threshold, keeps the major outbreaks (final size ≥ MAJOR_CUTOFF), computes means and standard errors, evaluates G1/G2/G3, and emits a canonical (sorted-keys, comma/colon-separated) results JSON with its sha256. Exit 0 iff all gates pass.

Reproduce:

```
python3 ideas/fleet/epidemic_overshoot.py
```

Expected: all_pass=true, exit 0, h_star=0.6, z_star=0.892645, results-dict sha256 = 2ecda33ccab80be04904c973478093bb50a51cde8e5964da9d35e1ca4d340c3f.

## Why it matters (transferable mechanism)
Any self-limiting cascade with in-flight momentum overshoots its own stopping threshold: the level at which GROWTH turns negative (a reproduction number, a utilization ratio, a fill fraction crossing 1) is not the level at which the system SETTLES, because the units already committed keep acting after the crossing. The correct sizing anchor is the fixed point of the FULL dynamics (here z*, the final-size root), not the growth-stops threshold (here h*). The transferable audit: whenever a cutoff, quota, kill-switch, or intervention target is set at "the point where the thing stops getting worse," ask what is still in flight at that moment — the in-flight fraction determines an overshoot that carries the system strictly past the line, and the true settling point lies beyond. As a fleet-external pure-mechanism head there is NO lane build here; the deliverable is a citable measured verdict plus the "size by the settling fixed point, not the growth-stops threshold — account for the overshoot" correction.

## Dedup
Distinct from the nearby priors:
- **kelly-overbet-ruin** (P100, the round-22 UNRELATED closer): a repeated-MULTIPLICATIVE-betting interior-optimum / ensemble-vs-time-average trap in information theory / mathematical finance. This head is a self-limiting EPIDEMIC cascade whose settling point overshoots a growth-stops threshold — a different domain (epidemiology / Kermack–McKendrick final-size theory), a different object (a transcendental final-size fixed point z=1−e^{−R0 z}, not a log-growth argmax), and a different counterintuition (a threshold-vs-settling gap, not an arithmetic-vs-geometric mean gap). This is the mandated NEW unrelated domain, not a P100 re-skin.
- **schelling-mild-preference-tipping** (P-era) / **braess-selfish-routing-trap** (P092): a segregation tipping model and a congestion-game routing paradox — neither prices an SIR final size or a herd-immunity overshoot.
- **metastable-retry-storm-collapse** / **round-robin-domain-starvation-cliff**: threshold-crossing collapse dynamics, but retry-queue/scheduler models, not an epidemic final-size equation; the transferable "overshoot past a stopping line" template names them as candidate future heads, distinct from this measured SIR verdict.
- No prior idea in the tree models an SIR/epidemic process, the herd-immunity threshold 1−1/R0, or the Kermack–McKendrick final-size equation; grep of the full ideas/ tree + outbox history returns no epidemic/SIR/herd-immunity/final-size head.

## Model basis (declared model-dependence — the P024 discipline)
The overshoot z*>h* and its magnitude DO depend on structural assumptions: (a) a single closed, homogeneously-mixing population (no births/deaths, no spatial or network structure, no re-susceptibility); (b) a standard SIR generation structure (one infectious period, permanent immunity); (c) R0>1 and a large enough population for the deterministic final-size limit to govern (finite-N stochastic corrections are O(1/N) in the conditional mean and vanish in the gates via the anchor-match tolerance). Under a network or metapopulation structure the final size changes quantitatively (and the threshold shifts), and with waning immunity the "final size" is replaced by an endemic level — but the qualitative overshoot (settling point strictly beyond the growth-stops threshold) is robust wherever a self-limiting cascade has in-flight momentum. The claim is scoped: under the closed homogeneous SIR model with R0>1, the herd-immunity threshold h*=1−1/R0 and the final attack rate z* (root of z=1−e^{−R0 z}) are strictly different, z*>h*, demonstrated on the pinned constants, mechanism-explained, not asserted as a universal law.

## Probe report (v0, 2026-07-17)

**1. What is this really?** A Kermack–McKendrick final-size claim: in a closed homogeneous SIR epidemic with R0=2.5, the fraction ever infected z* (nonzero root of z=1−e^{−R0·z}≈0.893) strictly EXCEEDS the herd-immunity threshold h*=1−1/R0=0.60 — the epidemic overshoots the threshold at which growth already stopped, because infections in flight at the crossing keep transmitting.
**2. What would make it false?** If a stochastic SIR simulation's mean final attack rate (over major outbreaks) settled AT h*=0.60 rather than at z*≈0.893, or failed to reproduce the closed-form final-size root z*, or if there were no measurable transmission after the herd threshold is crossed. Any of G1/G2/G3 failing → REJECT.
**3. Simplest version that still bites?** SEED=20260717, R0=2.5, N_POP=5000, 4000 independent Reed–Frost chain-binomial epidemics from I0=1; keep major outbreaks (final size ≥10%); compare their mean final attack rate to h* (G1) and to z* (G2), and measure the fraction infected after the herd-threshold crossing (G3).
**4. What is the counterintuitive core?** The herd-immunity threshold h*=1−1/R0 is the epidemic PEAK (where R_eff=1 and prevalence is maximal), not the epidemic END. From that maximal infectious pool, "each infects fewer than one further" still adds a huge number of infections — the final size z*≈0.893 overshoots h*=0.60 by ≈0.29, so ~29% of the population is infected purely as overshoot past the point the disease was already receding.
**5. Where could I be fooling myself?** Minor (early-fadeout) outbreaks would deflate the mean if not separated — handled by the MAJOR_CUTOFF split (n_minor=426 discarded, the branching major-outbreak fraction 0.8935 matches theory). Finite-N stochastic bias could in principle trip the anchor match — but the sim reproduces z* to 4 decimals (|z|=0.13σ), well inside G2's 3σ. The post-threshold burn (0.1947) is measured from the DISCRETE crossing generation, whose cumulative already exceeds h*, so it is a conservative lower bound on the continuous overshoot; the headline overshoot is the z_sim−h*=0.2926 match to the closed form.
**6. What is the honest calibration?** Dry-sim margins at SEED=20260717: G1 overshoot z=2883.28σ (z_sim=0.892632 vs h*=0.6), G2 anchor |z|=0.13σ (z_sim=0.892632 vs closed z*=0.892645), G3 post-threshold burn z=224.07σ (burn=0.194675>0) — all clear the ≥3σ bar; exit 0; results-dict sha256 2ecda33c…d4340c3f. h*=0.60, z*=0.892645, overshoot 0.292645.
**7. What decision does it change?** Size a vaccination target, a lockdown-release point, or any self-limiting-cascade cutoff by the SETTLING fixed point (final size z*), not by the growth-stops threshold (herd immunity h*=1−1/R0) — and budget for the overshoot, the fraction infected/committed unnecessarily after the line is crossed. Reaching herd immunity through natural infection is not "the end"; it is the halfway-through-the-overshoot mark.
**8. How will we know it worked?** The committed stdlib verifier reproduces z_sim(major) ≈ z* within 3σ, z_sim > h* by ≥3σ, and positive post-threshold burn ≥3σ, with the results-dict sha256 matching 2ecda33ccab80be04904c973478093bb50a51cde8e5964da9d35e1ca4d340c3f.

**Recommendation: sim-ready**
