# snapshot_contract.py — one importable REQUIRED_MINER_FIELDS constant on both sides of FLAG 1

> **State:** captured
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
