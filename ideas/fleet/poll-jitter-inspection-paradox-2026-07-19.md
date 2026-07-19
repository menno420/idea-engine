# Poll-jitter inspection paradox — decorrelating health-check intervals doubles mean fault-detection latency at a fixed poll rate

> **State:** sim-ready
> **Class:** fleet · renewal theory / inspection paradox · monitoring & observability · counterintuitive · round-45 FLEET slot · PROPOSAL 189 → VERDICT 202 (+13)
> **Target:** sim-lab (VERDICT 202, +13 offset)
> 📊 Model: Claude Opus · high · idea/planning
> **Grounding:** https://en.wikipedia.org/wiki/Renewal_theory@9c02ed0 · fetched 2026-07-19
> **Reference (external, reachable):** [Renewal theory — Wikipedia](https://en.wikipedia.org/wiki/Renewal_theory) — verified reachable 2026-07-19 via WebFetch, documenting the inspection paradox and its size-biased-sampling resolution ("A vivid example is the bus waiting time paradox: For a given random distribution of bus arrivals, the average rider at a bus stop observes more delays than the average operator of the buses"; "The resolution of the paradox is that our sampled distribution at time t is size-biased … the likelihood an interval is chosen is proportional to its size") — the forward-recurrence (residual) life E[R]=E[X²]/(2E[X]) this head measures.
> **Verifier (firsthand):** ideas/fleet/poll_jitter_inspection_paradox.py · results-dict sha256 d9a789f57e4db6eaf5ab8c0b3b4f227b85c25f8ed7e989d7821d69a4878f2999

## The phenomenon (one line)

A fault occurring at a uniformly random instant waits, before its next poll, an expected time that grows with the VARIANCE of the poll interval even at a fixed mean poll rate — deterministic period T gives T/2, exponential jitter of the same mean gives T, and the general law is (T/2)(1+CV²).

## Domain

Fleet operations / monitoring & observability, resting on renewal theory (random incidence and the inspection paradox). Round-45 FLEET slot; the mechanism is pure probability, the framing is health-check / telemetry poll scheduling.

## The folk belief

"Jitter the poll interval to avoid thundering-herd polls — as long as I hold the mean poll rate fixed, decorrelating the schedule is free; a fault still waits about half a poll period, T/2, for its next check." Decorrelation is read as a pure win: it spreads load off the top-of-minute spike and does not, the intuition says, cost detection latency because the average rate is unchanged.

## The thesis (reasoned to its fuller form — Q-0254 duty)

The intuition silently assumes a fault lands in a TYPICAL poll gap. It does not. A fault arriving at a uniformly random instant lands inside a given inter-poll gap with probability proportional to that gap's LENGTH — the size-biased (length-biased) law: long gaps catch more faults precisely because they are long. Conditional on landing in a gap of length x, the wait to the next poll is uniform on (0, x), so the exact mean forward-recurrence (residual) life of the renewal poll process is E[R] = E[X²] / (2·E[X]) = (T/2)(1 + CV²), with CV² = Var(X)/T². The folk rule E[R] = T/2 is the CV = 0 special case (a perfectly clockwork poll cadence) and fails for every jittered schedule. Exponential jitter (CV = 1) of the SAME mean T therefore doubles the expected detection wait to exactly T; a heavier-tailed same-mean schedule inflates it further. The mean poll RATE is held fixed across all arms — only the interval variance changes — so the inflation is caused by variance alone, not by polling less often. Decorrelating monitoring poll intervals to dodge a thundering-herd spike thus silently buys mean fault-detection latency: the load you smoothed out reappears as time-to-detect.

## The formal model / Pinned world (committed constants)

- Renewal poll process: i.i.d. inter-poll intervals X with mean E[X] = T = 100 time units (all arms share this mean poll rate). A fault arrives at an instant drawn uniform over the covered horizon (random incidence); the detection wait is the forward-recurrence time to the next poll epoch, found by `bisect` into the cumulative poll-epoch timeline.
- Three arms, all mean 100:
  - **deterministic** — X ≡ T (CV = 0); analytic E[R] = T/2 = 50.
  - **exponential** — X ~ Exp(mean T) (CV = 1); analytic E[R] = T = 100 (the classic Poisson doubling).
  - **hyperexponential H2** — X drawn from a 50/50 mixture of Exp(mean 20) and Exp(mean 180); same mean 100, E[X²] = 0.5·2·20² + 0.5·2·180² = 32800, so analytic E[R] = E[X²]/(2·E[X]) = 32800/200 = 164 (CV² = 2.28).
- N_INTERVALS = 200000 renewal intervals per arm; N_OBSERVERS = 500000 uniform random fault times over the covered horizon.
- Digest posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY — the sha256 of the compact-canonical results dict IS the digest; stdout prints the pretty dump (indent=2, floats at 6 dp) and the digest line; no on-disk JSON.
- SEED = 20260717; relative band = 0.01 (1%); Z_MIN = 3.0.

## Pre-registered gates

- **G1 — paradox (exponential).** The exponential arm's mean simulated residual W_exp exceeds the deterministic-poll baseline T/2 at z ≥ 3, is within 1% of theory T = 100, and W_exp > T/2 (ratio W_exp/(T/2) ≈ 2). This is the head: same mean poll rate, doubled detection wait.
- **G2 — null contrast (deterministic).** The deterministic arm's mean residual W_det sits within a 1% band of T/2 = 50, AND the exponential-vs-deterministic contrast z_contrast = (W_exp − W_det)/√(SE_exp² + SE_det²) ≥ 3. This isolates interval VARIANCE, not the mean rate, as the cause: the two arms share the mean, only the deterministic arm posts T/2.
- **G3 — robustness (hyperexponential shift).** The hyperexponential same-mean arm's mean residual W_h2 is within 1% of the analytic E[X²]/(2μ) = 164, AND W_h2 exceeds T/2 at z ≥ 3. The (1+CV²) law generalizes past the exponential case to an arbitrary same-mean interval distribution.
- all_pass = G1 ∧ G2 ∧ G3.

## Pre-registered decision rule

sim-ready iff the verifier reproduces byte-identical results-dict sha256 with all_pass = true and G1 ∧ G2 ∧ G3 holding in order.

## Dry-sim results (SEED=20260717, verbatim from ideas/fleet/poll_jitter_inspection_paradox.py)

- **G1 (exponential paradox):** mean_residual_sim = 100.843948 (theory T = 100), det baseline T/2 = 50, ratio_vs_half_T = 2.016879, rel_err_vs_theory = 0.008439, **z = 355.431716** → PASS.
- **G2 (deterministic null contrast):** mean_residual_det = 50.018718 (expected 50), band_rel = 0.000374 (inside the 1% band), **z_contrast_exp_vs_det = 341.660906** → PASS.
- **G3 (hyperexponential robustness):** mean_residual_sim = 163.897575 (theory E[X²]/(2μ) = 164), rel_err = 0.000625, **z = 451.526684** → PASS.
- all_pass = true; results-dict sha256 = d9a789f57e4db6eaf5ab8c0b3b4f227b85c25f8ed7e989d7821d69a4878f2999 (byte-identical across two fresh cross-invocation runs).

## Reproduce

```
python3 ideas/fleet/poll_jitter_inspection_paradox.py
```

## Verifier

ideas/fleet/poll_jitter_inspection_paradox.py — stdlib-only (bisect, hashlib, json, math, random); SEED = 20260717; deterministic in-process double-run with an equality assert (`assert r1 == r2`) plus cross-invocation byte-identical results-dict sha256; digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY.

## Why it matters

The failure mode is general and lives wherever the fleet samples an ongoing process at a random instant. Any monitoring, health-check, scrape, or heartbeat cadence that is jittered "to spread load" while holding the mean rate fixed pays for that decorrelation in mean time-to-detect: the smoothed-out load spike reappears as detection latency, inflated by exactly (1+CV²). An operator who reads "same average poll rate" as "same average detection wait" under-budgets incident latency by up to 2× at CV = 1 and further under heavier tails — the exact quantity a fault-detection SLO turns on. The correction is one factor: multiply the naive T/2 detection budget by (1+CV²), or bound the jitter to keep CV small (see the caveats).

## Dedup

Ran `git grep -il` across `ideas/` for `inspection`, `residual`, `forward-recurrence`, and `renewal`, and scanned the tail of `control/outbox.md`: no prior PROPOSAL block prices poll-interval residual-life / fault-detection latency, and no P189/poll-jitter block exists on the bus (P188 population-momentum is the current high-water).

Nearest cousins, distinguished:

- **inspection-paradox-wait-inflation-2026-07-14.md** (the closest — HONEST OVERLAP FLAG). That prior head prices the SAME size-bias law E[W] = E[X²]/(2E[X]) = (μ/2)(1+CV²), but as an ABSTRACT bus-waiting / random-incidence MEASUREMENT over five pinned discrete integer-minute headway pmfs using exact-rational (`fractions.Fraction`) moment arithmetic plus a seeded confirmation arm, framed as a fleet-EXTERNAL pure-probability rotation-domain closer with no operational decision surface. THIS head is the fleet-OPS application: a specific monitoring decision (should you jitter health-check poll intervals to avoid a thundering-herd spike?), measured on continuous same-mean interval distributions (deterministic / exponential / hyperexponential) via a Monte-Carlo forward-recurrence simulation whose deliverable is a fault-DETECTION-LATENCY budget correction, not a bus-wait table. Same theorem, different object and different decision — flagged frankly for the coordinator to weigh rather than buried.
- **decorrelated-jitter-backoff-2026-07-19.md** (P173). That head is retry BACKOFF decorrelation — adding jitter to exponential RETRY schedules to stop a thundering herd re-colliding, and the quantity is total retry WORK (attempts to drain a herd, ≈ N²/2K → linear). This head is monitoring-POLL residual-life / detection LATENCY, where jitter HURTS (inflates the wait) rather than helps. Opposite sign, different quantity.
- **memoryless-pm-waste-2026-07-19.md** (P165). Preventive-maintenance age-replacement waste under a constant hazard — a renewal-reward cost-rate result about WHEN to replace a component, not about a random observer's residual life. Different renewal quantity.
- **bufferbloat-standing-queue-2026-07-19.md** / **kleinrock-conservation-zero-sum-2026-07-19.md**. Queue-occupancy laws (standing sojourn vs buffer size; conservation of mean-wait across disciplines) — server/service machinery, not renewal residual sampling by a random observer. No shared object.

## Model basis (declared model-dependence — the P024 discipline) — and honest caveats

The DIRECTION (E[R] > T/2 whenever the poll interval has positive variance at fixed mean) is theory-guaranteed by the inspection paradox and confirmed to survive the hyperexponential shift (G3). The MAGNITUDE is model-dependent, and the honest caveats are:

- **i.i.d.-renewal assumption.** The model draws intervals i.i.d.; real poll schedules can be NEGATIVELY autocorrelated (a jittered-but-scheduled cadence that "catches up" after a long gap), which can blunt the inflation — the (1+CV²) law is exact only for i.i.d. renewal draws (probe 1).
- **The doubling is the exponential (CV = 1) case.** Real jitter is usually BOUNDED (e.g. ±20% of the period), so CV is small and the effect is milder than the full 2× — bounding the jitter recovers most of the T/2 latency while keeping decorrelation (probe 3).
- **Detection wait, not end-to-end MTTR.** The model measures only the wait to the NEXT poll; a fixed per-poll processing / propagation delay is excluded and composes on top, so this is a lower bound on time-to-detect (probe 6).
- **Heavy tails diverge.** Under a near-infinite-variance same-mean poll-interval distribution, E[X²] → ∞ and the mean residual can be pushed arbitrarily high; the practical cutoff is wherever the tail is truncated (probe 7).

## Probe report (v0, 2026-07-19)

**1. Does the (1+CV²) inflation persist when poll intervals are negatively autocorrelated (a jittered-but-scheduled cadence) rather than iid renewal draws?** The exact (1+CV²) law is derived for i.i.d. renewal draws; negative autocorrelation (a schedule that shortens the next gap after a long one) partially cancels the size-bias and can reduce the inflation below (1+CV²). The direction (still ≥ T/2 for any positive marginal variance) holds, but the magnitude is a named follow-up, not covered by this i.i.d. sim.

**2. At what poll-interval CV does the added detection latency outweigh the thundering-herd load the jitter was introduced to prevent?** The added latency is (CV²/2)·T, so it grows quadratically in CV while the herd-relief benefit saturates once the load is spread over more than a few slots; the crossover is workload-specific but the head gives the exact latency cost curve (CV²/2)·T to price against a measured herd-relief benefit. Bounded jitter (small CV) is almost always on the good side of that trade.

**3. Does bounding the jitter (truncating the interval distribution) recover most of the T/2 latency while keeping decorrelation?** Yes — CV² scales with the width of the jitter window, so a ±20% bounded jitter has CV² ≈ 0.013 and inflates the wait by well under 1%, while still spreading polls across the window enough to break the top-of-minute spike. Decorrelation and low latency are compatible when the jitter is bounded rather than exponential.

**4. For a fleet of N independent monitors, does the minimum-over-N detection wait shrink fast enough that per-node jitter stops mattering at scale?** If N independent monitors each poll the same target, the fault is detected at the MINIMUM of N residuals, whose mean falls ≈ 1/N, so per-node interval variance matters progressively less as N grows. The paradox is a single-poller effect; redundant independent polling is one real mitigation, at N× the poll load.

**5. Does the paradox change sign for burst faults (a fault present for a finite window) versus instantaneous point faults?** For a fault present over a finite window of length w, detection requires a poll to land in that window, so the relevant quantity shifts from residual life to the probability a renewal epoch falls in [t, t+w]; the mean detection wait for a persistent fault is still the residual life, so the sign is unchanged for "time to first poll after onset". Very short transient faults (w ≪ T) are a different, coverage-probability question (kin to the healthcheck-blind-window head).

**6. How does the residual-life inflation compose with a fixed per-poll processing delay — additive, or does variance interact?** A fixed per-poll processing/propagation delay d adds linearly: total time-to-detect ≈ E[R] + d = (T/2)(1+CV²) + d, with no interaction, because d is a constant shift independent of where the fault lands. Variance in the processing delay itself would add its own term, but a fixed d is purely additive.

**7. Under a heavy-tailed (near-infinite-variance) poll-interval distribution, does mean detection latency diverge, and where is the practical cutoff?** Yes — E[R] = E[X²]/(2E[X]) diverges as E[X²] → ∞, so a poll-interval distribution with an infinite second moment (e.g. a Pareto with tail index ≤ 2) gives unbounded mean detection latency. In practice every real schedule is truncated (a max backoff / max interval), and the cutoff is exactly that truncation point — which is why capping the jitter window is the operational fix.

**8. Does the same size-biased sampling inflate the mean AGE of the last successful poll (staleness) symmetrically with the forward residual?** Yes — by the same length-biasing, the backward-recurrence (age) time has mean E[A] = E[X²]/(2E[X]) = E[R], so a random glance at a jittered-refresh metric sees data older than T/2 by the identical (1+CV²) factor. Forward (detection wait) and backward (staleness) inflations are symmetric; the staleness framing is the flagged companion head for a later slot.

**Recommendation: sim-ready**
