# Committee-sortition safety in a Byzantine fleet — a fleet of N=64 agents with B=21 Byzantine sits EXACTLY at the classical BFT safety bound N=3B+1 (n≥3f+1, f=21), yet a size-K=16 committee drawn by uniform sortition WITHOUT replacement is UNSAFE (≥ T=floor(K/3)+1=6 Byzantine members, breaking a K-node quorum that tolerates floor((K−1)/3)=5) with EXACT hypergeometric probability P = Σ_{i=T}^{K} C(B,i)·C(N−B,K−i)/C(N,K) = 296431911/685926212 ≈ 0.432163. A globally-safe fleet produces unsafe sub-committees ~43% of the time because sortition CONCENTRATES Byzantine nodes: the expected Byzantine count per committee K·B/N = 5.25 sits just below the threshold 6, so a large tail of committees crosses it. The exact hypergeometric tail (G1, `Fraction`, cross-checked by Vandermonde and by complement), the iid MC agreement (G2, |z|=2.20), the Byzantine-identity invariance (G3, a different Byzantine set of the same size, |z2|=0.69), and the falsification of the naive with-replacement Binomial(K,B/N) foil that OVERSTATES the tail (G4, rejected at |z|=6.08 on the same sample) all PASS. A coordination/consensus head over a fleet of agents.

> **State:** sim-ready
> **Status:** sim-ready
> **📊 Model:** Claude Opus · high · idea/planning

**Lane:** fleet · coordination / consensus over a fleet of agents · committee sortition under Byzantine faults
**Proposal:** 253 → Verdict 266 (+13 offset) — named by the `## PROPOSAL 253` block in `control/outbox.md`
**Verifier:** [`verify_253_bft_committee_sortition.py`](verify_253_bft_committee_sortition.py) · stdlib only (math, random, fractions, hashlib, json, argparse, sys) · SEED=20260717
**Digest:** `results_sha256 = 37567447cc2e96a1b1c57404ed3e43b52d09c829f186293cc5f4f6122a03802d`

## What this proposal does

Adds a fleet PROPOSAL establishing **committee-sortition safety in a Byzantine fleet** — a coordination/consensus head. A fleet of `N=64` agents, of which `B=21` are Byzantine, sits **exactly** at the classical BFT safety bound:

> `64 = 3·21 + 1`,  i.e.  `n ≥ 3f+1` with `f = 21`,

so the full system tolerates its 21 Byzantine agents. But a committee of `K=16` agents drawn by **uniform sortition WITHOUT replacement** is **UNSAFE** iff it contains

> `≥ T = floor(K/3)+1 = 6` Byzantine members

(a K-node BFT quorum tolerates only `floor((K−1)/3) = 5`). The number of Byzantine members in a sortition committee is `Hypergeometric(N, B, K)`, so the committee-failure probability is the **exact hypergeometric upper tail**

> `P = Σ_{i=T}^{K} C(B,i)·C(N−B, K−i) / C(N,K)`,  with `N=64, B=21, N−B=43, K=16, T=6`,

which evaluates to the **exact rational** `P = 296431911/685926212 ≈ 0.432163`.

**The insight.** A globally-safe fleet still produces UNSAFE sub-committees ~43% of the time. The expected Byzantine count per committee is `E[X] = K·B/N = 16·21/64 = 5.25`, just below the threshold of 6 — but sortition **concentrates** Byzantine nodes, so a large tail of committees crosses the threshold anyway. This is exactly why committee-BFT protocols must **size** committees to bound the sortition failure probability: the fleet-level `n≥3f+1` guarantee does **not** transfer to a uniformly-sampled sub-committee for free.

**Headline numbers.** Exact tail `P = 296431911/685926212 = 0.432163` (Vandermonde full-pmf residual `0`, tail-via-complement mismatch `0`). MC estimate over `N=400000` iid committee draws `p_hat = 0.430443`, `z = −2.1966`. Byzantine-identity invariance: a different Byzantine set `byz2 = {(i·3) mod 64 : i<21}` gives `p_hat2 = 0.432700`, `z2 = 0.6856`. The with-replacement Binomial(K, B/N) foil `P_binom = 0.435210` is rejected at `z_foil = −6.0822` on the same sample that accepts the hypergeometric `P` at `z = −2.1966`.

**Distinctness.** `byzantine` / `sortition` / `bft` / `3f+1` are **grep-0** across both repos (`control/outbox.md`, `ideas/`, `sims/`). `hypergeometric` appears only as the deck-variance tool in the mana-screw head (P163 — opening-hand finite-population *variance*, a different quantity in a different domain), and `committee` only in the Condorcet jury head (P202 — a **with-replacement binomial** majority-correctness object `M(n,p) = Σ C(n,k)p^k(1−p)^{n−k}`, which this proposal's G4 foil explicitly **rejects** as the wrong model for without-replacement sortition). The identity here — a hypergeometric committee-failure *tail* read against the `n≥3f+1` safety bound — is distinct from both.

## Method

Exact rational tail first, Monte-Carlo agreement second.

**Structural check.** `assert N == 3*B + 1` (64 = 3·21+1) and `assert T == 6` at module top — the fleet sits exactly at the classical BFT bound before any arithmetic runs.

**Exact backbone (`fractions.Fraction`, no float in the identity).** `pmf_exact(i) = Fraction(C(B,i)·C(N−B,K−i), C(N,K))` is the exact hypergeometric pmf. The tail `P = Σ_{i=T}^{K} pmf_i` is cross-checked two independent ways: (A) the full pmf `Σ_{i=0}^{K} pmf_i == 1` exactly (Vandermonde's identity `Σ_i C(B,i)C(N−B,K−i) = C(N,K)`), residual `== 0`; (B) the tail via complement `P == 1 − Σ_{i=0}^{T−1} pmf_i`, `0` mismatch. Because these are exact `Fraction` arithmetic, the tail value has no floating-point error.

**Monte-Carlo (iid — no thinning).** `rng = random.Random(SEED)`; each committee is a fresh `rng.sample(range(N), K)` of K distinct agents, so the per-committee UNSAFE indicators are **iid Bernoulli(P)** — the plain iid binomial standard error is the honest one. This is unlike a queue-occupancy sample path, which is autocorrelated and would need batch means / thinning; independent committee draws do not (stated in the verifier docstring). `z = (p_hat − P)/sqrt(P(1−P)/MC_N)`.

## Exact reference

The exact hypergeometric committee-failure tail (exact `Fraction`, cross-checked two ways, 0 residual / 0 mismatch):

| quantity | value |
|---|---|
| `N` (fleet) | 64 |
| `B` (Byzantine) | 21 |
| `N = 3B+1`? | **yes** — exactly at the BFT bound |
| `K` (committee, sortition draw) | 16 |
| `T = floor(K/3)+1` (unsafe threshold) | 6 |
| `E[X] = K·B/N` (expected Byzantine per committee) | 5.25 |
| **`P` (exact tail)** | **`296431911/685926212`** |
| `P` (float) | `0.432163` |
| Vandermonde full-pmf residual | `0` |
| tail-via-complement mismatch | `0` |

The mean `E[X] = 5.25` sits **below** the threshold `T = 6`, yet `P ≈ 0.432` — a large fraction of committees cross the threshold, the exact quantitative statement that sortition concentrates Byzantine nodes.

## Four gates (each in its own direction)

- **G1 — EXACT (`fractions.Fraction`, zero tolerance).** The hypergeometric upper tail `P = Σ_{i=6}^{16} C(21,i)·C(43,16−i)/C(64,16) = 296431911/685926212`, cross-checked two independent ways: the full pmf sums to 1 exactly (Vandermonde), residual `= 0`; and `P == 1 − Σ_{i=0}^{5} pmf_i`, mismatch `= 0`. No float enters the identity. `z` is not applicable → reported `"exact"`. PASS.
- **G2 — MC agreement (`|z| < 3`).** `N=400000` iid committee draws (`rng.sample`, without replacement), `p_hat = 0.430443` vs the exact `P = 0.432163`, `z = −2.1966`, `|z| < 3` [Z_ACCEPT=3.0]. iid draws → plain iid binomial SE is honest (no batch means). PASS.
- **G3 — invariance (Byzantine-identity, own direction).** The exact `P` is a function of the counts `(N,B,K,T)` only, not of *which* agents are Byzantine — structurally true by construction. Demonstrated empirically too: a **different** Byzantine set `byz2 = {(i·3) mod 64 : i<21}` (distinct because `gcd(3,64)=1`) gives `p_hat2 = 0.432700`, `z2 = 0.6856` against the same exact `P`, `|z2| < 3`. PASS.
- **G4 — falsifiability (reject at large `|z|`, own direction, SAME sample as G2).** Pre-registered naive foil: *"the committee behaves like `K` iid draws WITH replacement at rate `p = B/N`, so `P_binom = Σ_{i=T}^{K} C(K,i) p^i (1−p)^{K−i}`."* This ignores the finite-population **negative correlation** of sampling without replacement, so it **overstates** the tail: `P_binom = 0.435210 ≠ P = 0.432163`. On the same `N=400000` without-replacement sample, `z_foil = (p_hat − P_binom)/sqrt(P_binom(1−P_binom)/MC_N) = −6.0822`, `|z_foil| > 3` → REJECTED, while the same sample AGREES with the hypergeometric `P` at `z = −2.1966`. The two hypotheses are `≈3.9σ` apart, so the same sample lands inside the hypergeometric band and outside the binomial one — a decisive (`p ≈ 1.2·10⁻⁹`) rejection. PASS.

All four gates PASS; `all_pass = true`, `first_failing_gate = null`, `results_sha256 = 37567447cc2e96a1b1c57404ed3e43b52d09c829f186293cc5f4f6122a03802d`. Deterministic three ways: in-process double-run byte-identical (`in_process_double_run: IDENTICAL`), a `--selfcheck` path printing `SELFCHECK: byte-identical`, and a separate-process re-invocation byte-identical. SEED = 20260717 (hardcoded module constant). Verifier file sha256 `58e4159d96c70fca6cfc7563f67d521c1e5d546e5a09f3a9979984b863b16a0c`.

## Grounding

Two pinned Wikipedia revisions (MediaWiki API `revisions.sha1` == self-computed `hashlib.sha1` of the raw wikitext — exact match for BOTH):

- **"Hypergeometric distribution"**, oldid 1364778061:
  `https://en.wikipedia.org/w/index.php?title=Hypergeometric_distribution&oldid=1364778061@faaf98ed0a35df30e3201d6b085b18a9da033e54` (30058 bytes), fetched 2026-07-21. API `sha1 = faaf98ed0a35df30e3201d6b085b18a9da033e54`; self-computed `hashlib.sha1(rawwikitext) = faaf98ed0a35df30e3201d6b085b18a9da033e54` — **match**.
- **"Byzantine fault"**, oldid 1362230504:
  `https://en.wikipedia.org/w/index.php?title=Byzantine_fault&oldid=1362230504@b3ad268d56c25ed9b5484ee0ad91ad4cceb8fa8c` (36223 bytes), fetched 2026-07-21. API `sha1 = b3ad268d56c25ed9b5484ee0ad91ad4cceb8fa8c`; self-computed `hashlib.sha1(rawwikitext) = b3ad268d56c25ed9b5484ee0ad91ad4cceb8fa8c` — **match**.

**Quoted** literally on the pinned revisions (grep count > 0):
- *Hypergeometric page* — the **pmf** `\frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}` verbatim (grep `\binom{K}{k}` = 2, `\binom{N}{n}` = 7); **"without replacement"** (= 8); **"population"** (= 8); "hypergeometric" (= 41); the variable definitions "`N` is the population size", "`K` is the number of success states in the population", "`n` is the number of draws".
- *Byzantine fault page* — **"Byzantine"** (= 34); the **BFT bound** stated as "there needs to be at least `3''F''+1` players" (grep `3''F''+1` = 1) and "`''n'' > 3''t''`" (grep `3''t''` = 1); **"one-third"** (= 2) and **"two-thirds"** (= 2) — the one-third safety threshold.

**Disclosed letter remap (honest seam).** The hypergeometric page's symbols are `(N` = population, `K` = successes, `n` = draws, `k` = hits`)`. My instance maps: fleet `N=64` → page `N`; Byzantine `B=21` → page `K` (successes); committee `K=16` → page `n` (draws); Byzantine-in-committee `i` → page `k`. **Same formula, disclosed re-lettering** — my symbol `K` (committee size) is the page's `n`, and my `B` is the page's `K`.

**Derived** firsthand (grep count 0 on the pinned raw wikitext): **"sortition"** (grep 0, both pages), **"committee"** as a sortition body (grep 0 on the hypergeometric page; grep 1 on the Byzantine page, but that hit is the "IEEE joint **committee** on Fundamental Concepts and Terminology" org name, not a sortition committee — disclosed), **"bft"** as a token (grep 0 on the hypergeometric page), the literal ASCII **"3f+1"** (grep 0 — the bound is present only in wiki-markup form `3''F''+1` / `''n'' > 3''t''`), **"upper tail"** as a phrase (grep 0 on the hypergeometric page — my label; the word "tail" appears 4×), and the whole application: the sortition-committee framing, the `N=64/B=21/K=16` instance (the raw digits `64`/`21` appear incidentally in refs/other parameters on both pages — grep `64`=3, `21`=5 on the hypergeometric page — **not** as my fleet instance; disclosed), `T = floor(K/3)+1`, the exact tail VALUE `296431911/685926212`, the with-replacement binomial foil, the MC estimator, every z-value, SEED, and the digest.

**Honest posture — disclosed seams.** (1) Nothing is oversold as a novel *theorem*: the hypergeometric distribution (pmf, without-replacement sampling, population framing) and the `n≥3f+1` BFT bound are textbook and quoted on the two pinned pages. The firsthand contribution is the **verification apparatus**: the exact `Fraction` committee-failure tail, its two independent cross-checks (Vandermonde + complement), the iid MC agreement, the Byzantine-identity invariance leg, the with-replacement-binomial falsification, and every z-value + the digest. (2) The hypergeometric page uses a **different letter convention** than my instance (my committee-size `K` is its draw-count `n`) — disclosed above, same formula. (3) The BFT bound is quoted in **markup form** (`3''F''+1`, `n > 3t`, "one-third"), not the literal ASCII "3f+1" I use in prose. (4) The with-replacement binomial foil (G4) is precisely the model the Condorcet jury head (P202) uses for a *different* question (independent voters) — here it is the WRONG model for without-replacement sortition and is rejected, which is what makes this identity distinct.

## Probe report (v0, self-adversarial)

**1. Is the core claim exactly true (not merely approximate)?** Yes, and the exactness is the point. The committee-failure probability is the hypergeometric upper tail `P = Σ_{i=6}^{16} C(21,i)C(43,16−i)/C(64,16)`, computed in exact `fractions.Fraction` as `296431911/685926212`. G1 cross-checks it two independent ways with zero residual: the full pmf sums to exactly 1 (Vandermonde), and the tail equals `1 − Σ_{i=0}^{5} pmf_i`. No floating-point error enters the value; the MC legs only *confirm* it.

**2. Could the numbers be an artefact of the sampler rather than the mathematics?** No. The exact tail (G1) is RNG-free — pure `Fraction` arithmetic fixed before any draw. The MC legs (G2, G3) sample committees by `random.sample` (genuine without-replacement draws) and land `z = −2.20` and `z2 = 0.69` on the exact `P`. A wrong sampler (e.g. with-replacement) would push these out of band — which is exactly what G4 demonstrates: the with-replacement binomial model is rejected at `z = −6.08` on the same data.

**3. What is the most plausible wrong belief this could be confused with?** That a globally-safe fleet (`n≥3f+1`) yields a safe sub-committee "for free", or equivalently that the committee's Byzantine count is Binomial(K, B/N) (iid, with replacement). Both are refuted: the fleet is exactly at the bound yet `P ≈ 0.43`, and the with-replacement binomial (`P_binom = 0.435210`) is pre-registered as G4 and rejected at `|z| = 6.08` — it overstates the tail because it drops the finite-population negative correlation of sortition.

**4. Is the verifier deterministic and self-checking?** Yes. `build_results()` is a pure function of SEED and the module constants; every float enters the hashed payload via a fixed `f"{x:.6f}"` / `f"{z:.4f}"` string and the exact tail as `str(Fraction)`, so no float-repr / wall-clock / PID / set-iteration instability enters. `main()` asserts an in-process double-run is byte-identical, `--selfcheck` prints "SELFCHECK: byte-identical", and two separate invocations reproduce the digest byte-for-byte. Whole-dict `results_sha256 = 37567447cc2e96a1b1c57404ed3e43b52d09c829f186293cc5f4f6122a03802d`.

**5. Does the grounding actually support the claim, or is it overstated?** Honest and tight, seams disclosed. The hypergeometric pmf + without-replacement framing and the `n≥3f+1` BFT bound are QUOTED verbatim on the two pinned revisions (API sha1 == self-computed sha1 for both) — so nothing is oversold as a novel theorem. Disclosed: the hypergeometric page's letter convention differs (my committee `K` is its draw-count `n`); the BFT bound is quoted as `3''F''+1`/`n > 3t`, not literal "3f+1"; "sortition"/"committee"(as a body)/"upper tail" are my labels (grep 0); the exact tail value, the instance, the binomial foil, the MC agreement, the invariance leg, every z-value, SEED, and the digest are the firsthand contribution.

**6. Does it scale / is it robust?** The apparatus is general: `pmf_exact(i)` and the tail sum take any `(N,B,K,T)`; the MC estimator takes any Byzantine set. The result is a property of the counts, not of a hard-coded value — G3 shows it depends only on `(N,B,K,T)` (a different Byzantine set of the same size lands `z2 = 0.69`). The natural sizing sweep (hold `B/N` fixed, vary `K`) is flagged as the follow-on.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers the single most plausible wrong model (with-replacement Binomial(K, B/N)) and refutes it at `|z_foil| = 6.08` on the same sample that accepts the hypergeometric `P` at `|z| = 2.20`. The two hypotheses are only `≈3.9σ` apart (the finite-population gap for these parameters is modest but real), so the decisive-yet-not-enormous separation is disclosed honestly rather than inflated.

**8. Any residual risk before ruling?** The MC legs are **iid** committee draws (independent `random.sample`), so the plain iid binomial SE is the honest one and batch means are deliberately *not* used — stated in the verifier docstring; the exact `Fraction` tail (G1) carries the claim RNG-free with two independent cross-checks (Vandermonde + complement). The G2 point (`z = −2.20`) sits within band but not far from it — a genuine statistical draw at this SEED, disclosed, not tuned. The hypergeometric distribution and the `n≥3f+1` bound are textbook (the two pinned pages) and cited as such; the exact committee-failure tail, its cross-checks, the MC agreement, the Byzantine-identity invariance, the binomial falsification, and every z-value + the digest are the firsthand contribution. The paired sim-lab VERDICT 266 reproduction is a separate coordinator-driven slice. No further blocker.

**Recommendation: sim-ready**
