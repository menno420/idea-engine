# PROPOSAL 150 — founder-dilution waterfall: a higher headline valuation with participating + a liquidation multiple pays founders LESS at exit

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card is the session's FIRST content commit (alongside the claim) and is born `in-progress` to hold the `substrate-gate` RED so the PR cannot merge before the deliberate `complete` flip. Flipping to `complete` (the deliberate LAST commit, after the verifier + idea doc + outbox P150 block + heartbeat) releases the merge-on-green backstop. A red gate AFTER the flip is a real defect, not the HOLD.

## Objective

Draft and land round-35 VENTURE-slot PROPOSAL 150 — the founder-dilution liquidation waterfall: between two term sheets raising the SAME amount for the SAME company, the one with the HIGHER headline pre-money valuation can leave founders with LESS money at exit across a strict MAJORITY of realistic outcomes, because it carries a PARTICIPATING preferred with a liquidation MULTIPLE whose participation drag dominates the founder-friendly effect of the lower investor ownership fraction the higher valuation buys — everywhere except the extreme upside tail. Ship a markdown-first card, a committed stdlib-only deterministic verifier (SEED=20260717, ≥3σ /se gates, disclosed results-dict sha256), a deterministic double-run, an outbox block (P150 → V163, +13), and a heartbeat update. VERDICT 163 (P150 → V163, +13) is the next independent slice, NOT authored here.

## Constraints honored

- Round-35 VENTURE slot (rotation fleet→venture→game→unrelated; round-35 opened at the FLEET slot with P149, this is the VENTURE slot P150). Offset +13 (P150 → V163) — the verdict is NOT authored here. Offset authority = this repo's control/outbox.md P150 depends-ledger + control/status.md.
- Digest posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY (the P105…P149 family) with the P127+ TWIST (compact canonical hashed preimage, pretty indent=2 stdout dump, floats rounded 6 dp, no on-disk JSON, in-process double-run byte-identity assertion).
- Stdlib-only verifier (hashlib, json, math, random); pinned SEED=20260717; /se z convention (z=mean/se); ordered ≥3σ gates G1 majority-inversion → G2 typical-outcome gap → G3 robustness.
- Outbox `## PROPOSAL 150 · … · status: sim-ready` block appended once (append-only, deduped).
- Status heartbeat: proposal high-water P149 → P150 (union-max, no regress); verdict high-water kept (this is a PROPOSAL slice, no verdict authored); routines line UNCHANGED (coordinator-bound).
- Born-red first commit (card in-progress + claim) → verifier + idea doc → outbox + status → flip complete LAST.
