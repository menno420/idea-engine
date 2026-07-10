# A `check_plan_homing.py` guard — no active plan goes unrouted — link index

> **State:** historical(shipped 2026-06-20 in superbot PR #1174 as `scripts/check_plan_homing.py`)
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/plan-homing-guard-2026-06-19.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/plan-homing-guard-2026-06-19.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/plan-homing-guard-2026-06-19.md)).

No active plan goes unrouted: the dominant active thread (~8 plan docs) was reachable only by directory listing; the guard asserts every live plan is linked from a real agent route.
