# Idea — the ledger guard should exempt self-referential reconciliation PRs — link index

> **State:** historical(shipped 2026-06-16 in superbot, Q-0152)
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/ledger-guard-exempt-reconciliation-prs-2026-06-16.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/ledger-guard-exempt-reconciliation-prs-2026-06-16.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/ledger-guard-exempt-reconciliation-prs-2026-06-16.md)).

A reconciliation PR cannot list its own number (it doesn't exist when the body is written); exempt self-referential reconciliation PRs from the ledger guard's missing-PR check.
