# Idea — a lint that flags routine-common commands that would hit the `ask` permission brake — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/routine-permission-surface-lint-2026-06-16.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/routine-permission-surface-lint-2026-06-16.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/routine-permission-surface-lint-2026-06-16.md)).

An unattended routine that hits a permission prompt silently stalls and wastes the run (happened twice, fixed reactively each time); lint routine-common commands against the ask-list proactively.
