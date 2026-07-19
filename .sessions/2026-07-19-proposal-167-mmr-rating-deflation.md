# PROPOSAL 167 — MMR/Elo rating deflation: a competitive ladder's mean rating is not conserved — every game is a zero-sum transaction, so underrated newcomers who climb to their true skill and then retire carry those points OUT of the pool, deflating everyone's rating with no change in anyone's skill (round-39 GAME slot, P167 -> V180, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card lands first with `Status: in-progress` to hold the PR red on the substrate gate; it flips to `complete` as the final commit, after the outbox block, releasing the landing workflow. A red gate before that flip is the HOLD, not a defect.

## Objective
Author round-39 GAME-slot PROPOSAL 167 — the MMR/Elo rating-deflation head — with a stdlib firsthand verifier (SEED=20260717; >=3 sigma gates including a robustness gate under a shifted distribution) and a live-grounded proposal doc, targeting sim-lab VERDICT 180 (+13 offset).

## Constraints honored
- Merge-on-green only; zero merge calls; PR opens READY.
- WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest posture; deterministic in-process double-run; cross-invocation identical.
- Grounding URL verified live this session (oldid pinned).
- No model version identifiers in artifacts; family names only. Timestamps from date -u.

## GROUNDING (verified at HEAD)
Elo rating system, "Combating deflation": each game is an equal transaction (winner +N, loser -N), so rating points are conserved WITHIN games and can only enter or leave the pool with players. Players enter as low-rated novices and retire as high-rated experienced players, so under strictly equal transactions the pool's mean rating deflates in the long run. Verified live HTTP 200 this session at revision oldid=1364176765.

## Pre-registered Gate-plan (APPROVE iff ALL hold, in order G1 -> G2 -> G3; z_gate=3.0)
- **G1 deflation-real** — across R=40 independent ladders the pool mean displayed-rating drift is strictly negative at >=3 sigma (drift z < -3), rejecting the "zero-sum => the mean rating cannot move" folk null.
- **G2 churn-ledger identity (mechanism anchor)** — the pool's total displayed-rating change equals EXACTLY (points brought in by joiners) minus (points carried out by leavers); play moves zero net points. Max |residual| < 1e-6, proving the drift is 100% churn ledger and 0% game outcome.
- **G3 robustness / deeper-floor scaling (shifted world)** — under a deeper entry-underrating (lower floor) plus a shifted K and churn rate, deflation persists at >=3 sigma AND deepens (shifted mean drift < baseline mean drift).

## Probe questions
**1. Is the deflation an artifact of the warm start (displayed==true at t0)?** No — the churn-ledger identity (G2) shows the entire total-rating change equals joiners-in minus leavers-out to float precision, so the drift is the churn asymmetry regardless of the initial level.
**2. Could the drift be games leaking points rather than churn?** No — each game is exactly zero-sum in displayed rating (winner +K·delta, loser -K·delta); the only points source/sink is a join (in at the floor) or a retire (out at the climbed rating), which G2 confirms.
**3. Does the effect vanish if newcomers are not underrated?** As the floor approaches mean true skill the enter-low/retire-high gap closes and deflation shrinks to zero; G3 confirms a deeper underrating (lower floor) deepens deflation, bounding the claim to pools that seed newcomers below their skill.
**4. Is "mean rating stable" a strawman?** It is the folk reading of "Elo is zero-sum, so it can't inflate or deflate"; G1 rejects it at >=3 sigma because a zero-sum-PER-GAME system still drifts when points cross the pool boundary with players.
**5. Are baseline and shifted worlds measured on independent streams?** Yes — baseline draws Random(SEED+i), the shifted world Random(SEED+777+i); the two mean-drift samples are independent, so G3's ordering is a conservative between-world comparison.
**6. Does the digest depend on machine floats?** Floats are rounded to 6 dp before hashing; the compact-canonical dict sha256 is asserted stable in-process and reproduced cross-invocation on the same runtime.
**7. What breaks the deflation first?** Anti-deflation controls — rating floors, bonus-point injection, true-skill provisional seeding, or a bounded horizon that saturates at the floor — disclosed as crossovers; real ladders add exactly these to fight the drift.
**8. What does the verdict session check?** Reproduce the verifier byte-for-byte under SEED=20260717, match the results-dict sha256 exactly, and confirm G1/G2/G3 with all_pass=true, first_failing_gate=null, exit 0.

## Outcome
Verifier + doc authored; gates G1 (mean-drift deflation z=-78.058838) / G2 (churn-ledger identity, max residual 0.0) / G3 (shifted deeper-floor deflation z=-131.368189, shifted drift -797.745574 < baseline -498.683032) pass at the z_gate=3.0 bar; results-dict sha256 dcf252dd29f271a68a835046ea712256841c39fb657fc04c4f0aa8747e5855db disclosed in the doc; outbox PROPOSAL 167 appended sim-ready, proposal high-water advanced P166 -> P167; claim released. (Status flipped to complete as the final commit.)

## ⟲ Previous-session review
P166 (full-ratchet convexity, round-39 VENTURE, sim-ready -> V179) advanced round-39 to the VENTURE slot. This slice advances the rotation to the GAME slot per the fleet -> venture -> game -> unrelated order; offset held at +13 (P167 -> V180). No regressions to prior high-waters (union-max).

## 💡 Session idea
A companion game head: anti-deflation controls are themselves a mechanism — a rating FLOOR converts the smooth deflation into a reflected random walk whose stationary mean sits a predictable distance above the floor, so a ladder's effective skill zero-point is floor + E[climb], and mismatched floors across regions manufacture cross-region rating incomparability. Candidate for a later round.
