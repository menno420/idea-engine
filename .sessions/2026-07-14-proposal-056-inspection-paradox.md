# Session — PROPOSAL 056: the inspection paradox — does the "average wait = half the average headway" folk rule survive random incidence, or does headway variability inflate every real wait? (COMPLETELY-UNRELATED rotation, round 10 closer)

> **Status:** `complete`
> **Model/time:** fable · 2026-07-14T02:47:26Z (Ideas Lab worker slice — draft the
> COMPLETELY-UNRELATED rotation round-10 closer under standing owner ORDER 003/004.
> Card born in-progress as the designed gate hold; flipped complete in this PR's
> final commit at 2026-07-14T02:53:47Z once the 💡 slot resolved)

**📊 Model:** fable-family · content + outbox proposal only (idea file, card,
fleet index row, outbox append, claim file; no control/status.md or
control/inbox.md writes; no checker or script changes; nothing in sim-lab)

## Scope

Draft a genuinely new sim-shaped idea for the COMPLETELY-UNRELATED rotation
slot, round 10 closer, under standing owner ORDER 003 (continuous pipeline)
and ORDER 004 rule 3 ("Rotate lanes deliberately: fleet backlogs → venture's
book/product space → game mechanics → COMPLETELY UNRELATED domains"). Round
10 opened at fleet backlogs with P053 (#379), served venture with P054
(#382) and game mechanics with P055 (#385), so this head closes the round.
The slot's own spacing-4 history (P017, P024, P028, P032, P036, P040, P044,
P048, P052 → P056) confirms.

Domain: a TENTH fleet-external domain — **renewal theory & random incidence
(the inspection / waiting-time paradox)** — disjoint from the nine prior
occupants: social choice (P017), congestion routing (P024), tournament
seeding (P028), pattern races (P032), optimal stopping (P036), spatial
self-organization (P040), queue discipline (P044), stochastic ratchets
(P048), occupancy & collection (P052).

Deliverables this slice: this card (born-red first commit), the claim file,
`ideas/fleet/inspection-paradox-wait-inflation-2026-07-14.md` + the
`ideas/fleet/README.md` index row, and the `control/outbox.md` PROPOSAL 056
append. Seeds 20261361–364 strictly above the P055 high-water 20261360.

## 💡 Session idea

**The seed sweep should be band-agnostic and classify hits by CONTEXT, not by
digit count — because the trap class is bigger than Fraction numerators.**
The inherited P046–P055 sweep recipe pins the band (`20261[0-9]{3}`) and
carries a memorized exception list (20261542/20261664/20261833 = numerator
substrings). This session's boundary-aware sweep
(`(^|[^0-9])2026[0-9]{4,6}([^0-9]|$)`) surfaced a NEW specimen the recipe's
band can never see: a standalone 9-digit numeral `202670087` in sim-lab —
which turned out to be the decimal-fraction digits of `"delta_cond":
0.202670087` (verdict-032 results.json line 12401), data, not a seed. The
asymmetry is the point: a data numeral mistaken for a seed only WASTES
headroom (the next block allocates above it, harmlessly), but a REAL
out-of-band seed allocation invisible to the band regex COLLIDES the next
block — so the sweep must widen the match first and demote hits to data by
reading their context (a decimal point, a numerator position, a quoting
sentence), never by their length or by a remembered exception list. The
recipe refinement is one line: match any digit-boundary numeral at seed
magnitude or above, then classify each surviving hit at its source line.
**Dedup** (this slice, `rg -i 'band-agnostic|decimal.fraction|202670087'
ideas/ .sessions/` kit-excluded): no card or idea names the
classify-by-context rule or the decimal-fraction specimen; prior cards carry
only the Fraction-numerator exception list this refines.

## ⟲ Previous-session review

Newest predecessor card
(`.sessions/2026-07-14-proposal-055-badge-saturation.md`, P055 drafter,
round-10 GAME-MECHANICS slot): closed clean and paid forward twice here —
its seed-sweep line (high-water 20261360, the sweep-recipe trap
re-documented) let this slice allocate 20261361–364 in one pass, and its
fragility-disclosure norm ("name the surviving discriminator cell") is
carried into this head's registration: JITTER at ρ = 1.04 disclosed
APPROVE-side and SPREAD disclosed exactly ON the 11/10 band edge, so the
REJECT-first registration stays honest. One push further this slice: P055's
sweep line still used the band regex `20261[0-9]{3}` — exactly the recipe
this session found incomplete (a 9-digit decimal-fraction specimen sits
outside any band it can match), so this card's 💡 is the direct next
precision step on the lane's own inherited tool, the same
refine-the-inheritance move P055's ⟲ made on P054's walls-are-session-scoped
finding.