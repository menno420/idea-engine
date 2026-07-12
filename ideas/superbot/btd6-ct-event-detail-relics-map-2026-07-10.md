# Idea — enrich the BTD6 CT event detail with relics + the hex map — link index

> **State:** parked(routed — superbot lane build-direct: the premise VERIFIED STILL TRUE at live S `1ecc211` — the CT event detail renders name+window only (`build_event_detail_embed` `_builders.py:1333` has zero relic/map/`btd6_ct` branch; the detail surface files untouched since #953 itself, 2026-06-16), while EVERY ingredient the canonical doc names is live and reusable (`get_ct_tiles` `btd6_live_query_service.py:894`, `build_ct_map_file` `ct_map_view.py:74`, NK `/ct` + `/ct/:ctID/tiles` sources + parser + ingestion chain) — the doc's own Option-1 button is a small in-lane UX PR, its own disposition already says "promote to a focused PR when the BTD6 lane has capacity", nothing sim-shaped; slot #4 of the fifth mint is CONSUMED — the alternate (superbot-next/known-risks-fix-coupling-checker-doctrine) inherits the slot; probe 2026-07-12)
> **Class:** product · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/btd6-ct-event-detail-relics-map-2026-06-16.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/btd6-ct-event-detail-relics-map-2026-06-16.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/btd6-ct-event-detail-relics-map-2026-06-16.md)).

Enrich the BTD6 Contested Territory event detail with relics and the hex map — the drill-down is rich for race/boss/odyssey (which have tower-restriction metadata) but thin for CT.

## Probe report (v0, 2026-07-12)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/1ecc21138fe0a1eb672d03b66bd319164c29d55f/docs/ideas/btd6-ct-event-detail-relics-map-2026-06-16.md@1ecc211 · fetched 2026-07-12T02:29Z
> *(pin annotation: S = superbot live HEAD by `git ls-remote` this session =
> `1ecc21138fe0a1eb672d03b66bd319164c29d55f` — the SAME S the #228/#232/#238
> probes measured. The canonical doc is byte-identical `fd638e3`→S (md5
> `9f605c35…` both, clone-vs-raw cross-check), status still `ideas` — the
> harvest pin content IS the HEAD content. Tree evidence below read from a
> depth-1 clone AT S, then deepened `--shallow-since=2026-06-16` so the
> "did the lane grow this since capture" question is answered from git
> history, not guessed.)*

> Single-pass battery (panel not escalated: docs-only disposition,
> reversible park, no security/data/spend/public blast radius — README
> § probe battery). Verify-first at live S, tree-scanned not doc-trusted:
> stem-matched greps (`relic|ct_map|btd6_ct`, `build_ct_map_file|
> get_ct_tiles|build_ct_browser_embed`, `nk_btd6_ct`, `safe_edit`) over the
> depth-1 clone, then body-reads of `disbot/cogs/btd6/_builders.py`
> (`build_event_detail_embed` :1333-1483), `disbot/views/btd6/
> live_events_view.py`, `disbot/cogs/btd6/_event_helpers.py`,
> `disbot/views/btd6/ct_map_view.py`, `disbot/services/
> btd6_live_query_service.py` :874-981, `disbot/services/
> btd6_ingestion_service.py` :344, `disbot/migrations/040_btd6_sources.sql`
> :154-168, plus `git log --since=2026-06-16` over the four named surface
> files. Cross-lane ledger read (PR #180 card): superbot has no
> `docs/decisions.md` (re-confirmed carrying from the #228 probe's
> byte-unchanged read — 8 ADRs under `docs/decisions/`, none CT-shaped by
> title).

**1. What is this really?** A small/safe UX follow-up to superbot #953
(captured 2026-06-16 while building it): #953 made BTD6 Live Events
current-event-first with a rich per-event drill-down — rich for
race/boss/odyssey because those kinds carry `_towers` restriction metadata,
but a live CT event drills into **name + window only**, exactly the
"doesn't show all the info" class the owner flagged. Meanwhile the rich CT
data already renders in a SIBLING view (the panel's 🗺️ CT button:
`build_ct_browser_embed` + `build_ct_map_file`) — the detail just doesn't
connect to it. Who for: server users drilling into a live CT event from
the overview (CT WAS live in the owner's recording — a real, reachable
gap, per the doc's own capture note).

**2. What is the possibility space?** The doc's two options: (1) a
CT-gated "🗺️ Map & relics" button on the event detail that edits in place
to the rendered hex map + relic summary, with ↩ back; (2) an inline
"top relics" text field from `get_ct_tiles(ct_id, relics_only=True)`.
Wider (unclaimed by the capture): per-kind detail enrichers as a pattern
(each event kind gets its kind-specific deep block); relic-search from the
detail (`find_relic_locations` already exists at
`btd6_live_query_service.py:964`); CT team/group standings on the detail
(the `ct_group_flow.py` / `btd6_ct_team_service.py` surface is
leaderboard-shaped, adjacent not overlapping).

**3. What is the most advanced capability reachable by the simplest
implementation?** Option 1 at near-zero plumbing: `EventDetailView` is a
`HubView` (`live_events_view.py:486`) so a button slots natively; gate on
`vm.entity_kind == "btd6_ct"` (the VM already carries `entity_kind`,
:167/:174/:180); the button calls `build_ct_map_file(ct_id)`
(`ct_map_view.py:74` — already accepts a specific `ct_id`, already returns
`(None, ct_id)` for graceful degrade) and attaches via `safe_edit`
(`disbot/core/runtime/interaction_helpers.py:259`) + a relic summary from
`get_ct_tiles(ct_id, relics_only=True)`. Zero new data plumbing, zero new
render code — the entire slice is view wiring.

**4. What breaks it? (assumptions verified — the load-bearing answer.)**
The briefed fear was the inverse of the truth: the month-old pin does NOT
lie — measured at S `1ecc211`, the gap is STILL OPEN and the premise
STRONGER than a doc-trust read would risk. (a) **Current CT render
surface:** `rg -c "relic|ct_map|btd6_ct"` over
`disbot/views/btd6/live_events_view.py` + `disbot/cogs/btd6/
_event_helpers.py` returns ZERO hits, and `build_event_detail_embed`
(`_builders.py:1333-1483`) renders window/scores/rules/disabled-flags/
`_towers` restrictions with NO kind-specific CT branch — a live CT event
still shows name + window (+ score counts when indexed). (b) **Lane
growth since capture:** `git log --since=2026-06-16` over
`live_events_view.py`, `_event_helpers.py`, `_builders.py`,
`ct_map_view.py`, `btd6_live_query_service.py` shows the detail-surface
files last touched by `05c8621b` (#953 itself, 2026-06-16) — the
fast-shipping lane (sibling probe #238's finding) grew CT
leaderboard/group surfaces, not the event detail. (c) **Upstream data
source exists end-to-end:** the NK API client registers `nk_btd6_ct`
("Ninja Kiwi BTD6 /ct") and `nk_btd6_ct_tiles` ("/ct/:ctID/tiles") plus CT
leaderboard sources (`migrations/040_btd6_sources.sql:154-168`), the
parser is `services/parsers/ninjakiwi_ct.py`, the ingestion chain expands
parent→tiles (`btd6_ingestion_service.py:344-349`,
`path_param_builder=lambda ct_id: {"ctID": ct_id}`), and the query side
reads `btd6_ct_tile` facts (`utils/db/btd6_sources.py:439-462`,
`get_ct_tiles` `btd6_live_query_service.py:894-936` with relic resolution
against the catalog). (d) **Pillow-absent sandbox:** the degrade path is
already built — `build_ct_map_file` returns `(None, ct_id)` when Pillow is
unavailable (`ct_map_view.py:76-83` docstring + `render_ct_map -> bytes |
None`, `utils/btd6/ct_map_render.py:100`), so the slice must ship the
doc's text-summary fallback; sibling probe #228 measured `ct_map_render`'s
test as gating on `pillow_available()` (never forcing the ImportError) —
a lane-side test-hygiene note the build PR should inherit. (e) **Shared
builder caution holds:** `build_event_detail_embed` is also consumed by
the prefix surface (`_event_helpers.py:83/:130`) — the button belongs on
`EventDetailView`, never bolted into the shared builder, exactly the
doc's own caution.

**5. What does it unlock?** Closes the last thin event kind in the #953
drill-down family (the owner-flagged "this doesn't show all the info"
class), makes the CT map/relic renderer reachable from where users
actually are (the live-events flow, not just the panel's sibling button),
and — free — the relic summary field gives `find_relic_locations` its
first detail-surface consumer if the lane wants relic-search later.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing
unshipped: builders, service, parser, ingestion, migration are ALL live at
S. This probe's confirm cost, actual: one `git ls-remote`, one depth-1
clone + one `--shallow-since` deepen, ~10 targeted greps/body-reads —
decisive facts were the zero-hit surface grep, the `05c8621b` last-touch
log, and `migrations/040_btd6_sources.sql:154-168`. Build-time kill-test,
deterministic: drill into a live CT event → the button renders the hex map
+ relic summary; uninstall Pillow → the same button yields the text relic
summary (no crash); non-CT event details render byte-identical (the
`entity_kind` gate).

**7. Which lane, and what does it displace/duplicate?** Build lane:
**superbot** — legacy live lane; every named artifact lives there, and the
canonical doc's disposition already says "promote to a focused PR when the
BTD6 lane has capacity". Honest sim check: NOTHING sim-shaped — no
parameter space, no corpus, no contested design; the Q6 kill-test settles
it in one lane CI run + one manual drill-down. Judgment-only; NO outbox
proposal, outbox tail unchanged. Dedup, named — no duplicate head:
[`btd6-runtime-mechanics-from-game-2026-07-10.md`](btd6-runtime-mechanics-from-game-2026-07-10.md)
— captured; game-data extraction, distinct axis;
[`btd6-shorthand-corpus-eval-2026-07-10.md`](btd6-shorthand-corpus-eval-2026-07-10.md)
— historical; router-eval, distinct;
[`pil-card-render-contract-guard-2026-07-10.md`](pil-card-render-contract-guard-2026-07-10.md)
— parked(routed); names `btd6/ct_map_render` as a family member
(render-contract axis, not this feature) — its without-pillow test note is
carried into Q4(d) here; `ideas/websites/
superbot-site-stats-data-story-2026-07-10.md:117` references the
`ct_relics` fixture tree (`docs/btd6/btd6-data-backends.md`) —
data-adjacency only. HONEST NULL on the briefed dedup claim: the brief
said probe #232 consumed this head as "visible product win, zero
freeze/pace trigger" — greps over the tree AND `git log --all -S` for
`freeze/pace` / `btd6-ct-event-detail` find NO such line anywhere (the
#232 probe file + card contain zero btd6-ct mentions; this head appears
only in its own file, the section README bullet, and the fifth-mint slot-4
line at `control/status.md` @ `d68ac2d`). Not consumed before — this is
its first probe.

**8. What is the smallest shippable slice?** One superbot lane PR, view
wiring only: `EventDetailView` (`live_events_view.py:486`) gains a
`🗺️ Map & relics` button added iff `vm.entity_kind == "btd6_ct"`; callback
= `build_ct_map_file(vm.entity_key)` → on file: `safe_edit(attachments=
[file])` + `embed.set_image("attachment://ct_map.png")` + a relic-tile
summary field from `get_ct_tiles(entity_key, relics_only=True)`; on
`(None, ct_id)`: the text relic summary alone; ↩ back re-renders the
detail. Shared `build_event_detail_embed` untouched (prefix surface
unaffected). Deletable in one revert.

**Recommendation: park** — routed (superbot lane build-direct: the Q8
view-wiring slice, the canonical doc's own Option 1). Rationale: the
premise is verified STILL TRUE at live S `1ecc211` — the CT detail
renders name+window only while every ingredient (tiles API end-to-end,
map renderer, relic query, degrade path) is live and reusable — and the
doc's own disposition already routes it as a focused lane PR; nothing for
sim-lab to settle. Best implementation found: Option 1 exactly as
captured, with the Pillow text-fallback mandatory (Q4(d)) and the button
on the view, not the shared builder (Q4(e)). **Fifth-mint slot #4 is
CONSUMED by this park — per the mint's own "first to yield" flag, the
FIRST ALTERNATE (`superbot-next/known-risks-fix-coupling-checker-doctrine`)
inherits the slot.**
