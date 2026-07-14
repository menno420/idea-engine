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

- [`snapshot-stale-indicator-threshold-2026-07-13.md`](snapshot-stale-indicator-threshold-2026-07-13.md) — sim-ready · process (→ sim-lab): the READ contract's staleness rule ships a hedged constant ("default suggestion: 3 missed cycles ≈ 180 s" at the 60 s target cadence, `docs/mining-data-contract.md` § Delivery expectations @ `ae98dd0`) with both failure axes named in its own sentence (a cry-wolf stale badge vs presenting old numbers as live) and neither priced — pre-registered hermetic renewal-reward sim (exact-Fraction Arm A + seeded timeline Arm S, seeds 20261317–320), REJECT-first bands 1/200 false-stale · 240 s mean detection; harvested 2026-07-13 for the ORDER 003 fleet-backlogs rotation slot, round 8 (PROPOSAL 045)
- [`badge-saturation-coin-magnate-2026-07-14.md`](badge-saturation-coin-magnate-2026-07-14.md) — sim-ready · game-mechanics (→ sim-lab): the achievement catalog's showcase wealth badge (`COIN_MAGNATE_THRESHOLD = 10_000` shared-wallet coins, `server/views.py` @ `b983291`) carries its own calibration claim ("some miners hit it … and some don't", calibrated against the frozen 7-miner sample file) — never priced against the hub's committed faucet `_DAILY_TIERS` (E[`!daily`] = 169201/100 exact, superbot @ `3477594`, both pins firsthand): 10,000 coins is 5.91 expected dailies, so the badge may be an account-age stamp, not a wealth discriminator — pre-registered hermetic sim (exact absorbing-DP Arm A + seeded MC Arm S, seeds 20261357–360), REJECT-first bands 19/20 season-share at ≥ 3 of 4 claim-rate cells + ≤ 14-day full-engagement median; harvested 2026-07-14 for the ORDER 003 game-mechanics rotation slot, round 10 (PROPOSAL 055)

**SECTION COMPLETE (2026-07-11):** all 5 founding ideas probed-or-parked (1 folded ·
3 build-direct · 1 routed) — no captured heads remained; new heads arrive by capture
or harvest per README § Sections (first such harvest: the 2026-07-13
stale-indicator head above, PROPOSAL 045).

## Cross-links

Sibling-section captures about this lane, indexed by link per the PR #17 grammar —
never duplicated: the games-web↔mineverse scope-seam decision
([`../product-forge/games-web-mineverse-scope-seam-2026-07-11.md`](../product-forge/games-web-mineverse-scope-seam-2026-07-11.md))
and the read-projection fan-in fourth-consumer fact
([`../product-forge/read-projection-fanin-fourth-consumer-2026-07-11.md`](../product-forge/read-projection-fanin-fourth-consumer-2026-07-11.md)).
