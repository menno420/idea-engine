# Read-projection fan-in: a fourth consumer is visible, and games-web fits rung 1

> **State:** parked(absorbed — both facts ride the heartbeat's read-only-API fan-in note, their declared destination, since the #71 slice; verified at the fan-in note + the Sequence window still open at superbot inbox @ `58040c6` — see the disposition note below)
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

## Disposition (2026-07-11 — verify-and-park form, no battery: the #66/#131 class)

This capture was a fact-relay by its own declaration ("this capture only adds the
two facts"), and both facts reached their declared destination the day they were
born: the `control/status.md` read-only-API fan-in note has carried Fact 1 (the
mineverse FLAG-1 fourth convergent consumer, with the 8-slot vs 9-slot contract
divergence datapoint) and Fact 2 (games-web is a RUNG-1 committed-feed consumer —
"its rung-2 placement below is SUPERSEDED") since the #71 slice, naming this file as
the full capture; the #87 seam probe then sharpened the same note (three-transport
divergence · missing-bus finding · A>B>C ranking). Nothing here was ever a separate
probe head — the honest state is parked(absorbed), not a battery pass.

Window check at disposition time: the `Sequence:` ("before the manager routes the
batched providing ORDER") still holds OPEN — superbot's `control/inbox.md` now
exists (superbot PR #1977; the missing-bus blocker is gone) but carries only ORDER
001 at HEAD `58040c6` (fetched 2026-07-11T09:11Z), and fm ORDER 012/013 @ `3150f0e`
decided placement without yet filing the superbot-side order — so the facts sit at
their destination ahead of the routing they exist to inform, which is the capture's
whole point. The residual "smallest forge-side slice" (amend
`products/games-web/docs/phase2-data-api-proposal.md` to accept a committed feed +
map `games-web.character-sheet` onto `mining_snapshot.v1`) is a one-file
product-forge slice that naturally rides the providing ORDER's routing — recorded
here, nothing to route separately. State stays forward-only; no recommendation
token (disposition, not a probe).
