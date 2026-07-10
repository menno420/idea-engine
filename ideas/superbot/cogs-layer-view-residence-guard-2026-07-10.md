# Idea — a guard for `discord.ui.View` subclasses mislayered in `cogs/` — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/cogs-layer-view-residence-guard-2026-06-14.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/cogs-layer-view-residence-guard-2026-06-14.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/cogs-layer-view-residence-guard-2026-06-14.md)).

A guard for discord.ui.View subclasses mislayered in cogs/ files — the baseview-conformance ratchet only scans views/, so a View defined in a cog is invisible to it. Partially built: the direct-View half shipped (superbot PR #1163); the residence half remains.
