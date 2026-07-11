# Read-projection fan-in: a fourth consumer is visible, and games-web fits rung 1

> **State:** captured
> **Class:** process · **Target:** `menno420/product-forge`
> **Grounding:** https://raw.githubusercontent.com/menno420/product-forge/0a6efe96ef8021679b9f8a6ee63a617cd9d61ffc/products/games-web/docs/phase2-data-api-proposal.md@0a6efe9 · fetched 2026-07-11T03:33Z
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-mineverse/01a8b8572507f5dd5b65109161091b90272cc57b/control/status.md@01a8b85 · fetched 2026-07-11T03:34:14Z
> **Sequence:** before the manager routes the batched superbot read-only-API providing ORDER

**Canonical fan-in stays where it is — cross-linked, never duplicated:** the batched
superbot read-only-API providing ORDER, its two-rung split (RUNG 1 = zero-auth
committed `leaderboards` feed; RUNG 2 = token-scoped API on the same plumbing), and
its three known consumers (websites leaderboards page · PROPOSAL 002 phase 3 ·
product-forge games-web ORDER 001) are held in the `control/status.md` read-only-API
fan-in note and the PR #45 probe
([`ideas/websites/public-leaderboards-committed-feed-2026-07-10.md`](../websites/public-leaderboards-committed-feed-2026-07-10.md)).
This capture only adds the two facts newly visible from the lanes' live HEADs.

## Fact 1 — a FOURTH convergent read-projection demand exists

superbot-mineverse's heartbeat @ `01a8b85` carries **⚑ FLAG 1** to the superbot
manager/bot lane: emit a mining snapshot conforming to its
`schemas/mining_snapshot.v1.schema.json` into the bot→web read relay (~60s push +
on-demand). That is a fourth consumer-shaped ask landing on the same producer the
batched ORDER covers — different egress mechanism (relay push vs committed feed vs
API), same `mining_player_state` + `game_xp_service` source. The fan-in note predates
it. Concrete divergence datapoint: games-web's `games-web.character-sheet` fixes
`gear{}` at 8 slots; mineverse renders a 9-slot gear panel with wear — two contracts
for one dataset are already drifting apart before the producer has shipped either.

## Fact 2 — games-web's own design makes it a RUNG-1 consumer, not rung 2

The phase-2 proposal asks for an HTTP endpoint
(`GET /v1/games-web/character-sheet/{id}`), but its own transport is a client-side
JSON fetch, schema-validated, with fallback-to-mock on any failure — a **committed**
character-sheet feed (raw path, zero auth, same commit-back mechanism rung 1 proves)
is a drop-in conforming "live source" under that design. The endpoint ask can be
re-scoped onto the rung-1 mechanism; games-web stops waiting on rung 2 entirely.

## Smallest forge-side slice

Amend `products/games-web/docs/phase2-data-api-proposal.md` to (1) accept a committed
feed as a conforming transport, and (2) map `games-web.character-sheet` fields onto
`mining_snapshot.v1` — or record why one projection cannot serve both skins. (The
proposal's own §"the ask" item 1 already invites this: "does superbot already emit
something close? Map it, don't reinvent.")

**Why now:** the manager routes ONE batched ORDER; every consumer and every
contract-shape divergence visible at routing time is a migration nobody has to run
later.
