# Session — single-pass probe: superbot pil-card-render-contract-guard

> **Status:** `in-progress`
> **Model/time:** fable-5 · 2026-07-12 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session is doing

Single-pass probe (battery v0) of
`ideas/superbot/pil-card-render-contract-guard-2026-07-10.md` — TOP-5 #2 on the
fourth ledger (`control/status.md` @ `42f9642`): one cross-cutting test that
forces the PIL import to fail and asserts every card renderer in the family
returns `None` instead of raising, replacing per-module bespoke scaffolding.
Timing rationale under verification at live superbot HEAD: the pending
leaderboard-row-avatars routing (pins S `d647b2e`, this repo's PR #204 probe) is
about to grow the card-render family via `render_leaderboard_image`.

**Section-collision flag (dispatch boundary — no claim file):** this slice is
barred from `control/`, so no `control/claims/` entry exists; this born-red
first commit carries the `ideas/superbot/` collision flag instead, per the
PR #222/#225/#226 workflow convention.
