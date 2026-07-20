# PROPOSAL 201 — Graham's timing anomaly: give a greedy scheduler one more machine and the batch can finish later (P201 → V214, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD.** This card is committed `in-progress` on commit 1 to hold the PR red while the proposal is assembled; it flips to `complete` on the final commit after the doc, verifier, and outbox block are in. The born-red red is intended, not a defect.

## Objective
Author and land the round-48 FLEET-slot proposal P201 (→ V214, +13): Graham's multiprocessing timing anomaly — greedy list scheduling is non-monotone (adding a machine / shortening jobs / removing a dependency can each increase makespan) yet is bounded by (2 − 1/m)× optimum. Ship sim-ready with a deterministic stdlib-only verifier.

## Constraints honored
- Dedup-first: no prior makespan/list-scheduling/Graham head in `ideas/` (nearest neighbors distinct).
- Deterministic verifier, SEED=20260717, stdlib-only; results-dict sha256 byte-identical across two fresh runs.
- Three pre-registered gates with stated directions (G1/G2 high z; G3 zero violations, Fraction-exact).
- External grounding: Wikipedia "List scheduling" rev 1291511174 (bound + anomalies), 40-hex sha1 pin.
- Single-step git only; born-red HOLD; merge-on-green as the only merge path.

## GROUNDING (verified at HEAD)
https://en.wikipedia.org/w/index.php?title=List_scheduling&oldid=1291511174@e2de39981e1fdc4d2daf8d7411f1f3dc0f32aaa2 · fetched 2026-07-20 — states the (2−1/m) bound and the three anomalies verbatim, citing R. L. Graham 1969.

## Probe questions
**1.** Effect real & correctly stated? Yes — Graham 1969; concrete witnesses for all three levers.
**2.** Mechanism sound, not a bug? Yes — textbook greedy list scheduling; idle-allowing branch-search optimum, validated.
**3.** Counterintuitive? Yes — refutes "more resources never hurt" on three axes.
**4.** Deterministic/reproducible? Yes — sha256 2f81…eef identical across two fresh processes.
**5.** Gates pre-registered with directions? Yes — G1/G2 high z, G3 zero violations; all pass.
**6.** Grounding external & specific? Yes — Wikipedia List_scheduling rev 1291511174, both claims verbatim.
**7.** Un-built / non-duplicate? Yes — no prior makespan/Graham head; nearest neighbors distinct.
**8.** sim-lab reproducible & worth a VERDICT? Yes — clean-room reproduces sha256 + all gates; exact bound gate is a Fraction-exact target.

## Outcome
Proposal P201 shipped sim-ready: doc `ideas/fleet/graham-scheduling-anomaly-2026-07-20.md` + verifier `ideas/fleet/graham_scheduling_anomaly.py` (all_pass=true, sha256 2f81534216b6d8dee3d99446a0e451bde7cd64019d5f10b7de59a01921129eef) + outbox block P201→V214 + high-water P200→P201. Gates: G1 z=77.58, G2 add z=8.49 / shorten z=9.22, G3 0 violations (max ratio 11/7).

## ⟲ Previous-session review
Reviewed P200 (Banach's matchbox residual, → V213): a clean four-gate proposal (closed-form pmf vs exact DP, ≥3σ folk refutation, agreement, robustness) landed sim-ready; V213 is the outstanding sim in sim-lab. Pattern reused here: an exactly-true Fraction-exact gate (there closed-form pmf == exact DP; here the (2−1/m) bound == exhaustive optimum) paired with a high-z surprise gate. No defects found in P200's structure.

## 💡 Session idea
Reusable fleet-ops lens: pair every sampled "surprising rate" gate (high-z) with an "exactly-true" companion gate (closed-form vs exhaustive enumeration, Fraction-exact) so a proposal ships both a distribution-dependent empirical claim and a distribution-free provable one. It hardens the head against "the effect is just an artifact of your generator" — the exact gate survives any instance distribution.
