# Are the momentum KEEP margins beyond selection noise? A burden-priced Sharpe bar for research round 3

> **State:** sim-ready
> **Class:** product · **Target:** `menno420/trading-strategy` (verdict consumers: the
> trading lane's research-round pre-registration defaults — the round-3 shortlist bar —
> and the manager's routing call on the owner-proposal residual slice the section's own
> parked capture names; verification target `menno420/sim-lab` per the Q-0264 pipeline)
> **Grounding:** https://raw.githubusercontent.com/menno420/trading-strategy/7f7ca07a293872577fac0cbe835ef0bec728b3b4/control/status.md@7f7ca07 · fetched 2026-07-13T02:52:41Z

*(Live-state grounding, this slice: lane HEAD pinned `7f7ca07a293872577fac0cbe835ef0bec728b3b4`
via anonymous `git ls-remote` — the ledgered capability — and ONE raw fetch of the lane
heartbeat at that pin, 2026-07-13T02:52:41Z: `holdout: SPENT`, `paper_lane: FLAT/WATCH`,
`grading_due: 2026-07-17T09:01Z`, `next_2: lane intact; zero open orders`. No research
round 3 is registered — the decision window this head prices is OPEN. The tested margin
constants are quoted from this section's committed probe of the lane's own results doc
(`docs/research-round-2-results.md` §R3 @ lane HEAD `6799a4c`, fetched 2026-07-11 —
[`cross-sectional-momentum-family-2026-07-10.md`](cross-sectional-momentum-family-2026-07-10.md));
the one-read external budget was spent on the freshness check above, disclosed.)*

**Origin:** drafted under standing owner ORDER 003 (continuous pipeline) + ORDER 004
rule 3's rotation ("fleet backlogs → venture's book/product space → game mechanics →
COMPLETELY UNRELATED domains") — round 2 of the cycle: 021 took fleet-backlogs, this
head takes the VENTURE slot, and per the manager guidance quoted in the dispatching
order (ORDER 033: "find more strategies to backtest, as well as more stocks, more
indicators") round 2's venture weight goes to the TRADING half of the Venture Lab seat
— round 1 covered the books half (PROPOSAL 018 → VERDICT 020, an honest null). Harvest
source: this section's own post-holdout reseal material — the lane honestly falsified
its opening class (P4: 13/13 TRANSFER-FAILED), ran Research Round 2 under
pre-registration (78 configs; R3 `xsec_momentum` kept 3 of 6 as dev-candidates:
L=63/k=2 stitched-OOS Sharpe **1.627** vs equal-weight basket **1.147**, L=63/k=3
**1.631**, L=252/k=3 **1.277**), and promotion is CLOSED behind an owner-gated
post-2026 protocol that agents must not run. The open, computable, agent-legal
question nobody has asked: **are those KEEP margins (+0.484 / +0.480 / +0.130) bigger
than what best-of-6 SELECTION alone produces on momentum-free markets of the same
shape — and, as ORDER 033's "more strategies, more stocks, more indicators" multiplies
the config count N, how fast must the shortlist bar rise?** A best-of-N statistic is
biased up by construction; the lane's own discipline (burden denominators on every
number: 6 / 78 / 668) records N but has never priced it.

## The idea (reasoned to its fuller form — Q-0254 duty)

The lane's KEEP/KILL calls compare each config's stitched-OOS Sharpe against the
basket's and keep the winners — but the reported winner margins are MAXIMA over a
swept grid, and the null distribution of "max over N configs of (strategy Sharpe −
basket Sharpe)" is strictly positive-shifted even when no config has any edge. Two
decision-relevant numbers follow, neither computable from the lane's real data
without spending evaluation bars it must not spend: (1) **the selection-noise
calibration** — the probability that a momentum-FREE market of the lane's shape (9
instruments, 2,595 daily bars, realistic correlation and volatility clustering)
hands best-of-6 a margin ≥ the observed +0.484, which prices whether the
dev-candidates deserve owner attention now; and (2) **the burden-bar curve** — the
null q99 of the best-of-N margin as N grows through the grids ORDER 033's expansion
implies (N = 1, 6, 24, 96), which converts "more strategies, more stocks, more
indicators" from a slogan into a pre-registerable shortlist bar: sweep N configs,
demand Δ ≥ q99(N) before a KEEP earns a shortlist row. Both come from ONE hermetic
sim: synthetic null panels matched to the lane's protocol shape, the lane's own R3
rule applied verbatim, margins read off the same statistic the lane reports.

**What this head deliberately is NOT (the routing hazard honored):** the section's
parked capture warned verbatim that pushing this family to sim-lab could "re-backtest
the same dev bars with WEAKER provenance … and would route around an explicitly
reserved OWNER-ACTION." This sim touches ZERO real market bars, never evaluates the
three dev-candidates on any data, and never runs (or schedules) the owner-gated
post-2026 protocol — it computes the NULL DISTRIBUTION of the lane's own dev-stage
statistic. Its APPROVE consequence routes only the agent-legal act the lane's own
status already names: "flagged as proposal only, never scheduled/initiated/run by
agents."

**The sim (fully hermetic — the PROPOSAL 017/018/019/020/021 precedent; every fixture
is a pinned constant committed with the sim, zero repo/network reads in the verdict
session):** synthetic daily-return panels, J = 9 instruments × T = 2,595 bars (the
lane's aligned-index shape), one-factor Gaussian model
r_{j,t} = μ_d + m_{s_t}·σ_d·(√ρ·f_t + √(1−ρ)·z_{j,t}) with f, z i.i.d. N(0,1),
σ_ann = 0.30 (σ_d = 0.30/√252). Null cells sweep **vol model ∈ {IID (m ≡ 1), RSV}**
× **pairwise correlation ρ ∈ {0.0, 0.3, 0.6}** × **basket drift S_bh ∈ {0, 1.15}**
(μ_d = S_bh·σ_d·√(ρ + (1−ρ)/9)/√252, so the matched leg reproduces the lane's
reported basket Sharpe 1.147 in expectation) = **12 decision cells**. RSV = 2-state
Markov systemic volatility, transition p_cc = 0.98 / p_ss = 0.94 (stationary π =
(0.75, 0.25)), variance multipliers (0.6, 2.2) — unconditional unit variance EXACT
(0.75·0.6 + 0.25·2.2 = 1, asserted), one chain per panel shared by all instruments.
Every cell is momentum-free by construction (returns i.i.d. across time given the
vol state — no signal exists to find). Strategy layer = the lane's R3 protocol
verbatim on the period frame: rebalance every 21 bars (the lane's frozen interval)
→ 123 periods, warm-up 12 periods (max lookback 252 bars), evaluation = 111 period
returns uniform across configs; at each rebalance rank instruments by trailing
L-bar total log return (ties by instrument index), hold top-k to the next rebalance;
cost = 10 bp per side on replaced names (charge 0.001·2·replaced/k per rebalance);
benchmark = zero-cost equal-weight basket, same window. Sharpe = mean/std of period
returns × √12 (annualized); **Δ(config) = Sharpe_config − Sharpe_basket**. Burden
ladder, nested: **G1** = {L=63, k=2, momentum, equal} (the lane's headline config);
**G6** = the lane's own R3 grid L ∈ {63,126,252} × k ∈ {2,3}; **G24** = L ∈
{21,42,63,84,126,252} × k ∈ {2,3} × direction ∈ {momentum, reversal}; **G96** = L ∈
{21,42,63,84,105,126,189,252} × k ∈ {2,3,4} × direction ∈ {momentum, reversal} ×
weighting ∈ {equal, rank-linear} — G1 ⊂ G6 ⊂ G24 ⊂ G96, all at the frozen 21-bar
rebalance, so one panel's 8 sorted rankings serve every config. **M = 1,000** seeded
panels per cell, `random.Random(20260727)`, pinned loop order (cells lexicographic:
vol model IID→RSV, ρ ascending, S_bh ascending; panels sequential; per panel: regime
chain, then f_t, then z_{j,t} by instrument then bar). Per (cell, N ∈ {1,6,24,96}):
the full distribution of Δ_max(N) = max over G_N of Δ, reported as {q50, q90, q99},
plus the headline probabilities **P(Δ_max(G6) ≥ 0.484)** (the best KEEP margin) and
**P(Δ_max(G6) ≥ 0.130)** (the weakest KEEP margin, reporting-only — expected
selection-compatible, which itself informs the shortlist). **Arm A (analytic,
seedless — validation gates, run invalid on any failure):** (a) k=9 control config:
strategy ≡ basket, zero turnover after entry → Δ = 0 to 1e−12, asserted per panel on
the first 10 panels of every cell; (b) exchangeability gate: per cell at S_bh = 0,
the panel-mean PRE-COST strategy period return minus basket period return must lie
within 4 MC standard errors of 0; (c) vol-ratio gate: on IID/ρ=0.0/S_bh=0 cells the
measured pre-cost strategy-to-basket period-return std ratio must match √(9/k)
within 2% (selection is future-blind under the null — this checks exactly that);
(d) RSV unit-variance normalization asserted exactly; (e) CPython minor version
pinned and asserted; stdout + results.json byte-identical across two process runs.
**Decision-stability leg:** fresh seed **20260728**, M = 250 per cell, must
reproduce the same ruling. **Reporting-only legs (seed 20260729; cannot flip the
decision):** J = 18 universe ("more stocks" — same G6-shape grid on 18 instruments,
q99 shift reported), cost c ∈ {0, 25 bp}, σ_ann = 0.15 (cost drag doubles in Sharpe
units), all on the IID/ρ=0.3/S_bh=1.15 cell only. Feasibility arithmetic: 12 cells ×
1,000 panels × ~29k draws ≈ 350M draws + ~35k strategy ops per panel — single-digit
minutes in pure CPython, stdlib-only, no dependencies.

**Pre-registered acceptance bands and decision rule** (set BEFORE any code exists;
evaluated on P := P(Δ_max(G6) ≥ 0.484) over the 12 decision cells, in this order):

- **REJECT** ("the KEEP margins are selection-compatible — breadth first, no owner
  spend") iff **P ≥ 0.10 in ≥ 6 of 12 cells**. Checked FIRST — the
  protect-the-scarce-resource arm (owner attention is the program's scarcest
  resource), so an eager promotion recommendation cannot shadow it (the PROPOSAL
  019/021 evaluation-order discipline).
- **APPROVE** ("the top margins clear selection noise everywhere swept — the owner
  proposal is worth routing now") iff **P ≤ 0.01 in ALL 12 cells**.
- **NULL** otherwise — a legitimate and here EXPECTED-PLAUSIBLE outcome: the verdict
  names the flip axis (for each of vol-model, ρ, and S_bh: the share of its cells
  passing the APPROVE line and the median P at each value; largest spread = the
  named boundary — expected candidate: the RSV arm, since volatility clustering
  fattens the right tail of best-of-N Sharpe margins), and the citable finding is
  the CONDITIONAL rule ("the margins clear the i.i.d. bar but not the clustered-vol
  bar", or its converse), never either camp's soundbite.

**The burden-bar table ships on EVERY outcome:** {q90, q99} of Δ_max(N) per cell for
N ∈ {1, 6, 24, 96}, plus the max-over-cells row as the conservative round-3
shortlist bar per N — ORDER 033's expansion, priced: every extra strategy, stock
sweep, or indicator raises the bar by a now-measured amount.

**Consequence, pre-registered:** on APPROVE — the residual slice the section's
parked capture already names (a one-page owner PROPOSAL naming the five Round-2
dev-candidates — three xsec, two keltner — as pre-declared subjects of the next
owner-gated post-2026 protocol) rides the manager sweep WITH the quantified line
"the best KEEP margin +0.484 exceeds best-of-6 selection noise q99 in all 12 swept
nulls", and the burden-bar table attaches as the round-3 pre-registration default
(sweep N configs → shortlist bar Δ ≥ q99(N)). On REJECT — the routing note flips:
round-3 BREADTH under the burden bar outranks spending owner attention on the
current candidates, the owner proposal is NOT routed, and the quantified reason is
the measured per-cell P table. On NULL — the conditional rule is the finding, and
the cheapest LIVE probe is named: the lane computes lag-1..5 autocorrelation of
squared daily basket returns on its own committed dev bars (one lane-side script,
zero holdout spend, zero owner clicks, zero new data) — locating which null arm its
real data resembles before any routing call is made.

## Relations (adjacent heads — deliberately links, not duplication)

- vs the harvest source
  [`cross-sectional-momentum-family-2026-07-10.md`](cross-sectional-momentum-family-2026-07-10.md)
  (parked, overtaken-by-events): that capture queued the FAMILY and the lane built
  it first; its probe left two residuals — the owner-proposal "paperwork, not code"
  slice and the explicit routing hazard. This head is NOT the capture revived: it
  re-backtests nothing, evaluates no candidate on any bars, and prices the
  SELECTION-INFERENCE question (is +0.484 beyond best-of-6 noise?) plus the burden
  curve — questions the capture never posed. The hazard clause above is this head's
  contract with it.
- vs the section's other heads: `post-holdout-reseal-protocol` (parked — owner-gated
  holdout process, no computable question), `kit-upgrade-oldest-pin` /
  `wake-resilience-fresh-session-rebind` (process, lane-ops) — zero overlap.
- vs the outbox (PROPOSALs 001–021, re-read at HEAD `8022a9d`): no prior proposal
  touches trading, backtesting, portfolio selection, Sharpe inference, or multiple
  testing. Nearest by ROTATION SLOT is PROPOSAL 018 (venture round 1, books →
  VERDICT 020 null by sim-lab's own offset map — source numbers cited verbatim,
  never derived): same seat, different half — book-budget allocation vs backtest
  selection inference, zero shared model, metric, fixture, or consumer; V020's
  answered question (versioning vs breadth) is not re-asked. Nearest by SIM-FAMILY
  are PROPOSALs 017/019/020/021 (→ VERDICTs 019/021/022/023-in-flight): hermetic
  pre-registered grids with bands and stated evaluation order — method precedent
  reused, zero shared domain (social choice / backlog replenishment / casino
  bankroll fencing / migration-ID queueing).
- vs sim-lab (local clone @ `cf953a5`, verdicts through V022 finalized — V022 =
  PROPOSAL 020 by the offset map; V023 in flight for PROPOSAL 021): no verdict
  touches financial backtesting, selection bias, or Sharpe statistics.
- Tree-wide dedup sweep (`rg -g '!bootstrap.py' -g '!.substrate'` for
  selection-noise / selection-bias / multiple-testing / data-mining / overfit /
  momentum / Sharpe over ideas/ + .sessions/ + control/ + docs/): every hit is this
  section's own four files (the harvest source's "anti-overfitting discipline"
  prose included) plus two incidental venture-lab mentions of the word "momentum"
  in unrelated prose. No prior selection-inference or burden-pricing content
  anywhere in the tree.

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained modeling head, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe
> battery). Verify-first ran FIRST, live this slice: (a) **grounding** — lane HEAD
> pinned `7f7ca07` by `git ls-remote` (the ledgered capability) and the heartbeat
> raw-fetched at that pin (2026-07-13T02:52:41Z): holdout SPENT, paper lane
> FLAT/WATCH, zero open orders, no round 3 registered — the window is open, the
> margins tested are the lane's current best evidence. (b) **dedup** — the sweeps
> above; zero prior content. (c) **feasibility arithmetic** — in the sim preamble;
> single-digit minutes, stdlib-only.

**1. What is this really?** A pre-registered selection-noise calibration for the
one statistic the trading lane promotes on — best-of-grid stitched-OOS Sharpe
margin — asking whether the R3 KEEP margins exceed what a momentum-free market
hands a 6-config sweep by luck, and pricing how that bar rises as ORDER 033's
"more strategies, more stocks, more indicators" multiplies the sweep. The lane
records its burden denominators scrupulously; this head is the first thing that
converts a denominator into a required margin.

**2. What is the possibility space?** (i) Do nothing — the dev-candidates sit
unpriced; the owner proposal either goes forward on vibes (owner attention spent
on possibly-noise) or never goes (possibly-real edge parked forever). (ii) Wait
for the paper lane — it grades donchian(15,5) only, first evaluable signal ~Aug
2026, and says nothing about selection noise at any N. (iii) Run the real OOS
protocol — owner-gated, agents must not, and it SPENDS evaluation data that this
head's answer is free of. (iv) This head: 12 momentum-free null cells, the lane's
own rule verbatim, bands registered first, burden curve on every outcome. (v)
Over-scope (fat-tailed innovations, cross-sectional dispersion models, transaction
impact curves, walk-forward refit emulation) — named follow-ups only if a ruling
lands within reach of a band edge; the disclosed boundaries below state why they
are second-order for THIS question.

**3. What is the most advanced capability reachable by the simplest
implementation?** One ~300-line stdlib file: a one-factor panel generator with a
2-state vol chain, prefix-sum period returns, 8 sorted rankings reused by 96
configs, and exact analytic gates (k=9 identity, exchangeability, √(9/k) vol
ratio) — and it yields the fleet's first measured selection-bias table for ANY
evidence pipeline that promotes a best-of-N: the same curve prices idea-engine's
own "best probe of the batch" one day. The burden-bar table is reusable
methodology, not a one-shot number.

**4. What breaks it? (assumptions made explicit)** (a) **Model-true, not
market-true** — Gaussian one-factor returns with regime vol; no fat tails beyond
clustering, no cross-sectional dispersion dynamics, no momentum crashes. That is
why the RSV arm exists (the clustering direction is the expected flip axis), why a
cell-dependent result is a pre-registered NULL naming the axis, and why the NULL
consequence names the autocorrelation probe that locates the lane's REAL cell from
its own committed bars. (b) **Period-level Sharpe** (111 period observations, ×√12)
emulates the lane's daily stitched-OOS statistic with a WIDER null — fewer
observations fatten Δ_max tails, so the APPROVE direction is conservative and the
REJECT direction inherits the bias; the REJECT band (0.10, ten times the APPROVE
line) is set with that head-room, and the bias direction is stated in the verdict.
(c) **Cost and benchmark pins** — 10 bp per side and a zero-cost rebalanced basket
are model constants, not the lane's exact settings (not readable in-repo); both
push the strategy DOWN vs the basket, again conservative toward APPROVE, with c ∈
{0, 25 bp} bracketing. (d) **Tested constants are quoted, not re-fetched** — the
margins (+0.484/+0.480/+0.130 over basket 1.147) come from this section's
committed probe of the lane results doc @ `6799a4c` (2026-07-11); the one-read
budget went to the fresher heartbeat pin instead (holdout SPENT, no round 3 —
i.e., no NEWER margins exist to test). If the lane re-states its numbers before
verdict time, the fixture constants update in the intake, never mid-run. (e)
**PRNG stability** — seeds 20260727–29 pinned FRESH (registry 20260713–26 swept
across all prior heads before picking — the PROPOSAL 020 card's collision warning
heeded, the PROPOSAL 021 card's practice followed), loop order pinned, CPython
minor version pinned and asserted.

**5. What does it unlock?** The routing decision on the lane's five dev-candidates
(owner proposal now vs breadth first) made on numbers; the round-3 pre-registration
default that makes ORDER 033's expansion safe (every added config buys a known bar
increase, so "more strategies, more stocks, more indicators" can proceed WITHOUT
diluting the KEEP rule); the fleet's first reusable best-of-N selection-noise
table; and on NULL, a one-script live probe that turns the model-choice question
into a measurement on data the lane already owns.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing external at
sim time — every fixture ({J, T, period length, warm-up, σ_ann, vol-model
constants, ρ-grid, S_bh-grid, cost, grid definitions G1/G6/G24/G96, M, seeds
20260727–29, tested margins 0.484/0.130, band constants}) is stated in this file
and committed as a small JSON alongside the sim. Kill tests, run live this slice:
lane already ran round 3 or re-registered new margins (NOT killed — heartbeat @
`7f7ca07`: zero open orders, WATCH state, no round 3), a prior selection-inference
head anywhere in the tree (NOT found — sweeps above), a sim-lab verdict on it (NOT
found — verdicts through V022 read), infeasible runtime (NOT found — arithmetic in
the preamble). Sim-worthy or judgment-only: sim-worthy — the entire question is
order-statistics arithmetic against pre-registered thresholds; the judgment
question (are 0.01 / 0.10 the right lines?) is pinned by pre-registration and the
full P and quantile tables ship so a re-drawn line re-reads, never re-runs.

**7. Which lane should build it — and what does it displace or duplicate?** sim-lab
runs it (its harness, its verdict grammar; sim + fixture JSON committed in its
sims/ tree). The verdict's consumers are named in the header: the trading lane owns
the round-3 pre-registration default and the dev-candidate shortlist; the manager
owns the routing call on the owner proposal (Q-0260 — this repo never edits the
lane's files; the lane's own status already carries the proposal-only rule).
Duplicates nothing: the lane's own pre-registration machinery controls FORWARD
variance (freeze grids before running) but has never priced the BACKWARD question
(what did freezing N=6 already buy?); VERDICT 020 is the same-seat neighbor and
shares no question; the capture's probe is the provenance trail, not the analysis.

**8. What is the smallest shippable slice?** One sim-lab intake dir: one stdlib
file (panel generator + vol chain + ranking/portfolio layer + analytic gates +
legs), one fixture JSON (all constants copied verbatim from this file), one
results table {P(Δ_max(G6) ≥ 0.484), P(≥ 0.130), q50/q90/q99 of Δ_max(N)} × (12
cells × N ∈ {1,6,24,96}) plus the burden-bar summary row and the
stability/reporting legs, ending in exactly one of APPROVE / REJECT / NULL per the
pre-registered rule — reproducible from the fixtures alone, byte-identical on
re-run, no flags.

**Recommendation: sim-ready** — the question is crisp and computable, the bands and
decision rule (with stated evaluation order — REJECT checked first, protecting the
scarcest resource) are registered above BEFORE any code exists, the genre's failure
modes are pre-empted (model-dependence → two vol arms + axis-naming NULL + the
named autocorrelation probe on lane-owned data; frequency mismatch and cost pins →
disclosed conservative direction; owner-gate integrity → the hazard clause, zero
real bars, zero candidate evaluation), and every outcome changes what a named seat
does next. THE ONE QUESTION for the simulator: *Under the pinned momentum-free
panel model (J = 9 instruments × T = 2,595 daily bars; r_{j,t} = μ_d +
m_{s_t}·σ_d·(√ρ·f_t + √(1−ρ)·z_{j,t}), σ_ann = 0.30; 12 decision cells = vol model
{IID, RSV(p_cc = 0.98, p_ss = 0.94, variance multipliers (0.6, 2.2), exact unit
normalization asserted)} × ρ {0.0, 0.3, 0.6} × basket-Sharpe drift S_bh {0, 1.15};
M = 1,000 panels per cell, seed 20260727, pinned loop order; the lane's R3 rule
verbatim on the period frame — rebalance every 21 bars, warm-up 252 bars, 111
evaluation periods, rank by trailing L-bar return, hold top-k, 10 bp per-side
turnover cost, zero-cost equal-weight basket benchmark, Δ = annualized period
Sharpe minus basket Sharpe; nested burden grids G1 ⊂ G6 (the lane's own L ∈
{63,126,252} × k ∈ {2,3}) ⊂ G24 ⊂ G96; analytic gates — k=9 identity Δ ≡ 0,
exchangeability mean gate, √(9/k) vol-ratio gate within 2%, RSV normalization
exact — run invalid on any failure; stability leg seed 20260728 M = 250 must
reproduce the ruling; reporting-only legs seed 20260729: J = 18, c ∈ {0, 25 bp},
σ_ann = 0.15), what are P := P(Δ_max(G6) ≥ 0.484) per cell and the burden-bar
quantiles {q90, q99} of Δ_max(N) for N ∈ {1, 6, 24, 96} — and does the result land
REJECT (P ≥ 0.10 in ≥ 6 of 12 cells → the KEEP margins are selection-compatible:
round-3 breadth outranks the owner proposal, quantified per cell; checked FIRST),
APPROVE (P ≤ 0.01 in ALL 12 cells → the top margins beat selection noise everywhere
swept: the five-candidate owner proposal rides the manager sweep with the
quantified line, and the burden-bar table becomes the round-3 shortlist default),
or NULL (anything else → the flip axis named via per-axis APPROVE-pass shares and
median P — expected candidate the RSV arm — the conditional rule is the citable
finding, and the named live probe is lag-1..5 autocorrelation of squared daily
basket returns on the lane's own committed dev bars, zero holdout spend)?*
Done-when: the committed sim + fixture JSON reproduce the full P and quantile
tables plus the burden-bar summary byte-identically, all four analytic gates pass,
the stability leg reproduces the same ruling, and the verdict issues exactly one of
APPROVE/REJECT/NULL per the pre-registered rule (evaluation order stated) with the
model-true boundary, the wider-null frequency bias, and the cost/benchmark pins
stated as disclosed conservative directions, the reporting-only legs stated as legs
that cannot flip the decision, and the burden-bar table shipped on every outcome.
