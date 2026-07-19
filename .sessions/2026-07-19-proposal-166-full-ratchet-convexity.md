# PROPOSAL 166 — full-ratchet anti-dilution turns a linear down-round into a convex transfer of ownership from founders to the ratcheted investor (round-39 VENTURE slot, P166 -> V179, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card lands first with `Status: in-progress` to hold the PR red on the substrate gate; it flips to `complete` as the final commit, after the outbox block + heartbeat, releasing the landing workflow. A red gate before that flip is the HOLD, not a defect.

## Objective
Author round-39 VENTURE-slot PROPOSAL 166 — the full-ratchet anti-dilution convexity head — with a stdlib firsthand verifier (SEED=20260717; >=3 sigma gates including a robustness gate under a shifted distribution) and a live-grounded proposal doc, targeting sim-lab VERDICT 179 (+13 offset).

## Constraints honored
- Merge-on-green only; zero merge calls; PR opens READY.
- WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest posture; deterministic in-process double-run; cross-invocation identical.
- Grounding URL verified live this session (oldid pinned).
- No model version identifiers in artifacts; family names only. Timestamps from date -u.

## GROUNDING (verified at HEAD)
Full-ratchet vs broad-based weighted-average anti-dilution: on a down round a full ratchet resets the earlier investor's conversion price all the way to the new (lower) price, multiplying their as-converted shares by 1/p (p = new/old price ratio), while weighted-average only partially adjusts toward the blended price. The extra common-equivalent shares issued to the ratcheted investor scale as 1/p - 1 = d/(1-d) in the drop d, which is convex — so deepening the down round transfers ownership from common super-linearly, not proportionally.

## Probe questions
**1. Is the convexity an artifact of counting extra shares rather than ownership fraction?** No — founder ownership loss = N_C*dAD/(T*(T+dAD)) composes an increasing map with dAD = N_A*(1/p-1), itself convex in the drop; the verifier measures the ownership fraction directly and its second difference stays positive.
**2. Could weighted-average ever exceed full-ratchet dilution?** No — full ratchet is the maximal conversion-price reset (all the way to the new price), so dAD_FR >= dAD_WA for every drop; G1 tests the strict gap at >=3 sigma.
**3. Does the effect vanish for shallow down rounds?** As p approaches 1 both formulas converge and the gap closes; the disclosed crossover shows FR approximately WA near a flat round and the transfer opening as the drop deepens — the claim is bounded to genuine down rounds.
**4. Is the proportional folk belief a strawman?** It stands in for the common expectation that a d-percent down round costs founders roughly proportionally; G2 rejects it because full-ratchet loss at double depth exceeds twice the single-depth loss (super-linear) at >=3 sigma.
**5. Are FR and WA compared on the same sampled scenarios?** Yes — each scenario draws one (cap-table, drop, money) tuple and evaluates both formulas on it; the difference is within-scenario so the gate is a paired test, conservative on SE.
**6. Does the digest depend on machine floats?** Floats are rounded to 6 dp before hashing; the canonical-dict sha256 is asserted stable in-process and reproduced cross-invocation on the same runtime.
**7. What breaks the convex transfer first?** Pay-to-play forfeiture, carve-outs/exemptions, and narrow-vs-broad base change the magnitude; a full pay-to-play can strip anti-dilution from a non-following investor — disclosed as crossovers, bounding the claim to a standard ratchet with no forfeiture.
**8. What does the verdict session check?** Reproduce the verifier byte-for-byte under SEED=20260717, match the results-dict sha256 exactly, and confirm G1/G2/G3 z-margins with all_pass=true, exit 0.

## Outcome
(pending — flips to complete as the final commit.)

## ⟲ Previous-session review
P165 (memoryless-PM-waste, round-39 FLEET, sim-ready -> V178 pending) opened round-39 at the FLEET slot. This slice advances the rotation to the VENTURE slot per the fleet -> venture -> game -> unrelated order; offset held at +13 (P166 -> V179). No regressions to prior high-waters (union-max).

## 💡 Session idea
A companion venture head: pay-to-play interacts with the ratchet nonlinearly — an investor who declines to follow-on can forfeit anti-dilution, so the convex transfer is contingent on continued participation; modeling the follow-on decision as a threshold on expected dilution avoided vs check size yields a founder-favorable region where a deep enough ratchet deters the very follow-on that triggers it. Candidate for a later round.
