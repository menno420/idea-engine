# Registry-shrinkage sentinel fixture — "the world a suite finds is the world it leaves"

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot-next`
> **Grounding:** https://github.com/menno420/superbot-next@80464ab39f86d55cede1e38b4780e7b1cc4a1777 · fetched 2026-07-12T01:34:18Z

One session-scoped autouse fixture in the lane's `tests/conftest.py` that snapshots
`ref_inventory()` + `provider_names()` at each test-DIRECTORY boundary and asserts no
shrinkage — so the next one-way registry wipe fails red NAMING the leaking suite,
instead of surfacing as an 11-victim canonical-order mystery three bands downstream
(the flake class the lane just hand-diagnosed: three isolation-leak mechanisms behind
one ordering-dependent failure). Turns the debugging invariant the fix session stated
verbatim — "the world a suite finds is the world it leaves" — into a standing sentinel.
Source: lane session card [`.sessions/2026-07-12-canonical-order-flake-fix.md` § "💡
Session idea"](https://github.com/menno420/superbot-next/blob/80464ab39f86d55cede1e38b4780e7b1cc4a1777/.sessions/2026-07-12-canonical-order-flake-fix.md)
@ `80464ab` ([raw](https://raw.githubusercontent.com/menno420/superbot-next/80464ab39f86d55cede1e38b4780e7b1cc4a1777/.sessions/2026-07-12-canonical-order-flake-fix.md)).
