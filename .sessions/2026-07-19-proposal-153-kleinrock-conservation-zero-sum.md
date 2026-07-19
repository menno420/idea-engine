# PROPOSAL 153 — Kleinrock's conservation law: scheduling a single-server fleet queue is zero-sum — no work-conserving dispatch policy can lower the load-weighted mean wait (P153 → V166, +13)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card landed first with `Status: in-progress` to hold the PR red on the substrate gate; it flips to `complete` as this final commit, after the heartbeat, releasing the landing workflow. A red gate before that flip was the HOLD, not a defect.

## Objective
Author round-36's FLEET-slot PROPOSAL 153: a fresh, counterintuitive, quantifiable fleet-ops mechanism. Head: Kleinrock's conservation law — in a single-server M/G/1 dispatch queue, the load-weighted mean wait sum_i rho_i W_i is INVARIANT across every non-preemptive work-conserving discipline. Priority-to-short slashes short-job wait, but every rho-weighted second saved is repaid, rho-weighted, by long jobs: scheduling is zero-sum. Deliver a stdlib-only deterministic verifier (SEED=20260717, discrete-event M/G/1 under common random numbers, >=3 sigma gates including a shifted-distribution robustness gate) plus a proposal doc a VERDICT 166 session can check independently.

## Constraints honored
- stdlib-only verifier; SEED pinned 20260717; in-process double-run determinism assert; results dict + sha256 printed (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture).
- +13 offset (P153 → V166). Outbox append-only + dedupe. Status high-water take-max, never regress.
- Grounding cites a reachable real-world source; crossover/caveat disclosed honestly.
- Family model names only; timestamps from `date -u`.

## GROUNDING (verified at HEAD)
- Verifier ideas/fleet/kleinrock_conservation_zero_sum.py committed on branch claude/proposal-153-kleinrock-conservation-zero-sum (PR #613, commit f7354e1); results-dict sha256 1b40af51baa24c2041bbd822b190e5447c6299840604822580b3b3bb3153ee18 reproduced EXACT across an in-process + cross-invocation double-run.
- Idea doc ideas/fleet/kleinrock-conservation-zero-sum-2026-07-19.md; the doc Grounding line is pinned to control/outbox.md at origin/main commit 6a29f11 (outbox blob 05c6e63).
- External reference (reachable): Kleinrock's conservation law — L. Kleinrock, "A conservation law for a wide class of queueing disciplines," NRLQ 12(2):181-192 (1965); "Queueing Systems, Volume II" (1976); Wikipedia "M/G/1 queue" (Pollaczek-Khinchine) verified reachable.
- Offset +13 (P153 → V166), cited from the P153 outbox depends-ledger + heartbeat (predecessor P152 → V165).
- Merged origin/main 154ab76 IN to reconcile round-35 completion (V162–V165 landed).

## Probe questions
**1.** Is the conserved quantity sum_i rho_i W_i truly discipline-invariant, or an artifact of one arrival stream? — measured across 30 independent replications under common random numbers, FIFO vs priority-to-short vs priority-to-long: conserved sum coincides to ~0.08% while W1 swings 4.87x.
**2.** Does the invariance survive a shifted class mix and utilization? — G3 re-measures the conservation leak under P(short)=0.60 / S2=6.0 / rho=0.80; leak 0.023037, z=+23.740077.
**3.** Is the scheduling swing real and large, not a rounding effect? — G1 first establishes short jobs save a large rho-weighted wait under priority (transfer_short_mean=+7.450148, z=+30.100904) before conservation is claimed.
**4.** Where does it break? — the law is a steady-state mean statement for non-preemptive work-conserving disciplines; preemption (SRPT), non-work-conserving idling, and heavy finite-sample transients are the disclosed boundaries.

## Outcome — PROPOSAL LANDED (round-36 FLEET slot opens)
- Verifier ideas/fleet/kleinrock_conservation_zero_sum.py (stdlib-only discrete-event M/G/1, common random numbers across FIFO / priority-to-short / priority-to-long, R=30 replications): all_pass=true, first_failing_gate=null, exit 0. G1 transfer_short_mean=+7.450148 z=+30.100904 / G2 leak_mean=0.040689 z=+12.680569 (ceiling 0.10) / G3 shift_leak_mean=0.023037 z=+23.740077 (ceiling 0.10). results-dict sha256 1b40af51baa24c2041bbd822b190e5447c6299840604822580b3b3bb3153ee18 reproduced EXACT (byte-identical in-process + cross-invocation double-run).
- Invariance readout: conserved sum_i rho_i W_i = 28.180657 (FIFO) / 28.198485 (priority-short) / 28.177276 (priority-long), max-to-min spread ~0.08%, while short-job wait W1 swings 33.088966 → 6.794325 (4.87x) and long-job wait W2 33.186088 → 46.364871 (+39.7%). Scheduling is a zero-sum transfer, not a reduction.
- Idea doc committed; outbox PROPOSAL 153 block appended (target / idea / question / done-when / depends / loop); heartbeat overwritten (proposal high-water ADVANCES P152 → P153, verdict high-water STAYS V165); claim released. Merged origin/main 154ab76 IN (round-35 COMPLETE V162–V165). The final flip to `complete` releases the born-red HOLD; landing via idea-engine merge-on-green (arm-race backstop known), zero agent merge calls.

## ⟲ Previous-session review
Round-35 landed COMPLETE (V162–V165): FLEET P149→V162, VENTURE P150→V163, GAME P151→V164 (sim-lab #239, mirror #612), UNRELATED P152→V165 (sim-lab #238 @da2ea70, mirror #611). Verifier posture carried forward: whole-dict digest (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY, P127+ compact-canonical twist), a shifted-distribution robustness gate, common-random-numbers variance reduction, honest caveat disclosure. This slice opens round-36 at the FLEET slot with P153 → V166. NON-CONTIGUITY note for the successor: V137/P124, V132/P119, and round-26 FLEET P113 → V126 (mirror #527 @cee9162) remain open below the high-water — do not read "round-35 COMPLETE" as closing them.

## 💡 Session idea
The conservation law is a steady-state MEAN invariant; the natural round-36 follow-on sharpens it to the TAIL. Candidate: SRPT-vs-FIFO tail-vs-mean tradeoff — Shortest-Remaining-Processing-Time minimizes MEAN wait (it is preemptive, so NOT bound by the non-preemptive conservation law), but under a heavy-tailed service distribution it can INFLATE the p99 wait of the largest jobs relative to FIFO; gate (G-a) SRPT mean wait < FIFO mean wait at >=3 sigma (the known optimality), (G-b) SRPT p99 wait of the top service-decile > FIFO p99 for that decile at >=3 sigma (the tail penalty the mean hides), (G-c) the effect strengthens as the service-time tail heavies. The lesson sharpens from "scheduling cannot cut aggregate wait" to "the one discipline that CAN cut mean wait pays for it in the tail of the jobs it starves." Named, not authored.
