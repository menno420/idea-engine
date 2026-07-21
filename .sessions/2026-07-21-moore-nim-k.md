# PROPOSAL 259 — Moore's Nim (Nim_k): P-positions ⇔ every binary column-sum ≡ 0 (mod k+1)

> **Status:** complete

> **📊 Model:** Claude Opus · high · idea/planning
started: 2026-07-21T14:53:38Z

💓 Heartbeat:
- round/slot: round-70 GAME slot · combinatorial game / Sprague–Grundy · Moore's Nim (Nim_k) closed form
- lane: P259 → V272 (+13 offset)
- branch: claude/proposal-259-moore-nim-k
- verifier: ideas/superbot-games/verify_259_moore_nim_k.py (stdlib only: argparse, functools, hashlib, itertools, json, math, random, sys, fractions)
- claim: Moore's Nim (Nim_k), normal play (last to move wins). A move selects between 1 and k heaps inclusive and removes a positive number of tokens from EACH selected heap. Write each heap in binary; for each bit-position j let c_j = Σ_i bit_j(a_i). The position is a P-position (player to move loses) IFF c_j ≡ 0 (mod k+1) for every j. For k=1 the modulus is 2, collapsing to ordinary Nim (nim-sum XOR == 0).
- SEED: 20260717 · results_sha256: da147d54d970d71754baa2994189c9e5f73cfbbf1ad36c7b2366f9ddf870402d
- determinism: in-process double-run IDENTICAL · --selfcheck byte-identical · separate re-invocation byte-identical
- G1 EXACT (exhaustive, integer/XOR, 0 tolerance) — for k ∈ {1,2,3} enumerate ALL positions with m heaps (m=1..4) and each heap in [0,H) (k=1:H=8, k=2:H=6, k=3:H=5); assert moore_predicate == (outcome_oracle is P) for EVERY position. positions_checked=7014, mismatches=0 · pass
- G2 MC agreement (|z|<3) — (k,m,b)=(2,5,6), heaps uniform in [0,2^6); independent exact P-fraction f = (11/32)^6 = 1771561/1073741824 ≈ 0.001650; N=200000 iid positions give p̂=0.001765, z=1.268354 · pass
- G3 invariance/robustness (0 violations) — (a) k=1 collapse: moore_predicate(heaps,1) == (XOR==0) exhaustively (0 violations); (b) permutation + zero-pad invariance of BOTH moore_predicate and outcome_oracle over 400 random positions (0 violations) · pass
- G4 falsifiability (reject at |z|>3) — ordinary-Nim (mod 2) foil applied to k=2 misclassifies at ê=0.345800 vs the true oracle, z_foil=51.409363; the true theorem predicate makes theorem_errors=0 on the same N=5000 sample · pass
- all_pass: true · first_failing_gate: null · decision: PASS

✅ Flip note (born-red → complete): this card committed FIRST with Status: in-progress to hold the PR red behind the substrate-gate born-red HOLD; it flips to complete as the deliberate LAST commit, after the idea doc (ideas/superbot-games/moore-nim-k-2026-07-21.md), the verifier (ideas/superbot-games/verify_259_moore_nim_k.py), the ## PROPOSAL 259 outbox block, the Nim oldid 1362772636 grounding pin, the full-64 digest da147d54d970d71754baa2994189c9e5f73cfbbf1ad36c7b2366f9ddf870402d, and all four gates landed. The flip clears the born-red HOLD and releases native squash auto-merge.

## What this proposal does
Adds a superbot-games PROPOSAL establishing the exact P-position closed form for **Moore's Nim (Nim_k)** under normal play. A position is a multiset of heap sizes (a_1,…,a_m); a move selects between **1 and k** heaps inclusive and removes a **positive** number of tokens from **each** selected heap. Moore's theorem: writing every heap in binary and letting c_j be the column-sum of bit j across all heaps, the position is a **P-position IFF c_j ≡ 0 (mod k+1) for every j**. For k=1 the modulus is 2, so the criterion becomes "every binary column-sum is even" — the nim-sum (XOR) is 0 — exactly ordinary Nim (Bouton). Ships a stdlib-only firsthand verifier that proves the theorem against an INDEPENDENT memoized outcome oracle (P/N recursion that does not assume the theorem) through four gates.

## Method
Ground-truth game engine first, closed-form predicate second, then the two are forced to agree. `outcome_oracle(heaps,k)` is a memoized recursion over sorted-tuple canonical states: terminal (all zero) is a P-position; a position is N iff some legal move (choose 1..k nonzero heaps, drop each chosen heap to any strictly-smaller value) reaches a P-position, else P. `moore_predicate(heaps,k)` independently checks that every binary column-sum is ≡ 0 (mod k+1). G1 exhaustively enumerates every position (k∈{1,2,3}, m≤4, small H) and asserts theorem ⇔ true outcome with 0 mismatches. G2 draws N=200000 iid positions and compares the empirical P-fraction to the independently-derived exact f=(11/32)^6. G3 checks the k=1 collapse to XOR==0 exhaustively plus permutation/zero-pad invariance of both the predicate and the oracle. G4 rejects the ordinary-Nim (mod 2) foil applied to k=2 at z_foil=51.41 while the true predicate scores 0 errors on the same sample.

## ⟲ Previous-session review
PROPOSAL 255 (Mock Turtles / coin-turning odious closed form, → V268) landed with the born-red + four-gate + full-64-digest choreography; this slice reuses that contract exactly and extends the shipped combinatorial-game set into **Moore's Nim (Nim_k)** — the multi-heap generalisation where up to k heaps are touched per move and the P-criterion generalises the nim-sum from mod 2 to mod (k+1). Distinct from the shipped game heads: Mock Turtles / coin-turning (P255), Green Hackenbush = Nim / colon principle (P247), Wythoff (P239), Fibonacci-nim / Zeckendorf (P243), the subtraction game (P219, g=n mod 4). `moore` / `index-k` / `nim_k` is grep-0 across both repos.

## 💡 Session idea
Next untaken combinatorial-game atoms surfaced in dedup: (a) Moore's Nim **misère** play (the terminal-adjustment variant, take k objects from one heap when all heaps reduce to zero mod k+1); (b) the per-heap bounded-removal variant (remove at most r from each chosen heap → reduce heaps mod r+1 first, then apply the mod-(k+1) column rule); (c) Wythoff-style two-pile golden-ratio P-positions as a paired head. All grep-checked today.
