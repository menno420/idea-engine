# PROPOSAL 189 — Poll-jitter inspection paradox: decorrelating health-check intervals doubles mean fault-detection latency at a fixed poll rate (round-45 FLEET slot, P189 → V202, +13)

> **Status:** in-progress
> 📊 Model: Claude Opus · high · idea/planning
>
> Born-red HOLD: this card lands born-red (`in-progress`) to hold the PR red on the first commit. It flips to `complete` as the last commit, after the verifier reproduces a byte-identical results-dict sha256 and all gates pass.

## Objective
Show that adding jitter to monitoring / health-check poll intervals — a standard decorrelation trick used to avoid thundering-herd polls — inflates the expected time a randomly-timed fault waits before its next poll, at a FIXED mean poll rate. Deterministic polls of period T give expected detection wait T/2; exponentially-jittered polls of the SAME mean T give T (double). The excess is exactly ((1+CV²)/2)·T by the renewal inspection paradox: the forward-recurrence (residual) life of a renewal process has mean E[R] = E[X²] / (2·E[X]).

## Constraints honored
- stdlib-only verifier (hashlib, json, math, random); SEED = 20260717 pinned.
- deterministic in-process double-run with an assert; cross-invocation byte-identical results-dict sha256.
- ≥3σ gates: G1 paradox present, G2 deterministic null contrast, G3 robustness under a shifted (hyperexponential) same-mean distribution.
- DIGEST-POSTURE: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY; the compact-canonical results-dict sha256 IS the digest; stdout prints the pretty dump (indent=2) with floats at 6 dp; no on-disk JSON.

## Pinned world
- T (mean poll interval) = 100 time units.
- n_intervals = 200000 renewal intervals per arm; n_observers = 500000 uniform random fault times over the covered horizon.
- Arms: deterministic (CV=0, E[R]=50), exponential (CV=1, E[R]=100), hyperexponential H2 (p=0.5, component means 20 and 180, same mean 100, E[X²]=32800 → E[R]=164).

## Gate-plan (pre-registered)
- **G1 paradox (exponential):** mean simulated residual W_exp exceeds the deterministic-poll baseline T/2 at z ≥ 3; W_exp within 1% of theory T = 100; ratio W_exp/(T/2) ≈ 2.
- **G2 null contrast (deterministic):** mean simulated residual W_det within a 1% band of T/2 = 50, AND the exponential-vs-deterministic contrast z_contrast ≥ 3 (isolates interval VARIANCE, not the mean rate, as the cause).
- **G3 robustness (hyperexponential shift):** mean simulated residual W_h2 within 1% of the analytic E[X²]/(2μ) = 164, AND W_h2 exceeds T/2 at z ≥ 3 (the (1+CV²) law generalizes past the exponential case).
- all_pass = G1 ∧ G2 ∧ G3.

## GROUNDING (verified live)
https://en.wikipedia.org/wiki/Renewal_theory@9c02ed0 — renewal theory inspection paradox / forward-recurrence residual life E[R]=E[X²]/(2E[X]); verified reachable 2026-07-19 via WebFetch (documents the bus-waiting-time inspection paradox and its size-biased-sampling resolution).

## Probe questions
**1. Does the (1+CV²) inflation persist when poll intervals are negatively autocorrelated (a jittered-but-scheduled cadence) rather than iid renewal draws?**
**2. At what poll-interval CV does the added detection latency outweigh the thundering-herd load the jitter was introduced to prevent?**
**3. Does bounding the jitter (truncating the interval distribution) recover most of the T/2 latency while keeping decorrelation?**
**4. For a fleet of N independent monitors, does the minimum-over-N detection wait shrink fast enough that per-node jitter stops mattering at scale?**
**5. Does the paradox change sign for burst faults (a fault present for a finite window) versus instantaneous point faults?**
**6. How does the residual-life inflation compose with a fixed per-poll processing delay — additive, or does variance interact?**
**7. Under a heavy-tailed (near-infinite-variance) poll-interval distribution, does mean detection latency diverge, and where is the practical cutoff?**
**8. Does the same size-biased sampling inflate the mean AGE of the last successful poll (staleness) symmetrically with the forward residual?**

## Outcome
results-dict sha256 = d9a789f57e4db6eaf5ab8c0b3b4f227b85c25f8ed7e989d7821d69a4878f2999; all_pass = true; G1 z=355.431716, G2 z_contrast=341.660906, G3 z=451.526684; mean residuals det≈50 / exp≈100 / h2≈164.

## ⟲ Previous-session review
Round-44 closed with P188 (population momentum, UNRELATED slot → V201, +13). The rotation is fleet → venture → game → unrelated; this card opens round-45 in the FLEET slot (P189 → V202). Sibling V201 (population-momentum verdict) and its mirror run concurrently — outbox/heartbeat concurrency is expected, so rebase-and-union before each push.

## 💡 Session idea
Companion head for a later slot: the SAME inspection paradox raises the mean AGE of the freshest telemetry sample a dashboard shows — a random glance at a jittered-refresh metric sees data older than half the refresh period by the same (1+CV²) factor — quantifying staleness risk in decorrelated scrape schedules.
