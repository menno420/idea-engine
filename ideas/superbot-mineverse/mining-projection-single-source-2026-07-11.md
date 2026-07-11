# One bot-side mining projection, two serializations — before two contracts freeze against one source

> **State:** captured
> **Class:** product · **Target:** `menno420/superbot`
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-mineverse/510fa3e05cdac1244d70e65b71d048b7fdf38dd0/control/status.md@510fa3e · fetched 2026-07-11T04:00:19Z
> *(pin annotation: lane HEAD via ls-remote 03:59:59Z; the roster's gen-#4 row for this lane is pinned at `1120a3b` — four ladder rungs behind this heartbeat — lane truth cited per the freshest-wins rule)*
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/dd8dc10e0a108b4f77a7c7bcd155e4b351aa2881/docs/proposals/games-program-mapping-conformed-2026-07-10.md@dd8dc10 · fetched 2026-07-11T04:01:23Z
> **Sequence:** before the manager routes the batched superbot read-only-API providing ORDER / games-web phase-2

## Problem

Two independently-contracted read projections of the SAME bot-side mining state are
now demanded, written on opposite sides of this lane's birth, neither citing the
other. Side one: mineverse ⚑ FLAG 1 (heartbeat @ `510fa3e`, carried verbatim every
overwrite) asks the bot lane to emit `mining_snapshot.v1` into the part-4d bot→web
read relay — 16 per-miner v1 fields projected from `mining_workflow` /
`mining_player_state` via `game_xp_service`, additive-only, ~60s push cadence, done =
validates against `schemas/mining_snapshot.v1.schema.json`. Side two: fleet-manager's
conformed games-program mapping (surface (a), dated 2026-07-10 — the lane was born
2026-07-11T01:46Z) places a committed-JSON game-state feed on the superbot lane for
games-web phase 2, "contract v1 (family = mining character-sheet on games-web's
committed consumer schema)". Same producer-side source, two contracts, two egress
mechanisms — and the consumer shapes are already drifting (8 fixed gear slots vs a
9-slot gear panel with wear over one dataset; see the seam and fan-in captures below,
cross-linked never duplicated). If the bot lane builds these as two independent
derivations, field semantics drift is not a risk, it is a schedule.

## Idea

ONE bot-side projection module owning the read of `mining_workflow` /
`mining_player_state` / `game_xp_service` and emitting BOTH contracts from a single
in-memory projection of the ~16 v1 fields — the relay push (FLAG 1's envelope) and
the committed-JSON feed (the mapping's surface (a)) become two serializers over one
source of truth, so the second surface is a re-serialization, never a re-derivation.
Field-name/semantics questions get answered once, on the module, and every consumer
contract inherits the answer.

Cross-links (the seam decision and the fan-in fact live in the product-forge section;
this capture is the producer-side consequence):
[`../product-forge/games-web-mineverse-scope-seam-2026-07-11.md`](../product-forge/games-web-mineverse-scope-seam-2026-07-11.md) ·
[`../product-forge/read-projection-fanin-fourth-consumer-2026-07-11.md`](../product-forge/read-projection-fanin-fourth-consumer-2026-07-11.md)

**Why now:** the batched read-only-API providing ORDER and games-web phase-2 are both
unrouted at fetch time — this is the last moment "one projection, two serializations"
is a design choice rather than a migration; whichever way the games-web↔mineverse
seam resolves, the producer side of both outcomes is this same module.
