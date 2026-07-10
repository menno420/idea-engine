# Idea: backup dump integrity check — link index

> **State:** historical(executed 2026-06-13 in superbot — CREATE TABLE-count gate in `backup-db.yml`)
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/backup-integrity-check-2026-06-13.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/backup-integrity-check-2026-06-13.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/backup-integrity-check-2026-06-13.md)).

Verify each database backup dump contains a minimum number of CREATE TABLE statements before trusting it — a cheap integrity floor on the nightly dump.
