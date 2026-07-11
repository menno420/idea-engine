# Shim replay-determinism property harness — FLAG 2's done-when, executable before the builder starts

> **State:** parked(build-direct — one-file lane test slice; its evidence is its own runs; no sim question until a real endpoint exists)
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

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-mineverse/2b1bd0b9695ba4975d358895d0b9a52ab98507f4/tests/test_actions.py@2b1bd0b · fetched 2026-07-11T05:35:57Z

Single-pass battery v0, expiry-aware head (Sequence: before the bot lane starts
FLAG 2). Same build-time verify-first as the sibling probe run in this batch
(05:34:43–05:35:57Z): mineverse HEAD still `2b1bd0b`, its status.md (04:27Z) still
carries FLAGs 1+2 as unpicked externally-blocked specs, superbot-next's queue has
zero mineverse/FLAG work, roster gen #5 shows no pickup — **window open**.
`tests/test_actions.py` re-fetched at both pins 05:35:57Z: byte-identical between
capture pin `510fa3e` and live `2b1bd0b`. One capture correction, counting-method
not drift: the live file has **35** `def test_` functions, not the capture's "34
cases" — the file bytes are unchanged since the pin, so the discrepancy is in how
the source card counted, not in the contract.

**1. What is this really?** An upgrade of FLAG 2's acceptance semantics from
example-based (35 test functions, each pinning a single behavior — one replay, one
409, one audit row) to a SEQUENCE invariant: replay determinism over arbitrary
accepted action sequences. Written against the shim NOW, it makes the shim's
semantics the executable contract before a real endpoint can anchor them by
accident — FLAG 2's done-when stops being "the examples pass" and becomes "the
invariant holds".

**2. What is the possibility space?** Ascending: (i) a single committed-seed
generator + three assertions (idempotent full-sequence replay — every response
`replayed:true`, state unchanged; 409 `reason_code=replayed_action` on mutated
`action_id` reuse without clobbering the original; cross-shim replay reproducing
identical audit `params_digest` rows + final state); (ii) a multi-seed sweep;
(iii) hypothesis-with-shrinking (rejected — no new deps, the lane vendors jsonschema
tests-only and nothing else); (iv) the identical property run against the REAL
endpoint via the `make_shim_server` → base-URL fixture seam (`shim` fixture,
test_actions.py line 126, yields `(state, base_url)`); (v) a divergence-class
taxonomy once a real endpoint exists to diverge.

**3. What is the most advanced capability reachable by the simplest implementation?**
One test function, stdlib `random` with a committed seed — a portable determinism
contract that runs verbatim against the real endpoint on day one through the
base-URL seam the source card's guard recipe already names.

**4. What breaks it?** (a) One committed seed is ONE trajectory, not a property
sweep — a coverage illusion if oversold; state honestly. (b) The byte-identical-body
assertion over-constrains if the real endpoint legitimately varies response bytes
(timestamps, ordering) — pin the invariant to contract fields, not whole bodies, or
it false-fails at the fixture swap. (c) If the shim's semantics are wrong, the
harness cements the wrong contract — mitigated: the shim IS the contract's only
reference today (per the stage-(c) source card). (d) Real-endpoint concurrency is
outside what the single-process shim models.

**5. What does it unlock?** An executable spec for the FLAG 2 builder on day one; a
regression net for any shim change; later, a live divergence detector via the
base-URL swap — the property is the reusable artifact, the shim is just its first
host.

**6. What does it depend on?** `tests/test_actions.py` @2b1bd0b (verified
byte-identical to pin 510fa3e, 05:35:57Z); the `make_shim_server` fixture seam (line
41/126, verified present); the vendored tests-only jsonschema; FLAG 2 still unpicked
(verified, see header — the harness is honest only while the shim is the sole
reference).

**7. Which lane should build it?** superbot-mineverse — it owns the shim and its
tests; the property later binds the bot lane's real endpoint through the fixture
seam. Not idea-engine, not sim-lab.

**8. What is the smallest shippable slice?** One property test in
`tests/test_actions.py` — committed-seed random walk over the closed action enum
(~100 actions), the three assertions from Q2(i), a second fresh shim for the
reproduction leg; zero new deps. Honest sim-judgment: a property harness is proven
by its own runs — RUNNING it is cheaper than simulating it, and the one genuinely
open empirical question (which divergence classes appear shim-vs-real) is
unanswerable until FLAG 2's endpoint exists — nothing for sim-lab to settle today.

**Recommendation: park** — build-direct: one-file lane test slice whose evidence is its own runs; the only sim-shaped question needs the not-yet-existing real endpoint; window verified open.
