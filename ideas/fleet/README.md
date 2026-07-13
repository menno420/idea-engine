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
- [`verdict-registry-2026-07-11.md`](verdict-registry-2026-07-11.md) — hermetic
  `## Sim verdict` note lint against a pinned field set + PROPOSAL↔VERDICT cross checked
  vs the local outbox (registry FILE judged overkill — the notes + the local outbox ARE
  the registry; sim-lab grammar half routed via the manager) · park(built-here —
  SIM-VERDICT category in `scripts/check_ideas.py`, probed + built in the same PR);
  origin: V005 fan-in card 💡, armed by V006's ruling-field drift (PR #121)
