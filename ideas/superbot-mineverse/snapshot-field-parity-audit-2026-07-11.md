# Snapshot field-parity audit — make mining_snapshot.v1 sufficient for the seam's cheapest outcome

> **State:** captured
> **Class:** product · **Target:** `menno420/superbot-mineverse`
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-mineverse/510fa3e05cdac1244d70e65b71d048b7fdf38dd0/control/status.md@510fa3e · fetched 2026-07-11T04:00:19Z
> *(pin annotation: schemas/mining_snapshot.v1.schema.json path-verified 200 at the same pin, 04:00:21Z; games-web contract facts cited via the product-forge seam capture's pins, never re-derived here)*
> **Sequence:** before either contract freezes — i.e. before the games-web↔mineverse seam ruling and the batched providing ORDER

## Problem

This is the mineverse side of the scope seam
([`../product-forge/games-web-mineverse-scope-seam-2026-07-11.md`](../product-forge/games-web-mineverse-scope-seam-2026-07-11.md)):
that capture's cheapest-looking outcome (A) has games-web consuming the
mineverse-side projection instead of a bespoke character-sheet endpoint. Whether that
ruling can actually be taken depends on a fact nobody has measured: does
`mining_snapshot.v1` (16 per-miner v1 fields @ `510fa3e`) COVER what
`games-web.character-sheet` v1.0.1 renders? The one datapoint already visible cuts
both ways — mineverse renders a 9-slot gear panel with wear while games-web fixes
`gear{}` at 8 slots without it — and the divergence was found by accident, in a
cross-repo read, not by any audit either lane ran.

## Idea

One lane-side slice: a field-by-field coverage audit of `mining_snapshot.v1` against
`games-web.character-sheet` v1.0.1 — for each games-web field: covered / coverable by
additive v1 field / semantically different (like the gear-slot count) — committed as
a short table next to `docs/mining-data-contract.md`, plus the additive v1 fields the
audit shows are cheap to add now. The lane's own conformance machinery
(`tests/test_schema_gate.py`, Draft202012Validator) already gates additions. Result:
IF the seam resolves to "games-web consumes the mineverse projection", the relay is
already sufficient the day of the ruling — additive v1 fields are cheap before
anyone consumes them; breaking changes after two frontends render the contract are
not.

**Why now:** both contracts are pre-freeze at fetch time (FLAG 1 unbuilt, games-web
phase-2 unrouted); the audit is cheap exactly until the first consumer ships against
either shape, and it sharpens the seam probe's option (A) from plausible to costed.
