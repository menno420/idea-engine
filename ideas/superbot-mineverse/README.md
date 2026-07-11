# ideas/superbot-mineverse

> **Target lane:** `menno420/superbot-mineverse` (roster-derived section — see README.md § Sections).

Ideas FOR this lane: files per the idea grammar, harvested lane-born ideas indexed by
link below. Claim this section (`control/claims/`) before working it.

## Index

*(ordered per Q-0259 priority — games completion wave + rebuild pace first; first
batch grounded @ superbot-mineverse `510fa3e` (heartbeat 03:58Z, ladder
0/a/b/c done + (d) prepared, 187 tests) + fleet-manager `dd8dc10` (roster still gen
#4 @ 01:58Z — its row for this lane is four ladder rungs behind the heartbeat; lane
truth cited throughout), 2026-07-11. Honesty-guard drops recorded on the batch card:
structured machine-readable FLAG/dependency records (cross-cutting kit doctrine —
belongs to a substrate-kit/fleet section claim, not this one) and the remaining 9
ungraduated lane session-card 💡s (left in-lane; only the two FLAG-de-risking ideas
graduated, each linking its source card at the pin).)*

- [`mining-projection-single-source-2026-07-11.md`](mining-projection-single-source-2026-07-11.md) — parked(folded) · product (→ superbot): two independently-contracted read projections of the same bot-side mining state are now demanded — FLAG 1's push-cadence `mining_snapshot.v1` relay and fleet-manager's committed-JSON mining character-sheet feed — written on opposite sides of this lane's birth, neither citing the other; ONE bot-side projection module emitting both contracts makes the second surface a re-serialization, not a re-derivation
- [`snapshot-field-parity-audit-2026-07-11.md`](snapshot-field-parity-audit-2026-07-11.md) — parked(build-direct) · product: the mineverse side of the scope seam — probed 2026-07-11, first-cut coverage matrix run at both live pins (`2b1bd0b` · `a9c7401`): misses are three consumer-side flavor requireds (`gear.rarity`/`skills.xp`/`structures.status`) + a 7/9 slot map (`tool`/`light` homeless), no producer data debt — seam option (A) costed at one adapter + one games-web patch bump; durable table = lane PR, relaxation = product-forge PR, both providing-ORDER companions
- [`snapshot-contract-shared-constant-2026-07-11.md`](snapshot-contract-shared-constant-2026-07-11.md) — parked(build-direct) · product: graduates the lane-born ORDER 000 card idea — importable `snapshot_contract.py` / `REQUIRED_MINER_FIELDS` the superbot exporter imports too, turning FLAG 1 conformance into a CI drift gate on both sides instead of a runtime validator surprise — probed 2026-07-11 at live `2b1bd0b` (contracts byte-identical to pin, FLAG 1 unpicked): the schema-derived constant already lives in-test, the slice is a ~20-line scope promotion; sequenced with the seam ruling / FLAG 1 pickup
- [`shim-replay-determinism-harness-2026-07-11.md`](shim-replay-determinism-harness-2026-07-11.md) — parked(build-direct) · product: graduates the stage-(c) shim card idea — property-based replay-determinism test (idempotent replay / 409 on mutated reuse / audit-digest reproduction) holdable first against the shim, later verbatim against the real FLAG 2 endpoint via the fixture base-URL seam — probed 2026-07-11 at live `2b1bd0b` (file byte-identical to pin, FLAG 2 unpicked): one committed-seed property test, zero new deps; its evidence is its own runs, no sim question until a real endpoint exists
- [`heartbeat-ladder-field-2026-07-11.md`](heartbeat-ladder-field-2026-07-11.md) — parked(routed) · process (→ fleet-manager): a machine-parseable `ladder:` heartbeat line so the roster generator surfaces stage-level drift — probed 2026-07-11 at fleet-manager `6dedff6` / kit `941be2e`: the roster went MACHINE-GENERATED between capture and probe (gen #5, `scripts/gen_roster.py`, fm PR #62 — re-reads every heartbeat at verified HEAD each wake), mooting the auto-re-pin third of the payoff; the surviving structured-stage-diff value is a KIT grammar declaration decision (no ladder field in `grammar.py`; PR #59's fold-in-over-declare bars undeclared lane keys) with fm's generator as first consumer — routed via the heartbeat fan-in + cross-linked on `ideas/substrate-kit/README.md`; zero-grammar interim (ladder token in `phase:`, machine-quoted into the roster) available to any staged lane today

**SECTION COMPLETE (2026-07-11):** all 5 ideas probed-or-parked (1 folded · 3
build-direct · 1 routed) — no captured heads remain; new heads arrive by capture or
harvest per README § Sections.

## Cross-links

Sibling-section captures about this lane, indexed by link per the PR #17 grammar —
never duplicated: the games-web↔mineverse scope-seam decision
([`../product-forge/games-web-mineverse-scope-seam-2026-07-11.md`](../product-forge/games-web-mineverse-scope-seam-2026-07-11.md))
and the read-projection fan-in fourth-consumer fact
([`../product-forge/read-projection-fanin-fourth-consumer-2026-07-11.md`](../product-forge/read-projection-fanin-fourth-consumer-2026-07-11.md)).
