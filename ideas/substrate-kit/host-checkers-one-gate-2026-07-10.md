# Host checkers under the one gate — config-registered extra checks in `check --strict`

> **State:** captured
> **Class:** product · **Target:** `menno420/substrate-kit`

## Problem

The kit's doctrine is one gate: every checker "all under one `check --strict`"
(kit README § Checkers), and the planted `substrate-gate.yml` runs exactly that
command in CI. But adopters grow **local** checkers the kit never sees: this repo
runs a three-command preflight beside the kit's (`scripts/check_sections.py` +
`scripts/check_ideas.py` + `check_ideas.py --outbox`) that exists only as session
ritual — the substrate-gate never runs any of it, so a PR that drifts the section
tree or breaks the idea grammar merges GREEN if the session forgets the ritual. And
the host cannot fix this by editing the gate: since the §6.1 change the workflow is
KIT-OWNED — "hand edits are OVERWRITTEN" on upgrade, carve-outs belong in a separate
workflow file. So every adopter with local checkers must either maintain a parallel
CI workflow or accept unenforced rules — both against the kit's own one-gate
doctrine.

## Idea

Let `substrate.config.json` register host checkers — e.g.
`"extra_checks": [{"cmd": ["python3", "scripts/check_ideas.py"], "strict": true}]`
— which `cmd_check` runs after its own suite, folding exit codes into the one
verdict. The kit-owned gate then enforces host rules with zero gate edits, upgrades
keep working (config is host-owned, workflow is kit-owned — the seam is already
drawn), and a session's preflight collapses back to the single documented command.
Precedent inside the kit itself: the §6.3 adopters format gate was "wired into
`cmd_check` like the existing checkers" — this generalizes that wiring from
kit-authored to host-registered. Guardrails: declared commands must live in the
repo tree, run with no network expectations, and `check` should print each extra
checker's name so a red is attributable.

## Grounding

- One-gate doctrine + checker list: kit README § Checkers @
  [`7e600c6`](https://raw.githubusercontent.com/menno420/substrate-kit/7e600c6f4b9e0e685d7d5a11aed37d435d009dae/README.md);
  the "wired into `cmd_check` like the existing checkers" precedent @
  [`7e600c6`](https://raw.githubusercontent.com/menno420/substrate-kit/7e600c6f4b9e0e685d7d5a11aed37d435d009dae/control/status.md)
  (last-shipped, §6.3).
- KIT-OWNED gate, hand edits overwritten, carve-outs → separate workflow: this
  repo's installed `.github/workflows/substrate-gate.yml` header (v1.7.0 plant) +
  the CHANGELOG [Unreleased] §6.1 entry @
  [`7e600c6`](https://raw.githubusercontent.com/menno420/substrate-kit/7e600c6f4b9e0e685d7d5a11aed37d435d009dae/CHANGELOG.md).
- The live unenforced-ritual case: `menno420/idea-engine` — `scripts/` checkers +
  the three-command preflight recorded across PR #11/#13 session cards and the
  20:55Z heartbeat's wake-preflight note; `substrate.config.json` has no field to
  declare them.

**Why now:** this repo just grew its third local checker mode in one day (PR #13's
`--outbox`) and the wake-preflight-wiring candidate is already on the heartbeat's
ripest-next list — a config seam in the kit is the version of that fix every
adopter inherits, not just this lane.
