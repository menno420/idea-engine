# games-web ↔ superbot-mineverse scope seam — two lanes now render the same miner state

> **State:** captured
> **Class:** product · **Target:** `menno420/product-forge`
> **Grounding:** https://raw.githubusercontent.com/menno420/product-forge/0a6efe96ef8021679b9f8a6ee63a617cd9d61ffc/control/inbox.md@0a6efe9 · fetched 2026-07-11T03:31:46Z
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-mineverse/01a8b8572507f5dd5b65109161091b90272cc57b/control/status.md@01a8b85 · fetched 2026-07-11T03:34:14Z
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/93d3a4d/docs/roster.md@93d3a4d · fetched 2026-07-11T03:31:30Z
> **Sequence:** before the manager routes games-web phase-2 / the batched superbot read-only-API providing ORDER

## Problem

product-forge ORDER 001 (2026-07-10T18:41Z) routed games-web to the forge under the
*"no owning lane exists"* test: a comic browser-RPG rendering of the MINING character
sheet, mock-first, real data explicitly deferred. Since then the premise moved:
**superbot-mineverse was born** (roster gen #4: "LANE BORN THIS WINDOW",
mining-browsergame) and at live HEAD `01a8b85` it is far past its roster row — stages
0/a/b/c done, 163 tests, and it already renders miner state in a browser: 9-slot gear
panel with wear, vault with tier pips, depth/biome ladder, tabbed leaderboards, all
from its own versioned `mining_snapshot.v1` contract (16 per-miner v1 fields projected
from `mining_player_state` + `game_xp_service`). games-web phase-1 renders the same
underlying miner (gear paper-doll — 8 fixed slots — stats, skills, structures) from
its own `games-web.character-sheet` v1.0.1 contract. An owning lane for
browser-rendered mining state now exists, and games-web phase-2 as proposed would
build a **second live-data path to the same producer**.

## Idea

Capture the seam decision so the manager rules it *before* phase-2 investment, instead
of discovering the collision after both contracts freeze. The probe should verify the
overlap precisely at both lane HEADs and recommend among: **(A)** games-web
specializes to the owner-named comic-RPG *presentation layer*, consuming the
mineverse-side projection (`mining_snapshot.v1` / its FLAG-1 read relay) instead of a
bespoke character-sheet endpoint; **(B)** deliberate two-product continuation with an
explicit contract reconciliation (see the sibling convergence capture,
`read-projection-fanin-fourth-consumer-2026-07-11.md`); **(C)** fold — games-web's
comic-RPG skin migrates into mineverse's frontend and the forge subtree goes
historical per its own incubator mechanic. Not prejudged here: (A) looks cheapest
from this read, but mineverse's mandate is the *live economy* while ORDER 001's is
*superbot's existing games* plural — the probe must check whether games-web's roadmap
beyond mining makes the overlap partial, not total.

**Why now:** mineverse is deepening (slice 2 in flight at fetch time) and the batched
read-only-API providing ORDER is not yet routed — this is the last cheap moment to
reconcile: ORDER 001 kept phase 1 mock-first precisely to stay "cheap to redirect".
