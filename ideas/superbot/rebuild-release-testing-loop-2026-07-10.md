# Idea — the in-server release → test → verify loop (announce · coverage · test-mode · approve) — link index

> **State:** parked(routed — superbot-next lane build; probe 2026-07-11)
> **Class:** product · **Target:** `menno420/superbot-next`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/rebuild-release-testing-loop-2026-07-03.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/rebuild-release-testing-loop-2026-07-03.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/rebuild-release-testing-loop-2026-07-03.md)).

Owner-originated in-server release loop: announce changes, track test coverage, a test mode, and per-command approve/verify sign-off — the concrete machinery for three gaps the final judgment flagged (change communication, field feedback, live co-test throughput).

## Probe report (v0, 2026-07-11)

> **Grounding:** https://github.com/menno420/superbot-next@2f4b2c3dcf4a13f32dd1e758908a886cc5b1d704 · fetched 2026-07-11
> *(pin annotation: N = the newest entry of the `commits/main.atom` feed at
> fetch time — commit stamp 2026-07-11T17:55:14Z; confirmed by ONE raw read of
> `docs/decisions.md` at the full pin: 73 ledger entries, `[D-0049]` at :368.)*

> Single-pass battery. Verify-first reads: superbot-next `docs/decisions.md` @
> `2f4b2c3` (ledger D-0001…D-0073; D-0049/D-0048/D-0021 read in full),
> superbot-next `control/inbox.md` (ORDERS 001–013) + `control/status.md`
> (band-7 lane wrap 2026-07-11) + `docs/status/testing-report-2026-07-09.md`;
> canonical idea @ superbot `fd638e3` (87 lines, raw).

**1. What is this really?** An owner-originated four-component in-server
release-testing loop (canonical: superbot
`docs/ideas/rebuild-release-testing-loop-2026-07-03.md` @ `fd638e3`): (A) a
release announcer posting a new/changed/improved-commands digest to a
designated channel; (B) per-command "tested-since-change" coverage off a usage
store; (C) a dedicated test/debug mode; (D) explain-then-approve, where
confirmation doubles as the `verified_live` sign-off (Q-0234/Q-0222).
Name-which-half (from the #194 mint, confirmed one level deeper this probe):
**C's substrate is BUILT and live-verified** — D-0049 test-mode composition
root, CUT-1 smoke PASS (live boot on the test token, gateway READY as Galaxy
Bot#6724, exit 0; testing-report row 1). **D's store is BUILT but empty** —
D-0021 `verified_live` registry (signer+signed_at+build_sha+linked evidence
mandatory, `tools/check_verified_live.py` the gate), zero rows minted ("NO
records minted — Q-0244 VERIFIED needs prefix_twin_live + pipeline_replay
PASSES", testing-report). **A, B, and D's in-server flow are ABSENT**: no
entry in D-0001…D-0073 builds them (greps for announce/coverage/approve/release
hit only unrelated senses — xp `announce_channel`, parity-table coverage, kit
release tags), and no superbot-next inbox ORDER (001–013) touches the loop.

**2. Possibility space.** Minimal changelog digest → usage-store coverage
signal ("changed since vN, not exercised since the change") → the approve flow
as THE `verified_live` minting surface → a full co-test loop where each
release drives a targeted in-server testing session and the coverage signal
ranks the live-testing queue (mechanizing exactly the row-9-shaped pending
passes).

**3. Most advanced capability via simplest implementation.** Component D as
one app-command/button flow that mints a complete `verified_live` row into the
D-0021 registry. Simplest: one interaction + one registry write on an
already-built store with an already-built checker. Most advanced: it makes
Q-0244's VERIFIED tier reachable routinely — the registry stops being a debt
list.

**4. What breaks it.** (i) Hard sequencing: app-command tree registration is
deliberately NOT armed in D-0049 (leg C stays COMPARE-ONLY — "the local
app-command tree is EMPTY until app-command registration lands, and
tree.sync() pushes the TREE, not the snapshot — enabling it would erase the
remote tree"), so any slash/button UI for A/D must land after that arms.
(ii) Component B needs a usage store that does not exist — a new seam, not a
composition; bundling it with A/D is the scope-creep failure mode. (iii)
Conflation risk with the ADJACENT-BUT-DIFFERENT D-0048 review-feed poster (the
AI review loop, parked with NL arming, key-gated via OWNER-ACTION 5) — one
"announcer" serving both would tangle an owner-facing release digest with the
key-gated AI surface. (iv) A one-click approve degrades into exactly the
checkbox D-0021's why bans ("a live sign-off should not be just a checkbox")
— the flow must attach evidence links, not just a click.

**5. What it unlocks.** First `verified_live` rows minted (registry currently
empty); the change-communication + field-feedback + live-co-test-throughput
gaps the final judgment flagged get their concrete machinery just as Band 7
closes (D-0048, 2026-07-09; band-7 parity lane wrapped 2026-07-11) and CUT
composition makes releases real; component B turns the pending live-testing
passes (testing-report row 9 et al.) into a ranked queue instead of owner
memory.

**6. Dependencies.** superbot-next app-command tree registration (named in
D-0049's not-armed list) for any slash/button UI; D-0021 registry + checker
(built); D-0049 test-mode root (built, smoke PASS); an owner-designated
announce channel (config); B additionally needs a new usage/coverage store
(unbuilt). No AI-key dependency for A/C/D — the loop is deliberately not part
of the key-gated NL surface.

**7. Which lane builds it?** superbot-next — it owns `sb/`, the
capability/manifest grammar, the D-0021 registry and its `tools/check_*` seam,
and the test-mode root the loop wraps. Honest sim check: NO distinct evidence
question survives — the open forks (digest source, coverage-store shape,
approve UX) are one-lane design calls its own decision ledger settles; unlike
PROPOSAL 009's settlement corpus there is no historical instance set to
reconstruct and no cross-contract dispute reproduction would arbitrate. No
proposal; outbox tail stays 009.

**8. Smallest shippable slice.** Component D's minting flow: one app-command
(or component interaction) writing a complete `verified_live` row with linked
evidence — landing immediately AFTER app-command tree registration arms, as
its first consumer. (Close second: A as a boot-time digest composed from the
decisions-ledger delta — zero new stores — but D unblocks the Q-0244 VERIFIED
tier that every pending live-testing pass already waits on.)

**Recommendation: park** — routed (superbot-next lane build). Rationale: three
of four components are compositions on already-decided superbot-next
substrates (D-0021 registry, D-0049 test-mode root) sequenced behind
app-command tree registration, and the remaining forks are one-lane design
calls, not sim-reconstructable evidence questions — routed to the manager as
an ORDER-worthy flag (sequence: after app-command registration arms, before
the live-testing wave that needs `verified_live` rows).
