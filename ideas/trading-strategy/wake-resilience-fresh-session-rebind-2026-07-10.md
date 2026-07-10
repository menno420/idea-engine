# Wake resilience — unbind the 4-hourly trigger from a single mortal session

> **State:** captured
> **Class:** process · **Target:** `menno420/trading-strategy`

## Problem

The lane is PARKED GREEN, so its standing wake **is** its liveness: with no work in
flight, the 4-hourly trigger (`trig_01Mvn5xRmqGmZJNRHgjqyLpN`) is the only thing
that ever reads the inbox. The manifest flags that trigger as "**session-bound — F-1
watch item**": it fires into one specific persistent session, so the day that
session archives or dies, the lane goes dark with zero error surface — exactly the
failure class kit-lab already fixed on its own seat (F-1 rebind-then-delete,
executed per the manifest's kit-lab row). Worse, the obvious fix
(fresh-session-per-fire) is currently walled: the lane's own status ⚑ (b) records
that fresh environments die silently at provision until the owner pastes
`environments/setup-universal.sh` into the environment config.

## Idea

A one-session rebind, sequenced behind the ⚑ (b) owner click: once the setup script
is pasted, create a new trigger with fresh-session-per-fire semantics (same cadence,
same ritual prompt), verify one live fire survives provision (the status ⚑ (b)
fallback already defines the health check: heartbeat within 10 min or dead), then
delete the session-bound trigger — rebind-then-delete, never a gap. Record the
mechanism verbatim in `control/status.md` per the lane's ORDER 006 precedent. Until
the click lands, the capture doubles as the written statement of the risk: one
archived session = dark lane.

## Grounding

- Manifest trading-strategy row: "4-hourly standing wake — WORKS, self-armed
  (`trig_01Mvn5xRmqGmZJNRHgjqyLpN` … session-bound — F-1 watch item)"; kit-lab row
  for the F-1 rebind-then-delete precedent
  ([superbot @ `6f283b9`](https://raw.githubusercontent.com/menno420/superbot/6f283b91160546af2864a0fd30b6e2d81b148a8f/docs/eap/fleet-manifest.md), fetched 2026-07-10).
- Lane reality @ [`e713abb`](https://github.com/menno420/trading-strategy/tree/e713abb125766db2b1562980369a11290b8772b9):
  `control/status.md` ⚑ (b) (env setup-script wall, verbatim, with the 10-min
  dead-child rule) and routine-state line; `control/inbox.md` ORDER 006 (the
  mechanism-documentation convention).

**Why now:** a parked lane with a mortal clock is one session-archive away from
silently leaving the fleet — and the P5 session about to be dispatched is exactly
the kind of event that churns sessions.
