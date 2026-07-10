# Reconciliation helper: classify a band's PRs as merged / closed-unmerged / open — link index

> **State:** historical(shipped 2026-06-20 in superbot as `scripts/band_pr_status.py`)
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/band-pr-merge-status-helper-2026-06-19.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/band-pr-merge-status-helper-2026-06-19.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/band-pr-merge-status-helper-2026-06-19.md)).

A helper that classifies a reconciliation band's PRs as merged / closed-unmerged / open, replacing the by-hand verification that the ledger checker cannot do (it can't tell a closed-unmerged PR from a missing merged one).
