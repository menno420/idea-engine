# games-web ↔ superbot-mineverse scope seam — two lanes now render the same miner state

> **State:** parked(routed — manager decision: the seam (specialize/reconcile/fold) is a fleet routing call, verified UNRULED live 2026-07-11T04:34Z; ranking (A) specialize > (B) reconcile-artifacts-kept > (C) fold decided-and-flagged into the heartbeat's read-only-API fan-in note for the :30 sweep — primary battery below, producer-side sibling folded)
> **Class:** product · **Target:** `menno420/product-forge`
> **Grounding:** https://raw.githubusercontent.com/menno420/product-forge/0a6efe96ef8021679b9f8a6ee63a617cd9d61ffc/control/inbox.md@0a6efe9 · fetched 2026-07-11T03:31:46Z
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-mineverse/01a8b8572507f5dd5b65109161091b90272cc57b/control/status.md@01a8b85 · fetched 2026-07-11T03:34:14Z
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/93d3a4d/docs/roster.md@93d3a4d · fetched 2026-07-11T03:31:30Z
> **Sequence:** before the manager routes games-web phase-2 / the batched superbot read-only-API providing ORDER

## Problem

product-forge ORDER 001 (2026-07-10T18:41Z) routed games-web to the forge under the
*"no owning lane exists"* test: a comic browser-RPG rendering of the MINING character
sheet, mock-first, real data explicitly deferred. Since then the premise moved:
**superbot-mineverse was born** (roster gen #4: "LANE BORN THIS WINDOW",
mining-browsergame) and at live HEAD `01a8b85` it is far past its roster row — stages
0/a/b/c done, 163 tests, and it already renders miner state in a browser: 9-slot gear
panel with wear, vault with tier pips, depth/biome ladder, tabbed leaderboards, all
from its own versioned `mining_snapshot.v1` contract (16 per-miner v1 fields projected
from `mining_player_state` + `game_xp_service`). games-web phase-1 renders the same
underlying miner (gear paper-doll — 8 fixed slots — stats, skills, structures) from
its own `games-web.character-sheet` v1.0.1 contract. An owning lane for
browser-rendered mining state now exists, and games-web phase-2 as proposed would
build a **second live-data path to the same producer**.

## Idea

Capture the seam decision so the manager rules it *before* phase-2 investment, instead
of discovering the collision after both contracts freeze. The probe should verify the
overlap precisely at both lane HEADs and recommend among: **(A)** games-web
specializes to the owner-named comic-RPG *presentation layer*, consuming the
mineverse-side projection (`mining_snapshot.v1` / its FLAG-1 read relay) instead of a
bespoke character-sheet endpoint; **(B)** deliberate two-product continuation with an
explicit contract reconciliation (see the sibling convergence capture,
`read-projection-fanin-fourth-consumer-2026-07-11.md`); **(C)** fold — games-web's
comic-RPG skin migrates into mineverse's frontend and the forge subtree goes
historical per its own incubator mechanic. Not prejudged here: (A) looks cheapest
from this read, but mineverse's mandate is the *live economy* while ORDER 001's is
*superbot's existing games* plural — the probe must check whether games-web's roadmap
beyond mining makes the overlap partial, not total.

**Why now:** mineverse is deepening (slice 2 in flight at fetch time) and the batched
read-only-API providing ORDER is not yet routed — this is the last cheap moment to
reconcile: ORDER 001 kept phase 1 mock-first precisely to stay "cheap to redirect".

## Probe report (v0, 2026-07-11 — batched with `../superbot-mineverse/mining-projection-single-source-2026-07-11.md`, the producer-side consequence of the same read-path surface per its own capture text; that file carries the pointer disposition, this file carries the primary battery)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-mineverse/2b1bd0b9695ba4975d358895d0b9a52ab98507f4/control/status.md@2b1bd0b · fetched 2026-07-11T04:33Z
> **Grounding:** https://raw.githubusercontent.com/menno420/product-forge/8c64db4c26591093c24bba068e21250f638f67d6/control/status.md@8c64db4 · fetched 2026-07-11T04:33Z
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/acb786ff7b5abeda534758a23b4f26d2bcdf7f4d/control/inbox.md@acb786f · fetched 2026-07-11T04:33Z

*Timeliness verified live FIRST (the PR #25/#48 discipline — this capture's `Sequence:`
names a closing window): seam UNRULED / providing ORDER UNROUTED at 04:34Z.
fleet-manager's inbox ends at ORDER 016 and none of 001–016 touch the seam or the
read-only API; its status (04:10Z slice) shipped only the model-attribution relay;
superbot has NO `control/inbox.md` at HEAD `bd80501` (raw 404 at the pin —
corroborated by fm status's own "NOT relayed + why: superbot — no control/inbox.md
exists at main HEAD"); both demand-side asks stand unanswered (mineverse FLAGs 1+2
carried verbatim @ `2b1bd0b`; product-forge's phase-2 flag @ `8c64db4`). The window is
still open — probe honest.*

**1. What is this really?** A routing-decision capture, not a feature: ORDER 001 routed
games-web to the forge under "no owning lane exists", and the premise then inverted —
superbot-mineverse now renders the ENTIRE `mining_snapshot.v1` contract (its 04:27Z
heartbeat: deepening well DRY, no in-flight lanes, everything remaining blocked on the
bot-lane FLAGs), while games-web phase-1 is COMPLETE at contract v1.0.1 and phase-2 is
blocked on the same producer. The live object is the miner-state READ PATH, and the
live fact is sharper than the capture knew: THREE mutually different transport shapes
are now demanded for it — FLAG 1's ~60s push relay of `mining_snapshot.v1`, games-web's
proposed live `GET /v1/games-web/character-sheet/{id}`, and the fm conformed mapping's
committed-JSON feed ("API placement: superbot lane, contracted committed-JSON feed per
#1920" — fm inbox ORDER 012 done block) — and no document reconciles them.

**2. What is the possibility space?** The capture's three rulings, plus a transport
axis it couldn't see: **(A) specialize** — games-web becomes the comic-RPG presentation
layer over the mineverse-side projection (consuming `mining_snapshot.v1` fields on
whichever transport the providing ORDER fixes); **(B) reconcile** — deliberate
two-product continuation with the contract reconciliation made explicit (the sibling
captures: field-parity audit + shared schema constant); **(C) fold** — the comic-RPG
skin migrates into mineverse's frontend, the forge subtree goes historical per the
incubator mechanic. Orthogonally: push relay vs committed-JSON vs live GET — where fm
ORDER 012/013 already DECIDED committed-JSON on the superbot lane; the seam ruling
should inherit that, not re-litigate it. On overlap partiality (the capture's own open
check): ORDER 001's mandate is "superbot's existing games" plural, mineverse's is the
live mining economy — but everything games-web has SHIPPED (phase 1) is the mining
character sheet, so today the overlap is total in built surface and partial only in
unbuilt mandate; (A) costs the plural roadmap nothing it has already spent.

**3. What is the most advanced capability reachable by the simplest implementation?**
The sibling's shape, which is why the pair is one probe: ONE bot-side projection module
reading `mining_workflow` / `mining_player_state` / `game_xp_service` and emitting
contracts as serializers over a single in-memory projection — `mining_snapshot.v1`
first, the `games-web.character-sheet` envelope as a second serializer ONLY if the
parity audit says one serialization cannot serve both skins. It is ruling-invariant:
under (A) the second serializer is never built (games-web maps `character-sheet` fields
onto `mining_snapshot.v1` — the fan-in capture's Fact 2 shows its fallback-to-mock
design accepts a committed feed as a conforming live source); under (B) both
serializers are cheap because field semantics are answered once, on the module; under
(C) only one consumer remains. The simplest implementation therefore does not need to
wait for the ruling — which is the strongest argument for routing the producer side
now.

**4. What breaks it?** (i) A late ruling — both demand-side lanes are IDLE on this seam
today (mineverse: "no in-flight lanes … externally blocked"; games-web: "phase-2 stays
BLOCKED"), so every unruled window is two parked lanes and rising odds one side builds
its own transport; (ii) measured field-semantics drift — games-web fixes `gear{}` at 8
slots, mineverse renders 9 slots with wear, found by accident in a cross-repo read;
under (B)-without-audit the contracts freeze incompatible; (iii) the providing ORDER
has NO landing surface — superbot carries no `control/inbox.md` at `bd80501`, so
routing must first pick/create the bus surface (a prerequisite invisible from any
single lane); (iv) verbatim-copying games-web's GET proposal into the ORDER re-opens
the transport question ORDER 012 already closed.

**5. What does it unlock?** The ruling unblocks BOTH lanes' entire externally-blocked
backlogs at once — mineverse's FLAGs 1+2 are its whole remaining ladder, games-web's
phase-2 is its only open edge — and collapses the four-consumer fan-in into one
providing ORDER: one projection, one transport, N serializations, with the parity
audit deciding whether N=1 suffices (which would make (A) free).

**6. What does it depend on?** Manager attention (nothing in fm inbox 001–016 touches
this); a superbot bus surface existing (none at `bd80501`); the field-parity audit
(sibling capture `../superbot-mineverse/snapshot-field-parity-audit-2026-07-11.md` —
the ONE measurable input the ruling lacks, cheap exactly while both contracts are
pre-freeze); and fm ORDER 012/013's standing placement decision (superbot lane,
committed-JSON), which the ruling inherits.

**7. Which lane should build it?** None — this is the manager's routing call, the
park(routed) class: idea-engine cannot rule which lane owns games-web's future, and
the seam spans three repos the manager alone commands. What this probe hands the :30
sweep (decided-and-flagged, not routed-up as a question): recommend **(A)-shaped** —
games-web specializes to the comic-RPG presentation layer consuming the projection the
providing ORDER creates; keep (B)'s reconciliation artifacts (parity audit + shared
constant) as the ORDER's mineverse-side companions because they are what make (A) safe
to take; defer (C) — folding buys no producer-side savings (the projection costs the
same under (A) and (C)) and spends the forge's incubator mechanic.

**8. What is the smallest shippable slice?** Here: this probe + the sharpened
read-only-API fan-in note (shipped in this PR's heartbeat). Fleet-side, the slice the
ranking implies: ONE batched providing ORDER that (i) names the superbot-lane
projection module over `mining_workflow`/`mining_player_state`/`game_xp_service`,
(ii) fixes transport = committed-JSON per ORDER 012, (iii) emits `mining_snapshot.v1`
as the first serialization with FLAG 1's ~60s push cadence reconciled as a parameter
of the SAME module (not a second derivation), and (iv) re-scopes games-web's GET ask
onto the committed feed its own fallback-to-mock transport already conforms to.

**Recommendation: park** — (routed — manager decision): the seam is a fleet routing
call verified live-and-unruled at four HEAD pins (04:32–04:34Z) with both demand-side
lanes idle-blocked on it — decision-ripe now; the probe's ranking (A >
B-artifacts-kept > C) and the three-transports + missing-bus findings ride the
heartbeat's read-only-API fan-in note to the manager's :30 sweep.
