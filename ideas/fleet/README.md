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
