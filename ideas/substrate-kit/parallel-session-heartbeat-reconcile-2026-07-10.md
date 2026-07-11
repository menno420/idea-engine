# Parallel-session heartbeat reconcile — the one-writer rule's blind spot, codified

> **State:** parked(routed — substrate-kit lane build: the planted control/README gains a "parallel sessions, same lane" section + two mechanical checker advisories (non-monotonic `updated:` stamp · reconcile-dropped-facts); this repo's README § Landing conventions recipe is the working reference implementation; premise verified INTACT at live kit HEAD `be72c09` — see probe report)
> **Class:** process · **Target:** `menno420/substrate-kit`

## Problem

The coordination protocol's conflict-freedom rests on "one writer per file" — which
holds across Projects but **not within one**: a lane running parallel slices (the
Q-0265 continuous-chaining mode this repo operates under) has N in-flight branches
that each end with a `control/status.md` overwrite. This repo hit the collision
repeatedly on one day: PR #15's branch had to `git merge origin/main` mid-flight and
hand-reconcile the heartbeat after siblings #13/#14 landed (merge commit 25b26b2);
PR #12 pre-wrote a predicted PR number that turned out wrong and needed a fixup
commit (7ce1607); and successive stamps landed out of order against wall-clock
(21:40Z/22:25Z stamps on commits that landed 20:31Z/20:44Z — recorded in the 20:55Z
heartbeat). The reconcile recipe is proven but *oral* — nothing the kit plants warns
a second parallel session, and nothing checks the result.

## Idea

Codify the discipline in the kit, cheapest teeth first: (1) the planted
`control/README.md` gains a "parallel sessions, same lane" section — forward-only
reconcile on conflict (`git merge origin/main`, recommit a heartbeat that keeps BOTH
sides' facts, rerun the full preflight), never pre-write facts you don't have yet
(PR numbers, merge shas). (2) The status checker learns two advisories it can verify
mechanically from git history: a non-monotonic `updated:` stamp (newer commit,
older timestamp) and a heartbeat that *lost* a sibling's `last-shipped`/orders facts
across a merge (the reconcile-dropped-facts failure). (3) Optionally later: a
`bootstrap heartbeat` helper that regenerates the file from structured fields so
reconciliation is a field-merge instead of prose surgery. The one-writer rule stays
the contract; this covers the case the contract never named.

## Grounding

- Live collisions in this repo: PR #15 (merge commit 25b26b2, sibling fold recorded
  in its message), PR #12 heartbeat-number fixup (commit 7ce1607, "created as #12,
  heartbeat predicted #11"), and the timestamp-sequence note in `control/status.md`
  @ 03ae14d — all `menno420/idea-engine` git history.
- The rule with the blind spot: planted `control/README.md` § "The one rule that
  keeps it conflict-free" (two *Projects* never touch the same file — same-Project
  parallel sessions do).
- Continuous mode as the new normal: README § Coordination (owner ruling 2026-07-10,
  Q-0265) — every lane that adopts chained slices inherits this collision shape.

**Why now:** gen-2 lanes are arming standing wakes fleet-wide (manifest @
[`dc19b1e`](https://raw.githubusercontent.com/menno420/superbot/dc19b1e8a5443101a1a4cadf9a2f4e65133f49a3/docs/eap/fleet-manifest.md),
post-launch note) — parallel-session heartbeat collisions stop being an idea-engine
quirk the moment a second lane chains slices.

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/substrate-kit/be72c09ede329d01950ec764b409132a7eda007c/src/engine/templates/control-README.md.tmpl@be72c09 · fetched 2026-07-11T08:14Z
> **Grounding:** https://raw.githubusercontent.com/menno420/substrate-kit/be72c09ede329d01950ec764b409132a7eda007c/CHANGELOG.md@be72c09 · fetched 2026-07-11T08:14Z
> *(pin annotation: kit live HEAD via `git ls-remote` 2026-07-11T08:13:45Z = `be72c09`, read
> through a blobless clone at the pin. The coordinator's evidence sweep earlier this session
> read the same surfaces at `c970f0a` (the v1.10.0 wave close-out, committed 07:52:13Z);
> the `c970f0a..be72c09` delta is ONE control-only claim file — kit PR #186's in-flight
> v1.10.1 payload claim (gate tail-1 multi-card shadowing fix + doctrine emphasis
> normalization), disjoint from both heads in this batch — so both reads bind. ONE shared
> verify-first sweep serves this report and the sibling
> [`behind-stall-auto-updater-2026-07-10.md`](behind-stall-auto-updater-2026-07-10.md) —
> batched as TWO FULL batteries per the #132/#116 sibling-batteries precedent: the pair
> targets two DISTINCT kit surfaces (the planted control/README template + status checker
> here, the CI workflow set + enabler generator there) with different failure modes and
> different smallest slices.)*

Single-pass battery v0 (no panel trigger: not contested, not high-blast-radius — a routing
decision over a docs-only diff). **Verify-first, expiry-aware — the shared sweep:** newest
tag at the 08:13:45Z ls-remote is **v1.10.0** (NO v1.11.0), `CHANGELOG.md` @ `be72c09`
carries an **EMPTY `## [Unreleased]`** (immediately followed by `## [1.10.0] - 2026-07-11`)
— nothing staged, **neither head overtaken kit-side**. This head's specifics: the kit-planted
control/README template (`src/engine/templates/control-README.md.tmpl@fa20735`, the dist
embeds the same bytes) contains **NO reconcile guidance whatsoever** — repo-wide
`git grep -i reconcil` outside `dist/` hits only `.sessions/` retros plus the template's
one "reconciled as twins" aside about DUPLICATE ORDER EXECUTION (kit PRs #50/#51), and its
only "parallel sessions" sentence is the work-claims paragraph — collision *prevention*
(one-writer-per-file, per-lane heartbeats, claims). A same-lane parallel-session
`control/status.md` overwrite race is unaddressed: the capture's premise HOLDS at HEAD.
Grounding drift, one line: both heads in this batch pin superbot
`docs/eap/fleet-manifest.md@dc19b1e` for "why now" — that manifest is now a tombstone
(superseded 2026-07-11 by fleet-manager `docs/roster.md`); the premise (multiple lanes
running standing wakes/chained slices) survives, the pointer is historical.

**1. What is this really?** Codification of a proven-but-oral recipe at the seam that
planted the blind spot. The kit's whole collision model is *prevention* — one writer per
file across Projects, per-lane heartbeats, one-file-per-claim — and it never names the case
this repo lives daily under Q-0265 continuous chaining: N sibling branches on ONE lane,
each ending in a `control/status.md` overwrite. The working fix exists ONLY host-side:
this repo's root README § Landing conventions "Sibling landed mid-flight" bullet
(forward-only `git merge origin/main`, reconcile keeping both sides' facts — yours win for
your own fields — rerun preflight, push; proven PRs #10–#17, the monotonic-counter renumber
rule from PR #52's merge `516bdab`), lived ~20 times since — the `status.md` phase/orders
chains record the applications. Grooming rounds 3–4 encoded it HOST-side only; the kit-side
gap is exactly what this head routes.

**2. What is the possibility space?** Ascending: (i) a "parallel sessions, same lane"
section in the planted control/README — forward-only merge on conflict, keep-both-facts
reconcile, never pre-write facts you don't have (PR numbers, merge shas: the PR #12
`7ce1607` fixup is the measured cost of guessing); (ii) two checker advisories the status
checker can verify MECHANICALLY from git history: a non-monotonic `updated:` stamp (newer
commit, older wall-clock — the 21:40Z/22:25Z-stamps-on-20:31Z/20:44Z-commits sequence in
this repo's own history) and reconcile-dropped-facts (a sibling's `last-shipped`/orders
facts present in the merge parent but absent after the merge); (iii) a `bootstrap
heartbeat` field-merge helper that regenerates the file from structured fields (heavier;
later). Negative space: leaving it oral (measurably produced fixup commits and
hand-surgery here); any locking scheme (against the whole conflict-free design).

**3. What is the most advanced capability reachable by the simplest implementation?**
One template paragraph — pure docs, planted into every adopter at their next
`upgrade`/`adopt`, the same distribution the claims convention and the wake ritual already
ride — plus the stamp advisory, which is genuinely cheap: the checker already parses
declared `heartbeat_files`, and comparing the committed `updated:` value against the
file's own commit timestamps needs only the local git log. Together they convert this
repo's ~20-times-lived recipe into fleet default behavior at zero new machinery.

**4. What breaks it?** (a) The reconcile discipline itself is prose — "kept both sides'
facts" is not fully machine-checkable; the dropped-facts advisory needs a heuristic
(sibling fact present in merge parent, gone after) that can false-positive on legitimate
chain compaction, so advisory-first is a correctness requirement, matching the kit's own
observe-before-block doctrine. (b) The non-monotonic-stamp advisory has benign causes
(clock skew, a deliberate backdated correction) — advisory, never strict. (c) Template
growth vs the kit's lean-plant doctrine — answered by the same test the wake-ritual
sections passed: guidance that prevents a measured, repeated failure class earns template
bytes. (d) A lane that never runs parallel slices pays a paragraph of reading for nothing
— acceptable: the failure appears exactly when a second session appears, which is when
the paragraph is read.

**5. What does it unlock?** Safe continuous chaining for every lane that adopts the
Q-0265 mode (the collision stops being an idea-engine quirk the moment a second lane
chains slices — and pokemon-mod-lab already runs hourly fresh-session wakes); heartbeat
facts that stay trustworthy for downstream readers (fleet-manager's `gen_roster.py`
re-reads lane heartbeats every wake — a reconcile that silently drops a sibling's facts
poisons the roster); and it pattern-completes the kit-planted ritual family (wake ritual,
order claims, work claims) with the one case the contract never named.

**6. What does it depend on?** The kit lane (the template and the status checker are
kit-owned surfaces); this repo's README recipe as the reference implementation (stable
since PR #17, renumber rule since #52); git history availability at check time for the
two advisories (local, zero-network); nothing sim-shaped — no verdict gate.

**7. Which lane should build it?** substrate-kit, unambiguously: the planted
control/README and the status checker ship from the kit and regenerate at every adopter's
upgrade — codifying host-side (what this repo already did) provably does NOT propagate
(the gap this head exists to close). Joins the standing kit-lane fan-in bundle
(carveout-needles-config + enabler-card-status-guard-upstream(sharpened) +
kit-line-self-drift + this head + the behind-stall sibling) — one manager ORDER could
carry all five, same config/template/check seam family. Not idea-engine (this repo writes
only itself); routing = this section README's index + the heartbeat notes for the
manager's :30 sweep.

**8. What is the smallest shippable slice?** One kit PR: the "parallel sessions, same
lane" template section (forward-only merge · keep-both-facts reconcile · never pre-write
facts) + the non-monotonic-stamp advisory in the status checker + one test; the
dropped-facts advisory rides a second slice once the heuristic has a false-positive
story. Red/green reference exists in this repo's history: PR #15's mid-flight reconcile
(merge `25b26b2`) green, PR #12's pre-written number (`7ce1607`) red.

**Recommendation: park** — routed (kit lane build: planted control/README "parallel
sessions, same lane" section + two mechanical checker advisories; this repo's README
§ Landing conventions recipe is the working reference implementation) — premise verified
INTACT at live kit HEAD `be72c09` (no reconcile guidance in the planted template, whose
model is collision prevention only; no v1.11.0, `[Unreleased]` empty), and no simulator
question exists — template/checker features are proven by their own red/green (the #114
precedent for this same lane, reaffirmed by #132).
