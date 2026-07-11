# snapshot_contract.py — one importable REQUIRED_MINER_FIELDS constant on both sides of FLAG 1

> **State:** parked(build-direct — one-file lane CI slice, no sim question; sequenced with the seam ruling / FLAG 1 pickup)
> **Class:** product · **Target:** `menno420/superbot-mineverse`
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-mineverse/510fa3e05cdac1244d70e65b71d048b7fdf38dd0/.sessions/2026-07-11-session.md@510fa3e · fetched 2026-07-11T04:00:20Z
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-mineverse/510fa3e05cdac1244d70e65b71d048b7fdf38dd0/control/status.md@510fa3e · fetched 2026-07-11T04:00:19Z
> **Sequence:** before the bot lane starts FLAG 1's relay exporter

## Problem

Graduates a lane-born idea (source card linked above — the lane's ORDER 000
walking-skeleton session, its 💡 verbatim: ship a `snapshot_contract.py` "that
validates any snapshot against the oracle field names pinned in
`tests/test_snapshot.py::REQUIRED_MINER_FIELDS` — then the live exporter on the
superbot side can import the same constant and structural drift becomes a test
failure instead of a runtime surprise"). The lane's `docs/ideas/` backlog is empty;
this idea exists only on that session card, and it de-risks exactly the seam FLAG 1
opens: today the required-field truth lives in a TEST constant on the web side, while
FLAG 1's done-when ("relay payload validates against the v1 schema") is a RUNTIME
check on the bot side — the two sides share no importable artifact, so an exporter
field rename surfaces as a validator rejection in production cadence, not in either
repo's CI.

## Idea

Promote the constant out of the test into an importable `snapshot_contract.py`
(REQUIRED_MINER_FIELDS + the envelope's required keys, derived from — or asserted
byte-equal against — `schemas/mining_snapshot.v1.schema.json` so the schema stays the
single source of truth), keep `tests/test_snapshot.py` importing it, and let the
superbot-side exporter (FLAG 1's builder; ideally the single projection module of
[`mining-projection-single-source-2026-07-11.md`](mining-projection-single-source-2026-07-11.md))
import or vendor-pin the same constant with a CI assertion. Contract conformance
becomes a compile-time/CI drift gate on BOTH sides: either side renaming a field goes
red at PR time, before a single relay push.

**Why now:** FLAG 1 is informational-until-picked-up at the pin — the constant is a
one-file lane slice that must exist BEFORE the exporter's first line to do its job;
after the exporter ships, the same artifact is a retrofit against live traffic.

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-mineverse/2b1bd0b9695ba4975d358895d0b9a52ab98507f4/tests/test_snapshot.py@2b1bd0b · fetched 2026-07-11T05:35:57Z

Single-pass battery v0, expiry-aware head (Sequence: before the bot lane starts
FLAG 1). Verify-first at build time: `git ls-remote` 05:34:43Z — superbot-mineverse
HEAD still `2b1bd0b`; its `control/status.md` (updated 04:27Z, re-fetched 05:34:55Z)
still carries both FLAG blocks as unpicked specs ("all remaining work externally
blocked (bot-lane FLAGs 1+2 …)"); superbot-next's queue (status.md @ 05:01Z) is
Discord parity ports, zero mineverse/FLAG work; fleet-manager roster gen #5 (04:28Z)
shows no FLAG pickup. **Window open.** All three pinned contract files re-fetched at
both pins 05:35:57Z: `tests/test_snapshot.py`, `schemas/mining_snapshot.v1.schema.json`,
`tests/test_actions.py` each byte-identical between capture pin `510fa3e` and live
`2b1bd0b` — the capture's grounding has not drifted. And the null check:
`snapshot_contract.py` at mineverse main is a 404 (fetched 05:35:57Z) — nobody built it.

**1. What is this really?** A scope promotion, not new validation. The capture's
"derived from the schema" clause is ALREADY satisfied in-test: `tests/test_snapshot.py`
@2b1bd0b line 22 reads `REQUIRED_MINER_FIELDS = tuple(_SCHEMA["$defs"]["miner"]["required"])`
(and the next line derives `REQUIRED_ENVELOPE_FIELDS = tuple(_SCHEMA["required"])` =
`schema_version` / `generated_at` / `guild_id` / `miners`). The schema-derived
required-fields truth exists; what's missing is only an importable NON-TEST module, so
the FLAG 1 exporter can vendor-pin the same artifact and both sides gate in CI.

**2. What is the possibility space?** Ascending: (i) a bare constants module
(`snapshot_contract.py` re-exporting the two derived tuples); (ii) + a
`validate_snapshot()` helper wrapping the vendored tests-only jsonschema; (iii) a
vendor-pin recipe with a byte-equal/hash CI assertion on the bot side; (iv) a full
contract package. Plus the null alternative: the exporter vendors
`schemas/mining_snapshot.v1.schema.json` itself and derives its own constant — the
module is then convention, not necessity; the schema is already the single source of
truth.

**3. What is the most advanced capability reachable by the simplest implementation?**
A ~20-line module that reads the schema at import time and exposes
`REQUIRED_MINER_FIELDS` (16 fields at v1) + `REQUIRED_ENVELOPE_FIELDS`, with
`tests/test_snapshot.py` switched to import it. Bot side vendor-pins + hash-checks in
its CI → a two-sided PR-time drift gate on field renames in EITHER direction, for the
cost of one file and a two-line test edit.

**4. What breaks it?** (a) No cross-repo import exists — the bot side's copy is a
SECOND artifact that itself drifts unless its CI asserts byte-equality against the
pinned raw path (network in CI) or against a vendored schema — ceremony the schema
alone already provides; the marginal value over "vendor the schema" is the import
surface. (b) That surface's only buyer, the FLAG 1 exporter, does not exist yet.
(c) The pending seam ruling: the just-merged parity audit (PR #92,
[`snapshot-field-parity-audit-2026-07-11.md`](snapshot-field-parity-audit-2026-07-11.md))
costed seam option (A) at one client-side adapter incl. serializer constants + one
games-web patch bump — the ruling may relocate where this family of constants lives;
building before it risks the constant getting a second home.

**5. What does it unlock?** The FLAG 1 builder starts against an executable contract
instead of prose; the parity-audit adapter gets a stable import; contract drift goes
PR-red in CI instead of runtime-red at relay cadence (the source card's exact
"test failure instead of a runtime surprise").

**6. What does it depend on?** `schemas/mining_snapshot.v1.schema.json` @2b1bd0b
(verified byte-identical to pin 510fa3e, 05:35:57Z); FLAG 1 still unpicked (verified,
see header — the artifact must precede the exporter's first line to do its job); a
bot-lane vendor/pin mechanism (does not exist yet); the manager's seam-ruling
sequencing (pending at the :30 sweep).

**7. Which lane should build it?** superbot-mineverse — it owns the schema and the
tests; the superbot bot lane consumes via vendor-pin when FLAG 1 is picked up. Not
idea-engine, not sim-lab.

**8. What is the smallest shippable slice?** `snapshot_contract.py` (~20 lines,
schema-derived miner + envelope requireds) + `tests/test_snapshot.py` switching its
two constant lines to import it — zero behavior change; the existing tests prove the
promotion.

**Recommendation: park** — build-direct: a one-file lane CI slice with no empirical question a sim can settle; sequenced with the seam ruling / FLAG 1 pickup so the constant lands in its final home.
