# Context-cost telemetry — measure real per-session reads, not modeled ones — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/context-cost-telemetry-2026-07-02.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/context-cost-telemetry-2026-07-02.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/context-cost-telemetry-2026-07-02.md)).

The retention simulator's read-cost constants are modeled, not observed; add telemetry measuring real per-session reads (greps, skim words, boot-route words) so retention policy rests on data.
