# Channel-deployed component-menu primitive (role menus · starboard · polls) — link index

> **State:** parked(mooted-in-part — the deploy lifecycle is BUILT consumer-private at live S `1ecc211`: role menus shipped the full build-in-panel→post→persist-message_id→re-attach shape as their own code (`RoleMenuView(PersistentView)` + `reattach_role_menus`, bot1.py-wired), starboard shipped reaction-based with its own message_id rows and no components, polls stay unbuilt; the NAMED generic seam `deploy_component_message`/`deployed_messages` is absent at S — the doc's own extract-at-consumer-#1 window closed when reaction-roles PR 2 merged without it; re-open when a SECOND channel-deployed component consumer lands at S; probe 2026-07-12)
> **Class:** product · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/channel-deployed-component-menu-primitive-2026-06-21.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/channel-deployed-component-menu-primitive-2026-06-21.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/channel-deployed-component-menu-primitive-2026-06-21.md)).

One reusable channel-deployed PersistentView primitive (build in a panel, post to a channel, persist message_id, re-attach on restart) — the exact shape needed by role menus, starboard, and polls.

## Probe report (v0, 2026-07-12)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/1ecc21138fe0a1eb672d03b66bd319164c29d55f/docs/ideas/channel-deployed-component-menu-primitive-2026-06-21.md@1ecc211 · fetched 2026-07-12T02:01Z
> *(pin annotation: S = superbot live HEAD by `git ls-remote` 02:00:30Z =
> `1ecc21138fe0a1eb672d03b66bd319164c29d55f` — the SAME S the #228/#232
> probes measured. The canonical doc is byte-identical `fd638e3`→S (md5
> `03240bc6…` both, 38 lines), status still `ideas` — the harvest pin
> content IS the HEAD content. Tree evidence below read from a depth-1
> clone AT S, not from raw guesses.)*
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-next/af985c17def5ff2478103cb363ebb150cb583a97/docs/decisions.md@af985c1 · fetched 2026-07-12T02:04Z
> *(pin annotation: N = superbot-next live HEAD by `git ls-remote`
> 02:03Z = `af985c17def5ff2478103cb363ebb150cb583a97` — N has moved past
> the #232 probe's `cc59a6e`; `docs/decisions.md` re-read fresh at
> `af985c1`, D-0040/D-0062 cited from that read.)*

> Single-pass battery (panel not escalated: docs-only disposition,
> reversible park, no security/data/spend/public blast radius — README
> § probe battery). Verify-first at live S, tree-scanned not doc-trusted:
> stem-matched greps (`deploy_component|deployed_message|component_message`,
> `PersistentView`, `timeout=None`, `add_view\(`) over the depth-1 clone,
> then body-reads of `disbot/core/runtime/persistent_views.py`,
> `disbot/core/runtime/message_anchor_manager.py`,
> `disbot/views/roles/role_menu_view.py`,
> `disbot/views/roles/role_menu_builder.py`, `disbot/cogs/starboard_cog.py`,
> `disbot/utils/db/starboard.py`, `disbot/bot1.py`, and the
> reaction-roles plan header. Cross-lane ledger read (PR #180 card):
> superbot has no `docs/decisions.md`; superbot-next's read at N instead.

**1. What is this really?** A platform-extraction capture (2026-06-21,
Q-0089, minted off the Carl-bot reaction-roles overhaul plan): ONE shared
seam for "an operator-deployed, DB-persisted component message in a guild
channel" — provisionally `deploy_component_message(...)` + a
`deployed_messages(guild_id, channel_id, message_id, kind, ref_id)`
registry owning post → persist `message_id` → re-attach-on-boot →
teardown — so role menus (reaction-roles PR 2), starboard
(fun-and-ease §B1), and polls/suggestions (superbot-vision AG-15) become
"define the view + the toggle handler." Who for: superbot feature builders
(agents), indirectly every server operator who deploys a component message.
The doc's own build rule: extract AT consumer #1 (roles PR 2) because
consumer #2 was already backlogged.

**2. What is the possibility space?** Four lifecycle consumers visible at
capture: per-user panel anchors (already owned by
`message_anchor_manager`), role menus, starboard, polls/suggestion board;
plus the centralized guild-teardown (INV-I) hook the doc prices. Widest
form: every future channel-posted component message rides one registry, one
restore pass, one GC, one teardown hook.

**3. What is the most advanced capability reachable by the simplest
implementation?** Today, at live S, the simplest implementation is NO new
code: the base-class half already exists
(`disbot/core/runtime/persistent_views.py` — `PersistentView`,
`timeout=None` at `:104`, registry + `register()`), and the re-attach
pattern exists TWICE as ~40-line loops (`restore_anchors`,
`message_anchor_manager.py:110-168`, wired `bot1.py:339`;
`reattach_role_menus`, `role_menu_view.py:447-483`, wired
`bot1.py:343-345`). A third consumer copies one loop. The primitive only
compresses copy #3 — which does not exist yet.

**4. What breaks it? (assumptions verified — the staleness check, the
load-bearing answer.)** The pin is stale in effect even though the doc is
byte-identical: the idea's premise ("today each would hand-roll…") was
overtaken lane-side. Measured at S `1ecc211`, part-built — split per the
PR #189 badge duty: **built half:** the LIFECYCLE, consumer-private.
Role menus shipped the EXACT claimed shape end-to-end as their own code —
build-in-panel (`RoleMenuBuilder`, `role_menu_builder.py:449`) →
post-to-channel (`_post_new` `:874`) → persist message_id
(`reaction_role_service.set_menu_location(menu_id, target.id, message.id)`
`:382`) → live-bind (`interaction.client.add_view(view,
message_id=message.id)` `:383/:911/:952`) → boot re-attach
(`reattach_role_menus`, `role_menu_view.py:447-483`, whose own docstring
says "Mirrors ``message_anchor_manager.restore_anchors`` but keyed on the
``role_menus`` rows") — with `RoleMenuView(PersistentView)` at
`role_menu_view.py:232`; the reaction-roles plan header reads "PR 2
MERGED (#1219)". Starboard shipped too, but reaction-based: raw-reaction
listeners (`starboard_cog.py:39/:46`), posts/edits the hall-of-fame
message and persists `starboard_message_id` via its own table
(`utils/db/starboard.py:81-96` `upsert_entry`) — no components on the
posted message, so no view to re-bind; it hand-rolled only the
"post + remember id + edit" half. **Open half:** the generic seam itself —
`rg -in "deploy_component|deployed_message|component_message"` over the S
tree returns ZERO hits (stem-matched) — and component polls: `!poll` is
the legacy `utility_cog.py:298` command, AG-15 suggestion box unbuilt. So
the extract-at-consumer-#1 justification EXPIRED: PR 2 merged without the
extraction, consumer #2 arrived component-less, and the classic rule the
doc itself cites now says wait for the second real copy. Rebuild side, at
N `af985c1`: D-0040 already ported the whole role family into the
rebuild's own grammar (migration 0017 `role_menus`+options stores, the
`role.hub` panel with pinned verbatim `role:*` custom_ids), D-0062
re-routed `!rolemenu` at `PanelRef("role.hub")`, and starboard + utility
(`!poll`) are named not-yet-ported (D-0040 deviation 5, D-0062) — any
generic deployed-message seam N ever needs will be minted in N's
manifest/panel grammar, not as this S-side helper, so building it at S
now widens the successor boundary for zero scheduled consumers.

**5. What does it unlock?** Priced honestly: nothing today. If a SECOND
channel-deployed component consumer lands at S (component polls, a
component-modernized starboard), extraction fires per the doc's own
second-copy rule with role menus as the refactor donor — and this report
is the donor map (the five call-sites above).

**6. What does it depend on? (cheapest confirm/kill, priced)** This
probe's confirm cost, actual: one `ls-remote`, one depth-1 clone, ~8
targeted greps/body-reads — the decisive facts were the zero-hit
primitive grep, `role_menu_view.py:447`'s mirror-docstring, and the plan
header "PR 2 MERGED (#1219)". Kill test for the park: at a future S
re-pin, grep for a NEW `bot.add_view(..., message_id=...)` call-site
family outside `views/roles/` (or a components-based starboard/poll
module) — a hit re-opens the head with the extraction now justified;
`deploy_component_message` appearing means the lane self-served, flip
toward historical.

**7. Which lane, and what does it displace/duplicate?** Build lane if
re-opened: **superbot** (legacy live lane — the consumers and both
existing re-attach loops live there; N explicitly re-grammars this class
per D-0040). Honest sim check: NOTHING sim-shaped — every open question is
refactor-economics + timing judgment (extract now vs at second copy), no
numeric parameter space, no corpus; judgment-only, NO outbox proposal.
Dedup, named — no duplicate head owns the primitive:
[`fun-and-ease-brainstorm-2026-07-10.md`](fun-and-ease-brainstorm-2026-07-10.md)
— captured; its §B1 starboard is this head's consumer #2, now built
lane-side reaction-based (that file's future probe should carry this
finding);
[`superbot-vision-2026-07-10.md`](superbot-vision-2026-07-10.md) —
captured; AG-15 polls/suggestion box is consumer #3, still unbuilt;
[`community-platform-features-2026-07-10.md`](community-platform-features-2026-07-10.md)
— captured; feeds/counters adjacency only;
[`rebuild-layout-success-simulator-2026-07-10.md`](rebuild-layout-success-simulator-2026-07-10.md)
— probed; touches `role_menu_layout_sim.py` (layout scoring, not
deployment) — tangential;
[`pil-card-render-contract-guard-2026-07-10.md`](pil-card-render-contract-guard-2026-07-10.md)
— parked(routed); `role_menu_render` is a card-family member — tangential.
Lane-side machinery that partially displaces the idea:
`disbot/core/runtime/persistent_views.py` +
`disbot/core/runtime/message_anchor_manager.py` (the pieces the doc named)
plus the consumer-private `reattach_role_menus` third path, all cited in Q4.

**8. What is the smallest shippable slice?** None here (docs-only lane;
this pricing is the deliverable). At S, if re-opened by a second consumer:
extract the `deployed_messages` registry + `deploy_component_message`
helper BY refactoring role menus onto it (donor code
`role_menu_builder.py:382-383` + `role_menu_view.py:447-483`), then the
new consumer joins — one PR, behavior-preserving for menus.

**Recommendation: park** — mooted-in-part: the claimed lifecycle is built
and live at S `1ecc211` inside its first consumer (role menus, PR 2
#1219), starboard shipped without components, polls remain unbuilt, and
the named generic seam is absent — so the extraction the doc justified at
consumer #1 lost its window and now waits, per the doc's own second-copy
rule, for a second channel-deployed component consumer at S (with N
re-gramming the class per D-0040 in the meantime). Best implementation
found: the role-menu path itself (`RoleMenuView(PersistentView)` +
builder post/persist + `reattach_role_menus`) — it IS the primitive,
consumer-private, and the donor for any future extraction. Nothing
sim-shaped; no outbox entry.
