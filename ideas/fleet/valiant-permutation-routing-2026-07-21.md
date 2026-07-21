# Valiant two-phase (random-intermediate) oblivious routing on the hypercube Q_n — the exact phase-1 backbone. On Q_n (N = 2^n nodes), Valiant's scheme routes each packet first to a UNIFORMLY RANDOM intermediate node d, then on to its true destination, by left-to-right bit-fixing. Phase-1 route length L = Hamming distance H(s, d) is distributed EXACTLY Binomial(n, 1/2): pmf p_k = C(n,k)/2^n, so E[L] = n/2, Var[L] = n/4, and it is INDEPENDENT of the source s — this source-invariance is exactly why the random intermediate defeats adversarial permutations. The probability generating function is G(x) = E[x^L] = ((1+x)/2)^n exactly, and the average congestion over the N·n directed edges = E[total edge-crossings]/(N·n) = (N·(n/2))/(N·n) = 1/2 exactly. These exact expectations are the backbone of Valiant's O(n)=O(log N) w.h.p. delivery result (the Chernoff tail rests on E[L]=n/2). A routing/load-balancing head distinct from every shipped one.

> **State:** sim-ready
> **Status:** sim-ready
> **📊 Model:** Claude Opus · high · idea/planning

**Lane:** fleet · randomized parallel routing / Valiant two-phase random-intermediate oblivious routing on the hypercube
**Proposal:** 257 → Verdict 270 (+13 offset) — named by the `## PROPOSAL 257` block in `control/outbox.md`
**Verifier:** [`verify_257_valiant_permutation_routing.py`](verify_257_valiant_permutation_routing.py) · stdlib only (json, hashlib, math, random, fractions, sys) · SEED=20260717
**Digest:** `results_sha256 = fd0d970057a36cfb2f2ad3dfe200acd09d3ce303d8c1eb37e88f6d3330fa759f`

## What this proposal does

Adds a fleet PROPOSAL establishing the **exact phase-1 backbone of Valiant's two-phase (random-intermediate) oblivious routing** on the hypercube `Q_n` (`N = 2^n` nodes):

> Route each packet first to a **uniformly random intermediate** node `d`, then on to its true destination, by left-to-right bit-fixing. The phase-1 route length `L = H(s, d)` (Hamming distance from source `s` to `d`) is **exactly** `Binomial(n, 1/2)`: `p_k = C(n,k)/2^n`, so `E[L] = n/2`, `Var[L] = n/4`, **independent of the source `s`** — and the average congestion over the `N·n` directed edges is exactly `1/2`.

Because `d` is uniform on `{0,1}^n` and independent of `s`, the XOR `s^d` is uniform on `{0,1}^n`, so `L = popcount(s^d) ~ Binomial(n, 1/2)` regardless of `s`. That **source-invariance** is precisely why Valiant's random intermediate defeats an adversarial permutation: no adversary can inflate phase-1 length. The **probability generating function** is `G(x) = E[x^L] = ((1+x)/2)^n` exactly (from `Σ_k C(n,k) x^k = (1+x)^n`). The **average edge congestion** over the `N·n` directed edges of `Q_n` is `E[total crossings]/(N·n) = (N·(n/2))/(N·n) = 1/2`. These exact expectations are the backbone of Valiant's `O(n) = O(log N)` w.h.p. delivery result — the Chernoff tail on delivery time rests on `E[L] = n/2`.

**Headline numbers (n = 12, N = 4096, N_mc = 400000).** Exact backbone `checked = 75`, `mismatches = 0`: PGF identity holds over 5 rational `x` × 5 values of `n`, `E[L] = 6`, `Var[L] = 3`, pmf normalization + symmetry, congestion `= 1/2`. MC mean route length `5.997945` vs `E[L] = 6.0`, `z = −0.749864`; derived edge-congestion estimate `0.499829` vs `1/2`, `z = −0.749864`. Source-permutation invariance (bit-reversal adversary): `adv_mean = 6.002165`, `adv_z = 0.79122`. `n`-invariance across `n ∈ {8, 10, 12, 14}`: `z = −0.215486, −0.112088, 1.232978, 2.686444` (all `|z| < 3`, `mean/n → 1/2`). Foil "route length `= n = 12`" rejected at `z_foil = −2190.134211`; foil "congestion `= 1.0`" rejected at `z = −2190.134211`; same sample accepts the true mean at `z = −0.749864`.

**Distinctness.** This is a **randomized-routing / load-balancing** head about the **phase-1 route-length distribution, edge congestion, and source-invariance** on the hypercube — NOT a max-load object. `valiant`, `random-intermediate`, `two-phase` are **grep-0 as heads** across both repos (`control/outbox.md`, `ideas/`, `sims/`). It is orthogonal to every shipped routing/load-balancing head: balls-into-bins max-load (P225), derangement / no-home-task (P229), power-of-two-choices (two shipped heads), consistent-hashing. The distinctive content is the exact `Binomial(n,1/2)` phase-1 route-length backbone + the `((1+x)/2)^n` PGF + the `1/2` edge-congestion identity + the source-permutation invariance that underpins Valiant's `O(log N)` guarantee.

## Method

Exact rational backbone first, Monte-Carlo agreement + invariance + falsifiability second.

**Exact backbone (`fractions.Fraction`, no floats).** `pmf(n)` builds the exact `Binomial(n,1/2)` pmf `p_k = C(n,k)/2^n`. G1 verifies, at zero tolerance: (a) the **PGF identity** `Σ_k C(n,k) x^k = (1+x)^n`, hence `G(x) = Σ_k p_k x^k = ((1+x)/2)^n`, checked at rational `x ∈ {1, 2, 1/2, 3, −1/3}` for `n ∈ {1, 2, 3, 8, 12}`; (b) `E[L] = Σ_k k p_k = n/2 = G'(1)`; (c) `Var[L] = Σ_k k² p_k − E[L]² = n/4 = G''(1) + G'(1) − G'(1)²` (with `G''(1) = n(n−1)/4`); (d) the pmf sums to `1` and is symmetric `p_k = p_{n−k}`; (e) the average directed-edge congestion `(N·(n/2))/(N·n) = 1/2` with `N = 2^n`. `checked = 75`, `mismatches = 0`.

**Monte-Carlo phase-1 route length.** `sample_route_lengths(rng, n, draws)` draws `draws` uniform pairs `(s, d)` in `{0,1}^n` (`rng.getrandbits(n)`) and forms `L = popcount(s^d)`, an iid `Binomial(n,1/2)` draw. Because the draws are **independent**, the plain iid standard error `SE = sqrt(sample_var / N_mc)` is the honest one — no batch-means / thinning is used (that machinery is only for autocorrelated sample paths; stated in the verifier docstring). `random.seed(SEED)` is re-seeded at the START of each Monte-Carlo gate so gate order cannot perturb the payload. Every MC-derived float enters the hashed payload rounded to 6 decimals; every exact rational as `str(Fraction)`.

## Exact reference

Exact `Binomial(n,1/2)` phase-1 backbone (verified in `fractions.Fraction`, `checked = 75`, `mismatches = 0`):

| quantity | closed form | at n = 12 |
|---|---|---|
| pmf | `p_k = C(n,k)/2^n` | `p_k = C(12,k)/4096` |
| PGF | `G(x) = ((1+x)/2)^n` | `((1+x)/2)^12` |
| mean route length | `E[L] = n/2` | `6` |
| variance | `Var[L] = n/4` | `3` |
| avg directed-edge congestion | `(N·(n/2))/(N·n) = 1/2` | `1/2` |
| source dependence | none (uniform intermediate) | source-invariant |

The PGF identity, the two moments (via the pmf AND via `G'(1)`, `G''(1)`), the pmf normalization/symmetry, and the congestion identity are independent routes that agree exactly — the teeth of G1.

## Four gates (each in its own direction)

- **G1 — EXACT (`fractions.Fraction`, zero tolerance).** (a) PGF identity `Σ_k C(n,k) x^k = (1+x)^n` ⇒ `G(x) = ((1+x)/2)^n` at 5 rational `x` × 5 values of `n`; (b) `E[L] = n/2` via the pmf and via `G'(1)`; (c) `Var[L] = n/4` via the pmf and via `G''(1)+G'(1)−G'(1)²`; (d) pmf sums to `1` and `p_k = p_{n−k}`; (e) average congestion `(N·(n/2))/(N·n) = 1/2`. `checked = 75`, `mismatches = 0`. `z` not applicable → reported `"exact"`. PASS.
- **G2 — Monte-Carlo agreement (`|z| < 3`).** `N_mc = 400000` uniform pairs `(s, d)` at `n = 12`, `L = popcount(s^d)`. Empirical `mean_len = 5.997945` vs `E[L] = 6.0`, `SE = 0.00274`, `z = −0.749864` `[Z_ACCEPT = 3.0]`; iid draws → plain iid SE is honest. Derived edge-congestion estimate `mean/n = 0.499829` vs `1/2`, `z_congestion = −0.749864`. PASS.
- **G3 — robustness / invariance (own direction).** (a) **Source-permutation invariance** (Valiant's core): re-estimate the mean route length with sources taken from the **bit-reversal permutation** of the node index (an adversarial, non-uniform source ordering) paired with uniform-random intermediates — `adv_mean = 6.002165`, `adv_z = 0.79122` `< 3`. The adversary cannot inflate phase-1 length because the intermediate is uniform and independent of the source. (b) **n-invariance**: `E[L]/n = 1/2` across `n ∈ {8, 10, 12, 14}`, `z = −0.215486, −0.112088, 1.232978, 2.686444` (all `|z| < 3`, `mean/n → 1/2`). PASS.
- **G4 — falsifiability (reject at large `|z|`, own direction, SAME sample as G2).** Primary pre-registered naive foil: *"every packet crosses all `n` dimensions, so route length `= n = 12` / edge congestion `= 1`"*, predicted mean `12.0` — REJECTED at `z_foil = −2190.134211`, `|z_foil| ≫ 50` `[Z_REJECT = 50.0]`, on the SAME sample that accepts the true mean at `z = −0.749864`. Secondary foil: *"route length `= n/2` but each edge is traversed deterministically so congestion `= 1.0` not `1/2`"* — congestion `= 1.0` rejected vs the measured `0.499829` at `z = −2190.134211`. PASS.

All four gates PASS; `all_pass = true`, `first_failing_gate = null`, `results_sha256 = fd0d970057a36cfb2f2ad3dfe200acd09d3ce303d8c1eb37e88f6d3330fa759f`. Deterministic three ways: in-process double-run byte-identical (`in_process_double_run: IDENTICAL`), a `--selfcheck` path printing `SELFCHECK: byte-identical`, and a separate-process re-invocation byte-identical. SEED = 20260717 (hardcoded module constant). Verifier file sha256 `7e204af1e5ee84e8c89fccc975d6e3ffa3440571e5d049f16c5af3faf819c7d4`.

## Grounding

One pinned Wikipedia revision (MediaWiki API `revisions.sha1` == self-computed `hashlib.sha1` of the raw wikitext — exact match):

- **"STC104"**, oldid 1317632376:
  `https://en.wikipedia.org/w/index.php?title=STC104&oldid=1317632376@9945529d84c498378e412e0d6dcd464fec499fd2` (9688 bytes), fetched 2026-07-21. API `sha1 = 9945529d84c498378e412e0d6dcd464fec499fd2`; self-computed `hashlib.sha1(rawwikitext) = 9945529d84c498378e412e0d6dcd464fec499fd2` — **match**. (The STC104 is the INMOS/T9000-family packet router that implemented Valiant's two-phase randomized routing; the article names the scheme and cites Valiant 1982.)

**Quoted** literally on the pinned revision (grep count > 0):
- **"two-phase randomized routing"** (grep = 2) — the scheme's name.
- **"randomly chosen intermediate node"** (grep = 1) and **"before routing it to the destination"** (grep = 1) — the two-phase random-intermediate structure verbatim: *"routing packets to a randomly chosen intermediate node, before routing it to the destination"*.
- **"random destination"** (grep = 1) — *"prepend a header with a random destination"*, the implementation of the random intermediate.
- **"average worst case"** (grep = 1) — *"reduce all traffic to an average worst case with predictable latency and bandwidth"*, the load-balancing effect.
- **"Valiant"** (grep = 2), the citation **"A scheme for fast parallel communication"** (grep = 1, Valiant, SIAM J. Comput. 11(2), 1982), and **"hypercube"** (grep = 1, in the supported network topologies).

**Derived** firsthand (grep count 0 on the pinned raw wikitext): the phase-1 route-length identity `L = popcount(s^d) ~ Binomial(n, 1/2)` and its pmf `C(n,k)/2^n` (grep `Binomial` = 0); `E[L] = n/2`, `Var[L] = n/4` (grep `n/2` = 0); the PGF `G(x) = ((1+x)/2)^n`; the average directed-edge **congestion** `= 1/2` (grep `congestion` = 0); the **source-invariance** and the bit-reversal-adversary check (grep `Hamming` = 0); the `O(log N)` / `O(n)` delivery claim (grep `O(log` = 0, `O(n` = 0 — attributed to the cited Valiant 1982 paper but NOT stated on this page); every z-value and the two foils; SEED `20260717` (grep = 0); the results digest (grep `sha256` = 0).

**Honest posture — disclosed seams.** (1) The pinned STC104 article is an **engineering** description: it names *"two-phase randomized routing"*, the *"randomly chosen intermediate node"* mechanism, cites *Valiant 1982*, and lists the *hypercube* as a supported topology — so the **scheme, the random-intermediate idea, and Valiant's attribution are quoted verbatim**. It does **NOT** state the route-length distribution, the moments, the PGF, the edge-congestion value, or the `O(log N)` bound; those are the **firsthand derivation** here (`Binomial`, `n/2`, `congestion`, `Hamming`, `O(log` are all grep-0 on the page). (2) In particular the `O(log N)` w.h.p. guarantee is Valiant's well-known result (attributed to the cited 1982 paper) but is **not** quoted on this page — disclosed. (3) The bit-reversal adversary, the `n`-invariance sweep, every z-value, the two foils, SEED, and the digest are mine. Nothing is oversold as novel: Valiant's two-phase randomized routing is textbook (Valiant 1982; Valiant–Brebner 1981; the pinned STC104 page), cited as such; the firsthand contribution is the exact `Binomial(n,1/2)` phase-1 backbone (pmf, PGF, moments, congestion) verified end-to-end in `fractions.Fraction`, the MC agreement, the source-permutation + `n`-invariance legs, and the `route-length = n` / `congestion = 1` falsifications.

## Probe report (v0, self-adversarial)

**1. Is the core claim exactly true (not merely approximate)?** Yes, exactly. `d` uniform on `{0,1}^n` and independent of `s` ⇒ `s^d` uniform on `{0,1}^n` ⇒ `L = popcount(s^d) ~ Binomial(n, 1/2)` exactly, so `p_k = C(n,k)/2^n`, `E[L] = n/2`, `Var[L] = n/4`. G1 verifies the PGF identity, both moments (via the pmf AND via `G'(1)`, `G''(1)`), pmf normalization/symmetry, and the congestion identity in exact `fractions.Fraction` with `mismatches = 0` (`checked = 75`). The `1/2` edge-congestion is the exact ratio `(N·(n/2))/(N·n)`.

**2. Could the numbers be an artefact of the sampler rather than the mathematics?** No. The exact backbone (G1) is RNG-free `Fraction` arithmetic fixed before any draw. The Monte-Carlo legs (G2, G3) only *confirm* the analytic values: G2 lands `z = −0.749864` from `E[L] = 6.0`, the adversarial-source leg lands `z = 0.79122`, and the four `n`-invariance instances all land `|z| < 3`. A wrong sampler would push these out of band, not fake agreement across the exact identities plus four independent MC instances.

**3. What is the most plausible wrong belief this could be confused with?** That every packet crosses all `n` dimensions (route length `= n`, congestion `= 1`) — the "worst-case deterministic path" intuition. It predicts mean `12.0`. This is pre-registered as G4 and refuted: on the same `N = 400000` sample that accepts the true mean at `z = −0.749864`, the foil sits `z_foil = −2190.13` away, `|z_foil| ≫ 50`; the paired "congestion `= 1.0`" foil is refuted at `z = −2190.13`.

**4. Is the verifier deterministic and self-checking?** Yes. `build_results()` is a pure function of SEED and the module constants; `random.seed(SEED)` is re-seeded at the START of each MC gate so gate order cannot perturb the payload; every MC-derived float enters the payload via `round(x, 6)` and every exact ratio as `str(Fraction)`, so no float-repr / wall-clock / PID / set-iteration instability enters. `main()` asserts an in-process double-run is byte-identical, `--selfcheck` prints "SELFCHECK: byte-identical", and two separate invocations reproduce the digest byte-for-byte. Whole-dict `results_sha256 = fd0d970057a36cfb2f2ad3dfe200acd09d3ce303d8c1eb37e88f6d3330fa759f`.

**5. Does the grounding actually support the claim, or is it overstated?** Honest and tight, seams disclosed. The pinned STC104 page quotes the scheme name, the random-intermediate mechanism, Valiant's attribution, and the hypercube topology — but NOT the route-length distribution, the moments, the PGF, the congestion value, or the `O(log N)` bound (all grep-0). So the firsthand contribution is exactly the exact `Binomial(n,1/2)` backbone + the MC/invariance/falsifiability apparatus, and this is disclosed rather than dressed up as quoted.

**6. Does it scale / is it robust?** The apparatus is general: `pmf`, the PGF check, and both moments take any `n`; `sample_route_lengths` takes any `n` and `draws`; the `n`-invariance sweep runs `n ∈ {8, 10, 12, 14}` and the adversarial leg any `n`. G1 exercises 75 exact checks; G3 uses an adversarial-source estimator plus four independent `n`-instances. The result is a property of the phase-1 route-length distribution, not a hard-coded value.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers the single most plausible confusion (route length `= n` / congestion `= 1`) and refutes it at `|z_foil| = 2190.13` on the same sample that accepts the true mean at `z = −0.749864`. A wrong distribution would fail either the exact backbone (G1, `mismatches > 0`) or push the G2/G3 z's far out of band while the foil moved into band — the gates read in opposite directions.

**8. Any residual risk before ruling?** The Monte-Carlo legs are **iid** draws (not autocorrelated sample paths), so the plain iid SE is the honest one and batch means are deliberately *not* used; the exact `Fraction` backbone (G1) carries the claim RNG-free with independent routes (pmf vs `G'(1)`/`G''(1)` vs congestion identity). Valiant's two-phase randomized routing is textbook (Valiant 1982; the pinned STC104 page) and cited as such; the exact backbone, the MC agreement, the source-permutation + `n`-invariance legs, the falsifications, and every z-value + the digest are the firsthand contribution. The paired sim-lab VERDICT 270 reproduction is a separate coordinator-driven slice. No further blocker.

**Recommendation: sim-ready**
