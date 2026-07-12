# Session — single-pass probe: websites merge-hold-at-head

> **Status:** `complete`

- **📊 Model:** fable-5 · single-pass battery (no panel triggers) · docs-only
  probe slice (one probe append + state flip + index re-badge + card; no code)

## What this session did

Single-pass probe (battery v0, no panel triggers) of
`ideas/websites/merge-hold-at-head-2026-07-11.md` — fifth-mint TOP-5 #5
(ledger @ `d68ac2d`), harvested 2026-07-12 by PR #236 from the websites lane
(canonical @ websites `8f97654`, born in the archive-prep capture, websites
PR #154). Process-class head: represent repo-wide merge holds as
`control/claims/HOLD-<scope>.md` files at origin/main HEAD so zero-context
routine wakes see the hold mechanically.

Verify-first, live: websites HEAD verified **equal to the harvest pin**
`8f9765483a7df57ce426e7d11d200f10b5495ed7` (`git ls-remote` + read-only
blobless clone this session — the lane is PARKED, zero drift). Decisive
findings: **not self-served** (`control/claims/` at websites HEAD is
README-only, no hold ritual anywhere, `git log ebef8bd..HEAD -- control/README.md
docs/project/` empty); **the incident is transport-real** (#143 `ebef8bd` and
#146 `31cfd9f` in main history — the two mid-hold merges; #148 `7d1ff88`;
#150 `9775697` "hold window resolved"; #141 owner-merged later as `0545906`;
retro `docs/retro/archive-ready-2026-07-11.md` §3 fetched at the pin records
the failure verbatim). One citation reported-not-verified, declared in the
report: PR #148's BODY (`mergeable_state: behind` quote) — GitHub MCP is
scoped to idea-engine (access-denied captured) and `api.github.com` is walled
(`docs/CAPABILITIES.md:53`); corroborated by the retro's quote + the verified
merge sequence.

The probe's decisive Q4 (the sticky-note test): **no current merge automation
reads `claims/`** — GitHub auto-merge armed at PR creation fires on green with
no agent in the loop (and a hold landing AFTER a sibling's checks green does
not re-trigger them); the kit gate workflow is the enforcement hook that
blocks auto-merge but reads cards + inbox purity only; the kit claim checker
would ALREADY parse a grammar-conformant `HOLD-*.md` today (verified against
`bootstrap.py` `_work_claim_findings`) but its >72h `claims-stale` wording
prescribes prune-on-sight — inverted advice for a legitimate long hold.

Verdict: **parked(routed — kit/manager layer)** — one substrate-kit four-touch
slice: (1) HOLD grammar + `lift-when:` in the planted claims README, (2) the
checker's HOLD stale-wording carve-out, (3) one before-merging ritual line in
the planted `control/README.md`, (4) a hold-aware gate-workflow step so armed
auto-merge is machine-blocked. Nothing sim-shaped (deterministic red/green
kill-test: scratch adopter + `HOLD-main.md` + armed sibling PR — one CI run
settles it). No outbox proposal; routing is forced through the manager sweep
because the canonical lane is PARKED (self-serve never comes) and idea-engine
writes only itself (Q-0260).

Dedup swept (`rg` over hold/claim/lock/merge-queue/auto-merge/branch-protection,
kit files excluded): `control/claims/README.md` grammar — substrate not
duplicate (HOLD = new negative-claim CLASS); kit `session-card-hold` /
`BORN_RED_HOLD_MESSAGE` (`bootstrap.py:1759`) — nearest miss, per-PR own-card
hold, its gate step is the enforcement PATTERN to copy;
`open-pr-awareness-at-wake` (parked, lane self-served websites#90) — the
discovery dual; its un-built substrate-kit fleet-generic half is the SAME
planted-README surface → **bundling finding for the manager: one kit slice,
both ritual lines**; `fleet/open-work-preflight-sweep` — same wake-sweep
family; `fleet/coordinator-archive-handoff-ceremony` (the fifth mint's
rejected kit-lane bundle candidate) — overlapping routing target, zero
mechanism overlap, hold lifecycle could ride the same kit doc bundle;
`fleet/gate-ritual-convergence` — supplies the make-ritual-merge-blocking
doctrine; superbot-idle sim-hold queue states — different object. No
duplicate idea file.

**Section-collision flag (dispatch boundary — no claim file):** this slice is
barred from `control/`, so no `control/claims/` entry exists; this card's
born-red first commit carried the `ideas/websites/` collision flag per the
PR #222/#225/#226/#228 workflow convention.

## Close-out

**Evidence:**

- ideas touched (2): `ideas/websites/merge-hold-at-head-2026-07-11.md`
  (state flip captured→parked(routed — kit/manager layer…) + probe report v0
  append), `ideas/websites/README.md` (index bullet re-badge per the PR #192
  card convention)
- sessions touched (1): `.sessions/2026-07-12-merge-hold-at-head-probe.md`
- code touched: none · control touched: none (dispatch boundary; the
  manager-sweep flag rides the idea file + this card, not a heartbeat line)
- git: branch `probe/merge-hold-at-head` off main `2aa1b2f`, born-red card
  first commit `d7f988d`, probe+close-out commit follows; draft PR flipped
  ready per dispatch instructions — parked READY, never merged by this slice,
  auto-merge never armed by this slice.
- verify: `python3 bootstrap.py check --strict` and
  `python3 scripts/preflight.py` run before push (results in the PR).

**Judgment (the half only the session knows):**

- Decisions made: no D-entry — probe verdict only (park routed, kit/manager
  layer). One framing call, declared: the retro shows post-hold merges
  (#147/#148/#150/#145) kept knocking #141 behind BY DESIGN after the hold
  resolved — the probe scopes the HOLD file to bounded windows and names the
  drift-watchdog as its standing complement for indefinite owner-click waits,
  rather than letting the capture's framing imply holds replace the watchdog.
- Next session should know: the routed slice's spec lives in the probe's Q8
  (four touches, kit-side). Guard recipe for the checker carve-out:
  `_work_claim_findings` in the kit's engine (local copy `bootstrap.py`, grep
  the stem `claims-stale`) — the finding text "likely an orphan; delete it"
  must fork on the `HOLD-` filename prefix; test target: the kit's
  `tests/test_grammar.py` sibling for claim findings. The armed-PR race
  (Q4.i) is the part no doc line fixes — any future sim-shaped question would
  live there, but the gate step + hold-start sweep answer it deterministically.

## 💡 Session idea

The kit claim checker's finding TEXTS hard-code one response verb for the
whole directory ("delete it" on stale) — correct for work-claims, actively
inverted for any long-lived coordination file the directory later hosts (this
probe's HOLD class is the first live instance). Cheap kit fix with fleet-wide
reach: finding messages should key their prescribed VERB on the file's class
(filename prefix), not on the directory — otherwise every new claim class
shipped into `control/claims/` inherits advice written for a different
lifecycle, and a compliant agent executes the wrong verb confidently.
Dedup-grepped: `fleet/lint-bundle` (checker wording hygiene, this repo's
checkers not the kit's claim scan) and the fifth-mint alternate
known-risks-fix-coupling (checker-doctrine coupling, other repo) are nearest;
neither covers response-verb-per-class in kit finding texts.

## ⟲ Previous-session review

PR #240 (registry-shrinkage-sentinel probe): adopted wholesale — (a) its
live-HEAD-first discipline paid differently here: `ls-remote` showed the
websites pin IS live HEAD (lane PARKED), which upgraded every harvest citation
to a HEAD citation for free AND supplied the routing argument (self-serve
never comes); (b) the born-red-card collision flag under the dispatch boundary
used verbatim; (c) its "verify the substance, rule on the substance" pattern
applied to the canonical doc's "stale machinery for free" claim — verified
TRUE with a wrinkle (the stale nag exists but its wording prescribes deleting
the hold), which became the probe's Q4.iv and a session idea. Its card was
hand-written from the first commit; so was this one.

## Handoff → next wake

This consumes the fifth mint's #5 slot (websites/merge-hold-at-head). Facts
for the coordinator's heartbeat: verdict parked(routed — kit/manager layer),
manager-sweep flag = ONE substrate-kit four-touch slice (probe Q8) with a
bundling recommendation (carry open-pr-awareness' un-built fleet-generic
wake-sweep paragraph in the same planted-README edit); no outbox proposal;
the websites section index re-badged. Remaining fifth-mint heads: #3
oracle-copy consumed (#239), #2 registry-sentinel consumed (#240), #1
menu-primitive consumed (#238) — #4 btd6-ct-event-detail-relics-map is the
last unconsumed slot per the ledger @ `d68ac2d`.
