# Session — harvest: websites + superbot re-pin (the sized queue, both legs one pass)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session is doing

Consuming BOTH legs of the heartbeat's SIZED NEXT-HARVEST QUEUE in one pass
(branch `harvest/websites-superbot-repin`; claims fast-laned first as PR #119,
merged `baac2ff`, branch cut from that HEAD):

- **websites leg** — content re-harvest at the `check_harvest --bullet-drift`
  sizing (backlog.md +125/-54, activity-per-repo-filter +4/-4,
  open-pr-awareness-at-wake +5/-5 since pin `8c19e93`; 0 new / 0 deleted, 5/5
  filenames): append a Re-pin section to the lane-backlog entry, mirror the two
  idea files' upstream front-matter outcomes forward-only, bump the section pin
  to live HEAD.
- **superbot leg** — two stale index gists only (fleet-manifest-freshness-checker
  +6/-1: the RETIRED 2026-07-11 superbot#1974 fact; reconcile-fleet-runtime-digest
  +7/-4: reframed off the retired checker onto the fm generated roster / lane
  heartbeats), pin bump `41899e1` → `58040c6`.
- **RITUAL ADDITION adopted** — `python3 scripts/check_harvest.py --write-pins`
  in the SAME session that re-pins, recording both sections' first
  `.harvest-pin.json` so CHANGED detection goes zero-extra-network from here on.

**📊 Model:** fable-5 · docs-only (idea-file appends + index gists + pins +
heartbeat + card; no code)

## 💡 Session idea

Equal diffstat is not content identity — treat it as a hypothesis, verify by tree
diff. This slice's websites leg was sized at HEAD `ce2ec38` (+125/-54 etc.) and by
work time HEAD was `d862364` with the SAME per-doc numbers; the honest move was
one `git diff <sized-sha> <live-sha> -- docs/ideas/` in the already-open blobless
clone (empty = byte-identical, pin the newer sha with the sized facts; non-empty =
re-size). That one cheap command is what lets a re-pin slice chase a moving
upstream without ever re-reading everything — and `--write-pins`' refusal to
record away from the pin is the guard that FORCES the re-verify instead of letting
a stale-sha pin slide through. Worth having as a named recipe in the harvest
ritual: size → re-verify identity at live HEAD → pin live → `--write-pins`, same
session.

## ⟲ Previous-session review

PR #116 (superbot-idle theme heads, the FIFTH section close): its batching logic
— probe heads whose remote pins COINCIDE, so one verify-first sweep amortizes
across verdicts — is exactly the shape of this slice, applied to harvest legs
instead of probe heads (both legs were sized by the same `check_harvest
--bullet-drift` run, so one session consumes both). Its heartbeat discipline
(⚑ needs-owner preserved verbatim, prior-slice PR stamped at demotion,
last-shipped never a guessed number) carries forward here. Its handoff named the
VERDICT 006 fan-in note as best-next-slice — the coordinator routed that to a
sibling (claim `fix/verdict-006-fanin`, PR #118, live at this branch's cut) and
dispatched this queue-consumption instead; both claims are disjoint from this
one's sections, shared-heartbeat overlap only. Its 💡 (batch by shared seams)
also predicted this slice's one surprise: the websites leg's live HEAD moved
AGAIN between sizing runs (`ce2ec38` → `d862364`) but the docs/ideas tree is
byte-identical between them — verified by tree diff, not assumed from equal
+N/-M numbers.

## Close-out

Both queue legs consumed, verified end-to-end:

- **websites** re-pinned `8c19e93` → `d862364` (full 40-hex in the section README
  per the pin grammar). The sizing run saw `ce2ec38` (websites #102); HEAD moved
  once more to `d862364` (#103, a control-only heartbeat commit) before the
  re-pin — `git diff ce2ec38..d862364 -- docs/ideas/` in the blobless clone came
  back EMPTY, so the section pins the newer sha with the sized facts (stated in
  the Re-pin section's Grounding paragraph). Lifecycle at the pin: 6 captured /
  19 built / 3 retired (was 10/9/1 @ `8c19e93`) — 7 captured→Built (slices
  10–15: #3 `?repo=` filter #86 · #13 open-PR awareness `open_work.py` #90 ·
  #8 review-row check `review_row_check.py` #96 · #7 `wait_deploy.py` #92 ·
  #12 `rung:` telemetry #90 · contract tests `test_json_contracts.py` #88 ·
  backlog fact-check pass #99), 2 captured→Retired (#5 unseen-orders badge
  superseded by /orders; #2 PR-#9 salvage — nothing to salvage, superseded by
  PR #10), 3 born-straight-to-Built (relay-PR merge protocol "one WRITER, not
  one MERGER"; `cron_slots.py`; `/ideas` `?state=` filter), 5 new-born captured
  (kit-lane `--apply-docs` carve-out flag · conveyor-health chips · `tooling:`
  heartbeat token · manager-generated `lanes.json` · nav overflow guard),
  survivor #10. Citation split honesty-noted (PR #37 pattern): lane PR numbers
  from squash subjects except open-pr-awareness' explicit `shipped_pr: 90`.
  `activity-per-repo-filter` flipped `historical(menno420/websites#86)`;
  `open-pr-awareness-at-wake` state UNTOUCHED (parked(build-direct) stands),
  forward-only upstream-outcome note appended, probe report untouched.
- **superbot** re-pinned `41899e1` → `58040c6`: two index gists refreshed only
  (checker RETIRED 2026-07-11 superbot#1974 per its Q-0105 kill-switch, badge
  stays historical; digest idea reframed onto the fm generated roster / lane
  heartbeats, badge stays captured) — both verified by full raw reads of the
  changed docs at `58040c6`.
- **RITUAL ADDITION adopted:** `check_harvest.py --write-pins` recorded both
  sections' first `.harvest-pin.json` (237 + 5 doc blob shas, each at its pin);
  the follow-up report-mode run returned `OK — 2 harvested section(s) fresh at
  canonical HEAD` with 0 changed — the CHANGED class is now armed at zero extra
  network for the next sweep.

Files touched: `ideas/websites/{README.md, lane-backlog-2026-07-10.md,
activity-per-repo-filter-2026-07-09.md, open-pr-awareness-at-wake-2026-07-10.md,
.harvest-pin.json}`, `ideas/superbot/{README.md, .harvest-pin.json}`, this card,
`control/status.md` (heartbeat; ⚑ OWNER-ACTION preserved verbatim), both claim
files deleted in-branch per convention. Claims fast-laned first as PR #119
(control-only), branch cut from `baac2ff`; siblings at cut: `upgrade/kit-v1.9.0`
(#117) and `fix/verdict-006-fanin` (#118) — disjoint scopes, shared-heartbeat
overlap only. Gate: `python3 scripts/preflight.py` all seven PASS +
`python3 bootstrap.py check --strict` exit 0 on the final tree before push.

## Handoff → next wake

Both harvested sections are FRESH at canonical HEAD with pin records — the
next `check_harvest` sizes honestly, CHANGED included. Ripest next: (a) the
five new-born websites captured bullets are un-probed heads (the manager-
generated `lanes.json` one is fleet-routing-shaped and pairs with the kit-lane
carve-out flag as relay candidates for the :30 sweep); (b) websites #10
(meta.md state-line convention) is the oldest surviving captured bullet — a
manager-relay one-liner, cheap to route; (c) the substrate-kit fleet-generic
half of open-pr-awareness (planted `control/README.md` convention) is still
un-built and now has TWO lane-self-served data points behind it.
