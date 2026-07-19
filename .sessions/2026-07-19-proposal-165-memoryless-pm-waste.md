# PROPOSAL 165 — preventive maintenance of a memoryless component is pure waste: age replacement holds the unplanned-failure rate at exactly λ while raising cost rate (round-39 FLEET slot, P165 -> V178, +13)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card lands first with `Status: in-progress` to hold the PR red on the substrate gate; it flips to `complete` as the final commit, after the outbox block + heartbeat, releasing the landing workflow. A red gate before that flip is the HOLD, not a defect.

## Objective
Author round-39 FLEET-slot PROPOSAL 165 — the age-replacement memoryless-maintenance null — with a stdlib firsthand verifier (SEED=20260717; >=3 sigma gates including a robustness gate under a shifted distribution) and a live-grounded proposal doc, targeting sim-lab VERDICT 178 (+13 offset).

## Constraints honored
- Merge-on-green only; zero merge calls; PR opens READY.
- WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest posture; deterministic in-process double-run; cross-invocation identical.
- Grounding URL verified live this session (oldid pinned).
- No model version identifiers in artifacts; family names only. Timestamps from date -u.

## GROUNDING (verified at HEAD)
Reliability-centered maintenance + the memoryless property: age-based scheduled replacement reduces failures only for wear-out (increasing-hazard) items; for a constant-hazard (exponential) component a survived unit is as-good-as-new, so early replacement cannot lower the failure rate — it only adds planned-swap cost.

## Probe questions
**1. Is the failure-rate invariance an artifact of the chosen threshold T?** No — for the exponential the renewal-reward algebra gives failure rate = F(T)/E[cycle] = lambda for every finite T; the verifier confirms it across a shifted (lambda-prime, T-prime) world.
**2. Could the cost penalty vanish if planned replacement were nearly free?** As c_plan approaches 0 the penalty shrinks but stays > 0 for any finite T; run-to-failure is still the cost optimum for constant hazard.
**3. Does this contradict real PM programs that do cut failures?** No — those items have increasing hazard (wear-out). The Weibull(shape 2.5) crossover in the verifier shows a finite T-star that beats run-to-failure, bounding the claim to non-increasing hazard.
**4. Is the 10% promised reduction a strawman?** It is a stand-in for the folk expectation that PM cuts failures; the gate rejects it at >=3 sigma because the measured reduction is statistically zero.
**5. Are the two policies compared on the same noise?** They are run as independent replicates; the difference SE combines both, so z is conservative (paired sampling would only tighten it).
**6. Does the digest depend on machine floats?** Floats are rounded to 6 dp before hashing; the canonical-dict sha256 is stable in-process (asserted) and cross-invocation on the same runtime.
**7. What breaks the invariance first?** Any departure from constant hazard (aging, imperfect repair, or replacement lead-time), disclosed as crossovers in the doc.
**8. What does the verdict session check?** Reproduce the verifier byte-for-byte under SEED=20260717, match the results-dict sha256 exactly, and confirm G1/G2/G3 z-margins with all_pass=true, exit 0.

## Outcome
Verifier + doc authored; gates G1/G2/G3 pass at >=3 sigma; results-dict sha256 disclosed in the doc; outbox PROPOSAL 165 appended sim-ready, proposal high-water advanced P164 to P165. (Status flips to complete as the final commit.)

## ⟲ Previous-session review
P164 (friendship paradox, round-38 UNRELATED, PR #638) landed sim-ready -> V177 pending. This slice opens round-39 at the FLEET slot per the fleet -> venture -> game -> unrelated rotation; offset held at +13 (P165 -> V178). No regressions to prior high-waters (union-max).

## 💡 Session idea
A companion FLEET head: replacement lead-time turns the memoryless null into a strict LOSS — under nonzero repair/procurement delay, even run-to-failure of a constant-hazard unit carries an availability tax that scales with delay/MTBF, so the real lever is spares depth (Palm), not PM cadence. Candidate for a later round.
