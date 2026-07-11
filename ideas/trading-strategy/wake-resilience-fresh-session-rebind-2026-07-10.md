# Wake resilience — unbind the 4-hourly trigger from a single mortal session

> **State:** parked(build-direct — owner-click-gated: the risk class is LIVE but mutated — the named trigger `trig_01Mvn5xRmqGmZJNRHgjqyLpN` was already deleted by the lane's own Q-0265 rebind-then-delete cutover 2026-07-10T21:03:05Z, yet its successor failsafe `trig_01YBaVeKAW2fSD83S9F37s2d` is STILL session-bound; the fresh-session fix remains one lane-side rebind gated solely on the lane's own ⚑ (b) env setup-script paste, still open @ `d0d789e`)
> **Class:** process · **Target:** `menno420/trading-strategy`
> **Grounding:** https://github.com/menno420/trading-strategy@d0d789ef7319fde6b9b416e72240a01fe3b79097 · fetched 2026-07-11T01:49:58Z (manifest row: behind)
> *(pin annotation: probe-time re-check pin — capture pin was `e713abb` (2026-07-10); the manifest row @ superbot HEAD `a762384` (ls-remote 01:49:58Z) still names `trig_01Mvn5xRmqGmZJNRHgjqyLpN` "session-bound — F-1 watch item", but the lane heartbeat @ `d0d789e` records that trigger DELETED 2026-07-10T21:03:05Z — the F-1 watch item now points at a trigger that no longer exists while the risk lives in its successor; freshest wins: lane heartbeat + HEAD tree-scan)*
> **Sequence:** after the trading-strategy ⚑ (b) owner click (env setup-script paste) — the capture's own ordering constraint, re-verified STILL OPEN in the lane heartbeat @ `d0d789e`

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

## Probe report (v0, 2026-07-11)

*Probed 2026-07-11T01:49Z, single-pass per the README panel default (sim-lab VERDICT 002
— no ambiguity signal; the rebind itself is reversible and gated, no irreversible
surface). Live-state recon FIRST per the lane-self-served prior (three datapoints, two
under ~20 min) and the PR kit-upgrade-pin card's explicit handoff ("re-check the gate
AND the new kit-planted `scripts/env-setup.sh` at probe time"). Lane HEAD `d0d789e`
(ls-remote 2026-07-11T01:49:58Z — unchanged since its v1.8.0 upgrade 01:15:34Z);
superbot HEAD `a762384`; lane tree read via a read-only blobless clone at that pin.*

**Live state, with citations — the verify-first read found the premise MUTATED, not
moot (the section's first head where the live check did NOT flip the verdict to
overtaken):**

- **The named trigger is GONE — deleted by the lane itself.** Lane
  `control/status.md@d0d789e` routine-state line: "CUTOVER COMPLETE — created +
  verified trigger `trig_01YBaVeKAW2fSD83S9F37s2d` 'trading-strategy failsafe wake'
  cron `0 */2 * * *` bound to coordinator session `session_01NwvvbgUVSdQvY8eYwtuEoo`
  (created_via meta_mcp, 2026-07-10T21:03:05Z), THEN deleted predecessor
  `trig_01Mvn5xRmqGmZJNRHgjqyLpN`". Rebind-then-delete — the exact mechanism this
  capture prescribed — was executed by the lane the same day, and the cadence moved
  4-hourly → 2-hourly under the Q-0265 continuous-mode cutover (failsafe deadman +
  send_later chain, the fleet-standard pattern).
- **But the successor is STILL session-bound.** "bound to coordinator session
  `session_01NwvvbgUVSdQvY8eYwtuEoo`" — a persistent-session bind, not
  fresh-session-per-fire. The F-1 failure class survives intact: the day that
  coordinator session archives or dies, the failsafe fires into a dead session and the
  lane goes dark with zero error surface. The capture's fix remains UN-executed.
- **The ⚑ (b) owner click is STILL OPEN.** Lane heartbeat @ `d0d789e`, six-field form:
  "(b) ENV SETUP SCRIPT / fresh-environment sessions die silently at provision without
  it / paste the contents of `environments/setup-universal.sh` into the environment's
  setup-script field and save / Claude environment config for this project / not
  blocking (current pinned env works) / … treat any child with no heartbeat within
  10 min as dead → respawn."
- **Kit v1.8.0 changed the gate's SHAPE, not its existence.** The lane's v1.8.0 upgrade
  (`d0d789e`, 2026-07-11T01:15:34Z) planted `scripts/env-setup.sh` — the kit's
  setup-script contract (EAP §6.5): "Every fleet environment's setup shim prefers THIS
  file when it exists, so repo-specific setup lives here." The lane's
  `environments/setup-universal.sh` (synced 2026-07-09 from the fleet-manager canonical
  template, blob `6b4459b`) already carries that per-repo escape hatch. Net: the owner
  click is still ONE paste of the shim into the env panel, but it is now durable — all
  future repo-specific setup rides the committed hook, no re-paste. The gate did NOT
  dissolve; it narrowed to a single durable click.
- **Divergence (freshest-wins):** the manifest row @ superbot HEAD `a762384` still
  reads "`trig_01Mvn5xRmqGmZJNRHgjqyLpN` … session-bound — F-1 watch item" — the watch
  item names a trigger deleted ~5 h before this probe's fetch (staleness datapoint
  SIXTEEN, same row as datapoints 5–6/13/15); a manifest-driven fixer would rebind a
  nonexistent trigger while missing the live successor.

**1. What is this really?**
A liveness-risk capture whose named artifact is gone but whose risk class survived the
replacement: the lane's Q-0265 cutover exercised rebind-then-delete (proving the
mechanism is lane muscle) yet re-bound to another mortal session. What remains is
exactly the capture's core — unbind the lane's only clock from a single session —
updated to target `trig_01YBaVeKAW2fSD83S9F37s2d`, still walled behind the same ⚑ (b)
paste.

**2. What is the possibility space?**
(i) Do nothing: the lane's `next-update-by: 2026-07-17` weekly cadence now bounds the
dark window at ~a week of manager staleness math instead of forever — mitigated, not
fixed. (ii) The capture's fix, retargeted: post-click, one fresh-session-per-fire
rebind of the failsafe. (iii) The fleet-generic layer: EVERY Q-0265 seat runs a
coordinator-session-bound failsafe (this repo's own `trig_0178q9Je2xRFJgthwamrg9Br`
included) — the same rebind applies fleet-wide once each lane's env setup is pasted;
that residue is manager/kit surface, not this lane's. (iv) A parallel second
fresh-session deadman alongside the session-bound one is NOT a click-free hedge — any
fresh session dies at provision until the paste lands; the wall is the same wall.

**3. What is the most advanced capability reachable by the simplest implementation?**
After one owner paste: ONE `create_trigger` with fresh-session-per-fire semantics +
one verified live fire (heartbeat within 10 min — the lane's own dead-child rule is
the ready-made health check) + delete the predecessor = a lane clock that survives any
session archive, forever. Zero code; the rebind-then-delete choreography is already
proven in this exact lane (21:03:05Z) and at kit-lab before it (manifest F-1
precedent).

**4. What breaks it?**
(a) Executing BEFORE the click: fresh sessions "die silently at provision" (the lane's
own ⚑ (b) wording; two sessions killed per the `setup-universal.sh` header) — a
fresh-session failsafe armed pre-paste looks fixed while firing corpses, strictly
worse than the session-bound status quo. (b) Manifest-driven execution: the F-1 watch
item names a deleted trigger (datapoint 16) — only the lane heartbeat identifies the
live target. (c) Prompt shape: a fresh-session fire starts from ZERO context — the
rebind must rewrite the failsafe prompt as a standalone cold-start ritual (sync HEAD →
read inbox → resume loop), not the current chain-context wording.

**5. What does it unlock?**
Closes the lane's F-1 watch item for real (a parked-adjacent lane whose clock cannot
die with a session); retires the ⚑ (d) fear-of-archiving interaction (dead sessions
become archivable without liveness risk); template for the same rebind on every other
Q-0265 seat once their pastes land.

**6. What does it depend on?**
Solely the trading-strategy ⚑ (b) owner paste — a true owner-only ask (the environment
setup-script panel is owner-side surface; the lane itself verified the wall in dead
sessions, and its heartbeat already carries the six-field OWNER-ACTION entry — no
duplicate ask needed from this repo). Plus the cold-start prompt rewrite (Q4c),
in-slice. Nothing else: kit v1.8.0's `scripts/env-setup.sh` is already committed at
lane HEAD.

**7. Which lane should build it?**
`menno420/trading-strategy` — its own trigger, its own meta_mcp session tooling
(proven at the 21:03Z cutover), its own ⚑ (b), and its ORDER 006 convention for
recording the mechanism verbatim in `control/status.md`. Not sim-lab: a rebind proves
itself with one live fire against the 10-min heartbeat rule — there is no evidence
question a simulator could settle better than the live fire does.

**8. What is the smallest shippable slice?**
One lane session, post-click, zero code: create the fresh-session-per-fire trigger
(same `0 */2 * * *` cadence, cold-start ritual prompt), verify ONE live fire produces
a heartbeat within 10 min, delete `trig_01YBaVeKAW2fSD83S9F37s2d`, record the
mechanism verbatim in the routine-state line per ORDER 006 precedent —
rebind-then-delete, never a gap, exactly as this capture wrote it.

**Recommendation: park** — build-direct, owner-click-gated: the risk is live (the
successor failsafe is still bound to one mortal session) and the fix is one lane-side
rebind the lane has already proven it can execute, gated solely on its own ⚑ (b) env
setup-script paste (still open @ `d0d789e`); no sim-lab question — one live fire
against the lane's 10-min heartbeat rule is the whole proof.
