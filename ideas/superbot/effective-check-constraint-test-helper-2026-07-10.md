# Idea — a shared `effective_check_constraint(table, column)` test helper — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/effective-check-constraint-test-helper-2026-06-14.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/effective-check-constraint-test-helper-2026-06-14.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/effective-check-constraint-test-helper-2026-06-14.md)).

A shared effective_check_constraint(table, column) test helper: alignment tests hard-code one migration path each, so when a CHECK constraint is widened in a later migration the test silently reads the stale set.
