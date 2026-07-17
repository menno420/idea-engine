# The refund window is a conversion instrument, not a cost center: for an indie digital product the net-revenue-maximizing refund window is INTERIOR — strictly more generous than the refund-minimizing zero-window, because a money-back window lifts conversion (saturating) while its refund cost becomes a real loss only once the window is long enough to arm serial wardrobers (a discontinuous abuse threshold), so the optimum sits right up to but not past it

> **State:** sim-ready
> **Class:** venture-lab · indie digital-product refund policy · non-monotone net revenue under a saturating conversion lift + a discontinuous abuse threshold
> **Target:** sim-lab (VERDICT 107, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@8efd823 · fetched 2026-07-17T09:34:21Z
> **Harvest source (firsthand):** ideas/venture-lab/ (the Ship-It / KDP self-publishing + digital-product venture world; refund-window / return-policy length is a live per-product decision object — priors read this session: big-pond-badge-inversion, series-readthrough-saturation-crossover, bundle-pwyw-floor-lattice, impulse-price-blanket-series-collapse, channel-concentration-vs-diversification, ku-exclusivity-fork, keyword-tiling-vs-independent-picks)

## The phenomenon (one line)
Lengthening a digital product's refund window raises net revenue at first — the money-back safety-net converts hesitant buyers faster than honest refunds erode it — until the window crosses the point where serial wardrobers can extract full value and still refund; past that abuse threshold net revenue drops discontinuously, so the net-revenue-maximizing window is INTERIOR and strictly MORE generous than the zero-window an abuse-fearing seller defaults to.

## The folk belief
"Refunds are a cost and generous windows are an abuse magnet — so keep the refund window as short as possible to protect margin." Net revenue is modeled as monotone DECREASING in window length (every extra day only invites more refunds). Under that model the answer is always the minimum window (W=0 / no refunds).

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Two forces move in opposite directions as the window W grows.
(1) Conversion safety-net (upside): a prospective buyer is uncertain about fit and risk-averse; a money-back window lowers perceived downside, so browse→buy conversion rises with W and SATURATES — conv(W) = c0 + dC·(1 − e^(−W/τ)). Diminishing: the first days of protection buy most of the confidence.
(2) Refund leakage (downside), with TWO sub-terms:
  - honest dissatisfaction: a fraction d of buyers turn out dissatisfied, realizing it at a stochastic time t ~ Exp(ρ); they refund iff t ≤ W. This term rises smoothly and saturates at d — a longer window catches more honest dissatisfaction.
  - wardrobe abuse: a fraction φ of buyers extract full value then refund, but ONLY if the window is long enough for full extraction — modeled as a hard threshold: they refund iff W ≥ W_abuse. This term is a STEP: zero below W_abuse, then φ of buyers lost at once.
Net revenue per unit demand NR(W) = conv(W)·(1 − d·(1−e^(−ρW)) − φ·1{W≥W_abuse}). Below W_abuse, NR rises then flattens as the saturating conversion gain races the smoothly-growing honest-refund term — the in-regime optimum sits near the top of the conversion S-curve. At W_abuse the abuse step subtracts φ discontinuously; if that cliff exceeds the marginal conversion gained by going longer, the global optimum is the last window BEFORE the wardrobers arm. The optimal policy is "as generous as you can be without giving wardrobers time to extract full value" — strictly more generous than W=0, strictly less than an unbounded window, sitting on the safe side of a discontinuity the fee-minimizing seller never sees.

## Pinned world (committed constants — sim-lab must reproduce exactly)
- Refund-window grid (decision variable, 9 points, index 0..8): W = [0, 3, 6, 9, 12, 13, 14, 18, 30] days.
- Price P = 40.0. Arrivals per rep A = 5000 (product views).
- Conversion: conv(W) = c0 + dC·(1 − e^(−W/τ)); c0 = 0.030, dC = 0.030, τ = 6.0. (W=0 → 0.030; W→∞ → 0.060, a doubling.)
- Buyer types (disjoint, per converted buyer): abuser w.p. φ = 0.08; else dissatisfied w.p. d = 0.20; else satisfied. (u~U(0,1): abuser if u<φ; dissatisfied if φ≤u<φ+d; else satisfied.)
- Honest dissatisfaction realizes at t ~ Exp(ρ), ρ = 1/9 per day; honest refund iff t ≤ W.
- Wardrobe abuse refund iff W ≥ W_abuse, W_abuse = 14. (Wardrobers need ≥14 days for full extraction — COMMITTED ASSUMPTION, the discontinuity.)
- Refunded sale returns $0; kept sale returns P. Net revenue per rep = P·(n_buyers − n_refunds).
- N_REPS = 400. SEED = 20260717 (SEEDLESS w.r.t. the shared seed block 20261730 — left untouched; the sim pins its own SEED constant; P089–P093 precedent).
- Stochastics: n_buyers ~ Binomial(A, conv(W)); per buyer draw type + (if dissatisfied) exponential realization time; count refunds by the rules. Deterministic string-keyed random.Random streams (key "SEED:regime:rep", sha256-routed) — no wall-clock, no network, no PYTHONHASHSEED dependence.

## Pre-registered gates (evaluation order R1 → R2 → R3 → R4; APPROVE iff ALL hold)
- **R1 — interior optimum dominates BOTH endpoints.** W* = argmax_W mean net-revenue must be INTERIOR (index ≠ 0 and ≠ 8) and beat idx0 (W=0, the refund-minimizing folk choice) AND idx8 (W=30, maximally generous) each by ≥3σ (combined SE). Dry-sim: W*=idx5 (W=13); vs W=0 gap $3558.9 / se 38.16 → 93.3σ; vs W=30 gap $894.4 / se 41.19 → 21.7σ.
- **R2 — the abuse cliff is a real discontinuity.** The last window before wardrobers arm (W=13, idx5) outsells the first armed window (W=14, idx6) by ≥3σ, DESPITE W=14 converting MORE buyers. Dry-sim: gap $862.2 / se 41.66 → 20.7σ; conv(13)=0.056563 < conv(14)=0.057091 yet net-rev $9575.7 > $8713.5 — "more generous, less net" (refunds jump 43.1→67.4 as φ arms).
- **R3 — the interior optimum is not a knife-edge.** Across the abuser-fraction grid φ∈{0.06,0.07,0.08,0.09,0.10} (nominal ρ) AND ρ×{0.8,1.2} (nominal φ), argmax stays INTERIOR (never idx0 or idx8). Dry-sim: [φ06→5, φ07→5, φ08→4, φ09→5, φ10→5, ρ×0.8→5, ρ×1.2→5]. DISCLOSED: at φ=0.08 the argmax lands idx4 (W=12) rather than idx5 (W=13) — idx4/idx5 are a <1σ near-tie in the nominal table ($9566.2 vs $9575.7, gap 9.5 / se ~30) and the sweep's independent RNG stream lands the coin-flip the other way; both are strictly interior. The invariant is "interior, not an endpoint," not a fixed index.
- **R4 — the conversion lift is the sole cause (control).** With dC = 0 (refund window gives NO conversion lift; conv(W)=c0 constant), net-revenue becomes monotone DECREASING in W (only refund cost, no upside), so argmax must return to idx0 (W=0) at ≥3σ over idx1. Dry-sim: argmax=idx0; gap $315.8 / se 34.21 → 9.2σ. Restores the folk monotone; isolates the safety-net as the driver.

## Pre-registered decision rule
APPROVE iff R1 ∧ R2 ∧ R3 ∧ R4 all hold on the pinned world; else REJECT with the first failing gate named. Twin evaluators (an R1→R4 if-chain and a table-driven scan) MUST agree on the verdict token and the first-failing gate; disagreement → hard SystemExit (no verdict emitted).

## Disclosed verifier (the sim-lab spec)
One-command, stdlib-only, hermetic Python (hashlib, json, math, random). Pinned-world constants at file top (W grid, P, A, c0, dC, τ, d, φ, ρ, W_abuse, N_REPS, SEED). Binomial conversion draws + per-buyer type + exponential realization on string-keyed random.Random streams ("SEED:regime:rep", sha256-routed); NO wall-clock/network/git/PYTHONHASHSEED. Emits results.json via json.dumps(sort_keys=True, indent=2) carrying verdict, first_failing_gate, per-window (W, conv, mean_netrev, se, mean_buyers, mean_refunds), the four gate blocks (gap, combined_se, margin_sigma, pass), the R3 argmax sweep vectors, twin agreement, and self_checks. fixtures.json pins the world + a first-rep anchor draw (written on first run, verified thereafter). An analytic sanity anchor asserts every MC mean matches the closed form E_netrev(W)=A·conv(W)·P·(1 − d·(1−e^(−ρW)) − φ·1{W≥W_abuse}) within rel-err <1% (dry-sim max rel-err 0.44%). Double-run must be byte-identical (results-dict sha256 stable). Self-checks (≥12; dry-sim ran 15) gate exit 0. Dry-sim reference: results-dict sha256 c3cfdae48800373c9c838144f41ade70b4092e8862f648f38630b756e93480dc (SEED=20260717, N_REPS=400, A=5000; Bernoulli-loop binomial on Python 3.11 — random.binomialvariate is 3.12+; an independent verifier may reimplement the draw and CONFIRM gate outcomes rather than the digit-level digest).

## Why it matters (venture-ops)
Refund-window length is a live, zero-cost, high-leverage policy on every digital product the venture ships (Gumroad / Etsy / KDP / app-store / course platforms all expose it), and the default instinct — "keep returns tight, they're a cost and an abuse magnet" — is exactly the dominated choice when the window also buys conversion. The model says: set the window as generous as you can WITHOUT giving wardrobers time to extract full value — the largest SAFE window, not the shortest window. It also predicts a diagnostic signature the venture can watch for: a refund-rate STEP (not a smooth rise) as the window lengthens marks the wardrobe threshold; the optimum is the day before that step.

## Dedup
Distinct decision-object from every venture prior. NOT big-pond-badge-inversion (P090: single-title category SELECTION under a rank-K badge threshold; this is refund-POLICY length under an abuse threshold — a post-purchase lifetime mechanic, a different lever and a different discontinuity). NOT series-readthrough-saturation-crossover (P086: quality-budget allocation across series depth). NOT bundle-pwyw-floor-lattice / impulse-price-blanket-series-collapse (P074/P078: pre-purchase PRICE structure, not post-purchase refund policy). NOT channel-concentration / keyword-tiling / ku-exclusivity / kill-clock / sample-window-toll. No prior models refunds, returns, or any post-purchase / lifetime mechanic — the whitest space in the venture corpus. The novel object: net revenue NON-MONOTONE in refund-window length, a saturating conversion lift racing a step-discontinuous abuse term, yielding an interior optimum strictly more generous than the folk minimum.

## Model basis (declared model-dependence — the P024 discipline)
The conversion lift (c0, dC, τ), the buyer-type fractions (d, φ), the dissatisfaction rate ρ, and the wardrobe threshold W_abuse are COMMITTED ASSUMPTIONS, not measured from a live storefront. The verdict tests the INTERNAL decision-logic under these constants — "does a saturating conversion lift racing a step-discontinuous abuse term produce an interior net-revenue optimum that dominates both the zero-window and the max-window, and does removing the conversion lift restore the folk minimum?" — not the empirical magnitude of any term for a specific product. The world is calibrated (a doubling conversion lift, a 14-day wardrobe threshold, 8% wardrobers) to exhibit the mechanism cleanly; R3 shows the qualitative conclusion (interior, not an endpoint) survives the φ-grid and ρ±20%. What would FALSIFY the decision claim, not just retune it: a conversion lift so small the abuse cliff always dominates (optimum collapses to W=0, R4-like) or an abuse threshold so high the wardrobers never arm within any offered window (optimum runs to the max window, monotone).

## Probe report (v0, 2026-07-17)
> Single-pass battery (panel not escalated: dedup clears against all 28 venture-lab priors by decision-object — post-purchase refund policy is unmodeled space; kill-test is the R4 control; feasibility/liveness confirmed by a run dry-sim; grounding firsthand on the venture-lab decision world at idea-engine@8efd823, fetched this session).

**1. What is this really?** A policy-length optimization with a hidden discontinuity: net revenue is non-monotone in refund-window length because a saturating conversion safety-net races a step-discontinuous wardrobe-abuse term. The decision object is "how long a refund window," and the folk minimize-refunds rule is dominated.

**2. Is it genuinely new?** Yes — see Dedup. No venture prior models refunds / returns or any post-purchase mechanic; the closest priors are pre-purchase price structure (P074/P078) and category selection (P090), different objects and mechanisms.

**3. What would kill it?** The R4 control (dC=0) — if the interior optimum survived removing the conversion lift, the phenomenon would be some other artifact and the idea is INVALID. Dry-sim: dC=0 returns argmax to W=0 at 9.2σ, so the conversion safety-net is the sole cause. Also killed if the abuse threshold sat outside the offered window range (monotone, no cliff).

**4. Is it feasible to simulate?** Yes — stdlib-only, binomial + per-buyer type draws, ~18s for the full double-run (400 reps × 9 windows × sweeps, A=5000 on Python 3.11's Bernoulli loop). Fully specified pinned world; no external data.

**5. What did the dry-sim measure?** All four gates pass with headroom: R1 93.3σ over W=0 and 21.7σ over W=30; R2 20.7σ (conv up, net down); R4 9.2σ; R3 argmax interior at all 7 sweep points. Global optimum W=13 (the day before the 14-day wardrobe threshold). Twin evaluators agree APPROVE / first_failing=None; double-run byte-identical (results-dict sha256 c3cfdae4…80dc); 15/15 self-checks.

**6. What correction was disclosed?** No model / mechanism correction. One environmental note: Python 3.11 lacks random.binomialvariate (3.12+), so the binomial conversion draw uses the exact Bernoulli-sum fallback with A held at the pinned 5000 (runtime fine); no constant, N_REPS, or seed altered. R3 additionally discloses that at φ=0.08 the argmax lands idx4 (W=12) vs idx5 (W=13) — a <1σ near-tie decided by the sweep's independent RNG stream; both interior, invariant preserved.

**7. What are the stability bounds / sanity checks?** Sanity: the closed form E_netrev(W)=A·conv(W)·P·(1 − d·(1−e^(−ρW)) − φ·1{W≥W_abuse}) matches every Monte-Carlo mean to <1% (dry-sim max rel-err 0.44%); the abuse term is deterministically zero below idx6 and φ above, checkable by hand; conv(W) monotone increasing and refund-frac monotone increasing are asserted. Margins are σ-scaled against the binomial / refund SE, not asserted.

**8. How will we know it worked?** V107 reproduces the pinned world one-command, hits verdict=APPROVE / first_failing_gate=None with R1 (both endpoints) ≥3σ, R2 ≥3σ, R3 argmax interior across all sweeps, R4 ≥3σ, twins agree, and the results-dict double-run is byte-identical — reported with the per-window table and the four margins.

## Gate power + margin ledger
| gate | claim | dry-sim margin | floor |
|---|---|---|---|
| R1 | interior optimum dominates BOTH endpoints | 93.3σ vs W=0 (gap $3558.9 / se 38.16); 21.7σ vs W=30 (gap $894.4 / se 41.19) | 3σ each |
| R2 | abuse cliff: more generous window, less net | 20.7σ (gap $862.2 / se 41.66); conv 0.05656→0.05709 up, net $9575.7→$8713.5 down | 3σ |
| R3 | interior across φ∈[0.06,0.10], ρ×[0.8,1.2] | argmax [5,5,4,5,5,5,5]; all interior (idx4/idx5 near-tie disclosed) | interior ∉ {0,8} |
| R4 | dC=0 restores folk minimum (W=0) | 9.2σ (gap $315.8 / se 34.21) | 3σ |

**Recommendation: sim-ready**
