# Session — PROPOSAL 057: the paper lane's BEAT coin — trade P&L cancels exactly out of the committed cycle-window verdict, the null window coin sits ABOVE the fair line, and the count grammar cannot see skill at first-year n (FLEET-BACKLOGS rotation, round 11 opener)

> **Status:** `complete`
> **Model/time:** fable · 2026-07-14T03:23:50Z (Ideas Lab worker slice — draft the
> FLEET-BACKLOGS rotation round-11 opener under standing owner ORDER 003/004.
> Card born in-progress as the designed gate hold; flipped complete in this PR's
> final commit at 2026-07-14T03:31:58Z once the 💡 slot resolved)

**📊 Model:** fable-family · content + outbox proposal only (idea file, card,
lane index row, outbox append, claim file; no control/status.md or
control/inbox.md writes; no checker or script changes; nothing in sim-lab)

## Scope

Draft a genuinely new sim-shaped idea for the FLEET-BACKLOGS rotation slot,
round 11 OPENER, under standing owner ORDER 003 (continuous pipeline) and
ORDER 004 rule 3 ("Rotate lanes deliberately: fleet backlogs → venture's
book/product space → game mechanics → COMPLETELY UNRELATED domains"). Round
10 closed fully served: fleet backlogs → P053 (#379), venture → P054 (#382),
game mechanics → P055 (#385), COMPLETELY UNRELATED → P056 (#387) — so round
11 reopens at fleet backlogs. Slot rounds 1–10 harvested websites ×2,
superbot ×2, substrate-kit ×2, fleet-manager, curious-research ×2,
superbot-mineverse; round 11 rotates the harvest source to a repo this slot
has NEVER drawn: **trading-strategy** (its three prior pipeline taps P022/
P026/P034 were all the VENTURE slot's trading half — different slot,
different documents, disclosed below and in the idea file).

Harvested head: the paper lane's pre-registered grading grammar —
`docs/paper-lane-protocol.md` §7 (cycle-window BEAT/MISS comparator,
ambiguity A6's committed claim that the cycle comparator is "the meaningful
reading that is *less* favorable to the strategy") read FIRSTHAND at
trading-strategy HEAD `d857e50ad7bc32bed5b2999cce16b4bf8a37246e` via
add_repo + shallow clone this session.

Deliverables this slice: this card (born-red first commit), the claim file,
`ideas/trading-strategy/paper-lane-beat-coin-2026-07-14.md` + the
`ideas/trading-strategy/README.md` index row, and the `control/outbox.md`
PROPOSAL 057 append. Seeds 20261365–368 strictly above the P056 high-water
20261364.

## Constraints honored

- control/status.md and control/inbox.md untouched (coordinator/manager-only).
- sim-lab read-only (dedup ledger read at origin/main `626d16e`).
- Open claims and PRs of other sessions untouched (the live V067 verdict
  claim, the order-008 housekeeping claim, the terminal P055/P056 drafter
  claims; PRs #361/#364 parked owner-held, #389 the prune fast-lane — none
  mine).
- Outbox append-only; no renumbering; all timestamps from real `date -u`.

## 💡 Session idea

**Pre-registered n* rows should pin the ALGORITHM shape, not just the
numbers: float-scan-then-exact-verify at the found n only.** This session's
drafting harness timed out (2-minute wall) trying to scan n = 8..∞ for the
power-≥ 1/2 crossing in exact `fractions.Fraction` arithmetic — binomial
tail sums over exact rationals grow quadratically in bigint size with n, so
an exact scan over hundreds of n values is the one place the pipeline's
"exact Fractions everywhere" reflex is actively hostile. The honest,
byte-stable recipe (used in P057's spec): scan in floats to LOCATE n*, then
verify the crossing pair (n* − 1, n*) exactly — two exact evaluations
instead of hundreds, same certainty, no timeout. Worth folding into the
sim-lab conventions doc the next time an n*/threshold-crossing row appears,
BEFORE a verdict session rediscovers the wall mid-run.

## ⟲ Previous-session review

Previous card (`.sessions/2026-07-14-proposal-056-inspection-paradox.md`,
P056 drafter): its 💡 — make the seed sweep band-agnostic and classify hits
by CONTEXT, not digit count — held up in practice this session: the
boundary-aware regex `(^|[^0-9])2026[0-9]{4,6}([^0-9]|$)` re-confirmed the
same three data-not-seed specimens (20261542/20261833/202670087) with zero
new false positives and caught the true high-water 20261364 first try. One
gap it left open: the sweep recipe still lives only in claim files and
cards, re-derived each session — it belongs in a committed one-liner script
so the trap knowledge stops being oral tradition.
