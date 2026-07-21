# PROPOSAL 249 — PageRank / random-surfer stationary distribution on a FIXED 4-node directed graph (0→{1,2}, 1→{2,3}, 2→{0}, 3→{} dangling), damping d=1/2, uniform teleport 1/N: the row-stochastic Google matrix has the EXACT rational left-eigenvector π=(52/179, 40/179, 50/179, 37/179) (πG=π, Σπ=1) — refuting the naive belief that the stationary attention share is proportional to raw in-degree (in-degree share (1/5,1/5,2/5,1/5) is rejected on the same random-surfer sample at max|z|=646.5)

> **Status:** in-progress

> **📊 Model:** Claude Opus · high · idea/planning
started: 2026-07-21T09:15:03Z

💓 Heartbeat:
- round/slot: fleet · PageRank / random-surfer — exact stationary distribution of the Google matrix on a fixed 4-node directed graph (closed-form rational left-eigenvector)
- lane: P249 → V262 (+13 offset)
- branch: claude/proposal-249-pagerank-random-surfer
- verifier: ideas/fleet/verify_249_pagerank_random_surfer.py (stdlib only: json, hashlib, math, random, fractions), file sha256 3e1e7647fb485f0739ebce9f4d3f288f09ea5c97b15115e7166cf91324f812c1
- SEED: 20260717 · results_sha256: 18ba2ac7a7bfe36dc476214f79d55c26c3e212d8073d581ae226da55d4154355
- determinism: in-process double-run IDENTICAL · --selfcheck byte-identical · separate re-invocation byte-identical
- G1 EXACT (fractions.Fraction, zero tolerance) — build the row-stochastic Google matrix G exactly (non-dangling row G[i][j]=d·A[i][j]/outdeg(i)+(1−d)/N; dangling row uniform 1/N), solve π by Gaussian elimination over Fraction on (Gᵀ−I) with the Σπ=1 constraint → π=(52/179,40/179,50/179,37/179); πG=π with max residual EXACTLY 0 on every entry and Σπ=1 exactly; independent adjugate/cofactor null-vector of (Gᵀ−I) equals π exactly (adjugate_mismatches=0); exact power iteration from uniform converges to π within 1e-18 in 32 iters (corroboration — λ₂≠0 so an exact stochastic matrix never reaches π in finitely many exact steps) · z=null (exact) · pass
- G2 MC AGREEMENT (|z|<3, batch means) — ONE random-surfer chain, burn-in 50000, then 200 batches × 20000 steps = 4,000,000 post-burn-in steps; per-node batch-means z against π: node0 −1.7965, node1 −0.3012, node2 0.8511, node3 0.8993, max|z|=1.7965 [Z_ACCEPT=3.0]; random-walk occupancy is AUTOCORRELATED so the iid binomial SE is dishonest — batch means (batches ≫ mixing time) give an honest SE · pass
- G3 EQUIVARIANCE/INVARIANCE (own direction) — apply the fixed non-trivial node relabel σ=[2,0,3,1], rebuild G and re-solve π on the permuted graph EXACTLY, assert it equals σ(π_original) exactly: relabel_mismatches=0 (a verifier that hard-codes node indices breaks this) · pass
- G4 FALSIFIABILITY (own direction, SAME MC sample) — the plausible naive hypothesis "π ∝ in-degree" = (1/5,1/5,2/5,1/5) is REJECTED on the same batch-means sample at max|z|=646.5432 (node2 −646.5, node0 568.6, ≫ Z_REJECT=6.0) while that same sample AGREES with the true π at max|z|=1.80 — the teeth: raw in-degree ignores that a link's weight is itself set by the linking node's PageRank and the damping/teleport structure · pass
- all_pass: true · first_failing_gate: null · decision: PASS

✅ Flip note (born-red → complete): this card committed FIRST with Status: in-progress to hold the PR red behind the substrate-gate; it flips to complete as the deliberate LAST commit, after the idea doc, the verifier, the outbox PROPOSAL 249 block, the claim, the full-64 digest match, and all four gates landed. The flip clears the born-red HOLD and releases native squash auto-merge.

## What this proposal does

Adds a fleet PROPOSAL establishing the EXACT rational stationary distribution of the PageRank random-surfer process on a fixed directed graph. On the N=4 graph with out-links 0→{1,2}, 1→{2,3}, 2→{0}, 3→{} (node 3 is dangling — no out-links), with damping d=1/2 and uniform teleport 1/N, the row-stochastic Google matrix G has the exact rational left-eigenvector

    π = (52/179, 40/179, 50/179, 37/179) ≈ (0.2905, 0.2235, 0.2793, 0.2067),

the unique probability vector with πG=π. Fleet framing: a random-surfer token routes across a fleet of agents; the damping d is the "follow a link" probability and (1−d) is the restart/teleport probability, and π is each agent's exact steady-state attention / reputation share. The proposal ships a stdlib-only firsthand verifier that (i) builds G and solves π EXACTLY (zero residual) with an independent adjugate cross-check, (ii) confirms π against a Monte-Carlo random-surfer chain via batch means, (iii) shows the answer is EQUIVARIANT under node relabelling, and (iv) FALSIFIES the plausible-but-wrong belief that the stationary share is proportional to raw in-degree. Fills a confirmed gap: PageRank / random-surfer / Google-matrix stationary distribution is grep-0 across both repos and disjoint from the prior Markov/queueing stationary heads (Parrondo, Jackson product-form, M/M/c Erlang-C, Palm/M/G/∞).

## Method

Exact rational arithmetic first, Monte-Carlo second. G is built as exact Fractions: a non-dangling row i has G[i][j]=d·(A[i][j]/outdeg(i))+(1−d)/N, and the dangling row (outdeg 0) is uniform 1/N (the link part becomes uniform, so d·(1/N)+(1−d)/N=1/N). Every row sums to 1 exactly. G1 solves πG=π by Gaussian elimination over Fraction on (Gᵀ−I) with one row replaced by the Σπ=1 constraint, asserts the residual πG−π is exactly 0 on every entry and Σπ=1, and independently re-derives π as the adjugate null-vector of (Gᵀ−I) (a genuinely distinct route — direct cofactor determinants, no reuse of the elimination) with 0 mismatches; exact power iteration from the uniform vector corroborates by converging to π within 1e-18. G2 runs one long random-surfer chain (each step: with prob 1−d teleport uniformly, else follow a uniform out-link, dangling⇒teleport), discards burn-in, and applies BATCH MEANS — because random-walk occupancy along a sample path is autocorrelated, the iid binomial SE is dishonest, so per-node batch means over 200 batches give an honest SE and z against π. G3 relabels the nodes by a fixed non-trivial permutation, rebuilds and re-solves π exactly, and asserts equivariance π_permuted=σ(π). G4 rejects the naive in-degree-proportional hypothesis on the same MC sample.

## ⟲ Previous-session review

PROPOSAL 248 (middle-thirds Cantor set — exact Lebesgue measure 0 and exact Hausdorff = box-counting dimension log2/log3 → V261) landed with the born-red + four-gate + full-64-digest choreography; this slice reuses that contract exactly and extends the shipped set into the PageRank / random-surfer / Markov-stationary lane. Within the stationary-distribution family it is disjoint from the named prior heads — Parrondo's paradox (stationary π of the capital-parity chain), Jackson product-form independence, M/M/c Erlang-C delay (P241, birth-death stationary law), and Palm / M/G/∞ insensitivity: those are queueing / game-theoretic stationary objects, whereas this is the exact closed-form left-eigenvector of the Google matrix (random-surfer web/attention model) on a fixed directed graph with a dangling node — grep-0 across both repos.

## 💡 Session idea

Next untaken PageRank / random-surfer / spectral-graph atoms surfaced in dedup (all grep-checked today, all grep-0): (a) the exact SENSITIVITY of π to the damping factor d — π(d) is a rational function of d, with π(0)=uniform and π(1)=the dangling-free chain's stationary law, and the "PageRank leak" of dangling mass as d→1; (b) personalized / topic-sensitive PageRank with a non-uniform teleport vector v, and the linearity π(v) as an exact convex combination; (c) the exact HITTING / commute times and Kemeny's constant of the same random-surfer chain (Σ_j π_j·m_ij is independent of i); (d) the power-iteration convergence rate governed exactly by the subdominant eigenvalue |λ₂| ≤ d. Each has a clean exact rational form and a stdlib-checkable structure on a fixed small graph.
