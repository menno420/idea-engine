# Continuously-verified backups — the restore drill as a scheduled workflow (2026-07-02) — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/continuously-verified-backups-2026-07-02.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/continuously-verified-backups-2026-07-02.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/continuously-verified-backups-2026-07-02.md)).

Upgrade the one-shot restore drill into standing CI: a scheduled workflow restores the newest backup into a Postgres service container and asserts substance (table floor, row counts on load-bearing tables, spot values), opening an issue on failure.
