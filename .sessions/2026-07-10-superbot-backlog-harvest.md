# Session — harvest slice: superbot docs/ideas/ backlog indexed by link into ideas/superbot/

> **Status:** `in-progress`
> **Model/time:** fable-5 · 2026-07-10 (worker slice, dispatched by the coordinator under
> continuous-chaining mode; fifth shipped slice of the repo)

## What this session is doing

Harvesting `menno420/superbot` → `docs/ideas/` (the canonical backlog) into
`ideas/superbot/` **by link** per README § Idea file grammar — one link-index entry per
canonical doc (pinned sha), a one-paragraph gist, state `captured` unless the canonical
doc records a further outcome (built/rejected → mirrored). No probing, no copying —
superbot's backlog stays canonical where it is.
