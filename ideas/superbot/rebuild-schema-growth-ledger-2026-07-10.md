# Idea — rebuild schema-growth ledger (enforce the second-consumer rule mechanically) — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot-next`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/rebuild-schema-growth-ledger-2026-07-03.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/rebuild-schema-growth-ledger-2026-07-03.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/rebuild-schema-growth-ledger-2026-07-03.md)).

Enforce the second-consumer rule mechanically: every schema-field addition to the rebuild grammar carries a same-PR ledger entry naming the ≥2 consumers that justified it, with a CI checker diffing grammar fields against the ledger.
