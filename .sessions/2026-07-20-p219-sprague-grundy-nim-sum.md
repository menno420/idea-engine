# Session 2026-07-20 — PROPOSAL 219 Sprague–Grundy / nim-sum zero criterion (round-52 GAME slot)

> **Status:** `complete`

## 💡 Session idea
Nim / Sprague–Grundy: a disjunctive-sum position is a loss for the player to move (a P-position) iff the nim-sum (XOR) of its component Grundy values is zero. Two exact corollaries carry it — the `Sub({1..k})` Grundy closed form `G(n)=n mod (k+1)`, and the exact Nim P-density `1/2^b` (exactly `1/8` for 3 heaps over `{0..7}`). Six SEED=20260717 gates (exact-Fraction, MC |z|<3, Sprague–Grundy-sum, robustness, falsifiability) all PASS; disclosed results-dict sha256 = `e50e461d105e4984f6f562def0eba3f527ef4030512f9cf75294ddd6709002b7`.

## ⟲ Previous-session review
Round-52 rotation: FLEET P217 (consistent-hashing max-gap = H_n/n) → V230 landed; this opens the GAME slot as P219 (P218 VENTURE not yet authored; proposal high-water was P217). DEDUP: grepped all lanes (`nim|sprague|grundy|pursuit|minimax|zero-sum|penney|efron|banzhaf|shapley|condorcet|stackelberg|vickrey|auction|nash|bargaining|correlated|chicken|blotto|parity`) across fleet, superbot-games, venture-lab, etc. Prior game-theory cards: Penney, Efron dice, correlated equilibrium, Stackelberg, Vickrey, Banzhaf/Shapley power, Blotto, all-pay, Nash bargaining, Condorcet, Braess, PoA, volunteer's dilemma, winner's curse, Gale-Shapley. No nim / Sprague–Grundy / subtraction-game Grundy card exists → distinct. High-water advance P217 → P219.

## 🫀 Heartbeat
Left to the coordinator per the single-writer rule (control/status.md is coordinator-owned; not touched here). Claim bundled into commit 1: control/claims/claude-p219-sprague-grundy-nim-sum.md.

> 📊 Model: Claude Opus · high · idea/planning

## Decisions made
- Head: Sprague–Grundy nim-sum zero criterion + `Sub({1..k})` Grundy closed form `G(n)=n mod (k+1)`. Chosen because it is exactly true, reproducible stdlib-only, and un-built (no prior nim/Grundy card in any lane).
- 6 pre-registered gates: G1 MC 3-heap P-density ≈ 1/8 (|z|<3, z=1.446904); G2 exhaustive density == Fraction(1,8) (64/512); G3 `G(n)==n mod 4` on [0,256] zero-mismatch; G4 disjunctive-sum `G==G(a)⊕G(b)` on [0,40]² zero-mismatch; G5 `G(n)==n mod (k+1)` for k∈{2,3,4,5}; G6 naive total-parity rejected at |z|>3 (z=-334.45).

## Next session should know
P219 → VERDICT 232 (+13 offset). Next slice: P218 opens round-52 VENTURE slot (still unauthored), then P220 UNRELATED. Grounding pins Nim oldid 1362772636 + Sprague–Grundy theorem oldid 1362556548; caveat scoped: the XOR/nim-sum criterion and mex/Grundy framework are on those revisions, but `G(n)=n mod (k+1)` as a closed-form equation is verifier-established firsthand, not on Wikipedia.
