# Myerson's optimal reserve for iid Uniform[0,1] bidders is r* = 1/2 for every n, capturing an exact 1/12 of extra revenue at n = 2

> **State:** sim-ready
> **Status:** proposed as PROPOSAL 226 -> VERDICT 239 (+13 offset); verifier landed in sim-lab PR #320 (squash 71365ae).
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Regular_distribution_(economics)&oldid=1304906615@45d380f12e80c8a69f221ff09bd3eb34b44cfe05 · fetched 2026-07-20

**Verifier:** `sim-lab/sims/verdict-239-myerson-reserve/myerson-optimal-reserve.py` — Python 3 stdlib only, SEED=20260717, Z_GATE=3.0, N_MC=200000. **Disclosed digest** `results_sha256: b125afaf186e8d2430783b89af1a877193a65752db77884458485ced7ec918f0`.

## Head

Sell one indivisible item to `n` bidders whose private values are iid Uniform[0,1]. Myerson's optimal-auction theory allocates to the bidder with the highest **virtual value** `psi(v) = v - (1-F(v))/f(v)` when it is non-negative, and charges the threshold. For Uniform[0,1], `F(v)=v` and `f(v)=1`, so `psi(v) = 2v - 1`, zero at `v = 1/2`. Hence the optimal mechanism is a second-price auction with a **reserve r* = 1/2, independent of n**, and its expected revenue is the exact rational

`R*(n) = 2n/(n+1) - 1 + (1/2)^n / (n+1)`.

At `n = 2` this is `R*(2) = 5/12`, versus the no-reserve second-price revenue `1/3` — the reserve captures an extra **1/12**.

## Why it matters

The reserve price is the seller's single most consequential lever, and the counter-intuitive result is that the optimal reserve does **not** depend on how many bidders arrive: two or two hundred, `r* = 1/2` for Uniform[0,1]. It is also strictly positive — "just run a Vickrey auction with no floor" leaves an exact `1/12` on the table at `n = 2`. This is the cleanest closed-form instance of mechanism design's central lesson: a revenue-maximizer optimizes virtual values, not values.

## Exact core identities

- Virtual value `psi(v) = v - (1-v)/1 = 2v - 1`; `psi(1/2) = 0` (exact).
- Optimal revenue = expected positive virtual value of the winner: `R*(n) = integral_{1/2}^{1} (2x-1) n x^{n-1} dx = 2n/(n+1) - 1 + (1/2)^n/(n+1)`.
- Exact fractions: `R*(1)=1/4`, `R*(2)=5/12`, `R*(3)=17/32`, `R*(4)=49/80`, `R*(5)=43/64`.
- No-reserve second-price revenue `R(n,0) = (n-1)/(n+1)`; at `n=2` that is `1/3`, so the reserve gain at `n=2` is `5/12 - 1/3 = 1/12`.
- Three independent exact routes to `R*(n)` agree for `n in {1,2,3,4,5}`: the closed form, the virtual-surplus integral `integral_r^1 (2x-1) n x^{n-1} dx`, and a first-principles sell-decomposition (pay `r` when exactly one bidder clears the reserve, pay the second value when >=2 clear).

## Gate battery

| Gate | Direction | Rule | Result |
|---|---|---|---|
| G1 psi_zero_at_half | EQUALITY | `psi(1/2)=2*(1/2)-1=0` exact (Fraction) | PASS |
| G2 three_routes_agree | EQUALITY | `R_closed == R_integral == R_decomp` for n in {1,2,3,4,5} (Fraction) | PASS |
| G3 R2_5_12_gain_1_12 | EQUALITY | `R*(2)=5/12`, no-reserve `1/3`, gain `1/12` (Fraction) | PASS |
| G4 mc_n2_agrees | AGREEMENT | MC revenue (n=2) vs `5/12`, \|z\|<3; observed z=-0.822 | PASS |
| G5 mc_n3_agrees | AGREEMENT | MC revenue (n=3) vs `17/32`, \|z\|<3; observed z=1.816 | PASS |
| G6 grid_opt_at_half | ROBUSTNESS | exact `R(n,r)` maximized at `r=1/2` on dyadic grid {0,1/8,...,1}, n in {2,3,5} | PASS |
| G7 reject_no_reserve | REJECTION | paired MC (n=2): `E[rev(1/2)-rev(0)]>0` rejects "no reserve optimal"; z=175.4 | PASS |

Each gate runs in its own direction: EQUALITY gates use `fractions.Fraction` (no float); AGREEMENT gates pass at |z|<3 (>=3 sigma); the ROBUSTNESS gate confirms 1/2 beats every other grid reserve; the REJECTION gate kills the plausible-but-wrong "no reserve" alternative at large z.

## Determinism & digest

`build_results()` is a pure function of SEED and fixed parameters and holds no digest of itself. The harness builds it twice and asserts byte-identical canonical JSON (in-process guard, exit 3 on divergence); a separate re-invocation reproduces stdout byte-for-byte. The whole-dict digest is `results_sha256: b125afaf186e8d2430783b89af1a877193a65752db77884458485ced7ec918f0` (Python 3.11.15).

## Grounding & scope

The pinned revision of Wikipedia's *Regular distribution (economics)* article quotes the virtual-valuation formula `w(v) = v - (1-F(v))/f(v)` verbatim (there written with symbol `w` rather than `psi`) and states the Myerson principle that the optimal single-item auction is a Vickrey (second-price) auction augmented with "reserve prices to guarantee non-negative virtual valuations" — i.e. a reserve set where the virtual value is zero. The article lists the uniform distribution only as an example of a regular distribution; it does not specialize to Uniform[0,1], does not compute `psi(v)=2v-1`, and does not solve `psi(r*)=0`. Accordingly the specific numbers used here — `r*=1/2`, `R*(2)=5/12`, no-reserve revenue `1/3`, and the `1/12` reserve gain — appear nowhere in the pinned wikitext and are **derived** independently from the general theory, not quoted from the source.

## Reproduce

`cd sim-lab/sims/verdict-239-myerson-reserve && python3 myerson-optimal-reserve.py`

Exit 0; prints the results dict, `results_sha256: b125afaf186e8d2430783b89af1a877193a65752db77884458485ced7ec918f0`, and `all_pass: True`.

## Probe report (v0, 2026-07-20)

**1. What exactly is claimed?** For `n` iid Uniform[0,1] bidders the Myerson-optimal single-item auction is second-price with reserve `r*=1/2` (independent of `n`) and expected revenue `R*(n)=2n/(n+1)-1+(1/2)^n/(n+1)`; at `n=2`, `5/12` versus a no-reserve `1/3`.

**2. Is the core identity exactly true?** Yes — `psi(1/2)=0` and the `R*(n)` values are exact (`fractions.Fraction`), cross-checked by three independent closed forms agreeing for `n in {1..5}`.

**3. What is the sharpest falsifiable prediction?** That imposing `r=1/2` strictly out-earns no reserve; the paired Monte-Carlo rejects "no reserve is optimal" at `z ~ 175`.

**4. What plausible-but-wrong alternative is killed?** "Run Vickrey with no floor" (`r=0`) and "the optimal reserve should shrink as bidders grow" — both fail: `r*=1/2` is grid-optimal for `n in {2,3,5}` and independent of `n`.

**5. How is determinism guaranteed?** SEED=20260717, a single `random.Random` stream consumed in fixed order; a double-build canonical-JSON identity guard; byte-identical re-invocation; a whole-dict sha256 disclosed.

**6. What are the scope limits?** Uniform[0,1] only (a regular distribution); symmetric risk-neutral bidders; a single indivisible item; independent private values. Other distributions give a different `r*` (the zero of their virtual value).

**7. What did the grounding actually say?** The pinned Wikipedia revision quotes the virtual-value formula and the reserve-at-zero-virtual-value principle but states none of the numbers here — those are derived, as the scope note records.

**8. Recommendation rationale.** Exact core proven three ways, MC agreement within 3 sigma, a robustness sweep, and a high-z falsifier — all deterministic with a disclosed digest that the landed sim-lab verifier reproduces.

## One-line design fix

None needed — the verifier is landed and green (sim-lab PR #320); this card ships as-is.

**Recommendation: sim-ready**
