# PROPOSAL 243 — Fibonacci nim (Whinihan's game): the player to move loses iff n is a Fibonacci number (1,2,3,5,8,13,21,…), and the optimal winning move is to remove the smallest Fibonacci summand of n's Zeckendorf representation — refuting the naive "multiples of 3" and "powers of two" losing-set guesses

> **Status:** complete

> **📊 Model:** Claude Opus · high · idea/planning
started: 2026-07-21T05:04:43Z

💓 Heartbeat:
- round/slot: superbot-games · combinatorial game theory — Fibonacci nim P-positions (closed-form Fibonacci + Zeckendorf strategy)
- lane: P243 → V256 (+13 offset)
- branch: claude/fibonacci-nim-zeckendorf
- verifier: ideas/superbot-games/verify_243_fibonacci_nim.py (stdlib only: json, hashlib, math, random, fractions)
- SEED: 20260717 · results_sha256: 344cdaa21a550c745184aaab00951db1063f522d3fe25544738299fdf8ee7dce
- determinism: in-process double-run IDENTICAL · separate re-invocation byte-identical
- G1 EXACT identity (integer arithmetic) — from-scratch game oracle win(n,cap) over n∈[1,800]: loses(n) iff n∈Fib, mismatches=0; constructive Zeckendorf strategy legal (s≤n−1) and leaves-P (win(n−s,min(2s,n−s))==False) for every winning n, zeckendorf_strategy_violations=0 · pass
- G2 MC agreement — p0=|Fib∩[1,800]|/800=14/800=7/400=0.0175; 200000 uniform ints in [1,800] classified via the DP; p_hat=0.01785, z=1.19370699368, |z|<3 [Z_GATE=3.0] · pass
- G3 invariance/robustness — (a) second horizon N2=1200 reproduces the P-set on [1,800] byte-identical, == Fibonacci prefix, invariance_discrepancies=0; (b) from every winning start our DP player beats a uniformly-random opponent, games_played=31440, optimal_player_losses=0 · pass
- G4 falsifiability — naive "P=multiples of 3" REJECTED at |z|=20.413966739 (274 disagreements/800); secondary "P=powers of two" REJECTED at |z|=4.29119123911 (18 disagreements/800); both |z|>3 · pass
- all_pass: true · first_failing_gate: null · decision: PASS

⏳ Flip note (born-red): this card opens Status: in-progress to hold the PR red behind the substrate-gate; it flips to complete as the deliberate LAST commit, after the idea doc, the verifier, the outbox PROPOSAL 243 block, the full-64 digest match, and all four gates land. The flip clears the born-red HOLD and releases the landing workflow.

## What this proposal does
Adds a superbot-games PROPOSAL establishing the exact closed-form outcome of Fibonacci nim (Whinihan 1963): one pile of n tokens, the first move takes 1..n−1, every later move takes 1..2·(opponent's last take) capped at the tokens left, last token wins. The player to move LOSES (P-position) iff n is a Fibonacci number, and the optimal winning move from any non-Fibonacci n is to remove the smallest Fibonacci summand of n's Zeckendorf representation (which is always legal and always leaves the opponent a P-position). Ships a stdlib-only firsthand verifier that implements the GAME as a bottom-up outcome oracle win(n,cap) — NOT the theorem — and compares it to an independently-built Fibonacci set and Zeckendorf decomposition. Fills a confirmed gap: Fibonacci nim / Zeckendorf-strategy is distinct from the Nim/Sprague-Grundy nim-sum head (P219/V232) and the Wythoff/Beatty golden-ratio head (P239/V252); it was literally flagged as an untaken atom in the Wythoff session-idea list.

## Method
Exact integer arithmetic + an iid Monte-Carlo. A bottom-up table win(n,cap) is built over n∈[1,N=800] (and N2=1200) from the raw move rules: a move takes m∈1..min(cap,n); m=n wins immediately, else the opponent faces (n−m,min(n−m,2m)); the mover wins iff some m leaves the opponent losing; the opening state is (n,n−1) and n=1→(1,0) loses. The Fibonacci set and Zeckendorf decompositions are built by integer recurrence, then compared. G1 asserts the oracle's P-set equals the Fibonacci set (0 mismatches) and the smallest-Zeckendorf-summand move is legal and leaves-P for every winning n (0 violations). G2 samples 200000 uniform piles and checks the loss-rate against the exact 7/400 (|z|<3). G3 recomputes the oracle at N2=1200 (identical P-set on the overlap) and plays 31440 randomized games where our DP player always wins. G4 rejects the "multiples of 3" foil (|z|≈20) and the "powers of two" foil (|z|≈4.3). Grounding honest against pinned Wikipedia "Fibonacci nim" (oldid 1341159330, raw-wikitext sha1 fcebea2e… verified two ways) and "Zeckendorf's theorem" (oldid 1344127047, sha1 0cc894e5…); all four cited claims are QUOTED verbatim, with the DP oracle, density fraction, z-values, and digest firsthand.

## ⟲ Previous-session review
PROPOSAL 242 (Markowitz global minimum-variance portfolio & two-fund separation → V255) landed with the born-red + four-gate + full-64-digest choreography; this slice reuses that contract exactly on the superbot-games lane. It is distinct from the shipped combinatorial-game heads: the Nim/Sprague-Grundy nim-sum head (P219/V232, XOR-of-heaps) and the Wythoff/Beatty golden-ratio cold-position head (P239/V252, ⌊nφ⌋ Beatty pairs). This is Whinihan's single-pile take-away game with a doubling reply cap, whose losing positions are the Fibonacci numbers and whose optimal move is the smallest Zeckendorf summand — the exact "Zeckendorf/Fibonacci-base" atom flagged as untaken in the Wythoff session-idea list.

## 💡 Session idea
Next untaken take-away / Fibonacci-base atoms surfaced in dedup: (a) the multi-pile Sprague-Grundy extension of Fibonacci nim (the pinned article notes the same-pile-cap variant is analysable by Sprague-Grundy); (b) the "subtract a Fibonacci number" game and its Grundy sequence; (c) the Wythoff-array / Fibonacci-base characterisation linking Wythoff cold positions to Zeckendorf digits. All grep-checked today.
