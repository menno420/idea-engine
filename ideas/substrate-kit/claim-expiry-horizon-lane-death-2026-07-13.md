# Claim-expiry horizons vs lane death — can silence-based abandonment be tuned, or does the fleet need lease renewal?

> **State:** sim-ready
> **Class:** process (pipeline rotation — inbox ORDER 004 rule 3's FLEET-BACKLOGS
> slot, round 3; round 1 harvested the websites backlog (P019 → V021), round 2 the
> superbot backlog (P021 → V023), this round rotates the harvest source into the
> kit-planted claims doctrine) ·
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline);
> verdict consumer: `menno420/substrate-kit` — the lane that owns the two planted
> horizon constants and the `claims-stale` checker this sim tunes or retires.

**Origin:** drafted this slice under standing owner ORDER 003 (continuous pipeline) +
ORDER 004 rule 3 ("Rotate lanes deliberately: fleet backlogs → …"). The survey
deliberately weighted the sections fleet-slot rotation has not yet tapped
(`ideas/substrate-kit/`, `ideas/superbot-next/`, `ideas/superbot-mineverse/`,
`ideas/product-forge/`) — and found their indexed heads are, by their own probes,
red/green contract checks ("no sim-lab proposal — no simulator question" on all six
substrate-kit heads; "nothing sim-shaped" across superbot-next; mineverse SECTION
COMPLETE). The genuinely sim-shaped material in that territory is where kit-planted
doctrine carries **invented constants**: the claim-expiry horizons. This file is
homed in `ideas/substrate-kit/` because the verdict's consumer surface is
kit-owned end to end.

## The premise (pinned, verified this slice)

The fleet's claim machinery expires claims by **inferred silence**:

- **The constants are planted fleet-wide and admittedly un-evidenced.** At
  substrate-kit HEAD `917261b3c49b465690031a97676131dea3b1f2c8` (anonymous blobless
  clone this slice): `src/engine/checks/check_claims.py:95` `CLAIM_STALE_HOURS = 24`
  (order claims), `:102` `WORK_CLAIM_STALE_HOURS = 72` (work claims) — and the kit's
  own comment at `:97–101`: "long sessions and weekend gaps are real, so the horizon
  is deliberately looser than the order-claim 24h. **Seeded at 72h; revisable by
  data like every horizon constant.**" No data exists. The planted prose mirrors the
  code: this repo's `control/README.md` § "Claiming an order" ("a claim with no
  visible build activity … after ~24h may be treated as abandoned") and
  `control/claims/README.md` § "Arbitration + expiry" ("older than ~72h with no
  visible build activity may be treated as abandoned — prune it on sight").
- **Both failure modes the horizon trades off are realized, not hypothetical.**
  Expire too EAGERLY and an alive-but-quiet lane gets its claim stolen → twin
  execution — the exact class the claim ritual was built for (substrate-kit PRs
  #50/#51: two lanes independently executed the same ORDER 005 the same day; a whole
  session's work reconciled as twins). Expire too LAZILY and a dead lane's claim
  blocks the work — the doctrine's own hard rule "a dead lane must never deadlock an
  order", and lanes really do die: product-forge CLOSED OUT with all triggers
  disarmed (`4fdfa8a`), the 2026-07-11 coordinator archive dismantled its own
  failsafes (docs/current-state.md § Ops facts), sim-lab OA-005 records a failsafe
  bound to a to-be-archived session.
- **The tension is live in this repo tonight** (anchor facts, reporting-only, n
  small): at HEAD `b11e2584`, `control/claims/claude-proposal-017.md` was pruned
  15.1 min after creation (added `80baad5` 01:02:33Z, deleted `d0dca70` 01:17:40Z)
  while `claude-proposal-018.md`–`023.md` sit UNDELETED 1.5–5.5 h after their
  sessions merged — real pruning lag next to real sub-hour tempo. Tonight's
  inter-claim-creation gaps ({0.26, 0.31, 0.56, 0.47, 1.28} h across 018→023)
  bracket the burst end of how often sibling sessions actually look at the claims
  directory.

The open question no one has priced: **is any silence horizon θ simultaneously safe
against twins and fast against orphans — and if so, are the planted 24 h / 72 h in
the feasible window, or does the answer depend so strongly on a lane's activity-gap
tail and the fleet's check tempo that silence is the wrong signal altogether** (in
which case the honest fix is an explicit lease-renewal stamp, a signal an
alive-but-quiet lane CAN send and a dead lane CANNOT)?

## The idea (reasoned to its fuller form — Q-0254 duty)

A pre-registered, fully hermetic dual-arm sim of the silence-expiry race. One claim
per replication:

**Lane model.** A lane claims at t=0 (a visible-activity event) and works through
**M further visible-activity events** (commits / PR pushes / heartbeat lines naming
the claim) separated by i.i.d. gaps G drawn from a two-component exponential mixture
(short intra-session gaps + a heavy tail of overnight/weekend silences — the kit
comment's "long sessions and weekend gaps are real", made a dial). Work completes at
the final event. **Death:** with probability p_d the lane dies immediately after a
uniformly chosen intermediate activity event and is silent forever (dead = never
returns; the archived-lane class above).

**Observer model.** Contender sessions check the claim at Poisson rate λ_c. At a
check, if silence = (now − last visible activity) > θ, the claim is treated as
abandoned and TAKEN OVER (pruned + re-claimed) — the doctrine's "prune on sight".

**Gap regimes (pinned mixtures, hours)** — the rows of the decision grid:
- **R1 burst-fleet** (tonight's shape): w = 0.9 on mean 1.5 h, 0.1 on mean 12 h; M = 6.
- **R2 daily-cadence**: w = 0.7 on mean 6 h, 0.3 on mean 24 h; M = 4.
- **R3 weekend-gapped**: w = 0.6 on mean 12 h, 0.4 on mean 48 h; M = 3
  (P(G > 72 h) ≈ 0.089 — alive lanes really can exceed the planted work horizon).

**Check-rate columns:** λ_c ∈ {1/4, 1/12, 1/48} h⁻¹ (C4 burst / C12 standard / C48
sparse — tonight's observed sub-hour claim tempo brackets C4 from below; a lane
checked only by 2-hourly-failsafe siblings across a quiet fleet sits near C48).
**9 decision cells** = 3 regimes × 3 check rates. **Horizon grid:**
θ ∈ {6, 12, 24, 48, 72, 168} h — both planted constants in-grid by design. p_d is
deliberately NOT a decision axis (see Arm A: neither decision metric depends on it);
p_d = 0.10 pinned for Arm S event weighting, sensitivity {0.02, 0.30} reporting-only.

**Decision metrics per (cell, θ):**
- **T** — false-takeover probability: P(an alive-throughout claim is stolen at least
  once before completion) — the twin-work risk.
- **O95** — p95 orphan latency: 95th percentile of (takeover time − death time) for
  dead claims — the deadlock cost.

**Arm A (seedless, exact closed forms — platform-independent).** For an exponential
gap component with mean m, memorylessness gives the per-gap steal probability
exactly: q_i(θ) = e^(−θ/m_i) · (λ_c·m_i)/(1 + λ_c·m_i); mixture
q(θ) = Σ w_i·q_i(θ); over M independent gaps and Poisson checks on disjoint windows,
**T_A = 1 − (1 − q(θ))^M** exactly. A dead claim is taken at the first Poisson check
after silence crosses θ: **O95_A = θ + ln(20)/λ_c** exactly. Arm A therefore covers
BOTH decision metrics on ALL 54 (cell, θ) points with no sampling error.

**Arm S (seeded event-driven MC — validates Arm A and adds the richer mechanics).**
M_S = 4,000 claims per (cell, θ), `random.Random(20260744)`, pinned loop order
(cells lexicographic R1→R3 then C4→C48; θ ascending; replications sequential; per
claim: death coin, death position, gaps in order, contender checks by
inter-arrival draws). **Agreement gates, run invalid on failure:**
|T_S − T_A| ≤ 1.0 pp on every (cell, θ), and |O95_S − O95_A| ≤ max(4 h, 5%
relative). **Decision-stability leg** seed 20260745, M_S = 1,000: must reproduce
the same ruling. **Reporting-only legs** (seed 20260746, cannot flip the decision):
p_d ∈ {0.02, 0.30}; takeover-chain extension (the taker can itself die; total
time-to-done per θ); wasted-sessions count on false takeover; multi-steal counts.
Aux self-check stream seed 20260747, never read by any decision number.
**Self-checks:** the p_d = 0 leg must produce zero orphan events; a θ → ∞ leg must
produce T = 0 exactly; per-leg draw-count audits; stdout + results.json
byte-identical across two process runs; CPython minor version pinned and asserted.
Seeds 20260744–47 allocated strictly above P024's registry high-water 20260743.

**Feasibility and decision rule (registered BEFORE any code; evaluated in this
order).** Feas(cell) = {θ in grid : T(θ) ≤ 0.05 AND O95(θ) ≤ 120 h} (twin risk at
most 1-in-20 alive claims; a dead lane blocks at most 5 days at p95); θ*(cell) =
min Feas(cell).
- **APPROVE** ("silence horizons work; pin ONE fleet-wide"): ∃ a single θ† in the
  grid with θ† ∈ Feas(cell) in ≥ 8 of 9 cells (Arm A exact values, Arm S gates
  passed, stability leg reproducing) → recommended row = the smallest such θ†; the
  verdict MUST state whether the planted WORK_CLAIM_STALE_HOURS = 72 lies within
  one grid step of θ†, and where the order-claim 24 h reading falls (see boundary).
- **REJECT** ("silence is the wrong signal — route the lease-renewal slice"):
  Feas(cell) = ∅ (no θ in the grid satisfies both bounds) in ≥ 5 of 9 cells.
- **NULL** (anything else — a legitimate and here plausible outcome): the flip axis
  named via per-axis feasible-cell shares and per-axis median θ* — expected
  candidates the R3 weekend tail (alive silences overlapping death from above) and
  the C48 sparse-check column (O95 = θ + 143.8 h structurally busting the latency
  band) — with the CONDITIONAL per-regime/per-tempo rule as the citable finding.

**Consequence, pre-registered.**
- **APPROVE** → the substrate-kit lane gets the evidence row for pinning
  `CLAIM_STALE_HOURS` / `WORK_CLAIM_STALE_HOURS` (`check_claims.py:95`/`:102`) at
  the sim-pinned θ† — the kit's own "revisable by data" comment contract, served
  with data; the planted "~24h/~72h" README prose graduates from vibes to measured.
  Routed lane-side via the manager sweep (Q-0260 — this repo never edits kit
  files); natural ride: the kit-lane fan-in bundle this section already tracks
  ("kit-lane fan-in now THREE routed heads — one ORDER could carry all three").
- **REJECT** → horizon tuning is abandoned as the fix: the routed build is an
  explicit **lease-renewal stamp** — claim bullets carry a `renewed: <ISO8601>`
  field re-stamped each working wake, and `claims-stale` keys on missed renewals (a
  signal an alive-but-quiet lane CAN send and a dead lane CANNOT), with the
  measured per-cell infeasibility table as the evidence row.
- **NULL** → the per-regime conditional table ships (e.g. silence horizons safe for
  burst/daily lanes at ≥ one check per 12 h; weekend-tail or sparse-check lanes
  need renewal stamps), and the cheapest LIVE probe is named: one `git log
  --diff-filter=AD` pass over `control/claims/` plus heartbeat `updated:` stamps in
  each adopted repo measures that repo's REAL (gap-tail, check-tempo) cell — zero
  new tooling, locating every lane on this verdict's grid before any constant is
  re-pinned.

## Relations (adjacent heads — deliberately links, not duplication)

- vs the outbox (001–024): **no proposal asks a claim-lifecycle question.** Nearest
  by METHOD (hermetic fleet-ops policy grid): P012 → V014 (control variable: wake
  scheduling; objective: worker-turns per caught trigger), P019 → V021 (backlog
  replenishment threshold; dry-wake fraction), P021 → V023 (migration ID-assignment
  policy; renumber treadmill) — same sim FAMILY, zero shared control variable,
  metric, fixture, or consumer: this head's variable is the abandonment horizon θ,
  its objectives are twin-rate vs orphan latency, its landing zone is
  `check_claims.py` + the planted claims doctrine. P013/P015's kit-heartbeat family
  is content LINTING, not claim lifecycle.
- vs superbot `tools/sim/claim_layout_sim.py` (cited by the doctrine itself): that
  sim measured claim STORAGE LAYOUT — shared-append vs one-file-per-claim merge
  conflicts (~98% vs 0%) via real `git merge` runs — and settled it; the EXPIRY
  question is untouched by it (different mechanism entirely). This head takes the
  settled layout as given.
- vs sim-lab verdicts V001–V024 (local clone @ `6c7e278`, offset map read; V025/026
  in flight for P023/P024): none touches claims, leases, TTLs, or abandonment — the
  word "claim" appears only as encounter-claim game mechanics (V001) and "covered
  claims" prose. Tree-wide `rg -i 'lease|ttl|abandonment horizon|claim-expir|
  claims-stale|renewal'` (bootstrap.py/.substrate excluded) hits only the claims
  doctrine files themselves.
- Runners-up this slice, deduped and dropped (honesty guard — genuine only): a kit
  upgrade-lag policy sim (the behind-stall head's own probe shows the binding
  question is a TOKEN-MECHANICS choice — plain-GITHUB_TOKEN pushes don't trigger
  workflows — not a rate question a sim would settle); mineverse shim-replay
  determinism (its own index: "no sim question until a real endpoint exists");
  superbot-next doctrine heads (all "nothing sim-shaped" — deterministic red/green
  checkers, proven by their own runs).

## Model basis (the P024 💡 field, dogfooded — declared model-dependence)

- **(1) Behavioral assumption the number rides on:** alive-lane silences follow a
  **two-component exponential-mixture gap model** and contender checks a **Poisson
  process** — standard neutral choices; the memoryless components are what make Arm
  A exact. The measured feasibility of any θ is a property of THESE tails at THESE
  check tempos (which is exactly why gap regime and check rate are the decision
  axes, bracketed wide).
- **(2) Single most-likely-to-flip alternative:** **empirically measured gap
  distributions** — real lane activity bunches at wake boundaries and weekends
  harder than any exponential mixture; a strongly bimodal measured tail would move
  every T(θ) curve. That flip is not a rival model to argue about — it is the
  named NULL-case live probe (one git-log pass per repo), which converts this
  question from modeling to measurement at zero tooling cost. Adversarial silence
  (a lane gaming the horizon) is explicitly out of scope: claims are cooperative
  machinery among honest lanes.

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained mechanism sim over
> pinned constants; report-only evidence, no spend/publish/irreversible surface —
> README § probe battery). Verify-first ran FIRST, live this slice: (a) **premise
> pins** — kit cloned anonymous/blobless @ `917261b3`, both constants + the
> "revisable by data" comment read in `check_claims.py` at the cited lines; the
> planted prose re-read in this repo's `control/README.md` + `control/claims/
> README.md` at HEAD `b11e2584`. (b) **dedup** — outbox 001–024 re-read at HEAD;
> the tree-wide lease/TTL/expiry sweep above returned only the doctrine files;
> sim-lab verdict ledger checked through V024. (c) **kill test NOT triggered** —
> no prior head prices claim expiry; the layout sim is a different mechanism;
> the anchor facts (15-min prune vs 6 undeleted claims) confirm both directions
> of the tension are live TONIGHT. (d) **feasibility arithmetic** — Arm A is 54
> closed-form evaluations (instant); Arm S is 9 × 6 × 4,000 short event walks
> (~10⁶ events) — seconds in pure CPython, stdlib-only.

**1. What is this really?** A pre-registered measurement of whether
silence-inferred abandonment — the mechanism the kit plants in every adopted repo —
can be tuned to be simultaneously twin-safe (T ≤ 0.05) and orphan-fast (O95 ≤
120 h), across the gap-tail regimes and check tempos the fleet actually spans; and
a decision, with the kit's two planted horizon constants standing in-grid as named
defendants. The kit's source comment ("revisable by data like every horizon
constant") is a standing order this sim fills.

**2. What is the possibility space?** (i) Do nothing — the constants stay vibes;
every adopted repo inherits them; the next twin or deadlock re-litigates by
anecdote. (ii) Tune by live incident data — there are ~2 labeled incidents
(one twin pair, zero measured orphan takeovers); years from powered. (iii) A pure
closed-form note without pre-registration — computes the same curves but decides
nothing (no bands, no consequence; the P019/P021 lesson is the registered decision
rule is what makes the number binding). (iv) This head: exact dual-arm sweep,
bands first, three pre-registered consequences each of which is a real routed
action. (v) Over-scope (multi-claim contention queues, adversarial lanes,
manager-side arbitration) — different questions, named out of scope; the
layout/collision half is already measured art.

**3. What is the most advanced capability reachable by the simplest
implementation?** One ~250-line stdlib file. The memoryless-mixture choice makes
the ENTIRE decision surface closed-form (T_A and O95_A exact on all 54 points —
zero sampling error where it matters), with the MC arm reduced to validation plus
the reporting-only rich mechanics (takeover chains, wasted work). A complete
feasibility atlas of a fleet-wide coordination constant, byte-reproducible, from
constants a reviewer can check by hand against the two formulas.

**4. What breaks it? (assumptions made explicit)** (a) **The gap model is a
model** — declared in `## Model basis` with the empirical-measurement flip named
as the NULL-case probe; regimes bracket wide (means 1.5 h → 48 h tails). (b)
**Poisson contender checks** — real checks bunch at wake bursts; bracketed by the
C4/C48 axis rather than modeled as bursts (boundary stated in the verdict). (c)
**Decision metrics are p_d-free by construction** — T conditions on alive claims,
O95 on dead ones; p_d only weights how often each mode is PAID, so it is a
reporting dial, not a decision axis (stated, so no reader mistakes the grid for
ignoring death rates). (d) **Single-claim independence** — no contention among
contenders for the same steal; first-check-wins is the doctrine's own rule and
the steal timing is what matters, not the winner. (e) **Order-claim mapping is a
READING, not a sweep** — the sim models the work-claim class; the verdict reads
the 24 h order constant against the burst-regime columns and says so (order
execution gaps are contractually short: "claim FIRST, build second"), never
claiming a separate order-class sweep ran.

**5. What does it unlock?** The first evidence row for a kit constant that every
adopted repo inherits (the kit's own comment invites exactly this); on REJECT, the
lease-renewal slice with its infeasibility table attached — a mechanism change
justified by measurement instead of the next incident; on NULL, a per-regime rule
plus a zero-tooling probe that locates every real lane on the grid; and a
completed round-3 fleet-backlogs rotation slot harvested from a THIRD distinct
backlog source (websites → superbot → kit doctrine).

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing at verdict
time — fully hermetic (the P017–P024 discipline): every fixture is a pinned
constant committed with the sim; the kit-line premise pins and the anchor
multisets are quoted INTO the fixture JSON at drafting, zero network reads in the
verdict session. Kill tests run live this slice: prior claim-lifecycle head
anywhere (NOT found), the layout sim covering expiry (it does NOT — real-merge
layout mechanics only), constants already evidence-backed (NOT — the kit comment
says seeded), runtime infeasible (NOT — arithmetic above). Sim-worthy or
judgment-only: sim-worthy — both metrics are computable probabilities against
registered bands; the one judgment question (are 0.05 / 120 h the right
materiality lines?) is pinned by pre-registration and shipped with full curves so
a re-drawn line re-reads, never re-runs.

**7. Which lane should build it — and what does it displace or duplicate?**
sim-lab runs it (harness, verdict grammar, sims/ tree). The verdict consumer is
the substrate-kit lane (constants + checker + planted doctrine); co-consumers:
every kit-adopted seat (inherits any re-pin via upgrade), the fleet manager
(routing + the fan-in bundle), idea-engine as first adopter and anchor-data
source. Duplicates nothing: layout ≠ expiry, and no verdict through V024 touches
claim lifecycle.

**8. What is the smallest shippable slice?** One sim-lab intake dir: one stdlib
file (closed-form Arm A + event-driven Arm S + gates + self-checks), one fixture
JSON ({regime mixtures (w, m₁, m₂, M), λ_c grid, θ grid, p_d constants, M_S,
seeds 20260744–47, band constants (0.05, 120 h, 8/9, 5/9), anchor multisets
quoted}, values copied verbatim from this file), one results table
{T, O95} × (cell, θ) plus the Feas/θ* summary and per-axis shares, ending in
exactly ONE of APPROVE/REJECT/NULL per the pre-registered rule — byte-identical
on re-run (Arm A platform-independent closed forms; Arm S pinned to a stated
CPython minor version), no flags.

**Recommendation: sim-ready** — the question is crisp and fully computable, the
bands and three-consequence decision rule are registered above BEFORE any code
exists, both genre failure modes are pre-empted (model-dependence → declared
model basis + bracketed decision axes + the named empirical flip probe;
degeneracy → p_d-free decision metrics stated, exact-identity self-checks), and
every outcome changes what a reader does: pin the constants, build the renewal
stamp, or ship the conditional rule + measure the real cells. THE ONE QUESTION
for the simulator: *Under the pinned silence-expiry race model (one claim per
replication; an alive lane emits M+1 visible-activity events separated by i.i.d.
gaps from a two-component exponential mixture — R1 burst (0.9 on mean 1.5 h, 0.1
on 12 h, M=6), R2 daily (0.7 on 6 h, 0.3 on 24 h, M=4), R3 weekend (0.6 on 12 h,
0.4 on 48 h, M=3); with probability p_d = 0.10 the lane instead dies silent after
a uniform intermediate event; contenders check at Poisson rate λ_c ∈ {1/4, 1/12,
1/48} h⁻¹ and take over any claim silent past θ ∈ {6, 12, 24, 48, 72, 168} h —
both kit-planted constants in-grid), what are T (false-takeover probability for
alive-throughout claims) and O95 (p95 death→takeover latency for dead claims) per
(regime × check-rate) cell and θ — in BOTH Arm A (seedless exact closed forms:
T_A = 1 − (1 − Σᵢ wᵢ·e^(−θ/mᵢ)·λ_c·mᵢ/(1+λ_c·mᵢ))^M; O95_A = θ + ln(20)/λ_c) and
Arm S (seeded event-driven MC, M_S = 4,000 per (cell, θ), seed 20260744, pinned
loop order; gates |T_S − T_A| ≤ 1.0 pp and |O95_S − O95_A| ≤ max(4 h, 5%) on
every point or the run is invalid; stability leg seed 20260745 must reproduce the
ruling; reporting-only legs seed 20260746: p_d ∈ {0.02, 0.30}, takeover chains,
wasted sessions) — and with Feas(cell) = {θ : T ≤ 0.05 AND O95 ≤ 120 h}, does the
result land (evaluated in this order) APPROVE ("pin one fleet-wide horizon": ∃
single θ† feasible in ≥ 8 of 9 cells → recommended θ† = the smallest, the verdict
stating whether the planted 72 h lies within one grid step of it and where the
24 h order-class reading falls), REJECT ("silence is the wrong signal — route the
lease-renewal `renewed:` stamp slice": Feas = ∅ in ≥ 5 of 9 cells), or NULL
(anything else — the flip axis named via per-axis feasible shares and median θ*,
expected candidates the R3 weekend tail and the C48 sparse-check column, the
conditional per-regime rule the citable finding)?* Done-when: the committed
stdlib sim + fixture JSON reproduce the full {T, O95} × (cell, θ) table, the
Feas/θ*/per-axis-share summary, and all gate/self-check results byte-identically
on re-run, and the verdict issues exactly ONE of APPROVE/REJECT/NULL per the
pre-registered rule (evaluation order stated) — stating the model-basis caveat
(exponential-mixture gaps × Poisson checks; the empirical git-log measurement
named as the flip AND as the NULL-case probe), the p_d-free-decision-metrics
boundary, the cooperative-lanes boundary (adversarial silence out of scope), and
the order-claim reading-not-sweep boundary, with the reporting-only legs stated
as legs that cannot flip the decision; honest-null explicit: a NULL lands as a
finalized verdict naming the binding axis, not a re-run request.
