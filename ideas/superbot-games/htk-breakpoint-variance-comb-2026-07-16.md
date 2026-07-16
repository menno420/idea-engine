# Consistency beats raw power at a hits-to-kill breakpoint: a lower-mean, low-variance damage build kills in FEWER hits than a higher-mean, high-variance build when enemy HP sits at an integer hits-to-kill edge — the discreteness advantage RECURS on a comb at every multiple of the tight build's damage floor and reverses only once the higher mean saves a whole hit

> **State:** sim-ready
> **Class:** game-mechanics — round-18 game slot (standing ORDER 003 · rotation slot per ORDER 004 rule 3). Adjudication: sim-lab VERDICT 100.
> **Target:** sim-lab
> **Grounding:** https://github.com/menno420/idea-engine@6c36e66e41d7e021be469cfb2a7844d914b2eb37 · fetched 2026-07-16T18:59:26Z
> **Harvest source (firsthand):** the game-mechanics idea tree read FIRSTHAND @ 6c36e66 — ideas/superbot-games/, ideas/superbot-idle/, ideas/superbot-mineverse/, ideas/gba-homebrew/. The lanes ship committed combat/loot/damage ladders (gba-homebrew brineward-band-necessity, gloamline-survival-ceiling) whose kill economics are hit-count funnels; NONE models per-hit damage DISTRIBUTION or the variance-vs-mean tradeoff at an integer hits-to-kill breakpoint. The damage distributions, HP grid, cohort size and seeds are stipulated pinned constants, disclosed as calibration-not-estimate per the TRUTH bar.

## The phenomenon (one line)

Two equal-cost damage builds face an enemy killed by cumulative damage ≥ H; the HIGHER-average build (WILD) is folk-wisdom "strictly better," but the LOWER-average, low-variance build (TIGHT) kills in fewer hits whenever H sits at a hits-to-kill breakpoint — because hits-to-kill is an INTEGER (a ceiling), a low roll on the swingy build spills below the breakpoint and costs a whole extra hit that the higher average cannot buy back — and this advantage RECURS on a comb at every multiple of the tight build's damage floor, reversing only once the enemy is tanky enough that the higher mean saves a full hit.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

Hits-to-kill against a cumulative-damage target is HTK = the smallest n with sum of n per-hit damages ≥ H. For a DETERMINISTIC per-hit damage D this is HTK = ceil(H/D) — a step function of D with breakpoints at D = H/k. The player's build shapes the DISTRIBUTION of per-hit damage, not merely its mean, and the integer ceiling makes the SHAPE decisive near a breakpoint.

Take TIGHT ~ Uniform[100,110] (mean 105, minimum 100) versus WILD ~ Uniform[75,165] (mean 120 — higher — minimum 75, maximum 165), equal cost.

**At H = 100 (the one-shot breakpoint).** TIGHT's minimum roll is 100 = H, so TIGHT ALWAYS one-shots: HTK ≡ 1, zero variance. WILD's mean is higher (120), but its spread reaches down to 75; whenever WILD rolls below 100 — probability (100−75)/(165−75) = 25/90 ≈ 0.278 — it FAILS to one-shot and needs a second hit. Mean HTK: TIGHT = 1.000, WILD = 1.2785 (dry-sim, seeds [1..5], C=4000). The lower-mean build kills faster by 0.28 hits (74.9σ). The extra average damage WILD carries is wasted as overkill on the hits that land, while its variance costs a WHOLE extra hit on the hits that fall short. Consistency beats raw power exactly at the breakpoint.

**The comb (recurrence).** Because the advantage is a DISCRETENESS effect, it recurs at every hit-count lattice edge H = k·(TIGHT minimum) = k·100. At H = 300, TIGHT tiles the enemy in exactly three minimum rolls (3×100 = 300, and two hits ≤ 220 < 300), so HTK ≡ 3 with zero variance; WILD (mean HTK 3.041) occasionally spills to a fourth hit, so TIGHT wins AGAIN (+0.041, 40.3σ, all five seeds). The reversal is not a single crossing — it is a comb.

**Where the comb dies.** WILD's higher mean does buy a genuine hit-count saving once the enemy is tanky enough. At H = 500, WILD's mean HTK is 4.69 — a full hit below TIGHT's deterministic 5 — so WILD wins (−0.31, 110.6σ) even though 500 is a multiple of 100. And in a BAND INTERIOR (H = 140, between the 1-hit and 2-hit edges) TIGHT has slack — it kills in two hits with 60 damage of headroom — so WILD's mean wins there too (−0.28, 99.5σ). The sign of the paired difference over the grid {80, 100, 140, 300, 500} is therefore [+, +, −, +, −]: TIGHT wins on the lattice edges (1-hit floor at 80/100, 3-hit floor at 300), WILD wins in the interior (140) and once its mean saves a full hit (500).

**Honest falsification-and-correction (disclosed — the calibrate-against-the-world discipline).** The FIRST pre-registration of this head guessed the tight-wins window is confined to the one-shot breakpoint and the paired difference stays negative for all H above the first crossover. A seeded dry-sim FALSIFIED that: the recurrence at H = 300 is real (all five seeds, 40σ). R4 was corrected to the true discreteness-comb sign pattern BEFORE registering. This is the V098/P086 lesson working as designed — the sim, not the guess, sets the gate, and a ceiling metric produces periodic reversals a single-point registration misreads as monotone.

**Deterministic control (mechanism isolation).** Replace both builds by their MEAN (TIGHT = 105, WILD = 120 deterministic) and recompute HTK = ceil(H/mean): WILD ≤ TIGHT at every grid H (the higher-mean build weakly wins or ties everywhere). So 100% of TIGHT's wins are caused by variance at the discreteness breakpoints, never by mean.

## Pinned world (verbatim — sim-lab must reproduce exactly)

- **Enemy:** a single target with hit points H. The enemy dies when CUMULATIVE realized damage across hits ≥ H. **HTK (hits-to-kill) = the number of hits taken to reach H** (HTK ≥ 1 always — the overkill floor).
- **Builds (EQUAL cost; differ only in the per-hit damage distribution, both Uniform):** **TIGHT** — per-hit damage ~ Uniform[100, 110] (mean 105, minimum 100); **WILD** — per-hit damage ~ Uniform[75, 165] (mean 120, minimum 75, maximum 165). WILD has the HIGHER mean and the WIDER spread.
- **Cohort:** C = 4000 trials per seed. Seeds S = [1, 2, 3, 4, 5] (fresh trials per seed; report per-seed + mean).
- **HP grid:** H ∈ {80, 100, 140, 300, 500}.
- **Metric:** mean HTK over the C-trial cohort (LOWER = faster kill = better). Paired difference per seed d_s(H) = mean HTK_WILD(seed) − mean HTK_TIGHT(seed) (POSITIVE ⇒ TIGHT wins). σ = std-of-the-mean of the per-seed paired difference = stdev(d_s over the 5 seeds, sample/ddof=1) / sqrt(5); margin = |mean d| / σ.
- **CRITICAL — shared randomness / common random numbers:** for each seed use ONE `random.Random(seed)` stream; per trial pre-draw a list of at least 25 base uniforms u_i ∈ [0,1); BOTH builds compute hit i's damage as lo + u_i·(hi − lo) for their OWN [lo, hi], reading the SAME u_i. TIGHT and WILD MUST see identical per-(trial, hit) uniforms (paired comparison; else NULL). A fresh trial stream is drawn per seed.

## Pre-registered gates (ACCEPT iff ALL hold; else REJECT — order R1→R2→R3→R4)

Calibrated on a stdlib dry-sim over seeds [1..5], C = 4000, common random numbers (throwaway, NOT committed). Margins in σ = std-of-the-mean of the per-seed paired difference (n = 5).

- **R1 (the trap — consistency beats power at the one-shot breakpoint).** At H = 100, mean HTK(TIGHT) < mean HTK(WILD) for ALL 5 seeds (d_s(100) > 0 every seed), paired margin ≥ 3σ. **Calibrated:** TIGHT = 1.00000, WILD = 1.27850; mean d = +0.27850; per-seed d = [+0.27850, +0.27300, +0.29200, +0.27050, +0.27850] (all > 0); **74.90σ**. The lower-mean build kills faster.
- **R2 (honest converse — the higher mean wins once the enemy is tanky enough to save a full hit).** At H = 500, mean HTK(WILD) < mean HTK(TIGHT) for ALL 5 seeds (d_s(500) < 0 every seed), paired margin ≥ 3σ. **Calibrated:** TIGHT = 5.00000, WILD = 4.69050; mean d = −0.30950; per-seed d = [−0.30125, −0.31750, −0.31300, −0.30600, −0.30975] (all < 0); **110.60σ**.
- **R3 (well-posedness / stability sanity).** In EVERY run every realized HTK ≥ 1 (the overkill floor — no kill in fewer than one hit), AND mean HTK is monotone NON-DECREASING in H for BOTH builds across the grid. **Calibrated:** global minimum realized HTK = 1; TIGHT mean-HTK over {80,100,140,300,500} = [1.00000, 1.00000, 2.00000, 3.00000, 5.00000] (non-decreasing); WILD = [1.05470, 1.27850, 1.71930, 3.04135, 4.69050] (non-decreasing).
- **R4 (the wins are variance-at-discreteness, located on the hit-count comb — NOT raw mean).** (a) The sign of mean d(H) over the grid {80, 100, 140, 300, 500} is [+, +, −, +, −] — TIGHT wins at the hit-count lattice edges H ∈ {80, 100} (1-hit floor) and H = 300 (3-hit floor, the RECURRENCE), loses in the band interior H = 140 and where WILD's mean saves a full hit H = 500; AND (b) the deterministic control (both builds replaced by their mean, HTK = ceil(H/mean)) has HTK_WILD ≤ HTK_TIGHT at EVERY grid H, so without variance the higher-mean build never loses — proving the tight wins are caused by variance at the discreteness breakpoints, not by mean. **Calibrated:** mean d(H) = [+0.05470, +0.27850, −0.28070, +0.04135, −0.30950] = signs [+, +, −, +, −], each ≥ 40σ from zero and all-seeds-consistent (margins 49.75σ, 74.90σ, 99.54σ, 40.28σ, 110.60σ); deterministic HTK (TIGHT 105 / WILD 120) = 1/1, 1/1, 2/2, 3/3, 5/5 (WILD ≤ TIGHT at every H).

**Disclosed expected landing: ACCEPT** (all four hold on the dry-sim). Falsifiability axes: if the two builds saw INDEPENDENT reader draws the paired comparison is confounded by draw noise → NULL; if the deterministic control ever showed TIGHT STRICTLY winning at some H, the "variance-driven" claim is false → REJECT; if any gated sign flips under independent re-derivation, R4 → REJECT. Honest failure mode disclosed above: the first R4 registration ("d stays negative above the crossover") was falsified by the dry-sim's H = 300 recurrence and corrected to the comb pattern before registering.

## Disclosed verifier

Committed stdlib-only Python (`random`, `statistics`, `math`), fixed seeds S = [1..5], C = 4000, common random numbers (one per-seed stream, ≥25 pre-drawn uniforms per trial shared by both builds), implementing the two Uniform builds and the cumulative-damage funnel. It prints the {H × build} mean-HTK table (per-seed + mean), the per-seed paired differences d_s and their σ-margins at each H, the R1 verdict at H = 100 and R2 verdict at H = 500, the R3 floor + monotonicity checks, the R4 sign pattern over the grid plus the deterministic-control table, and ONE ruling ACCEPT/REJECT under the pre-registered R1→R2→R3→R4 order. **Fixture** = the seed-1, H = 100, first-20-trial HTK under BOTH builds on identical draws (committed alongside). **NULL condition:** the per-hit draw is under-specified so TIGHT and WILD see different uniforms (the shared-randomness requirement violated) — the comparison is then confounded by draw noise, not build.

## Why it matters (game-ops)

A designer or player choosing between a consistent weapon (tight damage) and a high-roll weapon (higher average, swingy) hears one folk belief: "higher average DPS is strictly better." This head prices exactly when that is WRONG. Against an enemy whose HP sits at a hits-to-kill breakpoint for the consistent build — a multiple of its minimum roll — consistency wins: a low roll on the swingy weapon costs a whole extra hit that the higher average cannot buy back, because HTK is an integer (R1, and the comb recurrence R4). The higher average earns its keep only when the enemy is tanky enough that the mean saves a WHOLE hit (R2). The actionable rule: match the weapon to the enemy — consistent damage for breakpoint-HP targets (bosses tuned to round numbers, one-shot thresholds), high average for tanky targets. And for designers: enemy HP tuned to round multiples of a common damage floor silently rewards low-variance builds — a balance lever most tuning passes miss, and one this head makes measurable.

## Dedup

Tree-wide read of the game lanes @ 6c36e66. No prior game idea prices damage VARIANCE, hits-to-kill, or an integer HTK breakpoint:
- **superbot-games:** combo-grace-budget-cliff (P083) is a shared grace-window BUDGET cliff (floor(B0/ℓ)+1); explore-action-pacing, mining-booster-bypass-throttle, menu-width-leverage-inversion are faucet / throttle / menu-reward heads. None touches per-hit damage or HTK.
- **superbot-idle:** owned-track-launch-flag-dial (P079), event-fold-visibility-floor (P077), prestige-reset-policy, generator-purchase-path, idle-economy-kernel — idle-economy heads, no combat distribution.
- **superbot-mineverse:** badge-saturation, max-depth-hint-visibility-clip (P075), snapshot-stale-indicator, write-contract-rate-tier-degeneracy — read/write-contract heads.
- **gba-homebrew:** brineward-band-necessity (loot/price ladder), gloamline-survival-ceiling (night ramp), wickroad-stale-ink (stale-information bet) — none models a per-hit damage distribution or a variance-vs-mean kill tradeoff.

NONE models per-hit damage distribution, cumulative-damage hits-to-kill, or the variance-vs-mean tradeoff at an integer kill breakpoint. Distinct also from the venture P086 saturation crossover: P086's reversal is a SMOOTH saturation at a ceiling (r_max) and crosses ONCE as a budget allocation splits; this reversal is a DISCRETENESS effect (the integer ceiling of HTK), it RECURS on a comb rather than crossing once, and the deciding variable is VARIANCE, not budget. This is the pipeline's FIRST head to price a per-hit damage distribution against an integer hits-to-kill lattice.

## Probe report (v0, 2026-07-16)

> Single-pass battery (panel not escalated: self-contained game-mechanics probe, the sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide read of all four game
> lanes confirmed no prior head prices damage variance, hits-to-kill, or an integer HTK breakpoint
> (the nearest game heads are budget/faucet/throttle/contract/loot-ladder shapes, none a per-hit
> distribution). (b) **kill test NOT triggered** — no recorded drop of a damage-distribution head on
> any card. (c) **harvest source read FIRSTHAND** — the game-mechanics idea tree @ 6c36e66; the
> damage distributions / H grid / C / seeds are DISCLOSED as stipulated pinned constants
> (calibration-not-estimate), since no committed combat-damage table pins them. (d) **grounding
> reachability** — HONEST: the phenomenon is a stdlib cumulative-damage sim any verdict session runs
> cold; the game tree grounds the WHY (hit-count kill economics are the lanes' recurring combat
> shape), not the distribution constants. All registered numerals were produced live this session by
> a throwaway stdlib dry-sim (seeds [1..5], C = 4000, common random numbers; NOT committed), and one
> registered claim (the R4 comb) was CORRECTED after the dry-sim falsified the initial guess.

**1. What is this really?** A pre-registered head-to-head between two equal-cost damage builds —
TIGHT (low-variance, lower mean) and WILD (high-variance, higher mean) — over a cumulative-damage
hits-to-kill funnel, measured across an HP family H ∈ {80, 100, 140, 300, 500}. The claim is a
VARIANCE-AT-DISCRETENESS reversal: the lower-mean build kills faster at hit-count breakpoints
because the integer ceiling of HTK turns a low roll into a whole extra hit, and the advantage
recurs on a comb at multiples of the tight build's damage floor.

**2. What is the possibility space?** (i) Don't run it — the round-18 game slot goes unserved and
the pipeline stays thinner toward V100. (ii) A folklore retelling ("consistency vs raw DPS") —
retells the intuition without the exact comb, the breakpoint locations, or the deterministic
control that isolates variance from mean. (iii) A single-HP snapshot — misses that the ranking is
a COMB across H; one H decides nothing (and mis-registering one point as monotone is exactly the
trap that falsified this head's first R4). (iv) This head: a seedful funnel-sim sharing each trial's
draws across both builds, four pre-registered gates, a deterministic control, a disclosed fixture.
(v) Over-scope (non-uniform damage laws, crit distributions, multi-target cleave, per-enemy HP
populations, armor/mitigation) — each a named follow-up, none in scope.

**3. What is the most advanced capability reachable by the simplest implementation?** One ~120-line
stdlib file (`random` only): C trials × shared per-hit uniforms, two builds' [lo,hi] ranges, a
cumulative-damage funnel, run over 5 seeds × 5 HP values, printing the {H × build} mean-HTK table,
the paired σ-margins, the comb sign pattern, and the deterministic control — that single kernel
yields the breakpoint trap (R1), the multi-hit converse (R2), the floor + monotonicity sanity (R3),
and the variance-driven comb with its mechanism control (R4) in well under a second per
configuration.

**4. What breaks it? (assumptions made explicit)** (a) **Shared randomness is LOAD-BEARING** — if
the two builds draw independent per-hit streams, the paired comparison is confounded by draw noise,
not build; the disclosed verifier NULLs if the draw is under-specified. (b) **The Uniform damage
law is a deliberate choice** — it makes the minimum roll (and thus the one-shot floor) exact and the
comb clean; a normal or triangular law would round the corners and move the margins, and that is a
named follow-up, not a claim about true weapon damage laws. (c) **The distribution constants are
stipulated, not fit** — the head prices the phenomenon UNDER the pinned distributions, not a claim
about a real game's damage tables. (d) **R4's deterministic control is the mechanistic core** — if
variance-removed play ever showed TIGHT strictly winning, the "variance-driven" story is false and
the head is REJECTED.

**5. What does it unlock?** A measured, citable answer to "consistent weapon or high-roll weapon?"
— directly actionable because it corrects the folk belief and hands the player a rule: consistent
damage for breakpoint-HP targets (round-number bosses, one-shot thresholds), high average for tanky
targets where the mean saves whole hits. For designers it exposes a hidden lever: round-number
enemy HP silently rewards low-variance builds.

**6. What is the cheapest experiment that decides it?** The head IS the cheapest deciding
experiment: the {H × build} table settles all four gates in one short run. The single cheapest
sanity probe is the seed-1, H = 100, first-20-trial fixture: TIGHT is 1 on every trial while WILD
needs a 2nd hit on the trials where it rolls under 100 — visible by counting before any statistic.

**7. What would make this a mistake to run?** If the builds saw different per-hit draws (confounds
build with noise — the pre-registered NULL guards exactly this), if the distribution constants were
presented as an ESTIMATE rather than a stipulated calibration (the TRUTH bar — disclosed), or if the
disclosed ACCEPT made the run theater. It does not: the value is the independent hermetic
re-derivation (the verdict session re-implements the funnel and must reproduce the comb sign pattern,
the R1/R2 margins, and the deterministic control from scratch), and REJECT is genuinely reachable
(a mis-shared draw, a failed control, or a flipped sign each sink it).

**8. How will we know it worked?** A committed sim-lab report with: the {H × build} mean-HTK table
per-seed and mean over S = [1..5]; the R1 margin at H = 100 and R2 margin at H = 500 in σ; the R3
floor (min HTK = 1) and monotonicity check; the R4 comb sign pattern over the grid with the
deterministic-control table; the seed-1, H = 100, first-20-trial fixture matching the committed
values; and ONE ruling ACCEPT/REJECT under the pre-registered R1→R2→R3→R4 order.

## Gate power + margin ledger

Dry-sim margins in σ units (σ = std-of-the-mean of the per-seed paired difference, n = 5 seeds,
C = 4000, common random numbers; NOT committed — sim-lab re-derives):
- **R1 (H = 100, TIGHT < WILD):** mean d = +0.27850 hits, **74.90σ** (need ≥ 3σ). All 5 per-seed diffs strictly positive.
- **R2 (H = 500, WILD < TIGHT):** mean d = −0.30950 hits, **110.60σ** (need ≥ 3σ). All 5 per-seed diffs strictly negative.
- **R3:** floor holds (global min HTK = 1); both mean-HTK sequences non-decreasing over {80,100,140,300,500}.
- **R4:** comb sign pattern [+, +, −, +, −] with per-H margins [49.75σ, 74.90σ, 99.54σ, 40.28σ, 110.60σ] (all ≥ 40σ, every seed agreeing on sign); deterministic control HTK 1/1, 1/1, 2/2, 3/3, 5/5 (WILD ≤ TIGHT everywhere), isolating variance as the cause.

Every gated margin clears 3σ by ≥ 13× at C = 4000, so no cohort increase is needed; the signs are all-seeds-consistent, so the disclosed ACCEPT is reachable and REJECT remains live via a mis-shared draw, a failed deterministic control, or a flipped comb sign.

**Recommendation: sim-ready**
