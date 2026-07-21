# PROPOSAL 239 — Wythoff's game cold positions are exactly the golden-ratio Beatty pairs: the P-positions (Sprague-Grundy value 0) are P_n=(⌊nφ⌋,⌊nφ²⌋) with the exact identity b_n=a_n+n and φ=(1+√5)/2, the two sequences partition Z+ (Beatty, since 1/φ+1/φ²=1) so the lower density is 1/φ≈0.618 — refuting both the "(k,2k)" losing-position guess and the "even 50/50 split" density belief

> **Status:** complete

> **📊 Model:** Claude Opus · high · idea/planning
started: 2026-07-21T01:57:49Z

💓 Heartbeat:
- round/slot: fleet · combinatorial game theory — Wythoff cold positions (closed-form Beatty characterisation)
- lane: P239 → V252 (+13 offset)
- branch: claude/wythoff-beatty
- verifier: ideas/fleet/verify_239_wythoff_beatty.py (stdlib only: json, hashlib, math, random, fractions)
- SEED: 20260717 · results_sha256: 9fe0e90d2c4544a9c38c051be34b9369fdf84f12b53e4ed16818feb5c87eabcc
- determinism: in-process double-run IDENTICAL · separate re-invocation byte-identical
- G1 EXACT identity (integer arithmetic, fractions.Fraction where a ratio appears) — over board panel N∈{30,60,90} the Sprague-Grundy mex-DP Grundy-0 positions equal EXACTLY the isqrt-Beatty pairs {(a_n,b_n):b_n≤N}; b_n−a_n==n for all n≤200000; exact Beatty partition of 1..M for M∈{1000,100000,1000000} (zero overlap, full cover, |{a_n≤M}|+|{b_n≤M}|==M as Fraction); error_count=0 · pass
- G2 MC agreement — K=200000 uniform ints in [1,1000000], lower-Wythoff membership p̂=0.617290 vs 1/φ=0.618034, z=−0.684799, |z|<3 [Z_ACCEPT=3.0] · pass
- G3 invariance — isqrt-Beatty generator == greedy/mex generator (a_n=mex{a_i,b_i:i<n}, b_n=a_n+n) exactly over the panel; Grundy table pile-swap symmetric G(x,y)==G(y,x) all cells; mismatch_count=0 · pass
- G4 falsifiability — SAME MC sample: naive "even 50/50 split" density=1/2 REJECTED at z_reject=104.907365 (≥6, Z_REJECT=6.0); naive universal "(k,2k)"/b_n=2a_n refuted — holds only at coincidental fits n=0 (0,0) and n=1 (1,2), breaks at n=2 (3,5) with 199999 counterexamples over the panel · pass
- all_pass: true · first_failing_gate: null · decision: PASS

✅ Flip note (born-red → complete): this card committed FIRST with Status: in-progress to hold the PR red behind the substrate-gate; it flips to complete as the deliberate LAST commit, after the idea doc, the verifier, the outbox PROPOSAL 239 block, the full-64 digest match, and all four gates landed. The flip clears the born-red HOLD and releases native squash auto-merge.

## What this proposal does
Adds a fleet PROPOSAL establishing the exact closed-form characterisation of the cold (P) positions of Wythoff's game — the two-pile take-away game where a move removes k≥1 from one pile or the same k≥1 from both, last to move wins. The previous-player-wins positions (Sprague-Grundy value 0) are exactly the golden-ratio Beatty pairs P_n=(⌊nφ⌋,⌊nφ²⌋), φ=(1+√5)/2, with the exact integer identity b_n=a_n+n; the lower and upper sequences partition the positive integers (Beatty's theorem, 1/φ+1/φ²=1), giving lower density 1/φ≈0.618, not 1/2. Ships a stdlib-only firsthand verifier with a float-free isqrt floor and a Sprague-Grundy mex-DP cross-check. Fills a confirmed gap: Wythoff/Beatty is grep-0 across both repos and disjoint from the Nim/Sprague-Grundy nim-sum head (V232/P219) and the Banzhaf head (V216/P203).

## Method
Exact integer arithmetic. a_n=⌊nφ⌋=(n+isqrt(5n²))//2 (float-free, exact because n√5 is irrational), b_n=a_n+n=⌊nφ²⌋. G1 runs a Sprague-Grundy mex-DP over the board (Grundy value = mex of positions reachable by the three Wythoff move types; cold = Grundy 0) and asserts the Grundy-0 set equals the isqrt-Beatty pairs exactly, plus b_n−a_n==n and the exact 1..M Beatty partition (fractions.Fraction for the count ratios). G2 estimates the lower-Wythoff density by uniform sampling and compares to 1/φ. G3 cross-checks the isqrt generator against an independent greedy/mex construction and verifies pile-swap symmetry of the Grundy table. G4 rejects the naive "even 50/50 split" density (z_reject≈105) on the same sample and refutes the naive "(k,2k)" universal rule (breaks at (3,5)).

## ⟲ Previous-session review
PROPOSAL 238 (insurance risk-pooling / diversification variance law, → V251) landed with the born-red + four-gate + full-64-digest choreography; this slice reuses that contract exactly and extends the shipped set into combinatorial game theory, an atom distinct from the shipped probability/coordination heads. Within combinatorial games it is disjoint from the Nim/Sprague-Grundy nim-sum head (V232/P219) and the Banzhaf-power head (V216/P203): those are XOR-of-heaps and voting-power; this is Wythoff's two-pile game whose cold positions are the golden-ratio Beatty pairs.

## 💡 Session idea
Next untaken combinatorial-game atoms surfaced in dedup: (a) the misère-Wythoff cold positions (the pinned article notes (0,1) and (2,2) become cold, with a swap for n,m>2); (b) the Zeckendorf/Fibonacci-base characterisation of Wythoff cold positions and the "Wythoff array"; (c) subtract-a-square (Grundy sequence of the take-a-perfect-square game). All grep-checked today.
