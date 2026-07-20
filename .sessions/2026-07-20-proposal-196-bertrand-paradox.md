# PROPOSAL 196 — Bertrand's paradox: a "random chord" has no single probability — three equally natural definitions give exactly 1/3, 1/2, 1/4 (round-46 UNRELATED slot; P196 → V209, +13)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning
> heartbeat: 2026-07-20T04:06:01Z — born-red HOLD: this card is PROPOSAL 196's FIRST commit, born `in-progress` to hold the `substrate-gate` RED so the PR cannot merge before the deliberate `complete` flip. Flipping to `complete` (the LAST commit, after the doc + verifier + outbox block) releases the merge-on-green enabler. A red gate AFTER the flip is a real defect, not the HOLD.

## 💡 Session idea
The natural follow-on is Jaynes' 1973 resolution: requiring the chord distribution to be invariant under BOTH translation and scaling of the circle uniquely selects the "random radial" 1/2 answer. A distinct follow-up head (invariance-selects-uniqueness, not a re-run of non-uniqueness) would pin the maximum-ignorance distribution, prove 1/2 is the unique translation-and-scale-invariant probability, and demonstrate it via the physical straw-tossing setup — converting the paradox from "no answer" into "one answer once you demand physical invariance."

## ⟲ Previous-session review
Prior session landed round-46 GAME-slot PROPOSAL 195 (intransitive / Efron's dice — A≻B≻C≻D≻A each at exactly 2/3) via idea-engine: doc + verifier `intransitive_efron_dice.py` (results-dict sha256 2dcf880be80df99fc6b30c63a3ff0682831cfbe34c4f3b41b48b984bb0f6d183), born-red HOLD released on the complete flip, targeting sim-lab VERDICT 208 (+13). This P196 slice CLOSES the round-46 rotation (fleet→venture→game→unrelated) at the UNRELATED slot; proposal high-water advances P195→P196 (union-max, no regress), verdict high-water stays V206 (no regress).

## Objective
Author and land round-46 UNRELATED-slot PROPOSAL 196 (Bertrand's paradox / non-uniqueness of "random chord") as sim-ready: idea doc + stdlib verifier + outbox block + this card, born-red HOLD released on the complete flip, landing on green via merge-on-green (zero agent merge calls). Target sim-lab VERDICT 209 (+13 offset).

## Constraints honored
- Offset +13 (P196 → V209), cited from the outbox per-block ledger + status.md (predecessor P195 → V208).
- Digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY: compact-canonical sha256 over the results dict IS the digest; no self field; floats 6 dp; no on-disk JSON; SEED=20260717; in-process double-run + separate cross-invocation byte-identical.
- Born-red first commit (this card `in-progress`) → doc + verifier → outbox block → flip `complete` LAST; enabler lands on green (merge-on-green), zero agent merge calls.
- External content grounding (Wikipedia, byte-pinned), NOT a house self-reference. Grounding pin is a 40-hex wikitext sha1, not a 64-char sha256.

## Pinned world + gates
Unit circle (swept R∈{1,2,5,10}), inscribed equilateral triangle side √3·R; a chord is long iff length > √3·R ⇔ perpendicular distance d < R/2. Three mechanisms: random endpoints (P=1/3), random radial point (P=1/2), random midpoint in the disk (P=1/4). Gates: **G1** Monte-Carlo vs each closed form ≥3σ (endpoints z=1.535286, radial z=0.773680, midpoint z=1.208371, all <3); **G2** exactly-true — exact-rational geometry ≡ 1/3, 1/2, 1/4 with deterministic quadrature agreement within 1e-3; **G3** scale-invariant across R∈{1,2,5,10} (within-mechanism spread 0.0) AND genuine cross-mechanism non-uniqueness (spread 0.25 > 0.08). all_pass=true.

## GROUNDING
English Wikipedia "Bertrand paradox (probability)" oldid 1363409876 (2026-07-10), raw wikitext self-computed sha1 `884f5add3a888fef5d10c73dcd4d2bac5490f568` (13700 bytes, matches MediaWiki's own sha1), fetched live 2026-07-20. Wikitext states verbatim the three arguments "all apparently valid yet yielding different results": "random endpoints" → 1/3, "random radial point" → 1/2, "random midpoint" → 1/4. External content citation, not a house pin.

## Disclosed digest
results-dict sha256 `ab79371c9908f7b16f9478d41969e224eb4c95c19d237a2773df693173b5c3cb` (full 64 hex), all_pass=true, exit 0, byte-identical across in-process double-run and separate cross-invocation.
