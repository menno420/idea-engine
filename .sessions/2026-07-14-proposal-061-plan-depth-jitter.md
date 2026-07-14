# Session — PROPOSAL 061: plan-queue depth vs refill-lag jitter — does the committed "DEPTH >= the cadence" bar actually keep the superbot plan queue never-dry? (FLEET-BACKLOGS rotation, round 12 opener)

> **Status:** `complete`
> **Model/time:** fable · 2026-07-14T06:26:27Z (Ideas Lab worker slice — draft the
> round-12 FLEET-BACKLOGS rotation slot proposal under standing owner
> ORDER 003/004. Card born in-progress as the designed gate hold; flipped
> complete in this PR's final commit at 2026-07-14T06:35:22Z)

**📊 Model:** fable-family · content-only slice (idea file, card, superbot index
row, outbox append, claim file; no scripts/, no control/status.md or
control/inbox.md writes; nothing in sim-lab or superbot)

## Scope

Draft a genuinely new sim-shaped idea for the FLEET-BACKLOGS rotation slot,
round 12 OPENER, under standing owner ORDER 003 (continuous pipeline) and
ORDER 004 rule 3 ("Rotate lanes deliberately: fleet backlogs → venture's
book/product space → game mechanics → COMPLETELY UNRELATED domains (I want
those too)"). Round 11 closed fully served (fleet backlogs → P057 #391,
venture → P058 #395, game mechanics → P059 #402, unrelated → P060 #404), so
round 12 reopens at fleet backlogs; the slot's own spacing-4 history (P019,
P021, P025, P029, P033, P037, P041, P045, P049, P053, P057 → P061) confirms.

Harvest source: superbot `docs/operations/autonomous-routines.md` +
`scripts/check_reconciliation_due.py`, read FIRSTHAND this session via
add_repo + shallow clone at superbot HEAD
`50481b7167e6315dd10f496deec8ac9f0dc03d77` — the slot's THIRD tap of the
superbot repo, DISCLOSED per the P053/P057 second-tap precedent, not hidden:
P021 and P033 both harvested the session-journal/assign-at-merge append
mechanics, while this head prices a document and a constant family neither
touched — the Q-0164 planning bar ("The bar is DEPTH >= the cadence — leave
enough genuine buildable work to reach the NEXT pass (~30 PRs of capacity)"),
the Q-0107/Q-0134 30-PR reconciliation band (`STEP = 30`,
`latest // STEP > marker // STEP`), the marker-reset-to-latest convention,
and the committed incident anchor ("The old '~9 PRs' horizon drained the
queue ~20 PRs before each refill").

Deliverables this slice: this card (born-red first commit), the claim file,
`ideas/superbot/plan-depth-refill-jitter-2026-07-14.md` + the
`ideas/superbot/README.md` index row, and the `control/outbox.md`
PROPOSAL 061 append. Seeds 20261381–384 strictly above the P060 high-water
20261380.

## Constraints honored

- control/status.md and control/inbox.md untouched (coordinator/manager-only).
- control/outbox-archive-2026-07-14.md untouched (rolled archive, terminal).
- sim-lab read-only (dedup ledger + seed sweep read on the local clone;
  nothing edited).
- Open claims and PRs of other sessions untouched (the live V070/V071
  verdict claims, the order-008 housekeeping claim; PRs #361/#364 parked
  owner-held — none mine).
- Outbox append-only (appended via shell, never loaded into an editor); no
  renumbering; all timestamps from real `date -u`.
- superbot read FIRSTHAND read-only (public shallow clone per the Q-0272
  standing authorization, re-read via superbot docs/fleet-reading-path.md @
  50481b7 this session); no superbot file edited.

## 💡 Session idea

**A committed convention can carry an unstated theorem — and the theorem is
what protects it from a well-meaning "fix".** The sharpest thing this harvest
found is not the fragility (depth 30 dries ≈ 17.6% of cycles under lag jitter)
but the virtue nobody wrote down: superbot's marker-reset-to-LATEST-PR rule
makes every refill window borrow back exactly the previous pass's lateness, so
"depth = cadence" is EXACTLY never-dry under any steady lateness — a property
that dies instantly if someone "corrects" the marker to the band crossing
(which looks more principled and is strictly worse). The durable pattern: when
a doc commits a convention alongside a constant, ask what invariant the
convention silently buys before pricing the constant — conventions accrete
load-bearing algebra that no checker guards and no doc line states, and the
cheapest permanent fix on any verdict branch is the one sentence that turns
the accident into a contract ("reset to latest, NOT the crossing — this is
what makes steady lateness free"). Priced here as gate F2 + a pre-registered
consequence line on every branch, so the theorem ships whichever way the
ruling lands.

## ⟲ Previous-session review

Previous card (`.sessions/2026-07-14-proposal-060-noisy-reciprocity.md`, P060
drafter): its 💡 — a dedup-DROP with a recorded REASON is a harvest lane
because the reason is the expiry condition — is the round's best process find,
and this slice is its indirect beneficiary: P060's clean rotation restatement
("round 11 closer = unrelated") made deriving round 12's opener (fleet
backlogs) a one-line confirmation against ORDER 004 rule 3, and its
constraints-honored section again served as the slot checklist (fifth
consecutive card to reuse the shape — it is now effectively the template).
Its seed-sweep note carried the exact boundary-aware regex plus the three
data-not-seed specimens verbatim, which this session consumed directly; the
committed-sweep-script suggestion it inherited from P059 still stands
unbuilt — sixth card, same re-derivation from prose. One genuine nit: P060's
hermetic head needed no external read, so its card's "no external repo read
needed" line reads as slot doctrine, but it is UNRELATED-slot doctrine only —
the fleet-backlogs slot (this card) is defined by the firsthand harvest read;
a future drafter skimming P060's card for the checklist could miss that the
constraint flips per slot. Worth one clause in whichever card next restates
the rotation.
