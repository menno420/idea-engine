# PROPOSAL 153 — Kleinrock's conservation law: scheduling a single-server fleet queue is zero-sum — no work-conserving dispatch policy can lower the load-weighted mean wait (P153 → V166, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card lands first with `Status: in-progress` to hold the PR red on the substrate gate; it flips to `complete` as the final commit, after the heartbeat, releasing the landing workflow. A red gate before that flip is the HOLD, not a defect.

## Objective
Author round-36's FLEET-slot PROPOSAL 153: a fresh, counterintuitive, quantifiable fleet-ops mechanism. Head: Kleinrock's conservation law — in a single-server M/G/1 dispatch queue, the load-weighted mean wait sum_i rho_i W_i is INVARIANT across every non-preemptive work-conserving discipline. Priority-to-short slashes short-job wait, but every rho-weighted second saved is repaid, rho-weighted, by long jobs: scheduling is zero-sum. Deliver a stdlib-only deterministic verifier (SEED=20260717, discrete-event M/G/1 under common random numbers, >=3 sigma gates including a shifted-distribution robustness gate) plus a proposal doc a VERDICT 166 session can check independently.

## Constraints honored
- stdlib-only verifier; SEED pinned 20260717; in-process double-run determinism assert; results dict + sha256 printed (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture).
- +13 offset (P153 → V166). Outbox append-only + dedupe. Status high-water take-max, never regress.
- Grounding cites a reachable real-world source; crossover/caveat disclosed honestly.
- Family model names only; timestamps from `date -u`.

## GROUNDING (verified at HEAD)
- Pending final run — the flipped card and the idea doc carry the reproduced results-dict sha256, gate z-scores, and the repo/external grounding lines.

## Probe questions
**1.** Is the conserved quantity sum_i rho_i W_i truly discipline-invariant, or an artifact of one arrival stream? — measured across independent replications under common random numbers, FIFO vs priority-to-short vs priority-to-long.
**2.** Does the invariance survive a shifted class mix and utilization? — a dedicated robustness gate re-measures the conservation leak under a shifted config.
**3.** Is the scheduling swing real and large, not a rounding effect? — a gate first establishes short jobs save a large rho-weighted wait under priority before conservation is claimed.
**4.** Where does it break? — the law is a steady-state mean statement for non-preemptive work-conserving disciplines; preemption, non-work-conserving idling, or heavy finite-sample transients are the disclosed boundaries.

## Outcome
Pending final verifier run — filled at the deliberate `complete` flip.

## ⟲ Previous-session review
Round-35 closed with FLEET P149→V162 and VENTURE P150→V163 landed, GAME P151→V164 and UNRELATED P152→V165 (Braess paradox) authored. Verifier posture carried forward here: whole-dict digest, common-random-numbers variance reduction, a shifted-distribution robustness gate, honest caveat disclosure. Proposal high-water P152; this slice opens round-36 at the FLEET slot and advances it to P153 (take max, never regress).

## 💡 Session idea
Pending — recorded at the flip.
