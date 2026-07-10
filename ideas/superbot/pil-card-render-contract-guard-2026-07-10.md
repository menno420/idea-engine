# Idea: a shared `bytes | None` lazy-PIL contract guard for the card-render family — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/pil-card-render-contract-guard-2026-06-22.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/pil-card-render-contract-guard-2026-06-22.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/pil-card-render-contract-guard-2026-06-22.md)).

A shared bytes|None lazy-PIL contract guard for the card-render family so every renderer honors the same 'return None when PIL is unavailable' contract without bespoke per-test scaffolding.
