# Ideas Lab seat — SEAT DORMANT revival record (owner order 2026-07-14)

> **Status:** `reference`
>
> The EAP FINAL SHUTDOWN handoff (ORDER 014, PR #424). The Ideas Lab seat
> (idea-engine + sim-lab) went dormant by owner order on 2026-07-14. This is
> the revival record: what was running, what was stopped, and the exact path
> back. Pointers over restatements — doctrine lives in the fleet-manager
> central copies, not here. (Distinct from the untracked root `HANDOFF.md`
> the kit regenerates per session — this file is the tracked, permanent
> dormancy record.)

## 1. Routine record — written down FIRST, per the shutdown order

Recorded verbatim at shutdown (2026-07-14T23:42:25Z), per
`docs/ROUTINES.md` ("record verbatim — every create/delete call"):

- **Failsafe cron**: name "Ideas Lab failsafe wake", id
  `trig_01YGs7oTwL3XoXj59hDHbPyi`, cron `30 1-23/2 * * *` (every 2h),
  self-bound to coordinator session_0146BSTEg76Sx9TSEZndRMkX. Still armed
  at this write. **Deletion is the coordinator's step AFTER PR #424
  merges**, with absence verified to exhaustion (a first-page miss is not
  absence — walk the registry, per `docs/ROUTINES.md`).
- **Pacemaker**: the ~15-min `send_later` one-shot chain closed ~09:47Z
  2026-07-14 at EAP end. Nothing outstanding.
- **Business crons**: NONE — the failsafe was this seat's only scheduled
  trigger.

The live registry is the proof; this record is only the claim
(`docs/ROUTINES.md`). At revival, verify against the registry before
assuming anything here still holds.

## 2. Revival path

1. **Owner re-pastes the coordinator brief** — the central copy lives at
   fleet-manager `docs/prompts/v3` (ideas-lab brief). That brief, not this
   doc, is the source of truth for seat doctrine, scope, and rails.
2. **New coordinator re-arms the wake chain per the brief's BOOT §3** —
   failsafe cron (self-bound, verify the first scheduled delivery actually
   lands) + the turn-scoped pacemaker. Binding doctrine: `docs/ROUTINES.md`
   (this repo's copy) and the fleet-manager central copies it defers to.
3. **Read-first order for the new coordinator**: `control/status.md` (the
   final SEAT DORMANT heartbeat — routine facts single-homed there) →
   `docs/eap-closeout-walkthrough-2026-07-14.md` §E (batons, open threads,
   the proposed-next-stamp recipe) → this doc's parked list → then the
   normal boot set per `.claude/CLAUDE.md`.

## 3. State at shutdown (facts, dated 2026-07-14)

- Pipeline FINAL: 63 proposals / 76 verdicts; newest P063 → V074
  REJECT-REORDER (sim-lab#140 @ 9aaf72b). Pipeline DRY — no unverdicted
  proposal.
- claims/ EMPTY; 0 open PRs besides #424 at the shutdown sweep
  (2026-07-14T21:15Z).
- Orders 001–014 closed (014 = the shutdown itself; its post-merge
  coordinator step is the failsafe deletion above).
- Fleet seed high-water: 20261562 (V074, seeds 20261559–62) — allocate
  strictly above at revival.
- Kit v1.17.0 (#423 @ d086bfa); `python3 bootstrap.py check --strict` green.

## 4. Parked list (carried over, none new at shutdown)

All owner-facing items live in `docs/eap-closeout-walkthrough-2026-07-14.md`
§C — the single checklist. Non-owner watches:

- ASK 005 (roster-generator registry-only-row contract) — awaits the
  fleet-manager, fm-side.
- Kit ASKs 001–003 — with the substrate-kit lane; evidence standard: the
  next kit-upgrade PR retains the `claude/*` enabler allowlist line.
- makerbench build — waits on the owner's tweak reply (ORDER 004 rule 4).
- Standing ORDER 003 (continuous pipeline) — suspended by dormancy; whether
  its ≥1-in-flight duty resumes is the revived seat's first decision
  (round 13 would open at the fleet-backlogs rotation slot).

## 5. Duplication ledger — where each fact is homed

- Routine facts: `control/status.md` routine-disposition block (single
  home) — §1 above is the shutdown-time snapshot of it.
- Owner actions: walkthrough §C (single checklist; the heartbeat only
  points at it).
- Batons / open threads / next-stamp recipe: walkthrough §E.
- EAP history and measurements: `docs/audits/eap-project-audit-2026-07-14.md`.
- Seat doctrine, scope, rails: fleet-manager central copies (the
  `docs/prompts/v3` ideas-lab brief) — never restated here.
- The shutdown directive itself: `control/inbox.md` ORDER 014.
