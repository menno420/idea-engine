# Idea — `check_loop_health.py` should fall back when `gh` is unavailable — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/loop-health-gh-unavailable-fallback-2026-06-19.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/loop-health-gh-unavailable-fallback-2026-06-19.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/loop-health-gh-unavailable-fallback-2026-06-19.md)).

check_loop_health.py assumes `gh` is installed/authenticated, but the in-container reconciliation environment lacks it; add a graceful fallback. Promoted to a plan in superbot (band-#1170 pass) but not recorded built in the doc.
