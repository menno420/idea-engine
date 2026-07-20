# Session — PROPOSAL 232 (coprime density = 6/π² → VERDICT 245)

> **Status:** `complete`
> Born-red HOLD: this card lands `in-progress` on the first commit to hold the PR red through the substrate-gate, and flips to `complete` as the deliberate last commit once the idea doc, verifier, outbox block, and claim are in place and the paired sim-lab reproduction is verified green. Merge is by native squash auto-merge on all-green.

## 💡 Session idea
Cross-cutting FLEET slot. PROPOSAL 232: for two integers drawn independently and uniformly from {1,…,N}, the probability they are coprime is the exact Möbius-inversion density Q(N)=(1/N²)·Σ_{k=1}^{N} μ(k)·⌊N/k⌋², converging to 6/π²=1/ζ(2)≈0.6079271018540267 as N→∞ — the number-theoretic coprime density (Cesàro 1881; Basel ζ(2)=π²/6), NOT the plausible-but-wrong "just avoid a shared factor of 2 ⇒ 3/4" value. Paired reproduction mirror in sim-lab under sims/verdict-245-coprime-density/ (offset +13); the canonical independent ruling is a separate coordinator-driven VERDICT 245 slice.

## ⟲ Previous-session review
P230 (VENTURE, bilateral double auction → VERDICT 243) landed. This slice stakes the coordinator-assigned P232 (coprime density / Basel ζ(2), an untaken pure-number-theory atom, distinct from any covered card). This slice does not touch control/status.md (coordinator-owned) and does not author a VERDICT block or advance the verdict high-water; proposal high-water advances to P232.

## 🫀 Heartbeat
Verifier ideas/fleet/verify_232_coprime_density.py authored firsthand; born-red card holds the PR through substrate-gate until the deliberate final flip. To be verified green before flip: exit 0, all four gates PASS, results_sha256 754580401315c5e987d30467f1d99ee125605f6203de69d9340f910308840fec byte-identical across in-process double-run + separate re-invocation (SEED=20260717, stdlib-only, Python 3.11.15). G1 EXACT two routes (brute A(N)==Möbius B(N)) for N∈{1,2,3,4,5,6,10,50,100,200}, Q(6)=23/36. G2 MC N=10000 M=200000 z_agreement=+0.774312 (p̂=0.608795, Q_N=60794971/100000000≈0.60794971, asymptote 6/π²≈0.6079271018540267). G3 EXACT partition invariant Σ_{d=1}^{N} A(⌊N/d⌋)==N² for N∈{1,2,3,10,20,50,100,200} plus 0<Q(N)<1 (N≥2; Q(1)=1 boundary). G4 falsifiability — the naive 3/4 rejected on the SAME MC sample at z_naive=−145.835897 (|z|≥8), the 2-only fallacy predicts 0.75 while the true density is 6/π²≈0.6079. Grounding pins Wikipedia "Coprime integers" oldid 1363371102 sha1 254a5e6988f14ce74d40502b159f687ea8c4947c. A byte-identical copy is carried in the paired sim-lab reproduction PR (branch claude/proposal-232-coprime-density-mirror); the canonical independent ruling is a separate coordinator-driven VERDICT 245 slice.

> **📊 Model:** Claude Opus · high · idea/planning

## Decisions made
- Chose the Möbius-inversion finite-N density Q(N)=(1/N²)Σμ(k)⌊N/k⌋² with two independent exact routes (brute-force gcd count vs Möbius sieve) — a self-certifying identity, not a restatement.
- G3's teeth is the exact partition invariant Σ_d A(⌊N/d⌋)=N² (unique-gcd decomposition), checked as exact integer equality; the strict 0<Q<1 check applies for N≥2 (Q(1)=1 is the degenerate single-pair boundary, recorded honestly).
- G4 falsifier is the plausible-but-wrong "avoid a shared factor of 2 ⇒ 3/4" hypothesis, rejected at z_naive≈−146 on the same MC sample — opposite polarity to G2's agreement.
- Grounding pinned to the "Coprime integers" revision, which states 6/π²=1/ζ(2)≈0.607927102 and the P_N→6/π² limit (Cesàro 1881, Hardy–Wright Thm 332) literally; the finite-N Möbius identity, the partition invariant, every z-value, and the 3/4 falsifier are honestly labelled derived.
- Did not author a VERDICT block or advance the verdict high-water, and did not touch control/status.md — the canonical VERDICT 245 ruling is a dedicated slice.

## Next session should know
- The paired sim-lab reproduction mirror lands the byte-identical verifier under sims/verdict-245-coprime-density/; the canonical independent VERDICT 245 ruling is still pending its dedicated coordinator-driven slice.
- No edits were made to control/status.md.
