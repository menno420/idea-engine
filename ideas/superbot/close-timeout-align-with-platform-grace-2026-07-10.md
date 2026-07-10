# Idea — align the lifecycle close-timeout with the platform's kill-grace (defense-in-depth) — link index

> **State:** captured
> **Class:** product · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/close-timeout-align-with-platform-grace-2026-06-16.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/close-timeout-align-with-platform-grace-2026-06-16.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/close-timeout-align-with-platform-grace-2026-06-16.md)).

Defense-in-depth follow-up to the deploy-downtime fix (superbot PR #948): align the bot lifecycle's close timeout with the platform's kill-grace window so a slow shutdown can never outlive its host.
