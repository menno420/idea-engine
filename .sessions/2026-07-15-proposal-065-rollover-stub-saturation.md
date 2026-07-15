# Session — PROPOSAL 065: outbox rollover stub saturation — the 200KB roll that is secretly a countdown, and why the obvious fix only buys 2.9× (fleet-backlogs rotation, round 13 opener)

> **Status:** `complete`
> **Model/time:** fable · 2026-07-15T04:52:43Z (Ideas Lab worker slice — draft the
> round-13 FLEET-BACKLOGS rotation slot proposal under standing owner
> ORDER 003/004; round 12 closed fully served by P064 (#427). Card born
> in-progress as the designed gate hold; flipped complete in this PR's
> final commit at 2026-07-15T05:04:43Z. PR #428)

- **📊 Model:** fable-class · high · idea/planning

## Scope

Draft a genuinely new sim-shaped idea for the FLEET-BACKLOGS rotation slot,
round 13 OPENER, under standing owner ORDER 003 (continuous pipeline) and
ORDER 004 rule 3 ("Rotate lanes deliberately: fleet backlogs → venture's
book/product space → game mechanics → COMPLETELY UNRELATED domains (I want
those too)"). Round 12 closed fully served — P061 fleet (#408), P062
venture (#410), P063 game mechanics (#419), P064 unrelated closer (#427) —
so round 13 opens at fleet backlogs; the slot's own spacing-4 history
(P019, P021, P025, P029, P033, P037, P041, P045, P049, P053, P057, P061 →
P065) confirms. The walkthrough §E baton line "round 13 opens at the
fleet-backlogs rotation slot" is NOW correct arithmetic: P064 (#427)
flagged and served the miscounted round-12 unrelated closer, and this
slice consumes the corrected baton.

Slot repo: the slot's SECOND tap of **fleet-manager** (first: P037 → V048,
the review-queue row-trigger threshold) — DISCLOSED per the P053/P057/P061
repeat-tap precedent, not hidden: P037 priced a detection/classification
trigger on row counts; this head prices a document and constant family it
never touched — fm's **outbox rollover convention**
(`docs/conventions/outbox-rollover.md`), quoted verbatim in THIS repo's own
`control/outbox.md` ROLLOVER 001 block ("200KB threshold ·
terminal-blocks-only · dated archive files · mandatory pointer stubs ·
content-stable numbering") and executed here once already (the 2026-07-14
roll, ORDER 010). Every model constant is measured FIRSTHAND from the live
bus file in this tree at HEAD 256ea5c — 57 stubs (mean 529.9 B, min 517,
max 543), full blocks P058–P064 (mean 16,212 B), ROLLOVER receipt 1,002 B,
header 456 B, live file 154,629 B — then pinned as clean invented-pinned
constants in the idea file; zero external reads this session and zero
repo/network reads at verdict time (the hermetic precedent).

The head: **compaction with mandatory per-item tombstones is a counter,
not a thermostat** — each roll replaces evicted blocks with pointer stubs
that never leave, so the post-roll floor rises monotonically, roll spacing
decays to thrash, and the live file has a computable saturation wall N*
(the roll that can no longer bring the file under the threshold). At the
measured constants the wall is N* = 233 proposals — and the obvious fix
(one range stub per roll) only multiplies capacity 2.88× because the roll
RECEIPTS (each roll's own ROLLOVER block) are a second tombstone family
worth 24.8% of the wall. Bounded-forever requires compacting the receipt
chain too (floor pins at 34,030 B, exact).

Deliverables this slice: this card (born-red first commit), the claim
file, `ideas/fleet/outbox-rollover-stub-saturation-2026-07-15.md` + the
`ideas/fleet/README.md` index row, the `control/outbox.md` PROPOSAL 065
append, housekeeping (two terminal claim prunes — P064 drafter, PR #427
merged 2026-07-15T04:36:32Z; eap-extension-ack, PR #426 merged
04:06:27Z — both verified merged at live GitHub this session), and the
`control/status.md` heartbeat overwrite (coordinator grammar). Seeds
20261567–570 strictly above the tree high-water 20261566 (P064's
registration; fleet sim-lab high-water 20261562 re-swept READ-ONLY at
origin/main aa8627e this session).

## Constraints honored

- control/inbox.md untouched (manager-written); control/status.md
  overwritten ONLY as the ordered heartbeat housekeeping in this slice's
  scope (coordinator grammar preserved, plain `kit:` line kept).
- control/outbox-archive-2026-07-14.md untouched (rolled archive,
  terminal). Outbox append-only (appended via shell, never loaded into an
  editor); no renumbering; all timestamps from real `date -u`.
- Claim prunes are TERMINAL-only: both deleted claims' PRs verified merged
  at live GitHub (mcp pull_request_read: #427 merged 2026-07-15T04:36:32Z,
  #426 merged 04:06:27Z) before deletion.
- sim-lab READ-ONLY: dedup ledger + seed sweep on a fresh shallow clone at
  origin/main aa8627e (fetched this session); nothing there touched.
- No external repo read needed: the priced convention's constants are
  quoted in this tree's own ROLLOVER 001 block and measured from the live
  bus file at HEAD 256ea5c; fm's convention doc is named as the consumer,
  never read (the lane repo boundary respected — this repo edits no other
  repo).
- Seed sweep boundary-aware at drafting HEAD 256ea5c: this tree maxes at
  genuine 20261566 (P064's allocation); sim-lab @ aa8627e maxes at genuine
  20261562 (V074's 20261559–62) — the larger standalone numerals
  (20261833, 202670087, and sim-lab results.json digit runs like
  2026964142) are the documented Fraction-numerator / decimal-fraction
  data-not-seed specimens; the P046–P064 sweep-recipe trap re-confirmed.
- The `📊 Model:` line above uses the kit's taught three-field payload
  (the P064 fix, carried forward).

## 💡 Session idea

**Price the policy's own exhaust: any compaction whose per-operation receipts
live on the compacted surface has a second wall hiding behind the first — and
it is invisible until you decompose the floor by mass family.** Drafting's
genuine surprise was not the wall (per-item tombstones obviously accumulate);
it was that the OBVIOUS fix — replace 57 per-block stubs with one range stub
per roll — bought only 2.88× when intuition said ~10×. The wall-composition
decomposition explained it: at saturation the roll RECEIPTS (each roll's own
permanent ROLLOVER block) are 24.8% of the wall mass, so once stubs go O(1)
the receipts become the binding tombstone family, and boundedness requires
compacting the receipt chain too (newest receipt supersedes the chain — floor
constant forever, exact). The durable pattern generalizes past files: every
cleanup mechanism EMITS as it cleans (audit rows, done-markers, "known upkeep"
lines, ack blocks, session stubs), and any analysis that prices only the
primary waste stream will certify a fix that moves the wall instead of
removing it. The test is one line: decompose the post-cleanup floor by mass
family, and check whether the cleanup's own emissions appear in it. Kin to
P064's "write down the generator, not the generated value" but a different
axis: that one was about batons caching stale conclusions; this one is about
mechanisms whose bookkeeping is self-defeating at scale — the ledger OF the
cleanup accumulating on the surface the cleanup exists to bound.

## ⟲ Previous-session review

Previous session (the P064 drafter, PR #427 @ `256ea5c`): exemplary in the two
ways this slice directly consumed — (a) the born-red card discipline and the
three-field 📊 payload fix landed cleanly (this card inherits both, zero
friction), and (b) its decide-and-flag on the walkthrough §E baton miscount
was exactly right: it served the unserved round-12 closer, named "round 13
opens at fleet backlogs with P065" as the corrected baton, and this slice
consumed that correction without re-litigating — its 💡 (carry the RULE plus
raw state, never a cached conclusion) was applied verbatim in this slice's
heartbeat baton ("rule 3 + raw state: round 13 has 1 of 4 slots served —
venture next"). One nit, and it is an instance of that same 💡: P064's seed
sweep recorded the sim-lab pin's "max genuine 20261562" plus two enumerated
data-not-seed specimens (20261833, 202670087) — a cached specimen LIST. This
session's sweep at the SAME pin met fresh large numerals the list does not
name (results.json digit runs like 2026964142) and had to re-derive their
status from the sweep-recipe trap note; stating the discrimination RULE
("standalone 2026-prefixed numerals inside results-quoting text are data, not
seeds") rather than enumerating specimens would have made the next sweep
self-verifying — the generator, not the generated values.
