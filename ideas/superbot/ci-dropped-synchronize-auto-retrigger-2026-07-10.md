# Idea: auto-re-trigger Code Quality when GitHub drops the `pull_request: synchronize` event — link index

> **State:** historical(promoted and built same day in superbot PR #1288)
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/ci-dropped-synchronize-auto-retrigger-2026-06-22.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/ci-dropped-synchronize-auto-retrigger-2026-06-22.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/ci-dropped-synchronize-auto-retrigger-2026-06-22.md)).

GitHub can drop the `pull_request: synchronize` event delivery itself, leaving a PR head with zero required-check runs and auto-merge jammed; auto-detect and re-trigger the run.
