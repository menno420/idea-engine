# Idea — scale the ledger-checker window to "merges since the last reconciliation marker" — link index

> **State:** historical(implemented 2026-06-19 in superbot, Q-0015 grooming pass)
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/ledger-window-scale-to-marker-2026-06-19.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/ledger-window-scale-to-marker-2026-06-19.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/ledger-window-scale-to-marker-2026-06-19.md)).

The ledger checker's fixed 15-PR window under-scans burst bands (~21 missing, 13 flagged); size the window to 'merges since the last reconciliation marker'.
