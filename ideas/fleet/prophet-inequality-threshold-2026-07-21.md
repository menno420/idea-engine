# Prophet inequality — single-threshold 1/2 guarantee — for independent nonnegative X_1..X_n revealed in order, the single-threshold stopping rule ALG_τ that accepts the first X_i ≥ τ (else takes the last variable X_n), with τ = E[max_i X_i]/2, satisfies the EXACT guarantee E[ALG_τ] ≥ (1/2)·E[max_i X_i], and the constant 1/2 is optimal — a one-parameter family drives the online ratio down to 1/2 while greedy take-first collapses to 1/10. Headline instance (X_1 ∈ {1,0} each w.p. 1/2, X_2 ∈ {2,0} each w.p. 1/2): E[max] = 5/4, τ = 5/8, E[ALG_τ] = 1, ratio 4/5. Tight family (X_1 = 1 sure, X_2 = M w.p. 1/M): ratio 1/(2−1/M) → 1/2 as M → ∞ (2/3, 3/5, 4/7, 5/9 for M = 2,3,4,5). Teeth (1 sure then 10 sure): threshold ratio 1 vs greedy take-first 1/10. The exact Fraction enumeration (G1, guarantee holds on 6 instances, headline fractions reproduce, threshold-necessity take-first = 1/10), the seeded Monte-Carlo agreement (G2, |z| = 1.90, N = 200000), the positive-scale invariance of the ratio (G3, exact under λ ∈ {2,3,100,1/7}), and the falsification of the naive "gambler matches the prophet" foil (G4, rejected at z_foil = −160.27, tight family monotone toward 1/2) all PASS. An optimal-stopping / online-algorithms head over the fleet lane.

> **State:** sim-ready
> **Status:** sim-ready
> **📊 Model:** Claude Opus family · high effort · idea-proposal authoring

**Lane:** fleet · optimal stopping / online algorithms · prophet inequality single-threshold 1/2 guarantee
**Proposal:** 258 → Verdict 271 (+13 offset) — named by the `## PROPOSAL 258` block in `control/outbox.md`
**Verifier:** [`verify_258_prophet_inequality_threshold.py`](verify_258_prophet_inequality_threshold.py) · stdlib only (fractions, hashlib, itertools, json, math, random, sys) · SEED=20260721
**Digest:** `results_sha256 = 1c235e4991e2775e0c5813966f6cec313c296580c83a27195b287d9e4e3068fb`

## Statement — the claim exactly

For independent nonnegative random variables `X_1, …, X_n` revealed in order, define the single-threshold stopping rule `ALG_τ` that

> accepts the first `X_i ≥ τ` and stops; if no variable reaches `τ`, it takes the last variable `X_n`,

with the threshold set to half the expected prophet value,

> `τ = E[max_i X_i] / 2`.

The **prophet inequality** guarantees

> `E[ALG_τ]  ≥  (1/2) · E[max_i X_i]`,

and the constant `1/2` is **optimal**: no online rule can guarantee a larger fraction of `E[max]` against every product of nonnegative distributions. A one-parameter family drives the achievable ratio down to `1/2`, and the greedy "take-first" rule can do as badly as `1/10` on an instance where the threshold rule stays at ratio `1`.

## Assumptions

- **Independence** — the `X_i` are mutually independent (joint law is the product of the marginals).
- **Nonnegativity** — `X_i ≥ 0` (negative values may be clamped to 0 without changing the outcome).
- **Known distributions** — the marginals `D_i` are known in advance; only the realised values arrive online.
- **Fixed order** — the reveal order `X_1, …, X_n` is fixed (not the free-order / IID prophet-secretary variants).
- **Single threshold** — one fixed number `τ = E[max]/2`, computed from the known distributions, is used for every step (no per-step or adaptive threshold).

## Exact closed form / headline values

Exact `fractions.Fraction`, no float in the guarantee.

| instance | `E[max]` | `τ = E[max]/2` | `E[ALG_τ]` | ratio `E[ALG_τ]/E[max]` | guarantee ≥ 1/2 |
|---|---|---|---|---|---|
| generic (`X_1∈{1,0}` ½/½, `X_2∈{2,0}` ½/½) | `5/4` | `5/8` | `1` | **`4/5`** | ✓ |
| tight `M=2` (`X_1=1`, `X_2∈{2,0}` ½/½) | `3/2` | `3/4` | `1` | `2/3` | ✓ |
| tight `M=3` | `5/3` | `5/6` | `1` | `3/5` | ✓ |
| tight `M=4` | `7/4` | `7/8` | `1` | **`4/7`** | ✓ |
| tight `M=5` | `9/5` | `9/10` | `1` | `5/9` | ✓ |
| teeth (`1` sure then `10` sure) | `10` | `5` | `10` | `1` | ✓ |

- **Generic instance.** `X_1 = 1` or `0` each with probability `1/2`; `X_2 = 2` or `0` each with probability `1/2`. `E[max] = 5/4`, so `τ = 5/8`. `ALG_τ` accepts `X_1` iff `X_1 = 1 ≥ 5/8`, else takes `X_2`; exact `E[ALG_τ] = 1`, ratio `4/5 > 1/2`.
- **Tight family.** `X_1 = 1` (sure), `X_2 = M` with probability `1/M` and `0` otherwise. `E[max] = 1 + (M−1)/M = (2M−1)/M`, `E[ALG_τ] = 1`, ratio `M/(2M−1) = 1/(2 − 1/M)` — a decreasing sequence `2/3, 3/5, 4/7, 5/9, …` converging **down to `1/2`**. This family is exactly why `1/2` cannot be improved.
- **Teeth instance (threshold necessity).** `X_1 = 1` (sure), then `X_2 = 10` (sure). `E[max] = 10`, `τ = 5`; the threshold rule skips `X_1 = 1 < 5` and takes `X_2 = 10`, ratio `1`. The greedy **take-first** policy grabs `X_1 = 1` for ratio `1/10 < 1/2` — a threshold is genuinely necessary.

## Four-gate plan — each in its own direction

- **G1 — EXACT (`fractions.Fraction`, zero tolerance).** Exact product-support enumeration of `E[max]`, `E[ALG_τ]`, and the ratio for all six instances above; the guarantee `E[ALG_τ] ≥ E[max]/2` holds on every one (`guarantee_holds` on all 6). The headline fractions are asserted exactly — generic `(5/4, 1, 4/5)`, tight `M=4` `(7/4, 1, 4/7)`, teeth `(10, 10, 1)` — and the threshold-necessity fact `take-first ratio = 1/10 < 1/2` on the teeth instance. Reported **exact — z = n/a**. `pass = true`.
- **G2 — MC AGREEMENT (`|z| < 3`).** `N = 200000` seeded iid Monte-Carlo draws of the generic instance (`random.Random(SEED)`, all variables sampled in order), running the exact same `ALG_τ` rule; sample mean `0.9969950000` estimates the exact `E[ALG_τ] = 1`, plain iid `SE = 0.0015786481`, `z = −1.903527`, `|z| < 3` [Z_ACCEPT = 3.0]. iid draws → the plain iid SE is honest (no batch means / thinning; stated in the verifier docstring). `pass = true`.
- **G3 — INVARIANCE (positive scale, own direction, EXACT).** The ratio `E[ALG_τ]/E[max]` is invariant under `X → λ·X` for every `λ > 0`: for `λ ∈ {2, 3, 100, 1/7}` the generic-instance ratio stays exactly `4/5` via `Fraction` (`τ` scales with the values, so acceptance decisions are unchanged). Genuine content — the guarantee is a property of the shape of the distributions, not their units. Reported **exact — z = n/a**. `pass = true`.
- **G4 — FALSIFIABILITY (reject at large `|z|`, own direction, SAME MC sample as G2).** Pre-registered naive foil: *"the gambler matches the prophet"*, i.e. `E[ALG_τ] == E[max] = 1.25`. On the same `N = 200000` sample the mean `0.997` is rejected against that target at `z_foil = −160.266876`, `|z_foil| > 6` → REJECTED, while the same sample AGREES with the true `E[ALG_τ] = 1` at `z = −1.90`. Corroboration: the tight family ratios `2/3, 3/5, 4/7, 5/9` are **monotone decreasing toward `1/2`** and stay strictly above `1/2` (`r_5 < r_2` and both `> 1/2`), confirming `1/2` is approached but not improvable. `pass = true`.

All four gates PASS; `all_gates_pass = true`, `first_failing_gate = null`, `results_sha256 = 1c235e4991e2775e0c5813966f6cec313c296580c83a27195b287d9e4e3068fb`. Deterministic three ways: in-process double-run byte-identical, a `--selfcheck` path printing `selfcheck OK <same hash>`, and a separate-process re-invocation byte-identical. SEED = 20260721 (hardcoded module constant). Verifier file sha256 `e3a0f0a271920b0ac91c062a26469515c2f2edefac5dbdebfbf1ca37bbecf1c9`.

## Grounding

Pinned Wikipedia revision (MediaWiki API `revisions.sha1` == self-computed `hashlib.sha1` of the raw wikitext — exact match):

- **"Prophet inequality"**, oldid 1329732914:
  `https://en.wikipedia.org/w/index.php?title=Prophet_inequality&oldid=1329732914@2630c796b06718744230a4e60e007f1bda1d9edb`, fetched 2026-07-21. API `sha1 = 2630c796b06718744230a4e60e007f1bda1d9edb`; self-computed `hashlib.sha1(rawwikitext)` — **match**, raw wikitext length **8483 bytes**. (The article exists and is not a redirect.)

**Quoted** literally on the pinned revision (grep count > 0, both directions):
- the name "prophet inequality" (grep 6) and the framing "optimal stopping" (grep 3, incl. the short description "Bound on optimal stopping in random sequences").
- the **1/2 guarantee** — verbatim "an online algorithm … whose expected value is at least half that of the prophet: `\tfrac12 E[max_i X_i]`" (`half` grep 1, `\tfrac12` grep 4).
- the **single-threshold rule at `τ = E[max]/2`** — verbatim "A different threshold, `τ = \tfrac12 E[max_i X_i]`, also achieves at least this same expected value" and the general "threshold algorithm that sets a parameter `τ`" (`threshold` grep 5; the median-threshold `p = 1/2` construction is also on-page).
- **optimality** — "No algorithm can achieve a greater expected value for all distributions of inputs" (prose), with the "tight" form (grep 1) credited to Garling.
- the originators **Krengel** (grep 2), **Sucheston** (grep 2), **Garling** (grep 1), Krengel–Sucheston 1978.

**Derived** firsthand (grep count 0 on the pinned raw wikitext, both directions): the literal string `1/2` (0), `one-half` (0), the exact phrases `best possible` (0) / `cannot be improved` (0); the six enumerated instances and every rational in the reference table — `5/4, 4/5, 7/4, 4/7, 1/10` (all grep 0); the numeric application of `τ = E[max]/2` to each instance; the greedy **take-first** foil and its `1/10` ratio (`take-first` 0, `greedy` 0); the seeded Monte-Carlo estimator and every z-value (`Monte` 0); the `fractions.Fraction` enumeration (`Fraction` 0); the positive-scale-invariance leg; SEED `20260721` (0); and the results digest (`sha256` 0).

**Honest posture — disclosed seams.** The pinned article is RICH for this head: the single-threshold rule `τ = \tfrac12 E[max_i X_i]`, the `1/2` guarantee, and its optimality ("No algorithm can achieve a greater expected value") are all **QUOTED verbatim** — so nothing here is oversold as a novel theorem. The prophet inequality is textbook (Krengel–Sucheston 1978; Garling's tight form; the pinned page), cited as such. The firsthand contribution is the **verification apparatus**: the exact `Fraction` enumeration of `E[max]`, `E[ALG_τ]`, and the ratio on six concrete instances (with the "take the last variable if none accepted" tie-break made explicit and computed), the tight family exhibiting the monotone approach to `1/2`, the teeth instance quantifying threshold-necessity (`take-first = 1/10`), the seeded Monte-Carlo agreement, the positive-scale-invariance leg, the "gambler matches the prophet" falsification, and every z-value + SEED + the digest. One convention note: the page states the guarantee for the accept/stop process with value `0` if nothing is accepted; the verifier's tie-break "take the last variable `X_n` if none reaches `τ`" only ever helps the algorithm (it can add value, never subtract), so the `≥ 1/2` guarantee it checks is at least as strong as the on-page statement — disclosed.

## Reproduction

- **Verifier:** `ideas/fleet/verify_258_prophet_inequality_threshold.py` — stdlib only (`fractions, hashlib, itertools, json, math, random, sys`), no network, `SEED = 20260721` hardcoded.
- **File sha256:** `e3a0f0a271920b0ac91c062a26469515c2f2edefac5dbdebfbf1ca37bbecf1c9`.
- **Results digest:** `results_sha256 = 1c235e4991e2775e0c5813966f6cec313c296580c83a27195b287d9e4e3068fb`.
- **Command:** `python3 verify_258_prophet_inequality_threshold.py` prints the full results JSON and the digest.
- **Determinism (three checks):** in-process double-run byte-identical; `python3 verify_258_prophet_inequality_threshold.py --selfcheck` prints `selfcheck OK <same digest>`; a separate-process re-invocation reproduces the same `results_sha256` byte-for-byte. The hashed payload is a pure function of SEED and the module constants — exact ratios enter as `str(Fraction)` and every float via a fixed `"%.6f"` / `"%.10f"` format, so no float-repr / wall-clock / PID / set-iteration instability enters.

## Probe report (v0, self-adversarial)

**1. Is the core claim exactly true (not merely approximate)?** Yes. `E[max]`, `E[ALG_τ]`, and the ratio are computed in exact `fractions.Fraction` by enumerating the full product support of the independent variables. G1 checks the guarantee `E[ALG_τ] ≥ E[max]/2` on six concrete instances and asserts the headline fractions exactly — generic `(5/4, 1, 4/5)`, tight `M=4` `(7/4, 1, 4/7)`, teeth `(10, 10, 1)`. No floating-point error enters the guarantee; the MC leg only *confirms* the generic value.

**2. Could the numbers be an artefact of the sampler rather than the mathematics?** No. The guarantee (G1) and the scale-invariance leg (G3) are RNG-free — pure `Fraction` arithmetic fixed before any draw. The MC leg (G2) samples the generic instance and lands `z = −1.90` on the exact `E[ALG_τ] = 1`; a wrong policy value would push the sample out of band, which is exactly what G4 demonstrates (the "gambler matches the prophet" target is rejected at `z_foil = −160.27` on the same sample).

**3. What is the most plausible wrong belief this could be confused with?** That the gambler can *match* the prophet (`E[ALG_τ] = E[max]`), i.e. that online play loses nothing. It cannot: `1/2` is the optimal constant, and the tight family `X_1 = 1`, `X_2 = M` w.p. `1/M` drives the ratio down to `1/2` (`2/3, 3/5, 4/7, 5/9, …`). G4 pre-registers the "match the prophet" foil and rejects it at `|z_foil| = 160.27`, while the tight family shows the monotone approach to `1/2`. A secondary confusion — "just take the first good-looking offer" (greedy take-first) — is refuted by the teeth instance, where take-first is only `1/10`.

**4. Is the verifier deterministic and self-checking?** Yes. `compute()` is a pure function of SEED and the module constants; exact ratios enter the hashed payload as `str(Fraction)` (`"%d/%d"`) and every float via a fixed `"%.6f"` / `"%.10f"` string, so no float-repr / wall-clock / PID / set-iteration instability enters. `main()` runs an in-process double-run, `--selfcheck` prints `selfcheck OK <digest>`, and two separate invocations reproduce the digest byte-for-byte. `results_sha256 = 1c235e4991e2775e0c5813966f6cec313c296580c83a27195b287d9e4e3068fb`.

**5. Does the grounding actually support the claim, or is it overstated?** Honest and tight, seams disclosed. The pinned page QUOTES the single-threshold rule `τ = \tfrac12 E[max_i X_i]`, the `1/2` guarantee ("at least half that of the prophet"), and its optimality ("No algorithm can achieve a greater expected value for all distributions") verbatim — so nothing is oversold as a novel theorem; the prophet inequality is textbook (Krengel–Sucheston 1978; Garling's tight form) and cited as such. The firsthand contribution is the exact-`Fraction` enumeration apparatus, the tight-family optimality exhibit, the take-first threshold-necessity (`1/10`), the MC agreement, the scale-invariance leg, the falsification, every z-value, SEED, and the digest — all grep-0 on the pinned wikitext.

**6. Does it scale / is it robust?** The apparatus is general: `emax`, `ealg`, and the ratio take any product of finite-support nonnegative marginals. G1 exercises it across the generic instance and the tight family `M = 2..5`; G3 shows the ratio is exactly invariant under any positive rescale `λ ∈ {2, 3, 100, 1/7}`. The tight family is the natural sweep — `1/(2 − 1/M)` traces the approach to `1/2` — and is flagged as the follow-on for larger `M`.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers the single most plausible wrong belief (the gambler matches the prophet, `E[ALG_τ] = E[max] = 1.25`) and refutes it at `z_foil = −160.27` (`|z_foil| > 6`) on the same `N = 200000` sample that accepts the true value at `z = −1.90`. The tight family independently confirms `1/2` is approached but not improvable (`r_5 < r_2`, both `> 1/2`).

**8. Any residual risk before ruling?** The MC leg is iid draws (all variables sampled independently per trial via `random.Random(SEED)`), so the plain iid SE is the honest one and batch means are deliberately not used — stated in the verifier docstring; the exact `Fraction` guarantee (G1) and the exact invariance (G3) carry the claim RNG-free. Disclosed convention seam: the verifier's tie-break "take the last variable `X_n` if none reaches `τ`" only ever adds value versus the page's "value 0 if nothing accepted", so the `≥ 1/2` guarantee it checks is at least as strong as the on-page statement. The paired sim-lab VERDICT 271 reproduction is a separate coordinator-driven slice. No further blocker.

**Recommendation: sim-ready**
