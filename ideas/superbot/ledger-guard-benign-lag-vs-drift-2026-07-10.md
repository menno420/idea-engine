# Idea — the ledger guard should distinguish *benign newest-merge lag* from real drift — link index

> **State:** historical(implemented 2026-06-19 in superbot, Q-0015 grooming pass)
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/ledger-guard-benign-lag-vs-drift-2026-06-14.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/ledger-guard-benign-lag-vs-drift-2026-06-14.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/ledger-guard-benign-lag-vs-drift-2026-06-14.md)).

The ledger guard treated any recent unlisted merge as drift; partition findings into real drift (older than the reconciliation marker) vs benign newest-merge lag.
