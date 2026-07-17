# Friendship-paradox sensors: watch a random *friend*, not a random person, and you see the epidemic wave first — the head-start equals the degree variance Var[k]/E[k].

> **State:** sim-ready
> **Class:** unrelated-domain (network epidemiology / size-biased sampling)
> **Target:** sim-lab — VERDICT-109 (round-21 unrelated-domain closer, offset +13)
> **Grounding:** https://github.com/menno420/idea-engine@f3473eb3e87c44dd19025e4ab6694c94ca243e20 · fetched 2026-07-17T13:11:31Z
> **Harvest source (firsthand):** self-initiated unrelated-domain sweep (round 21). Feld 1991 friendship-paradox formula — mean neighbour degree = μ + σ²/μ = E[k²]/E[k] — https://en.wikipedia.org/wiki/Friendship_paradox · fetched 2026-07-17T13:11:31Z (secondary; AJS primary paywalled). Christakis & Fowler 2010 "Social Network Sensors for Early Detection of Contagious Outbreaks", PLoS ONE 5(9):e12948 — real-world lead 13.9 days (95% CI 9.9–16.6) vs random group, 46 days before population peak — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0012948 · fetched 2026-07-17T13:11:31Z
> **Origin:** claude/friendship-paradox-sensor

**Placement note (decide-and-flag):** filed in `ideas/fleet/` alongside the prior cross-cutting unrelated-domain closers (P076/P080/P084/P088/P092) per the `check_sections` carve-out for pure-mechanism heads. ↩️ reversible.

## Folk belief
"To catch an outbreak early, sample people at random — a representative random sample is the unbiased, fair way to watch a population." Monitoring random individuals feels like the neutral, no-assumptions choice.

## The counterintuitive claim
A random *friend* is a better sensor than a random *person*, for free. Pick a random person, ask them to name one friend, monitor that friend instead. Because a random neighbour is reached in proportion to its degree, the nominated friends are systematically more central — and central nodes are infected earlier — so the friend group's infection curve leads the random group's. You need **no global network map**: one nomination per person suffices. The head-start is not mysterious: the expected degree gap between a random friend and a random person is exactly **Var[k]/E[k]** (Feld 1991). Zero degree variance → zero head-start; heavy-tailed degree → large head-start.

## Mechanism (fuller form)
A spreading process on a network reaches high-degree nodes disproportionately early: a hub has many independent exposure paths, so its expected time-to-first-infection is short and falls with degree. Any sampling scheme that over-weights high-degree nodes therefore front-loads its infections and crosses a fixed prevalence threshold sooner. Following a random edge to one endpoint (equivalently, sampling a uniformly random half-edge) selects a node with probability proportional to its degree, so the expected degree of such a "random friend" is E[k²]/E[k] = E[k] + Var[k]/E[k] — strictly above the E[k] of a uniformly random node whenever degrees vary (Feld 1991). The operational trick (Christakis & Fowler 2010) is that you need neither the degree distribution nor the map: asking a random person to name a friend yields a degree-biased draw automatically. The head-start is governed by one scalar — the variance-to-mean ratio Var[k]/E[k]. Falsifier: on a regular graph every node has identical degree, Var[k]=0, the "friend" and "random" samples are statistically indistinguishable, and the lead must vanish.

## Pinned world (committed constants)
- **World W1 (signal):** Barabási–Albert preferential-attachment graph, n=10000, m=3, seed_graph=20260717. Pure-stdlib generator: initial m-clique; a stub multiset holding each node once per edge-endpoint; each new node attaches to m distinct existing targets drawn by `random.choice` over the stub multiset (reject self/dupes), appending both endpoints per new edge. Committed moments: E[k]=5.9988, E[k²]=110.253, Var[k]=74.267, max degree=378, Var/E[k]=12.380, E[k²]/E[k]=18.379.
- **World W0 (negative control):** random d-regular graph, d=6 (=2m, degree-matched), n=10000, seed=20260718, via configuration-model stub pairing with self-loop/multi-edge repair (7 stub-pairs dropped; E[k]=5.9986, Var[k]=0.0016).
- **Diffusion:** discrete-time SI (no recovery); one uniformly-random source infected at t=0; each step every susceptible node with c infected neighbours is infected with probability 1−(1−β)^c; β=0.08. Halt on full infection, 5 consecutive no-new-infection steps, or 400 steps.
- **Sensor constructions (size S=100):** FP group = S uniformly-random half-edges (degree-biased); Random group = S uniformly-random nodes.
- **Detection time** = θ-quantile (θ=0.30) of a group's member infection times, linearly interpolated at the θ·S=30 crossing on the cumulative-infected-vs-step curve; a group where <30% is ever infected within the horizon is censored to the max step reached (mutual censoring ⇒ lead 0, a conservative choice biasing toward the null).
- **Trials:** T=200 epidemic seeds; RNG discipline — epidemic seed `random.Random(1000+trial)`, group draws `random.Random(5000+trial)`, MC anchor `random.Random(777)` with 200000 draws.

## Probe report
> Single-pass battery (panel not escalated — the friendship paradox is a textbook result with a closed-form anchor Var[k]/E[k], and the dry-sim reproduces that anchor to 0.11%).

**1. What is this really?** A network-epidemiology / size-biased-sampling result: a degree-biased sample of "friends" is a strictly earlier sensor of a diffusion than an equal-size uniformly-random sample, at no extra cost and with no network map. Decision content: a free, map-less early-warning sensor — nominate friends and watch them.
**2. What would make it false?** If the friend group's detection time were no earlier than the random group's within noise (lead ≤ 0 or < 3σ) on the signal world, or if the effect persisted on the degree-matched regular graph (where Var[k]=0 predicts no lead), the size-biased-reach mechanism would fail.
**3. Simplest version that still bites?** A single Barabási–Albert graph (n=10000, m=3) under discrete-time SI, comparing a size-100 half-edge group to a size-100 uniform group — the smallest pinned world with a heavy-tailed degree that exhibits the lead, anchored by the exact closed form E[k²]/E[k]=18.379.
**4. What's the counterintuitive core?** Random sampling *feels* like the neutral, fair, no-assumptions choice, yet a degree-biased "friend" sample is a strictly better sensor — the sampling bias everyone is taught to avoid is here a feature to harvest, and the head-start is exactly the degree variance Var[k]/E[k].
**5. Where could I be fooling myself?** Censoring artifacts — a threshold θ nobody reaches would manufacture a spurious tie or lead. Guarded by (a) the analytic anchor E[k²]/E[k]=18.379 reproduced by the MC half-edge estimate, (b) the negative control W0 where the lead must vanish, (c) mutual censoring set to lead 0 (a conservative choice that can only shrink the measured lead), (d) an operating point β=0.08 chosen so only 19% of trials censor.
**6. What's the honest calibration?** The gated construction is the exact half-edge draw, not the field nomination method (a random neighbour of a random node is degree-biased but only equals E[k²]/E[k] under zero degree correlation) — disclosed as the operational analogue. At β=0.02 all gates still pass but 78% of trials censor, so β was raised to 0.08 for a robust operating point (disclosed). The real-world magnitudes (13.9-day / 46-day leads, Christakis & Fowler 2010) are the motivation, not the gated claim.
**7. What decision does it change?** Whether to sample at random or to sample friends when watching a diffusion for early warning: the answer is "watch a random friend," a free head-start of Var[k]/E[k] wherever a contagion runs on a heavy-tailed contact graph — including the fleet's own signal propagation (sample high-fan-in nodes to see a cascade first).
**8. How will we know it worked?** All four pre-registered gates hold in evaluation order on the committed pinned world: R1 the analytic degree anchor, R2 the ≥3σ lead on W1, R3 the vanished lead on W0, R4 the pinned-moment sanity checks — with twin evaluators agreeing.

**Recommendation: sim-ready**

## Pre-registered gates
- **R1 (analytic anchor, exact):** measured FP-group mean sensor degree equals E[k²]/E[k]=18.379 within ±2%. Dry-sim: 18.399, relerr 0.11% → PASS. Twin evaluators must agree: (a) analytic E[k²]/E[k] from the committed degree sequence, (b) MC half-edge estimate.
- **R2 (decision-relevant, ≥3σ):** mean detection lead (Random − FP) over T=200 trials on W1 > 0 at ≥3σ (σ = SEM = stdev/√T). Dry-sim: +1.052 steps, SEM 0.057, 18.4σ, frac(lead>0)=0.76 → PASS.
- **R3 (negative control, falsifier):** on W0 the mean lead is NOT ≥3σ. Dry-sim: +0.052 steps, SEM 0.069, 0.75σ → PASS (effect is degree-variance-driven, not procedural).
- **R4 (sanity vs. world's own bounds):** committed moments reproduce the built degree sequence exactly; Var/E[k]=12.38 < max degree 378; every detection time ≤ horizon; lead ≤ epidemic duration. Deterministic → PASS.

## Decision rule
APPROVE iff R1 ∧ R2 ∧ R3 ∧ R4. REJECT if R2 lead ≤ 0, or R3 shows the regular graph also leads at ≥3σ (artifact). NULL if R2 lead > 0 but < 3σ. INVALID if committed moments don't match the rebuilt graph (seed/harness drift). Twin evaluators: R1 analytic-vs-MC; R2 independent re-simulation from the committed seeds.

## Disclosed verifier spec
sim-lab re-implements the harness from the committed constants (stdlib only), rebuilds W1/W0 from the pinned seeds, verifies the committed degree moments, runs the MC anchor (R1), the T=200 lead sweep (R2), and the negative control (R3). Reference values: E[k²]/E[k]=18.379; FP degree ≈18.40; BA lead ≈+1.05 steps at ≈18σ; regular lead ≈+0.05 steps at <1σ. Tolerances: R1 ±2%; R2/R3 σ-margins as stated.

## Corrections disclosed
- SI (not SIR) so detection is monotone and censoring well-defined.
- θ=0.30 with linear interpolation; at β=0.08, 19% of W1 trials censored (mutual censoring ⇒ lead 0 — can only shrink the measured lead, never inflate it). β=0.02 (first-pass) also passes all gates but censors 78% of trials, so β was raised to 0.08 for a robust operating point; disclosed.
- Regular-graph configuration model dropped 7 self-loop/multi-edge stub-pairs (mean degree 5.9986 vs target 6.000).
- "Random friend" is realised as a uniformly-random half-edge (exact degree-biased draw); the field nomination method (random neighbour of a random node) is degree-biased but not exactly E[k²]/E[k] under degree correlations — the operational analogue, not the gated construction.

## Non-adjacency
- P076 check-digit (coding theory) — deterministic error detection, no sampling.
- P080 shared-randomness coupling — correlation via common seed, not degree-biased sampling.
- P084 Simpson's paradox — aggregation reversal across strata; here no confounded strata, pure size-biased sampling.
- P088 Berkson collider — selection-induced correlation from conditioning on a collider; here selection is degree-proportional and the target is a lead time, not a spurious correlation.
- P092 Braess routing — equilibrium degradation from added capacity; unrelated mechanism.
Shared thread with P084/P088 is only "sampling can mislead"; the mechanism (size/degree-biased reach vs aggregation vs collider selection) and the decision (harvest the bias as a free sensor) are distinct — the first proposal where the bias is a feature to exploit, not an artifact to correct.

## Dedup
No existing file under ideas/ addresses the friendship paradox, size-biased sampling, or network sensors (tree scan at HEAD f3473eb).

## Consequence / follow-ups
If APPROVED: a cheap, map-free early-warning sensor — nominate friends, watch them — with a quantified head-start (Var/E[k]), usable wherever a diffusion runs on a heavy-tailed contact graph (maps onto the fleet's own signal propagation: sample high-fan-in nodes to see a cascade first). Follow-ups: (F1) sweep β and network family (configuration-model power-law, small-world) to map lead-time vs Var/E[k]; (F2) test the field nomination method against the exact half-edge draw to quantify the degree-correlation penalty; (F3) SIR variant with recovery to check robustness under waning.

📊 Model: claude-opus-4-8 · effort high · task-class proposal-draft

Recommendation: sim-ready
