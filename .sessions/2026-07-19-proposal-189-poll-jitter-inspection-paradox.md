# PROPOSAL 189 — Ski-rental keep-warm: no fixed autoscaling policy is safe, but the break-even rule is 2-competitive in every idle regime (round-45 FLEET slot, P189 → V202, +13)

> **Status:** complete
> 📊 Model: Claude Opus · high · idea/planning
>
> Born-red HOLD: this card lands born-red (`in-progress`) to hold the PR red on the first commit. It flips to `complete` as the last commit, after the verifier reproduces a byte-identical results-dict sha256 and all gates pass.

## Objective
Show that for an autoscaled / keep-warm resource (a serverless instance, a pooled connection) neither fixed policy is safe: "always keep warm" wastes unbounded idle cost when requests are sparse, and "always tear down" pays unbounded cold-start cost when requests are frequent — each blows the 2× budget in the wrong idle regime. The ski-rental break-even rule — keep warm exactly until accumulated idle cost equals the cold-start cost B, then tear down — is provably within 2× of the clairvoyant optimum in EVERY regime, and averaged over exponential idle with mean = B it costs e/(e−1) ≈ 1.582×. Fleet lesson: set the keep-warm idle timeout equal to the cold-start cost; it dominates any fixed always-on / always-off choice across unknown load.

## Constraints honored
- stdlib-only verifier (hashlib, json, math, random); SEED = 20260717 pinned.
- deterministic in-process double-run with an assert; cross-invocation byte-identical results-dict sha256.
- ≥3σ gates: G1 long-idle always-warm blowup, G2 short-idle always-cold blowup, G3 matched-regime e/(e−1) constant + hyperexponential robustness.
- DIGEST-POSTURE: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY; the compact-canonical results-dict sha256 IS the digest; stdout prints the pretty dump (indent=2) with floats at 6 dp; no on-disk JSON.

## Pinned world
- Cold-start cost B = 1.0; rent cost = 1 per unit idle time; R = 200000 Monte-Carlo idle draws per arm.
- Idle regimes: short (Exponential mean 0.2B), matched (Exponential mean B), long (Exponential mean 5B); robustness arm = hyperexponential mean B (p=0.5, component means 0.2B and 1.8B).
- Policies scored against the clairvoyant optimum OPT = min(idle, B): break-even (warm to B then tear down), always-warm, always-cold.

## Gate-plan (pre-registered)
- **G1 long-idle:** in the long regime, always-warm's mean competitive ratio > 2 while break-even's stays < 2, and the paired per-instance (warm − break-even) cost gap is positive at z ≥ 3.
- **G2 short-idle:** in the short regime, always-cold's mean competitive ratio > 2 while break-even's stays < 2, and the paired per-instance (cold − break-even) cost gap is positive at z ≥ 3.
- **G3 matched + shift:** in the matched regime the break-even mean competitive ratio equals e/(e−1) ≈ 1.582 within 2%, and under a hyperexponential idle of the same mean the break-even ratio stays < 2 with the paired (cold − break-even) gap at z ≥ 3.
- all_pass = G1 ∧ G2 ∧ G3.

## GROUNDING (verified live)
> **Grounding:** https://en.wikipedia.org/wiki/Ski_rental_problem@f6919be · fetched 2026-07-20

Reference (external, reachable): "Its expected cost is at most e/(e-1) ≈ 1.58 times (when b tends to infinity) what one would pay if one had known the number of days one would go skiing." — Ski rental problem, Wikipedia (HTTP 200, verified 2026-07-20); the page also states "The break-even algorithm is known to be the best deterministic algorithm for this problem."

## Probe questions
**1. Does the 2-competitive guarantee survive when the cold-start cost B itself is random (variable spin-up time) rather than a fixed constant?**
**2. If idle durations are autocorrelated (bursty arrivals), does the per-instance break-even rule still bound regret, or does a predictive warm-pool win?**
**3. Where is the crossover — for what idle-mean μ/B does always-warm's expected cost first exceed break-even's by 2×?**
**4. Does the randomized threshold (e/(e−1) ≈ 1.582) beat the deterministic break-even in expectation over a realistic idle distribution, or only against an adversary?**
**5. For a POOL of K warm instances with correlated idle, does aggregating the break-even rule across the pool change the competitive ratio?**
**6. How does a per-request warm-hit benefit (latency saved) not captured in the rent/cold-start cost model shift the optimal timeout below B?**
**7. Under a heavy-tailed (Pareto) idle distribution, does the finite-mean assumption hold, and does the 2-competitive bound degrade?**
**8. Does charging a partial spin-down / spin-up cost (not a clean binary) preserve the break-even structure or introduce a dead-band?**

## Outcome
Verifier reproduced byte-identical stdout across two separate processes; results-dict sha256 = `0a0464162b20350c6d07104fed5bf62f1578021be85c0ecba18b4b07a3964c2b`.
- **G1 long-idle (μ=5B):** break-even ratio-of-means 1.903787 (< 2 ✓), always-warm 5.522566 (> 2 blowup), paired (warm − break-even) gap +3.281912 at z = 306.250137.
- **G2 short-idle (μ=0.2B):** break-even ratio-of-means 1.033101 (< 2 ✓), always-cold 5.030524 (> 2 blowup), paired (cold − break-even) gap +0.794634 at z = 1524.124639.
- **G3 matched (μ=B) + shift:** break-even ratio-of-means 1.579541 vs e/(e−1) = 1.581977, rel_err 0.00154 (< 2% ✓); hyperexponential-mean-B robustness arm break-even ratio 1.601131 (< 2 ✓) at z_hyper = 124.186516.
- all_pass = **true** (G1 ∧ G2 ∧ G3).

## ⟲ Previous-session review
Round-44 closed with P188 (population momentum, UNRELATED slot → V201, +13). The rotation is fleet → venture → game → unrelated; this card opens round-45 in the FLEET slot (P189 → V202). Two earlier drafts of this slot were dropped at the dedup gate: a poll-jitter inspection-paradox head (collides with the shipped `inspection-paradox-wait-inflation-2026-07-14.md`) and a coupon-collector coverage-tail head (collides with the shipped `coupon-collector-tail-2026-07-14.md`, P052). A full ideas/fleet/ inventory scan confirmed the ski-rental / autoscaling keep-warm lane is unoccupied, so this is the shipped head. Sibling V201 and its mirror run concurrently, so rebase-and-union before each push.

## 💡 Session idea
Companion head for a later slot: a predictive keep-warm that blends a cheap idle-duration forecast between break-even and always-warm — quantify how much regret below 2× a calibrated forecaster buys, and the forecast-accuracy threshold at which it beats the oblivious break-even rule.
