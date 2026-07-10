# Idea — reconciliation cadence-boundary jitter guard — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/recon-cadence-boundary-jitter-2026-06-24.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/recon-cadence-boundary-jitter-2026-06-24.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/recon-cadence-boundary-jitter-2026-06-24.md)).

A guard against reconciliation cadence-boundary jitter: a pass fired ~50 minutes after the previous one on a 4-merge band because the marker reset landed right before a cadence boundary.
