# Book portfolio: breadth vs versioning depth — where does the K-th version stop paying?

> **State:** sim-ready
> **Class:** venture · **Target:** `menno420/venture-lab` (verdict consumer — its book
> pipeline's allocation default; verification target `menno420/sim-lab` per the Q-0264
> pipeline)
> **Grounding:** https://raw.githubusercontent.com/menno420/venture-lab/main/control/inbox.md@81c47ec7897b9c1fd601d0f45cec81c0862f7ccc · fetched 2026-07-13T01:11Z

**Origin:** drafted under standing owner ORDER 003 (continuous pipeline) + ORDER 004
rule 3's rotation ("fleet backlogs → venture's book/product space → game mechanics →
COMPLETELY UNRELATED domains") — PROPOSALs 015/016 were game mechanics, 017 the
unrelated-domain slot; this slice serves the venture book/product slot. The owner's
venture night-run order (venture-lab `control/inbox.md` ORDER 008 @ `81c47ec`,
carrying the owner's DIRECT ORDER verbatim) sets the seat's book thesis: "BOOKS:
multiple new book ideas AND multiple versions of each (different angles, audiences,
lengths) — versions are cheap once the research exists", with the morning tally
counting "book versions written". That directive contains an untested allocation
policy: at a FIXED production budget, every version written is a new title NOT
written. This head pre-registers the breadth-vs-depth question and hands the venture
lane a measured default instead of a vibe.

## The idea (reasoned to its fuller form — Q-0254 duty)

The venture lane's book pipeline faces the same fixed-budget allocation question
every production night: spend the next slice on a NEW title (another lottery ticket
in a heavy-tailed discovery market) or on ANOTHER VERSION of an existing title
(higher per-title quality if you can pick the best version, or another listing if
you publish all versions — at the risk that versions of the same book cannibalize
one audience instead of reaching several). Both instincts have respectable backing:
best-of-K selection gains are real but flatten fast (order statistics — the expected
max of K draws grows only ~√(2·ln K)), while heavy-tailed marketplaces reward ticket
COUNT (more independent draws at the tail). Which force wins depends on measurable
structure — version-to-version quality spread, discovery-lottery weight, version
cost, selection fidelity, audience separation — and nobody has run the numbers for
this pipeline. The owner's clause "versions are cheap once the research exists" is a
claim about exactly one of those parameters (cost ratio c), and it is IN the sweep,
not assumed.

**The sim (fully hermetic — every fixture constructed by the sim itself, nothing
external; the PROPOSAL 017 precedent):** a production night is a budget **B = 12
units** (size leg B = 6, reporting only). A new title costs 1 unit; each additional
version of an existing title costs **c ∈ {0.25, 0.5, 0.75}** units (the owner's
"versions are cheap" = low c; it is swept, not granted). A policy is a
versions-per-title count **K ∈ {1, 2, 3, 4, 6}**; the effective title count is
T_eff(K) = B / (1 + c·(K−1)), used fractionally for expected values (exact by
linearity of expectation; integer-T legs cover the hit-probability reporting).
Title latent appeal θ ~ N(0,1); version i of a title has quality q_i = θ + ε_i with
ε_i ~ N(0, σ_v²), **σ_v ∈ {0.2, 0.5, 1.0}** (how DIFFERENT versions really are —
the owner's "different angles, audiences, lengths" is the high end). A published
book with quality q earns r = exp(q + L) in relative units, with discovery lottery
L ~ N(−σ_m²/2, σ_m²) so E[exp(L)] = 1 exactly, **σ_m ∈ {0.5, 1.5, 2.5}** (mild to
extreme winner-take-most). Two publication modes, both run:

- **Mode P (pick-best):** publish 1 of the K versions; the true-best version is
  picked with probability **f ∈ {0.2, 0.6, 1.0}** (selection fidelity — can the
  lane/owner actually identify the best version pre-publication?), else a uniform
  random version.
- **Mode A (publish-all):** all K versions are listed; per-version
  r_i = exp(θ + ε_i + L_i); title revenue R = (1−s)·max_i r_i + s·Σ_i r_i with
  audience separation **s ∈ {0, 0.5, 1}** (s=0: versions fully cannibalize one
  audience, only the discovery winner earns; s=1: fully separate audiences,
  revenues add — K independent lottery tickets).

Per cell (Mode P: c×σ_v×σ_m×f = 81 cells; Mode A: c×σ_v×σ_m×s = 81 cells), the
headline is **K\*(cell) = argmax_K of expected revenue per unit budget**
E[R_title(K)] / (1 + c·(K−1)), and **ΔR(cell) = R(K\*)/R(K=1) − 1** (the measured
gain of optimal versioning over pure breadth). Two arms: **Arm A (analytic,
no RNG)** — on the Mode P f=1 slice, E[R_title(K)] = e^{1/2} · E[exp(σ_v·M_K)] with
M_K the max of K iid standard normals, computed by Simpson quadrature of
∫ exp(σ_v·x)·K·φ(x)·Φ(x)^{K−1} dx over [−10, 10] at step 0.001 using stdlib
`math.erf` — exact-to-quadrature K\* for that slice. **Arm S (seeded Monte Carlo)**
— M = 20,000 titles per (mode, cell, K); `random.Random(20260716)` for Mode P and
`random.Random(20260717)` for Mode A, draws in a pinned loop order (cells
lexicographic, K ascending, titles sequential; per title: θ, then ε_1..ε_K, then
lottery/pick draws — order pinned in the sim file); a decision-stability leg re-runs
the full grid at M = 2,000 with seed 20260718 and must reproduce the same
APPROVE/REJECT/NULL outcome (decision-level, not per-cell). Arm S must agree with
Arm A within 1.5% on every f=1 cell or the run is invalid. Hit-probability legs
(reporting only, cannot flip the decision): at integer T = ⌊T_eff⌋ and B ∈ {6, 12},
P(≥1 title beats the within-cell p90 of the K=1 title-revenue distribution) per
policy. Results table pins the CPython minor version; byte-identical on re-run.

**Pre-registered acceptance bands and decision rule** (set BEFORE any code runs):

- **APPROVE** ("versioning-heavy allocation is robust — adopt a quota") iff in
  BOTH modes: K\* ≥ 2 in ≥ 80% of cells AND median ΔR ≥ +0.10.
- **REJECT** ("breadth dominates at fixed budget") iff in BOTH modes: K\* = 1 in
  ≥ 80% of cells.
- **NULL** otherwise (modes disagree, or the K\* mass straddles) — a legitimate,
  reportable outcome: the verdict names the flip axis (for each swept axis, the
  K\*≥2 cell-share at each of its values; largest spread = the named boundary —
  expected candidates: audience separation s and selection fidelity f) and the
  citable finding becomes the CONDITIONAL rule, not either camp's default.

**Consequence:** on APPROVE — the venture book pipeline adopts a default
versions-per-title quota equal to the grid-median K\* for fixed-budget production
nights, and the measured marginal curve (ΔR vs K) rides the book-pipeline template
so "one more version" is priced, not vibed. On REJECT — the lane's default flips to
new-titles-first, versions produced only on a demand signal, and a QUANTIFIED
routing note goes to the manager's sweep: under every swept model a versions-quota
forgoes ~|median ΔR| of expected portfolio return (evidence FOR the owner's morning
read; the standing order itself is untouched — decide-and-flag, never
countermand). On NULL — neither "always version" nor "always breadth" may be cited
as settled; the named-axis conditional rule is the citable finding, and the lane's
cheapest LIVE probe is named: publish two versions of ONE existing-research book
with disjoint audience keywords and record whether their draws actually separate
(measuring s in the wild for the price of one night's slice).

## Relations (adjacent heads — deliberately links, not duplication)

- vs `ideas/venture-lab/` (all 13 files re-read this slice): the book-adjacent heads
  are single-SKU content plays — `agent-fleet-playbook-ebook-2026-07-11.md`
  (shortlist #5, one e-book) and `sellables-brainstorm-batch-2026-07-11.md` #8 (the
  backtester e-book) — neither asks any allocation question across titles/versions.
  `pre-publish-conservative-forecast-2026-07-10.md` is per-listing forecast
  DISCIPLINE (Q-0259 r.4 honest ranges), orthogonal to allocation and untouched here
  (this sim outputs relative units only, never a dollar forecast).
  `webhook-test-kit-family-2026-07-11.md` records that PRICE elasticity
  ($19/$29/$39 + bundle) was already routed to sim-lab by the venture lane itself
  (its status.md@389bb37 routing block) — the reason this head deliberately avoids
  the pricing/bundling shape entirely.
- vs the outbox (PROPOSALs 001–017, re-read at HEAD `80baad5`): 001–011 and 015–016
  are superbot/game/kit heads, 012–014 fleet-meta process sweeps, 017 social choice
  — ZERO venture book/product proposals exist; this is the first. Nearest by METHOD:
  012 (policy grid, worker-turn economics) and 017 (pre-registered bands +
  APPROVE/REJECT/NULL + hermetic fixtures) — band discipline reused, no shared
  domain, fixture, or consumer.
- vs sim-lab (outbox read via MCP at this drafting): VERDICTs 001–018 — none touch
  venture's book/product space. Venture-lab itself has NO `control/outbox.md` at
  main (raw fetch 404 @ `81c47ec`), so no books SIM-REQUEST exists to duplicate or
  race.
- Tree-wide dedup sweep (`grep -ri` for breadth/portfolio/best-of/versions-per/
  cannibaliz, `bootstrap.py` + `.substrate` excluded): the only "portfolio" hits are
  trading ASSET portfolios (`ideas/trading-strategy/cross-sectional-momentum-family-
  2026-07-10.md` — securities, not production allocation) and a judge-panel
  "best-of" workflow head (`ideas/superbot/judge-panel-as-saved-workflow-2026-07-10.md`
  — review sampling, not publishing). No prior breadth-vs-depth or
  version-allocation content anywhere in ideas/, .sessions/, or control/.

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained modeling head, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe
> battery). Verify-first ran FIRST, live this slice: (a) **grounding** — the owner's
> BOOKS directive re-read verbatim at venture-lab `control/inbox.md` ORDER 008 @
> `81c47ec` (raw fetch), not from memory. (b) **dedup** — the sweeps above; zero
> prior allocation content. (c) **feasibility arithmetic** — Arm S is 162 cells × 5
> K × 20,000 titles ≈ 16.2M title draws, each O(K) RNG calls: low tens of millions
> of draws, a few minutes in pure CPython, no dependencies; Arm A is 27×5
> one-dimensional quadratures, instant.

**1. What is this really?** A pre-registered allocation policy sim for the venture
book pipeline: at fixed budget, does the K-th version of a book beat the next new
title — measured across every defensible combination of version cost, version
spread, discovery-lottery weight, selection fidelity, and audience separation,
under both publication modes the owner's directive admits (pick the best version
vs list all versions as separate angles/audiences/lengths).

**2. What is the possibility space?** (i) Don't run it — the lane keeps allocating
by instinct and the tally counts versions whose marginal value nobody priced.
(ii) Ask the owner — a structured-choice question with zero evidence attached;
strictly worse than asking AFTER this verdict prices the options (Q-0263.2:
paste-ready asks). (iii) A/B live on the marketplace — the honest endgame for s and
f, but it costs real listings and weeks of draw data; the sim tells the lane
WHETHER the answer even depends on s/f before anyone spends listings on measuring
them. (iv) This head: two modes × 81 cells, bands registered first, NULL names the
binding axis. (v) Over-scope (per-title budget adaptivity, sequential stopping
rules, cross-title cannibalization) — each is a natural follow-up ONLY if this
verdict lands non-NULL; the static-K question is the one the owner's directive
poses tonight.

**3. What is the most advanced capability reachable by the simplest
implementation?** One ~250-line stdlib file: a title is one θ draw plus K ε draws;
both modes' revenue rules are two lines each; Arm A is a textbook order-statistics
quadrature with `math.erf`. That file yields an exact analytic marginal-gain curve
(f=1 slice), a full two-mode robustness grid, and a decision the venture lane can
apply the same night it lands — from a sim a verdict session runs cold in minutes.

**4. What breaks it? (assumptions made explicit)** (a) **Models are models** — the
lognormal-lottery marketplace and normal quality spread are standard neutral
choices, not sales data (the same epistemic stance as PROPOSAL 017's IC/IAC); that
is exactly why the ruling requires BOTH modes to clear a band and why the straddle
is a pre-registered NULL naming the binding axis, never a judgment call.
(b) **Quality elasticity pinned** — revenue's exp(q) link fixes elasticity at 1;
the σ_m sweep covers the regime where lottery dwarfs quality (elasticity
effectively → 0), so the pin is bracketed, and this is stated in the verdict.
(c) **Relative units only** — the sim allocates effort; it never forecasts
earnings, so Q-0259 r.4 conservative-forecast discipline is untouched.
(d) **Static K** — real nights could adapt K per title on early signal; the static
answer is the correct BASELINE and the adaptive question is a named follow-up, not
scope creep. (e) **PRNG stability** — `random.Random` pinned per mode, loop order
pinned, CPython minor version pinned in the results table; Arm A is seedless
quadrature, so the f=1 headline is platform-independent.

**5. What does it unlock?** The pipeline's first venture-lane verdict — a measured
default (quota, breadth-first, or a named conditional) for the exact allocation
decision the owner's ORDER poses every production night; the marginal-gain curve as
a permanent line in the book-pipeline template; on NULL, a costed shortest path to
the real answer (the two-version live probe measures s for one slice's budget).

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing external at
sim time — every fixture ({B, c, K, σ_v, σ_m, f, s, M, seeds, band constants}) is
stated in this file and committed as a small JSON alongside the sim. Kill tests,
run live this slice: an existing venture allocation/versioning head anywhere in
the tree (NOT found — sweeps above), an existing venture-lab books SIM-REQUEST
(NOT found — no outbox file exists at `81c47ec`), infeasible runtime (NOT found —
arithmetic in the preamble). Sim-worthy or judgment-only: sim-worthy — the entire
question is a computable argmax against pre-registered thresholds; the one
judgment question (are 80%-of-cells and +10% the RIGHT materiality lines?) is
pinned by pre-registration and stated as the disputable bands, never the measured
numbers.

**7. Which lane should build it — and what does it displace or duplicate?** sim-lab
runs it (its harness, its verdict grammar; sim + fixture JSON committed in its
sims/ tree). The verdict's consumer is the venture-lab book pipeline (allocation
default + template line) and the manager's routing sweep (the REJECT-case routing
note). Duplicates nothing: the domain sweeps found zero allocation prior art, and
the one venture question already routed to sim-lab (webhook price elasticity, by
the lane itself) is a pricing head this file deliberately does not touch.

**8. What is the smallest shippable slice?** One sim-lab intake dir: one stdlib
file (both modes + Arm A quadrature + Arm S grid), one fixture JSON (all constants
copied verbatim from this file), one results table {K\*, ΔR, per-axis K\*≥2 shares,
hit-probability legs, Arm A/S agreement} × both modes, ending in exactly one of
APPROVE / REJECT / NULL per the pre-registered rule — reproducible from the
fixtures alone, byte-identical on re-run, no flags.

**Recommendation: sim-ready** — the question is crisp and computable, the bands and
decision rule are registered above BEFORE any code exists, the genre's failure
modes are pre-empted (model-dependence → dual-mode requirement + axis-naming NULL;
forecast creep → relative units only), and every outcome changes what the venture
lane does with its next production night. THE ONE QUESTION for the simulator:
*Under the pinned production-night model (budget B=12, version cost c ∈ {0.25, 0.5,
0.75}, K ∈ {1,2,3,4,6}, T_eff = B/(1+c·(K−1)); title appeal θ ~ N(0,1), version
quality θ + ε with ε ~ N(0, σ_v²), σ_v ∈ {0.2, 0.5, 1.0}; revenue exp(q + L),
L ~ N(−σ_m²/2, σ_m²), σ_m ∈ {0.5, 1.5, 2.5}; Mode P pick-best with fidelity
f ∈ {0.2, 0.6, 1.0}; Mode A publish-all with audience separation s ∈ {0, 0.5, 1},
R = (1−s)·max r_i + s·Σ r_i), what is K\* = argmax_K E[revenue per unit budget] and
ΔR = R(K\*)/R(1) − 1 per cell — Arm A analytic (f=1 slice, Simpson quadrature,
seedless) and Arm S seeded MC (M=20,000; seeds 20260716 Mode P / 20260717 Mode A;
stability leg M=2,000 seed 20260718; Arm A/S agreement ≤ 1.5% on every f=1 cell) —
and does the result land APPROVE (both modes: K\* ≥ 2 in ≥ 80% of cells AND median
ΔR ≥ +0.10 → adopt a versions-per-title quota = grid-median K\*), REJECT (both
modes: K\* = 1 in ≥ 80% of cells → new-titles-first default + a quantified routing
note to the manager), or NULL (anything else → the flip axis is named with
per-value K\*≥2 shares, the conditional rule is the citable finding, and the
two-version live probe is the named next step)?* Done-when: the committed sim +
fixture JSON reproduce the results table across both modes and all legs
byte-identically, Arm S matches Arm A within tolerance on the f=1 slice, the
stability leg reproduces the same ruling, and the verdict issues exactly one of
APPROVE/REJECT/NULL per the pre-registered rule with the pinned-elasticity and
relative-units caveats stated and the hit-probability legs reported as sensitivity
that cannot flip the decision.
