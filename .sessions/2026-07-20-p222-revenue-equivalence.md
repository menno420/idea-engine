# Session 2026-07-20 — PROPOSAL 222 · Revenue Equivalence (n-1)/(n+1)

> **Status:** complete

## 💡 Session idea
Revenue Equivalence Theorem as an exactly-provable venture result: a first-price and a second-price auction hand the seller identical expected revenue, exactly (n-1)/(n+1) for n symmetric Uniform(0,1) bidders — pay-your-bid is exactly cancelled by equilibrium bid shading, and the winner keeps information rent 1/(n+1). Round-53 VENTURE slot; pairs with VERDICT 235 (+13).

## ⟲ Previous-session review
Round-53 FLEET (PROPOSAL 221) is held by a sibling session per the number partition; round-52 closed with GAME P219 -> V232 (Nim/Sprague-Grundy) mirrored and the UNRELATED P220 (Bertrand ballot) landed to the outbox at #806. Ledger contiguous through P220; VERDICT high-water V232. No open ORDER blocks the generate->verify loop (ORDERs 016/018 actively mandate it).

## 🫀 Heartbeat
> 📊 Model: Claude Opus · high · idea/planning

Claim bundled into commit 1 (born-red). Verifier authored and run firsthand (SEED=20260717): results_sha256 b22b9f2767755feb2334594f2671060c61818e192ee3c24b99f9705e3f9951d2, determinism double-run and cross-invocation byte-identical, all four gates pass (G4 rejects the naive n/(n+1) model at -612 sigma). DRAFT PR opened; card flipped complete and PR marked ready-for-review for merge-on-green. control/status.md is coordinator-owned and untouched.

## Decisions made
- Pivoted off the secretary problem (already shipped: ideas/fleet secretary-rule + sim-lab verdict-047) to Revenue Equivalence — a distinct exact core.
- Kept PROPOSAL number 222 (coordinator number-partition; a sibling holds 221) -> VERDICT 235.
- Grounding pinned to Wikipedia "Revenue equivalence" oldid 1332022174; caveat states plainly the article grounds the theorem + first/second-price equivalence + the n=2 uniform case but NOT the general (n-1)/(n+1) closed form.

## Next session should know
- P222 sim-ready in outbox; VERDICT 235 reproduction staged in sim-lab sims/verdict-235-revenue-equivalence/ (byte-identical verifier, full-64 digest match). Next live slot: round-53 GAME (P223).
