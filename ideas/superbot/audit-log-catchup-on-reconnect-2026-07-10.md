# Idea — Audit-log catch-up on reconnect (gap-free logging across restarts) — link index

> **State:** captured
> **Class:** product · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/audit-log-catchup-on-reconnect-2026-07-01.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/audit-log-catchup-on-reconnect-2026-07-01.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/audit-log-catchup-on-reconnect-2026-07-01.md)).

Gateway-based logging misses everything during restarts/deploys; on reconnect, fetch the Discord audit log and backfill (with dedup) the moderation events that happened while disconnected — gap-free logging across downtime.
