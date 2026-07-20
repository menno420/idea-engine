# VERDICT 237 — Cayley's formula via the Prüfer bijection (adversarial re-verification of PROPOSAL 224)

> **Status:** complete

📊 Model: Opus 4.x · high · review/verify
updated: 2026-07-20T18:36:52Z

## 💡 Session idea
Independently re-verify PROPOSAL 224 (round-53 UNRELATED slot) — Cayley's formula: the number of labeled trees on the vertex set {1..n} is EXACTLY T(n)=n^(n-2) for n>=2, proven bijectively by the Prüfer sequence (labeled trees ↔ {1..n}^(n-2)), plus the uniform-random-labeled-tree consequences E[deg(v)]=2−2/n, P(specific edge {i,j})=2/n, P(v is a leaf)=((n−1)/n)^(n-2). Reproduce the sim-lab verifier byte-identical, confirm the full-64 results_sha256, evaluate all six gates each in its own direction, and rule → APPROVE if the digest matches and every gate passes.

## ⟲ Previous-session review
Prior slice ruled VERDICT 236 (grim-trigger folk-theorem threshold δ*=(T−R)/(T−P), round-53 GAME slot) APPROVE. Carry-forward is GATE-POLARITY discipline: read each gate in ITS OWN direction — exact identities are self-certifying (G1 brute union-find Cayley identity, G2 encode/decode bijection roundtrip + no-collision, G3 exact-Fraction consequences), Monte-Carlo z-tests are AGREEMENT gates when the closed form is the null (G4 n=12, G5 robustness sweep, all |z|<3), and deliberately-wrong models are FALSIFIABILITY gates read at the opposite polarity (G6 rejects P=1/2 and P=1/n). Also carried: the QUOTED-vs-DERIVED grounding discipline over which V235 was QUALIFIED — confirm the count is on-page (quoted) and the random-tree statistics are derived firsthand (off-page).

## Ruling: APPROVE

Independent adversarial re-verification of PROPOSAL 224 (round-53 UNRELATED slot). The labeled-tree count reproduces firsthand as the EXACT integer T(n)=n^(n-2) for n=2..6 (1,3,16,125,1296) and holds n=2..8; the Prüfer map is a genuine bijection (all 125 trees at n=5 roundtrip to themselves, 125 strings all 5^3 distinct, no collision); exact-Fraction consequences P(edge{1,2})=2/5, mean deg(1)=8/5, leaf prob=64/125.

- Verifier byte-identical to committed (diff exit 0; logic untouched).
- results_sha256 7e8dbff568cf62ab3e15ebdc1d9a7e893f024d10f4bd39b1630cbc444317ad1b reproduced full-64 EXACT, deterministic across an in-process double-run + a separate re-invocation (SEED=20260717, N_MC=200000).
- All six gates PASS each in its own direction; G6 rejects naive P=1/2 (z=−298.4) and P=1/n (z=+134.4) in the correct opposite polarity.
- Independent Matrix-Tree (Kirchhoff determinant) cross-check reproduces 1,3,16,125,1296 by a different method than the verifier.
- Grounding pin honest: Wikipedia "Cayley's formula" oldid 1293533452, raw wikitext sha1 910071d1648b9817de6852fa2d98e1e6b260e94a (4632 B) — count is QUOTED (on page), uniform-random-tree consequences are DERIVED firsthand (absent from page). P224 got the attribution discipline V235 was QUALIFIED over correct.
