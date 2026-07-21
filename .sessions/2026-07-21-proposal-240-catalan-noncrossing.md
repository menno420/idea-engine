# PROPOSAL 240 — Catalan numbers count non-crossing handshakes: a uniformly random perfect matching of 2n circle points is non-crossing with probability exactly C_n/(2n−1)!! where C_n=binom(2n,n)/(n+1) and (2n−1)!! is the number of perfect matchings — n=2→2/3, n=3→1/3, n=4→2/15 — refuting both the "half are planar" P=1/2 belief and the "count=2^(n−1)" guess

> **Status:** in-progress

> **📊 Model:** Claude Opus · high · idea/planning
started: 2026-07-21T02:32:00Z

💓 Heartbeat:
- round/slot: fleet · enumerative combinatorics — non-crossing perfect matchings (Catalan handshake probability)
- lane: P240 → V253 (+13 offset)
- branch: claude/proposal-240-catalan-noncrossing
- verifier: ideas/fleet/verify_240_catalan_noncrossing.py (stdlib only: json, hashlib, math, random, fractions, itertools)
- SEED: 20260717 · results_sha256: 6b7c1a8ba3ca4a96e91ca5405c089cb037d3cf32d933fcf20b508e5f8faf24bf
- determinism: in-process double-run IDENTICAL · --selfcheck byte-identical · separate re-invocation byte-identical
- G1 EXACT identity (closed form == brute force, exact rational via fractions.Fraction) — for n∈{2,3,4,5,6} the three Catalan routes (recurrence, binom(2n,n)/(n+1), binom(2n,n)−binom(2n,n+1)) agree; for n∈{2,3,4} brute-force enumeration of all (2n−1)!! matchings gives total==(2n−1)!! and non-crossing==C_n, and P_brute==Fraction(C_n,(2n−1)!!) exactly {2:2/3, 3:1/3, 4:2/15}; error_count=0 · pass
- G2 MC agreement — MC_N=200000 uniform random matchings; n=3 (P=1/3) z=1.0262; n=4 (P=2/15) z=−0.8332; both |z|<3 [Z_ACCEPT=3.0] · pass
- G3 invariance — n=3 MC under random dihedral relabeling (rotation r∈[0,2n)+optional reflection) still agrees with 1/3 at z=0.3336; AND exact brute-force non-crossing COUNT invariant under all 2n rotations and reflection for n∈{3,4} (count_invariant=True both) · pass
- G4 falsifiability — SAME n=3 MC sample: naive "half are planar" P=1/2 REJECTED at z_naive=−148.1037 (|z|≥6, Z_REJECT=6.0); naive "non-crossing count=2^(n−1)" fails exactly (2^2=4≠5=C_3) · pass
- all_pass: true · first_failing_gate: null · decision: PASS

✅ Flip note (born-red → complete): this card commits FIRST with Status: in-progress to hold the PR red behind the substrate-gate; it flips to complete as the deliberate LAST commit, after the idea doc, the verifier, the outbox PROPOSAL 240 block, the full-64 digest match, and all four gates landed. The flip clears the born-red HOLD and releases native squash auto-merge.

## What this proposal does
Adds a fleet PROPOSAL establishing the exact uniform-random probability that a perfect matching of 2n points on a circle is non-crossing. There are (2n−1)!! perfect matchings (the odd double factorial); exactly C_n of them are non-crossing (C_n the n-th Catalan number), so a uniformly random matching is non-crossing with probability exactly C_n/(2n−1)!! — n=2→2/3, n=3→1/3, n=4→14/105=2/15. Ships a stdlib-only firsthand verifier that brute-force enumerates all matchings for n∈{2,3,4}, cross-checks C_n three exact ways, and falsifies the "half are planar" (P=1/2) and "count=2^(n−1)" naive beliefs. Fills a confirmed gap: Catalan non-crossing matchings is grep-0 across both repos and orthogonal to the shipped Bertrand-ballot (P220), coprime-density (P232), and Burnside/necklace (P236) heads.

## Method
Exact enumeration + closed form. C_n via recurrence, binom(2n,n)/(n+1) (Fraction, asserted integral), and binom(2n,n)−binom(2n,n+1). (2n−1)!! = 1·3·5···(2n−1). The interleaving crossing test: chords (a,b),(c,d) with a<b,c<d cross iff a<c<b<d or c<a<d<b. G1 enumerates all perfect matchings for n∈{2,3,4}, counts non-crossing ones, and asserts P_brute==Fraction(C_n,(2n−1)!!) exactly. G2 estimates the frequency by uniform sampling (greedy: pair the first unmatched point with a uniformly random partner — uniform over all matchings) for n=3 and n=4. G3 re-runs the n=3 MC under a random dihedral relabeling and, exactly, verifies the non-crossing count is invariant under all 2n rotations and reflection. G4 rejects P=1/2 (z≈−148) on the same sample and shows 2^(n−1)=4≠5=C_3.

## ⟲ Previous-session review
PROPOSAL 239 (Wythoff's game cold positions == golden-ratio Beatty pairs, → V252) landed with the born-red + four-gate + full-64-digest choreography; this slice reuses that contract exactly and extends the shipped set into enumerative combinatorics (non-crossing structures / Catalan), an atom distinct from the shipped combinatorial-game (Wythoff/Nim), probability, and coordination heads. It is orthogonal to the Bertrand-ballot head (P220, lattice-path counting), the coprime-density head (P232, number theory), and the Burnside/necklace head (P236, group action counting): those count paths, coprime pairs, and orbits; this counts non-crossing perfect matchings and casts them as an exact uniform-random probability.

## 💡 Session idea
Next untaken non-crossing / Catalan-adjacent atoms surfaced in dedup: (a) the non-crossing partition lattice NC(n) and its Kreweras complementation (self-dual, also Catalan-counted); (b) Dyck-path / ballot cast of the same C_n with the reflection (André) bijection; (c) the expected number of crossings in a uniform random matching (= binom(n,2)/3, a clean linearity-of-expectation companion to this all-or-nothing non-crossing probability). All grep-checked today.
