# PROPOSAL 199 — Vickrey second-price auction: truthful bidding is weakly dominant (P199 → V212, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD.** This card is committed `in-progress` on commit 1 to hold the PR red (the intended born-red HOLD); the substrate-gate stays red until this line flips to `complete` on the final commit. The gate red is the HOLD, not a defect.

## Objective
Author and land PROPOSAL 199 in the round-47 GAME slot (ideas/superbot-games/): a counterintuitive-but-exactly-true mechanism-design head — in a sealed-bid **second-price (Vickrey)** auction, bidding your true value is a weakly dominant strategy, and the same shade s(v) = ⌊v·(n−1)/n⌋ that is optimal in a first-price auction never helps in Vickrey. Pairs to sim-lab VERDICT 212 (+13 offset).

## Constraints honored
- Born-red card `in-progress` on commit 1; flipped `complete` LAST.
- Verifier stdlib-only (hashlib/json/math/fractions/itertools/random), SEED=20260717, deterministic across in-process double-run + two separate process invocations.
- Gates: G1 exhaustive integer-exact dominance (0 deviations), G2 Fraction-exact expectation contrast, G3 ≥3σ Monte-Carlo surprise, G4 robustness/shift. Directions stated per gate.
- External grounding (Wikipedia Vickrey-auction revision, oldid + raw-wikitext sha1), not a house self-reference.
- Merge-on-green only; no manual/agent merge; no model version identifiers; timestamps from `date -u`.

## GROUNDING (verified at HEAD)
https://en.wikipedia.org/w/index.php?title=Vickrey_auction&oldid=1338833083@398d2e4148cc7ee83f1343f720f6e243926bb895 · fetched 2026-07-20T05:26:52Z — the "Proof of dominance of truthful bidding" section states and proves the head; the pinned SHA-1 is the raw-wikitext sha1 (matches MediaWiki's stored revision sha1). Caveat: raw wikitext bytes, not rendered HTML.

## Probe questions
**1.** What is this really? — the second-price *pricing rule* (not the sealed-bid format) is what makes truth dominant.
**2.** Surprising? — yes; "always shade" is right in first-price, wrong in second-price.
**3.** Exactly true? — yes; 0/245 profitable deviations (integer-exact) + Fraction-exact E-gaps.
**4.** Deterministic (stdlib)? — yes; results_sha256 a96d59f3…6527c, byte-identical across invocations.
**5.** Refuted by? — any profitable deviation, wrong-sign E-gap, first-price z<3σ, or Vickrey z>0.
**6.** Distinct? — yes; no prior Vickrey/VCG head; "second-price" elsewhere is scenario dressing.
**7.** Grounding real? — yes; dedicated proof section in the pinned Wikipedia revision.
**8.** Unblocks? — a strategyproof sealed-bid primitive + an exact-dominance/contrast harness for sim-lab.

## Outcome
Verifier all_pass=True (G1–G4), results_sha256 a96d59f378e5d04a4e211dafafa22244e09d22126ba2c9b1e5f1cc0bdeb6527c; proposal doc + outbox block staged; proposal high-water advanced to P199. Doc: ideas/superbot-games/vickrey-truthful-dominance-2026-07-20.md.

## ⟲ Previous-session review
Reviewed P198 (Weitzman's Pandora's Box, round-47 VENTURE, #735, landed at a69cc7c): a clean index-rule head whose gate asserts the closed-form index rule EXACTLY equals the brute-force optimum. The same "closed-form == exhaustive" exact-agreement discipline is carried forward here as G1/G2. No correction needed; its born-red HOLD + flip pattern is the template this card follows.

## 💡 Session idea
A reusable mechanism-design harness module for superbot-games: a tiny stdlib kernel exposing `{first_price, second_price, all_pay}` payoff functions plus an exhaustive weak-dominance enumerator and a seeded Monte-Carlo z-contrast, so future strategyproofness heads (VCG, Gibbard–Satterthwaite counterexamples, all-pay war-of-attrition) reuse one audited core instead of re-deriving the enumerator each time.
