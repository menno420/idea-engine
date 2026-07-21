# PageRank / random-surfer stationary distribution on a FIXED 4-node directed graph (0→{1,2}, 1→{2,3}, 2→{0}, 3→{} dangling), damping d=1/2, uniform teleport 1/N: the row-stochastic Google matrix has the EXACT rational left-eigenvector π=(52/179, 40/179, 50/179, 37/179) with πG=π and Σπ=1 — refuting the naive belief that the stationary attention share is proportional to raw in-degree (in-degree share (1/5,1/5,2/5,1/5) is rejected on the same random-surfer sample at max|z|≈646.5)

> **State:** sim-ready
> **Status:** sim-ready

**Lane:** fleet · PageRank / random-surfer / Markov-stationary
**Proposal:** 249 → Verdict 262 (+13 offset)
**Verifier:** [`verify_249_pagerank_random_surfer.py`](verify_249_pagerank_random_surfer.py) · stdlib only (json, hashlib, math, random, fractions) · SEED=20260717
**Digest:** `results_sha256 = 18ba2ac7a7bfe36dc476214f79d55c26c3e212d8073d581ae226da55d4154355`

## What this proposal does

Adds a fleet PROPOSAL establishing the **exact rational stationary distribution** of the **PageRank random-surfer** process on a fixed directed graph. On the `N = 4` graph with out-links

    0 → {1, 2}     1 → {2, 3}     2 → {0}     3 → {}   (node 3 is DANGLING — no out-links)

with damping `d = 1/2` and uniform teleport `1/N`, the row-stochastic **Google matrix** `G` has the exact rational left-eigenvector

    π = (52/179, 40/179, 50/179, 37/179) ≈ (0.2905, 0.2235, 0.2793, 0.2067),

the unique probability vector with `πG = π`, `Σπ = 1`. **Fleet framing:** a random-surfer token routes across a fleet of agents; the damping `d` is the "follow a link" probability and `(1 − d)` is the restart/teleport probability, and `π` is each agent's exact steady-state attention / reputation share. The proposal ships a stdlib-only firsthand verifier that (i) builds `G` and **solves `π` exactly** (zero residual) with an **independent adjugate cross-check**, (ii) confirms `π` against a Monte-Carlo random-surfer chain via **batch means**, (iii) shows the answer is **equivariant** under node relabelling, and (iv) **falsifies** the plausible-but-wrong belief that the stationary share is proportional to **raw in-degree**. Fills a confirmed gap: PageRank / random-surfer / Google-matrix stationary distribution is grep-0 across both repos and disjoint from the prior Markov/queueing stationary heads (Parrondo, Jackson product-form, M/M/c Erlang-C, Palm/M/G/∞).

## Method

Exact rational arithmetic first, Monte-Carlo second.

**Google matrix (exact, row-stochastic).** With adjacency `A`, out-degree `outdeg(i)`, `d = 1/2`, and teleport term `(1 − d)/N = 1/8`:

- non-dangling row `i`:  `G[i][j] = d · (A[i][j] / outdeg(i)) + (1 − d)/N`;
- dangling row (outdeg 0): the link part is uniform, so `G[i][j] = d·(1/N) + (1 − d)/N = 1/N`.

Every row sums to 1 exactly. Explicitly (over `fractions.Fraction`):

| row | → 0 | → 1 | → 2 | → 3 |
|---|---|---|---|---|
| **0** (→{1,2}) | 1/8 | 3/8 | 3/8 | 1/8 |
| **1** (→{2,3}) | 1/8 | 1/8 | 3/8 | 3/8 |
| **2** (→{0}) | 5/8 | 1/8 | 1/8 | 1/8 |
| **3** (dangling) | 1/4 | 1/4 | 1/4 | 1/4 |

**Stationary vector (exact solve).** `πG = π` with `Σπ = 1` is solved by Gaussian elimination over `Fraction` on `(Gᵀ − I)` with one row replaced by the all-ones normalization row (rhs 1). The result is `π = (52/179, 40/179, 50/179, 37/179)`. G1 asserts the residual `πG − π` is **exactly 0** on every entry and `Σπ = 1`, and re-derives `π` a second, independent way — as the **adjugate / cofactor null-vector** of `(Gᵀ − I)` (any nonzero column of `adj(M)` lies in the null space since `M·adj(M) = det(M)·I = 0`), normalized to sum 1 — asserting exact equality (0 mismatches). Exact power iteration from the uniform vector corroborates by converging to `π` within `10⁻¹⁸`.

**Random-surfer Markov chain (Monte-Carlo).** Each step: with probability `(1 − d)` **teleport** to a uniform-random node; else (probability `d`) **follow** a uniform-random out-link of the current node; a **dangling** node's follow degenerates to a uniform teleport. This transition law reproduces `G` exactly. G2 runs ONE long chain, discards burn-in, and applies **batch means** — because random-walk occupancy along a sample path is **autocorrelated**, the iid binomial SE is structurally too small (dishonest); partitioning the post-burn-in occupancy into `B` batches (each ≫ the mixing time, so ~decorrelated) gives an honest `se = stdev(batch means)/√B` and `z = (mean − π)/se`. G3 relabels the nodes and re-solves exactly; G4 rejects the naive in-degree hypothesis on the same sample.

## Exact reference

The Google matrix and the exact stationary vector, computed two independent exact ways (Gaussian elimination and the adjugate null-vector), agree bit-for-bit:

| node k | π_k exact | π_k ≈ | in-degree | naive π_naive ∝ in-degree |
|---|---|---|---|---|
| 0 | **52/179** | 0.290503 | 1 (←2) | 1/5 = 0.200 |
| 1 | **40/179** | 0.223464 | 1 (←0) | 1/5 = 0.200 |
| 2 | **50/179** | 0.279330 | 2 (←0,1) | 2/5 = 0.400 |
| 3 | **37/179** | 0.206704 | 1 (←1) | 1/5 = 0.200 |

The exact `π` is emphatically **not** the in-degree share: node 2 has the highest in-degree (2) yet only the **second**-highest PageRank (50/179 < 52/179), because node 0 — which node 2 links to — is itself the most authoritative, and node 0's single inbound link comes from node 2. Raw in-degree ignores that a link's weight is set by the linking node's own PageRank and by the damping/teleport structure (including the dangling node 3's uniformly redistributed mass).

## Four gates (each in its own direction)

- **G1 — EXACT (`fractions.Fraction`, zero tolerance).** Build `G` exactly (rows sum to 1); solve `π` by Gaussian elimination over `Fraction`. Assert `πG = π` with **max residual exactly 0** on every entry and `Σπ = 1` exactly. Independently cross-check via the exact **adjugate / cofactor null-vector** of `(Gᵀ − I)`: `adjugate_mismatches = 0` (equals the solved `π` exactly). Exact power iteration from uniform converges to `π` within `10⁻¹⁸` in **32 iterations** (corroboration; because `λ₂ ≠ 0` an exact stochastic matrix never reaches its stationary vector in finitely many exact steps, so the two EXACT routes are the Gaussian solve and the adjugate — power iteration is asymptotic). `z` is not applicable and is reported `null` / `"exact"`.
- **G2 — Monte-Carlo agreement (`|z| < 3`, batch means).** ONE random-surfer chain, burn-in `50 000`, then `200` batches × `20 000` steps = `4 000 000` post-burn-in steps. Per-node batch-means `z` against `π`: node0 `−1.7965`, node1 `−0.3012`, node2 `0.8511`, node3 `0.8993`, **max|z| = 1.7965 < 3** [Z_ACCEPT = 3.0]. Random-walk occupancy is **autocorrelated**, so the iid binomial SE would be dishonest — **batch means** (batch size ≫ mixing time) give an honest SE; this is stated explicitly in the verifier docstring.
- **G3 — equivariance / invariance (own direction).** Apply the fixed non-trivial node relabel `σ = [2, 0, 3, 1]` (old node `i` → new label `σ(i)`), rebuild `G` and re-solve `π` on the permuted graph **exactly**, and assert it equals `σ(π_original)` exactly: `relabel_mismatches = 0`. Concretely `π_permuted = (40/179, 37/179, 52/179, 50/179) = σ(π)`. A verifier that hard-codes node indices breaks this.
- **G4 — falsifiability (own direction, on the SAME G2 sample).** The plausible naive hypothesis `π_naive ∝ in-degree = (1/5, 1/5, 2/5, 1/5)` is **false**. On the same batch-means sample the `z` against `π_naive` is **REJECTED** at **max|z| = 646.5432** (node2 `−646.54`, node0 `568.61`, ≫ Z_REJECT = 6.0), while the same sample **agrees** with the true `π` at `max|z| = 1.80`. The teeth: raw in-degree is a plausible-but-wrong stationary law; PageRank weights each inbound link by the source's own score and redistributes dangling mass, so node 2 (in-degree 2) sits **below** node 0 (in-degree 1).

All four gates PASS; `all_pass = true`, `first_failing_gate = null`, `decision = PASS`, `results_sha256 = 18ba2ac7a7bfe36dc476214f79d55c26c3e212d8073d581ae226da55d4154355`. Deterministic three ways: in-process double-run byte-identical (`in_process_double_run: IDENTICAL`), a `--selfcheck` path printing `SELFCHECK: byte-identical`, and a separate-process re-invocation byte-identical. SEED = 20260717 (hardcoded module constant).

## Grounding

One pinned Wikipedia revision (API `revisions.sha1` == self-computed `sha1sum` of the raw wikitext — exact match):

- **"PageRank"**, oldid 1364775010:
  `https://en.wikipedia.org/w/index.php?title=PageRank&oldid=1364775010@faa1d38442418ee08add5a47d8950ae58d0bbedf` (74463 bytes), fetched 2026-07-21.

- **Quoted** literally on the pinned "PageRank" revision (grep count > 0): the exact PageRank formula `PR(p_i) = \frac{1-d}{N} + d \sum_{p_j \in M(p_i)} \frac{PR(p_j)}{L(p_j)}` (grep 1) — with the teleport term `\frac{1-d}{N}` (grep 5), the damping factor `d`, the out-degree normalization `L(p_j)` (grep 4); the phrase "**random surfer**" (grep 2, "a random surfer will land on that page by clicking on a link"); "**damping factor**" (grep 7) with the article's illustrative value `0.85` (grep 2); "**Google matrix**" (grep 2); "**Markov chain**" (grep 3) and the "probability distribution" over pages (grep 7).
- **Derived** firsthand (grep count 0 on the pinned raw wikitext): the specific fixed 4-node graph `0→{1,2}, 1→{2,3}, 2→{0}, 3→{}` and its adjacency; the chosen damping `d = 1/2` for THIS graph (the page's illustrative value is `0.85`, not `1/2`); the exact rational stationary vector `π = (52/179, 40/179, 50/179, 37/179)` (grep 0 for `179`, `52/179`); the matrix form `πG = π` solved as an exact rational left-eigenvector, and the independent adjugate null-vector cross-check; the **dangling**-node uniform-row handling (the words "dangling" and "teleport" are grep 0 on this revision — the uniform redistribution of a dead-end's mass is the standard Google-matrix construction, applied firsthand here, not literally on the page); the naive in-degree foil; the batch-means Monte-Carlo random-surfer chain; every z-value; SEED 20260717; and the results digest. **Honest posture** — the random-surfer model, the damping factor, the exact PageRank recurrence `(1−d)/N + d·Σ PR(p_j)/L(p_j)`, the Google matrix, and the Markov-chain / stationary-distribution framing are QUOTED textbook material on the pinned page; the specific fixed graph, the chosen `d = 1/2`, the exact rational `π`, the two exact solve routes, the dangling-uniform handling, the batch-means MC agreement, the equivariance leg, the in-degree falsification, and every z-value + the digest are the firsthand contribution. Nothing oversold as novel: PageRank and the Google matrix are textbook (Brin & Page 1998; Langville & Meyer), cited as such.

## Probe report (v0, self-adversarial)

**1. Is the core claim exactly true (not merely approximate)?** Yes. G1 builds the row-stochastic Google matrix `G` entirely in `fractions.Fraction`, solves `πG = π` with `Σπ = 1` by exact Gaussian elimination, and asserts the residual `πG − π` is **exactly 0** on every one of the four entries with `Σπ = 1` exactly — the max residual is a literal `0`, not a small float. The answer `π = (52/179, 40/179, 50/179, 37/179)` is re-derived a genuinely independent way (the adjugate/cofactor null-vector of `Gᵀ − I`, direct determinant expansion, no reuse of the elimination) and agrees bit-for-bit (`adjugate_mismatches = 0`). It is a closed-form rational eigenvector, not a fit.

**2. Could the numbers be an artefact of the sampler rather than the mechanism?** No. The exact `π` (G1) is fixed before any RNG is touched. The Monte-Carlo gate (G2) only *confirms* the occupancy of the actual random-surfer chain: with prob `1−d` teleport uniformly, else follow a uniform out-link (dangling ⇒ teleport). Its batch-means `z` against `π` lands at `max|z| = 1.80`.

**3. What is the most plausible wrong belief this could be confused with?** That the stationary attention share is proportional to **raw in-degree** — pre-registered as G4 and refuted on the same sample at `max|z| = 646.5` (node 2 has the highest in-degree yet only the second-highest PageRank). A secondary confusion — that the answer depends on the node *labelling* — is refuted by G3 (equivariance, 0 mismatches under the relabel `σ = [2,0,3,1]`).

**4. Is the verifier deterministic and self-checking?** Yes. A single `random.Random(20260717)` is seeded once and consumed in a fixed order across the whole chain; `build_results()` is a pure function of SEED and the module constants (no wall-clock / PID / unordered-set iteration in the hashed payload). Exact rationals serialize via `str(Fraction)` as `"num/den"`, integer visit counts as ints, and every z-value via a fixed `f"{z:.4f}"` string, so the bytes are stable. `main()` asserts an in-process double-run is byte-identical, `--selfcheck` prints "SELFCHECK: byte-identical", and two separate process invocations reproduce the digest byte-for-byte. Whole-dict `results_sha256 = 18ba2ac7a7bfe36dc476214f79d55c26c3e212d8073d581ae226da55d4154355`.

**5. Does the grounding actually support the claim, or is it overstated?** Honest and tight. The pinned "PageRank" revision carries the random-surfer model, the damping factor, the exact recurrence `(1−d)/N + d·Σ PR(p_j)/L(p_j)`, the Google matrix, and the Markov / stationary-distribution framing — all QUOTED. Derived-not-quoted (grep 0): the specific fixed 4-node graph, the chosen `d = 1/2` (the page's illustrative value is `0.85`), the exact rational `π`, the dangling-uniform handling (the words "dangling"/"teleport" are absent on this revision — the construction is standard and applied firsthand), the in-degree foil, and every z-value. Neither oversold nor undersold.

**6. Does it scale / is it robust?** The construction is general — `G` is built from an arbitrary adjacency and out-degrees, and the solve/adjugate/power-iteration routes are index-generic. G3 exercises exactly this: relabelling the nodes and re-solving reproduces `σ(π)` exactly (`relabel_mismatches = 0`), so the result is a property of the graph, not of a hard-coded index order. The dangling node 3 is handled by the standard uniform row, keeping `G` row-stochastic.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers the single most plausible wrong belief ("π ∝ in-degree") and refutes it on the same evidence at `max|z| = 646.5`, while G2 shows that same sample agrees with the exact `π` at `max|z| = 1.80`. A wrong teleport/damping split, an off-by-one in the dangling handling, or dropping the `(1−d)/N` term would break the exact G1 residual or push a G2 z past the accept band.

**8. Any residual risk before ruling?** The Monte-Carlo leg is an autocorrelated random walk, so — unlike an iid estimator — the honest SE requires **batch means** (batches ≫ mixing time); this is implemented and stated explicitly in the docstring, and the fast-mixing chain (spectral gap governed by `|λ₂| ≤ d = 1/2`) lands every per-node `|z| < 1.8`. The exact identity (G1) is what carries the claim and is RNG-free, with two independent exact routes (Gaussian solve + adjugate). The random-surfer model, the damping factor, the PageRank recurrence, and the Google matrix are textbook (Brin & Page 1998; Langville & Meyer; the pinned "PageRank" page) and cited as such; the exact rational `π`, the two solve routes, the dangling-uniform handling, the MC agreement, the equivariance leg, and the in-degree falsification are the firsthand contribution. The paired sim-lab VERDICT 262 reproduction is a separate coordinator-driven slice. No further blocker.

**Recommendation: sim-ready**
