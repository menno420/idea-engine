# Idea — an "audit-seam coverage" checker (catch unaudited mutations at authoring time) — link index

> **State:** historical(built advisory 2026-07-06 in superbot as `scripts/check_audit_seam.py`)
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/audit-seam-coverage-checker-2026-07-05.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/audit-seam-coverage-checker-2026-07-05.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/audit-seam-coverage-checker-2026-07-05.md)).

An authoring-time checker that catches code paths performing real mutations without reaching the audited seam (`emit_audit_action`) — the defect class behind four of the eight Stage-2 save fixes. Built warn-first with an allowlist and 19 unit tests.
