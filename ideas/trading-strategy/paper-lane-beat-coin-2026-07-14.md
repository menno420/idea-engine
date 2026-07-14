# The paper lane's BEAT coin: trade P&L cancels out of the committed cycle-window verdict — and the count grammar cannot see skill at first-year n

> **State:** sim-ready
> **Class:** product (pipeline rotation — the standing ORDER 003 FLEET-BACKLOGS slot, round 11 OPENER; harvest source rotated to a repo this slot has NEVER drawn: trading-strategy — slot rounds 1–10 drew websites ×2, superbot ×2, substrate-kit ×2, fleet-manager, curious-research ×2, superbot-mineverse)
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264 pipeline; routing is the manager's per Q-0260, this repo never edits trading-strategy files)
> **Grounding:** https://github.com/menno420/trading-strategy@d857e50ad7bc32bed5b2999cce16b4bf8a37246e · fetched 2026-07-14T03:16:41Z
> (FIRSTHAND: add_repo + shallow clone this session, first attempt succeeded — no wall; every harvested constant below read from that working tree; secondary anchor sweep at idea-engine HEAD `3ae82cb` + sim-lab READ-ONLY `626d16e`; every MODEL constant below is invented-but-pinned in this file, zero repo/network reads at verdict time — the P017–P056 hermetic precedent)
> **Origin:** standing ORDER 003 (continuous new ideas per repo) under ORDER 004 rule 3 (deliberate lane rotation, "fleet backlogs → venture's book/product space → game mechanics → COMPLETELY UNRELATED domains"); round 10 closed fully served (fleet backlogs → P053 #379, venture → P054 #382, game mechanics → P055 #385, COMPLETELY UNRELATED → P056 #387), so round 11 REOPENS at fleet backlogs — this head.

**Second-tap disclosure (repo level, not slot level):** trading-strategy has been tapped three times by the pipeline — P022 → V024, P026 → V028, P034 → V036 — but all three were the VENTURE slot's trading half, and all three priced the RESEARCH-ROUND selection machinery (xsec keep-margin selection noise; round-3 breadth-budget q99 power; drift-regime observability for the trust gate). This head is the FLEET-BACKLOGS slot's first draw of the repo and prices a document none of them touched: the forward PAPER LANE's pre-registered grading grammar. Zero shared machinery, argued in Relations below.

## The committed claim (harvested head)

`docs/paper-lane-protocol.md` @ `d857e50` — the lane's binding, pre-registered forward paper-trading protocol (sole subject `donchian × AAPL × daily`, params frozen `{"entry": 15, "exit": 5}`, ledger `experiments/paper/ledger.md` currently one WATCH row, lane FLAT) — commits in §7 a per-window verdict grammar:

- "**BEAT** iff strategy cycle return > B&H cycle return, strictly." Ties and late commits are MISS (§9 A5/A3).
- The comparison runs over the **cycle window** (previous exit fill → this exit fill): "Strategy return over the cycle = flat (0%) outside the outcome window plus the trade P&L inside it; benchmark = $10,000 of AAPL bought at the cycle start, sold at this exit fill, same costs both sides."
- And the committed justification (§9 A6): the cycle comparator is "the meaningful reading that is *less* favorable to the strategy, since every flat day (warm-up included) is charged at full B&H opportunity cost".
- Costs: "5 bps slippage + 1 bps commission per side" — `DEFAULT_SLIPPAGE_BPS = 5.0`, `DEFAULT_COMMISSION_BPS = 1.0` (`src/trading_lab/config.py:60–61` @ `d857e50`).
- Committed trade rate: "17 trades in ~18 months on the holdout read" with "n will be single-digit for months. Verdicts are counted, not tested" (§7, `docs/paper-lane-protocol.md:217`).

The grammar is decision-shaped and frozen before data — exactly right by the lane's own doctrine. What was never measured is what the grammar can DO: what a BEAT actually conditions on, where the zero-skill coin sits, and whether counting BEATs at the committed trade rate can distinguish skill from drift within any horizon the owner would recognize.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

Write a cycle as F flat days followed by an in-position segment with gross market return R_T over its held days, R_F = gross market return over the flat segment. Per §7: strategy cycle wealth factor = R_T × (cost factor both sides); benchmark = R_F · R_T × (the SAME cost factor both sides — same bars, same fills, same cost model, per the protocol's own text; inside the outcome window strategy and B&H "hold the identical asset at identical fills and costs", §9 A6). Then

**BEAT ⟺ R_T · C > R_F · R_T · C ⟺ R_F < 1.**

The trade's own P&L — the thing the lane watches — cancels EXACTLY out of the verdict. A closed window grades BEAT precisely when the MARKET FELL over the flat segment of its cycle. The §7 grammar is a flat-segment market-direction coin. Skill can only enter through timing correlation: being flat when the market falls. Two measurable consequences follow:

1. **The coin's null level is set by the MEDIAN of a product, not the mean.** The A6 "full B&H opportunity cost" charge is real at expectation level (E[R_F] = E[X]^F > 1 under positive drift — the flat days do cost expected dollars). But BEAT thresholds the REALIZED R_F at 1, and volatility drag puts the median of a gross-return product below its mean: for ±1%-type daily moves, the even-split path already lands R_F = (1 − 10⁻⁴)^(F/2) < 1. At an AAPL-like drift the zero-skill coin sits ABOVE 1/2 — a null trader BEATs more often than not while losing expected money to the benchmark. Win-rate and EV point in opposite directions; the grammar counts win-rate.
2. **At the committed trade rate, counts are powerless against honest skill.** With single-digit n for months and per-window probabilities that differ by ~0.11 between null and a pinned real skill, the exact best test at size 1/20 has ~4% power at n = 8 — and needs n* ≈ 56 windows (~5 years at 17-per-18-months) to reach 50%.

None of this contradicts the protocol's §8 firewall (counts never promote — that rule comes out VINDICATED, with numbers). What it prices is the INTERPRETATION surface: weekly review notes reporting "k BEAT of n" invite a majority-read that the null coin already produces by itself.

## Pinned model (committed constants — market/cycle/skill all invented-but-pinned, exact rationals)

- **Market:** i.i.d. daily gross return X = 101/100 w.p. `p_up`, = 99/100 w.p. 1 − `p_up` (per-day move s = 1/100 ≈ 15.9%/yr annualized — AAPL-like scale; sensitivity pair s ∈ {1/200, 1/50}, reporting-only). Drift grid `p_up` ∈ {1/2 (**ZERO**, control), 13/25 (**COMMITTED** decision cell, drift 1/2500/day ≈ +10.6%/yr), 27/50 (**DOUBLE**, ≈ +21%/yr)}.
- **Cycle structure:** flat length F from pmf {6: 1/4, 12: 1/2, 24: 1/4} (mean 27/2), in-position length T from pmf {4: 1/4, 8: 1/2, 16: 1/4} (mean 9), F ⊥ T, i.i.d. across cycles — mean cycle 45/2 trading days ⇒ 378/(45/2) = 16.8 windows per 18 months (378 trading days), matching the committed "17 trades in ~18 months" rate. The identity makes T decision-irrelevant (proven in-sim); it enters only this calibration and the EV reporting rows.
- **Skill:** the conditional flat-day up-probability is `p_up` − δ (in-position days correspondingly up-tilted, reporting-only — the identity routes every skill channel through the flat-segment law). δ = 0 (**NULL** world), δ = 1/25 (**SKILL** decision world), δ ∈ {2/25 strong, −1/25 anti — the donchian-shaped direction: momentum entries follow rises, tilting flat segments UP} reporting-only.
- **Protocol accounting, quoted:** 6 bps per side both strategies, $10,000 fixed notional, BEAT strict, ties MISS. Identity leg: under equal multiplicative per-side cost factors the cancellation is EXACT; the fixed-notional dollar variant's second-order cost asymmetry (benchmark sell cost charged on appreciated notional) is computed exactly per lattice point and its maximum absolute effect on the BEAT indicator reported (drafting expectation: zero sign flips anywhere on the support — verified or refuted in-sim).
- **Grading horizon grid:** n ∈ {8 (**decision** — the first-year closed-window floor implied by the committed rate net of the protocol's own warm-up forfeit and open-window truncation), 16, 34} reporting; plus the n* rows (minimal n with NP power ≥ 1/2 and ≥ 4/5).
- **No-tie theorem:** 101^k · 99^(F−k) = 100^F is impossible for any 0 ≤ k ≤ F (101 is prime and 101 ∤ 100^F), so P(R_F = 1) = 0 exactly and §9 A5's tie rule never fires in-world — asserted symbolically, checked over the full support.
- **Arm A (DECISION arm, seedless):** exact `fractions.Fraction` arithmetic — per-F BEAT thresholds k*(F) = max{k : 101^k 99^(F−k) < 100^F} (= F/2 exactly at F ∈ {6, 12, 24}), exact binomial CDFs for B(δ, drift) = P(BEAT), exact one-sided Neyman–Pearson count tests (smallest critical c with null tail ≤ 1/20, non-randomized/conservative — the grammar counts), exact power rows, exact EV-per-cycle rows E[Δ$] ∝ E[R_T]·(1 − E[R_F]); byte-identical across process runs.
- **Arm S (confirmation, seeded):** MC with `random.Random(20261365)` — N = 200,000 cycles per (drift, δ) decision world, pinned draw order (F draw, then F daily coins; common random numbers replaying each cycle across δ worlds), BEAT evaluated through the protocol arithmetic (both cost accountings), agreement gate |EST − EXACT| ≤ 1/100 absolute AND ≤ 4·SE on every decision B cell; plus 50,000 simulated 8-window seasons confirming the power row within the same gate. Stability seed 20261366 (N = 20,000, twin independently-written decision evaluators). Reporting seed 20261367 (s pairs, F-mix short-/long-heavy pairs {6: 1/2, 12: 3/8, 24: 1/8} / {6: 1/8, 12: 3/8, 24: 1/2}, δ = 2/25 and −1/25, n ∈ {16, 34}, EV rows, dollar-accounting bound). Aux seed 20261368 never read by any leg.
- Seeds 20261365–368 strictly above the P056 high-water 20261364 (re-swept this session — see Relations).

## Decision rules (pre-registered; evaluated in this order)

**REJECT** — "the committed cycle-window grammar fails as a first-year skill meter at the lane's own committed constants: the verdict statistic excludes trade P&L by exact identity, the null window coin is not conservative, and the count grammar cannot see honest skill at first-year n — weekly `k BEAT of n` lines must carry the measured null coin or they invite a false read in BOTH directions." Fires iff ALL of:
- (a) the identity gate proves BEAT ⟺ R_F < 1 with ZERO exceptions over the full enumerated lattice (every F in support × every k ∈ {0..F}) under the multiplicative cost accounting, AND
- (b) B(NULL, COMMITTED drift) ≥ 13/25, AND
- (c) exact NP power at n = 8, size ≤ 1/20, NULL vs SKILL (δ = 1/25) at the committed drift < 1/2, AND
- (d) Arm S confirms within the agreement gate on every decision cell.

Checked FIRST: the costly error is the owner (or the lane's weekly reviewer) reading an early BEAT majority as edge — or an early BEAT minority as damning — when the coin's null level and the test's power make both reads noise; the §8 firewall guards PROMOTION but nothing guards INTERPRETATION.

**INVALID** (controls misbehaving — report, no ruling): F1 pmf identities (F/T pmfs sum to 1; E[X] − 1 = s(2·p_up − 1) exact per world; mean cycle 45/2; implied windows/18mo ∈ [15, 19]); F2 the no-tie primality theorem + k*(F) = F/2 at every even F in support; F3 the ZERO-drift closed form B(NULL, ZERO) = 20656327/33554432 reproduced exactly; F4 monotonicity (B(NULL, ·) non-increasing in drift; B(δ, ·) increasing in δ at every drift; power non-decreasing in n and in δ); F5 hand fixture (F = 2 world: k*(2) = 1, P(BEAT) = 1 − p_up² by hand, matched exactly); draw-count sentinels; twin evaluators disagreeing; any Arm-S agreement breach.

**APPROVE** — "the grammar is a working first-year skill meter and the A6 'less favorable' reading holds at window level": NP power ≥ 4/5 at n = 8 AND B(NULL, COMMITTED) ≤ 1/2 AND the stability leg reproduces the ruling through twin evaluators. Mutually exclusive with REJECT by arithmetic.

**NULL** (anything else — every axis a finalized, citable finding, never a re-run request):
- power-straddle: power at n = 8 ∈ [1/2, 4/5) — the finding is the exact (n*₅₀, n*₈₀) pair in windows and calendar years at the committed rate;
- coin-straddle: B(NULL, COMMITTED) ∈ (1/2, 13/25) — the finding is the exact coin with its drift flip boundary (the DOUBLE world's B ≈ 0.5012 shows where the conjunct dies);
- sensitivity-conditional: a reporting world (s pair, F-mix pair, anti-skill δ) landing a decision conjunct across its band edge — named, never ruling;
- arm disagreement surviving the INVALID gate's diagnosis.

**Expected landing, DISCLOSED per the P048–P056 norm (the sim re-derives from scratch and must not trust these):** REJECT on all four conjuncts, at the drafter's exact/float harness (run this session): (a) structural, zero exceptions expected; (b) B(NULL, COMMITTED) = 1985628207794352919031012090343552/3552713678800500929355621337890625 ≈ **0.5589** ≥ 13/25 = 0.52; (c) power at n = 8 ≈ **0.0406** (critical c = 8: the size-1/20 test needs EIGHT BEATs of eight) < 1/2; B(SKILL) ≈ 0.6701. Falsifiability real: the DOUBLE-drift world lands B ≈ 0.5012 — BELOW conjunct (b)'s edge and inside the coin-straddle NULL band, so (b) genuinely discriminates on drift; the ZERO-drift control B = 20656327/33554432 ≈ 0.6156 exactly separates the vol-drag effect from drift (fair-EV world, 62% null coin); strong skill δ = 2/25 still posts power ≈ 0.12 < 1/2, so (c) is not an artifact of a weak alternative; n*₅₀ ≈ 56 windows (~5 years), n*₈₀ ≈ 124 (~11 years) — float drafting values, recomputed exactly in-sim.

## Consequence (pre-registered; routing is the manager's per Q-0260 — this repo edits no trading-strategy file, nothing here builds, publishes, spends, or touches any market)

- **REJECT** → paste-ready note for the lane, three lines: (i) every weekly aggregate `k BEAT of n (m weeks reviewed, f FLAT)` line gains the measured null-coin companion (a BEAT majority is the null EXPECTATION at AAPL-like drift, not evidence — and a BEAT minority is likewise not damning); (ii) the §8 promotion firewall gains its measured basis (counts could not promote even in principle before n* ≈ 56 windows ≈ 5 years — the firewall is vindicated, not violated); (iii) the free upgrade, named: the ledger already commits every signal-side close and fill, so an EV-grade companion column (cycle dollar difference vs B&H — the mean-level number the A6 charge actually prices) can ride the existing rows at zero new data — adopting it is a lane/owner intent call, never ruled here.
- **APPROVE** → §7's grammar and A6's "less favorable" claim gain their measured basis; the weekly notes stand as written.
- **NULL** → the named axis ships with its exact boundary (n* pair, coin flip boundary, or the sensitivity edge) — plus the free live probe: the lane's own ledger accrues real windows on its own clock; a year-1 re-read against the measured coin costs one file read.

**Application guard (two conditions, the V049/V053 pattern):** the verdict conditions on (1) the §7 cycle-comparator grammar, §9 A5/A6 resolutions, and the 6 bps/side · $10,000-notional accounting as committed @ `d857e50` — materially amended protocol text means re-run, not reuse; (2) the lane's forward dataset being empty-to-single-digit (ledger at `paper-0001` WATCH @ `d857e50`) — once real closed windows exist in force, the measured coin should be re-based on realized cycle structure rather than the pinned F/T pmfs.

## Boundaries (named, direction stated)

- **i.i.d. two-point market:** real daily returns are fat-tailed and mildly autocorrelated. The identity theorem (a) is distribution-free — it needs only §7's equal-costs-both-sides structure and shared in-window fills. The coin LEVEL is model-bound: fatter tails at equal drift push MORE of the mean into rare large up-days, dropping the median further — B0 moves AWAY from 1/2, the REJECT direction. Autocorrelation (momentum regimes) is the named most-likely-to-flip alternative for conjunct (b) and is bracketed qualitatively, not simulated.
- **The skill model is a conditional tilt, not a donchian re-implementation:** deliberately — the identity proves every long/flat rule's skill reaches the verdict ONLY as its achieved flat-day return tilt, so δ IS the general parameterization. The donchian-shaped direction (momentum entries follow rises → flat segments tilt UP → anti-skill δ = −1/25) rides as a reporting leg.
- **Truncation and lapses:** open windows stay ungraded and late commits are auto-MISS (§5/§6) — both shrink effective n or deflate observed BEATs, the REJECT direction; ignored in the decision arm, direction stated.
- **What this head does NOT price:** the strategy's actual edge (the holdout already ruled: CONFIRMED, not significant, t = 0.02), any promotion question (owner-gated by §8, untouched), and any real-money implication (none exists anywhere in this lane by construction).

## Relations (dedup argued)

- **P022 → V024 / P026 → V028 / P034 → V036** (the repo's three prior taps, all VENTURE-slot trading half): all price the RESEARCH-ROUND selection machinery — best-of-N keep-margin selection noise, breadth-budget q99 power, drift-regime observability for the trust gate. Zero shared machinery with the paper lane's forward grading grammar: no cycle comparator, no BEAT/MISS law, no forward-window power question. P026 is the nearest METHOD kin (a power analysis) — its object is the research-round shortlist bar under multiplicity; this head's is a pre-registered forward-grading comparator's structural identity + first-year count power. Different document, different consumer decision, different model class.
- **P053 → V064** (detection probability of a cron point-probe): method kin only (probability-of-seeing under a committed cadence); no renewal/market structure, no comparator identity, no hypothesis-test power object.
- **P054 → V065** (exact decision-tree over committed alternatives) and **P056 → V067** (median-vs-mean via size-biasing): method kin on "exact-Fraction pricing of a committed rule"; zero shared fixtures or consumers. The median-vs-mean mechanism here (vol drag on a product threshold) is distinct from P056's length-biased sampling law.
- **Sweep:** tree-wide `rg -i 'paper.?lane|BEAT.?MISS|cycle window|opportunity cost|win.?rate|B&H|buy.?and.?hold'` (bootstrap.py/.substrate excluded) at HEAD `3ae82cb` + sim-lab READ-ONLY @ `626d16e`: hits only the three trading-strategy taps' own prose (research-round machinery, argued above) and incidental fleet prose. No proposal P001–P056 and no verdict V001–V067 (V067 in flight = P056's inspection-paradox world, zero overlap) prices a grading comparator, a win-rate-vs-EV split, or forward-window count power.
- **Seed sweep:** boundary-aware regex `(^|[^0-9])2026[0-9]{4,6}([^0-9]|$)` over this tree @ `3ae82cb` and sim-lab @ `626d16e` (results.json excluded): max genuine allocations 20261364 (P056 aux) / 20261356; the standalone numerals 20261542/20261833/202670087 are Fraction-numerator and decimal-fraction digit substrings inside results.json-quoting text — data, not seeds (the P046–P056 sweep-recipe trap re-confirmed). This head allocates **20261365–368**.

## Probe report (v0, 2026-07-14)

> Single-pass battery (panel not escalated: self-contained pricing of pinned
> committed constants, sim is report-only evidence, no spend/publish/market/
> irreversible surface — README § probe battery). Verify-first ran FIRST,
> live this slice: (a) **source verified FIRSTHAND** — add_repo + shallow
> clone of trading-strategy succeeded on first attempt (no wall to record),
> every constant read from the working tree @ `d857e50` (protocol §§1–9,
> config.py:60–61, ledger WATCH row, the :217 trade-rate line). (b)
> **dedup** — the Relations sweeps above at `3ae82cb` / `626d16e`; PROPOSALs
> 001–056 (headers + idea slugs re-read) and VERDICTs V001–V067 swept, V067
> in flight = P056's world. (c) **kill test NOT triggered** — no prior head
> prices a grading comparator or forward count power. (d) **feasibility +
> honesty arithmetic checked** — the drafting harness was actually RUN this
> session (exact Fractions for the B cells and the n = 8 power; float only
> for the n* scan) and its landing DISCLOSED (REJECT on all conjuncts, with
> the DOUBLE-drift world proving conjunct (b) falsifiable — the P048–P056
> norm).

**1. What is this really?** A pre-registered pricing of a binding protocol's own grading grammar at its own committed constants: an exact cancellation theorem (the verdict is trade-P&L-blind), the exact null level of the resulting flat-segment coin across a drift grid, and the exact power of the committed "verdicts are counted" grammar at the committed trade rate — REJECT-first, dual-arm, byte-identical across process runs.

**2. What is the possibility space?** (i) Don't run it — the lane's weekly review notes start accruing `k BEAT of n` lines whose null behavior nobody has priced, and the first BEAT majority gets read as signal. (ii) Eyeball it — the cancellation is exactly the kind of algebra that hides in prose ("same costs both sides" reads as fairness, not as cancellation), and the median-vs-mean split is the classic trap the fleet's own P056 verdict just priced in another costume. (iii) Wait for real windows — n arrives at ~17/18-months; the coin question is answerable NOW, the data route takes years (that is finding #3). (iv) Price the strategy instead — the holdout already ruled and is SPENT; re-pricing it is forbidden by the protocol this head respects. (v) This head: hermetic, exact, pre-registered — the pipeline's standing shape.

**3. What is the most advanced capability reachable by the simplest implementation?** One stdlib file + one fixture JSON yields: a distribution-free structural theorem about a live grading rule; the exact null-coin surface B(drift, δ, F-mix); the exact power/n* table that converts "verdicts are counted, not tested" into calendar years; and a reusable kernel — win-rate-vs-EV pricing of a committed comparator — that transfers to every fleet surface that grades by thresholded comparisons (websites healthcheck PASS lines, venture kill-clock BEAT-style checkpoints, any future paper lane).

**4. What breaks it? (assumptions made explicit)** (a) the i.i.d. two-point market — identity distribution-free, coin level not; fat-tail direction stated (REJECT-ward), autocorrelation named as the flip alternative. (b) The δ skill parameterization — justified BY the identity (all skill flows through the flat-segment law); the anti-skill donchian direction rides as a reporting leg. (c) The n = 8 first-year pin — derived from the committed 17-in-18 rate net of the protocol's own warm-up forfeit; n ∈ {16, 34} report the horizon curve either way. (d) Protocol drift — the application guard conditions on §7/§9/cost text @ `d857e50`; amended text means re-run. None is hidden; each is an axis, a direction, or a pinned quote.

**5. What does it unlock?** The lane's weekly grading output becomes readable: either the notes gain the measured null-coin companion and the owner can never be misled by an early streak (REJECT), or the grammar is ratified as a working meter (APPROVE), or the exact boundary ships (NULL). Plus the pipeline's first win-rate-vs-EV verdict row and the count-power kernel.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing external at verdict time — fully hermetic; every harvested constant is committed at the FIRSTHAND pin `d857e50`. Cheapest kill BEFORE simming: a prior verdict pricing this comparator (none — V001–V067 swept), or the protocol already carrying a null-coin caveat (it does not — §7's only n caveat is the no-significance rule, which is about the strategy's evidence, not the coin's null level). Cheapest confirm AFTER: the lane's own ledger — real closed windows accrue on their own clock and a year-1 re-read against the measured coin is one file read.

**7. Which lane should build it — and what does it displace or duplicate?** sim-lab builds and runs the sim (the Q-0264 verify seat — this file is its intake spec); trading-strategy consumes the verdict as a weekly-note companion line + the vindicated-firewall citation, routed by the manager per Q-0260 (the lane is PARKED with weekly Friday grading only — the verdict lands before the first graded window can even exist, which is exactly the window to fix interpretation). It displaces nothing in flight (V067 holds the inspection-paradox world; the queued SIM-REQUEST batch covers other repos) and duplicates nothing (Relations above).

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one stdlib Python file (exact-Fraction lattice/binomial arm + seeded MC arm + gates + twin evaluators), one fixture JSON (the market/cycle/skill grids, the §7/§9/cost quotes verbatim @ `d857e50`, the accounting definitions, band constants (13/25, 1/2, 4/5, 1/20, the 1/100 + 4·SE agreement gates), the F1–F5 fixtures, per-leg trajectory counts, seeds 20261365–368), one REPORT.md with the identity proof outcome, the B surface, the power/n* table in windows AND calendar years, the EV rows, the ruling, and the named-axis/probe line on NULL — the standing INTAKE/VERDICT grammar, nothing else.

**Recommendation: sim-ready** — REJECT condition first as pre-registered above; expected landing disclosed and non-binding; honest nulls are findings.
