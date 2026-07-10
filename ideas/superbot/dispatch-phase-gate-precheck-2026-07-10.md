# Dispatch-side phase-gate pre-check — don't fire agent-feature work orders in fix-phase — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/dispatch-phase-gate-precheck-2026-06-15.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/dispatch-phase-gate-precheck-2026-06-15.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/dispatch-phase-gate-precheck-2026-06-15.md)).

Check the phase gate on the DISPATCH side before firing agent-feature work orders: a feature order fired into fix-phase burns the run when the executor (correctly) refuses to build.
