# Idea — refactor RPS tournament orchestration out of the cog — link index

> **State:** captured
> **Class:** product · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/rps-tournament-service-refactor.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/rps-tournament-service-refactor.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/rps-tournament-service-refactor.md)).

Preserved refactor spec from owner-authored issue #229: move RPS tournament orchestration (state, brackets, payouts, recovery) out of the cog into a service so it's testable and restart-recoverable.
