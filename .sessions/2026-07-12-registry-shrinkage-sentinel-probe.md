# Session — single-pass probe: superbot-next registry-shrinkage-sentinel-fixture

> **Status:** `complete`

- **📊 Model:** fable-5 · single-pass battery (no panel triggers) · docs-only
  probe slice (one probe append + state flip + index re-badge + card; no code)

## What this session did

Single-pass probe (battery v0, no panel triggers) of
`ideas/superbot-next/registry-shrinkage-sentinel-fixture-2026-07-12.md` — the
2026-07-12 superbot-next harvest's first head (@ `80464ab`): one autouse
conftest fixture snapshotting `ref_inventory()` + `provider_names()` at
test-directory boundaries and asserting no shrinkage, sourced from the lane's
canonical-order flake-fix card ("the world a suite finds is the world it
leaves").

Verify-first, live: N = superbot-next HEAD
`af985c17def5ff2478103cb363ebb150cb583a97` (`git ls-remote`-resolved this
session, two commits past the harvest pin; every probe-relevant file
byte-identical across the gap by `git diff --stat`). Decisive findings:
**the lane has NOT built it** (`tests/conftest.py` at N is an 8-line
sys.path bootstrap; all 10 sub-conftests grep zero for
ref_inventory/provider_names/shrinkage/sentinel; no static checker covers
runtime registry state; `git log 80464ab..HEAD -- tests/conftest.py` empty);
both snapshot APIs are measured-cheap (`sb/spec/refs.py:184` — a sorted
in-memory dict projection over the ref table, ≈1165 refs fully armed per the
manifest snapshot's refs projection; `rank_providers.py:79` — list arithmetic
over a ~5-entry dict); and the class is still alive by the fix card's own
ledgered follow-up (artificial suite orders red 5 tournament + 2 band5 tests
on clean main).

The probe's design correction (battery Q4): the captured "session-scoped
autouse fixture" cannot see directory boundaries by pytest scope semantics
(session autouse runs once; `scope="package"` is inconsistent — only 14/34
unit dirs have `__init__.py`; a function-scoped finalizer fires before
module-scoped restores → false positives). Routed implementation: a
`pytest_runtest_teardown(item, nextitem)` **hookwrapper** in
`tests/conftest.py`, checking superset-then-rebaseline after `yield` on
directory change. Honest coverage note carried into the report: the sentinel
sees leak mechanisms 2+3 (9/11 victims); mechanism 1 (ai reader-seam
pollution) is invisible to both snapshot APIs — named gap, no inventory API
exists.

Verdict: **parked(routed — lane build-direct)** — superbot-next test-only
slice, ~40–60 lines, deterministic red/green kill-test (drop one #222 re-arm
→ red naming the boundary); nothing sim-shaped (a shuffle-corpus sim would
only estimate what one lane CI run settles). No outbox proposal.

Dedup swept: `composition-parity-registration-diff` (parked lane-self-served
— partial-overlap not duplicate: boot-time both-roots parity vs in-session
temporal non-shrinkage); `effect-arming-compensator-checklist` +
`band-binding-doctrine-encoding` (distinct — doctrine-doc surface);
superbot `live-tree-test-culprit-attribution` (distinct — cross-merge drift
attribution, other repo); superbot `reference-integrity-invariants`
(distinct — static dangling-ref); superbot `autospec-mock-fidelity-guard`
(distinct). No duplicate idea file.

Inbox read-only check (dispatch ask): `control/inbox.md` carries ORDERs 001
and 002 only — **no ORDER 003 or later** at branch time.

**Section-collision flag (dispatch boundary — no claim file):** this slice is
barred from `control/`, so no `control/claims/` entry exists; this card's
born-red first commit carried the `ideas/superbot-next/` collision flag per
the PR #222/#225/#226/#228 workflow convention.

## Close-out

**Evidence:**

- ideas touched (2): `ideas/superbot-next/registry-shrinkage-sentinel-fixture-2026-07-12.md`
  (state flip captured→parked(routed — lane build-direct…) + probe report v0
  append), `ideas/superbot-next/README.md` (index bullet re-badge per the
  PR #192 card convention)
- sessions touched (1): `.sessions/2026-07-12-registry-shrinkage-sentinel-probe.md`
- code touched: none · control touched: none (dispatch boundary; READ-ONLY
  read of `control/inbox.md` for the ORDER-003 check)
- git: branch `probe/registry-shrinkage-sentinel` off main `d68ac2d`,
  born-red card first commit `437bd93`, probe+close-out commit follows;
  draft PR flipped ready per dispatch instructions — landed by the kit-owned
  auto-merge flow, never merged by this slice.
- verify: `python3 bootstrap.py check --strict` and
  `python3 scripts/preflight.py` run before push (results in the PR).

**Judgment (the half only the session knows):**

- Decisions made: no D-entry — probe verdict only (park routed, lane
  build-direct). One evidence-over-claim call, declared: the capture's OWN
  mechanism ("session-scoped autouse fixture … at each test-DIRECTORY
  boundary") is internally inconsistent under pytest scope semantics; the
  probe corrects the implementation in the routed slice rather than parking
  on the flaw — the invariant is sound, the fixture-scope wording was the
  source card's shorthand, and killing a live gap over its author's
  shorthand would be letter-over-substance in the wrong direction.
- Next session should know: the lane self-serve check for this head is one
  raw fetch — `tests/conftest.py` at lane HEAD; anything beyond 8 lines
  means re-verify before relaying. The routed slice's spec lives in the
  probe's Q8 (hookwrapper, superset-then-rebaseline, kill-test recipe).
  Mechanism 1 (reader-seam pollution) remains unsentineled fleet-wide — a
  future capture needs a seam-inventory API lane-side first.

## 💡 Session idea

A harvested 💡 that names a MECHANISM ("session-scoped autouse fixture") is
the author's shorthand, not a spec — this probe's decisive Q4 finding was
that the mechanism as written cannot implement the invariant as stated
(pytest scope semantics), while the invariant itself verified sound and
open. Cheap harvest-time fix: when a source card's idea names a concrete
mechanism, the capture should tag it `(mechanism: as-stated, unverified)` so
the probe budget plans a design-check pass instead of discovering mid-probe
that the battery's Q4 is really a redesign.

## ⟲ Previous-session review

PR #230 (warn-first-checker-authoring-kit probe): adopted wholesale — (a)
its live-HEAD-first discipline paid again (N moved `80464ab`→`af985c1` since
harvest; the byte-identical diff over probe-relevant files is what lets
harvest citations carry); (b) the born-red-card collision flag under the
dispatch boundary used verbatim; (c) its letter-vs-substance honesty pattern
inverted here deliberately: #230 parked on a trigger that fired on letter
not substance, this probe UPHELD a head whose letter (fixture scope) was
wrong but whose substance (the invariant + the open gap) verified — the
shared rule is "verify the substance, rule on the substance". Improvement
carried: its card noted auto-draft evidence diffing against the wrong base;
this card was hand-written from the first commit.

## Handoff → next wake

This consumes the fifth mint's probe-of-mint-#1 successor slot per the
coordinator's dispatch (coordinator-side heartbeat edit — NOT done here,
control/ is coordinator-only). Facts for the heartbeat: verdict
parked(routed — lane build-direct) with a design correction the lane should
inherit (hookwrapper, not session-scoped fixture); no outbox proposal;
inbox still ORDERs 001–002 only; the superbot-next section index now
carries the re-badge. The routed slice is manager-sweep material: one lane
test-only PR, spec in the probe's Q8.
