# Idea: leaderboard row avatars (the Arcane-defining visual) — link index

> **State:** parked(routed — superbot lane build; probe 2026-07-11)
> **Class:** product · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/leaderboard-row-avatars-2026-07-01.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/leaderboard-row-avatars-2026-07-01.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/leaderboard-row-avatars-2026-07-01.md)).

Per-row avatar thumbnails on the leaderboard image card — the single thing that makes Arcane's board feel real rather than a chart; every needed piece already exists.

## Probe report (v0, 2026-07-11)

> **Grounding:** https://github.com/menno420/superbot@d647b2e9a75700439d6c194f7778972892f6bd45 · fetched 2026-07-11
> **Grounding:** https://github.com/menno420/superbot-next@ab1e9162596f897000a43d085f2b6aa3f78090ad · fetched 2026-07-11
> *(pin annotation: both pins = blobless-clone HEADs at probe time (S = superbot
> `d647b2e`, commit stamp 2026-07-11T20:26:07+02:00; N = superbot-next
> `ab1e916`, 2026-07-11T20:34:44+02:00). Canonical idea file is byte-unchanged
> since its creation commit `8c9eb3d1` — the `fd638e3` harvest pin content IS
> the HEAD content.)*

> Single-pass battery. Verify-first reads at S: the render body
> `disbot/utils/ux_patterns/image_builders.py:90-180`, the projection
> `disbot/services/rank_providers.py:39-60` + all 12 providers, the invocation
> site `disbot/cogs/leaderboard_cog.py:56-79`, the seams
> `disbot/utils/card_render.py:425` + `disbot/services/xp_helpers.py:35` +
> `disbot/utils/rank_render.py:97`; superbot `docs/decisions/` (8 ADRs) +
> `control/inbox.md` — zero leaderboard/avatar hits. At N: `docs/decisions.md`
> D-0038/D-0061, `parity/parity.yml:88`, `control/inbox.md` — zero orders
> touching leaderboard visuals.

**1. What is this really?** Per-row circular avatar thumbnails on the
`!leaderboard` image card — the owner-captured "Arcane-defining visual"
(canonical: superbot `docs/ideas/leaderboard-row-avatars-2026-07-01.md` @
`fd638e3` = `d647b2e`, Q-0089) — composed from seams the 2026-07-01 polish PR
already shipped: `CardCanvas.avatar_disc` (card_render.py:425 @ `d647b2e`,
returns False on decode failure so the initials disc always covers),
`fetch_avatar_png` (xp_helpers.py:35, the one network→bytes seam, `None` on
any failure), and `render_leaderboard_image` (image_builders.py:90). Verified
NOT built at S HEAD: the render signature takes `rows/title/value_texts/theme`
only — no avatar parameter — and the row loop (image_builders.py:133-180)
draws rank number + name + bar + value, no disc. No avatar LRU exists
(grep `lru|cache` in xp_helpers.py hits only the F-1 xp-config cache).

**2. What is the possibility space?** Minimal: bounded-concurrent top-N avatar
fetch + one disc per row on the XP board. Next ring: the board is
PROVIDER-FED (12 registered `RankProvider` categories at
rank_providers.py:107-588 — xp/coins/mining/creatures/fishing/farm/gamexp/
crafting/deathmatch/rps/counting/karma), so one render change lights avatars
on every category at once. Micro-idea ring: the in-process avatar LRU
(user_id → bytes, short TTL) also removes repeat CDN hits from the `!rank`
stat-toggle re-render (xp_helpers.py:223 re-fetches per render today). Outer
ring: the same fetched-bytes list feeds any future top-N visual (spotlight
top-3s, podium cards).

**3. What is the most advanced capability reachable by the simplest
implementation?** One additive `avatars: tuple[bytes | None, ...] | None`
parameter on `render_leaderboard_image` + `avatar_disc`-or-initials per row +
one bounded `asyncio.gather` in the cog's card path — and the visible gap to
Arcane/MEE6 closes across ALL 12 leaderboard categories simultaneously,
because the card is provider-fed (zero per-category work).

**4. What breaks it?** (i) The idea's "we already have every piece" OVERCLAIMS
one piece: `RankEntry` (rank_providers.py:39-60) exposes only
`label/name/score/value_text` — NO `user_id`/member. Providers hold
`row["user_id"]` in scope when building entries (e.g. XpProvider.top,
rank_providers.py:115-131) but the structured projection drops it, so avatar
resolution needs a `user_id: int | None = None` field plus population across
the 12 providers — small, additive, but it is real work the canonical note
does not price. (ii) The layout claim "the layout already leaves room" is
STALE at HEAD: `_LB_NAME_X = _LB_PAD + 46` (image_builders.py:56) is a ~46px
gutter shared with the size-28 rank number — a row-height disc (row is 64px,
image_builders.py:50) needs a name-column shift, i.e. a constants edit, not
free space. (iii) Unbounded/unisolated fetches — the canonical note already
prescribes the fix (bounded gather, per-fetch `None` → initials disc, one slow
CDN/departed member never stalls the board). (iv) Cutover horizon: this lands
on the LEGACY bot — superbot-next D-0038 deviation (5) @ `ab1e916` reads "no
image cards (leaderboard/rank Pillow rendering = presentation)" and D-0061
classes card render drift as successor-boundary, so the rebuild re-ports the
visual later (build-twice cost, named honestly; acceptable for the Q-0259
live-bot visible-win slot since the live bot IS the product until cutover).

**5. What does it unlock?** Closes the last visible gap to the incumbents on
the board (the owner's explicit Arcane/MEE6 comparison target, canonical §Why)
on the surface players actually see today; the avatar LRU independently speeds
the single-user `!rank` re-render path; and it sets a captured presentation
bar (goldens exist: tests/unit/cogs/test_leaderboard_card.py) that
superbot-next's live-adapter presentation band must eventually match.

**6. What does it depend on?** All at S, all shipped: Pillow-optional render
(returns `None` → embed fallback, unchanged), `avatar_disc` + `initials_disc`
(proven live on the rank card — rank_render.py:97's
avatar-then-initials fallback), `fetch_avatar_png`, discord member cache for
`guild.get_member(user_id)` (departed member → `None` → initials disc,
consistent with `_clean_name`). Needs NO new store, NO migration, NO AI key,
NO owner action. Missing piece: the `RankEntry.user_id` projection growth
(Q4-i). Sequenced by nothing — the superbot lane auto-merges on green
(Q-0197) and is KEEP per the fleet review
(`docs/planning/fleet-review-2026-07-11.md:69` @ `d647b2e`).

**7. Which lane should build it?** superbot (the legacy live lane) — it owns
`disbot/` presentation, the board is live there, and superbot-next explicitly
DEFERS image cards to its presentation/live-adapter successor band (D-0038
deviation 5), so routing it to the rebuild would park it behind the cutover
and forfeit the "visible now" value that put it in the TOP-5. Honest sim
check: NO evidence question survives — the open calls (concurrency bound, LRU
size/TTL, disc radius/name-column shift) are one-lane visual design calls
with no parameter space a simulator would settle and no historical corpus to
reconstruct. No proposal; outbox tail stays 009.

**8. What is the smallest shippable slice?** One superbot PR: (a) `RankEntry`
grows `user_id: int | None = None` (additive — embed consumers untouched) and
the 12 providers populate it from the `row["user_id"]` already in scope; (b)
`render_leaderboard_image` grows an optional `avatars` tuple and the row loop
draws `avatar_disc`-or-initials with the name column shifted right; (c) the
cog's `_file_from_entries` path (leaderboard_cog.py:71) resolves members and
fetches avatars via bounded `asyncio.gather` with per-fetch `None` fallback.
The avatar LRU rides the same PR or a trivial follow-up.

**Recommendation: park** — routed (superbot lane build). Rationale: verified
unbuilt at S HEAD and pure-additive on shipped, live-proven seams; the one
unpriced gap (RankEntry has no `user_id`) and the stale layout claim are
build-PR details, not evidence questions — nothing for sim-lab to settle, so
this routes to the manager as an ORDER-worthy live-bot build flag (superbot
lane, Q-0259 games-first live-bot slot).
