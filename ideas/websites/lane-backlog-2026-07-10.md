# websites ideas backlog — the lane's single never-idle list — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/websites`
> **Grounding:** https://raw.githubusercontent.com/menno420/websites/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/backlog.md@144dfce · fetched 2026-07-10T22:33Z

**Canonical idea (stays in websites — indexed by link, never copied):**
[`menno420/websites → docs/ideas/backlog.md`](https://github.com/menno420/websites/blob/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/backlog.md)
— harvested 2026-07-10 by the websites lane-backlog harvest slice, pinned @ websites `144dfce`
([raw](https://raw.githubusercontent.com/menno420/websites/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/backlog.md)).

The websites lane's single backlog list — rung 3 of its never-idle work ladder
(`docs/project/project-instructions.md`), one bullet per idea with lifecycle states
`captured → planned → built → retired` per its `docs/ideas/README.md`, seeded
2026-07-10 from ideas previously scattered across session cards, the queue-state NEXT
list, and the retros, every bullet source-cited. At the pin it holds **13 captured
bullets, 6 built, 0 retired**; a substantial idea additionally gets one standalone
file in `docs/ideas/` ("one home per idea"), and four such files exist — each indexed
as its own sibling entry in this section.

**Captured bullets @ pin (indexed by link, one line each)** — all under the backlog's
[`## Captured / planned` heading](https://github.com/menno420/websites/blob/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/backlog.md#captured--planned-pick-highest-value-buildable-first):

1. `/fleet` manifest-parse freshness badge — surface manifest-sourced vs fallback (and its age) on the page itself, a likely template tweak.
2. Re-check closed-unmerged PR #9 branch — diff the still-live `claude/rework-dashboard` against `main`, salvage or retire its hardening explicitly.
3. Per-repo `?repo=` filter on the activity views — narrow the three `/activity` routes to one lane's stream over the cached timeline (own doc, sibling entry).
4. kit-version rollup on `/fleet` — summary header plus per-card badge over the already-parsed `kit:` line, pure presentation.
5. "Unseen orders?" badge on `/fleet` — flag a lane whose inbox last-commit is newer than its heartbeat `updated:` stamp.
6. `/queue.json` + manager round-trip check — a JSON owner-queue variant so a filed ask is machine-verifiable write → poll → confirm.
7. `scripts/wait-deploy.py` — post-merge sha-convergence poller turning the manual "merge = deploy" check into a deterministic PASS/FAIL.
8. Review-queue row auto-check — mechanically flag a merged PR whose runtime changed-line count owes a fleet review-queue row under the binding 50-line rule.
9. Stalled-claim aging on `/orders` — badge a claimed order whose `claimed-by:` stamp is older than the claim ritual's ~24h expiry.
10. `meta.md` state-line convention — ask the manager to standardize one `deployed:` line format in the forming `projects/` registry.
11. Own-heartbeat parse self-check in `quality` — run the repo's own `control/status.md` through the `/fleet` parsers at PR time so a malformed heartbeat fails before it renders wrong.
12. Ladder-rung telemetry — one `rung:` token per wake so orders-vs-self-generated work and backlog dryness become trends the manager can read.
13. Open-PR awareness at wake — list open PRs + PR-less unmerged `claude/*` branches before picking a work rung (own doc, sibling entry).

**Honesty note (the sim-worthy count claim):** the lane heartbeat @ the pin claims
"Q-0264 sim-worthy candidates now seven, all in docs/ideas/backlog.md (newest:
stalled-claim aging on /orders)" — @ `0cd08d2`/`b30b4f1` the same claim said six —
but no heartbeat write ever enumerates the full set. The four it once enumerated
(@ `44a9fa6`) included "healthcheck-failure auto-files an issue," which has NO
backlog bullet at the pin (grep for issue/alert: zero hits). This entry indexes the
count claim verbatim and does not assert a specific six (or seven).

## Re-pin (2026-07-11 content re-harvest)

> **Grounding:** https://raw.githubusercontent.com/menno420/websites/8c19e930f6dedd8b230538789a579cf1ce337f3c/docs/ideas/backlog.md@8c19e93 · fetched 2026-07-11T01:02Z (manifest row: behind)

The backlog's CONTENT moved 47/31 lines under an UNCHANGED filename set between the
first-harvest pin `144dfce` and HEAD `8c19e93` (`git diff --stat 144dfce..8c19e93 --
docs/ideas/`, blobless clone; `check_harvest` correctly reports the shape as
`HEAD MOVED (docs unchanged)` — the filename-set-only label the PR #49 honesty
correction documented). At the re-pin the list holds **10 captured, 9 built,
1 retired**. Bullet-lifecycle flips vs the numbered list above (original numbering
kept — the trail is the product):

- **#1 (`/fleet` manifest-parse freshness badge) → Retired** — the lane's slice-7
  fact-check found it already shipped as the PR #36 `lane_source` notice; the
  backlog's FIRST Retired entry.
- **#4 (kit-version rollup), #6 (`/queue.json` round-trip), #9 (stalled-claim
  aging) → Built** — one "fleet polish batch" slice (lane PR #81, slice 8).
- **#11 (own-heartbeat parse self-check) → Built** — lane PR #79 (slice 7); probed
  as [`own-heartbeat-parse-self-check-2026-07-11.md`](own-heartbeat-parse-self-check-2026-07-11.md),
  parked(overtaken-by-events).
- **Two NEW captured bullets born:** same-shape contract tests for
  `/orders.json` / `/queue.json` / `/projects.json` / `/reviews.json` (residue of
  the slice-9 `/fleet.json` shape-contract build, lane PR #83 — the pattern file
  now exists to copy), and a backlog fact-check pass before promoting a bullet
  (the lane's own harvest-side twin of this repo's lane-self-served lesson).
- **#8 (review-queue row auto-check)** stayed `captured` — probed 2026-07-11 as
  [`review-queue-row-auto-check-2026-07-11.md`](review-queue-row-auto-check-2026-07-11.md),
  parked(build-direct).
- Unchanged captured: #2, #3, #5, #7, #10, #12, #13.

**Cross-links (by link, never duplicated):** backlog #1 and #4 touch the same
`/fleet` surface named as a future sparkline consumer in
[`fleet-program-pulse-feed-2026-07-10.md`](fleet-program-pulse-feed-2026-07-10.md);
backlog #3 plus the shipped Atom feed relate to the `/activity` "living epilogue"
folded into that same pulse-feed capture; backlog #13 is the same failure class as
idea-engine's own claims ritual (`claims/README.md`) — the order-claim fix applied
to branches.

## Re-pin (2026-07-11 second content re-harvest)

> **Grounding:** https://raw.githubusercontent.com/menno420/websites/d8623642cabf068125dccb69ac775f2de0311104/docs/ideas/backlog.md@d862364 · fetched 2026-07-11T06:47Z

The backlog's CONTENT moved **+125/-54 lines** under an UNCHANGED filename set
between the first re-pin `8c19e93` and this one (`check_harvest --bullet-drift`
sizing, confirmed by the blobless-clone diff; the sizing run saw HEAD `ce2ec38`,
websites #102 — HEAD then moved once more to `d862364`, #103, whose `docs/ideas/`
tree is **byte-identical** to `ce2ec38`'s by tree diff, so this section pins the
newer sha with the same facts). At this re-pin the list holds **6 captured,
19 built, 3 retired** (was 10/9/1 at `8c19e93`). Bullet-lifecycle flips vs the
original numbering above (the trail is the product — nothing deleted upstream):

- **Seven captured→Built** (all merged 2026-07-11, the lane's continuous-mode
  slices 10–15):
  - **#3 (`?repo=` per-repo filter) → Built** — slice 10; sibling entry
    [`activity-per-repo-filter-2026-07-09.md`](activity-per-repo-filter-2026-07-09.md)
    flipped `historical(menno420/websites#86)` this pass (see its re-pin note for
    the front-matter-vs-commit-subject citation split).
  - **#13 (open-PR awareness at wake) → Built** — slice 12, shipped as
    `scripts/open_work.py` via websites PR #90 (front-matter `shipped_pr: 90`
    explicit); sibling entry
    [`open-pr-awareness-at-wake-2026-07-10.md`](open-pr-awareness-at-wake-2026-07-10.md)
    stays parked(build-direct) — the lane self-served the probe's recommended
    slice; forward-only outcome note appended there.
  - **#8 (review-queue row auto-check) → Built** — slice 14, shipped as
    `scripts/review_row_check.py` (commit `cbc87c8` subject cites lane PR #96);
    the lane self-served this one too, ~a day after this repo's probe
    [`review-queue-row-auto-check-2026-07-11.md`](review-queue-row-auto-check-2026-07-11.md)
    parked it build-direct — second confirmed instance of the lane-self-served
    lesson.
  - **#7 (`wait-deploy` sha-convergence poller) → Built** — slice 13, shipped as
    `scripts/wait_deploy.py` (commit `3f2ea62` cites lane PR #92).
  - **#12 (ladder-rung telemetry) → Built** — slice 12, same wake-tooling batch
    as #13 (commit `47b6168`, PR #90): optional `rung:` heartbeat line, in
    `fleet.KNOWN_KEYS`, rendered on /fleet.
  - **Re-pin new-born A (same-shape contract tests) → Built** — slice 11,
    `tests/test_json_contracts.py` pinning /orders.json /queue.json
    /projects.json /reviews.json key sets (commit `b16e23f` cites PR #88).
  - **Re-pin new-born B (backlog fact-check pass) → Built** — slice 15: the
    habit line lives in the lane's `docs/ideas/README.md` § Lifecycle and the
    first full pass ran the same slice (commit `d6b91c9` cites PR #99).
- **Two captured→Retired:**
  - **#5 ("unseen orders?" badge) → Retired** — slice 15 fact-check verdict:
    superseded by /orders, which computes actual per-repo outstanding orders
    (done/claimed/open/unknown), strictly stronger than the commit-time proxy.
  - **#2 (re-check PR #9 branch) → Retired** — slice 11 investigation: nothing
    to salvage; the branch's one unique hardening commit `a0b459f` is fully
    superseded on main by PR #10 (verified by diff upstream); branch left for a
    delete-rights sweep.
- **Five NEW captured bullets born:** flag to the kit lane that
  `upgrade --apply-docs` regenerates `.substrate/upgrade-report.md` WITHOUT the
  #156-mandated carve-out scan section (lived on the lane's v1.9.0 upgrade,
  PR #101); conveyor-health chips ("ideas: 3c/1b") on the readiness-board rows;
  a `tooling: pr-capable | ritual-only` capability token in the fired session's
  heartbeat; ask the manager for a generated `lanes.json` (the /fleet ↔
  fm-`gen_roster.py`-internals coupling broke once already — caught by cron
  run 2, fixed as the `ce2ec38` commit itself, websites #102); nav overflow
  guard (ten header links and growing).
- **Three Built entries not from captured bullets** (born straight to Built,
  slices 13–15): the relay-PR merge protocol on the bus (`control/README.md`
  doctrine "Landing other sessions' control-only work" — one WRITER, not one
  MERGER; generalized from relay PR #94 + the 04:03Z stranded-heartbeat rescue
  PR #98); `scripts/cron_slots.py` (5-field cron → next UTC fire slots, the
  `17 */6 * * *` incident pinned as a test); the `/ideas` `?state=` filter with
  per-repo lifecycle counts.
- **Survivor: #10 (meta.md state-line convention)** — the only pin-time captured
  bullet still captured.

**Honesty note (citation split, the PR #37 pattern):** "Built/Retired" states,
merge dates, artifact names and slice numbers above are quoted from the backlog's
own text at the pin; the LANE PR numbers are cited from upstream front-matter only
where it carries one (`open-pr-awareness`: `shipped_pr: 90`) — every other PR
number (#86, #88, #92, #96, #99, #98, #94, #101, #10, #102) is inferred from the
squash-commit subjects `(#NN)` in the blobless clone's `git log` at `d862364`,
plus the backlog/retired prose itself. `activity-per-repo-filter`'s front-matter
still says `shipped_pr: null` at this pin — its #86 comes from commit `580f5e0`'s
subject, stated as such in the sibling entry.

## Re-pin (2026-07-11 third content re-harvest)

> **Grounding:** https://raw.githubusercontent.com/menno420/websites/c81ce767ac336c7915a73de18ca2ddbb868efcc1/docs/ideas/backlog.md@c81ce76 · fetched 2026-07-11T09:50Z
> *(pin annotation: drift read at `02adf7c` — HEAD moved once more to `c81ce76` mid-harvest, a control-only heartbeat commit whose `docs/ideas/` tree is byte-identical by tree diff (backlog blob `0897a6f` at both), so the newer sha is pinned with the same facts, the #123 precedent)*

The backlog's CONTENT moved **+101/-27 lines** (blob `f1d93e3` → `0897a6f`) under
an UNCHANGED filename set between the second re-pin `d862364` and this one — sized
by `check_harvest --bullet-drift` and, for the first time, ALSO caught as a
`CHANGED` finding by the `.harvest-pin.json` blob compare the second re-pin
recorded (the PR #115 content-identity leg working live, zero extra network). The
PR #149 lint-bundle run sized this wake at HEAD `6663e6c`; HEAD moved to
`02adf7c` (lane PR #114) before this harvest — the drift was re-sized there. At
this re-pin the list holds **6 captured, 24 built, 5 retired** (was 6/19/3 at
`d862364`). Flips vs the second re-pin's roster (the
trail is the product — nothing deleted upstream):

- **Three captured→Built** (the lane's continuous-mode slices 17–19, all merged
  2026-07-11):
  - **Second-re-pin new-born (conveyor-health chips) → Built** — slice 17:
    per-repo lifecycle count chips on the readiness-board rows, deep-linked to
    the `/ideas` `?state=` filters over the same TTL cache (commit `e32be3d`
    cites lane PR #104).
  - **Second-re-pin new-born (`tooling:` capability token) → Built** — slice 18:
    optional `tooling: pr-capable | ritual-only` heartbeat line —
    `control/README.md` + `fleet.KNOWN_KEYS` + /fleet flags ritual-only fires as
    "cannot land work" (commit `383b773` cites lane PR #107).
  - **Second-re-pin new-born (nav overflow guard) → Built** — slice 19:
    secondary pages grouped under a no-JS `<details>` "more ▾" dropdown,
    top-level links 11 → 6 (commit `ddbbf27` cites lane PR #109).
- **One captured→Retired: the `upgrade --apply-docs` carve-out kit flag** —
  fixed upstream in kit #176; the lane verified the fix live on its own v1.10.0
  upgrade (PR #105: `--apply-docs` rode the upgrade invocation and the carve-out
  section survived natively). Retired-in-place: the bullet still sits under
  `## Captured / planned` with a `retired` state token — the state token, not
  the section heading, is what this index mirrors.
- **Two born straight to Built:**
  - **Board-row fleet chip** — slice 18: per-row heartbeat age/stale badge via
    `fleet.heartbeat_freshness`, board repos only, no guessed ages (commit
    `383b773`, lane PR #107 — same slice as the tooling token).
  - **Time-discipline guard for tests** — slice 21: `tests/test_time_discipline.py`
    AST-scans the suite for age-measuring calls without a frozen `now=`; first
    run caught 17 latent sites across 5 files (commit `02adf7c` cites lane
    PR #114 — the pin commit itself).
- **One born already-Retired: the model-doctrine idempotence kit flag** — born
  on the lane's v1.10.0 upgrade card (emphasis-sensitive phrase match appended a
  near-duplicate doctrine paragraph), fixed upstream in kit #187 / v1.10.1, and
  verified on the lane's own v1.10.1 upgrade (PR #113: `.sessions/README.md`
  byte-identical across the upgrade). Also retired-in-place under
  `## Captured / planned`.
- **Four NEW captured bullets born:** fold the kit v1.10.1 every-card
  session-gate loop into the live `quality.yml` lane (the folded step still
  derives the PR's card with `tail -1`, the multi-card shadowing shape v1.10.1
  fixed in the staged gate); a backlog low-water heartbeat signal
  (`backlog: low (N left)` below ~3 so the manager routes work before
  upkeep-dry); a nav manifest as the single `(href, label, group)` source for
  `base.html` + a membership test (born from the nav-overflow build — the
  guard's membership list currently exists twice by hand); a route-level clock
  freeze for TestClient tests (born from the time-discipline build — the static
  guard cannot see route tests exercising the real wall clock).
- **Survivors: the `lanes.json` manager ask + #10 (meta.md state-line
  convention)** — the only two second-re-pin captured bullets still captured;
  #10 is now a two-consecutive-re-pin survivor.

**Honesty note (citation split, same pattern as above):** states, slice numbers,
artifact names and retirement reasons are quoted from the backlog's own text at
the pin; every lane PR number in this section (#104, #105, #107, #109, #113,
#114, and upstream kit #176/#187) is inferred from the squash-commit subjects
`(#NN)` in the blobless clone's `git log d862364..02adf7c` or from the backlog
prose itself — no front-matter in this delta carries a `shipped_pr:`.
