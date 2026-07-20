# Ski-rental keep-warm — no fixed autoscaling policy is safe, but the break-even rule is 2-competitive in every idle regime

> **State:** sim-ready
> **Class:** online algorithms · ski-rental competitive analysis · counterintuitive · round-45 FLEET slot · PROPOSAL 189 → VERDICT 202 (+13)
> **Target:** sim-lab (VERDICT 202, +13 offset)
> 📊 Model: Claude Opus · high · idea/planning
> **Grounding:** https://en.wikipedia.org/wiki/Ski_rental_problem@f6919be · fetched 2026-07-20
> **Reference (external, reachable):** [Ski rental problem — Wikipedia](https://en.wikipedia.org/wiki/Ski_rental_problem) — verified reachable 2026-07-20 via WebFetch (HTTP 200). Quote: "The break-even algorithm is known to be the best deterministic algorithm for this problem." and, for the randomized rule: "Its expected cost is at most e/(e-1) ≈ 1.58 times (when b tends to infinity) what one would pay if one had known the number of days one would go skiing." The page documents the break-even (rent-until-break-even-then-buy) strategy and the randomized e/(e−1) ≈ 1.58 optimum; the deterministic worst-case 2× bound is the standard textbook competitive ratio (the page's worked example lands at 1.9×, approaching 2× as B grows).
> **Verifier (firsthand):** ideas/fleet/ski_rental_keep_warm.py · results-dict sha256 0a0464162b20350c6d07104fed5bf62f1578021be85c0ecba18b4b07a3964c2b

## The phenomenon (one line)

For an autoscaled / keep-warm resource you cannot safely pick a fixed policy: "always keep warm" wastes unbounded idle cost when requests are sparse, "always tear down" pays unbounded cold-start cost when requests are frequent, yet the ski-rental break-even rule — keep warm exactly until accumulated idle cost equals the cold-start cost B, then tear down — stays within 2× of the clairvoyant optimum in EVERY idle regime.

## Domain

Online algorithms / competitive analysis applied to fleet ops: autoscaling keep-alive, connection-pool idle timeouts, serverless keep-warm. The round-45 FLEET slot.

## The folk belief

"Pick the policy that fits your load: if the box is usually busy, keep it warm; if it's usually idle, tear it down." The belief is that a single fixed always-on / always-off choice, tuned to the typical load, is good enough. It is not — each fixed policy is *unboundedly* wasteful in the regime it was not tuned for, and load is exactly the thing you do not know in advance.

## The thesis (reasoned to its fuller form — Q-0254 duty)

Model one idle gap as a ski-rental instance. Renting = paying 1 per unit time to keep the instance warm; buying = paying the cold-start cost B once (here the spin-up you incur if you tore down and the next request arrives). The clairvoyant optimum for an idle gap of length t is OPT = min(t, B): if you knew the gap were short you would stay warm (cost t), if you knew it were long you would tear down immediately (cost B). You do not know t. The break-even rule keeps warm while the running idle bill is below B and tears down the instant it reaches B, paying at most 2B on any gap — B of rent then B of cold-start — which is at most twice OPT for every t. That is the classic 2-competitive guarantee, and it holds pointwise, with no distributional assumption. The two fixed policies have no such bound: always-warm pays t, which is t/B times OPT and diverges as gaps grow; always-cold pays B, which is B/t times OPT and diverges as gaps shrink. Averaged over exponential idle with mean = B, the break-even rule's expected cost lands at the ski-rental landmark e/(e−1) ≈ 1.582× the optimum. Fleet lesson: set the keep-warm idle timeout equal to the cold-start cost; it dominates any fixed always-on / always-off choice across unknown load.

## The formal model / Pinned world (committed constants)

- Cold-start (spin-up) cost B = 1.0; rent cost = 1 per unit idle time.
- R = 200000 Monte-Carlo idle draws per arm.
- Idle regimes: short (Exponential mean 0.2B), matched (Exponential mean B), long (Exponential mean 5B); robustness arm = hyperexponential mean B (p = 0.5, component means 0.2B and 1.8B).
- Per-instance costs for idle duration t: OPT = min(t, B) (clairvoyant); break-even = t if t < B else 2B; always-warm = t; always-cold = B.
- Competitive ratio reported per arm as ratio-of-means (mean policy cost / mean OPT).
- SEED = 20260717; z_gate = 3.0.

## Pre-registered gates

- **G1 — long-idle, always-warm blows up.** In the long regime (μ = 5B), always-warm's mean competitive ratio > 2 while break-even's stays < 2, and the paired per-instance (warm − break-even) cost gap is positive at z ≥ 3.
- **G2 — short-idle, always-cold blows up.** In the short regime (μ = 0.2B), always-cold's mean competitive ratio > 2 while break-even's stays < 2, and the paired per-instance (cold − break-even) cost gap is positive at z ≥ 3.
- **G3 — matched constant + shift robustness.** In the matched regime (μ = B) the break-even mean competitive ratio equals e/(e−1) ≈ 1.582 within 2%, and under a hyperexponential idle of the same mean the break-even ratio stays < 2 with the paired (cold − break-even) gap at z ≥ 3.
- all_pass = G1 ∧ G2 ∧ G3.

## Pre-registered decision rule

sim-ready iff the verifier reproduces byte-identical results-dict sha256 with all_pass = true and G1 ∧ G2 ∧ G3 holding.

## Dry-sim results (SEED=20260717, verbatim from ideas/fleet/ski_rental_keep_warm.py)

- **G1 long-idle (μ = 5B):** break-even ratio_be = 1.903787 (< 2 ✓); always-warm ratio_warm = 5.522566 (> 2 blowup); paired (warm − break-even) mean = +3.281912, **z = 306.250137** → PASS.
- **G2 short-idle (μ = 0.2B):** break-even ratio_be = 1.033101 (< 2 ✓); always-cold ratio_cold = 5.030524 (> 2 blowup); paired (cold − break-even) mean = +0.794634, **z = 1524.124639** → PASS.
- **G3 matched (μ = B) + shift:** break-even ratio_be_match = 1.579541 vs e/(e−1) = 1.581977, rel_err = 0.00154 (< 2% ✓); hyperexponential-mean-B robustness arm ratio_be_hyper = 1.601131 (< 2 ✓), z_hyper = 124.186516 → PASS.
- all_pass = **true**; results-dict sha256 = 0a0464162b20350c6d07104fed5bf62f1578021be85c0ecba18b4b07a3964c2b (byte-identical across two fresh invocations).

## Reproduce

```
python3 ideas/fleet/ski_rental_keep_warm.py
```

## Verifier

ideas/fleet/ski_rental_keep_warm.py — stdlib-only (hashlib, json, math, random); deterministic in-process double-run with an equality assert; digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY.

## Why it matters

The failure mode is general: for an online idle-timeout decision under unknown future load, no fixed rule is safe — every always-on / always-off choice is unboundedly wasteful in the regime it was not tuned for. The break-even rule (timeout = cold-start cost) is a single setting that stays within 2× of clairvoyant everywhere, and near the natural scale (idle mean ≈ cold-start cost) it costs only ≈ 1.58×. Wherever a fleet holds a warm resource against an uncertain next arrival — a keep-alive connection, a pooled worker, a serverless instance — this says set the idle timeout to the spin-up cost rather than betting on a load guess.

## Dedup

Ran `git -C . grep -il "ski"`: every hit is substring noise — "skills", "known-risks", "Buchholz", etc. — with no ski-rental head. Ran `git -C . grep -il "keep-warm"`: the only hit is this proposal's own session card (the new head itself); no prior keep-warm head exists. A full ideas/fleet/ inventory scan found no ski-rental / autoscaling keep-warm / competitive-analysis-timeout head. Distinct from checkpoint-interval-optimum work (Young–Daly checkpoint spacing minimizes expected lost compute — an offline expected-cost optimization, not an online per-gap competitive decision) and from metastable-retry-storm-collapse (a retry-feedback bistability, not an idle-timeout online decision). Two earlier P189 drafts were dropped for dedup before this one: a poll-jitter inspection-paradox head (collides with the shipped `inspection-paradox-wait-inflation-2026-07-14.md`) and a coupon-collector coverage-tail head (collides with the shipped `coupon-collector-tail-2026-07-14.md`, P052). This ski-rental / keep-warm head is the shipped, unoccupied lane.

## Model basis (declared model-dependence — the P024 discipline)

Honest caveats. (1) G1/G2 report ratio-OF-MEANS competitive ratios and paired per-instance z-gaps — these are averaged blowups and a significance test on the per-gap cost difference, NOT the worst-case pointwise bounds; the pointwise 2-competitive guarantee is the theory, the sim shows the average consequence. (2) The e/(e−1) ≈ 1.582 landmark reported at G3 is the matched-regime ratio-of-means (average-case at idle-mean = B), which numerically coincides with — but is conceptually distinct from — the classic randomized worst-case e/(e−1) competitive ratio on the page; do not read the matched-regime average as the adversarial bound (probes 4, 5). (3) The model is per-request oblivious with a fixed cold-start B and a clean binary warm/cold; variable spin-up (probe 1), a per-request warm-hit latency benefit (probe 6), and partial spin-down/spin-up costs (probe 8) are outside it. (4) The finite-mean assumption underwrites the average ratios; heavy-tailed (Pareto) idle can break it (probe 7).

## Probe report (v0, 2026-07-20)

**1. Does the 2-competitive guarantee survive when the cold-start cost B itself is random (variable spin-up time) rather than a fixed constant?** The pointwise 2× bound is stated for a known B; with random B the break-even threshold must be set against E[B] (or a realized draw), and the guarantee holds in expectation only if the threshold tracks the actual spin-up — an untested extension flagged in the model basis, not claimed here.

**2. If idle durations are autocorrelated (bursty arrivals), does the per-instance break-even rule still bound regret, or does a predictive warm-pool win?** The competitive bound is per-gap and needs no independence, so it still holds gap-by-gap; but under strong autocorrelation a predictor that anticipates the next gap can beat oblivious break-even in expectation. The 2× ceiling survives; the average can be improved.

**3. Where is the crossover — for what idle-mean μ/B does always-warm's expected cost first exceed break-even's by 2×?** In our arms always-warm's ratio-of-means is already 5.52 at μ = 5B and break-even is 1.90; the crossover where always-warm's expected cost exceeds break-even's is well below μ = 5B — probe 3 is the pinned question for a follow-up sweep, not resolved by the three pinned points here.

**4. Does the randomized threshold (e/(e−1) ≈ 1.582) beat the deterministic break-even in expectation over a realistic idle distribution, or only against an adversary?** The e/(e−1) randomized rule is optimal against an *adversary*; over a benign realistic distribution the deterministic break-even can match or beat it. Our matched-regime 1.5795 is an average-case coincidence with the adversarial constant, not evidence the randomized rule wins on average.

**5. For a POOL of K warm instances with correlated idle, does aggregating the break-even rule across the pool change the competitive ratio?** Applied per-instance the bound composes trivially (each instance is ≤ 2× its own OPT, so the pool is ≤ 2× pool-OPT); a pool-aware policy exploiting cross-instance correlation could do better on average, an open extension.

**6. How does a per-request warm-hit benefit (latency saved) not captured in the rent/cold-start cost model shift the optimal timeout below B?** A latency reward for staying warm adds value to renting, which pushes the break-even threshold *above* B (keep warm longer); a penalty for holding capacity pushes it below B. The clean B threshold is optimal only for the pure rent/cold-start cost model.

**7. Under a heavy-tailed (Pareto) idle distribution, does the finite-mean assumption hold, and does the 2-competitive bound degrade?** The pointwise 2× bound is distribution-free and survives any idle law, heavy-tailed or not. The *average* ratios (and the e/(e−1) landmark) rely on a finite mean; a Pareto with index ≤ 1 breaks the finite-mean averages while leaving the worst-case guarantee intact.

**8. Does charging a partial spin-down / spin-up cost (not a clean binary) preserve the break-even structure or introduce a dead-band?** A partial/continuous spin cost turns the sharp break-even threshold into a hysteresis dead-band (tear down only past B + δ, spin up only past a lower mark), preserving the break-even *structure* but widening it — outside the clean binary model here.

**Recommendation: sim-ready**
