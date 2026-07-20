# PROPOSAL 200 — Banach's matchbox problem: residual matches in the other box (P200 → V213, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD.** This card is committed `in-progress` on commit 1 to hold the PR red (the intended born-red HOLD); the substrate-gate stays red until this line flips to `complete` on the final commit. The gate red is the HOLD, not a defect.

## Objective
Author and land PROPOSAL 200 in the round-47 UNRELATED slot (ideas/fleet/): a counterintuitive-but-exactly-true probability head — in **Banach's matchbox problem**, when you first find one of two N-match boxes EMPTY, the OTHER box still holds on average E[K] = (2N+1)·C(2N,N)·2^(−2N) − 1 ≈ 2·sqrt(N/π) − 1 matches — about 7 at N=50, NOT the ≈0 that the "symmetry ⇒ both boxes empty" folk intuition suggests. Pairs to sim-lab VERDICT 213 (+13 offset).

## Constraints honored
- Born-red card `in-progress` on commit 1; flipped `complete` LAST.
- Verifier stdlib-only (hashlib, json, math, random, fractions), SEED=20260717, deterministic across in-process double-run + two separate process invocations (same 64-hex digest confirmed twice).
- Gates: G1 exactly-true (closed-form pmf == exact forward-DP pmf, Fraction-exact, N∈{10,50}), G2 ≥3σ folk refutation (z2 = sim_mean/se at N=50), G3 agreement (|z3|<3 vs closed form), G4 robustness/shift (ratio (E[K]+1)/sqrt(N) in [1.10,1.20], strictly decreasing, → 2/√π). Directions stated per gate.
- External grounding (Wikipedia "Banach's matchbox problem" revision, oldid + raw-wikitext sha1), not a house self-reference.
- Merge-on-green only; no manual/agent merge; no model version identifiers; timestamps from `date -u`.

## GROUNDING (verified at HEAD)
https://en.wikipedia.org/w/index.php?title=Banach%27s_matchbox_problem&oldid=1356179739@2a9bfea32a4ea817258b2a97ef8366cbaf7e6ec3 · fetched 2026-07-20 — the "Solution" section states the head verbatim: P[K=k] = C(2N−k, N−k)(1/2)^(2N−k) (equal to C(2N−k, N)·2^(−(2N−k)) by binomial symmetry), the asymptotic E[K] ≈ 2·sqrt(N/π) − 1, and "starting with boxes with N=40 matches, the expected number of matches in the second box is approximately 7." The pinned SHA-1 is the raw-wikitext sha1 (self-computed = MediaWiki's stored revision sha1, byte-exact). Caveat: raw wikitext bytes, not rendered HTML; the closed forms live in `<math>` LaTeX markup, and the printed expectation expression carries a wikitext typo ("r"), but the P[K=k] formula and the 2·sqrt(N/π)−1 asymptotic are unambiguous.

## Probe questions
**1.** What is this really? — the residual K in the OTHER box when one N-box is first found empty; K is emphatically NOT 0.
**2.** Surprising? — yes; "symmetry ⇒ both empty ⇒ K≈0" is the trap; E[K]≈7 at N=50.
**3.** Exactly true? — yes; closed-form pmf == exact forward-DP pmf elementwise (Fraction-exact) and E[K]closed == Σk·pmf, N∈{10,50}.
**4.** Deterministic (stdlib)? — yes; results_sha256 e162890959…c576f56, byte-identical across in-process double-run + two invocations.
**5.** Refuted by? — any pmf mismatch, wrong-sign E-gap, z2<3σ, |z3|≥3, or a ratio out of band / non-monotone.
**6.** Distinct? — yes; no prior Banach/matchbox head; nearby heads (birthday-collision, coupon-collector, german-tank, inspection-paradox) are different mechanisms.
**7.** Grounding real? — yes; dedicated Solution section in the pinned Wikipedia revision, byte-pinned sha1.
**8.** Unblocks? — a residual-negative-binomial primitive + an exact-pmf-vs-forward-DP harness for sim-lab.

## Outcome
Verifier all_pass=True (G1–G4), results_sha256 e162890959eba728cf83004508a213f3585009bcc8fbc6e8bebdab753c576f56; z2=1839.497873 (folk refutation), z3=0.681218 (agreement); E[K](50)=7.038513, P(K=0)(50)=0.079589; ratios N=10→1.170086, N=50→1.136817, N=200→1.130493 (→ 2/√π=1.128379). Proposal doc + outbox block staged; proposal high-water advanced to P200 (union-max). Doc: ideas/fleet/banach-matchbox-residual-2026-07-20.md.

## ⟲ Previous-session review
Reviewed P199 (Vickrey second-price truthful dominance, round-47 GAME, P199→V212): a mechanism-design head whose G1 asserts exhaustive integer-exact weak dominance and G2 a Fraction-exact expectation contrast, with the born-red HOLD + flip-last pattern. The same "closed-form == exhaustive/exact leg" exact-agreement discipline is carried forward here as G1 (closed-form pmf == exact forward-DP pmf, Fraction-exact). No correction needed; the born-red HOLD and cross-invocation digest posture are the template this card follows.

## 💡 Session idea
A reusable **residual-distribution harness** for ideas/fleet: a tiny stdlib kernel that pairs a closed-form pmf with an independent exact forward-DP enumerator over an absorbing-state space and auto-checks Fraction-exact elementwise equality plus a seeded Monte-Carlo z-contrast, so future "counterintuitive residual/waiting-time" heads (negative-binomial residuals, gambler's-ruin end-states, occupancy tails) reuse one audited exact-vs-DP core instead of re-deriving the enumerator each time.
