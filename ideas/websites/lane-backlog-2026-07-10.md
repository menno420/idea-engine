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

## Re-pin (2026-07-12 fourth content re-harvest)

> **Grounding:** https://raw.githubusercontent.com/menno420/websites/8f9765483a7df57ce426e7d11d200f10b5495ed7/docs/ideas/backlog.md@8f97654 · fetched 2026-07-12T01:47Z
> *(pin annotation: HEAD verified unmoved across the whole sweep — `8f97654` at
> `git ls-remote` AND at the shallow-clone read, the same sha all three 2026-07-12
> P002-family probes (PRs #222/#225/#233) verified; the lane's continuous-mode
> chain is PARKED per its heartbeat, so no mid-harvest tail-move this time)*

The backlog's CONTENT moved **+194/-30 lines** (blob `0897a6f` → `e14bb15`) between
the third re-pin `c81ce76` and this one — sized by `check_harvest --bullet-drift`
and caught as a `CHANGED` finding by the `.harvest-pin.json` blob compare (second
live catch for the PR #115 leg). This delta also carries the section's **first NEW
standalone doc since the first harvest**:
[`merge-hold-at-head-2026-07-11.md`](merge-hold-at-head-2026-07-11.md) (+40/-0,
indexed as its own sibling entry this pass). At this re-pin the list holds
**14 captured, 31 built, 6 retired** (was 6/24/5 at `c81ce76`; counts here are
per-bullet state markers — `captured`/`built`/`retired` tokens plus `— shipped`
entries — same granularity as the prior sections). The delta is the lane's
close-out wave: continuous-mode slices 23–35 plus the archive-prep capture.
Flips and births vs the third re-pin's roster:

- **Two captured→Built:** the quality.yml every-card session-gate fold (slice 23,
  lane PR #120) and the nav manifest single source (slice 24, lane PR #122 —
  `app/nav.py` + membership test).
- **One captured bullet REPLACED in place — a first for this backlog** ("nothing
  deleted upstream" no longer holds at bullet granularity): the route-level clock
  freeze shipped as `app/clock.py` (lane PR #130) but got NO Built entry — the
  bullet was rewritten into its residue capture, "Port the clock-freeze pattern
  to botsite/dashboard if they grow age-measuring code" (premise-checked
  tripwire: neither service measures wall-clock ages today, verified by the
  lane's own grep).
- **Five born straight to Built:** fast-lane control gates in quality.yml
  (slice 25, PR #125); control-gate suite tests (slice 26, PR #127);
  snapshot-aging banner on the review site (review-site expansion, PRs
  #132/#141); the HANDOFF read-first line applied to the live CLAUDE.md via
  `upgrade --apply-docs` (rode the v1.12.0 kit upgrade, PR #146); dogfood the
  pickup convention (`pickup: 011 19m` seeded as writer #1, PR #150,
  live-verified on deployed /orders).
- **One born already-Retired:** the hand-kept-list audit sweep — executed as
  rung-5 upkeep (slice 32, PR #142), CLASS CLEAR verdict recorded in the bullet.
- **Eleven NEW captured bullets born** (the close-out wave sheds seeds fast):
  sanitized `guilds[]` list in superbot's `dashboard.json` (cross-lane export
  ask, from the #145 dry-run bot-management build; ALSO already flagged to the
  manager on the lane heartbeat @ `8f97654`); bake-time questions sync from
  GitHub issues (review-bake fourth generator); ⚑ owner-gated live answer-bot on
  the review site (model-key spend — deliberately not built); hand-merge the
  v1.12.0 boot-set-trim deltas into CONSTITUTION.md/AGENT_ORIENTATION.md (diffs
  retrievable via `git show 31cfd9f:.substrate/upgrade-report.md` — the v1.12.1
  upgrade overwrote the report); pin the current-state kit line to
  `substrate.config.json` with a test; chain-entry refresh as a close-out ender;
  verdict-inheritance guard for carried heartbeat watches (`watch: <claim> ·
  verified <ISO>`); provenance-token list to the kit lane (gate half — ONE token
  convention, not two half-matching spoof detectors); the clock-freeze port
  tripwire (the replacement bullet above); persist pickup latencies before
  claims clear (protocol-layer ask to the manager); and merge holds announced in
  a file at HEAD (the standalone-doc pair — see the sibling entry).
- **Survivors: the `lanes.json` manager ask, backlog low-water heartbeat signal,
  and #10 (meta.md state-line convention)** — #10 is now a
  three-consecutive-re-pin survivor.

**Format anomaly, observed not fixed (read-only lane):** the `## Built` heading
is GONE at this pin — all 31 built entries sit under `## Captured / planned`
(the heading was lost in the delta; the `## Retired` heading survives). State
tokens, not section headings, are what this index mirrors — same rule the third
re-pin set for retired-in-place — but a future `--bullet-drift` sizing that
groups by heading will over-count the captured section until the lane restores
it.

**Honesty note (citation split, same pattern as above):** states, slice numbers,
artifact names and verdicts are quoted from the backlog's own text at the pin;
every lane PR number in this section (#120, #122, #125, #127, #130, #132, #141,
#142, #145, #146, #150, #154) is inferred from the squash-commit subjects
`(#NN)` in the shallow clone's `git log c81ce76..8f97654` (51 commits) — no
front-matter in this delta carries a `shipped_pr:`.

## Groom (2026-07-12 fourth-re-pin reconciliation)

> **Grounding:** https://raw.githubusercontent.com/menno420/websites/8f9765483a7df57ce426e7d11d200f10b5495ed7/docs/ideas/backlog.md@8f97654 · re-fetched 2026-07-12 by this groom pass; fetched bytes hash to blob `e14bb15408b1f45de14eae72efe990024f0e548c` by `git hash-object` — the fourth re-pin's blob claim verified byte-level, zero clone. Prior-pin fetch (`…/c81ce76/docs/ideas/backlog.md`) hashes to `0897a6f6a63a6e452689d94edd5919131e732ae1`; `git diff --no-index --numstat` between the two fetches = **+194/-30**, matching the sizing above exactly.

**Tally reconciliation — CONFIRMED, 14 / 31 / 6, no correction.** Independent
per-bullet count at blob `e14bb15` (51 bullets total, every bullet classified):
**captured 14** (14 `captured` tokens, all under `## Captured / planned`);
**built 31** = 3 `built` tokens + 28 `— shipped` outcome entries; **retired 6**
= 3 retired-in-place `retired` tokens under `## Captured / planned` + 3
`— retired <date>` entries under `## Retired`. 14+31+6 = 51 ✓. One precision
fix to the fourth re-pin's stated granularity, number unchanged: it reads
"per-bullet state markers — `captured`/`built`/`retired` tokens plus
`— shipped` entries", but the three `## Retired`-section entries carry
`— retired <date>` outcome prose, NOT `retired` tokens — the literal stated
rule reproduces retired=3, not 6. The reproducible count rule is: **state
token OR em-dash outcome prose (`— shipped` / `— retired`), section headings
never** — recorded here so the next re-pin counts the same way.

**Pin-integrity notes (@ `8f97654`, blob `e14bb15` — both anomalies verified
against the prior blob `0897a6f`, observed not fixed; read-only lane, and the
lane chain is PARKED so restoration has no ETA):**

1. **`## Built` heading GONE.** Heading set at `e14bb15`: `## Captured /
   planned` (line 10) and `## Retired` (line 441) only. At `0897a6f` it was
   `## Captured / planned` (10) / `## Built` (90) / `## Retired` (277). All 31
   built entries now sit under `## Captured / planned`; any heading-grouped
   sizing over-counts the captured section until the lane restores the heading
   (the fourth re-pin's format-anomaly paragraph above, now pinned with line
   numbers on both blobs).
2. **One bullet REPLACED in place — the backlog's first bullet deletion.**
   "Route-level clock freeze for TestClient tests" · `captured` (line 80 @
   `0897a6f`) is absent at `e14bb15`; in its slot sits "Port the clock-freeze
   pattern to botsite/dashboard if they grow age-measuring code" · `captured`
   (line 188 @ `e14bb15`). The original shipped as `app/clock.py` (lane
   PR #130) with NO `— shipped` Built entry — the ship is invisible at this
   pin except through the replacement bullet's own source citation. Checker
   gap already seeded upstream of this groom: the harvest card's 💡
   (bullet-title-set diff for `--bullet-drift`,
   `.sessions/2026-07-12-websites-fourth-reharvest.md`).

**Indexing-rule check (decide-and-flag): the link-index-only rule HOLDS.** Of
the eleven new captured bullets at this pin, ten are lane work items or asks
whose routing half already exists outside this head: the `guilds[]` export ask
is flagged on the lane heartbeat @ `8f97654` AND deduped in the harvest card;
the provenance-token list says "flagged in the heartbeat notes" in its own
bullet text; the pickup-latency ask says "flag to the manager in the
heartbeat"; the merge-hold pair is already this section's standalone sibling
entry, probed and routed 2026-07-12 (PR #243, parked(routed — kit/manager
layer)); the rest are lane-internal chores/tripwires. **ONE candidate named,
not captured: the verdict-inheritance guard for carried heartbeat watches**
(`watch: <claim> · verified <ISO>`, line ~154 @ `e14bb15`) — the only new
bullet that is idea-shaped AND fleet-relevant beyond this lane (heartbeat
grammar is kit/manager territory and the `/fleet` badge half spans lanes) AND
carries no routing flag in its own text; with the lane PARKED, self-serve
never comes. Named for a future probe/mint slot — no idea file created this
pass, per the section's no-mass-capture convention.

**Next step: keep-as-index(re-pin cadence)** — tally exact at the pin,
anomalies recorded above, indexing rule holds with one named candidate; the
lane chain is PARKED at `8f97654`, so the next re-pin fires on the first
harvest sweep that finds HEAD moved. State stays `captured` — no disposition
change.
