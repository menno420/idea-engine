# Session — fleet slice: open-work preflight sweep (the PR #40 card's 💡)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-10 ~23:35Z (worker slice, dispatched by the
> continuous-mode coordinator per Q-0265)

## Scope

Build the PR #40 probe card's 💡 ("idea-engine should adopt the open-work sweep
itself"): capture `ideas/fleet/open-work-preflight-sweep-2026-07-10.md`, probe it
(battery v0), and — if the verdict earns the README same-PR shortcut — add a SIXTH
report-only `CHECKS` entry to `scripts/preflight.py` (`--open-work`, gate-wiring
self-invoke pattern) listing open remote branches besides main plus uncommitted
local state as wake/pre-push ADVISORIES that never affect the exit code. No outbox
append expected (repo-internal PROCESS tooling; verdict expected park(built-here)).

## What this session did

- Claimed the surface (`claims/build-open-work-preflight-sweep.md`, flat filename per
  `claims/README.md`; cleared in this close-out commit).
- **Captured + probed** `ideas/fleet/open-work-preflight-sweep-2026-07-10.md` —
  battery v0, verdict **park(built-here — scripts/preflight.py --open-work,
  report-only sibling-branch + local-dirt advisory sweep, shipped in this PR)**;
  state advanced forward-only `probed → historical(#42)` in this close-out. Origin
  chain: the websites open-pr-awareness probe (PR #40, park(build-direct)) ruled
  each repo builds its OWN ritual step — websites gets a doc edit, substrate-kit
  gets the planted convention; this is idea-engine's instance, and here "one ritual
  step" means "one `CHECKS` entry" because this repo's ritual carrier is
  `scripts/preflight.py` (PR #16), which CI also runs (PR #18).
- **Built the sweep:** `check_open_work()` in `scripts/preflight.py` + sixth
  `CHECKS` entry (`open-work advisory (report-only, never gates)`), self-invoked as
  `preflight.py --open-work` per the `--gate-wiring` pattern so the worst-exit loop
  is untouched. Two legs, both stdlib + git transport only: `git ls-remote --heads
  origin` (every head except main, printed with short sha) and `git status
  --porcelain` (uncommitted local paths). **Unconditionally `return 0`** — findings,
  empty findings, timeout, dead network all PASS; failures degrade to a one-line
  "could not list … — advisory only, still PASS". This resolves the
  harvest-freshness probe's hermeticity rule (network checks must not red preflight)
  by exit semantics rather than by staying out: the check CANNOT contribute a
  nonzero exit, so CI stays hermetic by construction (probe Q4).
- **The idea's own mechanism, lived mid-slice:** the manual `ls-remote` at branch
  time (23:32Z) showed sibling `groom/sim-verdicts-001-004` in flight; it landed as
  PR #41 (sim-verdict fan-in, heartbeat + README touched) mid-slice and was
  forward-merged into this branch per the README recipe (`def3683`, no conflicts —
  this branch had not yet touched `control/status.md`). The sweep this slice ships
  is exactly the ritualization of that saving ad-hoc read.
- **No outbox append, no proposal** — verdict is park(built-here); nothing routes to
  sim-lab (the class's one open question, per-seat PR-tooling variance, is already
  INTAKE 005 there). Earn-rate bar held.

### Live green run (real output, this branch, post-build)

```
$ python3 scripts/preflight.py
check_sections: OK — 10 sections in sync with the manifest
preflight: PASS — check_sections (exit 0)
check_ideas: OK — 281 idea files conform to the README grammar
preflight: PASS — check_ideas (exit 0)
check_ideas: OK — outbox proposals and sim-ready ideas are consistent
preflight: PASS — check_ideas --outbox (exit 0)
check: control-status check passed (--status-only).
preflight: PASS — bootstrap check --strict --status-only (exit 0)
gate-wiring: OK — .github/workflows/substrate-gate.yml non-control lane runs scripts/preflight.py
preflight: PASS — gate-wiring self-check (exit 0)
open-work: no open remote branches besides main
open-work: 2 uncommitted local path(s) (advisory):
open-work:    M scripts/preflight.py
open-work:   ?? ideas/fleet/open-work-preflight-sweep-2026-07-10.md
open-work: OK — advisory sweep complete (report-only, never affects the exit)
preflight: PASS — open-work advisory (report-only, never gates) (exit 0)
preflight: OK — all 6 checks green
(exit 0)
```

### Smoke demo — Q8's own test, real output post-push (the sweep lists its own branch)

```
$ python3 scripts/preflight.py --open-work
open-work: 1 open remote branch(es) besides main (advisory — a sibling may be in flight; merge forward-only, never rebase):
open-work:   b6447c1c7  build/open-work-preflight-sweep
open-work: working tree clean
open-work: OK — advisory sweep complete (report-only, never affects the exit)
(exit 0)
```

### Smoke test — graceful failure (origin temporarily renamed away, then restored)

```
$ python3 scripts/preflight.py --open-work
open-work: could not list remote branches (fatal: 'origin' does not appear to be a git repository) — advisory only, still PASS
open-work: 2 uncommitted local path(s) (advisory):
open-work:    M scripts/preflight.py
open-work:   ?? ideas/fleet/open-work-preflight-sweep-2026-07-10.md
open-work: OK — advisory sweep complete (report-only, never affects the exit)
(exit 0)
```

Remote restored via `git remote rename`; healthy re-run green. NOTE (advisory-list
honesty): the sweep's "no open remote branches besides main" in the full run above
is itself a datapoint — `groom/sim-verdicts-001-004` had ALREADY merged (PR #41) and
been deleted between this slice's branch cut and that run; the live read tracked it
where a committed ledger would have gone stale, the exact class the websites probe
named.

- **📊 Model:** fable-5 · high · one capture+probe+build (sixth preflight check) +
  docs ceremony (no proposal — park(built-here) verdict)

## 💡 Session idea

**Merged-branch pruning ritual (advisory-fatigue guard).** The sweep prints every
non-main remote head at every wake forever — squash-merge leftovers and abandoned
branches will accumulate as permanent advisory noise (this repo deletes merged
branches today, so the list is currently honest; nothing ENFORCES that). A
one-line close-out convention ("delete the remote branch after merge verification")
plus, later, an open-work annotation for heads whose tip is already an ancestor of
origin/main (`git merge-base --is-ancestor` needs the ref fetched — a
`--fetch` deep mode, NOT day-0) would keep the advisory signal high. Anchors:
`check_open_work()` leg 1 in `scripts/preflight.py`; test = push a throwaway ref
whose tip is on main, confirm annotation.

## ⟲ Previous-session review

PR #41 (sim-verdict fan-in grooming; card `.sessions/2026-07-10-sim-verdicts-fanin.md`)
promised: README § The probe battery carries VERDICT 002's panel-escalation default
(single-pass default, escalate only on repeat-disagreement or high-blast-radius,
always-on rejected, measured costs cited); `## Sim verdict` notes appended to the
three touched superbot idea files with states untouched forward-only; VERDICT 003's
websites note explicitly DEFERRED (websites claim sibling-held at its branch time,
unblocked by PR #40's landing). Verified on this merged tree: README lines 78–88
carry the panel-default paragraph with the 4.00×/3.05×/1.61× measurements and the
PR #23 ≈127k-token live datapoint; all three `## Sim verdict` appends present
(wild-encounters, explore-hub-federated-world, idea-probe-brainstorm-simulator @
sim-lab `8713f26`); `ideas/websites/superbot-site-stats-data-story-2026-07-10.md`
indeed still carries NO sim-verdict note (the deferral was honest, first item for a
next slice); claims/ carried only README.md at this branch's cut. Its heartbeat
last-shipped reads "this slice" (the honest-stamp rule) — updated to #41 by this
slice's overwrite. All checks out; nothing contradicted.

## Handoff → next wake

Nothing to babysit: claim cleared, no proposal in flight, the sweep is live in both
the wake ritual and CI (gate runs the same wrapper) from merge on. From now on every
wake sees sibling branches WITHOUT the remembered ad-hoc `ls-remote` — read its
advisory lines before claiming work; merge forward-only when a sibling is in
flight. Ripest next: the DEFERRED VERDICT 003 websites note (one-file append on
`ideas/websites/superbot-site-stats-data-story-2026-07-10.md` — ruling + pin on the
PR #41 card), websites next probe heads (own-heartbeat parse self-check,
review-queue row auto-check), public-leaderboards probe, check_harvest
output-refinement bundle, grooming round 3 (freshest-wins + post-verdict
state-grammar gap), this card's 💡 (merged-branch pruning / ancestor annotation).
