# Session — harvest slice: websites lane backlog (5 docs link-indexed, second SECTIONS lane)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-10 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## Scope

Second instance of the lane-backlog harvest (the PR #7/#26 recipe): link-index the
websites lane's own `docs/ideas/` docs — the backlog list plus its four standalone
idea files — into `ideas/websites/`, and register the section in
`scripts/check_harvest.py` SECTIONS (the one-line second-lane addition the heartbeat
has carried as a standing note since PR #22/#26). This is the exact follow-up the
PR #31 card's 💡 queued ("Lane-backlog harvest, second instance ready") and the
heartbeat names first in ripest-next. Ship as one merged-on-green PR.

## What this session did

- Claimed `ideas/websites/` + the SECTIONS row
  (`claims/harvest-websites-lane-backlog.md`, flat filename per claims/README;
  cleared in this branch's final commit). Inbox read first — verified still empty at
  origin/main HEAD `b251d56`; `claims/` held only its README at claim time. Note:
  main had moved past the recon's `f967969` (PRs #32–34 landed) — branch forked from
  `b251d56`.
- **Re-pinned the lane at harvest time (Q-0260 rails):** `git ls-remote` websites
  HEAD = `144dfced7282806efe778eaacb3565a13e35c2fa`, fetched 2026-07-10T22:33Z — TWO
  commits past PR #31's pin `0cd08d2` (`b30b4f1` = /orders #77, then `144dfce` =
  heartbeat overwrite #78). Diffed before gisting: `docs/ideas/` is byte-unchanged
  `b30b4f1 → 144dfce` (only `control/status.md` moved), so the recon's backlog read
  holds at the pin. All five canonical docs read in full at the pin (blobless clone,
  checkout `144dfce`) before writing gists.
- **5 new link-index entries** per the PR #7/#26 template (state line, Class/Target,
  blessed byte-form Grounding line with raw url@sha + fetch time, canonical link
  block, gist in this harvester's own words):
  - `lane-backlog-2026-07-10.md` → `docs/ideas/backlog.md` (captured · process) —
    the lane's single never-idle list, 13 captured + 6 built + 0 retired @ pin; plus
    a compact 13-line captured-bullets index (linked once to the backlog's
    `## Captured / planned` anchor), an HONESTY note on the heartbeat's un-enumerated
    sim-worthy count claim, and Cross-links to the sibling capture entries.
  - `activity-atom-feed-2026-07-09.md` → same-named doc,
    **historical(menno420/websites#41)** (product) — lane records it shipped
    (D-0025; merge commit `20559c6` "(#41)"). Front-matter honesty: its
    `shipped_pr:` field carries a branch name, so #41 is grounded in the merge
    commit + backlog Built bullet.
  - `activity-per-repo-filter-2026-07-09.md` → same-named doc (captured · product).
  - `open-pr-awareness-at-wake-2026-07-10.md` → same-named doc (captured · process).
  - `scheduled-healthcheck-workflow-2026-07-10.md` → same-named doc,
    **historical(menno420/websites#69)** (process) — front-matter records
    `state: built · shipped_pr: 69 · merged_date: 2026-07-10`.
  The 5 pre-existing capture entries and their index rows were left untouched
  (forward-only; no retrofit).
- **Honesty gap indexed, not asserted:** the lane heartbeat @ the pin claims "Q-0264
  sim-worthy candidates now seven, all in docs/ideas/backlog.md (newest:
  stalled-claim aging on /orders)" — it said SIX @ `0cd08d2`/`b30b4f1` (the count the
  PR #31 card and this repo's heartbeat carry) and has never enumerated the full
  set; the four it once enumerated (@ `44a9fa6`) included "healthcheck-failure
  auto-files an issue," which has NO backlog bullet at the pin. The backlog entry
  indexes the count claim verbatim and refuses to assert a specific six (or seven).
- **Section README:** harvest pin header added in the PIN_RE-parseable shape —
  pinned @ websites `144dfce` (`144dfced7282806efe778eaacb3565a13e35c2fa`) — with
  the ideas/superbot wording (per-entry `@ <sha>` annotations not retrofitted;
  entries mirror recorded outcomes). 5 new index rows in the exact
  `(canonical: websites `docs/ideas/<file>.md` @ `144dfce`)` row grammar.
- **`scripts/check_harvest.py`:** websites registered as the second SECTIONS lane —
  exactly the predicted one-line addition. Run this session (verbatim):

  ```
  $ python3 scripts/check_harvest.py
    (contents API 403 — falling back to blobless ls-tree)
  section ideas/superbot/README.md ← menno420/superbot/docs/ideas @ main
    HEAD MOVED:   menno420/superbot@main is 41899e1 (41899e15899516fda0093718ccb91a51961c5fe3), harvest pin is 655e0fe
    NEW upstream doc (not indexed): docs/ideas/games-theme-engine-website-first-2026-07-10.md
    summary: 236 indexed · 237 live upstream · 1 new · 0 unmarked · 0 deleted · HEAD moved
    (contents API 403 — falling back to blobless ls-tree)
  section ideas/websites/README.md ← menno420/websites/docs/ideas @ main
    HEAD UNMOVED: menno420/websites@main = harvest pin 144dfce
    summary: 5 indexed · 5 live upstream · 0 new · 0 unmarked · 0 deleted · HEAD unmoved
  check_harvest: DRIFT — 2 finding(s) across 2 section(s) (report-only; sizes the next re-harvest slice)
  ```

  **Websites section clean at ship time** (5 indexed · 5 live · 0 new/unmarked/
  deleted · HEAD unmoved). The 2 drift findings are the SUPERBOT section's —
  pre-existing, not this slice's scope, and now sized for the next re-harvest:
  superbot HEAD moved `655e0fe → 41899e1` with 1 NEW doc
  (`games-theme-engine-website-first-2026-07-10.md`). Recorded on the heartbeat.
- **Grounding pins fetched this session:** websites `144dfce` (ls-remote + blobless
  clone, 22:33Z); PR #41 attribution via the lane's merge commit `20559c6`; this
  repo's own tree at branch base `b251d56`.
- Landing per README § Landing conventions: PR READY never draft, merge-on-green;
  `python3 scripts/preflight.py` + `python3 bootstrap.py check --strict` green
  before push; heartbeat overwrite as the deliberate LAST content step; claim
  cleared in the final commit.

**📊 Model:** fable-5 · docs-plus-one-line (5 link-index files + section README +
card + heartbeat; one-line SECTIONS addition in `scripts/check_harvest.py`)

## 💡 Session idea

**check_harvest could suggest `historical()` re-badging from the lane's own Built
ledger:** the costliest judgment in this harvest was outcome-mirroring — deciding
`captured` vs `historical(#N)` required cross-reading each doc's front-matter
(`state:`/`shipped_pr:`), the backlog's `## Built` bullets, and (when the
front-matter carried a branch name instead of a PR number, as `activity-atom-feed`'s
does) the lane's merge commits. The checker already fetches the canonical tree; a
pass that parses the canonical backlog's Built section + each doc's front-matter
`state:` and diffs against the index rows' states would flag "entry says captured,
lane says built" as a fourth drift class (RE-BADGE) — catching the staleness that
NEW/DELETED can't see: an already-indexed idea whose upstream outcome changed after
harvest. Pairs with the PR #26 card's `--emit-entries` 💡 (one emits new entries,
this one re-badges old ones).

## ⟲ Previous-session review

PR #31's card (websites first capture batch; the previous websites-section session)
promised, all verified on this tree at branch base `b251d56`: the 4 capture files
exist in `ideas/websites/` (`fleet-program-pulse-feed`,
`public-leaderboards-committed-feed`, `contract-driven-explorer-facets`,
`story-bubble-texts-content-feed`, each with a blessed Grounding pin) with their 4
index rows beside the untouched sim-ready head; its claim
`claims/batch-websites-follow-on-captures.md` is cleared (`claims/` holds only its
README); it appended NO outbox entry and NO probe (earn-rate bar held); and its 💡
IS exactly this slice — "Lane-backlog harvest, second instance ready," naming
`docs/ideas/backlog.md`, the six self-flagged candidates, and the SECTIONS
one-line anchor — consumed as written, including its recorded drop of this work
from the capture batch ("a harvest slice, not a capture … left as the section's
ripest follow-up slice"). Its handoff's probe-priority (leaderboards first,
explorer-facets second) stands untouched by this slice. Honest gap found while
consuming it: the card's "SIX Q-0264 sim-worthy candidates" pin aged within hours —
the lane heartbeat @ this slice's pin `144dfce` claims SEVEN, still un-enumerated
(indexed verbatim with an honesty note on the backlog entry, per the recon's
recommendation not to assert a specific set). Consumed recipes: PR #26's harvest
recipe (pin shape, row grammar, outcome-mirroring) and the heartbeat's ls-remote +
blobless-clone capability pair, both friction-free.

## Handoff → next wake

Inbox first, as always. `ideas/websites/` is now at full depth: 5 owner/probe-side
captures + 5 lane-born link-index entries, section pinned @ `144dfce`, second
SECTIONS lane live in `check_harvest.py`. Ripest follow-ups:

- **Superbot re-harvest, sized this session:** HEAD `655e0fe → 41899e1`, 1 NEW doc
  (`games-theme-engine-website-first-2026-07-10.md`) — a small PR #26-shaped slice.
- **Ripest probe candidates from the harvested backlog:** (1) open-PR-awareness-
  at-wake — mechanical scope, two lived failures, cross-lane relevance (this repo's
  claims ritual is the same class), and one of the lane's own flagged sim-worthy
  heads; (2) own-heartbeat parse self-check — dogfood pair to shipped heartbeat
  enrichment, pure `quality` addition with the parsers already live; (3)
  review-queue row auto-check — the documented 116-PRs/zero-rows failure state
  plus the lane's own #67/#72/#75/#77 qualifying unflagged makes the evidence
  question concrete.
- Standing next-slices from the heartbeat otherwise unchanged (public-leaderboards
  probe, freshest-wins one-liner, kit v1.7.0→v1.7.1 self-upgrade,
  `--emit-entries`, and now the RE-BADGE 💡 above).
