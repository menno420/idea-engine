# Session — single-pass probe: websites fleet-program-pulse-feed

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-12 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session did

Single-pass probe (battery v0, no panel triggers) of
`ideas/websites/fleet-program-pulse-feed-2026-07-10.md` — the PROPOSAL 002 probe
Q2's unclaimed generalization (fleet-general git-history graph exporter →
committed schema-stamped `pulse.json` per repo + fleet rollup).

Verify-first at live lane HEAD `8f97654` (blobless clone + `ls-remote`,
2026-07-11T23:57Z): the capture's first-commit window HALF-CLOSED — the exporter
it wanted shaped at the story page's first commit already shipped SINGLE-REPO on
a page nobody predicted (`review/gen_snapshot.py` → committed
`review/data/snapshot.json`, rendered honest-degrade by `review/story.py`: the
capture's exact metric list, one repo). What remains genuinely missing is the
FLEET ROLLUP — no artifact anywhere produces program-wide history, re-verified by
sim-lab VERDICT 011 (owner-002 four-websites audit @ sim-lab HEAD `0622118`,
fetched raw this session: `/fleet` live-heartbeats-only; `review` NOT deployed —
owner-action; control-plane 25 dead in-content links). The story page itself
(phase 1) is UNROUTED at websites `control/inbox.md` @ `8f97654` (ORDERs 001–011,
none story-shaped) despite VERDICT 003 clearing phases 1–2 explicitly.

Verdict: **parked(build-direct — rides the story-page routing)**. No simulator
question exists (deterministic git-walk data, judgment/routing only); best
implementation found: parameterize the lane's proven `gen_snapshot.py` walk over
the fleet-manager `LANES` registry (+ the missing rollup, per-metric honest
absence), regenerating the review snapshot through the same code path as
behavior-identity proof — one lane-sized slice INSIDE the manager's PROPOSAL 002
phase-1 routing.

Files touched: the idea file (state flip + Sequence line + probe report append),
`ideas/websites/README.md` (index bullet echo), this card.

Coordinator-imposed deviations, declared: PR opened DRAFT (not READY) and never
self-merged — the coordinator lands it; NOTHING under `control/` written by this
slice (no claim file, no heartbeat overwrite) per its dispatch boundary —
section-collision risk noted instead of claimed, and the routing flag for the
manager (fold the fleet-general instruction into the story-page ORDER) is carried
by the probe report + this card, not a heartbeat line.

## Close-out (auto-drafted 2026-07-12 — edited per the README rule)

<!-- substrate:auto-draft -->

**Evidence (auto-draft corrected — the draft diffed against an unrelated base and
listed ~500 untouched files; the REAL diff of this branch vs `origin/main`
`a9b41f6` is):**

- ideas touched (2): `ideas/websites/fleet-program-pulse-feed-2026-07-10.md`
  (state flip + probe report append), `ideas/websites/README.md` (index echo)
- sessions touched (1): `.sessions/2026-07-12-fleet-program-pulse-feed-probe.md`
- code touched: none · control touched: none (dispatch boundary)
- git: branch `probe/fleet-program-pulse-feed` off main `a9b41f6`, born-red card
  first commit `32585a7`, probe+close-out commit follows; PR #222 (draft).
- verify: `python3 bootstrap.py check --strict` → green except the DESIGNED
  born-red hold pre-flip; green after this flip (recorded below before push).

**Judgment (the half only the session knows — resolve every slot):**

- Decisions made: no D-entry — probe verdict only (park, build-direct, rides the
  story-page routing). One report-format note: the recommendation token is the
  grammar's bare `park` with the build-direct reason in prose (the
  `check_ideas.py` LEGAL_RECOMMENDATION_RE only blesses `park(built-here…)` as a
  parenthesized form).
- Next session should know: the manager's story-page routing (PROPOSAL 002
  phases 1–2, cleared by VERDICT 003) is STILL unrouted at websites inbox @
  `8f97654` — when it routes, the fleet-general exporter instruction should ride
  it (one line: "lift `review/gen_snapshot.py` fleet-general, add the rollup").
  The `review` service deploy is a standing VERDICT 011 owner-action; until it
  deploys, the only shipped renderer of this data shape has no URL.

## 💡 Session idea

A capture whose whole value is "decide X at the FIRST commit of Y" should carry
`Sequence: before <Y's first commit>` at capture time — this one didn't, and its
window half-closed invisibly when the lane shipped the shape on a DIFFERENT page
(`review/gen_snapshot.py`) than the one the capture watched (the story page).
Expiry-aware probe ordering (README) only works when first-commit-shaped windows
are stamped as sequences; "watch the named artifact" misses the mechanism landing
under another name — the same invariant-not-artifact lesson as the #56 card, on
the capture side.

## ⟲ Previous-session review

PR #101 (venture-lab revenue-relay probe): its verify-first-at-live-lane-HEAD
discipline was adopted wholesale here and paid off identically — the lane had
moved past the capture's pin and the decisive fact (exporter already shipped) was
only visible in the live tree, not in any index. Its claim→re-read→build ritual
could NOT be adopted (this slice is barred from `control/`) — the workflow
improvement to carry forward: when a dispatch boundary forbids the claim ritual,
declare the collision risk in the born-red card's FIRST commit (done here) so
parallel sessions see the section is being worked even without a claim file.

- **📊 Model:** fable-5 · single-pass battery (no panel triggers) · docs-only
  probe slice (one probe append + state flip + index echo + card; no code)

## Handoff → next wake

The routing flag (fold fleet-general into the story-page ORDER) sits in the probe
report Q6/Q8 and this card — a coordinator heartbeat line would strengthen it
(this slice could not write one). Ripest related follow-up when the story page
routes: `story-bubble-texts-content-feed-2026-07-10.md` (captured — the same
page's narrative half, cheapest decided before the skeleton hardcodes chapter 1).
