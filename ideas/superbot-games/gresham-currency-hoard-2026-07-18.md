# PROPOSAL 147 — Gresham currency hoarding: good money is hoarded out of circulation. A game economy issues two currencies at nominal parity — a STABLE "good" currency and a DEPRECIATING "bad" one — and the folk belief is "a premium hard currency circulates and drives the economy." Model the players as rational spenders and Gresham's law bites: they SETTLE with the melting bad currency first and HOARD the stable good one, so the good currency's circulation velocity COLLAPSES toward zero and the bad currency does almost all the settlement — even though both faucets mint symmetric nominal income; the SIGN of decay's effect on which currency circulates depends on spender rationality — with naive proportional spenders good circulates MORE (folk belief holds), with rational hoarders good is driven OUT of circulation.

> **State:** sim-ready
> **Class:** superbot-games · two-currency game-economy design / Gresham's-law currency hoarding (monetary microeconomics)
> **Anchor:** Gresham's law — "bad money drives out good": when a superior and an inferior currency must be accepted at equal face value, people spend the inferior one and hoard the superior one, so the good money disappears from circulation
> **Target:** sim-lab (VERDICT 160, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@cb24ad8e2aa06a1d0d8a3841bcd2e6bffe8e2cea · fetched 2026-07-18T21:04:30Z
> **Reference (external, reachable):** [Gresham's law — Wikipedia](https://en.wikipedia.org/wiki/Gresham%27s_law) — verified reachable 2026-07-18 via WebFetch ("a monetary principle stating that 'bad money drives out good' … When both superior and inferior currency must be accepted at equal face value, people spending money will hand over the 'bad' coins rather than the 'good' ones, keeping the 'good' ones for themselves … inferior currency dominates circulation while superior currency disappears through hoarding")
> **Verifier (firsthand):** `ideas/superbot-games/gresham_currency_hoard.py` · results-dict sha256 `90995ccd7c152402a6189a3fbdb60a401d04f750767127eae449cf8f67f7b969`
> 📊 Model: Claude Opus · high · idea/planning

## The phenomenon (one line)
When a game runs two currencies at nominal parity — a stable one and one that quietly loses value each period — a rational player settles every purchase with the melting currency and hoards the stable one, so the stable "good" currency's circulation velocity collapses toward zero and the depreciating "bad" currency does almost all the trade, even though the two faucets mint identical nominal income.

## The folk belief
"Issue a premium hard currency at par with the soft currency and it will circulate and drive the economy. Two interchangeable currencies at parity spend equally — players will just spend whichever they happen to have, so a valuable second currency adds liquidity and turnover." Economy designers treat a stable premium currency as a circulation booster: mint it, put it at par, and it greases the marketplace.

## The game-design thesis (reasoned to its fuller form — Q-0254 duty)
Model the economy as a population of N players, each holding a wallet of a **good** currency (stable — a held unit keeps its value) and a **bad** currency (depreciating — a holding penalty melts a fraction of any UNSPENT bad balance each period). Both faucets are **symmetric in nominal units**: every period each player draws good income **g ~ Uniform[0, INC_MAX]** and bad income **b ~ Uniform[0, INC_MAX]** from the SAME distribution. Both currencies settle **today's** expense **at par** — one unit of either pays one real unit of a mandatory per-period expense **E ~ Uniform[0, E_MAX]**. The ONLY asymmetry is the melt on carried bad currency.

A player must decide, each period, which currency to settle E with. The two channels:
- **Rational (hoarder):** a unit of bad currency held to next period is worth only GAMMA of its value; a unit of good currency held keeps its value. So the payoff-maximizing move is to SPEND the melting bad currency first (use it before it loses value) and HOARD the stable good currency. Good units pile up in the wallet, unspent.
- **Naive (proportional):** the player has no currency preference and settles E in proportion to current unit holdings.

Now Gresham's law is a mechanical consequence. Under rational hoarding, good currency is spent only when the bad balance can't cover the expense — so the good currency's **circulation velocity** (fraction of received good units that ever get spent) collapses toward zero, while the bad currency circulates hard. Under naive proportional spending the OPPOSITE happens: because the good currency never melts it ACCUMULATES in wallets, so a proportional payer holds — and therefore settles — MORE in good than in bad. The **sign** of the circulation gap (share of real settlement done in bad minus share done in good) is set by spender rationality: strongly POSITIVE with hoarders (good driven out), NEGATIVE with naive payers (good circulates more, folk belief holds). The whole result is a model-dependence claim (P024): Gresham hoarding is not a property of the currencies (the faucets are symmetric) — it is a property of rational agents facing a holding penalty.

Concretely (SEED = 20260717, committed constants): with rational hoarders the good currency settles only **12.93%** of real expense (share_bad **0.870675**) and its velocity is **0.129105** — while the identical economy with naive proportional spenders settles **69.94%** in good (velocity **0.69817**). Same symmetric faucets, opposite circulation — the stable currency's velocity **collapses from 0.698 to 0.129** (an **~81.5% drop**) the moment players stop being indifferent and start hoarding.

## The formal model (committed constants — sim-lab must reproduce exactly)
- N players, T periods, R independent trials (per-trial RNG seed offset from SEED by r·7919). Wallets start empty.
- Per period per player: draw good income g ~ Uniform[0, INC_MAX] and bad income b ~ Uniform[0, INC_MAX] (SYMMETRIC faucets); add to wallets. Draw a real expense E ~ Uniform[0, E_MAX]; settle `pay = min(E, wallet_total)` at par (1 unit = 1 real).
- **Rational** settlement: `from_bad = min(pay, bad_wallet)`, `from_good = pay − from_bad` (spend the melting currency first). **Naive** settlement: `from_good = pay·(good_wallet/total)`, `from_bad = pay·(bad_wallet/total)` (proportional to unit holdings).
- After settlement the UNSPENT bad balance melts: `bad_wallet ← (bad_wallet − from_bad)·GAMMA`; good never melts.
- Circulation share_c = total real settled in currency c / total real settled; velocity_c = total settled in c / total received in c. Headline metric = circulation gap = share_bad − share_good.
- Two worlds **naive** (proportional control) and **rational** (hoarder head) share the per-trial seed → COMMON RANDOM NUMBERS (identical income and expense draws), a low-variance paired contrast.
- **Model note (declared):** the two faucets are symmetric in nominal units and both settle today's expense at par — the ONLY asymmetry is the holding penalty GAMMA on unspent bad currency. This is the minimal object that exhibits Gresham hoarding: absent the melt the currencies are identical and no one prefers either; the melt alone (not any faucet or settlement asymmetry) drives good money out of circulation.

## Pinned world (committed constants)
- SEED = 20260717
- SIGMA_GATE = 3.0
- N = 1000; T = 100; R = 40
- INC_MAX = 2.0; E_MAX = 2.0; GAMMA = 0.90 (10%/period melt on unspent bad currency)
- Headline metric = circulation gap share_bad − share_good (common random numbers per trial across the two spender worlds)

## Pre-registered gates (APPROVE iff ALL hold, in order G1 → G2 → G3)
- **G1 — estimator agreement.** Split the R rational-world circulation gaps into two independent halves; the half-vs-half difference has |z| < SIGMA_GATE — the two halves do NOT significantly disagree, so the estimator is stable and the headline is not an artifact of one noisy half.
- **G2 — mechanism control.** In the NAIVE (proportional) world the circulation gap (share_bad − share_good) is NOT significantly positive (z = gap/se < SIGMA_GATE). Without rational hoarding there is no Gresham effect — the good currency circulates at least as much as the bad, isolating rational hoarding as the cause. (One-sided by construction: the control asserts good money is NOT driven out; a negative gap — good circulating more — passes.)
- **G3 — head.** In the RATIONAL (hoarder) world the circulation gap is SIGNIFICANTLY positive — the gap has z = gap/se ≥ SIGMA_GATE. The counterintuitive core: the good currency is hoarded OUT of circulation and its velocity collapses.

## Pre-registered decision rule
APPROVE (sim-ready confirmed) iff G1 AND G2 AND G3 all hold in order and the verifier exits 0 with a reproducible results-dict sha256 across a deterministic double-run. Any gate failing ⇒ REJECT/REVISE.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```
{
  "all_pass": true,
  "first_failing_gate": null,
  "g1_agreement": true,
  "g1_half_a_gap": 0.741044,
  "g1_half_b_gap": 0.741657,
  "g1_z": -0.69753,
  "g2_control": true,
  "g2_naive_gap": -0.398765,
  "g2_se": 0.000276,
  "g2_z": -1442.35432,
  "g3_head": true,
  "g3_rational_gap": 0.741351,
  "g3_se": 0.000436,
  "g3_z": 1701.028769,
  "n": 1000,
  "naive_share_bad": 0.300617,
  "naive_share_good": 0.699383,
  "naive_vel_bad": 0.300463,
  "naive_vel_good": 0.69817,
  "params": {
    "e_max": 2.0,
    "gamma": 0.9,
    "inc_max": 2.0
  },
  "proposal": 147,
  "r": 40,
  "rational_share_bad": 0.870675,
  "rational_share_good": 0.129325,
  "rational_vel_bad": 0.870242,
  "rational_vel_good": 0.129105,
  "seed": 20260717,
  "sigma_gate": 3.0,
  "t": 100
}
Results-JSON sha256: 90995ccd7c152402a6189a3fbdb60a401d04f750767127eae449cf8f67f7b969
G1 agreement    : PASS (half_a-half_b, z=-0.70, |z|<3.0)
G2 control      : PASS (naive gap=-0.3988, z=-1442.35, not-sig-positive z<3.0)
G3 head         : PASS (rational gap=+0.7414, z=+1701.03, z>=3.0)
all_pass        : True first_failing_gate: None
```
Results-dict sha256: `90995ccd7c152402a6189a3fbdb60a401d04f750767127eae449cf8f67f7b969` (deterministic double-run, exit 0 both times).

## Verifier
`ideas/superbot-games/gresham_currency_hoard.py` — stdlib only (`random, math, json, hashlib`). Simulates the N-player two-currency economy over T periods for two spender worlds (naive proportional, rational hoarder) under common random numbers, R paired trials each, and runs the three ordered z-gates (half-vs-half estimator agreement, the naive not-significantly-positive control, and the rational significant-gap head). Emits the whole results dict (no self-referential sha field; every float rounded to 6 decimals; the compact canonical serialization's sha256 IS the disclosed digest; stdout dumps the pretty indent=2 view — the WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture, P127+ twist). Writes no JSON to disk.

## Reproduce
```
python3 ideas/superbot-games/gresham_currency_hoard.py
```
Expected: prints the results JSON, `Results-JSON sha256: 90995ccd7c152402a6189a3fbdb60a401d04f750767127eae449cf8f67f7b969`, three `PASS` lines, exit 0.

## Why it matters (game design)
A second currency is not a liquidity dial — whether it circulates or vanishes depends on whether it holds value RELATIVE to the currency it shares a wallet with. Put a stable premium currency next to a soft currency that inflates, and rational players do the economically correct thing: they spend the melting soft currency on everything and let the premium currency pile up untouched. The marketplace you denominated in the premium currency goes illiquid; the "hard money" you minted to add turnover becomes a savings account. Design consequences: (1) never assume a valuable currency circulates — a currency only circulates if holding it is at least as costly as spending it, so a stable currency next to an inflating one is a hoard magnet, not a medium of exchange; (2) if you WANT the premium currency to move, add a holding cost (expiry, a wallet cap, a spend-or-lose window) or a spend-only sink so hoarding is not free; (3) if you want it HELD (a store of value / status reserve), that is fine — but then instrument it as savings, not velocity, and don't expect a liquid market in it. Read "we added a premium currency and the soft-currency market got MORE active while the premium market froze" as Gresham's law, not a launch dud.

## Dedup
- Distinct from every prior game-lane card: shop-reroll (optimal stopping), streak-shield (regression to the mean), energy-cap (renewal overflow forfeiture), matchmaking-winrate-mirage (Elo compression under SBMM), compounding-reward-inequality (log-normal Gini), PRD proc-rate compression, snipe-clearing-leak (auction microstructure), guild-volunteer-dilemma (N-player public-goods provision), single-elim favorite-collapse (tournament order statistics), balance-triangle pick-rate inversion (zero-sum matrix equilibrium), Ringelmann raid coordination overhead (group-size per-capita output decay), rank-decay churn cliff (loss-aversion-driven churn), pity-anticipation-collapse (gacha pity timing), rubber-band PID controller instability. **None model a two-currency ECONOMY, currency hoarding, Gresham's law, or a circulation-velocity collapse whose sign flips with spender rationality.**
- Closest neighbours are energy-cap (also a "value you don't spend is lost" pressure) and rank-decay (also a per-period decay): energy-cap is deterministic renewal overflow forfeiture on a single resource, and rank-decay is a loss-aversion churn decision — neither has TWO competing currencies, a hoard-vs-spend allocation, or a circulation-share metric. This is the FIRST monetary-microeconomics / Gresham's-law card in the game lane and the FIRST two-currency card in any lane.

## Model basis (declared model-dependence — the P024 discipline)
The result is a **sign-dependence** claim: the sign of the circulation gap (share_bad − share_good) is set by spender rationality. The DIRECTION (good hoarded out of circulation under rational spenders; good circulating at least as much as bad under naive proportional spenders) holds for any model where (a) two currencies settle at par today, (b) one carries a strictly positive holding penalty and the other does not, and (c) at least the rational arm minimizes expected holding loss — which makes spending the depreciating currency first strictly optimal. The specific magnitudes (rational velocity 0.129 vs naive 0.698; share_good 12.9% vs 69.9%) are pinned to (INC_MAX, E_MAX, GAMMA) = (2.0, 2.0, 0.90) and N = 1000, T = 100. **One declared modelling choice** (flagged, not hidden): the depreciation is modelled as a per-period **melt on the UNSPENT bad balance** (a holding penalty), which is the cleanest way to make bad currency strictly worse to HOLD while keeping it at par to SPEND today — exactly the Gresham premise (equal face value, unequal intrinsic/held value). An alternative that raises settlement PRICES in the bad currency over time would add a settlement asymmetry and confound "is good hoarded?" with "is bad just worth less per unit?"; the pure holding-penalty melt isolates the hoarding decision. Real economies add expectations, arbitrage, dual-price marketplaces, and heterogeneous discount rates; the minimal symmetric-faucet + single-melt model is the smallest object that exhibits Gresham hoarding, and richer frames only move how fast the good currency drains from circulation.

## Probe report (v0, 2026-07-18)

**1. What is this really?** A sign-flip circulation lever. Two currencies share a wallet at par; one melts if held, one doesn't. A rational player spends the melting one and hoards the stable one, so the stable "good" currency is driven OUT of circulation (Gresham's law). The net sign of the circulation gap (share settled in bad minus share settled in good) is set by spender rationality: strongly positive under hoarders (good vanishes from trade), negative under naive proportional payers (good circulates more, because it accumulates). "A premium currency at par adds liquidity" is true only for players with no preference.
**2. What would make it false?** If the rational-world gap were ≤ 0 or z < 3σ (G3 fails — hoarding does NOT drive good out of circulation), or if the naive control ALSO showed a significantly positive gap (G2 fails — the effect is not specific to rational hoarding, so it is some other asymmetry), or if the two halves of the trials disagreed (G1 fails — the estimator is unstable). Any of G1/G2/G3 failing → REJECT.
**3. Simplest version that still bites?** SEED = 20260717; a 1000-player economy, symmetric nominal faucets, a real expense at par, and a single holding penalty GAMMA = 0.90 (10%/period melt on unspent bad currency) already collapse the good currency's velocity from **0.698** (naive) to **0.129** (rational) — it settles only **12.9%** of real expense despite an identical faucet. One behavioural switch (hoard vs proportional) flips which currency circulates.
**4. What is the counterintuitive core?** "A valuable premium currency at par circulates and drives the economy" is inverted. Because the stable currency is the one worth KEEPING, rational players keep it — so the currency you minted to add turnover becomes a hoard and the marketplace denominated in it goes illiquid, while the currency you thought was disposable does all the trade. Good money is driven out of circulation exactly because it is good.
**5. Where could I be fooling myself?** The paired common-random-numbers estimator could look artificially tight — G1 guards it by requiring two independent halves of the trials to agree (z = **−0.70**, |z| < 3). The hoarding could be some generic sim artifact rather than the rationality — G2 is the control: the identical economy with naive proportional spenders produces NO significant positive gap (z = **−1442.35**, the good currency actually circulating MORE), so rational hoarding is doing the work. And the faucets could secretly favour bad — they do not: both currencies draw income from the SAME Uniform[0, INC_MAX] and settle at par; the only asymmetry is the holding melt, which is the Gresham premise itself.
**6. What is the honest calibration?** Dry-sim at SEED = 20260717: G3 head circulation gap = **+0.7414** (share_bad **0.870675** vs share_good **0.129325**), z = **+1701.03** ≥ 3σ, good-currency velocity **0.129105**; G2 control gap = **−0.3988** (share_good **0.699383** > share_bad **0.300617**), z = **−1442.35** (not significantly positive — good circulates more, folk belief holds), good-currency velocity **0.69817**; G1 halves agree, z = **−0.70**. All PASS in order, exit 0; results-dict sha256 **90995ccd…f7b969**; two runs byte-identical. The z-values are large because the economy is big (N = 1000, T = 100) and the paired estimator is low-variance — the honest headline is the **~81.5% velocity collapse** of the good currency (0.698 → 0.129), not the z magnitude.
**7. What decision does it change?** Stop assuming a premium currency circulates because it is valuable. If you want it to MOVE, price holding it (expiry, wallet cap, spend-or-lose window) or add a spend-only sink so hoarding is not free; if you want it HELD, instrument it as savings, not velocity, and don't expect a liquid market. Read "the soft-currency market got busier and the premium market froze" as Gresham's law.
**8. How will we know it worked?** The committed stdlib verifier reproduces, under SEED = 20260717, the estimator agreement (G1, halves within noise), the rationality-free control (G2, no significant positive gap and good circulating more under naive spenders), and the head (G3, a ≥ 3σ positive circulation gap with the good currency's velocity collapsing to 0.129 under rational hoarders) at their SIGMA_GATE = 3.0 bars, with the results-dict sha256 matching 90995ccd7c152402a6189a3fbdb60a401d04f750767127eae449cf8f67f7b969 across a deterministic double-run.

## One-line design fix
Treat a stable currency next to an inflating one as a hoard magnet, not a liquidity dial: because rational players spend the melting currency and keep the stable one, the "hard money" you minted for turnover freezes into savings — so if you want it to circulate, add a holding cost (expiry, wallet cap, spend-or-lose) or a spend-only sink, and measure the premium currency's velocity, not its issuance.

**Recommendation: sim-ready**
