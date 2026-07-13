# The round-3 breadth budget: does expanding past the q99 bar buy true discoveries, or does the bar eat the margin?

> **State:** sim-ready
> **Class:** product · **Target:** `menno420/trading-strategy` (verdict consumer: the
> round-3 pre-registration itself — grid size and shortlist bar chosen together, on
> power numbers instead of appetite; the manager's routing note on HOW ORDER 033's
> "more strategies, more stocks, more indicators" gets executed; verification target
> `menno420/sim-lab` per the Q-0264 pipeline)

*(Grounding, this slice — committed evidence only, zero network reads even at
drafting (the PROPOSAL 023 precedent): the parent verdict is committed in the local
sim-lab clone @ `5e356ed` — `sims/verdict-024-keep-margins-noise/{REPORT.md,
results.json}`, VERDICT 024 finalized 2026-07-13, null, flip axis DRIFT, vol axis
measured INERT. The lane-state pin is PROPOSAL 022's own committed drafting capture
(lane HEAD `7f7ca07`, heartbeat raw-fetched 2026-07-13T02:52:41Z: holdout SPENT,
paper lane FLAT/WATCH, NO round 3 registered — the decision window this head prices
was verified OPEN three hours ago and nothing in either control ledger has routed a
round-3 registration since). Anchor constants below are quoted verbatim from the
parent's committed `results.json` at the pinned clone.)*

**Origin:** drafted under standing owner ORDER 003 (continuous pipeline) + ORDER 004
rule 3's rotation — the VENTURE slot, round 3. Round 1 took the books half
(PROPOSAL 018 → VERDICT 020, honest null), round 2 the trading half (PROPOSAL 022 →
VERDICT 024, honest null). Round 3 stays on the trading half deliberately: V024's
own recommendation flags its burden-bar table as "round-3 pre-registration default
material", and the table is HALF a tool — it prices the bar (the null q99 of the
best-of-N margin: matched arm N=6 **0.399** → N=24 **0.516** → N=96 **0.619**) but
not what the lane BUYS by paying it. ORDER 033 says expand ("find more strategies to
backtest, as well as more stocks, more indicators"); V024 says expansion raises the
shortlist bar by a now-measured amount; nobody has priced the collision. If the
lane's true edges are modest, a 96-config sweep may be a machine for hiding them
behind its own bar — or, if edges live at horizons the current 6-config grid cannot
see, expansion may be the only way to find them at any bar. That is a POWER
question, it is fully computable hermetically, and it must be answered BEFORE the
lane registers round 3, because the registration fixes N and the bar together.

## The idea (reasoned to its fuller form — Q-0254 duty)

V024 measured the null side: with NO edge anywhere, best-of-N selection hands a
margin whose q99 rises ~0.1–0.2 Sharpe per ~4× config-count step. The missing side:
plant KNOWN edge into the same world and measure what each grid size actually
harvests under its own q99 bar. Two forces fight: **coverage** (a wider grid spans
more lookback horizons/directions — if the market's persistence lives at a horizon
the incumbent grid lacks, only expansion can see it) vs **multiplicity** (every
added config raises the bar every OTHER config must clear — and blanket expansion
adds decoys: reversal directions and redundant horizons that pay bar-cost while
carrying no edge). The resolution is an empirical curve, not a slogan: true-keep
yield Y(N) per design grid, planted-edge strength × persistence swept, the bar
recomputed per grid exactly as a pre-registered round 3 would set it. The verdict
hands the lane its round-3 registration row: blanket grid, targeted grid, or a
conditional coverage rule — plus a marginal price list for "one more indicator".

**The sim (fully hermetic — the PROPOSAL 017–025 precedent; every fixture a pinned
constant committed with the sim, zero repo/network reads in the verdict session):**
V024's panel machinery re-used at its committed pin (`sims/verdict-024-keep-margins-noise/`
@ sim-lab `5e356ed` — in-repo byte-reuse, the VERDICT 006/017 engine-copy
precedent), extended with ONE new layer. Base: J = 9 instruments × T = 2,595 daily
bars, one-factor Gaussian returns r_{j,t} = μ_d + α_{j,e(t)} + σ_d·(√ρ·f_t +
√(1−ρ)·z_{j,t}), σ_ann = 0.30, IID vol only (V024 measured the vol axis INERT —
per-axis spread 0.000 — so the RSV arm demotes to a reporting leg by citation, not
assumption), drift matched S_bh = 1.15 (the lane-relevant arm; V024's binding axis,
held at the value the lane's own basket Sharpe 1.147 selects; the zero-drift stress
arm demotes to a reporting leg). **Planted layer:** per instrument, epochs of E bars
(from bar 0, last partial epoch kept); per epoch, α_{j,e} = κ·(σ_d/√252)·g_{j,e},
g ~ N(0,1) i.i.d. — persistent cross-sectional drift dispersion with one-sigma
annualized Sharpe κ, the thing trailing-return ranking can genuinely detect, gone
at κ = 0 (the null legs are EXACTLY V024's IID matched cells, machinery-identical).
**Decision cells: κ ∈ {0.5, 1.0, 2.0} × E ∈ {21, 63, 252} × ρ ∈ {0.0, 0.3, 0.6} =
27.** Strategy layer verbatim from V024 (21-bar rebalance → 123 periods, warm-up
252 bars, 111 evaluation periods, rank by trailing L-bar total log return, hold
top-k equal-weight, 10 bp per side on replaced names, zero-cost equal-weight basket
benchmark, Δ = annualized period Sharpe − basket Sharpe, ties by instrument index).
**Design grids, nested:** G6 = the lane's own L ∈ {63,126,252} × k ∈ {2,3} ⊂
**G10** = G6 ∪ (L ∈ {21,42} × k ∈ {2,3}, momentum, equal — the TARGETED
short-horizon expansion, the new grid this head introduces) ⊂ G24 ⊂ G96 (V024's
definitions verbatim); design axis N ∈ {6, 10, 24, 96}. **The round-3 procedure,
emulated exactly:** per (ρ) the null bar b_N(ρ) = q99 of Δ_max(G_N) from a κ = 0
null leg (M = 1,000 panels per ρ, same machinery); per planted panel, shortlist =
{configs i ∈ G_N with Δ_i ≥ b_N(ρ)} — the familywise-1% rule V024's table implies.
**Oracle margins:** θ_i(cell) = mean Δ_i over the cell's M = 400 panels (no
selection — the config's true planted-world margin; per-config tables ship);
true-edge set = {i : θ_i ≥ 0.10} (materiality line, pre-registered judgment at the
scale V024 showed carries no selection evidence — full θ and Y curves ship so a
re-drawn line re-reads, never re-runs). **Decision metrics:** Y(cell, N) = expected
true keeps per sweep = E_panels[#{i ∈ G_N : Δ_i ≥ b_N(ρ), θ_i ≥ 0.10}]; F(cell, N)
= expected false keeps (reporting); N*(cell) = smallest N with Y(N) ≥ 0.95·max_N'
Y(N') (parsimony tie rule); cell DETECTABLE iff max_N Y(N) ≥ 0.25. **Chained
anchors (the PROPOSAL 023 precedent):** the null legs must reproduce the parent's
committed q99 values — V024 `results.json`, IID/S_bh=1.15 row: ρ=0.0 {N6 0.3983,
N24 0.4916, N96 0.5845}, ρ=0.3 {0.3669, 0.4272, 0.4549}, ρ=0.6 {0.3011, 0.3608,
0.3909} — within ±0.05 absolute (fresh-seed MC tolerance at M = 1,000), run invalid
outside it. **Validation gates (run invalid on any failure):** the k=9 identity
(Δ ≡ 0 to 1e−12, first 10 panels of every leg); familywise false-keep rate on an
INDEPENDENT null validation leg (M = 500 per ρ, reporting seed — bars from leg A
applied to leg B, rate within 3 binomial SE of 0.01, killing the in-sample
quantile circularity); oracle sign gates (θ(reversal L=63 k=2) < θ(momentum L=63
k=2) in every planted cell; θ of the E-matched momentum config non-decreasing in κ
at fixed (E, ρ) within 2 MC SE); CPython minor pinned and asserted; stdout +
results.json byte-identical across two process runs. **Decision-stability leg:**
fresh seed, M = 200 per decision cell, must reproduce the same ruling.
**Reporting-only legs (cannot flip the decision):** S_bh = 0 stress arm and the RSV
vol arm (each at κ=1.0/E=63, ρ ∈ {0.0, 0.3}); the **marginal-config price list** —
starting from G6, add ONE config of each class {covered-horizon duplicate (L=84,
k=2, mom, equal) · uncovered short horizon (L=21, k=2, mom, equal) · direction
decoy (L=63, k=2, reversal, equal) · weighting variant (L=63, k=2, mom,
rank-linear)}, bar recomputed at N=7, ΔY measured on the ρ=0.3 planted cells —
computed on the main-leg panels (the 8 sorted rankings per panel already serve
every config; zero extra panels). **Seeds:** 20260748 (main: null legs + 27 planted
cells), 20260749 (stability), 20260750 (validation + reporting legs), 20260751
(aux self-check stream, never read by any decision number) — allocated strictly
above the P025 registry high-water 20260747. **Feasibility:** ~10,800 planted +
~4,500 null/validation + ~1,000 reporting panels ≈ 16k panels ≈ the parent's
measured 15.5k at ~4.6 min, stdlib-only, single-digit minutes.

**Pre-registered acceptance bands and decision rule** (set BEFORE any code exists;
evaluated over DETECTABLE cells — count reported, and if fewer than 8 of 27 cells
are detectable the run lands NULL naming detectability itself the finding — in this
order):

- **REJECT** ("blanket expansion never pays — the bar eats the margin") iff
  **N*(cell) ≤ 10 in ≥ 80% of detectable cells**. Checked FIRST — the
  protect-the-evidence arm: the costly error is a round-3 registration that
  dilutes every real margin behind its own multiplicity bar (the PROPOSAL 019/021/022
  evaluation-order discipline).
- **APPROVE** ("blanket breadth survives the bar") iff **N*(cell) ≥ 24 in ≥ 80% of
  detectable cells AND median over detectable cells of (Y(96) − Y(6)) ≥ +0.25
  true keeps per sweep**.
- **NULL** otherwise — a legitimate and here EXPECTED-PLAUSIBLE outcome: the verdict
  names the flip axis (for each of κ, E, ρ: the share of its detectable cells with
  N* ≤ 10 and the median Y(96) − Y(6) at each value; largest spread = the named
  boundary — expected candidate E, the coverage axis: G6 sees no horizon below
  L=63, so E=21 cells should reward expansion while E ∈ {63, 252} cells pay the
  bar for nothing), and the citable finding is the CONDITIONAL coverage rule
  ("expansion buys coverage, not multiplicity — add configs only at horizons or
  directions the incumbent grid cannot see"), never either camp's soundbite.

**The marginal-config price list ships on EVERY outcome:** per added-config class,
the measured (bar increase, ΔY) pair — the literal price of "one more indicator",
converting ORDER 033 from a quota into an accounting identity.

**Consequence, pre-registered:** on APPROVE — the round-3 registration may take the
full blanket grid, with the in-run q99(N) bar (V024's matched-row table standing as
default) attached at registration; ORDER 033 executes as written. On REJECT — the
round-3 pre-registration default becomes G6 + TARGETED additions only (each added
config names the uncovered horizon/direction it hunts and pays its measured
marginal bar), and ORDER 033's "more" arm routes preferentially to universe
breadth — V024 measured J=18 slightly bar-LOWERING (q99 shift −0.041) — rather
than config breadth; the quantified reason is the per-cell Y table. On NULL — the
conditional coverage rule is the finding, the targeted-G10 row ships as the
default-if-hunting-short-horizons, and the cheapest LIVE probe is named: the lane
computes lag-1..6 period Spearman rank-autocorrelation of trailing-63-bar returns
on its own committed dev bars (one lane-side script, zero holdout spend, zero owner
clicks, zero new data) — locating the real (κ, E) cell before any registration
fixes N. Every outcome leaves the owner-gated post-2026 protocol untouched: zero
real bars, no dev-candidate evaluated, nothing scheduled (the harvest hazard clause
of PROPOSAL 022, inherited verbatim as a contract term).

## Model basis

The number rides on the planted epoch-dispersion family (persistent per-instrument
drift, i.i.d. Gaussian across epochs and instruments, one-factor Gaussian noise) —
a standard neutral choice for "detectable cross-sectional structure with a tunable
horizon", chosen because trailing-return ranking is exactly its matched detector.
The single most-likely-to-flip alternative: the lane's REAL persistence structure
(drifts that decay smoothly, regime-dependent dispersion, momentum crashes) — which
is deliberately the same measurement as the NULL-case live probe (the
rank-autocorrelation script on the lane's own committed bars).

## Relations (adjacent heads — deliberately links, not duplication)

- vs **PROPOSAL 022 → VERDICT 024** (the parent, same section — nearest by every
  axis, DELIBERATELY): the parent measured the SIZE of the selection test — the
  null distribution of Δ_max(N) with no edge anywhere in the world, ending in the
  burden-bar table. This head measures the POWER side: edge planted at known
  strength × horizon, yield per grid size under the parent's own bar. Zero planted
  signal exists anywhere in the parent (every cell momentum-free by construction);
  the parent's answered question (are the current KEEP margins selection-
  compatible? — null, drift-dependent) is settled and NOT re-asked; no measured
  number is recomputed — the parent's committed q99 values ride as chained anchors
  and its axis findings (vol INERT, drift binding) shrink this grid by citation.
- vs [`cross-sectional-momentum-family-2026-07-10.md`](cross-sectional-momentum-family-2026-07-10.md)
  (parked, overtaken-by-events): the provenance trail for the margins and the
  routing-hazard clause — no analysis shared; this head evaluates no candidate.
- vs PROPOSAL 018 → VERDICT 020 (venture round 1, books): fixed-budget allocation
  vs selection power — zero shared model, metric, fixture, or consumer. (One rhyme,
  disclosed: both are breadth-vs-depth questions; V020 allocates production effort
  across titles, this head allocates STATISTICAL burden across configs — the
  arithmetic and the deciding seat differ entirely.)
- vs the method family P017–P025 → V019–V027: hermetic pre-registered grids with
  bands, stated evaluation order, honest-null discipline — method precedent reused,
  zero shared domain.
- vs sim-lab (local clone @ `5e356ed`, verdicts V001–V027 all finalized): only
  V024 touches trading/selection — it is the parent, related as above; no verdict
  plants a true signal in any selection sim.
- Tree-wide dedup sweep (`rg -i -g '!bootstrap.py' -g '!.substrate'` for
  power-analysis / true-discovery / planted-signal / breadth-budget /
  false-discovery / coverage-vs-multiplicity over ideas/ + .sessions/ + control/ +
  docs/): hits are V024's own tally lines and the parent idea file's burden prose —
  no prior power/coverage content anywhere in the tree.

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained modeling head, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe
> battery). Verify-first ran FIRST, against committed evidence this slice: (a)
> **grounding** — parent verdict read at the local sim-lab pin `5e356ed` (V024
> finalized, null, vol INERT, drift binding; anchor constants extracted from its
> committed results.json verbatim); lane window from P022's committed capture
> (@ `7f7ca07`, 02:52:41Z — no round 3 registered) with no later registration
> routed through either control ledger at drafting. (b) **dedup** — the sweeps
> above; zero prior content. (c) **feasibility arithmetic** — in the sim preamble;
> ≈ the parent's measured runtime.

**1. What is this really?** The power half of V024's selection-inference program:
given the bar the lane must charge itself per grid size (measured, committed), the
first measurement of what each grid size actually YIELDS in true discoveries when
edge of known strength and horizon exists — i.e. the round-3 design question
(how many configs can the sweep afford?) converted from appetite into a curve.

**2. What is the possibility space?** (i) Register round 3 blanket-wide on ORDER
033's words alone — risks a sweep that hides its own findings behind the bar. (ii)
Register round 3 at G6 forever — risks permanent blindness to short-horizon edge
the grid cannot see. (iii) Wait for live data — the paper lane grades one config in
August and says nothing about grid design. (iv) This head: 27 planted cells, the
lane's rule verbatim, the parent's bars as anchors, bands registered first, a
marginal price list on every outcome. (v) Over-scope (adaptive/sequential designs,
FDR-style shortlists, cross-validated bars) — named follow-ups only if a ruling
lands near a band edge; the familywise q99 rule is what V024 shipped and what
round 3 would actually register.

**3. What is the most advanced capability reachable by the simplest
implementation?** One stdlib file re-using the parent's committed panel generator
plus ~80 new lines (epoch-drift layer, shortlist rule, yield accounting) — and it
yields the fleet's first measured power curve for ANY best-of-N evidence pipeline:
the same Y(N)-under-q99(N) arithmetic prices idea-engine's own batch-probe
promotion one day (V024 named the reusable-methodology rhyme; this head builds the
second half of it).

**4. What breaks it? (assumptions made explicit)** (a) **Model-true, not
market-true** — planted epoch-dispersion is a stylized edge; the `## Model basis`
note names it and the flip alternative, and the NULL probe measures the real cell
from lane-owned bars. (b) **The materiality line (θ ≥ 0.10) and detectability line
(Y ≥ 0.25) are pre-registered judgments** — full θ and Y curves ship, so re-drawn
lines re-read, never re-run. (c) **Oracle-margin coupling** — θ_i is estimated on
the same M = 400 panels the selection runs on; each panel contributes 1/400 to a
cross-panel mean, so the coupling is O(1/M) and disclosed, and the sign gates catch
gross failures. (d) **The familywise rule is the strictest reasonable shortlist** —
a laxer round-3 rule (e.g. per-config q99) would raise every Y; direction
disclosed, REJECT is therefore the conservative arm exactly where it is checked
first. (e) **PRNG stability** — seeds 20260748–51 pinned fresh above the registry
high-water 20260747, loop order pinned, CPython minor pinned and asserted.

**5. What does it unlock?** The round-3 registration row (N and bar chosen
together, on power); the marginal price of every config class ORDER 033 might add;
the targeted-G10 default if coverage is what pays; on NULL, a one-script live probe
that locates the lane's real cell before registration; and the reusable Y-under-bar
curve for every fleet best-of-N pipeline.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing external at
sim time — every fixture ({J, T, period frame, σ_ann, ρ-grid, S_bh, κ-grid, E-grid,
grid definitions G6/G10/G24/G96, marginal-config classes, M per leg, seeds
20260748–51, materiality/detectability lines, anchor constants with ±0.05
tolerance, band constants}) is stated in this file and committed as JSON alongside
the sim. Kill tests, run against committed evidence this slice: round 3 already
registered (NOT killed — P022's pin plus clean ledgers at drafting), a prior
power/coverage head anywhere in the tree (NOT found — sweeps above), a sim-lab
verdict on it (NOT found — V001–V027 read), infeasible runtime (NOT found — ≈ the
parent's measured minutes). Sim-worthy or judgment-only: sim-worthy — the entire
question is yield arithmetic against pre-registered thresholds; the judgment lines
are pinned and re-readable.

**7. Which lane should build it — and what does it displace or duplicate?** sim-lab
runs it (its harness, its verdict grammar, its own committed V024 machinery
re-used at pin). Consumers named in the header: the trading lane owns the round-3
registration this verdict parameterizes (routing is the manager's per Q-0260 —
this repo never edits the lane's files). Duplicates nothing: the parent computed
no yield, planted no signal, and introduced no G10; the lane's pre-registration
machinery freezes grids but has never had a power basis for CHOOSING one.

**8. What is the smallest shippable slice?** One sim-lab dir: one stdlib file
(parent generator + epoch layer + shortlist/yield accounting + gates + legs), one
fixture JSON, one results table {Y, F, N*, θ tables, marginal price list} ×
(27 cells × N ∈ {6,10,24,96}) plus anchors/gates/stability, ending in exactly one
of APPROVE / REJECT / NULL per the pre-registered rule — reproducible from the
fixtures alone, byte-identical on re-run, no flags.

**Recommendation: sim-ready** — the question is crisp and computable, the bands and
decision rule (REJECT first — protecting the evidence pipeline from its own
multiplicity) are registered above BEFORE any code exists, the genre's failure
modes are pre-empted (model-dependence → Model basis note + axis-naming NULL + the
named lane-owned probe; judgment lines → pinned, tables ship; parent coupling →
chained anchors with stated tolerance; owner-gate integrity → the inherited hazard
clause, zero real bars), and every outcome changes what a named seat does next.
THE ONE QUESTION for the simulator: *Under the pinned planted-edge panel model
(V024's committed machinery at sim-lab pin `5e356ed` re-used verbatim — J = 9 ×
T = 2,595 one-factor Gaussian panels, IID vol (RSV demoted to reporting by V024's
measured inert axis), matched drift S_bh = 1.15, ρ ∈ {0.0, 0.3, 0.6}; NEW planted
layer: per-instrument epoch drifts α_{j,e} = κ·(σ_d/√252)·g_{j,e} redrawn every E
bars, κ ∈ {0.5, 1.0, 2.0} × E ∈ {21, 63, 252} → 27 decision cells; the lane's R3
rule verbatim — 21-bar rebalance, 111 evaluation periods, trailing-L ranking,
top-k, 10 bp, basket benchmark, Δ = Sharpe − basket Sharpe; design grids G6 ⊂ G10
(targeted short-horizon) ⊂ G24 ⊂ G96, N ∈ {6, 10, 24, 96}; shortlist per panel =
configs with Δ ≥ b_N(ρ), the in-run κ=0 null q99 of Δ_max(G_N) at M = 1,000,
chained-anchored to V024's committed values {ρ=0.0: 0.3983/0.4916/0.5845 · ρ=0.3:
0.3669/0.4272/0.4549 · ρ=0.6: 0.3011/0.3608/0.3909} ± 0.05; oracle margins θ_i =
no-selection cell means, true edge θ ≥ 0.10; Y(cell, N) = expected true keeps per
sweep, N* = smallest N within 5% of max yield, detectable = max_N Y ≥ 0.25;
M = 400 panels per cell seed 20260748, stability leg M = 200 seed 20260749 must
reproduce the ruling, independent-leg familywise gate + k=9 identity + oracle sign
gates + anchor gate run-invalidating, seeds 20260750/51 for validation+reporting/
aux), what are Y(cell, N), F(cell, N), and N*(cell) across the 27 cells — and does
the result land REJECT (N* ≤ 10 in ≥ 80% of detectable cells → blanket expansion
never pays: round 3 registers G6 + targeted named-horizon additions only, ORDER
033's breadth routed to universe not configs; checked FIRST), APPROVE (N* ≥ 24 in
≥ 80% of detectable cells AND median Y(96) − Y(6) ≥ +0.25 → blanket breadth
survives its own bar: round 3 may register the full grid with the q99(N) bar
attached), or NULL (anything else, or < 8 detectable cells → the flip axis named
via per-axis N*-shares and yield spreads — expected candidate E, the coverage
axis — the CONDITIONAL coverage rule is the citable finding, the targeted-G10 row
ships as the short-horizon default, and the named live probe is lag-1..6 period
rank-autocorrelation of trailing-63-bar returns on the lane's own committed dev
bars, zero holdout spend)?* Done-when: the committed sim + fixture JSON reproduce
the full {Y, F, N*, θ, marginal price list} tables byte-identically, every gate
(anchors, independent-leg familywise, k=9 identity, oracle signs) passes, the
stability leg reproduces the same ruling, and the verdict issues exactly one of
APPROVE/REJECT/NULL per the pre-registered rule (evaluation order stated) — with
the model-basis note restated, the judgment lines shipped as re-readable tables,
the familywise-strictness direction disclosed, the reporting-only legs (S_bh = 0,
RSV, marginal list) stated as legs that cannot flip the decision, and the
owner-gated post-2026 protocol untouched on every path.
