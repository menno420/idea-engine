# Shim replay-determinism property harness — FLAG 2's done-when, executable before the builder starts

> **State:** captured
> **Class:** product · **Target:** `menno420/superbot-mineverse`
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-mineverse/510fa3e05cdac1244d70e65b71d048b7fdf38dd0/.sessions/2026-07-11-write-ui-shim-v1.md@510fa3e · fetched 2026-07-11T04:00:20Z
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-mineverse/510fa3e05cdac1244d70e65b71d048b7fdf38dd0/control/status.md@510fa3e · fetched 2026-07-11T04:00:19Z
> **Sequence:** before the bot lane starts FLAG 2's write endpoint

## Problem

Graduates the other lane-born idea (source card linked above — the stage-(c) shim
session, its 💡 verbatim: "for any accepted action sequence, replaying the sequence
through a fresh shim must reproduce identical audit digests and final state — a
cheap invariant harness the real bot-side endpoint could later be held to as well").
FLAG 2's done-when is already fixture-shaped — "shim contract fixtures
(tests/test_actions.py) pass against the real endpoint" — and the card's guard recipe
names the seam: swap the `shim` fixture's base URL (`make_shim_server` → base URL)
for the real endpoint. But the current 34 `test_actions.py` cases are example-based:
they pin single behaviors (one replay, one 409, one audit row), not the SEQUENCE
invariant that makes a write path trustworthy — that idempotent replay
(same `action_id` + same body → `replayed:true`, never re-executed) and 409
`replayed_action` on key reuse hold across arbitrary interleavings, and that the
audit trail deterministically reproduces.

## Idea

One lane-side slice, zero new deps beyond the tests-only jsonschema already vendored:
a property-based replay-determinism test in `tests/test_actions.py` — generate
random valid action sequences over the closed enum (stdlib `random` with a committed
seed is enough; no hypothesis dependency needed), apply them to a fresh shim, then
(a) replay the full sequence against the same shim and assert every response is
`replayed:true` with byte-identical bodies and zero re-execution (state unchanged),
(b) reuse an `action_id` with a mutated body and assert 409 `replayed_action` without
clobbering the original, and (c) replay the accepted subsequence through a SECOND
fresh shim and assert identical audit `params_digest` rows and final state. Because
it lives behind the same fixture base-URL seam, the identical property runs verbatim
against the real endpoint the day it exists — FLAG 2's done-when stops being "the
examples pass" and becomes "the invariant holds".

**Why now:** FLAG 2 is informational-until-picked-up at the pin — the harness is
cheapest and most honest written against the shim BEFORE any real implementation
exists to anchor on; once the builder lane starts, the shim's semantics quietly stop
being the contract's only reference.
