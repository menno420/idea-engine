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
- [`verdict-registry-2026-07-11.md`](verdict-registry-2026-07-11.md) — hermetic
  `## Sim verdict` note lint against a pinned field set + PROPOSAL↔VERDICT cross checked
  vs the local outbox (registry FILE judged overkill — the notes + the local outbox ARE
  the registry; sim-lab grammar half routed via the manager) · park(built-here —
  SIM-VERDICT category in `scripts/check_ideas.py`, probed + built in the same PR);
  origin: V005 fan-in card 💡, armed by V006's ruling-field drift (PR #121)
