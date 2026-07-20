# Session — PROPOSAL 227 (Hex never-a-draw → VERDICT 240)

> **Status:** `complete`
> Born-red HOLD: this card lands `in-progress` on the first commit to hold the PR red through the substrate-gate, and flips to `complete` as the deliberate last commit once the idea doc, outbox block, claim, and heartbeat are in place and the sim-lab verifier is verified. Merge is by the automated landing workflow on all-green.

## 💡 Session idea

Round-54 GAME slot. PROPOSAL 227: Hex is never a draw — for every complete two-colouring of the n×n board exactly one player connects (no-draw = Brouwer / topology; no-double-win = planarity). The transpose-and-colour-swap bijection then forces #{Red}=#{Blue}=2^(n²−1) exactly, so a uniform random fill gives P(first player connects)=1/2 EXACTLY — a size-independent rational that the first-mover's perfect-play advantage does not leak into. Paired verifier VERDICT 240 (offset +13).

## ⟲ Previous-session review

P226 (VENTURE, Myerson optimal reserve r*=1/2 → VERDICT 239) landed; its verdict block is the next verdict-mirror pending in the idea-engine outbox. The status heartbeat lagged the outbox by one VENTURE slot at boot (proposal/loop lines still read P225) — flagged for the coordinator; this slice does not touch `control/status.md`.

## 🫀 Heartbeat

Verifier `sims/verdict-240-hex-never-a-draw/hex-never-a-draw.py` (stdlib-only, SEED=20260717) verified green before flip: exit 0, four gates PASS each in its own direction, digest `76d9a3267140171bec9ad335b370c6028e1359d23f39c7c87f3d7125598ebed8` reproduced byte-identical across in-process double-run and a separate re-invocation (~40 s). G1 exhaustive-exact n∈{2,3,4} (draws==both==0, Red==Blue==2^(n²−1), Fraction==1/2); G2 MC n=11 z=−0.826; G3 never-draw invariant across 12 size×density cells + complement symmetry |z|<3; G4 square-lattice falsifiability z=−364.97 (square draws at q=0.526, hex draws 0). Grounding pins Wikipedia Hex oldid 1361476133; P=1/2 and the 2^(n²−1) count attributed as derived (theorem + topology quoted).

> **📊 Model:** Claude Opus · high · proposal-authoring / GAME slot

## Decisions made

- Chose Hex no-draw determinacy (distinct from covered game-theory slots and from the pie-rule/swap idea) for a clean exact-Fraction core with a genuine falsifiability contrast (square lattice draws).
- Exhaustive exact coverage capped at n=4 (n=5 = 2^25 colourings); n≥5 rests on the cited theorem + Monte-Carlo invariant gates.
- Idea link uses `blob/main/...` (the linter resolves the local path + state, not the remote SHA).

## Next session should know

- Round-54 rotation after this GAME slot: next is UNRELATED (P228 → V241).
- VERDICT 239 (Myerson) verdict block still needs mirroring into the idea-engine outbox; verifier already landed in sim-lab (#320).
- Idea-engine status heartbeat proposal/loop lines lagged the outbox by one slot at boot — coordinator to reconcile.
