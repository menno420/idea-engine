# CI collection parity guard — make the 73/121 class of gap impossible to recur

> **State:** parked(build-direct — folded into ORDER 001's execution: the lane's inbox ORDER 001 (P0 CI-collection, live-verified `status: new`/unclaimed/boot-gating @ `b134961`) already mandates a count-FLOOR assertion, but the floor is strictly weaker than this idea's census parity — it catches scope-shrink, not growth-side silent skip; the buildable slice is one census-parity step in the SAME `tests.yml` edit ORDER 001's executor makes (NOT the kit-owned `substrate-gate.yml` — the order's file pointer is stale and that file is regenerated on upgrade), proven by its own red/green run in lane CI — no sim question; manager routes the fold-in note)
> **Class:** process · **Target:** `menno420/superbot-games`

## Problem

The lane's merge gate currently **collects only 73 of 121 tests** — 48 tests exist in the
tree but never run in CI, so a green gate silently under-verifies. The manager already
filed the P0 fix for the *instance* (games inbox ORDER 001, boot-gating, per the
manifest row). But the failure *class* — collection drifting below the tree's real test
census without turning anything red — stays open after that fix: the same misconfigured
testpath/marker/import-error that caused this can recur on the next plugin package, and
nothing would notice.

## Idea

A small guard step in the gate, landed in the same era as the ORDER 001 fix: run
`pytest --collect-only -q` over the whole tree, compare the census against the count the
gate actually executed, and go RED on any shortfall (collection errors count as
shortfall — they are how tests silently vanish). No pinned magic number to maintain:
the tree's own census is the reference, so the guard never goes stale as tests are added.

## Grounding

- Fleet manifest games-plugins row (`https://raw.githubusercontent.com/menno420/superbot/main/docs/eap/fleet-manifest.md`,
  fetched 2026-07-10): "**ORDER 001 (P0 CI-collection: gate collects 73/121 tests)
  pending — boot-gating**".
- Complements, does not duplicate, ORDER 001: that order repairs today's 48-test gap;
  this guard makes the repaired state self-checking. (Same warn-first/checker doctrine
  the hub already applies — cf. the harvested checker family in `ideas/superbot/`.)

**Why now:** the moment ORDER 001 lands, the gate will be trusted again — that trust is
only honest if the collection census is checked on every run, not once.

## Probe report (v0, 2026-07-11)

> **Grounding:** https://github.com/menno420/superbot-games@b134961ef5dddf8a1cc15d97c11704629d81989a · fetched 2026-07-11T00:02Z (manifest row: behind)
> **Grounding:** https://github.com/menno420/superbot@7c6278ec990d9230aac439cb748465bf23bcec56 · fetched 2026-07-11T00:02Z
> **Sequence:** behind superbot-games inbox ORDER 001 (P0 CI-collection — live-verified `status: new`, UNCLAIMED, boot-gating at the pin above): fold this guard into that order's execution slice on the same externally-fired gen-2 boot and one lane claim (the PR #44 one-claim-ordered-slices rule); never a separate later edit to the same workflow step on a clockless lane

*Probed against live state, not the capture's snapshot. superbot-games @ HEAD `b134961`
(ls-remote 2026-07-11T00:02Z — unmoved since PR #44's 23:52Z read). ORDER 001 status:
`control/inbox.md` raw-read at that pin shows `status: new`, issued 2026-07-10T12:45Z;
UNCLAIMED — both lane heartbeats predate the issue time (`control/status-mining.md`
updated 07-10T00:20Z, and its orders line cites the gen-1 `control/inbox-mining.md`
001–005, not this order; `control/status-exploration.md` 07-09T20:09Z, wind-down
complete) and the lane is clockless (inbox ORDER 002 self-arm also `status: new`), so
execution is boot-gated exactly as the manifest row says ("ORDER 001 (P0 CI-collection:
gate collects 73/121 tests) pending — boot-gating", games-plugins row @ superbot HEAD
`7c6278e`; the row still records lane HEAD `adb5f9b`/kit v1.2.0 vs real `b134961`/v1.7.1
— the heartbeat's datapoint-11 staleness persists). The 73/121 gap re-verified REAL by
independent census (blobless clone @ `b134961`): `tests/**` carries 73 `def test_`
functions across 10 mining files, `games/exploration/tests/**` carries 48 across 7
files, total 121; the CI pytest step runs `python3 -m pytest tests/ -q`, so the
exploration root is invisible to it. One correction to the order the capture inherits:
that pytest step does NOT live in `substrate-gate.yml` (ORDER 001's cited anchor) — it
was moved verbatim to the host-owned `.github/workflows/tests.yml` during the
v1.2.0→v1.7.0 kit upgrade (that file's own header says so), and the kit-owned gate is
regenerated on every adopt/upgrade, so a fix landed at the order's stale pointer would
be silently overwritten. Also verified: the repo has NO pytest config file (no
pyproject.toml/pytest.ini/setup.cfg/tox.ini at root), so a bare tree-wide
`--collect-only` genuinely sees all 121 today.*

**1. What is this really?**
A self-checking property for the lane's merge gate — "every test the tree carries is a
test the gate ran" — distinguished from ORDER 001 by level: the order repairs the
INSTANCE (widen scope to 121) and pins a FLOOR (its task item 2: fail if collected <
121, hand-raised as suites grow); this idea makes the repaired state SELF-checking with
no number to maintain (tree census from `--collect-only` vs the count the gate
executed, red on any shortfall, collection errors counting as shortfall). It is the
checker-family doctrine (warn-first/self-verifying gates, cf. this repo's own
preflight `--gate-wiring` tripwire) applied to the one gate property that failed
silently in the lane's history.

**2. What is the possibility space?**
Three axes. **Reference source:** pinned floor (ORDER 001 item 2 — goes stale-lenient
as trees grow) → tree's own census via a second `--collect-only` pass (this capture —
never stale, but the census run must be config-independent) → census parity PLUS a
floor (belt-and-braces: parity catches growth-side skip, the floor catches a
census-side regression that shrinks both numbers together). **Comparison plane:**
executed-vs-census counts (simplest; blind to WHICH tests differ) → collected node-id
set diff (names the missing tests in the red output — same two pytest invocations,
strictly better failure message) → per-root subtotals (localizes the miss to a
package). **Home:** inline step in the lane's `tests.yml` (right place today — the
host-owned carve-out file that already runs the suite) → a `scripts/` checker the step
calls (testable locally, same one-writer file) → a substrate-kit generic
(`bootstrap check` census-parity for any adopter with a test suite — plausible
graduation, but the kit gate deliberately does NOT run host test suites; premature
before one lane proves the pattern).

**3. What is the most advanced capability reachable by the simplest implementation?**
Two pytest invocations and an integer compare buy the full property. The gate step
becomes: `collected=$(python3 -m pytest --collect-only -q | ...count...)` over the WHOLE
tree, run the suite over the whole tree (ORDER 001's fix), then assert
`executed == collected` and `collection errors == 0`. Because the reference is the
tree's own census, the guard is maintenance-free: adding a suite, a plugin package, or
a new test root can never silently widen the gap again — the census grows in the same
commit the tests do. With the node-id set diff variant (one `sort | comm` more), a red
run PRINTS the exact tests the gate missed — turning the failure class from "48 tests
quietly never ran for N weeks" into a named list on the first PR that introduces it.

**4. What breaks it?**
**Census inherits the gate's blindfold.** The guard compares two runs of the SAME
pytest; if a future pytest config sets `testpaths = tests` (none exists today —
verified), the census run honors it too, both numbers read 73, and the guard
certifies the exact failure it exists to catch. The census invocation must therefore
be explicitly tree-wide (`--collect-only -q .` from the repo root, or override
`testpaths`) and the slice should note WHY. **Deselection false-reds.** The moment the
suite legitimately deselects (`-m "not slow"`, `--ignore`), executed < census and the
guard reds honestly-but-wrongly; parity must compare like-for-like (same
markers/filters on both invocations, deselected counted explicitly) — today trivial
(no markers in use), but the slice should assert on pytest's own
collected/deselected/error arithmetic, not a naive pass-count. **Stale-pointer
mis-execution.** ORDER 001 cites `substrate-gate.yml`'s test-suite step; that step
now lives in `tests.yml`, and the kit-owned gate file is REGENERATED on upgrade — a
guard (or fix) landed at the cited path is silently deleted by the next
`bootstrap upgrade`. **Repo-boundary limit.** The census sees this tree only; once
games ship as plugin packages from other repos (the host-seam era), a package's tests
live outside this census — the guard proves lane-tree parity, not fleet-wide parity,
and must not claim more. **Output-parsing brittleness** across pytest versions
(`N tests collected` wording) — prefer exit-code + machine-readable counts
(`--collect-only -q` line count, or a tiny conftest hook) over grepping prose.

**5. What does it unlock?**
Trust in the gate's green that survives growth: ORDER 001's fix is honest on the day
it lands, and this guard keeps it honest on every commit after — the manager's
night-review Q7 class ("CI now gates X" claims that are false as stated) becomes
machine-checked in this lane. It retires the floor-raising chore before it is ever
performed (no hand-maintained 121). The red output (node-id diff variant) gives the
gen-2 plugin wave a per-PR proof that each new plugin package's tests actually joined
the gate — the exact assurance the host-seam conformance work (PR #44's probe) wants
from CI. And once proven here, the pattern is a one-page substrate-kit graduation
candidate for every adopter whose host workflow runs a suite.

**6. What does it depend on?**
**ORDER 001's execution** — the guard lands as part of (or immediately behind) the
scope fix; alone it would just red the gate on the known 48-test gap with no fix
attached (correct, but the P0 order already owns the fix). **The gen-2 boot** — the
lane is closed and clockless (both heartbeats final, ORDER 002 self-arm `status: new`),
so nothing executes until externally fired; this rides the same boot the PR #39
encounter-contract and PR #44 host-seam slices are sequenced on, one lane claim,
ordered. **The host-owned workflow seam** — `tests.yml` is the ONLY correct home
(kit-owned gate regenerates); this is also the correction ORDER 001's executor needs.
**Tree-wide collectability** — census parity requires `--collect-only .` to succeed
from the root (true today: no config, exploration tests are a proper package); any
future test root must stay reachable from root collection, which is exactly the
property the guard enforces.

**7. Which lane should build it?**
superbot-games — it is one step in the lane's own merge-gate workflow, inside a slice
the manager has already ordered (ORDER 001, P0). Not this repo (writes no lane code).
Not sim-lab — there is no evidence question: the guard's correctness is demonstrated by
one deliberate red (narrow the scope, watch it fail, restore) in the lane's own CI.
Not substrate-kit YET — the kit gate deliberately does not run host suites; graduation
is a later, separate idea once one lane has the pattern green. The manager's routing
move is a fold-in note on ORDER 001 (census parity instead of / in addition to the
item-2 floor, plus the stale-pointer correction), not a new order.

**8. What is the smallest shippable slice?**
One PR in superbot-games, the ORDER 001 execution itself, touching only
`.github/workflows/tests.yml` (and its evidence in the PR body per the order's item 3):
(a) widen the suite run to the whole tree; (b) add the parity step — tree-wide
`--collect-only -q` census, assert executed == collected and zero collection errors,
red on shortfall (satisfies the order's item-2 intent with the census replacing the
hand-raised floor, or alongside a floor if the executor keeps belt-and-braces);
(c) prove it in the same PR: one commit that temporarily narrows the run back to
`tests/` must turn the gate RED (the guard's own red/green demonstration), then revert.
Explicitly NOT in the slice: any edit to the kit-owned `substrate-gate.yml`, any
fleet-generic kit checker, any cross-repo package census.

**Recommendation: park** — build-direct, folded into ORDER 001's execution slice: a
gate self-check proving executed == collected is proven by its own red/green run in the
lane's CI, not by simulation — and it must ride the P0 order's own `tests.yml` edit
(live-verified `status: new`, unclaimed, boot-gating @ `b134961`; the order's item-2
floor is strictly weaker — it misses growth-side silent skip — and its cited file
anchor is stale: the pytest step moved to host-owned `tests.yml`, where the kit-owned
gate file would lose any fix on the next upgrade).
