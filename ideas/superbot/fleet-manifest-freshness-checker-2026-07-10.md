# Fleet-manifest freshness checker (2026-07-10) — link index

> **State:** historical(implemented in superbot PR #1923, 2026-07-10)
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/fleet-manifest-freshness-checker-2026-07-10.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/fleet-manifest-freshness-checker-2026-07-10.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/fleet-manifest-freshness-checker-2026-07-10.md)).

A checker comparing each fleet-manifest row's last-seen cell against the lane repo's live `control/status.md` heartbeat, turning the manifest from hand-maintained prose into a verified dashboard.
