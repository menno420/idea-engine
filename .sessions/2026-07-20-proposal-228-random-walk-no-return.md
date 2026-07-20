# Session — PROPOSAL 228 (random-walk no-return → VERDICT 241)

> **Status:** `complete`
> Born-red HOLD: this card lands `in-progress` on the first commit to hold the PR red through the substrate-gate, and flips to `complete` as the deliberate last commit once the idea doc, outbox block, and claim are in place and the sim-lab verifier is verified. Merge is by the automated landing workflow on all-green.

## 💡 Session idea

Round-54 UNRELATED slot. PROPOSAL 228: Feller's no-return identity for the simple symmetric ±1 random walk on Z from 0 — the probability the walk AVOIDS the origin throughout the first 2n steps equals the probability it is AT the origin at time 2n, both exactly u_{2n}=C(2n,n)/4ⁿ. Equivalently, over all 2^{2n} equally-likely sign sequences #{S_{2n}=0}=#{never revisit 0 in 1..2n}=C(2n,n) EXACTLY — two opposite-sounding events that are equinumerous path-for-path. Paired verifier VERDICT 241 (offset +13; sim-lab PR #325).

## ⟲ Previous-session review

P227 (GAME, Hex never-a-draw → VERDICT 240) landed; its verdict block is already mirrored in the idea-engine outbox (VERDICT 240 · ruled). Round-54 rotation advances GAME → UNRELATED for this slice. This slice does not touch `control/status.md` (coordinator-owned); the proposal high-water advances P227 → P228.

## 🫀 Heartbeat

Verifier `sims/verdict-241-random-walk-no-return/random-walk-no-return.py` (stdlib-only, SEED=20260717) verified green before flip: exit 0, four gates PASS each in its own direction, digest `75f5b3c166916598983389896cc762c906b1ef346c70f8b5c639b3a60e140f46` reproduced byte-identical across an in-process double-run and a separate re-invocation. G1 exhaustive-exact n∈{1,2,3,4,5,6} (A=#{S_{2n}=0}==B=#{never touch 0}==C(2n,n)={2,6,20,70,252,924}, Fraction(A,4ⁿ)==Fraction(B,4ⁿ)==u_{2n}); G2 MC n=12 N=200000 vs shared u_24≈0.16118026, z_return=+0.954447 / z_noreturn=−2.657831 both |z|<3; G3 p̂_noreturn==u_{2n} across n∈{5,8,12,20} (z_noreturn∈{+0.398,−0.833,−1.679,−1.182}) + left/right symmetry (z∈{−1.529,+1.503,−0.902,+0.250}) all |z|<3; G4 falsifiability rejects the (1/2)ⁿ independence fallacy (naive 1/4096≈0.000244 vs observed ≈0.161) at z_vs_naive=+4544.27 |z|>6. Grounding pins Wikipedia "Random walk" oldid 1359285496 (raw-wikitext sha1 bdcc6ea9…f9dd77); the 1-D recurrence and the general 2^{−n}C(n,(n+k)/2) point-mass formula are quoted, while the no-return identity, the u_{2n}=C(2n,n)/4ⁿ specialization, and the count identity are attributed as derived.

> **📊 Model:** Claude Opus · high · proposal-authoring / UNRELATED slot

## Decisions made

- Chose Feller's no-return=return identity (a clean exact-Fraction core over the complete path space) for the UNRELATED slot, distinct from the covered probability/random-walk cards (arcsine-lead-illusion, gamblers-ruin-edge-asymmetry, bertrand-ballot, birthday-collision).
- Exhaustive exact coverage capped at n=6 (2^{12}=4096 paths; n=7 is 2^{14}); n≥7 rests on the cited Feller theorem + the Monte-Carlo invariant gates.
- Grounding pinned to Wikipedia "Random walk" (recurrence + the general point-mass formula quoted); the u_{2n} return-probability specialization and the no-return identity flagged derived — the revision states neither as such. Guarded against the V235/V238 QUALIFIED "implied-quoted" seam by grepping the raw wikitext both ways.
- Idea link uses `blob/main/...` (the linter resolves the local path + state, not the remote SHA).

## Next session should know

- Round-54 rotation after this UNRELATED slot: next cycles back to FLEET (P229).
- Sim-lab verifier already merged (PROPOSAL 228 → VERDICT 241, +13 offset; PR #325 = f43bcbc); the VERDICT 241 verdict block is the next verdict-mirror pending in the idea-engine outbox (coordinator-owned routing).
- No edits made to `control/status.md`.
