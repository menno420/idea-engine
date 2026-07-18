# A free-to-play energy/stamina cap sold as "generosity" is an overflow-forfeiture TAX: the fraction of regenerated stamina a player can actually spend is the exact 1−e^{−C/μ}, a concave saturating function of the cap — so a busy player (long login gap μ) silently forfeits a fraction e^{−C/μ} of all regen that scales with their absence, DOUBLING the cap barely helps once C exceeds μ, and the cap is throughput-limited by login frequency, not by the cap.

> **State:** sim-ready
> **Class:** superbot-games · free-to-play energy/stamina pacing · retention-economy mechanic design
> **Target:** sim-lab (VERDICT 120, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@36f5a6f · fetched 2026-07-18T01:10:25Z
> **Verifier (firsthand):** committed stdlib-only reference sim `ideas/superbot-games/energy_cap_overflow_forfeiture.py` (random, math, json, hashlib) — dry-sim exit 0, all gates PASS, results-dict sha256 2e30020a…13f3ce29 (see Verifier + Dry-sim below).

## The phenomenon (one line)
Give players a stamina bar that regenerates 1 unit per period up to a cap C, and the fraction of all the stamina the game "generates" for a player that they actually get to SPEND is U(μ)=1−e^{−C/μ} — a concave function of the cap, decided by how often they log in (mean inter-login gap μ), not by how big the cap is: a frequent player (μ=60, logs ~hourly) captures ~86% of regenerated stamina, but a busy/casual player (μ=480, logs ~8-hourly) captures only ~22% — silently forfeiting ~78% of stamina the game generated for them, purely to overflow.

## The folk belief
"The energy cap is generosity — it lets players bank up to C stamina so they can come back after a break and have a full bar waiting. A bigger cap is strictly more player-friendly: raise the cap and casual players lose less to overflow, roughly in proportion." The cap is pitched (to players, and to the designer tuning retention/monetization) as a stored allowance that grows linearly with the cap and protects the player who steps away.

## The game-design thesis (reasoned to its fuller form — Q-0254 duty)
Stamina regenerates at a fixed rate (1 unit/period) but the amount you can BANK between logins is clamped at C. A player who returns after a gap of G periods finds min(G, C) stamina waiting — the overflow max(0, G−C) that regenerated while the bar was already full is gone, never spendable. So a player's lifetime stamina throughput is not the designed 1 unit/period; it is E[min(G, C)] per gap of mean length μ. For memoryless (Poisson) login behaviour — inter-login gaps iid Exponential(mean μ) — this has an exact closed form: the usable (spendable) fraction of all regenerated stamina is U(μ)=E[min(G,C)]/E[G]=1−e^{−C/μ}, and the overflow-forfeited fraction is W(μ)=e^{−C/μ}. Two consequences the folk belief misses. (1) **Concavity in the cap:** dU/dC=(1/μ)e^{−C/μ} is strictly decreasing, so once C reaches order μ the marginal usable stamina per extra unit of cap collapses exponentially — "double the cap" does NOT double usable stamina; for the casual player (μ=480) doubling C from 120 to 240 lifts usable stamina only from 22% to 39% (still forfeiting 61%). The cap is throughput-limited by login frequency, not by the cap. (2) **The tax scales with absence:** W(μ)=e^{−C/μ} rises monotonically with the login gap μ, so the player who steps away — the exact player the cap is sold to "protect" — forfeits the largest fraction, while the always-online player captures nearly all of it. The counterintuitive core: a mechanic framed as a stored allowance for the player who leaves is in fact an overflow tax whose rate rises with how long they leave — the cap converts absence into permanent forfeiture and rewards compulsive check-ins. The honest one-line fix is to decouple regen from presence: bank overflow into an uncapped "reserve" that drains at the regen rate on return (or scale the cap to a player's realized login cadence), so total lifetime stamina is regen-rate-limited (fair) rather than login-frequency-limited (regressive).

## The formal model (committed constants — sim-lab must reproduce exactly)
- Stamina regenerates continuously at 1 unit per period, banked up to cap C=120.
- A player's inter-login gaps are iid Exponential with mean μ (memoryless Poisson login process); on each login the player spends all available stamina, so the bank resets and starts refilling.
- Stamina banked between two logins separated by gap G = min(G, C); the overflow max(0, G−C) that regenerated while the bar was already full is FORFEITED (never spendable).
- **Usable fraction** for a scenario = Σ min(G_i, C) / Σ G_i over the login gaps (a ratio-of-sums estimator that converges to E[min(G,C)]/E[G]); **waste (overflow-forfeited) fraction** = 1 − usable fraction.
- Each replication draws N_GAPS=5000 gaps and records that replication's usable and waste fraction; a scenario's mean and standard error are taken over TRIALS=400 replications, se = sample-sd / √TRIALS (the P104/P105/P106 /se convention: z on the estimated mean).
- Two scenarios off the one seeded stream, in this order: FREQUENT (μ=60), then CASUAL (μ=480).

## Pinned world (committed constants)
- SEED = 20260717 (proposal-owned; SEEDLESS discipline)
- C = 120 (energy cap, regen-units — e.g. 120 minutes at 1 unit/min = a 2-hour bar)
- MU_FREQUENT = 60 (frequent player mean inter-login gap — logs ~hourly)
- MU_CASUAL = 480 (casual/busy player mean inter-login gap — logs ~8-hourly)
- N_GAPS = 5000 (login gaps per replication)
- TRIALS = 400 (independent replications)
- SIGMA_GATE = 3.0
- WASTE_MIN = 0.70 (G1 headline threshold on casual waste fraction)
- Closed-form anchors: U_frequent=1−e^{−2}=0.864665, U_casual=1−e^{−0.25}=0.221199, W_frequent=e^{−2}=0.135335, W_casual=e^{−0.25}=0.778801.

## Pre-registered gates (APPROVE iff ALL hold)
- **G1 — casual-forfeiture headline:** the casual player (μ=480, cap C=120) mean overflow-forfeited fraction W_casual ≥ WASTE_MIN=0.70 by ≥3σ (z on its standard error). The cap forfeits most of a busy player's regenerated stamina.
- **G2 — frequency-regressivity control:** casual waste fraction strictly exceeds the frequent player's (μ=60) by ≥3σ (two-sample se √(se_cas²+se_freq²)). The forfeiture is monotone in the login gap (W ∝ e^{−C/μ}) — the tax is on ABSENCE, not a cap-independent constant.
- **G3 — closed-form anchor MATCH:** the mean usable fraction U_sim matches the exact 1−e^{−C/μ} within 3σ (|z|<3) for BOTH scenarios — reproduces the exponential-overflow formula, proving G1's headline is 100% the overflow mechanism, not a sampling or estimator artifact.

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 ∧ G3 hold at their stated thresholds, in order, on the pinned world with SEED=20260717 and the committed reference verifier (the verifier's `all_pass` field encodes exactly `G1 ∧ G2 ∧ G3`). Any gate failing → REJECT (the overflow-forfeiture-tax claim is falsified for these constants). No post-hoc threshold moves; SEED is not changed; margins reported in σ on the standard-error of the estimated mean.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
- U_frequent = 0.864359 (se 0.000296) vs closed-form 0.864665 → captures ~86% of regen
- U_casual = 0.221325 (se 0.000135) vs closed-form 0.221199 → captures ~22% of regen
- W_frequent = 0.135641 (se 0.000296); W_casual = 0.778675 (se 0.000135) → casual forfeits ~78%
- **G1 casual-forfeiture:** W_casual 0.778675 ≥ 0.70 at z = 581.5691σ — PASS (a busy player forfeits >70% of regenerated stamina)
- **G2 frequency-regressivity:** W_casual 0.778675 > W_frequent 0.135641 at z = 1973.299σ — PASS (the tax rises with absence; casual forfeits ~5.7× the frequent player's fraction)
- **G3 closed-form anchor MATCH:** U_frequent |z| = 1.0304, U_casual |z| = 0.9307 (both < 3σ) — PASS (reproduces 1−e^{−C/μ})
- all_pass = true; **exit 0**
- Two runs byte-identical (deterministic under SEED).
- **Disclosed results-dict sha256 = 2e30020af5a97661506c29c962d047fb9561948098b09f5a826084b013f3ce29**
  (this is the sha256 of `json.dumps(results, sort_keys=True, separators=(",",":"))` over the results dict BEFORE its `results_sha256` self-field is added — the value the verifier prints as `Results-JSON sha256:`; the pretty-printed committed `energy_cap_overflow_forfeiture_results.json` file's own `sha256sum` is NOT this digest.)

## Verifier
Stdlib-only python3 (`random, math, json, hashlib` — no numpy), committed alongside this idea as `ideas/superbot-games/energy_cap_overflow_forfeiture.py`. Seeds once with SEED=20260717, then for each scenario (μ=60 then μ=480) runs TRIALS=400 replications of N_GAPS=5000 iid Exponential(mean μ) login gaps, banking min(gap, C) and forfeiting the overflow, recording each replication's usable and waste fraction. It computes each scenario's mean and standard error, evaluates G1/G2/G3 on the /se margin, and emits a canonical (sorted-keys, comma/colon-separated) results JSON with its sha256. Exit 0 iff all three gates pass.

Reproduce:

```
python3 ideas/superbot-games/energy_cap_overflow_forfeiture.py
```

Expected: all_pass=true, exit 0, G1 z=581.5691, G2 z=1973.299, G3 |z|=1.0304/0.9307, results-dict sha256 = 2e30020af5a97661506c29c962d047fb9561948098b09f5a826084b013f3ce29.

## Why it matters (game design)
Energy/stamina systems are the core pacing-and-monetization lever in free-to-play games (lives, hearts, gems-to-refill, timers). They are justified internally as generosity with a cap that lets players bank a comeback bar. This proposal shows the cap is an overflow tax whose rate rises with a player's login gap: for a Poisson login process the spendable fraction is the exact 1−e^{−C/μ}, so (a) raising the cap yields exponentially diminishing usable stamina once C ~ μ — "double the cap" is a near-null lever for the casual player — and (b) the forfeited fraction e^{−C/μ} is largest for the busy player the cap is sold to protect, converting absence into permanent forfeiture and rewarding compulsive check-ins. Decision rule for a designer: audit an energy cap by the login-cadence-conditional usable fraction 1−e^{−C/μ}, not the headline cap size; if lifetime stamina throughput is login-frequency-limited rather than regen-rate-limited, the system is regressive against busy players and the cap increase you shipped to "help casuals" barely moved their usable stamina. The fix is to make total lifetime stamina regen-rate-limited (an uncapped reserve that drains at the regen rate on return, or a cap scaled to realized login cadence), turning a regressive overflow tax into flat, absence-independent generosity.

## Dedup
Distinct from the nearby game priors:
- **shop-reroll-ruin** (P099): optimal-stopping / accept-threshold economics — an interior optimal reroll bar with a per-reroll cost; a single-agent spend-lever value trap. No time/overflow dynamics, no login-cadence axis.
- **streak-shield-regression** (P103): competitive-rating incidence — a win-streak-gated loss-protection resource whose supply is skill-monotone, measured by a paired cohort-uplift contrast. This proposal is NOT a rating/skill mechanic and NOT a paired-difference contrast — it is an energy-overflow throughput claim with an exact exponential closed form, the incidence axis is login FREQUENCY (μ), not skill (p).
- **pity-anticipation-collapse** (P091): gacha *pity* — a hard/soft counter guaranteeing a drop after N misses; a single-player anticipation distortion on a draw counter. This proposal is explicitly NOT a gacha-pity counter — there is no guarantee mechanic and no draw sequence; the lever is a regen cap and the mechanism is queueing overflow.
- **rubber-band-controller-instability** (P095): a discrete-time proportional (PID / rubber-band) catch-up controller with a stability boundary. This proposal is explicitly NOT a feedback controller — there is no gap signal, gain, or stability boundary; it is a static overflow-fraction result on a memoryless renewal (Poisson login) process.
- This proposal is **energy/stamina-pacing overflow economics** — how much of a regen budget a player captures as a function of login cadence and cap — with a distinct lever (regen cap C), distinct mechanism (bank-overflow forfeiture), and distinct math (the exact E[min(G,C)]/E[G]=1−e^{−C/μ} for exponential gaps), matching none of the optimal-stopping, rating-incidence, pity-counter, or feedback-controller priors.

## Model basis (declared model-dependence — the P024 discipline)
The exact 1−e^{−C/μ} closed form rests on the memoryless (Exponential/Poisson) login-gap assumption; the QUALITATIVE claims — usable fraction concave and saturating in C, forfeiture monotone increasing in μ — hold for ANY inter-login gap distribution with the stated mean (usable fraction is E[min(G,C)]/E[G], concave in C for every G because min(·,C) is concave, and increasing in a stochastically larger G), so the exponential is the clean closed-form representative, not a load-bearing artifact. The result does depend on structural assumptions: (a) regen is capped by a bank clamp with overflow discarded (the near-universal energy-system design); (b) the player spends to empty on each login (so the bank refills from 0 — partial spend only reduces the effective gap and moves toward the frequent regime, deepening no claim); (c) a single regen rate normalized to 1 unit/period (the cap C and mean gap μ are measured in the same regen-unit clock, so only the ratio C/μ matters — the pinned C=120 with μ∈{60,480} fixes C/μ∈{2, 0.25}). If overflow were banked into an uncapped reserve (the proposed fix), or the cap scaled to realized cadence, the forfeiture vanishes — which is exactly why the reserve/adaptive-cap is the pre-registered fix. The claim is scoped: under the (standard) discard-on-overflow energy cap with memoryless logins, spendable stamina is 1−e^{−C/μ} of regen — demonstrated on the pinned constants, mechanism-explained (usable = E[min(G,C)]/E[G]), not asserted as a universal law.

## Probe report (v0, 2026-07-18)

**1. What is this really?** An overflow-forfeiture claim on a free-to-play energy cap: stamina regenerates to a cap C and the overflow that accrues while the bar is full is discarded, so for Poisson logins (mean gap μ) the spendable fraction of all regenerated stamina is the exact 1−e^{−C/μ}. A frequent player (μ=60, C=120) captures ~86%; a casual player (μ=480) captures only ~22%, forfeiting ~78% to overflow.
**2. What would make it false?** If the casual player's mean overflow-forfeited fraction did NOT reach ≥0.70 by 3σ (G1), or did NOT strictly exceed the frequent player's by 3σ (G2 — no frequency-regressivity), or if the simulated usable fraction did NOT match 1−e^{−C/μ} within 3σ for both scenarios (G3 — the closed form is wrong). Any → REJECT.
**3. Simplest version that still bites?** SEED=20260717, two scenarios of 400 replications × 5000 iid Exponential login gaps at μ∈{60,480}, cap C=120; bank min(gap,C), forfeit the overflow, contrast usable/waste fractions against 1−e^{−C/μ}.
**4. What is the counterintuitive core?** The cap sold as a stored allowance for the player who steps away is an overflow tax whose rate e^{−C/μ} RISES with how long they step away — the busy player it "protects" forfeits the most, the always-online player captures nearly all of it, and doubling the cap barely helps because usable stamina saturates at 1−e^{−C/μ}. Generosity framed as a cap is regressive against absence.
**5. Where could I be fooling myself?** The exact closed form needs memoryless gaps; a heavier- or lighter-tailed gap distribution rescales magnitudes but not the concave-in-C / increasing-in-μ direction (min(·,C) is concave and the estimator is E[min(G,C)]/E[G] for any G). The ratio-of-sums estimator has O(1/N_GAPS) bias — N_GAPS=5000 makes it negligible, and G3's |z|<3 anchor match against the exact formula is exactly the guard that the estimator isn't quietly biased. "Spend to empty each login" is the deepest-forfeiture reading; partial spend only softens the tax, so the claim is not inflated by that choice.
**6. What is the honest calibration?** Dry-sim margins at SEED=20260717: G1 casual-forfeiture W_casual=0.778675 (se 0.000135) z=581.57σ; G2 frequency-regressivity gap 0.778675 vs 0.135641 z=1973.30σ; G3 anchor-match |z|=1.0304 (frequent) / 0.9307 (casual), both <3 — all clear their bars; exit 0; results-dict sha256 2e30020a…13f3ce29.
**7. What decision does it change?** Audit an energy cap by the login-cadence-conditional usable fraction 1−e^{−C/μ}, not the headline cap; if lifetime stamina is login-frequency-limited rather than regen-rate-limited, the cap is regressive against busy players and a cap bump is a near-null lever for casuals — bank overflow into an uncapped reserve (or scale the cap to realized cadence) to make generosity absence-independent.
**8. How will we know it worked?** The committed stdlib verifier reproduces the two-scenario overflow-fraction contrast under SEED=20260717 with all three gates holding (G1 W_casual≥0.70 by ≥3σ, G2 casual>frequent by ≥3σ, G3 both |z|<3 against 1−e^{−C/μ}) and the results-dict sha256 matching 2e30020af5a97661506c29c962d047fb9561948098b09f5a826084b013f3ce29.

## One-line design fix
Bank overflow into an uncapped reserve that drains at the regen rate on return (or scale the cap to a player's realized login cadence), so total lifetime stamina is regen-rate-limited (flat, absence-independent generosity) instead of login-frequency-limited (a regressive 1−e^{−C/μ} overflow tax).

**Recommendation: sim-ready**
