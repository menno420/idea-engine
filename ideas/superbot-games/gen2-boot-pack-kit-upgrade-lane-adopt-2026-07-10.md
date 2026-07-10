# Gen-2 boot pack — kit v1.7.0 upgrade + `adopt --lane` heartbeat declaration

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot-games`

## Problem

superbot-games runs the fleet's oldest live kit pin (**v1.2.0**) and carries a flagged
**two-writer heartbeat ⚑**: its cohabitation contract already splits the heartbeat by
hand (`control/status-mining.md` / `control/status-exploration.md` are each lane's sole
property — `docs/lanes.md` ownership table @ `adb5f9b`), but a v1.2.0 kit predates
`heartbeat_files`, so the gate cannot see or enforce the per-lane files the repo actually
uses. Gen-2 relaunch is imminent and currently **clockless and boot-gated** (manifest:
ORDER 001 P0 pending, ORDER 002 self-arm wake landed-unexecuted) — booting two Projects
onto an undeclared heartbeat scheme re-runs the exact collision class the split exists to
prevent.

## Idea

One bounded PR at the lane's next boot: `bootstrap upgrade` to kit v1.7.0, then
`bootstrap adopt --lane mining` + `adopt --lane exploration` — v1.7.0's `adopt --lane` is
skip-if-exists (never re-plants the sibling's files, the double-adoption fix) and
declares both files in `substrate.config.json` → `heartbeat_files`, so the status checker
gates each lane independently and a missing/heartbeat-less lane goes strict-RED instead
of invisible. Honors the lane's "kit adoption ONCE / second Project verifies" rule.

## Grounding

- Fleet manifest games-plugins row (`https://raw.githubusercontent.com/menno420/superbot/main/docs/eap/fleet-manifest.md`,
  fetched 2026-07-10): "kit v1.2.0 (v1.7.0 `adopt --lane` is the fix for its two-writer ⚑)";
  ORDER 001 P0 boot-gating; ORDER 002 unexecuted.
- `menno420/superbot-games` @ `adb5f9b` — `docs/lanes.md` (per-lane status file ownership;
  "Kit adoption — ONCE") and `control` protocol mirrored in this repo's
  `control/README.md` § Multi-Project repos (`heartbeat_files`, `adopt --lane` semantics).

**Why now:** the fix ships in the kit today, and the lane's first gen-2 boot session is
the one moment it can land before the two-writer flag becomes a live incident.
