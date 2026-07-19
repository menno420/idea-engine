# PROPOSAL 160 — Cauchy no-averaging: the law of large numbers fails for infinite-variance data (P160 -> V173, +13)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card lands first with `Status: in-progress` to hold the PR red on the substrate gate; it flips to `complete` as the final commit, after the heartbeat, releasing the landing workflow. A red gate before that flip is the HOLD, not a defect.

## Objective
Author round-37's UNRELATED-slot PROPOSAL 160: a fresh, counterintuitive, quantifiable mechanism from probability / heavy-tailed statistics. Head: for i.i.d. draws from a standard Cauchy distribution the sample mean X̄_n is itself standard Cauchy for every n — averaging never concentrates, so the law of large numbers fails and X̄_n has the same spread as a single draw, no matter how large n grows. Three scale-free landmarks: the sample mean's interquartile spread is invariant in n (IQR(X̄_n)/IQR(X₁) → 1), the sample median by contrast concentrates as ~ π/(2√n), and the Cauchy quartiles sit at ±1 so IQR = 2 independent of any sample. Deliver a stdlib-only deterministic verifier (SEED pinned, three ≥3σ gates including a scale-free robustness gate under a shifted Cauchy scale) plus a proposal doc a VERDICT 173 session can check independently. Hand to VERDICT 173 at +13 offset.

## Constraints honored
- stdlib-only Python 3 verifier; SEED pinned; in-process double-run determinism assert; results dict + sha256 printed (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY, floats 6 dp).
- three ordered z-gates (z_gate=3.0): G1 mean-does-not-concentrate (IQR of X̄_n matches IQR of a single draw, ratio ≈ 1, invariant in n) + closed-form match, G2 median-does-concentrate (spread shrinks as ~π/(2√n)) + closed-form match, G3 scale-free robustness under a shifted (wider) Cauchy scale.
- +13 offset (P160 → V173). Outbox append-only + dedupe. Proposal high-water take-max, never regress. Born-red HOLD; merge-on-green landing.
- Grounding cites a reachable real-world source; the undefined-mean / infinite-variance caveat disclosed honestly. Family model names only; timestamps from `date -u`.

## GROUNDING (verified at HEAD)
- Offset + high-water lineage: `control/outbox.md` at HEAD (round-37 GAME-slot P159 → V172 tail; proposal high-water pre-P160, +13 offset). Verify live before the outbox append.
- External phenomenon (reachable): the Cauchy distribution — the sample mean of n i.i.d. standard-Cauchy variates is itself standard Cauchy for every n, so the average does not converge and the law of large numbers does not apply. https://en.wikipedia.org/wiki/Cauchy_distribution — Wikipedia "Cauchy distribution"; stable law (α=1), robust spread IQR/2 = γ, sample median asymptotic law Normal(0, (πγ)²/(4n)) so scale ~ πγ/(2√n).

## Probe questions
**1.** Is the mean genuinely non-concentrating, or an MC artifact of too-few TRIALS? — Stable-law fact: the mean of n Cauchy(0, γ) is Cauchy(0, γ) exactly, so its spread is flat in n by construction; G1 measures spread(mean, n=100)/spread(mean, n=1) against the CLT-shrink null 1/√100 = 0.1 at ≥3σ (observed ≈ 1, hugging 1 not noise around 0.1).
**2.** Does the median actually concentrate on the same data, or is G2 circular given the shared spread measure? — Both estimators use the *same* IQR/2 spread on the *same* draws; G2 gates spread(median, n=100)/spread(median, n=1) below the no-concentration null 1.0 at ≥3σ (observed ≈ 1/√100) — the split is the estimator, not the measure.
**3.** Is the split scale-free or a one-γ / one-n artifact? — G3 re-runs at γ′=2.5, n′=200 and confirms mean-non-concentration (rejects 1/√200 ≈ 0.0707) AND median-concentration (rejects 1.0) both at ≥3σ — a property of the Cauchy law and the estimator, not a tuned scale.
**4.** Crossover, not the claim: the α=1 Cauchy is the extreme where averaging is useless; a stable law 1<α<2 gives the mean a slower-than-√n n^(1/α−1) shrink and α≥2 restores the CLT. Are these disclosed as crossovers, not asserted as the head? — disclosed as crossovers; the verified head is the α=1 estimator split (the mean cannot concentrate, the median does).

## Outcome
Verifier `ideas/fleet/cauchy_no_averaging.py` + doc `ideas/fleet/cauchy-no-averaging-2026-07-19.md` committed on branch claude/proposal-160-cauchy-no-averaging (PR #628). Verifier deterministic under SEED=20260717; results-dict sha256 `413e56925e89e34148cb9286df0f392c1a9881fc9072c7683b9f181f39ae7b5c` reproduced identical across an in-process + cross-invocation double-run. Three z-gates PASS in order — G1 mean-does-not-concentrate mean_ratio=1.016435 z=+91.179099 (vs CLT-shrink null 1/√100=0.1), G2 median-does-concentrate med_ratio=0.106589 z=+1103.622367 (vs no-concentration null 1.0), G3 robust-under-shift at γ′=2.5/n′=200 mean_ratio=0.999453 z_mean=+105.248919 / med_ratio=0.074954 z_med=+1871.391001; all_pass=true, first_failing_gate=null, exit 0. Headline: 100 averaged Cauchy readings are exactly as spread as one (ratio ≈ 1, not 0.1), while the median on the same data shrinks ~10× (ratio ≈ 0.107) — the estimator you pick, not the sample size, buys the precision. Outbox PROPOSAL 160 block appended (status: sim-ready, P160 → V173, +13); proposal high-water advanced P159 → P160; claim released.

## ⟲ Previous-session review
Round-37's GAME slot (PROPOSAL 159 — drop-rate median gap → V172) landed on three ≥3σ gates with a whole-dict digest and a shifted-rate robustness gate. This UNRELATED slice (P160 → V173) is topically unrelated but carries the same digest posture forward — WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY, floats rounded 6 dp, an in-process double-run determinism assert, and a shifted-scale robustness gate — so the two round-37 slices differ in subject while sharing the exact reproduction discipline.

## 💡 Session idea
Named, not authored: the "generalized-CLT / alpha-stable partial-concentration spectrum" — for a symmetric α-stable tail with 1 < α < 2 the mean exists but the sample mean concentrates only as n^(1 − 1/α), slower than the Gaussian √n. A companion card that measures the concentration exponent against the closed form 1 − 1/α, quantifying a "partial concentration" spectrum that bridges Cauchy (α=1, no concentration — this card) and Gaussian (α=2, full √n) — gateable by fitting the measured concentration exponent to 1 − 1/α across a sweep of α.
