# Vision: out-visual Dank Memer with a themeable card engine — link index

> **State:** parked(umbrella — children routed or owner-gated: the two agent-buildable children already carry their own routed heads (`leaderboard-row-avatars` = the flagship feature card, `pil-card-render-contract-guard` = the family contract seam, both parked(routed)); one NEW micro-child flagged as an avatars-ORDER rider (`/myprofile` avatar_disc adoption, profile_render.py:67 @ S `1ecc211`); everything else remaining under the umbrella is owner-gated art/design (mining_render redesign, H4 art pack + fonts, H5 animation + per-user premium themes); nothing sim-shaped; probe 2026-07-12)
> **Class:** product · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/visual-card-engine-vision-2026-06-23.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/visual-card-engine-vision-2026-06-23.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/visual-card-engine-vision-2026-06-23.md)).

North star: out-visual Dank Memer with one themeable card engine. The foundation shipped (card_render + the profile card); the strategy and per-feature card roadmap remain the live capture.

## Probe report (v0, 2026-07-12)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/1ecc21138fe0a1eb672d03b66bd319164c29d55f/docs/ideas/visual-card-engine-vision-2026-06-23.md@1ecc211 · fetched 2026-07-12T01:02Z
> *(pin annotation: S = superbot live HEAD by `git ls-remote` 01:01:39Z =
> `1ecc21138fe0a1eb672d03b66bd319164c29d55f` — the SAME S the sibling guard
> probe (PR #228) measured, so its render-family census byte-carries here
> without re-derivation. The canonical vision doc is byte-identical
> `fd638e3`→S (md5 `187aeef2…` both) — the harvest pin content IS the HEAD
> content, self-annotated horizons included.)*
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-next/cc59a6eabd603df173fad74ede53240c61f63e77/docs/decisions.md@cc59a6e · fetched 2026-07-12T01:04Z
> *(pin annotation: N = superbot-next live HEAD by the same `git ls-remote`
> run = `cc59a6eabd603df173fad74ede53240c61f63e77` — N moved since the #223
> probe's `d3dba9b` pin, but `docs/decisions.md` is byte-identical
> `d3dba9b`→`cc59a6e` (diff empty), so every decision-ledger claim carries.)*

> Single-pass battery (panel not escalated: docs-only disposition of an
> umbrella head, reversible park, no security/data/spend/public blast
> radius — README § probe battery). Verify-first at live S, per-horizon,
> body-read not doc-trusted: `disbot/utils/mining_render.py` import block,
> `disbot/utils/profile_render.py:67`, `disbot/utils/card_render.py`
> THEMES registry `:75-149` + export surface `:462/:467`,
> `disbot/services/xp_helpers.py` (zero `theme` hits),
> `scripts/check_consistency.py:825`, superbot `control/inbox.md` @ S.
> Dedup: `rg -il 'card|render|visual' ideas/superbot/` (kit machinery
> excluded), 22 hits triaged.

**1. What is this really?** Not a feature — the fleet's captured VISUAL
STRATEGY for superbot: out-visual Dank Memer by copying its topology (image
is the screen, native components are the controls, every season a re-skin of
ONE templated engine) on the already-working Pillow + `bytes|None` fallback
stack instead of DM's Node/Skia. Owner-directed capture (2026-06-23 DM
screenshot session); the owning surface is superbot's presentation layer.
Who for: the live bot's players (the visible-win surface Q-0259 weights
first) and the owner-as-artist — the doc's own H4 makes his art pack the
biggest visual jump. Crucially the head is an UMBRELLA: H1 (engine) shipped
at capture time; H2/H3 partially shipped by later dispatch runs, annotated
in-doc; H4/H5 unstarted. The probe question is dispositional: what does the
umbrella still own that its routed children don't?

**2. What is the possibility space?** The doc's own five horizons, re-measured
at live S `1ecc211`: **H1** engine + profile card — SHIPPED (`card_render.py`
Theme/THEMES/CardCanvas; registry now SIX skins — midnight/ember/verdant/
abyss/tidal/harvest, `:75-149` — grown past the doc's four: the config-only
skin claim is being dogfooded). **H2** migrate renderers — shipped except
`mining_render` (verified: no `card_render`/`CardCanvas` import at S; the
doc's own 2026-06-24 note rules the rebase a VISUAL REDESIGN DECISION for the
owner — no-font bitmap text + specialized rarity palette, not a mechanical
dedup), and the dedup invariant is CI-guarded live
(`rule_card_engine_helper_duplication`, `scripts/check_consistency.py:825`).
**H3** image-as-screen showpieces — started (`!rank` themed card + stat-toggle
re-render; per-category board skins via `RankProvider.card_theme`); remaining:
the hub panels, genuine season/world skin packs (blocked on H4 art), and the
doc's named "next obvious adopter" — `/myprofile` still draws
`initials_disc` (`profile_render.py:67` @ S), the `avatar_disc` primitive
shipped 2026-07-01 and never adopted there. **H4** real art + fonts — owner
domain by the doc's own words. **H5** animation + per-user premium themes —
unbuilt (export surface is `to_png`/`to_jpeg` only, `card_render.py:462/:467`;
no animation API) and monetization-shaped (cosmetics-not-power), i.e.
owner-posture-gated twice over.

**3. What is the most advanced capability reachable by the simplest
implementation?** For the umbrella's remaining agent-buildable surface: ONE
call-site edit — `/myprofile` swaps `initials_disc` for the live-proven
`avatar_disc`-then-initials fallback the rank card already uses
(`rank_render.py:97` pattern, network seam `fetch_avatar_png` already
shipped) — and the flagship self-identity card catches up to the incumbents'
one visible tell. Everything bigger under this head is either already routed
(avatars board card #204-probe, contract guard #228) or gated on owner
art/design calls, not on engineering.

**4. What breaks it? (assumptions verified)** (i) The S/N divergence the
ledger priced is REAL and DOCTRINAL at both live HEADs: S ships per-feature
cards ad hoc (family grown 4→9 modules / ~12 `bytes|None` entrypoints since
the 2026-06-22 census — the #228 probe's measurement at this same S) while N
excludes image cards WHOLESALE — D-0038 deviation (5) verbatim at
`cc59a6e`: "no image cards (leaderboard/rank Pillow rendering =
presentation)" — STILL STANDING (decisions.md byte-identical
`d3dba9b`→`cc59a6e`). (ii) But the build-twice cost is BOUNDED, not
runaway: D-0061's parity ledger (same file @ N) already classes
"successor-boundary render drift (rank/xpmenu PNG card … the myprofile PNG
card `_files`)" as a NAMED red class — the rebuild's own bookkeeping
tracks exactly which cards will need re-porting, so each S-side card widens
a ledgered debt, not an invisible one. (iii) The "each unprobed card widens
cutover cost" worry dissolves on enumeration: at live S there is NO un-routed
agent-buildable card left under this umbrella — the board card and the
contract guard have routed heads, `/myprofile` avatar adoption is a
one-call-site rider, and every other horizon item waits on the owner (H4
art, mining_render redesign, H5 monetization posture). (iv) Cost of parking:
zero build surface lost — the umbrella's value is the census, and this
report IS the refreshed census; the risk is a FUTURE per-feature card
shipping outside the strategy (new renderer off-engine) — already fenced by
the live duplication CI rule and the #228 guard's registry-by-pattern review
lever. (v) Superbot inbox @ S carries ORDER 001 done + ORDER 002 done only —
no card/avatar order routed yet; the avatars window stays open (same fact
the #228 probe parked on).

**5. What does it unlock?** Consuming TOP-5 #4 closes the games-wave visual
family end-to-end at probe level: strategy (this head), flagship feature
(avatars), contract seam (guard) — leaving the manager ONE sweep flag family
(route the avatars ORDER; the guard and the `/myprofile` micro-child ride
it) instead of an open umbrella; and the H5 re-open trigger (owner art pack
landing = season packs + animation become buildable) is now written down
instead of implicit in a 170-line canonical doc.

**6. What does it depend on? (cheapest confirm/kill, priced)** The umbrella
as strategy depends on nothing unshipped — engine live, fallback discipline
live, CI dedup guard live. The remaining children depend on: owner art (H4 →
season packs, H5 animation), an owner monetization posture (H5 premium
themes), and the manager routing the avatars ORDER (carrier for the guard +
the `/myprofile` rider). This probe's confirm cost, actual: two `ls-remote`
calls, one md5 doc-drift check, one decisions.md diff, six targeted raw
reads — the decisive facts were `mining_render`'s import block,
`profile_render.py:67`, `card_render.py`'s export surface, and D-0038 dev
(5) at live N. Kill-test for the park: any future S re-pin showing a NEW
off-engine renderer or an un-routed feature card reopens the umbrella.

**7. Which lane, and what does it displace/duplicate?** Build lane for
everything under it: **superbot** (legacy live lane — N defers the whole
class per D-0038 dev 5). Honest sim check: NOTHING sim-shaped — every open
question is owner visual judgment (does the card beat Arcane/DM to the eye,
which art, whether cosmetics monetize) with no numeric parameter space or
corpus; judgment-only, NO outbox proposal. Dedup, named:
[`pil-card-render-contract-guard-2026-07-10.md`](pil-card-render-contract-guard-2026-07-10.md)
— parked(routed), owns the CONTRACT SEAM (its registry is the attach point
this vision's future cards join; zero overlap with the strategy itself);
[`leaderboard-row-avatars-2026-07-10.md`](leaderboard-row-avatars-2026-07-10.md)
— parked(routed), owns the FLAGSHIP FEATURE CARD (the vision's H2/H3
leaderboard line item, carried to build); [`games-theme-engine-website-first-2026-07-10.md`](games-theme-engine-website-first-2026-07-10.md)
— parked(routed), the SAME core/skin doctrine at the games-program layer
(themes as validated data packs) — sibling doctrine, different layer, no
consumption either way; [`ux-lab-interface-gallery-2026-07-10.md`](ux-lab-interface-gallery-2026-07-10.md)
— captured, the UX sandbox where `image_builders` prototypes were born —
upstream neighbor, not overlap; [`mining-grid-encounters-2026-07-10.md`](mining-grid-encounters-2026-07-10.md)
et al. touch cards only as consumers. No duplicate head owns the strategy.

**8. What is the smallest shippable slice?** None HERE (docs-only lane). At
the target, per child: (a) the `/myprofile` avatar micro-child — one
call-site commit riding the avatars ORDER (swap
`profile_render.py:67` `initials_disc` → the `rank_render.py:97`
avatar-then-initials pattern; fetch seam exists); (b) the avatars + guard
slices as already specified in their own probes' Q8; (c) H4/H5: no agent
slice exists — first mover is an owner art drop or monetization call, and
the doc's own H4 note (gate `image_safe` on glyph coverage when a
colour-emoji font lands) is the ready-made first commit of that era.

**Recommendation: park** — umbrella, children routed or owner-gated.
Rationale: at live S `1ecc211` / N `cc59a6e` the strategy's foundation is
shipped and CI-fenced, both agent-buildable children already carry routed
heads (avatars #204-probe, guard #228), the one NEW gap found is a
one-call-site rider (`/myprofile` avatar_disc adoption — flag it onto the
avatars ORDER), and every remaining horizon item is owner-gated art/design
(mining_render redesign, H4 art pack, H5 animation + premium themes) with
the build-twice exposure bounded by N's own D-0061 successor-boundary
ledger; nothing numeric for sim-lab. Best implementation found: keep the
canonical doc as the strategy home; route nothing except the rider flag;
re-open trigger = owner art pack landing OR a new off-engine renderer at a
future S re-pin.
