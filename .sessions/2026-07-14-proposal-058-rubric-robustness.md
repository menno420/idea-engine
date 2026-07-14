# Session — PROPOSAL 058: rubric weight-robustness — is the fresh 7-concept batch's band partition an artifact of the fifth decimal of a judgment-call weight vector? (VENTURE rotation, round 11, PRODUCTS half)

> **Status:** `complete`
> **Model/time:** fable · 2026-07-14T04:04:15Z (Ideas Lab worker slice — draft the
> round-11 VENTURE slot proposal, PRODUCTS half, under standing owner ORDER
> 003/004. Card born in-progress as the designed gate hold; flipped complete in
> this PR's final commit at 2026-07-14T04:15:03Z)

**📊 Model:** fable-family · content + outbox proposal + ONE surgical checker
fix (idea file, card, lane index row, outbox append, claim file, and a
disclosed mid-session repair to `scripts/check_sections.py` — see 💡 below;
no control/status.md or control/inbox.md writes; nothing in sim-lab)

## Scope

Draft a genuinely new sim-shaped idea for the VENTURE rotation slot, round 11,
PRODUCTS half, under standing owner ORDER 003 (continuous pipeline) and ORDER
004 rule 3. Round 11 opened at fleet backlogs with P057 (#391), so the venture
slot is next; the slot's own half-alternation (P018 B → P022/P026 T → P030 B →
P034 T → P038 B → P042 P → P046 B → P050 P → P054 B) puts round 11 on the
PRODUCTS half.

Harvested head: venture-lab's fresh 7-concept ideation batch
`docs/products/ideas-2026-07-13-night.md`, read FIRSTHAND at venture-lab HEAD
`a9e202d69433dc69623a78dd3164ac4689d7c8f0` — the full 7 × 5 per-criterion
score table at the shipped rubric weights (Distribution 35 / Buildability 20 /
Launch-effort 15 / Speed 15 / WTP 15) and the rubric's own bands at 3.0/3.5 —
priced for weight-robustness: exact critical jitter radius per concept
(linear-fractional vertex arithmetic, seedless Fractions; drafting-time
x\*₁ = 1/27 ≈ ±3.70% and x\*₆ = 1/47 ≈ ±2.13% on the two knife-edge rows) plus
seeded-MC flip probability of the induced partition (≈ 0.225 at ±10%). This is
the P050 card's recorded re-openable runner-up ("the otherwise-attractive
rubric-weights head was UNDRAFTABLE (its honest sim needs the doc's actual
score table …) — the day a venture read is available"), now unlocked: the read
is available and the fresh batch publishes the full table. It also answers
P042's recorded drop reason (whether Distribution-35 is RIGHT is a judgment
call — whether the partition DEPENDS on the judgment call within a stated
neighborhood is falsifiable arithmetic).

Deliverables this slice: this card (born-red first commit), the claim file,
`ideas/venture-lab/rubric-weight-robustness-2026-07-14.md` + the
`ideas/venture-lab/README.md` index row, the `control/outbox.md` PROPOSAL 058
append, and the disclosed `scripts/check_sections.py` registry-only-seat fix.
Seeds 20261369–372 strictly above the P057 high-water 20261368. PR #395.

## Constraints honored

- control/status.md and control/inbox.md untouched (coordinator/manager-only).
- sim-lab read-only (dedup ledger read at origin/main `311c461`; the live V068
  session's PR #126 and claim untouched).
- Open claims and PRs of other sessions untouched (the order-008 housekeeping
  claim; PRs #361/#364 parked owner-held — none mine).
- Outbox append-only (appended via shell, never loaded into an editor); no
  renumbering; all timestamps from real `date -u`.
- One scripts/ change, disclosed: a genuine fleet-wide CI red (upstream roster
  format drift) repaired in the narrowest way the checker's own error message
  prescribes ("roster format changed? update this parser"); everything else
  content-only.

## 💡 Session idea

**A checker that fetches a LIVE upstream at gate time makes every PR hostage
to another repo's format drift — and this parser's own comment history shows
the drift class is recurring, so the two repos need a row-class CONTRACT, not
a fourth skip heuristic.** Hit live this slice: `check_sections.py` fetches
fleet-manager's `docs/roster.md` at CI time; the roster regenerated
mid-session and added grouped registry-only seat rows (`SuperBot World seat
(games+idle+mineverse)`, `Ideas Lab seat (idea-engine+sim-lab)`, …) whose
"no repo" declaration lives in the HEARTBEAT cell, not the Lane cell — the
parser (correctly) failed LOUD, which redded every non-control preflight in
the fleet between this session's recon (~03:50Z, green) and its drafting
(~04:12Z, red). The fix was an 11-line heartbeat-cell skip, but it is the
FOURTH format-drift repair recorded in the parser's own comments (the second
table, the `↳` sub-rows, the Lane-cell "no repo" seats, now the
heartbeat-cell seats). Each drift lands as a fleet-wide outage until some
mid-task session repairs it. The durable fix is a generator-side contract:
the roster generator stamps a machine token per row class (e.g. a literal
`registry-only` token in the Lane cell, by documented contract with this
parser), so future row classes are additive instead of breaking — worth an
outbox/manager routing note the next time a fleet-process head is drafted;
recorded here so the pattern stops being re-discovered one outage at a time.

## ⟲ Previous-session review

Previous card (`.sessions/2026-07-14-proposal-057-paper-lane-beat-coin.md`,
P057 drafter): its 💡 — pre-register the ALGORITHM shape for
threshold-crossing rows (float-scan-then-exact-verify), because exact-Fraction
scans over hundreds of candidates are where "exact everywhere" turns hostile —
held up as a design constraint here, applied one level earlier: P058's exact
arm was SHAPED so no scan exists at all (critical radii come from 32 per-vertex
LINEAR solves, each one exact division, because the perturbed total is
linear-fractional in the jitter factors), and the registration pins that
construction explicitly rather than leaving the implementer to invent a
scan. Its other observation — that the seed-sweep recipe lives as oral
tradition in cards and claims — is still true and got MORE true this session
(re-derived again from the recon report); it now shares a root cause with
this session's 💡: recurring session-derived procedures (seed sweep, roster
skip taxonomy) that belong in committed one-liners/contracts. Clean card
otherwise; its rotation statement ("round 11 reopens at fleet backlogs")
made this slice's slot derivation a one-line read.
