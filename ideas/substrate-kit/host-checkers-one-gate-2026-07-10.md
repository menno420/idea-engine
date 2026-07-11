# Host checkers under the one gate — config-registered extra checks in `check --strict`

> **State:** parked(routed — substrate-kit lane build, LAYER-CORRECTED: the seam lands in the gate GENERATOR — a host-owned config key the kit-owned workflow template renders as a named non-control-lane step — NOT in `cmd_check` subprocess execution (the capture's named mechanism collides with the kit's §3.2 no-shell-out check invariant); joins the kit fan-in bundle as its SIXTH head, consolidating with the enabler-guard head's already-routed "gate-preflight config seam" item; verified un-adopted at live kit HEAD `489e763` — see probe report)
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

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/substrate-kit/489e7632aee1379482614264a180cb6709c8d9a7/src/engine/cli.py@489e763 · fetched 2026-07-11T08:31Z
> **Grounding:** https://raw.githubusercontent.com/menno420/substrate-kit/489e7632aee1379482614264a180cb6709c8d9a7/src/engine/lib/config.py@489e763 · fetched 2026-07-11T08:31Z

Single-pass battery v0 (no panel trigger: not contested, not
high-blast-radius — a routing decision over a docs-only diff). This is the
section's LAST captured head.

*Verify-first at live kit HEAD `489e763` (blobless clone 2026-07-11T08:30Z;
HEAD committed 08:28:59Z — the kit moved DURING this session's read window,
`be72c09` → `489e763`, and the delta is the v1.10.1 payload merge `0499625`
"gate tail-1 multi-card shadowing fix + doctrine emphasis normalization" plus
its release claim — session-card grading + doctrine phrase matching, disjoint
from any host-checker surface). NOT overtaken kit-side: newest tag is
**v1.10.0 — no v1.10.1 tag yet, no v1.11.0**; `[Unreleased]` carries only the
tail-1 payload. **No `extra_checks` seam exists** — and the near-named symbol
is a false friend that a naive grep confirms wrong: `_extra_check_findings`
(`src/engine/cli.py:606` @ `489e763`; dist `bootstrap.py:12932`) is an
internal helper running the kit's OWN non-doc checkers (ledger, namespace,
seams, orientation budget, engagement), zero host-command execution anywhere
in `cmd_check`. The config schema is CLOSED against the capture's key:
`Config` (`src/engine/lib/config.py:150–260`) declares no
`extra_checks`/`host_checks` field, and `Config.from_dict` **drops unknown
keys** — the kit's own `kit_version` field comment says it verbatim: "a bare
JSON key would be stripped on the next load→save round-trip" — so a host
cannot even pre-adopt the key speculatively. Host-side, the capture's premise
MUTATED but the gap is INTACT: the "three-command preflight that exists only
as session ritual" is history — PR #18 hand-added the wake-preflight step
into the KIT-OWNED gate's non-control lane, and `scripts/preflight.py` now
runs EIGHT checks (three content checkers + the gate-wiring self-check +
three report-only advisories + the kit's `--status-only` leg) — but that
wiring survives ONLY as a re-apply duty on a file whose header says "hand
edits are OVERWRITTEN": dropped live by the PR #35 upgrade regen, re-applied
by hand on every hop since (#35/#54/#55, then the v1.9.0 and v1.10.0
upgrades), tripwired by `preflight --gate-wiring` (PR #36). And the residual
class the capture names is alive: `scripts/check_harvest.py` (569 lines) is
wired NOWHERE — not in `preflight.py::CHECKS`, not in the gate — exactly the
"silently falls back to session discipline" failure preflight's own header
comment warns about.*

**1. What is this really?** A seam-drawing move, not a checker: relocate the
host↔kit CI wiring from a hand edit on a KIT-OWNED file (the PR #18 step,
clobbered by every regen) to a HOST-OWNED declaration the kit consumes — the
one-gate doctrine ("every checker, one gate" — kit README, verbatim at
`489e763`) extended across the host boundary. It is the archetype of the
fan-in family already routed to this lane: host truth declared in
`substrate.config.json`, kit machinery honors it (carveout-needles declares
byte-needles; this declares checkers).

**2. What is the possibility space?** Ascending: (i) kit DOCUMENTS the
wrapper pattern (docs-only — zero code, but leaves the clobber debt exactly
where it is: the wiring still lives as a hand edit the next regen drops);
(ii) TEMPLATE-layer seam — the gate generator (`live_ci_workflow`,
`src/engine/adopt.py:1615`, already parameterized by
`config.interpreter_for_checks`) reads a host-owned config key (e.g.
`gate_host_checks: [{name, cmd}]`) and EMITS one named step per entry into
the generated workflow's non-control lane — regen re-derives the wiring from
host-owned config, so upgrades cannot drop it by construction; (iii)
ENGINE-layer seam as captured — `cmd_check` executes registered commands and
folds exit codes into the one verdict; (iv) both. Negative space: a separate
host workflow (the gate header's own advice) works but forfeits the
one-required-context property — a second required check is an owner-settings
ask per repo, an unrequired one is advisory by construction; and the status
quo re-apply duty, measurably a treadmill (five catches and counting).

**3. What is the most advanced capability reachable by the simplest
implementation?** Option (ii): one declared config field + a few template
lines in the generator + a regen smoke test. Every adopter's local checkers
become CI-enforced with zero gate hand-edits and the wiring SURVIVES every
upgrade; idea-engine's PR #18 step becomes generated output (retiring the
re-apply duty and, after one clean upgrade cycle, the gate-wiring tripwire's
reason to exist); and the kit's OWN captured backlog head
`docs/ideas/adopt-plants-pytest-gate-step-2026-07-10.md` @ `489e763` (origin:
superbot-games #16, a lane that "lived its whole gen-1 life with a
tests-blind gate") collapses into ONE DEFAULT ENTRY of the generalized key
(`tests/` exists → a pytest entry) instead of a bespoke template branch. The
job's exit code is already the fold — one red step reds the one required
context — so the "one verdict" property costs nothing.

**4. What breaks it?** (a) **The captured mechanism breaks the kit's own
invariant:** engine check code is pure-stdlib/no-subprocess by design — §3.2,
stated verbatim at `check_setup_script.py:38` ("Pure stdlib, no
``subprocess`` (§3.2)") and `adopt.py:690` ("the engine never shells out
(§3.2)"; CI extracts git blobs in bash for exactly this reason). An
`extra_checks` executor inside `cmd_check` would also run host commands in
every OTHER `check` context — Stop-hook advisories, session rituals,
`--status-only` fast lanes — where a slow or crashing host command is a new
failure class. The template layer delivers the same one-verdict property
without touching any of that; this probe corrects the capture's layer. (b)
**Closed config schema:** the key must be a DECLARED dataclass field
(`from_dict` drops unknowns), so this is a kit MINOR release + upgrade hop,
never a host-side patch. (c) **Untrusted-input surface:** the key makes
host-config-declared commands run in CI — no NEW trust inside one repo (CI
already executes repo code; the PR #18 hand edit does today what the key
would declare), but the capture's guardrails become requirements: commands
must resolve inside the repo tree, each step named so a red is attributable,
and the generator must emit them ONLY into the non-control lane (the fast
lane's control-only short-circuit stays untouched — heartbeat PRs never pay
host checkers). (d) **Routing overlap, the honest catch:** the sibling head
`enabler-card-status-guard-upstream-2026-07-11.md` was ALREADY scope-sharpened
to include "a config seam so hosts declare the gate's wake-preflight step
instead of hand-editing" (its Idea (b)) — this head is the generalized full
statement of that same landing zone (N declared checks, not one step), so the
bundle must consolidate them as ONE build item with two statements, or the
kit lane builds the seam twice.

**5. What does it unlock?** The re-apply-duty family dies at its root for the
gate: the PR #18 step becomes config-derived output, the gate-wiring tripwire
demotes to a regen smoke, the carve-out scan has one less host edit to bank
(shrinking what carveout-needles must cover), and `check_harvest`-class
orphans get a one-line declaration path instead of waiting for a wrapper
edit. Fleet-wide: superbot-games' tests-blind-gate class (the kit's own
backlog evidence) closes for every adopter at their next upgrade, and the
session story the capture wanted returns — the documented preflight command
and the CI gate provably run the SAME list, because both are derived from the
same host-owned declaration.

**6. What does it depend on?** A substrate-kit release (declared config
field + generator change + dist byte-pin — MINOR per the kit's own semver
key: "new capability (new checker, new command, new template)"), then each
adopter's upgrade hop to inherit the new template; per-host migration
(idea-engine: declare `scripts/preflight.py` in the key, verify the regen
carries the step, THEN drop the hand-edit and demote the tripwire —
observe-before-block, the enabler-anchors precedent); the non-control-lane
guard already present in the template (`steps.lane.outputs.control_only !=
'true'`) as the hook point. Nothing sim-shaped: a generated workflow step is
proven by its own red/green (the #114 precedent, three times reaffirmed on
this section).

**7. Which lane should build it?** substrate-kit, definitionally: the
generator (`live_ci_workflow`), the config schema, and the planted template
are all kit-owned, and the host CANNOT build this — the gate file's own
header routes hand edits to oblivion on every regen; the five-catch re-apply
history is the measured proof. idea-engine stays the working reference
implementation and migration consumer #1 (its preflight wrapper + PR #18
step are the exact bytes the first generated entry must reproduce). Routing:
JOINS the kit fan-in bundle as its SIXTH head (carveout-needles-config +
enabler-card-status-guard-upstream(sharpened) + kit-line-self-drift +
parallel-session-heartbeat-reconcile + behind-stall-auto-updater(sharpened) +
this) — one manager ORDER carries all six, and within the bundle this head
CONSOLIDATES with the enabler-guard head's gate-preflight seam item (same
landing zone; build once).

**8. What is the smallest shippable slice?** One kit PR: a declared
`gate_host_checks`-shaped config field (empty default = today's template
bytes, byte-stability asserted by the regen smoke) + `live_ci_workflow`
emitting one named, non-control-lane step per entry + one rendered-output
test with a single entry; migration #1 rides idea-engine's next upgrade hop
(declare the preflight, watch the regen carry it, drop the hand edit). The
red/green reference already exists in this repo's history: the gate WITH the
hand-carried step (every merged PR since #18) vs the PR #35 regen that
silently dropped it — the recorded live red this seam makes structurally
impossible.

**Recommendation: park** — routed (substrate-kit lane build, joins the kit fan-in bundle as its SIXTH head): the gap is real and evidenced from BOTH sides (this repo's five-times-caught PR #18 re-apply treadmill + the kit's own tests-blind-gate backlog head), but the capture's mechanism is the wrong LAYER — build the seam in the gate GENERATOR (host-owned config key → generated non-control-lane step), not `cmd_check` subprocess execution (§3.2 no-shell-out); documenting the wrapper pattern alone was weighed and rejected as the fix — it leaves the clobber debt in place; no sim-lab proposal (no simulator question — a generated workflow step is proven by its own red/green, the #114 precedent).
