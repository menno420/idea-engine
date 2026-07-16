# ideas/fleet

> **Target: the fleet itself** — cross-cutting workflow/doctrine/process ideas (routed
> toward the manager / substrate-kit), not any single lane.

## Index

- [`section-sync-checker-2026-07-10.md`](section-sync-checker-2026-07-10.md) — manifest-derived
  section sync checker · historical(#2): probed + built in the same PR
  (`scripts/check_sections.py`); origin: seed card 💡
- [`probe-report-lint-2026-07-10.md`](probe-report-lint-2026-07-10.md) — idea-grammar lint
  for the ideas tree · historical(#11): probed + built in the same PR
  (`scripts/check_ideas.py`); origin: first-probe card 💡
- [`wake-preflight-wrapper-2026-07-10.md`](wake-preflight-wrapper-2026-07-10.md) — one-command
  preflight wrapper · historical(#16): probed + built in the same PR
  (`scripts/preflight.py`); origin: PR #2 card 💡
- [`gate-ritual-convergence-2026-07-10.md`](gate-ritual-convergence-2026-07-10.md) — CI gate and
  wake ritual converge on `scripts/preflight.py` as the one check list · historical(#18):
  probed + built in the same PR (`substrate-gate.yml` non-control lane); origin: PR #16 card 💡
- [`harvest-freshness-checker-2026-07-10.md`](harvest-freshness-checker-2026-07-10.md) — link-index
  harvest drift checker (pin moved · new upstream docs · deleted upstream docs) ·
  historical(#22): probed + built in the same PR (`scripts/check_harvest.py`, wake-time,
  NOT preflight); origin: PR #7 card 💡, dispatched via PR #21 card
- [`open-work-preflight-sweep-2026-07-10.md`](open-work-preflight-sweep-2026-07-10.md) — report-only
  open-work advisory sweep (sibling remote branches + local dirt at wake/pre-push, always
  exit 0 — never gates) · historical(#42): probed + built in the same PR
  (`scripts/preflight.py --open-work`, sixth CHECKS entry); origin: PR #40 card 💡 via the
  websites open-pr-awareness probe
- [`branch-prefix-drift-tripwire-2026-07-11.md`](branch-prefix-drift-tripwire-2026-07-11.md) — report-only
  merged-branch-prefix vs `automerge.branch_patterns` drift advisory (recurring unmatched
  prefix = the enabler silently stopped arming that convention, always exit 0 — never
  gates) · historical(#62): probed + built in the same PR
  (`scripts/preflight.py --branch-prefix-drift`, seventh CHECKS entry); origin: PR #55
  card 💡
- [`stop-hook-telemetry-loop-exemption-2026-07-11.md`](stop-hook-telemetry-loop-exemption-2026-07-11.md) — end the
  self-feeding one-line telemetry-PR loop (#58..#100): exempt the three kit state
  anchors (`.substrate/guard-fires.jsonl` / `reflections.json` / `state.json`) + auto-drafted
  content-free session stubs from the HARNESS stop hook's git-cleanliness nag — nag-only,
  telemetry stays committable · park(built-here — `scripts/patch-stop-hook-git-check.sh`,
  SessionStart-wired, this PR); origin: the merged-PR ledger itself
- [`lint-bundle-2026-07-11.md`](lint-bundle-2026-07-11.md) — five standing advisory
  lint heads accumulated across session cards, built as one bundle · park(built-here —
  RECOMMENDATION + STATE-ECHO in `scripts/check_ideas.py` · `--states` in
  `scripts/check_harvest.py` · `--step-anchor-drift` + `--heartbeat-keys` in
  `scripts/preflight.py`, ninth/tenth CHECKS entries; six rotted index badges fixed by
  the live run); origin: PR #36/#29/#33/#22/#59 card 💡s, bundle-named by the PR #59
  card and the PR #144 grooming ledger
- [`coordinator-archive-handoff-ceremony-2026-07-11.md`](coordinator-archive-handoff-ceremony-2026-07-11.md) — kit-blessed
  archive-ready ceremony for a coordinator-chat archive (bounded wait on sibling
  claims · sweep · session enders · durable archive note · trigger disposition
  table · heartbeat last) · captured; origin: the 2026-07-11 archive close-out
  card 💡
- [`carried-watch-verdict-inheritance-guard-2026-07-12.md`](carried-watch-verdict-inheritance-guard-2026-07-12.md) — carried
  heartbeat watches must name and re-verify the verdict/evidence that justified them
  (`watch: <claim> · verified <ISO>` + report-only staleness advisory, mandatory re-affirm
  at generation handoff) · parked(routed — kit/manager layer: fifth-touch rider on the
  merge-hold substrate-kit slice — watch grammar + report-only `--watch-freshness`
  advisory; /fleet badge = manager rider); origin: websites backlog bullet @ `e14bb15`
  (line 158), surfaced as the one unrouted candidate by the PR #244 lane-backlog groom
- [`routine-cadence-economics-sim-2026-07-12.md`](routine-cadence-economics-sim-2026-07-12.md) — deterministic
  replay-and-sweep sim pricing wake policy (failsafe cadence × pacemaker chain ×
  event-driven wakes) in worker-turns per caught trigger vs catch latency, calibrated
  on this seat's own ~14h heartbeat trail (`fc0bab6..531b109`) · sim-ready (VERDICT 014 ·
  approve 2026-07-12 — keep hybrid(event-driven + failsafe-2h), posture unchanged; state
  stays per grammar, the V012/V013 precedent; PROPOSAL 012 consumed; sim-lab #53 @
  `477b452`, report `sims/verdict-014-routine-cadence-economics/`); feeds the ≤2026-07-13 post-EAP
  routine posture decision (fm `OQ-SITTING-0714-DECISIONS`); origin: generated this
  slice from the seat's own wake record
- [`heartbeat-contradiction-linter-2026-07-12.md`](heartbeat-contradiction-linter-2026-07-12.md) — heartbeat
  single-home rule (one fact, one block) + intra-file contradiction linter, specced as a
  measured (extraction grammar × normalization × scope) sweep over the real 22-revision
  `control/status.md` corpus (live specimen: `c77563c` LEFT ARMED vs DISMANTLED, same
  trigger id; hard FP case: `e66c78a`'s quotation-negation carry) · sim-ready; origin:
  session-2 boot card 💡, promoted as PROPOSAL 013
- [`external-review-authenticity-gate-2026-07-12.md`](external-review-authenticity-gate-2026-07-12.md) — mechanical
  pre-trust gate for external review replies: every checkable cited artifact (commit
  SHA in refs · PR/branch exists · path exists at the cited blob · line range ≤ EOF)
  validates against pinned repo state before the reply counts as signal, specced as a
  measured (extraction grammar × validation set × decision rule) sweep over the three
  recorded fabricated @codex replies (sim-lab #44/#53, 2026-07-12) vs the
  verified-genuine review corpus (idea-engine #264/#265, 17/17 accepted) ·
  sim-ready; origin: drafted this slice from sim-lab's fabrication-incident ledger
  (`dedc12e`) under standing ORDER 003, promoted as PROPOSAL 014
- [`irv-monotonicity-close-races-2026-07-13.md`](irv-monotonicity-close-races-2026-07-13.md) — first
  COMPLETELY-UNRELATED-domain rotation head (inbox ORDER 004 rule 3; domain: social
  choice — 3-candidate instant-runoff voting): pre-registered dual-arm sim (exhaustive
  IAC enumeration n=13/25 + seeded IC Monte Carlo n=99/1,001) measuring how often
  raising the winner makes it lose, overall vs close races, against registered
  APPROVE/REJECT/NULL bands (V_close ≥ 10% both arms / < 5% both / straddle =
  honest-null model-dependence finding) · sim-ready; homed here per the
  `check_sections.py` non-lane carve-out (roster-derived sections — no ad-hoc section;
  flagged in the file's placement note), promoted as PROPOSAL 017; origin: drafted
  this slice under ORDER 003 + ORDER 004 rule 3
- [`braess-paradox-added-edge-2026-07-13.md`](braess-paradox-added-edge-2026-07-13.md) — round-2
  COMPLETELY-UNRELATED-domain rotation head (inbox ORDER 004 rule 3; domain:
  transportation / Braess routing-game congestion — Wardrop selfish-user equilibrium,
  a DIFFERENT fleet-external domain from P017's social choice): pre-registered dual-arm
  sim (exhaustive integer census over affine-latency coefficients, 9⁴·4=26,244 fixtures,
  exact Fraction + seeded continuous Monte Carlo, seeds 20260740–43) measuring how OFTEN
  and by HOW MUCH adding a shortcut edge RAISES selfish-equilibrium travel cost, against
  registered APPROVE/REJECT/NULL bands (f_A ≥ 15% OR median-inflation ≥ 1.15 / f_A ≤ 3%
  AND max-inflation ≤ 1.05 / straddle-or-arm-disagreement = honest null) · sim-ready;
  homed here per the `check_sections.py` non-lane carve-out (roster-derived sections — no
  ad-hoc section; flagged in the file's placement note), promoted as PROPOSAL 024;
  origin: drafted this slice under ORDER 003 + ORDER 004 rule 3
- [`tournament-seeding-bracket-optimality-2026-07-13.md`](tournament-seeding-bracket-optimality-2026-07-13.md) — round-3
  COMPLETELY-UNRELATED-domain rotation head (inbox ORDER 004 rule 3; domain: sports
  statistics / tournament-format design — single-elimination bracket seeding under a
  Bradley–Terry win-probability model, a THIRD fleet-external domain after P017's
  social choice and P024's congestion routing): pre-registered fully-exact census sim
  (all 315 distinct 8-team brackets = 8!/2⁷, four committed strength profiles, exact
  `fractions.Fraction`, ZERO RNG/seeds/floats — dual independent algorithms gated on
  rational equality) measuring whether the standard seeding (1v8, 4v5 | 3v6, 2v7) is
  EXACTLY optimal for P(best team wins) and P(1-vs-2 final), against registered
  APPROVE/REJECT/NULL bands (REJECT iff exactly optimal in all 4 profiles, checked
  first / APPROVE iff suboptimal by ≥ 0.5 pp on (a) or ≥ 1.0 pp on (b) anywhere /
  straddle = honest null pinning the exact gap table) · sim-ready; homed here per the
  `check_sections.py` non-lane carve-out (roster-derived sections — no ad-hoc section;
  flagged in the file's placement note), promoted as PROPOSAL 028; origin: drafted
  this slice under ORDER 003 + ORDER 004 rule 3
- [`penney-game-responder-edge-decay-2026-07-13.md`](penney-game-responder-edge-decay-2026-07-13.md) — round-4
  COMPLETELY-UNRELATED-domain rotation head (standing ORDER 003 continuous pipeline,
  rotation per ORDER 004 rule 3; domain: recreational probability / sequential
  pattern-race games — Penney's game over fair-coin words, a FOURTH fleet-external
  domain after P017's social choice, P024's congestion routing, and P028's tournament
  seeding): pre-registered fully-exact census sim (all ordered word pairs at
  L ∈ {3,4,5} = 56/240/992 cells, exact `fractions.Fraction`, ZERO RNG/seeds/floats —
  Conway leading numbers vs an independent automaton-absorption arm gated on rational
  equality, classic anchors 3/4 · 7/8 · V(3)=2/3 as validity gates) measuring the decay
  curve of the responder's guaranteed minimax edge V(L) and the popularized flip-rule
  beater's exact optimality share, against registered APPROVE/REJECT/NULL bands
  (REJECT iff V(5) ≤ 13/25, stated first / APPROVE iff V(L) ≥ 3/5 at all swept L /
  straddle = honest null pinning the exact decay curve) · sim-ready; homed here per
  the `check_sections.py` non-lane carve-out (roster-derived sections — no ad-hoc
  section; flagged in the file's placement note), promoted as PROPOSAL 032; origin:
  drafted this slice under standing ORDER 003 (rotation rule per ORDER 004 rule 3)
- [`secretary-rule-cardinal-regret-2026-07-13.md`](secretary-rule-cardinal-regret-2026-07-13.md) — round-5
  COMPLETELY-UNRELATED-domain rotation head (standing ORDER 003 continuous pipeline,
  rotation per ORDER 004 rule 3; domain: sequential search / optimal stopping — the
  secretary problem's popularized "37% rule", a FIFTH fleet-external domain after
  P017's social choice, P024's congestion routing, P028's tournament seeding, and
  P032's pattern races): pre-registered fully-exact census sim (all 379 (N, r) cutoff
  cells over N ∈ {5,10,20,50,100,200} × 2 objectives × 2 end conventions, exact
  `fractions.Fraction`, ZERO RNG/seeds/floats — analytic closed forms vs an independent
  combinatorial rank-census arm gated on rational equality, plus a full permutation
  census at N ∈ {5,6,7} and classic anchors 1/2 · 11/24 · 13/30 as validity gates)
  measuring the folk cutoff's exact cardinal regret ΔV(N) against the best cutoff in
  its own family and its untold downside B(N) = P(bottom-half hire), against
  registered APPROVE/REJECT/NULL bands (REJECT iff ΔV ≤ 1/50 at every swept N, stated
  first / APPROVE iff ΔV ≥ 1/20 AND B ≥ 3/20 at every swept N ≥ 50 / anything else =
  honest null pinning the exact frontier; band liveness disclosed in-file) ·
  sim-ready; homed here per the `check_sections.py` non-lane carve-out (roster-derived
  sections — no ad-hoc section; flagged in the file's placement note), promoted as
  PROPOSAL 036; origin: drafted this slice under standing ORDER 003 (rotation rule per
  ORDER 004 rule 3)
- [`schelling-mild-preference-tipping-2026-07-13.md`](schelling-mild-preference-tipping-2026-07-13.md) — round-6
  COMPLETELY-UNRELATED-domain rotation head (standing ORDER 003 continuous pipeline,
  rotation per ORDER 004 rule 3; domain: emergent spatial self-organization /
  agent-based relocation dynamics — Schelling segregation tipping, a SIXTH
  fleet-external domain after P017's social choice, P024's congestion routing, P028's
  tournament seeding, P032's pattern races, and P036's optimal stopping):
  pre-registered seeded relocation-dynamics sweep (40×40 torus, 720/720/160 A/B/vacant,
  Moore-8, satisfaction = like-fraction among occupied neighbors ≥ τ with
  zero-occupied-neighbors ⇒ satisfied, live random-serial sweeps with uniform-random
  vacant-cell relocation to fixation or cap 500, τ grid {1/8, 1/4, 3/10, 3/8, 1/2,
  5/8, 3/4}, seeds 20261297–300, decision numbers exact Fractions) measuring whether
  the integration-compatible preference τ = 0.30 still amplifies into strong global
  segregation — median terminal like-neighbor share s(0.30) against registered
  APPROVE/REJECT/NULL bands (REJECT iff median < 11/20, stated first / APPROVE iff
  median ≥ 7/10 AND the stability leg reproduces / anything else = honest null naming
  the binding axis from four pre-registered shapes; no closed form exists, no
  expected landing pinned) · sim-ready; homed here per the `check_sections.py`
  non-lane carve-out (roster-derived sections — no ad-hoc section; flagged in the
  file's placement note), promoted as PROPOSAL 040; origin: drafted this slice under
  standing ORDER 003 (rotation rule per ORDER 004 rule 3)
- [`checkout-pooling-single-line-2026-07-13.md`](checkout-pooling-single-line-2026-07-13.md) — round-7
  COMPLETELY-UNRELATED-domain rotation head (standing ORDER 003 continuous pipeline,
  rotation per ORDER 004 rule 3; domain: stochastic service operations /
  queue-discipline design — the supermarket checkout pooling folk law, a SEVENTH
  fleet-external domain after P017's social choice, P024's congestion routing, P028's
  tournament seeding, P032's pattern races, P036's optimal stopping, and P040's
  spatial self-organization): pre-registered discrete-time common-random-numbers sim
  (c = 3 registers, Bernoulli-per-tick arrivals `randrange(35) < A` with decision cell
  A = 27 ⇒ ρ = 9/10 exactly, service pmf {2:3, 3:3, 4:2, 6:2}/10 with mean 7/2,
  POOLED vs SPLIT-RANDOM decision pair + SPLIT-JSQ reporting-only on the identical
  per-run stream, T = 20,000 with warm-up 2,000 and drain-to-empty so every wait is
  an exact integer, seeds 20261313–316, decision numbers exact Fractions) measuring
  whether ONE shared line beats per-register lines "dramatically" — the median
  per-run cohort mean-wait ratio R = Ŵ(SPLIT-RANDOM)/Ŵ(POOLED) against registered
  APPROVE/REJECT/NULL bands (REJECT iff median R < 3/2, stated first / APPROVE iff
  median R ≥ 2 AND the stability leg reproduces / anything else = honest null naming
  the binding axis from four pre-registered shapes; no closed form binds the lattice
  frame, no expected landing pinned) · sim-ready; homed here per the
  `check_sections.py` non-lane carve-out (roster-derived sections — no ad-hoc
  section; flagged in the file's placement note), promoted as PROPOSAL 044; origin:
  drafted this slice under standing ORDER 003 (rotation rule per ORDER 004 rule 3)
- [`parrondo-losing-games-combine-2026-07-13.md`](parrondo-losing-games-combine-2026-07-13.md) — round-8
  COMPLETELY-UNRELATED-domain rotation head (standing ORDER 003 continuous pipeline,
  rotation per ORDER 004 rule 3; domain: stochastic-ratchet / capital-dependent game
  switching — Parrondo's paradox, an EIGHTH fleet-external domain after P017's social
  choice, P024's congestion routing, P028's tournament seeding, P032's pattern races,
  P036's optimal stopping, P040's spatial self-organization, and P044's queue-discipline):
  pre-registered dual-arm sim (Arm A = seedless exact `fractions.Fraction` stationary
  solve + renewal drift on the capital-mod-3 random-switch Markov chain, the DECISION arm;
  Arm B = seeded Monte-Carlo drift validation, seeds 20261329–332) measuring whether two
  individually-losing games (Game A `a = 49/100`; capital-dependent Game B `b0 = 9/100`,
  `b1 = 37/50` at `EPS = 1/100`, `M = 3`) combine into a WINNER by a MATERIAL margin — the
  combined per-step drift `D_mix` against registered APPROVE/REJECT/NULL bands (REJECT iff
  `D_mix ≤ 0`, stated first / APPROVE iff `D_mix ≥ 1/1000` AND the stability leg reproduces
  / NULL in the thin `0 < D_mix < 1/1000` band or on validity failure; INVALID gate on the
  two isolated-loss preconditions; expected landing DISCLOSED — APPROVE, thinly, at the
  drafter's `D_mix = 26673/4429850 ≈ 0.006`, the sim re-derives from scratch) · sim-ready;
  homed here per the `check_sections.py` non-lane carve-out (roster-derived sections — no
  ad-hoc section; flagged in the file's placement note), promoted as PROPOSAL 048; origin:
  drafted this slice under standing ORDER 003 (rotation rule per ORDER 004 rule 3)
- [`coupon-collector-tail-2026-07-14.md`](coupon-collector-tail-2026-07-14.md) — round-9
  COMPLETELY-UNRELATED-domain rotation head, the round-9 closer (standing ORDER 003
  continuous pipeline, rotation per ORDER 004 rule 3; domain: occupancy & collection
  problems / the coupon collector's tail, a NINTH fleet-external domain after P017's
  social choice, P024's congestion routing, P028's tournament seeding, P032's pattern
  races, P036's optimal stopping, P040's spatial self-organization, P044's
  queue-discipline, and P048's stochastic ratchets): pre-registered dual-arm sim
  (Arm A = seedless exact `fractions.Fraction` harmonic-sum decision arm, the tail-cost
  fraction φ(N) = H_m/H_N over the grid N ∈ {20,50,100,200} with last-10% tail
  m = ⌈N/10⌉ = {2,5,10,20}, decision cell N = 50; Arm S = seeded MC draw-until-complete
  confirmation, N_runs = 200,000 via `random.Random(20261345)`, agreement gate
  |mean_S − E_A|/E_A ≤ 1/100 AND ≤ 4·SE per cell; seeds 20261345–348) measuring whether
  the folk belief "once you've got most of a random-draw set you're basically done" fails
  in the costly direction — φ against registered APPROVE/REJECT/NULL bands (REJECT iff
  φ(50) ≥ 2/5 AND φ(N) ≥ 2/5 in ≥ 3 of 4 cells AND Arm S confirms, stated first / APPROVE
  iff φ(N) ≤ 1/5 at EVERY grid N AND the seed-20261346 stability leg reproduces / anything
  else = honest null naming the binding axis; INVALID controls gate on the H_N /
  φ(m=N)=1 / φ(m=1)=1/H_N / exact-CDF / Arm-S identities; expected landing DISCLOSED per
  the closed-form-arm norm — REJECT at the drafter's exact φ(50) = (137/60)/H_50 ≈ 0.508,
  the sim re-derives from scratch) · sim-ready; homed here per the `check_sections.py`
  non-lane carve-out (roster-derived sections — no ad-hoc section; flagged in the file's
  placement note), promoted as PROPOSAL 052; origin: drafted this slice under standing
  ORDER 003 (rotation rule per ORDER 004 rule 3)
- [`inspection-paradox-wait-inflation-2026-07-14.md`](inspection-paradox-wait-inflation-2026-07-14.md) — round-10
  COMPLETELY-UNRELATED-domain rotation head, the round-10 closer (standing ORDER 003
  continuous pipeline, rotation per ORDER 004 rule 3; domain: renewal theory & random
  incidence / the inspection (waiting-time) paradox, a TENTH fleet-external domain after
  P017's social choice, P024's congestion routing, P028's tournament seeding, P032's
  pattern races, P036's optimal stopping, P040's spatial self-organization, P044's
  queue-discipline, P048's stochastic ratchets, and P052's occupancy & collection):
  pre-registered dual-arm sim (Arm A = seedless exact `fractions.Fraction` moment
  arithmetic, the wait-inflation factor ρ = E[X²]/E[X]² = 1 + CV² and E[W] = E[X²]/(2E[X])
  over five equal-mean-10 headway schedules CLOCKWORK/JITTER/SPREAD/MEMORYLESS/BUNCHED
  with CV² ∈ {0, 1/25, 1/10, 9/10, 64/25}; Arm S = seeded renewal-trajectory +
  uniform-landing MC confirmation, K = 100,000 intervals + N = 200,000 landings per cell
  via `random.Random(20261361)`, agreement gate ≤ 1/100 relative AND ≤ 4·SE on E[W] and
  P(W > 10) per cell; seeds 20261361–364) measuring whether the folk rule "average wait =
  half the average headway" fails in the costly direction — ρ against registered bands
  (REJECT iff ρ(BUNCHED) ≥ 2 AND ρ ≥ 11/10 in ≥ 3 of 4 stochastic cells AND Arm S
  confirms, stated first / APPROVE iff ρ ≤ 21/20 at EVERY stochastic cell AND the
  seed-20261362 stability leg reproduces / anything else = honest null naming the binding
  axis; INVALID controls gate on the pmf / size-bias / degenerate / monotonicity / hand
  identities; expected landing DISCLOSED per the closed-form-arm norm — REJECT at the
  drafter's exact ρ(BUNCHED) = 89/25 = 3.56 with E[W] = 89/5 = 17.8 min exceeding the
  entire 10-min mean headway, the sim re-derives from scratch) · sim-ready; homed here
  per the `check_sections.py` non-lane carve-out (roster-derived sections — no ad-hoc
  section; flagged in the file's placement note), promoted as PROPOSAL 056; origin:
  drafted this slice under standing ORDER 003 (rotation rule per ORDER 004 rule 3)
- [`cascade-independence-quota-2026-07-15.md`](cascade-independence-quota-2026-07-15.md) — round-12
  COMPLETELY-UNRELATED-domain rotation head, the round-12 closer (standing ORDER 003
  continuous pipeline, rotation per ORDER 004 rule 3; domain: sequential observational
  learning / information cascades — the BHW mechanism priced against a mandated
  blind-first independence quota, a TWELFTH fleet-external domain after P017's social
  choice, P024's congestion routing, P028's tournament seeding, P032's pattern races,
  P036's optimal stopping, P040's spatial self-organization, P044's queue-discipline,
  P048's stochastic ratchets, P052's occupancy & collection, P056's random incidence,
  and P060's repeated-game reciprocity; flags the EAP walkthrough §E "round 13 opens at
  fleet-backlogs" baton miscount — the committed spacing-4 slot arithmetic puts P064
  here): pre-registered fully-deterministic sim (Arm A = seedless exact
  `fractions.Fraction` absorbing-walk DP over the revealed-lead states with a
  Binomial(k, p) quota initial condition, p ∈ {11/20, 7/10, 4/5, 9/10} × N ∈ {25, 100,
  400} × quota k ∈ {0..min(N, 120)} + the p = 1/2 degeneracy and p = 1 anchors; Arm B =
  independently-written backward-recursion twin, exact-equal on every number, plus a
  2^12 exhaustive path census at N = 12; Arm R = seeded traces REPORTING-ONLY, seeds
  20261563–566, no statistical gate) measuring whether the folk claim "more visible
  history never hurts — the crowd self-corrects" survives its own herding tax —
  decision-cell (p = 7/10, N = 100) gain of the optimal blind-first quota against
  registered bands (REJECT iff G ≥ 6 correct actions AND k\* ≥ 5 AND e(k\*) ≤ e(0)/2,
  stated first / APPROVE iff G ≤ 2 AND k\* ≤ 2 / anything else = honest null naming the
  binding axis; INVALID controls gate on the Bayes-identity, three structure theorems
  (quota-null, parity, knife-edge), closed-form-anchor, hand-world, degeneracy, and
  battery identities; expected landing DISCLOSED per the closed-form-arm norm — REJECT
  at the drafter's exact G ≈ 8.6513 with k\* = 15 (odd at every computed cell) and
  e(0) = 9/58 vs e(15) ≈ 0.0332, the sim re-derives from scratch) · sim-ready; homed
  here per the `check_sections.py` non-lane carve-out (roster-derived sections — no
  ad-hoc section; flagged in the file's placement note), promoted as PROPOSAL 064;
  origin: drafted this slice under standing ORDER 003 (rotation rule per ORDER 004
  rule 3)
- [`deferred-acceptance-proposer-advantage-2026-07-15.md`](deferred-acceptance-proposer-advantage-2026-07-15.md) — round-13
  COMPLETELY-UNRELATED-domain rotation head, the round-13 closer (standing ORDER 003
  continuous pipeline, rotation per ORDER 004 rule 3; domain: two-sided matching / the
  Gale–Shapley deferred-acceptance mechanism — the folk "stability pins the outcome,
  which side proposes is a tie-break" belief priced against the market-size-born
  ordinal advantage the proposing side captures, a THIRTEENTH fleet-external domain
  after P017's social choice, P024's congestion routing, P028's tournament seeding,
  P032's pattern races, P036's optimal stopping, P040's spatial self-organization,
  P044's queue-discipline, P048's stochastic ratchets, P052's occupancy & collection,
  P056's random incidence, P060's repeated-game reciprocity, and P064's information
  cascades — deliberately NON-adjacent to P064's observational-learning domain: no
  signals, no sequential inference, a one-shot cooperative mechanism): pre-registered
  fully-deterministic sim (Arm A = seedless EXHAUSTIVE exact-`fractions.Fraction`
  census at n = 1, 2, 3 (46,656 profiles at the n = 3 decision cell) computing the
  side-gap Δ, multiplicity f, conditional gaps, and the strategy-proofness-asymmetry
  counts; Arm B = independently-written enumerate-then-take-lattice-extremes twin,
  exact-equal on every number, plus the 16-profile n = 2 hand census; Arm R = seeded
  n = 4/5/6 growth traces REPORTING-ONLY, seeds 20261600–603, no statistical gate)
  measuring whether the folk claim "a stable matching is a stable matching, side is a
  tie-break" survives its own lattice — decision-cell (n = 3) side-advantage against
  registered bands (REJECT iff Δ ≥ 1/5 AND f ≥ 1/5 AND M_prop = 0 with M_recv ≥ 1/100,
  stated first / APPROVE iff Δ ≤ 1/20 AND f ≤ 1/20 / anything else = honest null naming
  the binding axis; INVALID controls gate on the GS/stability identities, three
  structure theorems (polarization, gap-localization, strategy-proofness asymmetry),
  census anchors, hand-world, common-preference degeneracy, and battery identities;
  expected landing DISCLOSED per the exact-arm norm — REJECT at the drafter's exact
  Δ = 7/27 with f = 131/486, the gap living ENTIRELY off the singleton set
  (Δ | unique = 0 exactly, Δ | multi = 126/131) and M_recv = 1/54 vs M_prop = 0, the
  sim re-derives from scratch) · sim-ready; homed here per the `check_sections.py`
  non-lane carve-out (roster-derived sections — no ad-hoc section; flagged in the
  file's placement note), promoted as PROPOSAL 068; origin: drafted this slice under
  standing ORDER 003 (rotation rule per ORDER 004 rule 3)
- [`noisy-reciprocity-tft-collapse-2026-07-14.md`](noisy-reciprocity-tft-collapse-2026-07-14.md) — round-11
  COMPLETELY-UNRELATED-domain rotation head, the round-11 closer (standing ORDER 003
  continuous pipeline, rotation per ORDER 004 rule 3; domain: repeated games & the
  evolution of cooperation / reciprocity under trembling-hand execution noise, an
  ELEVENTH fleet-external domain after P017's social choice, P024's congestion routing,
  P028's tournament seeding, P032's pattern races, P036's optimal stopping, P040's
  spatial self-organization, P044's queue-discipline, P048's stochastic ratchets,
  P052's occupancy & collection, and P056's random incidence; reopens P024's
  card-recorded dropped runner-up with the drop reason answered): pre-registered
  fully-deterministic sim (Arm A = seedless exact `fractions.Fraction` stationary
  solves of all 256 rule-pair 4-state chains per noise cell over the COMPLETE 16-rule
  deterministic memory-one field, ε ∈ {1/1000, 1/100, 1/20, 1/10} + the ε = 0 orbit
  leg and ε = 1/2 degeneracy control; Arm B = independently-written Cramer twin,
  exact-equal on every pair value; Arm R = seeded finite-horizon estimates
  REPORTING-ONLY, seeds 20261377–380, no statistical gate) measuring whether the
  Axelrod folk claim "Tit-for-Tat is the best strategy" survives the complete field
  and any execution noise — decision-cell gap score(WSLS) − score(TFT) against
  registered bands (REJECT iff gap ≥ 2/5 at ε = 1/100 AND v(TFT,TFT) = 9/4 exactly at
  every grid ε (the echo identity) AND rank(TFT) worse than rank(WSLS) grid-wide AND
  v(WSLS,WSLS) ≥ 14/5, stated first / APPROVE iff TFT ranks 1 at the decision cell /
  anything else = honest null naming the binding axis; INVALID controls gate on the
  field/solve, echo-theorem, closed-form-anchor, transpose, ε = 1/2 degeneracy, and
  battery identities; expected landing DISCLOSED per the closed-form-arm norm —
  REJECT at the drafter's exact gap ≈ 0.4915 with ranks TFT 10 / WSLS 5 at all four
  grid ε and the ε-independent 9/4 echo tax, the sim re-derives from scratch) ·
  sim-ready; homed here per the `check_sections.py` non-lane carve-out
  (roster-derived sections — no ad-hoc section; flagged in the file's placement
  note), promoted as PROPOSAL 060; origin: drafted this slice under standing
  ORDER 003 (rotation rule per ORDER 004 rule 3)
- [`backlog-low-water-signal-tuning-2026-07-13.md`](backlog-low-water-signal-tuning-2026-07-13.md) — fleet-backlogs
  rotation head (inbox ORDER 004 rule 3; harvest source: the websites backlog's
  captured "Backlog low-water signal in the heartbeat" bullet @ `e14bb15`, invented
  "~3" threshold + untested "routing latency beats idle wakes" claim): pre-registered
  hermetic reorder-point sim — signal threshold N ∈ {0(off),1,2,3,4,6} × arrival
  regimes (one anchored to the backlog's own four measured re-pin intervals, births
  {2,5,4,11} / consumptions {5,9,4,3}) × consumption p_c × routing latency L, dry-wake
  fraction vs alarm cost against registered APPROVE/REJECT/NULL bands (REJECT-a
  organic-suffices checked first; APPROVE pins threshold = grid-median N\* and tests
  the "~3"); verdict consumers: kit `backlog:` grammar-token decision, manager
  routing, websites bullet disposition, idea-engine as first adopter · sim-ready;
  promoted as PROPOSAL 019; origin: drafted this slice under ORDER 003 + ORDER 004
  rule 3 from the websites lane-backlog harvest
- [`review-queue-row-threshold-2026-07-13.md`](review-queue-row-threshold-2026-07-13.md) — round-6
  FLEET-BACKLOGS rotation head (standing ORDER 003, rotation per ORDER 004 rule 3;
  harvest source: the fleet-manager's own backlog, a FIFTH repo for this slot — the
  review-queue auto-append rule's decide-and-flag N = 50 row-trigger threshold, priced
  on its own two named failure axes as a pre-registered hermetic dual-arm policy grid:
  size-arm defect miss REL(N) vs drain utilization ρ(N) over 9 cells × 6 thresholds,
  exact closed-form Fractions + seeded event-driven MC, seeds 20261285–88) · sim-ready;
  promoted as PROPOSAL 037 (drafted control-only via PR #315 — this file is the
  disclosed idea-doc BACKFILL healing the outbox LINK gate; the P037 block stays the
  source of truth)
- [`spool-scale-go-no-go-margin-2026-07-13.md`](spool-scale-go-no-go-margin-2026-07-13.md) — round-7
  FLEET-BACKLOGS rotation head (standing ORDER 003, rotation per ORDER 004 rule 3;
  harvest source: curious-research @ `a9fd5fa`, a SIXTH repo for this slot, untapped
  by any prior proposal — the spool-weight-scale build's own unquantified "leave
  yourself margin" default and its unmeasured "your own measured empty weight beats
  the seeded table, every time" claim, priced as a pre-registered hermetic
  error-budget sim: go/no-go margin grid M ∈ {0..100} g × three tare-knowledge
  regimes (measured-own / seeded-brand-table / midpoint-guess control) at the cited
  ±5 g resolution, exact-enumeration decision arm + seeded confirmation arm, REJECT
  checked first, seeds 20261301–304) · sim-ready; promoted as PROPOSAL 041; origin:
  drafted this slice under ORDER 003 + ORDER 004 rule 3 from the curious-research
  backlog harvest (ORDER 004 rule 4 untouched — nothing builds makerbench)
- [`magnet-press-fit-band-2026-07-13.md`](magnet-press-fit-band-2026-07-13.md) — round-9
  FLEET-BACKLOGS rotation head (standing ORDER 003, rotation per ORDER 004 rule 3;
  harvest source: curious-research @ `a9fd5fa`, the slot's SECOND tap of that repo —
  a different, untapped project subtree from P041's spool-scale: the effector-mount
  magnet tool's shipped, never-printed `magnet_fit = 0.15` mm press-fit interference
  default ("0.10-0.20 = a firm press-fit on most printers"), priced against the same
  repo's tolerance-coin band semantics (Press/Snug/Loose per-side clearances, one
  pinned exemplar row) as a pre-registered hermetic dual-arm sim: fit grid
  F ∈ {0.05..0.30} mm × pinned integer-lattice printer population, exact-Fraction
  enumeration decision arm + seeded common-random-numbers MC validation, REJECT
  checked first then an INVALID controls gate, seeds 20261333–336; expected landing
  DISCLOSED per the closed-form-arm norm — REJECT at the drafter's exact
  FAIL(0.15) = 145/861 ≈ 0.168 > 1/10, the sim re-derives from scratch; the shipped
  remedy-direction doc/geometry inversion carried as a reporting-only flag) ·
  sim-ready; promoted as PROPOSAL 049; origin: drafted this slice under ORDER 003 +
  ORDER 004 rule 3 from the curious-research backlog harvest (ORDER 004 rule 4
  untouched — nothing builds makerbench)
- [`outbox-rollover-stub-saturation-2026-07-15.md`](outbox-rollover-stub-saturation-2026-07-15.md) — round-13
  FLEET-BACKLOGS rotation head, the round-13 OPENER (standing ORDER 003, rotation per
  ORDER 004 rule 3; harvest source: the fleet-manager's outbox rollover convention —
  the slot's SECOND tap of that repo after P037's review-queue threshold, disclosed,
  zero shared fixtures — quoted verbatim in THIS repo's own `control/outbox.md`
  ROLLOVER 001 block ("200KB threshold · terminal-blocks-only · dated archive files ·
  mandatory pointer stubs · content-stable numbering") with every model constant
  measured from the live bus file at HEAD 256ea5c: 57 stubs mean 529.9 B, full blocks
  mean 16,212 B, receipt 1,002 B): pre-registered fully-deterministic sim (Arm A =
  seedless exact integer recurrence over the {T × s × b × W × policy} grid — committed
  per-block stubs vs range stub vs receipt-compacting range stub; Arm B =
  independently-written literal byte-ledger twin, exact-equal on every number; Arm R =
  seeded block-size-mix traces REPORTING-ONLY, seeds 20261567–570, no statistical
  gate) measuring whether the folk claim "a threshold-triggered archive roll keeps the
  live file bounded" survives its own tombstone arithmetic — decision-cell saturation
  wall against registered bands (REJECT iff N\* ≤ 300 AND ≥ 8 thrash rolls at
  spacing ≤ 2 AND the range-stub fix ≤ 4× while the receipt-compacting policy holds a
  constant floor over 100,000 appends, stated first / APPROVE iff N\* ≥ 500 with all
  first-20 spacings ≥ 4 / anything else = honest null naming the binding axis; INVALID
  controls gate on the floor-law/timing-invariance, receipt-free-invariance
  (N\* = ceil((T − H0)/s) = 386, b-independent), compact-boundedness (floor 34,030
  exact), closed-form-anchor, hand-world, degeneracy, and battery identities; expected
  landing DISCLOSED per the closed-form-arm norm — REJECT at the drafter's exact
  N\* = 233 with collapse at roll 34, wall composition 59.4% stubs / 24.8% roll
  receipts / 15.5% pending window, and the obvious range-stub fix at only 2.88×, the
  sim re-derives from scratch) · sim-ready; homed here per the `check_sections.py`
  non-lane carve-out (roster-derived sections — no ad-hoc section; flagged in the
  file's placement note), promoted as PROPOSAL 065; origin: drafted this slice under
  standing ORDER 003 (rotation rule per ORDER 004 rule 3) from the committed rollover
  convention's own first execution here (ORDER 010)
- [`wip-cap-dryness-floor-2026-07-15.md`](wip-cap-dryness-floor-2026-07-15.md) — round-14
  FLEET-BACKLOGS rotation head, the round-14 OPENER (standing ORDER 003, rotation per
  ORDER 004 rule 3; harvest source: THIS SEAT'S OWN COMMITTED BUS — the slot's first
  tap of the seat's own ORDER text and append cadence, disclosed against P065's
  byte-size tap of the same bus, zero shared fixtures — the owner's committed pair
  "WIP cap 3, backpressure holds" (ORDER 004, inbox:50) vs "the PROPOSAL→VERDICT
  pipeline is never dry" (ORDER 003 done-when, inbox:31), with TWO lived DRY events
  already committed (ORDER 012 "no unverdicted proposal exists", ORDER 014 "pipeline
  DRY at P063 → V074"), every cadence constant measured from the committed
  `## PROPOSAL 0NN ·` headers at HEAD dc155cb: burst gaps 1622/2674/2263/1387 s
  (S_d = 3973/2 s), the one echoed verdict pair S_v = 2246 s, r̂ = 4492/3973):
  pre-registered fully-deterministic sim (Arm A = seedless exact
  `fractions.Fraction` truncated-geometric closed forms on the closed 2-station
  cyclic loop, K ∈ {1, 2, 3, 4, 6, 12} × r ∈ {1/2, 3/4, 1, r̂, r₂, 2}, decision cell
  (K = 3, r̂); Arm B = independently-written Fraction Gaussian-elimination
  stationary-solve twin, exact-equal on every number; Arm R = seeded service-shape
  traces REPORTING-ONLY, seeds 20261610–613, no statistical gate) measuring whether
  the committed pair coheres — dry fraction D and backpressure fraction B against
  registered bands (REJECT iff D(3, r̂) ≥ 1/10 AND D(3, r) ≥ 1/20 grid-wide AND
  D(12, r̂) ≥ 1/40 AND B(3, r̂) ≥ 1/5, stated first / APPROVE iff D ≤ 1/50 AND
  B ≤ 1/20 / anything else = honest null naming the binding axis; INVALID controls
  gate on the chain/flow identities, three structure theorems (never-dry
  impossibility, max(0, 1 − r) frontier, balanced knee), census anchors, hand
  worlds, swap symmetry, and battery identities; expected landing DISCLOSED per the
  exact-arm norm — REJECT at the drafter's exact D(3, r̂) = 62712728317/304425042745
  ≈ 0.206 and B ≈ 0.298, with the deterministic-service exhibit D_det(3, r̂) = 0
  exactly pinning the tax as variance-born, the sim re-derives from scratch) ·
  sim-ready; promoted as PROPOSAL 069; origin: drafted this slice under standing
  ORDER 003 (rotation rule per ORDER 004 rule 3) from the seat's own committed
  cap/floor order pair
- [`pooled-screening-prevalence-wall-2026-07-15.md`](pooled-screening-prevalence-wall-2026-07-15.md) — round-14
  COMPLETELY-UNRELATED-domain rotation head, the round-14 closer (standing ORDER 003
  continuous pipeline, rotation per ORDER 004 rule 3; domain: screening design /
  combinatorial group testing — Dorfman two-stage pooled testing, the folk "batching
  always saves, and small pools are the safe hedge" belief priced against the exact
  two-stage cost law T(n, p) = 1/n + 1 − (1 − p)^n, a FOURTEENTH fleet-external
  domain after P017's social choice, P024's congestion routing, P028's tournament
  seeding, P032's pattern races, P036's optimal stopping, P040's spatial
  self-organization, P044's queue-discipline, P048's stochastic ratchets, P052's
  occupancy & collection, P056's random incidence, P060's repeated-game reciprocity,
  P064's information cascades, and P068's two-sided matching — deliberately
  NON-adjacent to both P064's observational learning (no signals, no inference, no
  herd) and P068's matching (no sides, no preferences, no market): a one-shot
  test-economy design against prevalence): pre-registered fully-deterministic sim
  (Arm A = seedless exact `fractions.Fraction` cost surface over a 12 × 64 grid +
  INTEGER-POWER wall certificates (3² > 2³, 3⁴ > 4³, 3⁵ > 5³, 2⁴ = 4²,
  (n+1)^n < n^(n+1) for n ≥ 3 ⇒ the wall p\* = 1 − 3^(−1/3) ≈ 0.3066 above which
  EVERY pool size strictly loses) + two exact polynomial dominance identities as
  theorem gates (T(2,q) − T(3,q) = (q − 2/3)²(q + 1/3) + 1/54 — the pair-pool never
  optimal, floor attained exactly at q = 2/3; T(2,q) − T(4,q) = (q² − 1/2)² — pools
  2 and 4 tie exactly at their common break-even, a registered margin-0 knife-edge);
  Arm B = independently-written outcome-tree twin, exact-equal on every number;
  Arm R = seeded screening careers REPORTING-ONLY, seeds 20261640–643 with aux
  20261643 never read, no statistical gate) measuring the batching folk belief
  against registered bands (REJECT iff the strict wall clause + practical damage
  ≥ 21/20 at p = 2/5 AND the 1/54 dominance floor AND savings T\* ≤ 1/4 at
  p = 1/100, stated first / APPROVE iff pooling still helps at p = 2/5 or the pair
  beats the triple somewhere / anything else = honest null naming the binding
  axis; INVALID controls gate on model identities, the three theorems, nine census
  anchors, the p = 1/2 pencil world, degeneracy controls, and battery identities;
  expected landing DISCLOSED per the exact-arm norm — REJECT with margins ×1.0641 /
  ×1.00-at-the-named-knife-edge / ×1.2783, the free-pool-test one-term APPROVE
  world and the p = 3/10 straddle edge both named, the sim re-derives from
  scratch) · sim-ready; promoted as PROPOSAL 072; origin: drafted this slice under
  standing ORDER 003 (rotation rule per ORDER 004 rule 3) as the round-14
  unrelated-slot closer
- [`check-digit-transposition-floor-2026-07-15.md`](check-digit-transposition-floor-2026-07-15.md) — round-15
  COMPLETELY-UNRELATED-domain rotation head, the round-15 closer (standing ORDER 003
  continuous pipeline, rotation per ORDER 004 rule 3; domain: algebraic error
  detection — check-digit design over decimal identifiers (Luhn / weighted mod-10 /
  ISBN-10 mod-11 / the Damm quasigroup), the folk "any standard check digit catches
  the typos that matter, and newer standards are stronger" belief priced against
  three exact structure facts, a FIFTEENTH fleet-external domain after P017's social
  choice, P024's congestion routing, P028's tournament seeding, P032's pattern races,
  P036's optimal stopping, P040's spatial self-organization, P044's queue-discipline,
  P048's stochastic ratchets, P052's occupancy & collection, P056's random incidence,
  P060's repeated-game reciprocity, P064's information cascades, P068's two-sided
  matching, and P072's group testing — deliberately NON-adjacent to the last three:
  no signals or inference (vs P064), no sides or preferences (vs P068), no
  probability, prevalence, or subset queries (vs P072's stochastic screening economy
  — this head is deterministic algebra on a single codeword)): pre-registered
  fully-deterministic sim — Arm A = the COMPLETE 3,628,800-cell quotient-space
  census (transposition floor = exactly 2 ordered pairs per boundary, excluded from
  0 by the one-line certificate Στ ≡ 0 ≠ 5 ≡ Σperm mod 10, attained by 46,400
  quotients with Luhn among them at precisely {09↔90}) + the 16-cell all-singles
  linear grid ({4 diagonal → 90, 12 off-diagonal → 10} — units mod 10 are all odd,
  so |a−b| = 5 escapes every linear boundary) + the migration-regression censuses
  (ISBN-10 mod-11: 0 undetected at EVERY distance; EAN-13 alternating 1,3: 10/90
  per adjacent boundary + 90/90 at distance 2 = 120 + 990 escape patterns over the
  full code) + the two priced exits (11th symbol, or the pinned Damm quasigroup
  table verified rows/columns/diagonal with 0/900 state censuses on the same ten
  digits); Arm B = independently-written full word-level enumerations at length 4,
  exact-equal through FOUR typed must-equal contacts (60 = 3×2×10 · 300 = 3×10×10 ·
  1800 = 2×90×10 · 0 = 0, the ordered-pair multiplicity law asserted directly — the
  drafter's own first hand derivation got the unordered counts and the enumeration
  corrected it, disclosed + pre-registered as a NULL axis); Arm R = seeded
  identifier careers REPORTING-ONLY, seeds 20261680–683 with aux 20261683 never
  read, no statistical gate) measuring the check-digit folk belief against
  registered bands (REJECT iff floor = 2 with Luhn optimal AND the ISBN→EAN strict
  regression AND both exits verified, stated first / APPROVE iff some quotient hits
  U = 0 or EAN's censuses are clean / anything else = honest null naming the
  binding axis; INVALID controls gate on model identities, the three theorems,
  twelve census anchors, three pencil worlds, degeneracy controls, and battery
  identities; expected landing DISCLOSED per the exact-arm norm — REJECT on all
  three conjuncts at the drafter's enumerated values, the eleventh-symbol and
  non-abelian falsifiability worlds both named, the sim re-derives from scratch) ·
  sim-ready; promoted as PROPOSAL 076; origin: drafted this slice under standing
  ORDER 003 (rotation rule per ORDER 004 rule 3) as the round-15 unrelated-slot
  closer
- [`verdict-registry-2026-07-11.md`](verdict-registry-2026-07-11.md) — hermetic
  `## Sim verdict` note lint against a pinned field set + PROPOSAL↔VERDICT cross checked
  vs the local outbox (registry FILE judged overkill — the notes + the local outbox ARE
  the registry; sim-lab grammar half routed via the manager) · park(built-here —
  SIM-VERDICT category in `scripts/check_ideas.py`, probed + built in the same PR);
  origin: V005 fan-in card 💡, armed by V006's ruling-field drift (PR #121)
- [`cycle-following-coupling-lever-2026-07-16.md`](cycle-following-coupling-lever-2026-07-16.md) — round-16
  COMPLETELY-UNRELATED-domain rotation head, the round-16 closer (standing ORDER 003
  continuous pipeline, deliberate lane rotation rule 3; domain: correlation design
  under shared randomness — the joint-vs-marginal gap of success events coupled
  through one random permutation's cycle skeleton (coordinated search / the
  cycle-following pointer strategy), the folk "marginals multiply into the joint;
  a strategy that moves no marginal cannot move the group" belief priced where it
  exactly breaks, a SIXTEENTH fleet-external domain after P017's social choice,
  P024's congestion routing, P028's tournament seeding, P032's pattern races,
  P036's optimal stopping, P040's spatial self-organization, P044's
  queue-discipline, P048's stochastic ratchets, P052's occupancy & collection,
  P056's random incidence, P060's repeated-game reciprocity, P064's information
  cascades, P068's two-sided matching, P072's group testing, and P076's algebraic
  error detection — deliberately NON-adjacent to the last three: no sides or
  preferences (vs P068), no prevalence prior or pooled tests (vs P072), no codes
  or check algebra (vs P076 — permutations there are pinned CHECK MAPS, here the
  random OBJECT)): pre-registered exact sim — Arm A = the harmonic law
  (joint pointer success = 1 − Σ_{k=b+1}^{m} 1/k exactly for b ≥ n; headline
  P₅₀ ≈ 0.3118278207 vs the independent pole exactly 2⁻¹⁰⁰ — a 3.953 × 10²⁹ lift —
  and the same-set pole exactly 0) + marginal invariance (a fixed element's cycle
  length is uniform, so every player stays exactly at b/m — the lift is pure
  dependence) + failure concentration (E[# failing | joint failure] = 50/T₅₀ ≈
  72.6562 of 100) + the certified 1 − ln 2 floor (gap ≈ 0.0049750) + the
  adversary/repair pair (relabeling is a conjugation NO-OP, {720, 0, 720}; the
  one-sided remap π∘σ restores exactly 276/720 against every pinned arrangement);
  Arm B = independently-written brute enumerations (m ∈ {4, 6, 8}: censuses
  10/276/14,736) + the cycle-type partition census (1,285,920 = 10!·893/2520),
  exact-equal through FOUR typed must-equal contacts incl. the below-budget
  inclusion-exclusion corrections (632,736 = 560,160 + 10!/50 · 5,916 = naive +
  8!/32 — the harmonic shortcut is genuinely FALSE below b = n, registered as its
  own live NULL axis); Arm R = seeded episode traces REPORTING-ONLY, seeds
  20261714–717 with aux 20261717 never read, 99N draw-count sentinel, no
  statistical gate) measuring the independence folk belief against registered
  bands (REJECT iff lever AND marginal invariance AND concentration/floor AND
  both repair censuses, stated first / APPROVE iff the pointer census equals the
  2⁻ᵐ product census or a marginal moves off b/m / anything else = honest null
  naming the binding axis; expected landing DISCLOSED per the exact-arm norm —
  REJECT on all four conjuncts at the drafter's enumerated values, the
  marginal-mover / composition / shortcut falsifiability worlds all named, the
  sim re-derives from scratch) · sim-ready; promoted as PROPOSAL 080; origin:
  drafted this slice under standing ORDER 003 (deliberate lane rotation, rule 3)
  as the round-16 unrelated-slot closer
