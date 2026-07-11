# Channel-level, role-scoped access is missing — live bot AND the frozen rebuild design — link index

> **State:** parked(routed — rebuild leg MOOTED: the A-12/R-16 `Lane.ROLE_SET` engine primitive landed live+tested at superbot-next; the remaining leg = consumer wiring + role/proof_channel effect arming, already lane-routed and sequenced behind the effect-arming compensator checklist head; live-bot item 4 (convenience command) stays live-bot backlog)
> **Class:** product · **Target:** `menno420/superbot`
> **Sequence:** before the superbot-next role/proof_channel effect-arming slice (itself sequenced behind `ideas/superbot-next/effect-arming-compensator-checklist-2026-07-10.md`)

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/channel-role-scoped-authority-gap-2026-07-07.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/channel-role-scoped-authority-gap-2026-07-07.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/channel-role-scoped-authority-gap-2026-07-07.md)).

'Only role X in channel Y' cannot be expressed by any of the three authority systems in the live bot — and the rebuild's frozen design has the same gap. Owner-raised, researched against both the same day.

## Probe report (v0, 2026-07-11)

> **Grounding:** https://github.com/menno420/superbot-next@168ef8080347905766893fd92ae3be1ec2ebbc4c · fetched 2026-07-11T14:36:46Z
> *(pin annotation: superbot-next live HEAD N = `168ef80` by `git ls-remote`; tree read via shallow clone at N. The R-16 engine evidence, all at N: `sb/spec/authority.py:54` — `ROLE_SET = "role_set"` in the `Lane` enum (`:10` names it "A-12 / rider R-16 (canonical plan §11b — the K6/S7 fold)"; `:109` — the `role:<binding_name>` ref form, "prefix beats the dot rule"); `sb/kernel/authority/channel_access.py:52-59` — `channel_role_sets: Mapping[int, frozenset[int]]`, the per-channel role-set constraint, deny leg `role_not_held` at `:101-102`; `sb/kernel/authority/resolve.py:100/144/207` handles the lane; `sb/kernel/authority/decision.py:58` — "lane: Lane # CAPABILITY | TIER | ROLE_SET (R-16)". Live unit tests: `tests/unit/authority/test_resolve_authority.py:136` (`test_role_set_lane_allow_set_and_fail_closed`) + `tests/unit/authority/test_channel_access.py:78` (`test_role_set_constraint_r16_under_all_channels`). BUT zero consumers at N: grep finds NO `authority_ref="role:` in any manifest/spec and NO writers of `channel_role_sets` outside kernel+tests. Amendment registry at N: `docs/planning/rebuild-amendments.yml:91` — R-16 consumers `[channel, moderation, security, community]`; `:67` — G-18 ResourceLifecycleSpec `status: pending-gate-0, consumers: [channel, role]`.)*
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-next/168ef8080347905766893fd92ae3be1ec2ebbc4c/control/status.md@168ef80 · fetched 2026-07-11T14:36:46Z
> *(pin annotation: read from the same clone at N; lane heartbeat `updated: 2026-07-11T13:40Z` — freshest version-truth layer, beats the lane README's stale "band 5 … in flight" line (fetched 14:35:18Z). Verbatim at the heartbeat: "Still queued: role/proof_channel live EFFECT action ports (GuildRoleActions, ChannelPermActions still unarmed)"; parity "33/49 subsystems ported … gate GREEN — 212/212 goldens" at #183; band-5 COMPLETE via #111.)*
> **Grounding:** https://github.com/menno420/superbot@9f46cb7840cb2216a012002fe27feb342d45f480 · fetched 2026-07-11T14:36:49Z
> *(pin annotation: superbot live HEAD S = `9f46cb7` by `git ls-remote`; tree read via shallow clone at S, later deepened 200 commits. The canonical idea doc (`docs/ideas/channel-role-scoped-authority-gap-2026-07-07.md`) is unchanged at S: owner quote ":4 — 'it's currently not easily possible to add certain role restrictions to certain channels'"; its § Recommended routing already routed items 1-3 into A-12 + R-16 same-day, leaving item 4 (live-bot convenience command) as "the open remainder — live-bot backlog". Counter-evidence to the capture's live-bot claim: `disbot/cogs/channel_cog.py` carries `!set <name|id> <@role> <True/False>` (`set_access`, `:214`, per-role `read_messages` overwrite) and `!permissions <name|id> <@role> <allow/deny>` (`modify_permissions`, `:677`, per-role `send_messages` overwrite), both routing `role.id` through `_apply_overwrite` → `overwrite_target_id` (`:174`) via the audited ChannelLifecycleService — byte-identical at the capture pin `fd638e3` and at S, last commit touching the file `080b53a` 2026-07-06, i.e. BEFORE the 2026-07-07 research. R-16 mirrored at S: `docs/planning/rebuild-amendments.yml:84` (fetched 2026-07-11T14:36:31Z); verdict recorded in `docs/decisions.md:73`.)*

> Single-pass battery (panel not escalated: routing/park decision on a
> link-index head, reversible, no security/data/spend/public blast radius —
> the authority MODEL itself is already built and unit-tested lane-side).
> Verify-first evidence from this session's phase-1 sweep at the live heads
> N (superbot-next `168ef80`) and S (superbot `9f46cb7`), pins above; greps
> stem-matched per the README battery discipline.

**1. What is this really?**
An owner-raised authority-model gap ("only role X in channel Y", owner quote
2026-07-07) captured against BOTH the live bot and the rebuild — and verify-first
shows both halves have moved. The rebuild half is MOOTED at the engine layer:
`Lane.ROLE_SET` (A-12/R-16) is live at N with the `role:<binding_name>` ref form,
per-channel `channel_role_sets`, a fail-closed deny leg, and passing unit tests
(first pin). The live-bot half was PARTIALLY FALSE at its own research date: the
capture says "no command targets an arbitrary role", but `channel_cog.py` already
shipped two per-role overwrite commands (`!set` `:214`, `!permissions` `:677`)
before the 2026-07-07 research (third pin) — the doc's narrow `!lock`/`!unlock`
hardcoded-`default_role` citation is correct, the blanket claim is not. What
actually remains: (a) rebuild-side CONSUMER WIRING — zero `authority_ref="role:`
consumers exist at N — plus arming the role/proof_channel EFFECT ports
(GuildRoleActions, ChannelPermActions, still unarmed per the 13:40Z heartbeat);
(b) live-bot item 4, a convenience command, backlog-parked by the canonical doc
itself.

**2. What is the possibility space?**
(i) Do nothing — the primitive sits unconsumed and every subsystem that ports
meanwhile accrues retrofit debt (Q4). (ii) Wire `role:` authority_refs into the
four R-16-named consumers (`[channel, moderation, security, community]`) as each
ports. (iii) Arm the effect ports first (the queued role/proof_channel slice),
then wire consumers against a live seam. (iv) Live-bot convenience command
(`!channel lock @role` sugar over the existing per-role overwrites) — item 4,
low-value now that `!set`/`!permissions` exist. (v) The declarative
role-set-binding lifecycle surface — G-18 ResourceLifecycleSpec, still
pending-gate-0 with consumers `[channel, role]`, the fuller future home.

**3. What is the most advanced capability reachable by the simplest implementation?**
Full "only role X in channel Y" declarative enforcement for ONE line of manifest
per consumer: the engine, ref-parsing, per-channel constraint, deny copy, and
tests all exist at N — a subsystem manifest adding `authority_ref="role:<binding>"`
buys the whole capability with zero new engine code, once the effect ports it
surfaces through are armed (already the queued next arming).

**4. What breaks it?**
Sequencing and retrofit drag, not design. (a) Retrofit-cost-per-band SHARPENED:
parity is 33/49 subsystems at #183 and moving fast — every further subsystem that
ports with a manifest lacking `role:` authority_refs is retrofit debt against the
four named consumers. (b) The arming seam is OWNED elsewhere: the parked head
`ideas/superbot-next/effect-arming-compensator-checklist-2026-07-10.md` is
sequenced BEFORE the role/proof_channel arming slice — arming without it re-buys
the #105→#111 compensator lessons; this head must not re-derive or race that
constraint. (c) A probe re-asserting the capture verbatim would misdirect: the
live-bot premise is partially false (Q1), so item-4 work priced off the capture's
"no command exists" claim would be priced off a wrong baseline.

**5. What does it unlock?**
The owner's ask becomes expressible declaratively across moderation, security,
community, and channel subsystems (proof-channel gating, role-scoped moderation
surfaces); the arming of GuildRoleActions/ChannelPermActions it rides on also
unblocks every other role/channel-mutating port; and closing it retires one of
the owner's few direct authority-model complaints with evidence instead of a
rebuild-era IOU.

**6. What does it depend on?**
(a) The role/proof_channel EFFECT arming — still queued at the 13:40Z heartbeat —
which is itself sequenced behind the effect-arming compensator checklist head
(cited at Q4; that head carries the sequencing constraint, this one only points
at it). (b) Consumer subsystems reaching their port slots: R-16 names
`[channel, moderation, security, community]` (`rebuild-amendments.yml:91` at N).
(c) For the fuller lifecycle surface, G-18 ResourceLifecycleSpec passing gate-0
(`:67`, consumers `[channel, role]`). (d) Nothing owner-shaped: the owner already
ruled by raising it; routing landed same-day (A-12 + R-16 at S).

**7. Which lane should build it?**
`menno420/superbot-next` builds the remaining leg — it owns the engine, the
manifests, the amendment registry, the queued arming slice, and the tests;
consumer wiring lands per-subsystem as each ports. Live-bot item 4 (the
convenience command) stays `menno420/superbot` backlog per the canonical doc's
own routing. Nothing for sim-lab: the authority model has live unit tests — the
open work is wiring, not uncertainty; no evidence question remains that the lane
cannot settle by building.

**8. What is the smallest shippable slice?**
Lane-side: the FIRST `authority_ref="role:<binding>"` consumer wiring — the
channel subsystem's manifest (first in R-16's own consumer list) landing with or
directly after the role/proof_channel arming slice, behind the checklist head;
red/green = one manifest line + the existing R-16 unit tests exercised through a
real consumer + a live-drive of the armed deny leg. This-repo-side: this park +
index re-badge (this slice — nothing else to build here, Q-0260).

**Recommendation: park** — routed: the engine primitive landed (A-12/R-16, live
unit tests at N); what remains is consumer wiring + effect arming, already routed
and sequenced in the superbot-next lane behind the effect-arming compensator
checklist head; no sim-shaped evidence question remains (the open work is wiring,
not uncertainty). NO outbox proposal.
