# Idea — `check_worker_pr_scope.py` (ultracode coordinator scope guard) — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/ultracode-worker-pr-scope-guard-2026-06-23.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/ultracode-worker-pr-scope-guard-2026-06-23.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/ultracode-worker-pr-scope-guard-2026-06-23.md)).

Mechanize the ultracode coordinator's by-hand safety check: a check_worker_pr_scope guard asserting each worker PR's diff stays inside its unit's declared ALLOWED globs (file-disjointness).
