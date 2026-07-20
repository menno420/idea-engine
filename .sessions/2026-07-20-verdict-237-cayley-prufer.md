# VERDICT 237 — Cayley's formula via the Prüfer bijection (adversarial re-verification of PROPOSAL 224)

> **Status:** in-progress

📊 Model: Opus 4.x · effort high · task-class verification/verdict
updated: 2026-07-20T18:36:52Z

## Ruling: APPROVE

Independent adversarial re-verification of PROPOSAL 224 (round-53 UNRELATED slot). The labeled-tree count reproduces firsthand as the EXACT integer T(n)=n^(n-2) for n=2..6 (1,3,16,125,1296) and holds n=2..8; the Prüfer map is a genuine bijection (all 125 trees at n=5 roundtrip to themselves, 125 strings all 5^3 distinct, no collision); exact-Fraction consequences P(edge{1,2})=2/5, mean deg(1)=8/5, leaf prob=64/125.

- Verifier byte-identical to committed (diff exit 0; logic untouched).
- results_sha256 7e8dbff568cf62ab3e15ebdc1d9a7e893f024d10f4bd39b1630cbc444317ad1b reproduced full-64 EXACT, deterministic across an in-process double-run + a separate re-invocation (SEED=20260717, N_MC=200000).
- All six gates PASS each in its own direction; G6 rejects naive P=1/2 (z=−298.4) and P=1/n (z=+134.4) in the correct opposite polarity.
- Independent Matrix-Tree (Kirchhoff determinant) cross-check reproduces 1,3,16,125,1296 by a different method than the verifier.
- Grounding pin honest: Wikipedia "Cayley's formula" oldid 1293533452, raw wikitext sha1 910071d1648b9817de6852fa2d98e1e6b260e94a (4632 B) — count is QUOTED (on page), uniform-random-tree consequences are DERIVED firsthand (absent from page). P224 got the attribution discipline V235 was QUALIFIED over correct.
