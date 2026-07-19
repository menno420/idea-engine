# For a priced venture round, a pre-money option pool dilutes the founders alone: the incoming investor's post-money stake equals I/(P+I) and is INVARIANT to the pool size, so founders absorb 100% of the pool and hand the investor an extra q·I/(P+I) versus a pro-rata pool

> **State:** sim-ready
> **Class:** counterintuitive-captable / venture-lab (fundraising / dilution slot)
> **Slot:** round-38 VENTURE
> **Target:** sim-lab (VERDICT 175, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine/blob/cfc5e72adb2677efb5a8b8d191c8a1c9368d3a71/control/outbox.md@22c71f610b2c0a56b5b0cf1555b7e3802b446af6 · fetched 2026-07-19T08:25:09Z
> **Reference (external):** Babak Nivi with Brad Feld, "The Option Pool Shuffle" (Venture Hacks) — the canonical statement that a term-sheet option pool created in the pre-money lowers the founders' effective valuation and dilutes them, not the incoming investor. https://venturehacks.com/option-pool-shuffle — verified live HTTP 200 this session: "Slipping the option pool in the pre-money lowers your _effective_ valuation to $6M. The _actual_ value of the company you have built is $6M, not $8M." Also Brad Feld & Jason Mendelson, *Venture Deals*, ch. on the option pool.
> **Harvest source (firsthand):** ideas/venture-lab/option_pool_shuffle.py + its recorded double-run (this branch).

## The phenomenon (one line)
In a priced round (invest I at pre-money P, post-money P+I) the term sheet also demands an option pool of size q; because the pool is created PRE-money, the incoming investor's post-money ownership stays exactly t = I/(P+I) whatever q is, and every share of the pool comes out of the founders' stake.

## The folk belief
An option pool dilutes everyone in proportion to their holdings — the investor and the founders share the hit — so a bigger pool just shaves a little off each shareholder, and negotiating the headline pre-money valuation is what matters.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Write the fully-diluted post-money cap table as three slices that sum to 1: the new investor's t, the option pool q, and the founders' remainder. The investor pays I for a post-money valuation P+I, so the investor's slice is fixed by the money: t = I/(P+I). The question is only WHERE the pool's q comes from.
- **Pre-money pool (the shuffle — actual VC practice).** The pool is carved out of the founders' pre-money stake before the investment. Investor = t; pool = q; founders = 1 − t − q. The investor's t does not depend on q at all: dt/dq = 0. Founders bear the whole pool.
- **Pro-rata pool (the "fair" folk model).** The pool dilutes existing holders AND the new investor proportionally: investor = t(1 − q); founders = (1 − t)(1 − q); pool = q. Here dt/dq = −t: the investor shares the hit.
Subtracting the two conventions at matched (P, I, q), the pre-money pool hands the investor exactly
    transfer = t − t(1 − q) = q·t = q·I/(P+I)
of the company that a pro-rata pool would have left with the founders — and founders lose that same q·t on top of eating the pool. The effective pre-money the founders actually receive is P − q(P+I), not P: each point of pool is worth a point of post-money off the founders' price, which is why a point of pool costs founders MORE than a point of headline valuation. The pool is a price on the founders' stock dressed as a neutral housekeeping line.

## Pinned world (committed constants — the verifier is the contract)
SEED=20260717 · N=4000 paired draws per regime · founders hold F0=10,000,000 pre-round fully-diluted shares (integer cap tables → quantization is the only noise). Baseline Series-A regime: investor post-money target t ~ Uniform[0.15, 0.30]; low pool q_lo ~ Uniform[0.05, 0.10]; high pool q_hi ~ Uniform[0.15, 0.25]. Shifted (mega-round) regime: t ~ Uniform[0.10, 0.20]; q_lo ~ Uniform[0.08, 0.12]; q_hi ~ Uniform[0.22, 0.30]; F0=100,000,000. Investor and founder fractions are read off ROUNDED integer share counts, not plugged from the closed form.

## Pre-registered gates (evaluation order G1 → G2 → G3; APPROVE iff ALL hold, z_gate=3.0)
- **G1 — the investor's fraction is invariant to the pool size (rejects the pro-rata null).** Over the paired draws, the change in the investor's realized fraction from q_lo to q_hi is ≈0 under the shuffle, while the pro-rata null predicts −t·(q_hi−q_lo); the divergence (pro-rata change minus shuffle change) is decisively non-zero at z ≥ 3. Observed shuffle_change_absmean = **0.0** (below 6 dp), prorata_minus_shuffle_change_mean = **-0.0283**, se = **0.000146**, z = **+194.139005**.
- **G2 — the founders→investor wealth transfer equals the closed form q·t.** At matched (P, I, q_hi) the investor-fraction gap between the shuffle and a pro-rata pool equals q·t within a tight relerr ceiling and is robustly positive at z ≥ 3. Observed transfer_mean = **+0.04526**, predicted_qt_mean = **+0.04526**, relerr_mean = **0.0** (below 6 dp, < 1e-3 ceiling), z = **+260.109119**.
- **G3 — robust to a shifted (mega-round / higher-pool) distribution.** G1 re-run under the shifted regime holds the invariance and keeps the divergence decisively above the null at z ≥ 3. Observed shuffle_change_absmean = **0.0**, prorata_minus_shuffle_change_mean = **-0.024062**, se = **0.000098**, z = **+246.501756**.

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 ∧ G3 all hold on a clean-room re-run (SEED=20260717) with the results-dict sha256 matching. Any gate false → REJECT naming first_failing_gate. Observed all_pass = **true**, first_failing_gate = **null**.

## Disclosed verifier (the sim-lab spec)
`ideas/venture-lab/option_pool_shuffle.py` — stdlib only (math, json, hashlib, random, statistics). Posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY. Builds the ordered results dict, asserts an in-process double run is byte-identical, prints the pretty indent=2 dump (floats 6 dp) and the compact canonical JSON's sha256. Expected results-dict sha256:
    f588004512fce81ea824be9fec0c95a3ba2f3e2a8ec03af5867b526bbcb5b4b5
Re-run twice cross-invocation; both must print IDENTICAL output and the sha256 above; exit 0 iff all_pass.

## Why it matters
Where the option pool sits on the cap table is a first-order fight in every priced round, and the folk model gets it exactly wrong: the pool is not shared dilution, it is founder dilution with a q·t bonus handed to the investor. Across the sampled Series-A bands the shuffle transfers on average **0.04526** of the company (≈4.5 points) from founders to the investor purely by convention — before a single share is priced differently. The lever that protects founders is not haggling the headline pre-money; it is negotiating the pool DOWN, sizing it to the real hiring plan, or pushing it into the post-money — a point of pool costs founders more than a point of valuation, because it comes off the effective pre-money P − q(P+I).

## Dedup (contrast vs prior lane heads)
- vs **founder-dilution-waterfall / any liquidation-preference head** — those model who gets paid at an EXIT (preference stacking, participation, the waterfall); this models ownership at the ISSUANCE event, no exit and no preference. The counterparty is the incoming investor's percentage, not a liquidation payout.
- vs **growth-endurance-dominance / retention-survivorship / nrr-composition** — SaaS cohort revenue compounding or decaying over time; this is a static single-round cap-table identity, no cohorts, no time series.
- vs **marketplace-take-rate-disintermediation** — a two-sided platform's operating pricing decision (the rake) with off-platform leakage; this is equity issuance in a financing, no platform and no demand curve.
- vs **sales-ramp-capacity-drag** — an S-curve hiring/quota-ramp revenue model; unrelated to cap-table ownership. First option-pool / pre-money-carve-out head in any lane.

## Model basis (declared model-dependence — the P024 discipline)
Exact given the standard priced-round cap-table model: the investor targets post-money fraction t = I/(P+I); the pool is q of post-money; the shuffle carves the pool from the founders' pre-money stake; the pro-rata null dilutes all holders by (1−q). The invariance dt/dq = 0 and the transfer = q·t are algebraic IDENTITIES of the pre-money convention, not distribution-dependent effects — the Monte Carlo only confirms they survive realistic integer-share quantization across the documented Series-A ranges, and the shift (G3) confirms the quantization noise shrinks, not grows, at scale. Declared crossover (disclosed, NOT the claim): the "who bears a pre-round carve-out" logic applies identically to advisor pools, warrant coverage, and pre-round expansion pools; the verified claim is the option-pool shuffle specifically. The one modelling choice is that the pro-rata pool is the right stand-in for "what founders naively expect" — chosen because it is the unique convention under which the pool dilutes all holders in proportion.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed | z | Verdict |
|------|------|-----------|----------|---|---------|
| G1 | invariance | divergence mean ≠ 0, z≥3 | -0.028300 (shuffle abs 0.0) | +194.139005 | PASS |
| G2 | identity | transfer = q·t, relerr<1e-3, z≥3 | +0.045260 (relerr 0.0) | +260.109119 | PASS |
| G3 | robustness | shifted divergence ≠ 0, z≥3 | -0.024062 (shuffle abs 0.0) | +246.501756 | PASS |

## Probe report (v0, self-adversarial)
**1.** Real invariance or a tautology? Under the shuffle the investor's fraction is t by construction — is G1 circular? No: the claim is that the standard pre-money convention IS that construction, and the FALSE alternative founders intuit is the pro-rata pool. G1 measures the divergence between the two conventions applied to the SAME economic ask; it is the pro-rata prediction (−t·Δq) that is rejected, and both fractions are read off realized integer cap tables, not plugged from t.
**2.** Knife-edge at the nominal draw? No — shuffle_change_absmean = 0.0 (below 6 dp) across all 4000 draws in BOTH the base and shifted regimes; the investor's fraction is invariant to the pool in every single draw, not on average only.
**3.** Where does it break? A pool negotiated into the POST-money, or a smaller pool sized to the real hiring plan, breaks the shuffle — those are exactly the founder-protective moves the phenomenon motivates. Disclosed. The invariance is exact under the pre-money convention for any (P, I, q).
**4.** z inflated by huge N? No — the divergence (≈ −0.028, a 2.8-point gap) is large relative to the tiny quantization se (1.5e-4), so z is driven by effect size, not N. G2's relerr against the closed form is 0.0 to 6 dp — it is an algebraic identity, not a fitted effect.
**5.** Determinism? SEED=20260717 pinned; in-process double run asserted byte-identical; cross-invocation double run printed IDENTICAL with sha256 f588004…b4b5. A verdict re-run must reproduce that digest.
**6.** Constants tuned to force a pass? The bands (t ∈ [0.15, 0.30], pools 5–25%) are the documented real Series-A ranges and F0 = 10M is a round founder-share count; because the invariance and transfer are identities, ANY bands pass — no constant sits near a pass margin.
**7.** Float ordering perturbing the digest? All dict floats round()-ed to 6 dp; compact JSON with sort_keys as the hashed preimage; no set/dict-ordering nondeterminism; the in-process assert catches drift.
**8.** Real or toy? The option-pool shuffle is a documented, named term-sheet phenomenon — Venture Hacks' "The Option Pool Shuffle" and Feld & Mendelson's *Venture Deals* are its canonical statements, and where the pool sits (pre- vs post-money) is a standard negotiated line in every priced round. The mechanism names why the pre-money pool is founder dilution, not shared dilution.

**Recommendation: sim-ready**
