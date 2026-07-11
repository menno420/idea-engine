# Snapshot field-parity audit — make mining_snapshot.v1 sufficient for the seam's cheapest outcome

> **State:** parked(build-direct — lane-side measurement, first cut run in the probe at both live pins (mineverse `2b1bd0b` · product-forge `a9c7401`, 2026-07-11T05:01Z): games-web's required-leaf coverage misses are three consumer-side flavor requireds (`gear.rarity` · `skills.xp/xp_max` · `structures.status`) plus a 7/9 gear-slot map with `tool`/`light` homeless — NO producer data debt, so seam option (A) is costed at one adapter + one games-web patch bump with zero `mining_snapshot.v1` breaking changes; durable table + slot map = one superbot-mineverse PR, requiredness relaxation = one product-forge PR, both companions of the batched providing ORDER — see probe report)
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

## Probe report (v0, 2026-07-11 — single pass)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-mineverse/2b1bd0b9695ba4975d358895d0b9a52ab98507f4/schemas/mining_snapshot.v1.schema.json@2b1bd0b · fetched 2026-07-11T05:01Z
> **Grounding:** https://github.com/menno420/product-forge/blob/a9c7401856e47974f5fc3f56f45f9cc5c844186f/products/games-web/data/schema/game-state.schema.json@a9c7401 · fetched 2026-07-11T05:02Z
> *(pin annotation: both pins are live HEAD at fetch time, `git ls-remote` 05:01:08Z — superbot-mineverse `2b1bd0b` UNMOVED since the seam probe's 04:33Z pin; product-forge moved `8c64db4`→`a9c7401` by exactly ONE commit, its PR #18 "control: append ORDER 003 — fix future-dated status.md heartbeat", control-only (+8 lines control/inbox.md, nothing under products/**) — the contract file's last touch stays commit `b86e7ef` (v1.0.1). Lane conformance anchors path-verified 200 at the mineverse pin: `tests/test_schema_gate.py` (Draft202012Validator) + `docs/mining-data-contract.md`.)*

*Timeliness verified live FIRST (this capture's `Sequence:` names a closing window):
NEITHER contract has frozen. mineverse @ `2b1bd0b`: FLAGs 1+2 still unbuilt, "all
remaining work externally blocked" (04:27Z heartbeat) — the snapshot's only live
consumer is the lane's own read side, and the schema is additive-only within v1 by its
own description. games-web @ `a9c7401`: contract v1.0.1, mock-only, ZERO external
consumers — the Pages deploy is prepped but NOT LIVE (run 29126980391 failed:
Pages not enabled, owner click OA-003 pending) and phase-2 is unrouted. The window is
open, but one owner click (Pages) or one FLAG-1 ship closes the cheap half — probe
honest, and urgent in the same direction the seam ruling is.*

**1. What is this really?** A measurement, not a design — and it is cheap enough that
this probe ran the first cut instead of describing it: a field-by-field diff of the two
committed JSON Schemas at the live pins above. The capture's one accidental datapoint
(9-slot gear vs 8) understated the finding in one way and overstated it in another:

| games-web v1.0.1 field (REQUIRED unless noted) | mining_snapshot.v1 source @ `2b1bd0b` | class |
|---|---|---|
| `schema_version` · `contract` | envelope `schema_version` (const `"1"`); `contract` is a self-identifier | covered / serializer-constant |
| `generated_at` | envelope `generated_at` | covered |
| `character.name` | `miner.display_name` | covered |
| `character.level` | `miner.xp.level` | covered |
| `character.class` · `character.title` (req), `character.portrait` (opt) | none | serializer-constant — comic-RPG flavor with no producer truth needed |
| `stats[] {key,label,value}` (minItems 1) | `coins` · `energy.current`/60 · `depth` · `record_depth` · `position` · `vault_level` | covered-by-projection (labels/hints are serializer-side) |
| `gear{}` — 8 fixed fantasy slots, additionalProperties:false | `equipment` — closed 9-slot mining set | **semantically different**: 7/9 map injectively (helmet→head · chestplate→chest · leggings→legs · boots→feet · weapon→main_hand · shield→off_hand · charm→trinket); `tool` and `light` — the two mining-defining slots — have no home (only `hands` is free): a miner's pickaxe is unrenderable |
| `gear.<slot>.name` | `equipment` values (open-ended item-name strings) | covered for the 7 mapped slots |
| `gear.<slot>.rarity` — REQUIRED enum(common…legendary) | none — no rarity concept anywhere in the snapshot or the oracle item model it describes | **semantically different** — and NOT cheaply additive: the producer has no truth to project |
| `gear.<slot>.power` (opt) | none (`gear_wear` is a different semantic) | no source |
| *(reverse direction)* `gear_wear` countMap | — | games-web has NO wear slot: the one gear datum mineverse renders beyond names is dropped |
| `skills[] {key,level}` | `skills` countMap name→rank | covered |
| `skills[].xp` · `.xp_max` — REQUIRED | none — snapshot `xp` is the game-level quartet {game, game_total, shared_total, level}; nothing per-skill | **semantically different** — additively coverable ONLY IF `game_xp_service` tracks per-skill xp (not answerable from the contract; the lane's one real reachability check) |
| `structures[] {key,tier}` | `structures` countMap name→count/tier | covered |
| `structures[].status` — REQUIRED enum(idle,working,upgrading,locked) | none | **semantically different** — no producer truth |

Headline, and it inverts the capture's costing direction: every games-web field family
is covered or projection-covered EXCEPT three required leaves — `gear.rarity`,
`skills.xp/xp_max`, `structures.status` — plus the slot vocabulary, and ALL THREE
misses are games-web-side presentation flavor with no producer truth behind them. The
cheap pre-freeze fix is mostly NOT "additive v1 fields on `mining_snapshot.v1`" (the
capture's framing): it is a games-web v1.1 relaxing three flavor requireds to optional
(a mock with zero consumers — patch-cheap today), plus a committed slot map, plus AT
MOST one candidate additive snapshot family (per-skill xp, if the oracle even has it).

**2. What is the possibility space?** (i) the capture as written — lane-side audit
table + additive snapshot fields; (ii) the inverted form the measurement supports —
games-web-side requiredness relaxation + a committed slot map, snapshot untouched;
(iii) fusion with the shared-constant sibling
(`snapshot-contract-shared-constant-2026-07-11.md`) — the slot map and field list live
in the importable `snapshot_contract.py` both sides' CI gates on, making the audit a
standing drift gate instead of a one-shot table; (iv) wait-for-the-ruling — rejected
by the capture's own window logic (the audit is cheap exactly until a consumer ships).

**3. What is the most advanced capability reachable by the simplest implementation?**
Option (A) of the seam becoming execution-ready the day of the ruling: a ~15-row
committed table + a games-web v1.1 patch means games-web renders REAL miners from
`mining_snapshot.v1` through a pure client-side adapter (slot map + serializer
constants for class/title, rarity/status/xp-bars degrading gracefully) — no second
serializer, no bespoke endpoint, no v2, no breaking change on either side. The audit
converts PR #87's ranking premise "(A) looks cheapest" into "(A) costs one adapter
file + one consumer-side patch bump + zero producer changes."

**4. What breaks it?** (i) Misreading the gaps as producer debt — an ORDER that makes
`mining_snapshot.v1` grow `rarity` invents data the oracle doesn't own
(pattern-exists ≠ pattern-can-produce, the README's reachability discipline); (ii) a
freeze event — Pages going live is ONE owner click away (OA-003) and FLAG 1 shipping
creates the first external consumer; either makes the games-web relaxation a breaking
change and the window's cheap half closes; (iii) per-skill xp reachability — if
`game_xp_service` doesn't track it, games-web's skill bars must degrade to level-only,
a renderer change beyond the schema patch; (iv) auditing the mock renderer instead of
the contract — the fixtures render fine forever; the schema is what freezes.

**5. What does it unlock?** The one measurable input PR #87's ruling lacked, delivered:
(A) is now costed, sharpening A > B-artifacts-kept > C with a number attached. Under
(B) the same table IS the reconciliation artifact; under (C) it is the migration
checklist — the measurement is ruling-invariant, only its label changes. It also
seeds the shared-constant sibling with its exact content (slot map + field list) and
hands the batched providing ORDER its mineverse-side acceptance row.

**6. What does it depend on?** Both contracts staying pre-freeze (verified live this
pass, pins above); the lane's existing conformance machinery for the durable gate
(`tests/test_schema_gate.py`, Draft202012Validator — path-verified at `2b1bd0b`); one
bot-side reachability check (does `game_xp_service` track per-skill xp — superbot
repo, answerable inside the lane's audit slice); and the manager's ORDER for the
cross-lane half (the games-web v1.1 relaxation belongs to product-forge; this repo
writes neither lane's files).

**7. Which lane should build it?** superbot-mineverse — it owns the schema,
`docs/mining-data-contract.md`, and the CI gate the table should live next to; the
relaxation half is product-forge's, one patch PR. NOT sim-lab: the audit is a
lane-runnable measurement over two committed files, and this probe already ran its
first cut — reproduced evidence would re-diff the same two schemas and tell the
manager nothing the matrix above doesn't. The decision-ripe consumer is the manager's
seam ruling, and the finding rides this PR's heartbeat fan-in note to the :30 sweep
now, without a sim round-trip.

**8. What is the smallest shippable slice?** Here: this probe report (first-cut matrix
+ (A)'s costing, folded into the read-only-API fan-in note). Lane-side, two
ORDER-companion one-PR slices: superbot-mineverse commits the audit table + slot map
beside `docs/mining-data-contract.md` (plus the ONE additive OPTIONAL per-skill-xp
family behind the existing schema gate, iff the reachability check passes);
product-forge ships game-state v1.1 relaxing `rarity`/`status`/`xp_max` to optional
while the mock still has zero consumers. Neither blocks the ruling; both make (A)
free to take.

**Recommendation: park** — (build-direct — feeds the manager's seam ruling): a
lane-side measurement whose first cut this probe ran at both live pins — the coverage
misses are three consumer-side flavor requireds (`gear.rarity` · `skills.xp/xp_max` ·
`structures.status`) plus a 7/9 slot map with `tool`/`light` homeless, and NO producer
data debt — so seam option (A) is now costed at one adapter + one games-web patch
bump with zero `mining_snapshot.v1` breaking changes; no simulator question remains,
and the sharpened fan-in line ships in this PR's heartbeat.
