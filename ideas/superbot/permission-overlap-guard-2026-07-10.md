# Permission-overlap guard for `.claude/settings.json` — link index

> **State:** historical(shipped 2026-06-21 in superbot as `scripts/check_permission_overlap.py`)
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/permission-overlap-guard-2026-06-21.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/permission-overlap-guard-2026-06-21.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/permission-overlap-guard-2026-06-21.md)).

A config lint flagging any permissions.allow rule fully contained in a broader ask/deny rule — a shadowed allow may never take effect depending on precedence semantics.
