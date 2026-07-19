# PROPOSAL 185 — Bufferbloat's standing queue: on a saturated server a BIGGER buffer buys latency, not throughput (round-44 FLEET slot, P185 → V198, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD.** This card lands on the FIRST commit with `Status: in-progress`, holding the substrate-gate red while the verifier is authored and proven. The final commit flips it to `complete`, releasing merge-on-green. Gate-red before the flip is the born-red exception, not a defect.

## Objective
Show, with a deterministic stdlib M/M/1/K simulation, that on a saturated single server (offered load ρ = λ/μ > 1) ENLARGING the finite buffer capacity K makes mean sojourn time grow ~linearly in K — a permanent "standing queue" — while goodput stays pinned at the service rate μ. The extra buffer delivers zero throughput and pure latency. This is bufferbloat: oversized drop-tail buffers hold a persistent backlog that adds delay without moving more work.

## Constraints honored
- stdlib-only (`random, math, json, hashlib, sys, collections`); Python 3.
- SEED = 20260717 pinned; fully deterministic.
- Common random numbers: the small-K and large-K runs share one arrival + service stream per trial, so ΔW is a clean paired difference.
- In-process double-run determinism asserted (`run()` run twice, canonical dicts must be identical).
- WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest: sha256 of the compact-canonical results dict IS the digest; the dict is not self-referential; pretty dump to stdout, floats 6 dp; no on-disk JSON.
- Pre-registered ordered gates G1→G2→G3, matching the shipped verifier exactly.
- Grounding URL returns HTTP 200 and documents the specific head.
- Timestamps from `date -u`.

## Pinned world (committed constants — sim-lab must reproduce exactly)
SEED = 20260717 · Z_GATE = 3.0 · TRIALS = 40 · N_ARR = 20000 · WARM = 4000 · MU = 1.0 · R_BASE = 1.25 · R_SHIFT = 1.5 · K_SMALL = 25 · K_LARGE = 75 · EPS = 0.02 · FCFS M/M/1/K · floats rounded 6 dp · whole-dict / no-self-field / stdout-only.

## Gate-plan (pre-registered — must match the shipped verifier; z_gate = 3.0)
- **G1 — latency scales with buffer size (≥3σ).** Paired ΔW = W(K_large) − W(K_small) over TRIALS trials is positive at ≥3σ: z = mean(ΔW)/(sd/√TRIALS) ≥ 3.0 AND mean(ΔW) > 0. A bigger buffer strictly adds latency.
- **G2 — no goodput dividend (bound).** The throughput gap is negligible and both buffers saturate the server: |thr(K_small) − thr(K_large)| ≤ EPS·μ AND thr(K_small) ≥ (1−EPS)·μ AND thr(K_large) ≥ (1−EPS)·μ. The added latency buys no throughput.
- **G3 — robust under a shifted load (≥3σ).** Repeat at ρ = 1.5: paired ΔW > 0 at ≥3σ AND the G2 no-dividend bound holds (throughput gap ≤ EPS·μ, both ≥ (1−EPS)·μ). The effect survives the load shift.

all_pass = G1 ∧ G2 ∧ G3.

## GROUNDING (verified at HEAD)
Bufferbloat: oversized network buffers hold a persistent standing queue under saturation, inflating latency without improving throughput. Verified live 2026-07-19T21:43:29Z: https://en.wikipedia.org/wiki/Bufferbloat@b060bda448fe039b88d48c76235f82ecefac8d80 — the page states, verbatim, "In a first-in first-out queuing system, overly large buffers result in longer queues and higher latency, and do not improve network throughput." Gettys & Nichols, "Bufferbloat: Dark Buffers in the Internet", ACM Queue 9(11), 2011.

## Probe questions
**1.** Does the paired ΔW = W(K_large) − W(K_small) clear ≥3σ and stay strictly positive under SEED = 20260717?
**2.** Is the throughput gap between the two buffers ≤ EPS·μ, with both throughputs ≥ (1−EPS)·μ (server saturated, zero goodput dividend)?
**3.** Does W scale ~linearly in K (report W_large/W_small against K_large/K_small)?
**4.** Does the cross-invocation double run reproduce the results-dict sha256 byte-for-byte?
**5.** Does the in-process double-run assertion hold (determinism)?
**6.** Does the grounding URL resolve live and document the standing-queue / latency-without-throughput head?
**7.** Does the shifted-load gate (ρ = 1.5) preserve both the ≥3σ latency growth and the no-dividend bound?
**8.** Are the pre-registered gates here identical to the gates the verifier ships?

## Outcome
_Pending born-red flip — filled at the finalize commit after the verifier is proven._

## ⟲ Previous-session review
PROPOSAL 184 (de Moivre small-sample variance artifact, round-43 UNRELATED slot, sim-ready, targets V197, +13): a clean estimation-statistics head — ranking units by an observed rate surfaces the smallest-sample units at BOTH extremes because SD(rate) = √(p(1−p)/n) blows up as n shrinks. Grammar clean, gates pre-registered at ≥3σ with shifted-p and shifted-range robustness gates, +13 offset consistent, no blocker seen. This P185 opens round-44 with the FLEET slot (rotation FLEET → VENTURE → GAME → UNRELATED).

## 💡 Session idea
Companion FLEET-OPS head for a future slot: **the AQM latency/throughput frontier** — an active-queue-management drop/mark threshold (CoDel/RED-style) applied to the same M/M/1/K world trades a small throughput haircut for a large latency cut, and the optimal threshold is set by the delay-bandwidth product, not the raw buffer size. Quantify the Pareto knee and gate the latency win at ≥3σ against a fixed-throughput floor. Stdlib-checkable, grounds to CoDel (Nichols & Jacobson, 2012).

(End of card content.)
