# PROPOSAL 133 — fan-out tail amplification (round-31 FLEET slot)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card intentionally holds the PR red until the slice is complete and verified. It flips to `complete` last, after the heartbeat, releasing the landing workflow (born-red HOLD is the sole gate-red exception).

## Objective

Draft and land round-31 FLEET-slot PROPOSAL 133 — the fan-out tail amplification mechanism: a scatter-gather request that waits for all N independent leaves inherits slow-tail probability P_slow(N) = 1 - (1-p)^N, so a 1%-per-leaf tail makes the MEDIAN of a ~69-way fan-out slow (crossover N* = ln2 / (-ln(1-p)) ~= 0.693/p). Ship a committed stdlib verifier, three pre-registered >=3 sigma gates, and a disclosed results-dict sha256. VERDICT 146 (P133 -> V146, +13) is the next independent slice, not written here.
