# Session 2026-07-20 — PROPOSAL 224 Cayley's formula via the Prüfer bijection: labeled trees on n vertices = n^(n-2) (round-53 UNRELATED slot)

> **Status:** `complete`

## 💡 Session idea
Cayley's formula: the number of labeled trees on the vertex set `{1..n}` is EXACTLY `n^(n-2)` for `n>=2`, proven bijectively by the Prüfer sequence — a bijection between labeled trees and strings `{1..n}^(n-2)`, so `|trees| = |{1..n}^(n-2)| = n^(n-2)`. Consequences for a uniformly random labeled tree fall straight out of the Prüfer encoding: `E[deg(v)] = 2 − 2/n`, `P(specific edge {i,j}) = 2/n`, `P(v is a leaf) = ((n−1)/n)^(n-2)`. Six SEED=20260717 gates (exact union-find identity, exact bijection roundtrip, exact `Fraction` probabilities, Monte-Carlo agreement `|z|<3`, robustness, and falsifiability rejecting naive alternatives) all PASS; disclosed results-dict sha256 = `7e8dbff568cf62ab3e15ebdc1d9a7e893f024d10f4bd39b1630cbc444317ad1b`. Round-53 UNRELATED slot; pairs with VERDICT 237 (+13). The paired verifier is ALREADY MERGED in sim-lab (PR #318).

## ⟲ Previous-session review
Round-53 rotation closed its FLEET/VENTURE/GAME legs: P221 (reservoir sampling) → V234, P222 (revenue equivalence) → V235, P223 (grim-trigger folk-theorem) → V236 all landed. This opens the round-53 UNRELATED slot as P224. DEDUP: grepped all lanes (`cayley|prüfer|prufer|labeled.tree|labelled.tree|spanning.tree|tree.count|n\^\{n-2\}|forest`) across fleet, superbot-games, venture-lab. Prior pure-math combinatorics cards in fleet: birthday-collision, coupon-collector, kaprekar, penney, secretary, hundred-prisoners, hat-check, Pólya-urn, random-walk-recurrence. No Cayley / Prüfer / labeled-tree-count card exists in any lane → distinct. Proposal high-water advances P223 → P224.

## 🫀 Heartbeat
Left to the coordinator per the single-writer rule (control/status.md is coordinator-owned; not touched here). Claim bundled into commit 1: control/claims/2026-07-20-p224-cayley-prufer.md. Born-red: this card opens `in-progress` to hold the substrate-gate RED through the idea-card + outbox-block commits, and is flipped `complete` as the deliberate LAST commit (the only RED across the build is the intended HOLD; `python3 bootstrap.py check --strict` exits 0 on the flipped tree).

> **📊 Model:** agent · high · idea/planning

## Decisions made
- Head: Cayley's formula `#{labeled trees on {1..n}} = n^(n-2)` for `n>=2`, proven bijectively via the Prüfer sequence (labeled trees ↔ `{1..n}^(n-2)`). Chosen because it is exactly true, reproducible stdlib-only (union-find brute count + Prüfer encode/decode + exact `Fraction` probabilities), and un-built (no prior labeled-tree-count / Prüfer card in any lane).
- 6 pre-registered gates: G1 exact Cayley identity (brute union-find tree counts `n=2..6` = `1,3,16,125,1296` = `n^(n-2)`); G2 exact bijection roundtrip (all 125 trees at `n=5` roundtrip; the 125 Prüfer sequences are all `5^3` distinct — no collision); G3 exact `Fraction` probs at `n=5` (`P(edge{1,2})=2/5`, mean `deg(1)=8/5`, leaf prob `64/125`); G4 MC agreement at `n=12` (|z|<3): `z_edge=−0.35`, `z_deg=0.809`; G5 robustness (identity `n=2..8` all match; edge-prob MC at `n=6/10/20` all |z|<3); G6 falsifiability (counts uniquely `≠ n^(n-1)/(n-1)!/2^(n-1)`; naive `P=1/2` rejected `z=−298.4`, naive `P=1/n` rejected `z=+134.4`).
- Grounding pinned to Wikipedia "Cayley's formula" oldid 1293533452 (raw-wikitext sha1 910071d1648b9817de6852fa2d98e1e6b260e94a; local `sha1sum` = MediaWiki API rev sha1, MATCH); caveat scoped: the page states the identity `n^(n-2)` verbatim and names the Prüfer-sequence proof, but does NOT state the uniform-random-tree consequences (`E[deg]=2−2/n`, `P(edge)=2/n`, leaf prob) — those are verifier-established firsthand.

## Next session should know
P224 → VERDICT 237 (+13 offset). Paired verifier already merged in sim-lab: `sims/verdict-237-cayley-prufer/cayley-prufer.py` (PR #318). Round-53 rotation now complete (FLEET P221→V234, VENTURE P222→V235, GAME P223→V236, UNRELATED P224→V237). Ledger contiguous through P224; proposal high-water P224.
