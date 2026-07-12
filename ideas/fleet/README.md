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
- [`verdict-registry-2026-07-11.md`](verdict-registry-2026-07-11.md) — hermetic
  `## Sim verdict` note lint against a pinned field set + PROPOSAL↔VERDICT cross checked
  vs the local outbox (registry FILE judged overkill — the notes + the local outbox ARE
  the registry; sim-lab grammar half routed via the manager) · park(built-here —
  SIM-VERDICT category in `scripts/check_ideas.py`, probed + built in the same PR);
  origin: V005 fan-in card 💡, armed by V006's ruling-field drift (PR #121)
