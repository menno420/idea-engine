# Open-work preflight sweep — sibling branches + local dirt as wake/pre-push advisories

> **State:** probed
> **Class:** process · **Target:** `menno420/idea-engine` (this repo's own preflight — built here, see report Q7)

**Origin:** the PR #40 session card 💡 (`.sessions/2026-07-10-probe-open-pr-awareness.md`
§ 💡, "idea-engine should adopt the open-work sweep itself") — that probe session
discovered sibling PR #38 only via an ad-hoc `git ls-remote`, the exact ad-hoc move the
idea it was probing wants ritualized. The parked class
(`ideas/websites/open-pr-awareness-at-wake-2026-07-10.md`, verdict park(build-direct))
says each repo builds its OWN ritual step — websites gets a wake-ritual doc edit,
substrate-kit gets the planted-`control/README.md` convention — and this file is
idea-engine's instance, scoped to what this repo already runs at every wake and every
pre-push: `scripts/preflight.py`.

**The idea:** a sixth, REPORT-ONLY `CHECKS` entry — `preflight.py --open-work` (the
`--gate-wiring` self-invoke pattern) — that lists (a) open remote branches besides main
(`git ls-remote --heads origin`) and (b) uncommitted local state
(`git status --porcelain`) as ADVISORIES at wake/pre-push time. It NEVER affects the
preflight exit code: findings are information ("a sibling is in flight — merge
forward-only before you push"), not failure; even a dead network prints "could not
list" and still passes. The claims ritual covers sections; the inbox covers orders;
this covers the third surface — in-flight BRANCHES — where the PR #39/#40 sibling
collisions actually happened.

## Probe report (v0, 2026-07-10)

> **Sequence:** after PR #40's probe of the websites open-pr-awareness idea (this is the "each repo builds its own step" instance that probe routed; probed while a live sibling branch `groom/sim-verdicts-001-004` sits on origin)

**1. What is this really?**
The idea-engine-local leg of the open-pr-awareness class PR #40 just probed — the same
one-wake-ritual-step build the probe routed to websites (doc edit) and substrate-kit
(planted convention), instantiated for THIS repo's ritual carrier. This repo's ritual
is not a prose WAKE line; it is `scripts/preflight.py` (PR #16), which the CI gate also
runs (PR #18) — so here "one ritual step" means "one `CHECKS` entry". It is the
branches/PRs dual of the `claims/` per-file section ritual: claims make INTENT visible
before work; the sweep makes IN-FLIGHT WORK visible before intent.

**2. What is the possibility space?**
- **Minimal:** a documented wake-ritual line ("run `git ls-remote --heads origin`
  first") — discipline-only, exactly the class the preflight wrapper (PR #16) exists to
  collect into one command.
- **Report-only advisory (this slice):** list branches + local dirt, classify NOTHING —
  the reader applies the three-state table from the websites probe by eye.
- **Classifier:** the three-state table (PR open · pushed PR-less · merged-stale) in
  code — needs PR-state data this seat cannot always reach (the PR #40 probe's Q4:
  seat-capability variance is PROPOSAL 005's open question, queued as INTAKE 005) and
  commit-count alone misclassifies squash-merge leftovers. Deliberately NOT this slice.
- **Committed open-work ledger:** rejected outright — the staleness inversion the
  websites probe's Q4 named; the sweep is a live read, never a committed artifact.
- **Gating check:** rejected — a network blip must never red a PR that changed nothing
  (the harvest-freshness probe's Q4 hermeticity rule, honored by construction here:
  the check ALWAYS exits 0).

**3. What is the most advanced capability reachable by the simplest implementation?**
One `CHECKS` entry + one ~40-line stdlib function gives EVERY wake and EVERY pre-push
run — and, via the gate↔ritual convergence (PR #18), every non-control CI run — an
automatic sibling-branch listing, for free, forever. The ad-hoc `ls-remote` that
prevented the websites #63 collision and discovered sibling PR #38 stops depending on
a session remembering to type it: the ritual command every session already runs prints
it. The live proof exists before the build: at THIS probe's branch time, origin
carries `groom/sim-verdicts-001-004` — a sibling in flight that this session now knows
to merge forward-only around, learned from the sweep it is about to ship.

**4. What breaks it?**
- **The hermeticity tension (the decisive one):** the harvest-freshness probe (PR #22)
  ruled network checks must NOT join `scripts/preflight.py` — but that checker GATES
  (its could-not-run is exit 2, which reds the wrapper). The resolution is exit
  semantics, not location: this check contributes exit 0 UNCONDITIONALLY — findings,
  empty findings, timeout, dead proxy, no `origin` — so CI stays hermetic by
  construction. If it ever grows a nonzero path, it has become a different (rejected)
  idea.
- **Advisory fatigue:** squash-merge leftovers and long-lived branches would print at
  every wake forever; without PR data the sweep cannot say which lines matter. Honest
  degradation per the PR #40 probe Q4: report, never classify — and keep the output to
  a few lines so the PASS wall stays readable.
- **Anchor drift:** `refs/heads/` parsing is stable git plumbing (safer than the gate
  tripwire's YAML byte-anchors), but a future move to a non-`origin` remote name would
  silently empty the sweep — the failure prints as "could not list", loud not silent.
- **False comfort:** the sweep lists branches, not PRs — a sibling working un-pushed is
  invisible. It narrows the collision window; the forward-merge recipe (README
  § Landing conventions) remains the actual safety net.

**5. What does it unlock?**
Sibling-collision discovery at the exact moments it matters (wake = before claiming
work; pre-push = before the race), without a new command, a new committed surface, or
a new writer; dead ad-hoc dependence (PRs #38/#39/#40 all leaned on remembered
`ls-remote`); and a live in-repo existence proof for the fleet-generic kit convention
PR #40 routed to substrate-kit — when the kit builds the planted-`control/README.md`
paragraph, this repo is the working reference implementation.

**6. What does it depend on?**
`git` + python3 stdlib (both already required); `git ls-remote` egress to origin
(universal — every session pushes; failure degrades to an advisory line);
`scripts/preflight.py` on main (PR #16) with its gate wiring (PR #18, tripwired by
PR #36). Nothing cross-lane, nothing unmerged, no simulator question — the one open
question in the class (per-seat PR-tooling variance) is already INTAKE 005 at sim-lab
and this slice deliberately builds BELOW it (branch sweep only, the leg that is
universal).

**7. Which lane should build it?**
**idea-engine — this repo, directly.** It edits this repo's own wrapper, consumed only
by this repo's sessions and gate (Q-0260: only this repo's sessions write here). The
websites step and the kit convention are ALREADY routed by the PR #40 probe — this is
the third, self-serve leg that probe explicitly called "a separate one-line capture,
not this build". Not substrate-kit today: the kit convention is a documented ritual
paragraph; whether kit ships a generic `open-work` helper is that lane's call.

**8. What is the smallest shippable slice?**
One edit at `scripts/preflight.py::CHECKS` (sixth entry, `--open-work` self-invoked
per the `--gate-wiring` pattern) + one `check_open_work()` function: run
`git ls-remote --heads origin`, print every head except main; run
`git status --porcelain`, print any uncommitted paths; wrap both legs so ANY failure
prints an advisory line instead of raising; `return 0` unconditionally. Test = the
live run on this very branch (it must list its own branch and the in-flight sibling
`groom/sim-verdicts-001-004`). Cheaper to build than to route: it ships **in this same
PR** per the README § probe-battery shortcut (first used by PR #2; same deviation
flag as every built-here sibling in this section).

**Recommendation: park(built-here — scripts/preflight.py --open-work, report-only sibling-branch + local-dirt advisory sweep, shipped in this PR)** —
rationale: trivial repo-internal PROCESS tooling per the blessed same-PR shortcut —
no simulator question (the class's one open question is already INTAKE 005; the sweep
itself is proven by its own live run on this branch, which lists a real in-flight
sibling), nothing routes to sim-lab, and the state advances to `historical(<this PR>)`
on merge.
