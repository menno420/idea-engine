# Idea — `check_workflow_gh_permissions`: a workflow's `permissions:` must cover the `gh` ops it runs — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/workflow-gh-permission-coverage-checker-2026-07-06.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/workflow-gh-permission-coverage-checker-2026-07-06.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/workflow-gh-permission-coverage-checker-2026-07-06.md)).

A checker asserting each workflow's permissions: block actually covers the gh operations its scripts run — under the GITHUB_TOKEN fallback an uncovered call silently no-ops.
