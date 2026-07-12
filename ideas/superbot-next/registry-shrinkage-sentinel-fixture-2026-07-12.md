# Registry-shrinkage sentinel fixture — "the world a suite finds is the world it leaves"

> **State:** parked(routed — lane build-direct: a ~40–60-line test-only slice in superbot-next `tests/conftest.py`, a `pytest_runtest_teardown` hookwrapper (NOT the captured session-scoped autouse fixture — pytest scope semantics can't see directory boundaries, see probe Q4) snapshotting `ref_inventory()` + `provider_names()` and asserting superset-then-rebaseline at each test-directory boundary — probed 2026-07-12: gap verified OPEN at live HEAD `af985c1` (tests/conftest.py is an 8-line sys.path bootstrap, zero sentinel logic in any of the 10 sub-conftests or 24 tools/ checkers), snapshot cost measured trivial (the armed ref table ≈ 1165 entries, in-memory dict projection), the class is demonstrably still alive (the fix card's own ledgered follow-up: artificial suite orders still red 5+2 tests on clean main); nothing sim-shaped — deterministic test hygiene the lane's own red/green kill-test settles)
> **Class:** process · **Target:** `menno420/superbot-next`
> **Grounding:** https://github.com/menno420/superbot-next@80464ab39f86d55cede1e38b4780e7b1cc4a1777 · fetched 2026-07-12T01:34:18Z

One session-scoped autouse fixture in the lane's `tests/conftest.py` that snapshots
`ref_inventory()` + `provider_names()` at each test-DIRECTORY boundary and asserts no
shrinkage — so the next one-way registry wipe fails red NAMING the leaking suite,
instead of surfacing as an 11-victim canonical-order mystery three bands downstream
(the flake class the lane just hand-diagnosed: three isolation-leak mechanisms behind
one ordering-dependent failure). Turns the debugging invariant the fix session stated
verbatim — "the world a suite finds is the world it leaves" — into a standing sentinel.
Source: lane session card [`.sessions/2026-07-12-canonical-order-flake-fix.md` § "💡
Session idea"](https://github.com/menno420/superbot-next/blob/80464ab39f86d55cede1e38b4780e7b1cc4a1777/.sessions/2026-07-12-canonical-order-flake-fix.md)
@ `80464ab` ([raw](https://raw.githubusercontent.com/menno420/superbot-next/80464ab39f86d55cede1e38b4780e7b1cc4a1777/.sessions/2026-07-12-canonical-order-flake-fix.md)).

## Probe report (v0, 2026-07-12)

> **Grounding:** https://github.com/menno420/superbot-next@af985c17def5ff2478103cb363ebb150cb583a97 · fetched 2026-07-12
> *(pin annotation: N = superbot-next live HEAD by `git ls-remote` this session =
> `af985c17def5ff2478103cb363ebb150cb583a97` — two commits past the harvest pin
> `80464ab` (#226 creature parity flip, #225 band7 btd6 freeplay). Every
> probe-relevant file is byte-identical across the gap (`git diff --stat
> 80464ab..af985c1` over the source card, `tests/conftest.py`,
> `sb/spec/refs.py`, `sb/domain/community/rank_providers.py` touches only two
> new band6/band7 test files + a 1-line composition-parity edit), so harvest-pin
> citations carry to HEAD unchanged. Tree scans via read-only blobless clone at
> N; file reads via raw at the pinned SHA.)*

> Single-pass battery (panel not escalated: read-only test tooling, reversible,
> no security/data/spend/public blast radius — README § probe battery).
> Verify-first at N: [`tests/conftest.py`](https://raw.githubusercontent.com/menno420/superbot-next/af985c17def5ff2478103cb363ebb150cb583a97/tests/conftest.py)
> is an **8-line sys.path bootstrap — no sentinel**; all 10 sub-conftests
> (integration, ai, band6, compiler, credentials, interaction,
> navigation_golden, panels, scheduler, workflow) grep ZERO for
> `ref_inventory|provider_names|shrinkage|sentinel|autouse.*session`; no
> `tools/check_*` covers runtime registry state (24 checkers, all static);
> `git log 80464ab..HEAD -- tests/conftest.py` is EMPTY — **the lane has NOT
> built this since harvest**. Source card and both snapshot APIs read at N.

**1. What is this really?** A standing tripwire for the isolation-leak class
the lane just paid an 11-victim diagnosis for: assert at every test-directory
boundary that the registry world is a superset of the world the directory was
handed ("the world a suite finds is the world it leaves" — the fix card's own
invariant, [source card @ N](https://raw.githubusercontent.com/menno420/superbot-next/af985c17def5ff2478103cb363ebb150cb583a97/.sessions/2026-07-12-canonical-order-flake-fix.md)
§ 💡). The diagnosed class, per that card's root-cause section — ONE trigger
(#213's `tests/integration/` collects first and imports the ENTIRE composition,
making import-time registration a session-start one-shot), THREE leak
mechanisms: (1) **ai, 2 victims** — an after-only conftest reset re-armed
`ENSURE_REFS()` whose tail (`install_ai_platform()`, `sb/manifest/ai.py:290`)
left composition-root READER seams armed over a closed DB pool; (2) **band2/
band3/band6, 6 victims** — an authority test ended with a bare
`clear_ref_table()` (table emptied, `sb.manifest.*` purged, no re-arm), and
cached `sb.domain.*` import-time registrations can never re-fire →
`RefUnresolved` downstream, aggravated by two ensure-only registration gaps;
(3) **band6 providers, 2 victims** — a band4 teardown wiped the rank-provider
registry to builtins-only and module-global boolean latches ("I ran once"
instead of registry truth) stranded `countlb`/`dm_lb` forever. Who it's for:
the next lane session that lands a one-way wipe — the sentinel turns three
bands of downstream mystery into a red that names the leaking directory.

**2. What is the possibility space?** (i) Do nothing — the canonical 11 are
fixed (#222: 1473 passed both orders) but the CLASS is alive by the fix card's
own ledger: "artificial orders skipping intermediate suites still flake …
reds 5 tournament tests on clean main too; … reds the 2 import-time-port-fill
pins" — same family, explicitly ledgered as follow-up. (ii) The captured
sentinel at directory-boundary granularity — the value peak (matches the
failure class: cross-suite leakage; matches the attribution need: names the
suite). (iii) Per-test granularity — sharper attribution but couples to every
function/class fixture's restore timing; unnecessary, the diagnosis needed
suite-level naming. (iv) Full set-EQUALITY instead of superset — wrong:
growth is legitimate (later suites lazily import more `sb.domain.*`, the
table grows monotonically in a healthy run); shrinkage is the defect. (v)
Extend to reader seams (mechanism 1's surface) — no seam-inventory API
exists today; over-reach for v1, honest gap named in Q4. (vi) A static
`tools/check_*` checker — cannot see runtime table state; the invariant is
behavioral, only a pytest-session observer can hold it.

**3. What is the most advanced capability reachable by the simplest
implementation?** One hookwrapper (~40–60 lines, `tests/conftest.py` only)
polices every current and FUTURE suite at once — ~36 directory boundaries
(34 `tests/unit/*` dirs + integration + session end) per run, under ANY
collection order, with zero per-suite opt-in: a new suite is covered the
moment it exists. Snapshot cost measured cheap at N: `ref_inventory()` is a
sorted in-memory dict projection ([`sb/spec/refs.py:184-190`](https://raw.githubusercontent.com/menno420/superbot-next/af985c17def5ff2478103cb363ebb150cb583a97/sb/spec/refs.py))
over the armed table — ≈1165 refs when fully armed (the snapshot's `refs`
projection at N: 536 handler / 294 workflow / 189 panel / 119 provider / 27
engine) — and `provider_names()` is list arithmetic over a ~5-entry dict
([`rank_providers.py:79-83`](https://raw.githubusercontent.com/menno420/superbot-next/af985c17def5ff2478103cb363ebb150cb583a97/sb/domain/community/rank_providers.py));
sub-millisecond per boundary, unmeasurable across a 1473-test run. Bonus
reach: the sentinel needs NO optional deps, so it fires even in the
minimal-deps CI job (pytest+pyyaml) where the 11 victims were invisible
because their dep-guarded suites skip — the wipe is detected in whatever job
runs the WIPING suite, victims present or not.

**4. What breaks it?** (i) **The captured mechanism is internally
inconsistent — the probe's design correction.** A "session-scoped autouse
fixture" runs its body ONCE per session (setup) and once at teardown; it
cannot observe per-directory boundaries by scope alone. pytest's
`scope="package"` is no rescue: only 14 of 34 `tests/unit/*` dirs have
`__init__.py` at N, so package grouping is inconsistent by construction.
And a function-scoped autouse fixture's finalizer runs BEFORE module-scoped
finalizers tear down (LIFO by scope), so a module fixture that legitimately
restores registry state after its last test would false-positive. The
correct seam: a `pytest_runtest_teardown(item, nextitem)` **hookwrapper** in
`tests/conftest.py` — after `yield` (i.e. after ALL fixture finalizers for
the outgoing scopes have run), if `nextitem is None` or `nextitem`'s
directory differs from `item`'s, assert current-world ⊇ baseline, then
re-baseline. (ii) **Mechanism 1 is invisible to v1**: the ai leak was armed
reader seams (state POLLUTION), not registry shrinkage — `ref_inventory()` +
`provider_names()` cover mechanisms 2+3 (9 of the 11 victims); the card's
fix (the ai conftest now ends seams un-armed) holds mechanism 1, unsentineled.
(iii) In-test legitimate wipes (the authority compile probes, band4's
builtins-only teardown) all restore before the boundary post-#222 — the
sentinel keys on boundaries precisely so intra-suite churn stays invisible.
(iv) A future INTENTIONAL permanent narrowing would need a one-line
baseline-reset escape; YAGNI until it exists.

**5. What does it unlock?** The next one-way wipe fails red AT the leaking
directory's boundary, naming it — versus the #222 diagnosis (minimal-chain
bisection across three bands, an invalidated experiment redone clean). The
ledgered follow-up class (artificial-order flakes, still red on clean main)
becomes locatable the same way — boundary checks hold under any order. And
the fix card's stated invariant graduates from prose in a session card to an
executable contract every future suite inherits free.

**6. What does it depend on?** Nothing unshipped: both snapshot APIs are
live at N (`sb/spec/refs.py:184` `ref_inventory`, `rank_providers.py:79`
`provider_names`), pure stdlib + pytest hooks, no deps, no store, no owner
action. Cheapest confirm/kill evidence, priced: this probe's confirm cost
was one `git ls-remote` + one blobless-clone tree scan + ~14 raw file reads
(decisive facts: no sentinel anywhere at N; both APIs cheap; source card
byte-identical harvest-pin→HEAD). The build-time kill-test is deterministic
and self-evidencing: reintroduce one fixed leak (e.g. drop the band4
teardown re-arm) → the sentinel MUST red at the band4 boundary naming it;
restore → green. Nothing probabilistic remains.

**7. Which lane should build it — and what does it displace or duplicate?**
**superbot-next** — build-direct: it owns `tests/conftest.py`, both
registries, and the diagnosis; the slice is a test-only PR in its own
walking-skeleton convention. Honest sim check: a sim COULD seed test-order
shuffles and measure detection rate, but the invariant is deterministic —
a wipe either shrinks the table at a boundary or it doesn't, and the Q6
red/green kill-test settles in one lane CI run what a shuffle corpus would
only estimate; routing this to sim-lab would re-run pytest and report "it
detects". No proposal; outbox tail unchanged. Dedup findings, named:
[`composition-parity-registration-diff-2026-07-10.md`](composition-parity-registration-diff-2026-07-10.md)
— parked(lane-self-served), **partial-overlap, not duplicate**: same ref-table
surface, orthogonal invariant axis (boot-time parity of two composition
roots via `tests/unit/invariants/test_composition_parity.py` vs in-session
temporal non-shrinkage across suite boundaries — the parity test cannot see
a mid-session wipe); [`effect-arming-compensator-checklist-2026-07-10.md`](effect-arming-compensator-checklist-2026-07-10.md)
+ [`band-binding-doctrine-encoding-2026-07-10.md`](band-binding-doctrine-encoding-2026-07-10.md)
— distinct (doctrine-doc slices, different surface);
`ideas/superbot/live-tree-test-culprit-attribution-2026-07-10.md` — distinct
(same name-the-culprit motive, other repo, cross-MERGE drift attribution not
in-session leakage); `ideas/superbot/reference-integrity-invariants-2026-06-16`
(link-index) — distinct (static dangling-ref invariant);
`ideas/superbot/autospec-mock-fidelity-guard-2026-07-10.md` — distinct (mock
fidelity). Shape precedents, not overlap: settle-once / pil-card
guard-an-invariant tests. No duplicate idea file.

**8. What is the smallest shippable slice?** One superbot-next test-only PR:
`tests/conftest.py` gains a module-level `{"baseline": None}` state + a
`@pytest.hookimpl(wrapper=True)` `pytest_runtest_teardown(item, nextitem)`
that, after `yield`, on directory change (or `nextitem is None`) computes
`missing_refs = baseline_refs - set(ref_inventory())` and
`missing_providers = baseline_providers - set(provider_names())`, fails with
a message naming the OUTGOING directory and the missing keys, then
re-baselines (superset-then-rebaseline — growth welcome, shrinkage red).
Cost: ~40–60 lines, zero runtime code, sub-ms per boundary, deletable in one
revert. Red/green reference: the Q6 kill-test (drop one #222 re-arm → red
naming the boundary; restore → green), plus full `pytest tests/ -q` staying
1473/2-skipped in both canonical and alternate orders.

**Recommendation: park** — routed (superbot-next lane build-direct: the
Q8 hookwrapper slice in `tests/conftest.py`). Rationale: the gap is verified
OPEN at live N `af985c1` (no sentinel anywhere; the class alive by the fix
card's own ledgered follow-up), the snapshot APIs are measured-cheap
(≈1165-entry in-memory projection), and the captured design needs one
correction the lane should inherit (directory boundaries need a teardown
hookwrapper, not a session-scoped autouse fixture); deterministic test
hygiene leaves nothing for sim-lab to settle.
