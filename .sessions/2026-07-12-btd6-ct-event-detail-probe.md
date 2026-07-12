# Session — single-pass probe: superbot btd6-ct-event-detail-relics-map

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-12 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session did

Single-pass probe (battery v0, no panel triggers) of
`ideas/superbot/btd6-ct-event-detail-relics-map-2026-07-10.md` — fifth-mint
slot #4, briefed as the WEAKEST slot (no window pressure, month-old pin
`fd638e3`, first to yield to the alternate). The briefed question was the
STALENESS check at live superbot HEAD: is the CT event-detail drill-down
still thin vs race/boss/odyssey, and does the relics/map data path exist?

Verify-first, live, tree-scanned: superbot HEAD S resolved by
`git ls-remote` this session = `1ecc21138fe0a1eb672d03b66bd319164c29d55f`
(the SAME S the #228/#232/#238 probes measured; canonical doc
byte-identical `fd638e3`→S, md5 `9f605c35…` both), inspected via a depth-1
clone at S, then deepened `--shallow-since=2026-06-16` so lane-growth was
answered from git history. The decisive facts: (a) the gap is STILL OPEN —
`rg -c "relic|ct_map|btd6_ct"` over `live_events_view.py` +
`_event_helpers.py` = zero hits, and `build_event_detail_embed`
(`_builders.py:1333-1483`) has no CT branch (a live CT event renders
name+window only); (b) the detail-surface files were last touched by
`05c8621b` (#953 itself, 2026-06-16) — the fast-shipping lane grew CT
leaderboard/group surfaces, not the event detail; (c) the relics/map data
path exists END-TO-END — NK sources `nk_btd6_ct` ("/ct") +
`nk_btd6_ct_tiles` ("/ct/:ctID/tiles") registered
(`migrations/040_btd6_sources.sql:154-168`), parser
`services/parsers/ninjakiwi_ct.py`, ingestion chain parent→tiles
(`btd6_ingestion_service.py:344-349`), query `get_ct_tiles`
(`btd6_live_query_service.py:894-936`), renderer `build_ct_map_file`
(`ct_map_view.py:74`) with the Pillow-absent `(None, ct_id)` degrade
built in; (d) `EventDetailView` is a `HubView` (`live_events_view.py:486`)
so the doc's Option-1 button is pure view wiring via `safe_edit`
(`interaction_helpers.py:259`).

Verdict: **parked(routed — superbot lane build-direct)** — the briefed
"assume the pin lies" fear inverted: the month-old pin tells the truth,
the premise is STRONGER at HEAD (everything reusable, zero new plumbing),
and the canonical doc's own disposition already routes it ("promote to a
focused PR when the BTD6 lane has capacity"). Nothing sim-shaped
(deterministic drill-down kill-test, no parameter space); NO outbox
proposal, outbox tail unchanged. **Fifth-mint slot #4 CONSUMED — the
FIRST ALTERNATE (superbot-next/known-risks-fix-coupling-checker-doctrine)
inherits the slot per the mint's own "first to yield" flag.**

HONEST NULL, flagged for the coordinator: the brief's dedup claim ("probe
#232 consumed btd6-ct-event-detail as 'visible product win, zero
freeze/pace trigger'") is NOT in the tree — repo-wide greps plus
`git log --all -S "freeze/pace"` and `-S "btd6-ct-event-detail" --
control/status.md` find no such line (the #232 file/card contain zero
btd6-ct mentions; the head's only ledger mention is fifth-mint slot 4 @
`d68ac2d`). This was the head's FIRST probe.

**Section-collision flag (dispatch boundary — no claim file):** this slice is
barred from `control/`, so no `control/claims/` entry exists; this born-red
first commit carries the `ideas/superbot/` collision flag per the PR
#222/#225/#226/#228/#232/#238 workflow convention.

## Close-out

**Evidence (hand-written):**

- ideas touched (2): `ideas/superbot/btd6-ct-event-detail-relics-map-2026-07-10.md`
  (state flip captured→parked(routed — superbot lane build-direct…) + probe
  report append), `ideas/superbot/README.md` (index bullet re-badge +
  byte-identity note per the PR #189/#192 card duties)
- sessions touched (1): `.sessions/2026-07-12-btd6-ct-event-detail-probe.md`
- code touched: none · control touched: none (dispatch boundary)
- git: branch `probe/btd6-ct-event-detail` off main `2aa1b2f`,
  born-red card first commit `b163ae9`, probe+close-out commit follows;
  draft PR flipped ready on green per dispatch instructions.
- verify: `python3 bootstrap.py check --strict` and
  `python3 scripts/preflight.py` run before push (results in the PR).

**Judgment (the half only the session knows):**

- Decisions made: no D-entry — probe verdict only (park, routed
  build-direct). One pricing call, declared: NOT filed sim-ready despite a
  verified-true premise — there is no question a simulator can settle that
  one lane CI run + one manual CT drill-down doesn't settle cheaper; the
  doc's own disposition line already names the route, so the probe's whole
  value-add was the live verification + the Q4 build notes (Pillow text
  fallback mandatory; button on the view, never the shared builder).
- Next session should know: the "weakest slot" flag and this park are
  compatible — weakest meant lowest urgency, not weakest premise; the slot
  yields to the alternate exactly as the mint predicted, but the head
  leaves with a BUILD-READY spec, not a rejection.

## 💡 Session idea

A mint that flags a slot "first to yield to the alternate" should also
pre-name what evidence would UPHOLD the slot instead — this probe found
the premise verified-true yet still consumed the slot as predicted, and
the only reason that isn't confusing to the next reader is prose in two
places; a one-line "yields unless X" on the mint would make slot-succession
mechanical.

## ⟲ Previous-session review

PR #238 (channel-deployed-component-menu probe): adopted — (a) its same-S
carry discipline paid a third time (S still `1ecc211` at this session's
ls-remote; the #228 without-pillow finding on `ct_map_render` carried
straight into Q4(d)); (b) the born-red-card collision flag (no claim file
under the dispatch boundary) used verbatim; (c) its md5 byte-identity
check on the canonical doc reused (clone-vs-raw cross-check). Deviation
from its shape, declared: this probe deepened the clone with
`--shallow-since` instead of trusting tree-state alone — "did the lane
grow this since capture" is a history question, and the log answer
(`05c8621b` last-touch) was cheaper and harder evidence than any grep.

- **📊 Model:** fable-5 · single-pass battery (no panel triggers) ·
  docs-only probe slice (one probe append + state flip + index re-badge +
  card; no code)

## Handoff → next wake

Fifth-mint slot #4 consumed → the FIRST ALTERNATE
(`superbot-next/known-risks-fix-coupling-checker-doctrine`) inherits the
slot — the coordinator's next probe dispatch should target it. Build-flip
trigger on future superbot re-pins: a CT branch appearing in
`build_event_detail_embed` or a `ct_map`/`relic` reference in
`live_events_view.py` means the lane self-served — flip this head toward
historical. Guard recipe:
`git ls-remote https://github.com/menno420/superbot.git main`, then
`rg -n "relic|ct_map|btd6_ct" disbot/views/btd6/live_events_view.py
disbot/cogs/btd6/_event_helpers.py` at the new SHA; test target
`python3 scripts/preflight.py` here.
