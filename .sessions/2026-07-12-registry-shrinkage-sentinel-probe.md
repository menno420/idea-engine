# Session — single-pass probe: superbot-next registry-shrinkage-sentinel-fixture

> **Status:** `in-progress`

- **📊 Model:** fable-5 · worker slice (dispatched by the coordinator under
  continuous-chaining mode per Q-0265) · single-pass probe

## What this session is doing

Single-pass probe (battery v0) of
`ideas/superbot-next/registry-shrinkage-sentinel-fixture-2026-07-12.md` — the
2026-07-12 harvest's first head from the superbot-next sweep @ `80464ab`:
one autouse conftest fixture snapshotting `ref_inventory()` +
`provider_names()` at test-directory boundaries and asserting no shrinkage,
sourced from the lane's canonical-order flake-fix card ("the world a suite
finds is the world it leaves").

**Section-collision flag (dispatch boundary — no claim file):** this slice is
barred from `control/`, so no `control/claims/` entry exists; this card's
born-red first commit carries the `ideas/superbot-next/` collision flag per
the PR #222/#225/#226/#228 workflow convention.

## Close-out

*(pending — flips with the complete badge)*
