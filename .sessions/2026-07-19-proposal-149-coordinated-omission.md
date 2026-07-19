# PROPOSAL 149 — coordinated omission: closed-loop latency measurement is blind to the tail it is meant to catch

> **Status:** `in-progress`  — born-red HOLD, flips to complete last
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card is the session's FIRST content commit (alongside the claim) and is born `in-progress` to hold the `substrate-gate` RED so the PR cannot merge before the deliberate `complete` flip. Flipping to `complete` (the deliberate LAST commit, after the verifier + idea doc + outbox P149 block + heartbeat) releases the merge-on-green backstop. The flip is taken once the verifier is committed, the disclosed results-dict sha256 reproduces EXACTLY across a deterministic double-run, the PROPOSAL 149 outbox block + heartbeat are written, and `python3 bootstrap.py check --strict` is green apart from this born-red card HOLD itself. A red gate AFTER the flip is a real defect, not the HOLD.

## Objective

Draft and land round-35 FLEET-slot PROPOSAL 149 — coordinated omission: a closed-loop / synchronous load generator (one that waits for each request to return before issuing the next) cannot send the requests it was scheduled to send during a service stall, so it silently OMITS the backlog those coordinated requests would have measured. The measured latency distribution is therefore biased LOW — p99/p99.9 can be understated by orders of magnitude — because the measurement method, not the system under test, sets the observed tail. Ship a markdown-first card, a committed stdlib-only deterministic verifier (SEED=20260717, ≥3σ /se gates, disclosed results-dict sha256), a deterministic double-run, an outbox block (P149 → V162, +13), and a heartbeat update. VERDICT 162 (P149 → V162, +13) is the next independent slice, NOT authored here.

## Constraints honored

- Round-35 FLEET slot (rotation fleet→venture→game→unrelated; round-35 opens at the FLEET slot with P149). Offset +13 (P149 → V162) — the verdict is NOT authored here. [[fill: after verifier — cite offset authority from control/status.md + outbox depends-ledger]]
- Digest posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY (the P105…P148 family) with the P127+ TWIST (compact canonical hashed preimage, pretty indent=2 stdout dump, floats rounded 6 dp, no on-disk JSON). [[fill: after verifier]]
- Stdlib-only verifier (hashlib, json, math, random — no numpy/scipy); pinned SEED=20260717; /se z convention (z = mean/se); ordered ≥3σ gates. [[fill: after verifier — exact gate ladder]]
- Outbox `## PROPOSAL 149 · … · status: sim-ready` block appended once (append-only, deduped) matching the P145…P148 skeleton (target / idea / question / done-when / depends / loop). [[fill: after verifier]]
- Status heartbeat: proposal high-water P148 → P149 (union-max, no regress); verdict high-water kept (this is a PROPOSAL slice, no verdict authored); routines line UNCHANGED (coordinator-bound). [[fill: after verifier]]
- Born-red first commit (card in-progress + claim) → verifier + idea doc → outbox + status → flip complete LAST.

## GROUNDING

Round-35 FLEET-slot of the fleet/cross-cutting proposal→verdict pipeline. Pinned world: SEED=20260717, ≥3σ /se gates, disclosed results-dict sha256. [[fill: after verifier — pinned constants (N, R, arrival rate, stall model, thresholds), closed-form anchor, external reference on coordinated omission, grounding branch-point commit]]

## Probe questions

**1. Is the mechanism genuinely new against the fleet backlog?** [[fill: after verifier — collision-check against prior fleet/unrelated heads]]

**2. Do all pre-registered gates PASS in order on the /se margin?** [[fill: after verifier — gate-by-gate z values]]

**3. Does the digest reproduce EXACTLY and deterministically?** [[fill: after verifier — results-dict sha256 + double-run byte-identity]]

**4. Does the proposal advance the proposal high-water without regressing anything?** [[fill: after verifier — high-water P148 → P149, baton]]

## Outcome

[[fill: after verifier — pinned-world result, gate z values, digest, transferable rule]]

## ⟲ Previous-session review

[[fill: after verifier — P148 baton pickup + carry-forwards honored]]

## 💡 Session idea

[[fill: after verifier — next independent slice seed]]
