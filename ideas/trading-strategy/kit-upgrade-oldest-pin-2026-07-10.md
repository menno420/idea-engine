# Kit upgrade — retire the fleet's oldest pin (v1.1.0 → v1.7.0)

> **State:** captured
> **Class:** process · **Target:** `menno420/trading-strategy`

## Problem

The manifest flags the lane as running "**kit v1.1.0 (oldest pin)**" while the kit
shipped v1.7.0 gen-2 CLOSED — six MINOR versions of gate and checker fixes the lane
has never received. This is not cosmetic drift: the lane's own `control/status.md`
documents live process friction that newer-kit repos don't have (auto-merge arm
fails pending-side with the "unstable status" wall on every PR, reconfirmed on
PR #36, forcing agents to poll-and-REST-merge), and the v1.7.0-era planted
`substrate-gate.yml` carries the control-fast-lane and session-card gating fixes
that were learned live across the fleet after v1.1.0 was pinned. A parked-green lane
is the cheapest possible moment to take an upgrade — no research in flight to
destabilize.

## Idea

One bounded slice on the lane: `bootstrap.py upgrade` to the current dist, re-render,
run `check --strict` plus the full pytest suite (147 green at ORDER 007), land as one
READY PR, and bump the `kit:` self-report line in `control/status.md` in the same
session (the kit-line contract requires exactly that). Sequencing note: land it
**around, not inside,** the ORDER 008 holdout session — the binding P5 protocol
session should run on a tree whose gates weren't changed the same hour.

## Grounding

- Manifest trading-strategy row: "kit v1.1.0 (oldest pin)"; kit-lab row: "gen-2
  CLOSED handoff-ready at **v1.7.0**", write-all distribution scope per Q-0261.3
  ([superbot @ `6f283b9`](https://raw.githubusercontent.com/menno420/superbot/6f283b91160546af2864a0fd30b6e2d81b148a8f/docs/eap/fleet-manifest.md), fetched 2026-07-10).
- Lane reality @ [`e713abb`](https://github.com/menno420/trading-strategy/tree/e713abb125766db2b1562980369a11290b8772b9):
  `control/status.md` health line (auto-merge "unstable status" wall on PR #36;
  147 tests as the upgrade's regression baseline) and ⚑ (c).
- Kit-line update-in-same-session rule: this repo's `control/README.md` § status
  format ("update it in the same session as every `bootstrap upgrade`").

**Why now:** the lane is parked green with one owner-gated order outstanding — the
last quiet window before post-holdout research restarts on top of whatever gates it
has.
