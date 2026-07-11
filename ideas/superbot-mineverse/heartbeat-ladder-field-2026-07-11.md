# A machine-parseable ladder line for the roster generator — fast newborn lanes outrun prose rows

> **State:** captured
> **Class:** process · **Target:** `menno420/fleet-manager`
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/dd8dc10e0a108b4f77a7c7bcd155e4b351aa2881/docs/roster.md@dd8dc10 · fetched 2026-07-11T04:00:21Z
> *(pin annotation: roster still generation #4, generated-at 2026-07-11T01:58Z, at fleet-manager HEAD `dd8dc10` — the same generation the earlier sibling batch pinned at `93d3a4d`)*
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-mineverse/510fa3e05cdac1244d70e65b71d048b7fdf38dd0/control/status.md@510fa3e · fetched 2026-07-11T04:00:19Z
> **Sequence:** before the roster's row format hardens across more generations

## Problem

Grounded by THIS lane's drift, measured at capture time. The roster gen-#4 row for
superbot-mineverse (@ `dd8dc10`, verbatim): "**LANE BORN THIS WINDOW**
(\"mining-browsergame\"): ORDER 000 walking skeleton merged to main; stage (a) READ
CONTRACT v1 + backlog slice in flight; `check: red` is the pre-existing born-red
unrendered-interview state (engaged: no, flips on slot render)", pinned at lane
`1120a3b` 01:57:13Z. The lane's own heartbeat @ `510fa3e` (updated 03:58:00Z) reads
"LADDER: 0 ✓ · (a) ✓ · (b) ✓ · (c) ✓ web-side · (d) PREPARED ✓" with check green /
engaged yes / 187 tests — FOUR ladder rungs, a check-state flip, and an engagement
flip inside ONE ~2h generation window. The roster already knows fast movers exist
(this exact row carries a "mid-sweep mover, re-pinned" annotation), but stage
progress lives in prose a generator can only carry forward verbatim, so the row is
stale-by-construction the moment a newborn lane moves — and newborn lanes move
fastest precisely while their rows matter most.

## Idea

A machine-parseable `ladder:` line in the kit heartbeat grammar — e.g.
`ladder: 0=done a=done b=done c=done d=prepared` — written by lanes that operate a
staged ladder, so the roster generator can (1) render stage state mechanically
instead of quoting prose, (2) diff it against the previous generation and surface
stage-level drift ("moved N rungs since gen #k"), and (3) re-pin fast movers
automatically when the drift exceeds a threshold, instead of relying on a mid-sweep
human-shaped catch. Seam honesty: the heartbeat format block is kit-owned grammar
(EAP §6.8 — undeclared top-level keys are drift and fold into `phase` in consumers'
parsers, this repo's control/README records the round-4 decision), so the field
becomes real as a KIT grammar addition; fleet-manager's generator is the consumer
that motivates and first exploits it. Until the kit declares it, lanes can carry the
same string inside `phase:` where it is at least grep-able.

**Why now:** the generated roster just became the fleet's canonical lane registry
(this repo's README § Sections re-pointed to it 2026-07-11), every idea-engine
section derivation and manager routing decision now reads these rows, and the fleet
is birthing lanes weekly — the row format is young enough that a grammar field is an
addition, not a migration.
