# PROPOSAL 245 — open-addressing unsuccessful search under uniform hashing: with m slots and n occupied (load factor α=n/m) the EXPECTED number of probes is EXACTLY (m+1)/(m−n+1), proved via the hockey-stick identity from the exact sum-of-products Σ_{i=0}^{n} C(n,i)/C(m,i), converging monotonically up to the classic 1/(1−α) — refuting the naive belief that 1/(1−α) holds exactly at finite (m,n) (at m=100,n=70 the truth is 101/31≈3.258, not 10/3≈3.333)

> **Status:** complete

> **📊 Model:** Claude Opus · high · idea/planning
started: 2026-07-21T06:17:50Z

💓 Heartbeat:
- round/slot: fleet · hashing / load-balancing — open-addressing unsuccessful-search expected probes (exact finite-table closed form)
- lane: P245 → V258 (+13 offset)
- branch: claude/p245-open-addressing-probes
- verifier: ideas/fleet/verify_245_open_addressing_probes.py (stdlib only: json, hashlib, math, random, fractions)
- SEED: 20260717 · results_sha256: 98d7398935db83b93f4e5b71ef4393abf487d3bc4371018d0d9d16e4f75e1746
- determinism: in-process double-run IDENTICAL · --selfcheck byte-identical · separate re-invocation byte-identical
- G1 EXACT identity (fractions.Fraction, zero tolerance) — over the battery {(1,0),(2,1),(3,2),(5,3),(10,7),(13,0),(16,8),(23,17),(50,35),(100,70),(128,96),(257,200)} the finite sum Σ_{i=0}^{n} C(n,i)/C(m,i), the closed form (m+1)/(m−n+1), and the hockey-stick ratio C(m+1,n)/C(m,n) are EXACTLY equal; anchors (1,0)→1, (2,1)→3/2, (3,2)→2, (10,7)→11/4 pinned; mismatches=0, anchor_mismatches=0, max discrepancy exactly 0, z=null ("exact") · pass
- G2 MC agreement — headline (m=100,n=70), N=200000 i.i.d. uniform-hashing searches (uniformly random probe permutation per trial, count probes to first empty), mean_hat=3.2596 vs E_exact=101/31≈3.2581, z=0.2616711626, |z|<3 [Z_ACCEPT=3.0]; trials INDEPENDENT (one probe-count each) so NO thinning needed · pass
- G3 invariance/robustness — expected probes depend only on (m,n) not WHICH slots occupied: config A (first n slots) z=0.3374925104, config B (fixed pseudo-random n-subset) z=−1.1046610225, two-sample invariance z=1.0187955206, all |z|<3; exact monotone-convergence sub-check at α=7/10 over m∈{10,100,1000,10000,100000} → 11/4,101/31,143/43,10001/3001,100001/30001 strictly increasing, all below limit 10/3, approaching it · pass
- G4 falsifiability — SAME headline (100,70) MC sample: naive "1/(1−α) exact at finite (m,n)"=10/3≈3.333 REJECTED at z=12.5653466132 (≫3, Z_REJECT=3.0) while the same sample agrees with exact 101/31 at |z|=0.26 · pass
- all_pass: true · first_failing_gate: null · decision: PASS

✅ Flip note (born-red → complete): this card committed FIRST with Status: in-progress to hold the PR red behind the substrate-gate; it flips to complete as the deliberate LAST commit, after the idea doc, the verifier, the outbox PROPOSAL 245 block, the claim, the full-64 digest match, and all four gates landed. The flip clears the born-red HOLD and releases native squash auto-merge.

## What this proposal does
Adds a fleet PROPOSAL establishing the exact finite-table probe cost of an unsuccessful search in an open-addressing hash table under the uniform-hashing model — each key's probe sequence is a uniformly random permutation of all m slots (Knuth / CLRS). With m slots and n occupied, load factor α=n/m, the expected number of probes an unsuccessful search makes is exactly (m+1)/(m−n+1), and as m,n→∞ at fixed α it increases monotonically to the classic 1/(1−α). Ships a stdlib-only firsthand verifier that proves the exact identity from its combinatorial definition, confirms it against a Monte-Carlo simulation of the actual uniform-hashing search, shows the count depends only on (m,n) not on which slots are occupied, and falsifies the plausible-but-wrong belief that 1/(1−α) holds exactly at finite (m,n). Fills a confirmed gap: open-addressing uniform-hashing unsuccessful-search probes is grep-0 across both repos and disjoint from birthday-collision (P132), balls-into-bins (P225), consistent-hashing-max-gap, and Maekawa grid-quorum (P209).

## Method
Exact rational arithmetic first, Monte-Carlo second. An unsuccessful search probes slots in a uniformly random order and stops at the first empty slot (which certifies the key absent); the probe count equals the position of the first empty slot in the probe permutation. As a sum of tail events E = Σ_{i≥0} P(first i probes all occupied) = Σ_{i=0}^{n} C(n,i)/C(m,i). The hockey-stick proof: C(n,i)/C(m,i)=C(m−i,n−i)/C(m,n), so Σ_{i=0}^{n} C(n,i)/C(m,i) = (1/C(m,n)) Σ_{j=0}^{n} C(m−n+j,j) = C(m+1,n)/C(m,n) = (m+1)/(m−n+1). G1 checks the finite sum, the closed form, and the hockey-stick ratio as exact fractions.Fraction. G2 draws a uniformly random probe permutation per trial with the seeded RNG, n occupied, and counts probes to the first empty — one probe-count per trial, trials independent, no thinning. G3 runs two occupancy configurations at the same (m,n) plus an exact monotone-convergence sub-check. G4 rejects the naive 1/(1−α)-at-finite-(m,n) belief on the same headline sample.

## ⟲ Previous-session review
PROPOSAL 244 (Buffon's needle short-needle crossing probability 2ℓ/(πd), → V257) landed with the born-red + four-gate + full-64-digest choreography; this slice reuses that contract exactly and extends the shipped set into hashing / load-balancing, an atom distinct from the shipped geometric-probability and queueing heads. Within hashing it is disjoint from the named prior allocation heads — birthday-collision (P132, coincidence probability), balls-into-bins (P225, max-load), consistent-hashing-max-gap (gap distribution), and Maekawa grid-quorum (P209, quorum size): those are collision/allocation/quorum objects; this is the exact expected probe count of an unsuccessful open-addressing search under uniform hashing.

## 💡 Session idea
Next untaken hashing / load-balancing atoms surfaced in dedup: (a) the SUCCESSFUL-search expected probes under uniform hashing, exactly (1/α)·ln(1/(1−α))·(...) with the exact finite (H_{m+1}−H_{m−n+1}) harmonic-difference form (a distinct object from this unsuccessful-search head); (b) the exact expected number of probes for the linear-probing model ½(1+1/(1−α)²) successful vs ½(1+1/(1−α)) unsuccessful (the quoted Wikipedia formulas — a different probe model, worth its own exact finite treatment); (c) cuckoo-hashing insertion failure / the load threshold. All grep-checked today.
