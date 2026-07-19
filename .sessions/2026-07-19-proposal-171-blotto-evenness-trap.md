# PROPOSAL 171 — the Colonel Blotto evenness trap: in a symmetric resource-allocation contest with equal budgets, spreading your budget EVENLY across every battlefield is a losing strategy — a lopsided allocator that CONCEDES a minority of fields and OVERLOADS the rest wins the majority of battlefields against a uniform splitter, and keeps winning the majority even while spending up to nearly HALF LESS budget (round-40 GAME slot, P171 -> V184, +13)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card lands first with `Status: in-progress` to hold the PR red on the substrate gate; it flips to `complete` as the final commit, after the outbox block, releasing the landing workflow. A red gate before that flip is the HOLD, not a defect.

## Objective
Author round-40 GAME-slot PROPOSAL 171 — the Colonel Blotto evenness-trap head — with a stdlib firsthand verifier (SEED=20260717; >=3 sigma gates including a robustness gate under a shifted distribution) and a live-grounded proposal doc, targeting sim-lab VERDICT 184 (+13 offset).

## Constraints honored
- Merge-on-green only; zero merge calls; PR opens READY.
- WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest posture; deterministic in-process double-run; cross-invocation identical.
- Grounding URL verified live this session (revision pinned).
- No model version identifiers in artifacts; family names only. Timestamps from date -u.

## GROUNDING (verified at HEAD)
Colonel Blotto game (Borel 1921; Roberson 2006): two players simultaneously distribute a fixed budget of resources across N battlefields; each field goes to whoever commits more, and the payoff is the count (or value) of fields won. The documented result is that spreading resources EVENLY is not a best response — asymmetric/randomized allocations dominate it, and a player can win a MAJORITY of battlefields against an equal-budget uniform opponent (and even, within a bounded budget deficit, against a richer one). Wikipedia "Blotto game" verified live this session (HTTP 200, revision pinned in the proposal doc).

## Pre-registered Gate-plan (APPROVE iff ALL hold, in order G1 -> G2 -> G3; z_gate=3.0)
- **G1 evenness-beaten (head)** — with EQUAL budgets, a concede-and-overload allocator (concede the largest minority of fields that still leaves a winning majority, dump the whole budget on the rest) wins strictly MORE than half the battlefields against a uniform splitter, at >=3 sigma across randomized battlefield counts — rejecting the folk null that equal budgets force an equal 0.5 share.
- **G2 concede-arithmetic identity (mechanism anchor)** — across a deterministic (B, concede-count, deficit) sweep the real concede-and-overload game's battlefield share equals the closed-form concede-arithmetic prediction with EXACTLY zero mismatches, and the majority-feasibility deficit frontier approaches 1/2 as the field count grows (a winning k exists whenever deficit*B < k < B/2). This proves the whole effect is the concede-overload arithmetic, and prices the "cheaper AND still wins" claim.
- **G3 robustness / heterogeneous-value deficit (shifted world)** — under RANDOM per-field values AND a 40% budget deficit, the value-targeted concede-and-overload (concede the cheapest fields, overload the dearest) still wins >0.5 of the total VALUE at >=3 sigma AND deepens versus the homogeneous equal-budget baseline.

## Probe questions
**1. Is "spread evenly" a strawman opponent?** No — uniform allocation is the natural, intuitive "fair" split and the folk optimum; the head is precisely that this intuitive strategy is dominated. The gate compares against exactly that uniform splitter.
**2. Could the win be an artifact of tie-breaking?** No — the concede-and-overload allocator wins overloaded fields STRICTLY (per-field allocation strictly exceeds the uniform 1.0) and loses conceded fields outright; G2's zero-mismatch identity confirms no field is decided by a tie in the head regime.
**3. Does the majority win survive a real budget deficit, or only at equal budget?** It survives a deficit approaching one half — G2's frontier shows a winning concede-count exists whenever the deficit is below ~1/2, and the deficit-demo run has the allocator spend 40% less and still take the field majority.
**4. Is the effect just the deterministic algebra of one configuration?** No — G1 and G3 randomize the battlefield count (and G3 the field values), so the >=3 sigma result is across a distribution of contests, not one lucky board.
**5. What is the counterintuitive core?** Equal budget does NOT buy equal share: concentrating force beats spreading it, so a "fair" even split loses the majority of fields to a lopsided opponent spending the same or less.
**6. Determinism?** SEED=20260717 pinned; run() executed twice in-process, compact-canonical serializations asserted byte-identical before hashing; floats rounded 6 dp; no set/dict-ordering nondeterminism (sort_keys).
**7. Real or toy?** Colonel Blotto is a textbook model for RTS/MOBA lane and army-split decisions, tower-defense placement, stat/power budgeting, ad-auction and political-campaign spend — anywhere a fixed budget is divided across contested fronts. The uniform-is-dominated result is the documented core, not a toy.
**8. What does the verdict session check?** Reproduce the verifier byte-for-byte under SEED=20260717, match the results-dict sha256 exactly, and confirm G1/G2/G3 with all_pass=true, first_failing_gate=null, exit 0.

## Outcome
Verifier + doc authored; gates G1 (evenness-beaten, equal-budget concede-overload mean battlefield share 0.537637 vs the 0.5 null, z=25.27061) / G2 (concede-arithmetic identity, 0 mismatches over 14421 checks, deficit frontier B8:0.37 / B20:0.44 / B40:0.47 -> 1/2) / G3 (heterogeneous-value 40%-deficit value-targeted share 0.788032 > baseline 0.537637, z=112.524168) pass at the z_gate=3.0 bar; deficit-demo confirms the challenger wins the field majority (share 0.553794, z=40.335299) while spending 40% LESS; results-dict sha256 05afdeffd9f44721fd6e71ee4595a024541b99976176bd30449b043c1755be63 disclosed in the doc; outbox PROPOSAL 171 appended sim-ready, proposal high-water advanced P170 -> P171; claim released. (Status flipped to complete as the final commit.)

## ⟲ Previous-session review
Round-40 opened at the FLEET slot (P169 sqrt-safety-staffing -> V182) and advanced through the VENTURE slot (P170 term-sheet winner's curse). This slice advances the rotation to the GAME slot per the fleet -> venture -> game -> unrelated order; offset held at +13 (P171 -> V184). No regressions to prior high-waters (union-max).

## 💡 Session idea
A companion game head: the SAME concede-and-overload logic inverts under a "majority contest with unequal field VALUES and a reveal delay" — if the uniform player can observe one of the conceded fields before committing, the Blotto advantage collapses to a second-mover information game, pricing exactly how much scouting/vision is worth as a budget-equivalent. Candidate for a later round.
