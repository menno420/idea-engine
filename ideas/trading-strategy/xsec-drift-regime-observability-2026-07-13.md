# Drift-regime observability — is the arm of V024's conditional trust rule readable from the basket stream in time to act?

> **State:** sim-ready
> **Class:** product (pipeline rotation — the standing ORDER 003 VENTURE slot,
> round 5, trading half; the successor move applied to the venture slot's V024
> line: rounds 1–4 were P018 books → V020 null, P022 trading → V024 null, P026
> trading → V028 approve, P030 books → V032 reject — this round follows V024's
> own first "What it did NOT settle" line, "Which null arm the lane's real data
> lives in", now sharpened by V028's LIMITS line "a bar registered for a
> regime-switching world should be recomputed under it") ·
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/idea-engine@11c5a1fab3b7377dc30a6a803c19caaf367631d2 · fetched 2026-07-13T08:54:42Z
> (drafting HEAD for the dedup sweep; parent-anchor home: the local sim-lab clone
> @ `cd47c0626fb01211fc214125fdbc83b95b8aef5f` — every V024 anchor constant below
> is machine-read from `sims/verdict-024-keep-margins-noise/results.json` at that
> pin, not transcribed from report prose; the sim itself is fully hermetic: zero
> repo/network reads at verdict time, every fixture a pinned constant committed
> with the sim, ZERO real market bars, no dev-candidate evaluated on any data,
> the owner-gated post-2026 protocol untouched — P022's harvest-hazard clause
> inherited verbatim as a contract term)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous
pipeline — "continue coming up with new ideas, that is your main purpose";
verified open/standing at HEAD `11c5a1f` before any work), VENTURE rotation
round 5, trading half. VERDICT 024 (idea-engine PROPOSAL 022, the +2 offset map
in sim-lab docs/current-state.md) ruled NULL with a drift-conditional finding:
the lane's top KEEP margins (+0.484/+0.480) clear best-of-6 selection noise in
EVERY drift-matched cell (P ≤ 0.004; matched q99(G6) 0.398324 < 0.484) and are
selection-compatible in the zero-drift stress arm (P up to 0.169 at ρ = 0) —
"Flip axis: S_bh (drift), spread 0.667", while the vol axis its own live probe
targets measured INERT (spread 0.000, "the probe is confirmatory"). VERDICT 028
(PROPOSAL 026) then APPROVED blanket breadth under its own bar (N* ≥ 24 in
11/11 detectable cells, median Y(96) − Y(6) = +14.2125), so ORDER 033's round-3
expansion executes with V024's q99(N) table attached — every shortlist row the
lane keeps from here on is trusted BECAUSE the world is assumed drift-matched.
Both verdicts leave the same joint open: the drift arm is located only by the
lane's committed FULL-WINDOW basket Sharpe 1.147 — a static average over 2,595
bars — and V028's LIMITS line says the quiet part: "a bar registered for a
regime-switching world should be recomputed under it." Nobody has priced
whether the drift STATE is readable from the basket stream at actionable
windows at all. This head prices exactly that: the same successor move as
P023←V022, P026←V024, P029←V027, P030←V020, and P033←V023, applied to the
venture slot's trading line at its own named open thread.

## The idea (reasoned to its fuller form — Q-0254 duty)

**The unpriced fork.** V024's manager note says the manager MAY treat the
matched-arm reading (top margins beyond noise, weakest margin not) as the
operative conditional. That is a STATIC trust rule: trust always, because the
full-window average says drift. If the lane's real basket alternates between
drifting and driftless regimes, the static rule mis-trusts during every
zero-drift stretch (where P(Δ_max(G6) ≥ 0.484) runs up to 0.154–0.169 by
V024's committed cells) and a NEVER-trust rule wastes every drifting stretch.
A drift-CONDITIONAL trust rule needs a cheap observable that reads the current
arm from the basket stream. The detection arithmetic says the frontier is
genuinely open, not rhetorical: the two arms are separated by exactly 1.15
annualized Sharpe units, and a trailing w-bar Sharpe estimate carries
SE ≈ √(252/w) — 2.00 at w = 63, 1.41 at w = 126, 1.00 at w = 252 — so even the
PURE-window balanced accuracy tops out near Φ(1.15/2) ≈ 0.72 at the longest
swept window, and regimes shorter than the window degrade it toward a coin.
Whether that is enough to beat the best static prior by a material margin,
nowhere enough (REJECT), or enough only in named cells (NULL) is a measured
question with all three outcomes live.

**The pinned model (constants inherited from P022/V024 verbatim where they
exist; the regime chain is the one new axis).** The observable is the
equal-weight basket's daily return stream — V024's own benchmark object —
reduced to per-bar Sharpe units: x_t = μ_{s_t} + ε_t, ε_t i.i.d. N(0,1),
state D (drift-matched) mean δ = 1.15/√252 = 0.07244319066010188 (the matched
arm's basket Sharpe 1.15, V024's committed constant), state Z (zero-drift)
mean 0. The reduction is exact, not an approximation: V024 defines the matched
drift so the basket Sharpe is 1.15 REGARDLESS of ρ, so the basket-level
detection problem is scale-free and ρ-invariant BY CONSTRUCTION — pinned below
as a code-level identity, the analogue of V024's k=9 identity. Vol model IID
only, by citation: V024 measured the vol axis inert (spread 0.000), the P026
demotion precedent. **Regime chain:** 2-state Markov on {D, Z}, geometric
sojourns with means (S_D, S_Z) ∈ {126, 252, 1008}² bars — 9 decision cells
spanning "regimes flip inside a dev window" (half-year) to "one regime is most
of the history" (four years); per-bar stay probability 1 − 1/S; start state
from the stationary π_D = S_D/(S_D + S_Z) (exact values per cell: 0.500,
0.333, 0.111, 0.667, 0.500, 0.200, 0.889, 0.800, 0.500). Path length
T = 2,595 bars (the lane's aligned-index shape, V024's T); scoring window
t ∈ [252, T) uniform across all variants (the largest w, so every variant is
defined at every scored bar); M = 1,000 paths per cell.

**Detector family (18 pre-registered variants, all evaluated on the same
paths):** statistic ∈ {SR_w = (√252/w)·Σ_{i=t−w+1..t} x_i — the trailing
w-bar annualized Sharpe with PINNED vol normalizer (the lane pins basket vol
from its full history; the realized-sd variant rides a reporting leg), UP_w =
the trailing w-bar up-bar share} × window w ∈ {63, 126, 252} × threshold
position λ ∈ {0.3, 0.5, 0.7}: SR threshold h = λ·1.15; UP threshold
u = 1/2 + λ·(p_D − 1/2) with p_D = Φ(δ) = 0.528875393055249 (exact via
math.erf, quoted to full precision in the fixture). Classify drift-on iff
statistic ≥ threshold. λ = 0.5 is the symmetric midpoint; 0.3/0.7 are the
asymmetric variants a skewed-occupancy cell wants.

**Metrics per (cell, variant).** E = misclassified scored bars / scored bars
(the trust-misallocation rate: trusting-while-Z plus quarantining-while-D,
occupancy-weighted as realized); TPR/TNR/BA shipped alongside; ΔE_oracle =
E_static_best − E, where E_static_best = min(π_D, π_Z) EXACT from the chain —
the best static prior, an oracle the lane does not even have (the V032
discipline imported: an adaptive rule must beat the best static rule, not a
strawman); ΔE_always = π_Z − E (the lane's de-facto always-trust rule,
reporting-only). Post-flip detection lag (bars from each D→Z and Z→D flip
until the detector first reads the new state, censored at the next flip,
censor fraction reported): median and p90, reporting-only.

**Decision bands (registered BEFORE any code; evaluated REJECT first).**
Decision statistic: per variant, the count of decision cells with
ΔE_oracle ≥ +0.10 (ten points of trust-misallocation removed vs the best
static prior — a material, owner-legible margin).

- **REJECT** ("cheap drift-gating never materially pays — build no lane
  tooling; the registration carries the unhedgeable-degradation caveat"): NO
  variant achieves ΔE_oracle ≥ +0.10 in ≥ 3 of 9 cells. Checked FIRST — the
  costly error is lane tooling (a regime gate on the shortlist) that
  measurably cannot beat a constant, the exact failure class V032 just priced
  on the books half.
- **APPROVE** ("ship the drift-conditional trust line"): ∃ ONE variant — the
  SAME (statistic, w, λ) across all cells — with ΔE_oracle ≥ +0.10 in ≥ 7 of
  9 cells, stability-reproduced.
- **NULL** (anything else — a legitimate and here expected-plausible outcome):
  the per-cell frontier table IS the pin; flip axes named via per-axis pass
  shares — expected candidates the occupancy skew |π_D − 1/2| (at 0.889/0.111
  the oracle-static error 0.111 already beats the pure-window detector ceiling
  ≈ 0.28, by arithmetic) and the min-sojourn axis (at S = 126 every swept
  window straddles flips) — and the CONDITIONAL rule is the citable finding:
  gate trust only where regime occupancy is genuinely uncertain AND sojourns
  clear the window, keep V024's static reading elsewhere.

**Consequence, pre-registered.** APPROVE → the lane's round-3 registration kit
(V024's q99(N) bar + V028's power table, already the standing default) gains a
drift-conditional TRUST line with the pinned detector row (statistic, w, λ):
q99-cleared shortlist rows are trusted while the detector reads drift-on and
quarantined while it reads drift-off; V024's manager note upgrades from static
to conditional. REJECT → NO regime-gating tooling is built; V024's static
matched-arm reading stays the operative conditional; and the round-3
registration carries the quantified caveat that its trust degrades
UNDETECTABLY at the swept windows — the exact pure-window ceiling table is the
evidence row (a REJECT here rules on this observable family, stated). NULL →
the conditional rule ships with its named cells, and the cheapest LIVE probe
is named: run the pinned best variant ON the lane's own committed dev bars
(one lane-side script, zero holdout spend, zero owner clicks, zero new data),
reporting its realized trailing-SR path, flip count, and occupancy split —
locating the lane's real (π_D, S) cell before any trust-rule decision. Every
outcome leaves the owner-gated post-2026 protocol untouched.

**Dual arms (the P017–P033 committed discipline).**

- **Arm A (exact, seedless, platform-independent):** pure-state window
  distributions in closed form — SR_w is Gaussian, SR_w ~ N(S_state, 252/w)
  in annualized units under a pure-state window, so TPR = Φ((1.15 − h)·
  √(w/252)) and FPR = Φ(−h·√(w/252)) via math.erf (written once, asserted
  against a hand pin); UP_w is exact Binomial(w, p_state) via math.comb —
  giving the exact pure-window ceiling table
  {TPR_∞, TNR_∞, BA_∞, E_∞} for all 18 variants; the exact stationary
  occupancies π_D, static baselines min(π_D, π_Z), and expected flip counts
  per cell from the chain closed forms. Arm A covers the ceiling and every
  control leg exactly; the mixed-window realized error is Arm S's
  contribution (the P033 arm-split pattern: exact where closed forms exist,
  simulated where the path dependence lives).
- **Arm S (seeded MC):** the full switching stream simulated whole, all 18
  variants evaluated per path via prefix sums; M = 1,000 paths per cell.
  Seeds 20260772 main / 20260773 stability (M = 250, must reproduce the
  ruling) / 20260774 reporting / 20260775 aux (self-check stream, never read
  by any decision number) — allocated strictly above the PROPOSAL 033
  registry high-water 20260771. Pinned loop order (cells lexicographic S_D
  then S_Z ascending, paths sequential, one uniform per bar for the chain and
  one normal per bar for the return, draw-count sentinels exact).

**Gates (run invalid on any failure):** frozen-state control legs (the chain
held in D, then in Z, M = 500 paths each at seed 20260774) must reproduce Arm
A's exact per-variant TPR/FPR within tolerances pre-checked in the fixture as
≥ 2.5σ of the registered-M estimators and calibrated FAMILYWISE across the 36
gate points BEFORE any run (the V027/V031 pipeline lesson; V028's
gate-calibration lesson applied at design time, breach-handling protocol
pinned before any draw); measured occupancy π̂_D within its pre-checked band
of exact π_D per cell; measured flip count within its band of the exact
expectation; the swap identity — relabeling D↔Z and reflecting λ → 1−λ
transposes the confusion matrix EXACTLY in Arm A and within MC SE in Arm S;
the ρ-invariance identity — one reporting cell re-run with returns scaled by
the ρ = 0.0 and ρ = 0.6 basket vols (0.30·√(ρ + (1−ρ)/9), V024's formula)
must produce BYTE-IDENTICAL classifications, the statistic being scale-free;
per-leg draw-count sentinels; twin independently-written decision evaluators;
stdout + results.json byte-identical across two full process runs; CPython
minor pinned and asserted.

**Reporting-only legs (cannot flip the decision):** the lag tables (median/p90
per flip direction per variant, censor fractions); ΔE_always (the always-trust
comparison — expected and worth printing: in high-π_Z cells the detector
crushes always-trust even where it loses to the oracle prior); the
realized-sd SR variant (same paths, w-bar realized sd in the normalizer — the
vol-estimation price as a ΔBA column); and the **occupancy-graded bar leg**,
the bridge to the trust semantics: V024's committed panel machinery re-used at
its IID/ρ = 0.3 cell (J = 9, T = 2,595, the lane's R3 rule verbatim, G6 only,
M = 400 panels per point, seed 20260774), path-level drift occupancy
φ_D ∈ {0, 0.25, 0.5, 0.75, 1} as one D-block covering the first ⌈φ_D·T⌉ bars —
measuring q99(Δ_max(G6)) as a function of occupancy, with CHAINED ANCHORS: the
φ = 1 point must land within its pre-pinned tail-count tolerance of V024's
committed matched value 0.366902 and the φ = 0 point of the committed
zero-drift value 0.604101 (both machine-read from results.json @ `cd47c06`;
the V028 calibrated tail-count anchor precedent — tolerance arithmetic in the
fixture, not a bare ±). The leg answers, reporting-only: does the selection
bar move monotonically between the two committed arms, so a partial-occupancy
regime reading CALIBRATES the bar by interpolation rather than demanding a
fresh null sweep per reading.

**Fixture (every value copied verbatim from this file into a committed
JSON):** {δ = 0.07244319066010188, p_D = 0.528875393055249, S-grid {126, 252,
1008}², T = 2,595, scoring start 252, statistic/window/λ grids, thresholds
h = λ·1.15 and u = 1/2 + λ·(p_D − 1/2), M per leg {1,000 / 250 / 500 / 400},
seeds 20260772–75, band constants (+0.10 / ≥ 3 of 9 / ≥ 7 of 9), the exact
π_D and min(π_D, π_Z) table, the V024 anchor pair {0.366902, 0.604101} with
its results.json pin `cd47c06`, familywise gate tolerances with their pre-run
SE arithmetic, the occupancy-leg layout rule}.

**Feasibility arithmetic:** main leg 9 cells × 1,000 paths × 2,595 bars ≈
23.4M normals + prefix-sum evaluation of 18 variants (O(T) each); frozen legs
2 × 500 × 2,595 ≈ 2.6M; occupancy leg 5 × 400 × 2,595 × 9 ≈ 46.7M normals +
the G6 ranking kernel V028 already ran at far larger scale in ~5.5 min —
total comfortably under ~8 min of stdlib CPython; Arm A is closed-form
evaluations via math.erf/math.comb.

## Relations (adjacent heads — deliberately links, not duplication)

- vs **PROPOSAL 022 → VERDICT 024** (the parent, deliberately — source numbers
  cited verbatim per the +2 offset map in sim-lab docs/current-state.md): its
  answered question — are the KEEP margins selection-compatible? NULL,
  drift-conditional — is settled and NOT re-asked; no null distribution is
  recomputed here. The parent measured the null PER ARM with the arm known;
  this head measures whether the ARM ITSELF is knowable from the stream in
  time to act. Its committed per-cell values enter only as chained anchors
  (0.366902 / 0.604101) and its matched-drift constant 1.15 as the state-D
  mean.
- vs **PROPOSAL 026 → VERDICT 028** (the power half): V028 measured yield
  under the bar with the world's regime STATIC per panel; its own LIMITS line
  ("a bar registered for a regime-switching world should be recomputed under
  it") and qualifier 2 ("the real boundary is detectability, not grid size")
  are this head's opening. Zero shared metric: Y/N* there, trust-error and
  detector ROC here. Its live rank-autocorrelation probe stays named and
  untouched — it locates (κ, E) for the round-3 registration; this head's
  probe locates (π_D, S) for the trust line.
- vs **PROPOSAL 030 → VERDICT 032** (venture round 4, books): the REJECT's
  discipline — an adaptive rule must beat the best STATIC rule — is imported
  here as the oracle-static baseline min(π_D, π_Z); zero shared model, metric,
  fixture, or consumer (night allocation there, trust gating here).
- vs **PROPOSALs 013/014 → VERDICTs 015/016** (detector-cell sweeps): method
  rhyme only — those tune text linters on committed corpora; this tunes a
  sequential detector on a pinned stochastic process, and the corpus does not
  exist (the process is the fixture).
- Dedup, tree-wide at the grounding pin (`rg -i "drift.?detect|regime.?detect|
  regime.?switch|change.?point|cusum|rolling.?sharpe|trailing.?sharpe|
  drift.?observab|trust.?window"`, bootstrap.py + .substrate excluded): every
  hit is the P022/P026 family's own RSV prose in control/outbox.md, doc-drift
  detection in the fleet/kit sections (`section-sync-checker`, enabler-card
  guard — document synchronization, not market drift), or unrelated websites
  prose; the same sweep over the local sim-lab clone @ `cd47c06` returns
  ZERO hits; no proposal 001–033 and no sim-lab verdict V001–V034 (offset map
  read) runs a regime detector, a change-point/classification question, or
  any drift observable on a return stream.
- Alternatives weighed this slice and passed on merit: a portfolio-level
  cross-family allocation head for the books half (V032 killed within-family
  adaptation one wake ago and its own follow-up clause gates richer families
  on a measured lane cell that does not exist yet — the V020 s-probe should
  land first); a venture-lab product backlog head (the committed anchors
  there are pricing/elasticity heads the lane itself already routed — P018's
  dedup clause — and the maker/ebook rows carry no committed numeric anchor
  to chain a hermetic sim to).

## Model basis (declared model-dependence — the P024 discipline)

This verdict's numbers are CONDITIONAL on an embedded model, named up front:

- **(1) Statistical assumptions:** Gaussian i.i.d. innovations around a
  2-state Markov drift — the two states are V024's own two committed arms,
  and geometric sojourns are the neutral persistence choice (the P022 RSV
  transition-matrix pattern applied to drift instead of vol). IID vol by
  V024's measured inertness; no fat tails, no drift levels between 0 and
  1.15 (the two-arm world is inherited, not asserted — a real basket drifts
  on a continuum, and the detector's job is only to pick the arm whose null
  applies).
- **(2) Single most-likely-to-flip alternative:** the lane's REAL sojourn and
  occupancy structure — deliberately the same measurement as the NULL-case
  live probe (the pinned detector run once on the lane's committed dev bars).
  Second-order: smooth drift decay between arms would make every threshold
  detector look better than the two-point world's worst case near the
  boundary — the two-point separation is the HARDEST version of the
  distinguishability question at fixed gap, stated.
- **(3) The oracle-static baseline is conservative toward tooling:** ΔE_oracle
  compares against min(π_D, π_Z), a prior the lane cannot know without the
  very observable under test — so REJECT (nothing beats even the oracle) is
  the strong claim, and the ΔE_always table ships so a reader can re-weigh
  against the lane's de-facto rule; the registered ruling stays on the oracle
  bar (the V032 discipline).
- **(4) Out of scope by design, named:** composite/multi-scale detectors
  (CUSUM, likelihood-ratio filters — the REJECT-case rescue family, carrying
  its own sim if routed); trust semantics for the weakest margin (+0.130 is
  selection-compatible EVERYWHERE by V024 and carries no promotion weight for
  ANY regime reading — restated, not re-run); transaction/allocation changes
  on regime flips (trust gating only — nothing here trades).

## Probe report battery (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained successor head over
> committed parent evidence, no spend/publish/irreversible surface — README §
> probe battery). Verify-first ran FIRST, live this slice: (a) **parent
> evidence read direct** — V024's REPORT.md AND its committed
> `sims/verdict-024-keep-margins-noise/results.json` read at the local sim-lab
> clone `cd47c06`; the anchor pair and the six per-cell (P_484, q99(G6)) values
> are machine-read from the results file, not from prose. (b) **dedup** — the
> tree-wide drift/regime/change-point sweep above returned only the parent
> family's own prose at `11c5a1f` and zero sim-lab hits; PROPOSALs 001–033
> re-read at HEAD before drafting (tail verified: PROPOSAL 033 ·
> 2026-07-13T08:43:05Z). (c) **kill test NOT triggered** — no prior proposal,
> idea file, or card runs any detector on a return stream; V024's own named
> probe is an autocorrelation measurement of the VOL axis it measured inert.
> (d) **feasibility arithmetic checked** — ~73M normals + prefix sums + one
> G6 reporting kernel, under ~8 min.

**1. What is this really?** A pre-registered operating-characteristic sweep
for the missing half of V024's conditional trust rule: the parent measured
which arm makes the KEEP margins trustworthy (drift-matched: P ≤ 0.004;
zero-drift: P up to 0.169) with the arm GIVEN; this head measures whether a
cheap basket observable (trailing Sharpe or up-share, three windows, three
thresholds) can READ the arm from the stream under a pinned regime-switching
chain — scored as trust-misallocation removed vs the best static prior, with
exact pure-window ceilings as the seedless arm and V024's committed values as
chained anchors.

**2. What is the possibility space?** (i) Don't run it — the round-3
registration (already APPROVED into motion by V028) trusts its q99-cleared
rows on a full-window average, and nobody knows whether that trust is
gateable or blind. (ii) Build a lane-side regime gate by vibes — the exact
V032 failure class (adaptive tooling that never beat the best static rule),
now with real owner attention downstream. (iii) Judgment-only ("Sharpe over
half a year is obviously too noisy" / "obviously fine") — the two camps'
soundbites are both live because the ceiling arithmetic sits at BA ≈ 0.72.
(iv) Measure the lane's real bars first — named as the live probe, but
uninterpretable without this head's frontier table (a realized flip count
means nothing until the detector's false-flip rate under a known chain is
priced). (v) This head: price the observable family per (occupancy, sojourn)
cell against pre-registered bands, REJECT first. (vi) Over-scope (CUSUM
filters, trading on flips, continuous drift models) — named out of scope;
the composite-detector family is the REJECT-case rescue design.

**3. What is the most advanced capability reachable by the simplest
implementation?** One ~300-line stdlib file: a two-state chain + normal
stream generator, prefix-sum evaluation of 18 threshold detectors, math.erf/
math.comb closed forms for every pure-state distribution and baseline, the
V024-anchored G6 occupancy kernel, twin decision evaluators. That single file
turns "is the drift arm readable?" from a two-soundbite argument into a
per-cell frontier: exactly which occupancy/sojourn worlds a pinned
(statistic, window, threshold) row wins in, by how much, at what lag — and
the exact ceiling table for the worlds where nothing wins.

**4. What breaks it? (assumptions made explicit)** (a) **Model-truth** — the
two-arm world and geometric sojourns are inherited neutral choices; the real
structure is the declared flip axis and the live probe is the instrument;
the two-point gap makes this the hardest fixed-gap version, stated.
(b) **Anchor transcription** — the anchor pair is machine-read from the
parent's committed results.json and gated by tail-count tolerances pre-pinned
with their SE arithmetic (the V028 calibration lesson at design time, not
after a gate exit). (c) **Band placement could cherry-pick** — both bands and
the +0.10 materiality line are committed here before any code; full E/BA/lag
tables ship so a re-drawn line re-reads, never re-runs. (d) **MC error near
the frontier** — the decision arm couples exact Arm-A ceilings and baselines
with familywise-calibrated frozen-state gates (≥ 2.5σ at registered M,
pre-checked in the fixture — the V027/V031 two-datapoint lesson).
(e) **Scoring-window edge effects** — the uniform t ∈ [252, T) scoring rule
is pinned; the first-window exclusion is identical across variants, so no
variant buys advantage from undefined bars.

**5. What does it unlock?** The round-3 registration kit becomes complete on
its own terms: V024 priced the bar, V028 priced the yield, this head prices
WHEN the resulting trust is valid — an APPROVE ships a pinned trust line, a
REJECT ships the quantified caveat that trust degradation is unhedgeable at
cheap windows (itself decision-grade: it kills future regime-gate proposals
at zero cost), and a NULL ships the conditional cell map plus the one-script
probe that locates the lane. The occupancy-graded bar leg additionally tells
every future selection sim whether partial-regime worlds interpolate (one
sweep, reusable) or need their own nulls.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing live —
by design: every fixture is a pinned constant in this file (the matched-arm
constant 1.15 and T = 2,595 inherited from P022 verbatim; anchors machine-read
from the parent's committed results.json @ `cd47c06`; seeds 20260772–75).
Kill tests, run live this slice: a prior drift/regime-detection head anywhere
in either tree (NOT found — sweeps quoted in Relations); parent anchors
unavailable (NOT found — results.json read direct, six-cell table extracted);
infeasible runtime (NOT found — arithmetic in the preamble); the ceiling
arithmetic already deciding the question (NOT found — BA ceiling 0.61–0.72
across windows straddles every band, and mixed-window degradation is exactly
what no closed form here prices). Sim-worthy or judgment-only: sim-worthy —
the frontier is a computable table against pre-registered bands; the one
judgment call (is +0.10 trust-error reduction the right materiality line?) is
pinned by pre-registration and disclosed, with full curves shipped.

**7. Which lane should build it — and what does it displace or duplicate?**
sim-lab runs it (its harness, its verdict grammar; the sim + fixture JSON
committed in its sims/ tree). The verdict consumer is trading-strategy (the
trust line on its round-3 shortlist semantics) via the manager's routing per
Q-0260 — this repo never edits the lane's files, and anything owner-gated
stays proposal-only per the lane's own standing rule. Duplicates nothing: the
parent priced the null per arm, V028 priced the yield per grid, no verdict
V001–V034 prices arm-readability; the lane's own committed probes (squared-
return autocorrelation, rank-persistence) target the vol and (κ, E) axes and
stay named.

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one
stdlib file (chain + stream generator, 18 prefix-sum detectors, closed-form
ceilings/baselines, frozen-state and swap/ρ-invariance gates, the G6
occupancy kernel with its two chained anchors, twin evaluators), one fixture
JSON (grids, bands, seeds, exact π/baseline tables, the anchor pair with its
results.json pin), one results table {E, BA, ΔE_oracle, ΔE_always, lags} ×
(9 cells × 18 variants) plus the ceiling and occupancy-bar tables, ending in
exactly one of APPROVE/REJECT/NULL per the pre-registered rule — reproducible
from the fixtures alone, byte-identical stdout + results.json across two
process runs, CPython minor pinned, no flags.

**Recommendation: sim-ready** — the question is crisp and fully computable
against committed parent anchors, the bands and decision rule are registered
above BEFORE any code exists (REJECT checked first; the materiality line and
oracle baseline are the strict arms), both genre failure modes are pre-empted
(model-dependence → constants inherited from the parent + the declared flip
axes + the named one-script live probe; machinery error → exact seedless
ceilings and baselines, familywise-calibrated frozen-state gates, the
ρ-invariance and swap identities, and two chained V024 anchors with pre-pinned
tail-count tolerances), and the verdict changes what the lane may build in
every branch. THE ONE QUESTION for the simulator: *Under the pinned two-arm
drift-regime stream (per-bar Sharpe units: state D mean δ = 1.15/√252 =
0.07244319066010188 — V024's matched arm — state Z mean 0, unit Gaussian
noise, ρ-invariant by construction and asserted; 2-state Markov chain with
geometric sojourns, 9 decision cells (S_D, S_Z) ∈ {126, 252, 1008}² bars,
stationary start, T = 2,595 bars, scoring t ∈ [252, T), M = 1,000 paths per
cell), which of the 18 pre-registered cheap detectors — statistic ∈ {trailing
annualized Sharpe SR_w with pinned vol normalizer, trailing up-share UP_w} ×
w ∈ {63, 126, 252} × threshold position λ ∈ {0.3, 0.5, 0.7} (SR threshold
λ·1.15; UP threshold 1/2 + λ·(p_D − 1/2), p_D = 0.528875393055249) — removes
at least +0.10 of trust-misallocation rate vs the EXACT best-static-prior
baseline min(π_D, π_Z) per cell (ΔE_oracle, the V032 beat-the-best-static
discipline), in BOTH Arm A (exact, seedless: pure-window Gaussian/Binomial
operating characteristics via math.erf/math.comb, exact occupancies,
baselines, and flip-count expectations) and Arm S (seeded MC of the full
switching stream, seeds 20260772–75 allocated above the P033 high-water
20260771, familywise-calibrated frozen-state gates per the V027/V031 lesson,
swap and ρ-invariance identities, draw-count sentinels, twin evaluators,
two-process byte-identity, CPython minor pinned), with reporting-only legs
that cannot flip the decision (post-flip lag tables; ΔE_always vs the
de-facto always-trust rule; the realized-sd SR variant pricing vol
estimation; and the occupancy-graded bar leg — V024's committed G6 machinery
at IID/ρ = 0.3, φ_D ∈ {0, 0.25, 0.5, 0.75, 1}, chained to the committed
anchor pair q99(G6) = 0.604101 at φ = 0 and 0.366902 at φ = 1 via pre-pinned
tail-count tolerances) — landing (REJECT first) REJECT ("cheap drift-gating
never materially pays — no lane tooling; the round-3 registration carries the
quantified unhedgeable-degradation caveat") iff NO variant clears ΔE_oracle ≥
+0.10 in ≥ 3 of 9 cells, APPROVE ("ship the drift-conditional trust line with
the pinned detector row") iff ONE variant clears it in ≥ 7 of 9
stability-reproduced, or NULL (anything else — the per-cell frontier is the
citable pin, flip axes named via per-axis pass shares over occupancy skew and
min-sojourn, the conditional rule ships, and the one-script live probe — the
pinned best variant run once on the lane's own committed dev bars — locates
the lane's real (π_D, S) cell at zero holdout spend and zero owner clicks)?*
Done-when: the committed stdlib sim + fixture JSON (values copied verbatim
from this file) reproduce the full {E, BA, ΔE_oracle, ΔE_always, lag} ×
(cell, variant) table plus the exact ceiling table and the occupancy-bar leg
byte-identically across two process runs (Arm A platform-independent closed
forms; Arm S pinned to a stated CPython minor), every gate passes
(frozen-state familywise gates, occupancy/flip-count identities, swap and
ρ-invariance identities, both V024 tail-count anchors, sentinels, twin
evaluators), the seed-20260773 stability leg reproduces the same ruling, and
the verdict issues exactly ONE of APPROVE/REJECT/NULL per the pre-registered
rule (evaluation order stated, REJECT first) — stating the two-arm boundary
(the hardest fixed-gap version; real drift is a continuum), the
oracle-baseline conservatism (ΔE_always ships so a reader can re-weigh; the
ruling stays on the oracle bar), the observable-family boundary (threshold
detectors only; composite filters are the REJECT-case rescue family carrying
their own sim), and the no-trading boundary (trust gating only; the weakest
margin +0.130 stays promotion-weightless per V024 on every regime reading),
with the reporting-only legs stated as legs that cannot flip the decision;
honest-null explicit: a NULL lands as a finalized verdict naming the binding
axes and the conditional rule, not a re-run request.
