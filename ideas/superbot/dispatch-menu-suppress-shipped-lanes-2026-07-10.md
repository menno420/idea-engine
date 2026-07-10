# Idea — let `dispatch_menu.py` suppress already-shipped lanes at the dispatch pick — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/dispatch-menu-suppress-shipped-lanes-2026-06-26.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/dispatch-menu-suppress-shipped-lanes-2026-06-26.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/dispatch-menu-suppress-shipped-lanes-2026-06-26.md)).

The dispatch pick has no guard against offering a roadmap lane whose linked plan already shipped — the freshness checker catches it only at session close; suppress shipped lanes at pick time.
