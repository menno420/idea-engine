# Shared encounter engine — write the consumer contract before mining builds it

> **State:** captured
> **Class:** product · **Target:** `menno420/superbot-games`

## Problem

`docs/lanes.md` @ `adb5f9b` rules: "Mining implements the shared encounter engine first;
exploration consumes it." But the engine's first real consumers are already owner-ruled
and live in *another repo's* backlog: **wild encounters** (activity-debounced channel
spawns — owner decision **Q-0186: build FIRST**) and **grid encounters** (depth-gated
sparse events — owner decision **Q-0198: loot/flavour first, combat fast-follow**), both
harvested into `ideas/superbot/` @ superbot `fd638e3`. Nothing in superbot-games names
them. A mining Project building "the shared encounter engine" from its own founding plan
alone will build a grid-shaped engine, and the activity-spawn consumer (plus
exploration's quest/encounter engine) will each need a retrofit — in a claim-first shared
path where interface changes cost a both-lanes announcement every time.

## Idea

One capture-level contract doc for `games/shared/` (this is that capture): the engine
takes a **spawn source** abstraction (activity counter · grid step · quest beat), a
**deterministic resolution seam** (loot/flavour first per Q-0198; combat delegated to the
creature engine as fast-follow), and **reward routing through the existing audited
seams** (Q-0186's own condition) — with wild encounters, grid encounters, and
exploration's quest engine named as the three launch consumers the public surface must
satisfy before it freezes.

## Grounding

- `https://raw.githubusercontent.com/menno420/superbot-games/main/docs/lanes.md` @
  `adb5f9b` (mining-implements/exploration-consumes rule; claim-first + interface-change
  announcement cost).
- `ideas/superbot/wild-encounters-activity-spawning-2026-07-10.md` and
  `ideas/superbot/mining-grid-encounters-2026-07-10.md` — link indexes pinned @ superbot
  `fd638e3` carrying the Q-0186 (BUILD FIRST) and Q-0198 (loot-first) owner rulings.
- `control/status.md` prior heartbeat: wild-encounters flagged among the harvest's
  ripest probe candidates.

**Why now:** the engine is the first shared-path code the cohabitation experiment will
stress; shaping its surface costs one doc today and a two-lane renegotiation later.
