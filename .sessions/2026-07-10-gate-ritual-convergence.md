# Session — fleet slice: gate↔ritual convergence (substrate-gate runs preflight.py)

> **Status:** `in-progress`
> **Model/time:** 2026-07-10 ~21:00Z (worker slice; idea origin: PR #16 session card 💡,
> `.sessions/2026-07-10-preflight-wrapper.md` @ `68c3d2a` — "Gate↔ritual convergence")

## What this session is doing

- Claim `ideas/fleet/` + the gate workflow (`claims/slice-gate-ritual-convergence.md`,
  flat filename per `claims/README.md`; cleared at close).
- Capture + probe (battery v0) the gate↔ritual convergence candidate →
  `ideas/fleet/gate-ritual-convergence-2026-07-10.md`.
- If the verdict is built-here: point `substrate-gate.yml`'s non-control lane at
  `python3 scripts/preflight.py` so CI and the wake ritual share ONE check list.
- This PR is its own live-fire test: the reworked gate must run green on this PR's
  own `pull_request` event before merge.
- NO outbox entry, no new proposal — backpressure holds (depth 3, zero sim-lab pulls).
