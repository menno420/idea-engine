# Ledger dedup linter (companion to the merge=union fix) — link index

> **State:** historical(shipped in superbot as `scripts/check_ledger_hygiene.py`, 2026-06-19; de-staled 2026-06-27)
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/ledger-dedup-linter-2026-06-16.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/ledger-dedup-linter-2026-06-16.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/ledger-dedup-linter-2026-06-16.md)).

Companion to the merge=union fix: union never dedups, so the append-only coordination ledgers accumulate duplicates — a linter that flags them.
