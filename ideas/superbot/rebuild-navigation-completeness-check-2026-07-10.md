# Idea — navigation-completeness check (enforce the Back+Home contract) — link index

> **State:** parked(half-built-at-target — built half: the Back+Home golden = A-3 inside superbot-next D-0020 (`sim/navigation_walk.py` + `tests/unit/navigation_golden/`, CI red-gated); open half: the preset-coverage assertion, a designed-in LOUD arm-later (`presets_checked=False`) blocked on band-1's preset grammar — in-lane arming, earns no slot here; probe 2026-07-12)
> **Class:** process · **Target:** `menno420/superbot-next`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/rebuild-navigation-completeness-check-2026-07-03.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/rebuild-navigation-completeness-check-2026-07-03.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/rebuild-navigation-completeness-check-2026-07-03.md)).

A navigation-completeness golden driving the panel framework through every node and re-render path, asserting Back + Home work at every depth — the enforcement arm of the rebuild's navigation contract.

## Probe report (v0, 2026-07-12)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/1ecc21138fe0a1eb672d03b66bd319164c29d55f/docs/ideas/rebuild-navigation-completeness-check-2026-07-03.md@1ecc211 · fetched 2026-07-12T00:14Z
> *(pin annotation: superbot live HEAD S = `1ecc21138fe0a1eb672d03b66bd319164c29d55f` by `git ls-remote` 00:13:56Z — the canonical doc is byte-identical at S HEAD vs the `fd638e3` harvest pin (md5 match, `50ddd6f…` both), status still `ideas` — capture only. The capture asks for TWO asserts, verbatim: (a) "a **navigation-completeness golden** that drives the panel framework through every declared node and every re-render path and asserts each resulting state carries both a working **Back** … and a working **Home**"; (b) "plus a **preset-coverage** assertion that every feature belongs to ≥1 preset (nothing is unreachable in *every* preset)".)*
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-next/d3dba9b53bf87ededee6ed4942a1e7c87e185add/docs/decisions.md@d3dba9b · fetched 2026-07-12T00:15Z
> *(pin annotation: superbot-next live HEAD N = `d3dba9b53bf87ededee6ed4942a1e7c87e185add` by `git ls-remote` 00:13:56Z; N also read as a blobless clone at the same HEAD. **D-0020 · status: decided · date: 2026-07-08** — landed in superbot-next PR #19, commit `c7defbc` — carries the A-3 golden verbatim: "A-3 navigation-completeness golden: sim/navigation_walk.py drives the REAL S9b panel engine (reachability from hub roots, direct-entry semantic-parent fallback per verification-review §3.4, Back/Home rendered AND static-table-bound, parent re-render population stability) + tests/unit/navigation_golden/ (green over the empty registry, proven non-false-greening by fixture negatives; presets_checked=False LOUD until band-1 preset grammar)". CI wiring read at the invocation site, not the doc claim: `.github/workflows/ci.yml:34` runs `python3 -m pytest tests/ -q` — the golden red-gates every N PR.)*

> Single-pass battery (panel not escalated: docs/process surface, reversible park, no
> security/data/spend/public blast radius — README § probe battery). This head was a
> mint-time TOP-5 exclusion whose named trigger FIRED ("A-3 golden landed inside
> D-0020 — price which half remains before it earns a slot", `control/status.md`
> notes @ `329547d`); the briefed question — which half remains and what it
> costs/earns — is answered under Q4/Q6/Q8 below. Body-exists-is-not-body-wired
> discipline applied: the golden's test file, the walker's field, and the CI
> invocation were all read at N HEAD, not inferred from D-0020's prose.

**The two halves, verified at N `d3dba9b`:**

- **BUILT half — the Back+Home golden (the capture's assert (a), in a STRONGER form
  than asked):** `sim/navigation_walk.py` walks every registered node via the REAL
  panel engine; per state it asserts reachability from hub roots, Back resolving to
  the real parent/stack (with the direct-entry semantic-parent fallback),
  Home rendered AND static-table-bound, and parent re-render population stability —
  re-render coverage included, exactly the capture's "across unlimited re-renders"
  clause. `tests/unit/navigation_golden/test_navigation_completeness.py` (137 lines
  @ N) is the CI proof: the golden suite walks whatever is registered (vacuously
  green over the near-empty registry today, arming automatically as port bands
  register panels), and a second suite proves the walker CANNOT false-green
  (fixture negatives: missing parent fallback red, unregistered parent red,
  `home_ok` asserts static-table binding, `rerender_ok` asserted). Red-gating via
  `ci.yml:34`.
- **OPEN half — the preset-coverage assertion (the capture's assert (b)):** NOT
  built, and DESIGNED not-yet-buildable: the walker reserves the leg as
  `presets_checked: bool = False   # arm-later: band-1 preset grammar`
  (`sim/navigation_walk.py:56` @ N) and the golden carries
  `test_preset_leg_is_a_loud_arm_later` asserting `presets_checked is False`
  (test file lines 92–94) — "loud arm-later, never a silent pass" (docstring lines
  14–17). The blocker is real at N HEAD: NO preset grammar exists anywhere —
  zero `preset` hits in `sb/spec/panels.py`, no `tools/check_*preset*`; the only
  preset-named files at N are band-7 AI behavior presets
  (`sb/domain/ai/behavior_presets.py`), an unrelated namespace.

**1. What is this really?** The enforcement arm of Q-0231 (framework-injected
Back+Home on every panel state at every depth) — a process idea from superbot's
Phase-A hub session (PR #1684), split by construction into the golden (assert (a))
and the preset-coverage leg (assert (b)). The verify-first read makes assert (a) a
DONE idea: superbot-next built it fresh inside D-0020 on 2026-07-08 — two days
before this repo harvested the capture — the same predates-the-harvest pattern as
the sibling `rebuild-layout-success-simulator-2026-07-10.md` (same decision,
different arm: that one is the layout SCORER, this one is the nav-contract
ENFORCER; no overlap consumed between them).

**2. What is the possibility space?** As-built (walker + golden + fixture-negative
oracle proofs + CI gate); the preset-coverage leg (reserved field, arms at band-1);
live-registry coverage growth (automatic — each port band's registered panels join
the walk with zero new test code); and downstream: the walker doubles as the
navigation oracle's substrate inside the same `sim/` home. Every branch is in-lane
follow-through at superbot-next, none is a new build.

**3. Most advanced capability reachable by the simplest implementation?** Already
reached at the target: the navigation contract is CI-proven over the real engine
with false-green immunity, and coverage scales with registration for free. The
simplest TRUE remainder is the arm-later flip itself: when band-1 mints the preset
grammar, add one coverage assertion over it and retire the loud `False` test —
a one-slice band-1 rider, its seam already reserved.

**4. What breaks it? (assumptions + the priced cost)** (a) The open half is
DEPENDENCY-BLOCKED, not neglected: building preset-coverage now means inventing the
preset grammar out of band — exactly the fabrication the lane deferred to band-1.
(b) The unarmed window's risk is BOUNDED by design: the leg cannot silently pass
(the loud test), so the only failure mode is band-1 shipping its preset grammar
WITHOUT flipping the leg — a body-exists-not-wired risk worth one verify at that
event, not a slot now. (c) The golden's vacuous-green-today is not a hole: the
fixture-negative suite proves the walker reds on real violations, and bands arm it
by registering. COST of the remaining half: zero here (nothing to route — the
arm-later is ledgered in the target's own decision, walker field, and test);
small at the lane (one assertion + one test retirement riding band-1). EARN:
closes assert (b) — nothing unreachable in every preset — a class no other checker
at N covers.

**5. What does it unlock?** Consuming this exclusion clears the last D-0020-shaped
head from the superbot section's mint-time list; the fired-trigger pricing itself
is the deliverable (the heartbeat carried "price which half remains before it
earns a slot" — answer: the preset half, and it earns arming-at-band-1, not a
slot).

**6. What does it depend on?** Built half: nothing — shipped and red-gating.
Open half: band-1's preset grammar (does not exist at N `d3dba9b`), then the
one-assertion flip; both owned by superbot-next's own band sequencing.

**7. Which lane should build it? (honest routing)** Nobody, now: the built half is
done by the right lane at the right layer; the open half is already scheduled by
the target's own design (the reserved field + loud test ARE the routing). NOT
sim-shaped: a boolean contract enforcement with no parameter space or corpus —
nothing for sim-lab to settle, so NO outbox proposal. The one forwardable watch:
when band-1's preset grammar lands, verify the leg actually armed (the Rule-6
registration lesson — body-exists is not body-wired).

**8. Smallest shippable slice?** None here. At the lane: the band-1 rider above
(mint preset grammar → assert every feature ∈ ≥1 preset → retire
`test_preset_leg_is_a_loud_arm_later`).

**Recommendation: park** — half-built-at-target: the Back+Home golden (assert (a))
shipped inside superbot-next D-0020 in stronger-than-asked form (real-engine walk,
re-render stability, static-table-bound Home, false-green-proofed, CI red-gated);
the remaining half is the preset-coverage assertion (assert (b)), a designed-in
loud arm-later blocked on band-1's preset grammar — it costs nothing here, earns
its arming inside band-1, and does not earn a TOP-5 slot; nothing routes to
sim-lab.
