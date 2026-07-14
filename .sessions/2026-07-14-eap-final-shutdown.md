# 2026-07-14 — EAP final shutdown: ORDER 014, dormancy handoff, final heartbeat

> **Status:** `in-progress`
> **Model/time:** Claude Fable · 2026-07-14T21:18:33Z (dispatched worker slice —
> land the owner's EAP FINAL SHUTDOWN directive: ORDER 014 appended to the
> bus, `docs/HANDOFF.md` revival record, `docs/current-state.md` dormancy
> section, final SEAT DORMANT `control/status.md` stamp. Card born
> in-progress as the designed gate hold; flips complete in this PR's final
> commit)

- **📊 Model:** Claude Fable · high · docs-only — shutdown landing (inbox
  ORDER append + handoff/current-state docs + final heartbeat overwrite; no
  scripts/, no ideas/ content, nothing in sim-lab)

## Scope

Land the owner's EAP FINAL SHUTDOWN directive (owner live turn in
coordinator chat, 2026-07-14, landed by coordinator scribe) as one PR:

1. **ORDER 014** appended verbatim to `control/inbox.md` (append-only; the
   shutdown directive itself — finish small, stop all routines, double-check
   the handoff, source-of-truth pointers, land it).
2. **`docs/HANDOFF.md`** — the SEAT DORMANT revival record: read-first
   order, the routine record (failsafe cron id/schedule/binding; the
   pacemaker chain already closed at EAP end; no business crons), revival
   re-arm instructions, the parked list, and the duplication ledger.
3. **`docs/current-state.md`** — dormancy section pointing at ORDER 014 and
   `docs/HANDOFF.md`.
4. **`control/status.md`** — final heartbeat overwrite: SEAT DORMANT
   (owner order 2026-07-14), neutral facts only.

FINISH SMALL sweep (directive step 1) ran first: newest ORDER at branch
time was 013 (all 001–013 done/acked per the 12:51:46Z heartbeat), newest
outbox entry CLOSE-OUT 001 posted, pipeline DRY (P063 → V074 same-day),
claims/ empty, 0 open PRs on the repo at 2026-07-14T21:15Z (GitHub MCP
`list_pull_requests state=open` → `[]`). Only landings since the 12:51Z
stamp are the kit upgrades #422 @ `a754d7e` and #423 @ `d086bfa`, both
merged. **Backlog dry at shutdown; nothing in flight** — the honest null.

## Constraints honored

- `control/inbox.md` append-only — ORDER 014 appended via shell after the
  existing ORDER 013 block; no earlier order edited.
- `control/outbox.md`, `control/outbox-archive-2026-07-14.md`, `claims/`
  untouched.
- `control/status.md` wholesale overwrite in its existing format (the
  heartbeat contract), `kit:` line kept plain, `updated:` from real
  `date -u`, monotonic past the prior 2026-07-14T12:51:46Z stamp.
- Routine DELETION is deliberately NOT performed here: this session's
  toolset does not own the coordinator's triggers — the coordinator
  (session_0146BSTEg76Sx9TSEZndRMkX) deletes and verifies-to-exhaustion
  after this PR merges, per `docs/ROUTINES.md`. The routine record is
  written down FIRST (directive step 2) in `docs/HANDOFF.md`.
- No auto-merge arming, no self-merge — the installed enabler handles
  in-pattern `claude/*` PRs (#367 precedent).
- All timestamps from real `date -u`.
