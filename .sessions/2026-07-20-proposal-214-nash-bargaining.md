# Session — PROPOSAL 214: Nash bargaining threat-point half pass-through

> **Status:** complete

## 💡 Session idea
Round-51 VENTURE slot (P214 → VERDICT 227, +13 offset). Head: improving your walk-away option (BATNA) by a dollar moves your symmetric Nash bargaining share by exactly fifty cents — ∂x₁/∂d₁ = ½ — because the surplus the two parties split shrinks by the same dollar and each carries half. Folk "one-for-one leverage" over-counts.

## ⟲ Previous-session review
- Boot: idea-engine @ e6934f4 (post ORDER 019), sim-lab @ 3dc5861 (VERDICT 225); hard-synced both to origin/main.
- Proposal high-water taken: P213 → advancing to P214 (union-max). Open pulls below the line: V226(P213), V225(P212), V137(P124), V132(P119), round-26 FLEET P113→V126.
- Dedup: grepped all ideas/** lanes. Nash bargaining has zero prior docs. Kelly, gambler's-ruin, and double-marginalization (partner-channel-margin-stacking) are TAKEN and avoided; lemons adverse-selection and independent-screens are adjacent info-econ docs, distinguished in the caveats. No pivot needed.
- Round-51 rotation: FLEET (P213) → VENTURE (this) → game → unrelated.

## Decisions made
- Verifier: stdlib-only, SEED=20260717, four gates. G1 exact (closed form == exhaustive Nash-product enumeration, Fraction); G2 SURPRISE (alternating-offers MC rejects folk full-pass-through at ≥3σ, consistent with ½); G3 robustness (pass-through = 1−α across the α-shift, strictly in (0,1)); G4 exact conservation + IR with a falsifiability leg that rejects the folk accounting.
- Grounding: Wikipedia "Cooperative bargaining" (external), pinned oldid + wikitext sha1; caveat scoped to what the page states (solution concept + axioms) vs the pass-through identity proven firsthand.
- Born-red HOLD on commit 1 (this card in-progress); flip complete last, land on merge-on-green only. Zero manual/agent merge calls.

## Next session should know
- P214 → V227 open pull once landed.
- Disclosed results_sha256: 47e09254b86486e2cdff63e54ec8a276287f4f00806cf32e0fb52daa5cb4f434.
- Round-51 rotation now open at: game slot next (after this VENTURE).

> 📊 Model: Claude Opus · high · idea/planning
