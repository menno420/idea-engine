# Post-EAP playtest kit — a paste-ready bundle for the owner's pending verdict

> **State:** parked(build-direct — one lane PR: pinned playtest artifact for the tree at sitting time + player-visible per-patch notes generated from the committed proof bundles + keep/tune/drop verdict form, plus a one-line fleet-manager owner-queue item-3 WHERE fix pointing at the kit; nothing sim-shaped — the bundle is proven by the owner sitting itself; owner-sitting-bound, EAP window ends 2026-07-14 and the sitting is shared with Lumen Drift — the manager routes it NOW or explicitly lets it lapse)
> **Class:** product · **Target:** `menno420/pokemon-mod-lab`
> **Grounding:** https://github.com/menno420/fleet-manager@1afca50e171a33591f8481f0ac837b989c280425 · fetched 2026-07-11T07:32Z
> *(pin annotation: probe-time re-grounding — the capture's superbot fleet-manifest pin `53fb5ef` is superseded (manifest = tombstone since fleet-manager PR #59 `b0639a9`); fleet state re-read at fleet-manager HEAD `1afca50` — roster gen #5 (generated 2026-07-11T04:28Z) + `docs/owner-queue.md` item 3 + `docs/review-queue.md` pokemon#8 row + `docs/findings/night-review-2026-07-10.md`; the lane repo itself re-verified DARK 2026-07-11T07:32Z: raw 404 on `control/status.md` and `README.md`, `git ls-remote` auth wall, GitHub MCP scoped to idea-engine — all lane facts below are roster/manager-relayed, shape-not-content per the README DARK-lane recipe)*
> **Sequence:** before the owner's post-EAP playtest sitting (window ends 2026-07-14; one shared sitting with the Lumen Drift play kit per the fm night-review's bundled-session plan)

## Problem

The lane's only pending gate is an owner item: **"playtest verdict"** (manifest row @
53fb5ef), and the owner ruled he will play the builds **after the EAP** (Q-0259 r.5),
whose window closes **2026-07-14** (manifest post-launch note). But nothing in the
lane's visible state names a packaged artifact path for that playtest — the parked
ender predates the ruling, and gba-homebrew's parallel row shows what "ready" looks
like ("owner: play it (~15 min)"). An owner ask that requires the owner to assemble a
build chain himself is a drafting defect by fleet doctrine (Q-0263 rule 2 / kit ORDER
008 class: asks are paste-ready or they don't reach the owner).

## Idea

Ship a **playtest kit** as one lane PR: (1) a pinned patch artifact for the current
12-patch build — patch format only, never a ROM (see the companion patch-only-egress
capture); (2) a one-page "what you'll notice" note listing the 12 QoL patches in
player-visible terms, so the verdict can name patches, not vibes; (3) exact apply+run
steps (patcher + emulator, click-path style); (4) a **verdict form** at the bottom —
3-5 fill-in lines (what felt good / what felt bad / option-board pick / blockers) so
the playtest output arrives machine-consumable and the improvement round (Q-0259 r.5:
"improvement rounds follow") boots from evidence instead of a chat paraphrase. Total
owner cost target: ~15 minutes, matching the gba-homebrew bar.

## Grounding

- Manifest pokemon-mod-lab + gba-homebrew rows and EAP-window note @
  [`53fb5ef`](https://raw.githubusercontent.com/menno420/superbot/53fb5ef9a294ab304b679dedd44ead55849295d5/docs/eap/fleet-manifest.md)
  (fetched 2026-07-10 ~20:35Z): "owner: playtest verdict + concept pick"; gba row
  "owner: play it (~15 min)"; "EAP window: through 2026-07-14".
- Q-0259 r.5 (owner plays after EAP, improvement rounds follow) + Q-0263 rule 2
  (paste-ready-or-nothing owner asks) @
  [`53fb5ef`](https://raw.githubusercontent.com/menno420/superbot/53fb5ef9a294ab304b679dedd44ead55849295d5/docs/owner/maintainer-question-router.md).
- Caveat, stated honestly: the lane repo is private/unreadable from here — if session
  008 already left a packaged artifact, this capture collapses to "add the verdict
  form and re-pin the artifact"; the first-boot session verifies against its own tree.

**Why now:** the EAP ends 2026-07-14 — the playtest becomes possible in days, and a kit
prepared before the owner sits down is the difference between a 15-minute verdict and a
stalled improvement round.

## Probe report (v0, 2026-07-11)

*Probed 2026-07-11T07:30–07:45Z, single-pass (no panel: bounded product slice, reversible,
no security/spend/public surface). Verify-first, per the DARK-lane recipe (README § Idea
file grammar) — the lane is still unreadable from here, re-verified three ways at probe
time (2026-07-11T07:32Z): raw fetch 404 on `control/status.md` AND `README.md`,
`git ls-remote` hits the auth wall ("could not read Username … terminal prompts
disabled"), GitHub MCP scoped to idea-engine only; fleet-manager's own record agrees
("Unauthenticated curl to the private pokemon repo 404s", fm `control/status.md` @
`1afca50`). So every lane fact here is manager-relayed at fleet-manager HEAD
`1afca50e171a33591f8481f0ac837b989c280425` (raw-main fetch 07:31Z verified byte-identical
to the HEAD blob), scoped shape-not-content. What the live registry shows — three capture
premises MUTATED, one intact: (1) the lane is UN-PARKED and AWAKE: roster gen #5
(`docs/roster.md`, generated 2026-07-11T04:28Z) rows it FRESH — heartbeat 04:03:05Z (~24m
at generation), phase "Option A (Emerald QoL+ deepening, Q-0266 flagged reversible", kit
v1.6.0 · check green · engaged yes, hourly wake `trig_01BTJjkMVMKtWPjuYe7643Hi`
`30 * * * *` (fresh-session mode, per the gen #4 note "pokemon UN-PARKED (Q-0266
decide-and-flag → Emerald QoL+; owner can override)"), repo evidence `297f67b`
04:13:49Z — the capture's "parked ender" framing is historical. (2) The owner ask now
EXISTS, half-drafted, manager-side: fm `docs/owner-queue.md` item 3 @ `1afca50`
("pokemon-mod-lab playtest — 4 game-feel patches, ONE pass"; HOW: "one play session; drop
reactions as a PR comment or inbox order — 'keep/tune/drop' per patch is enough"),
updated 2026-07-11: scope grown to the 12-patch #4–#8 train PLUS session-012 QoL+ slice 2
(pokemon PR #16, merge `aeaa4f7`, 02:40:09Z — bag R-tag art), and the review-queue row
pokemon#8 now stays open SOLELY on this playtest — the sha1/byte-identity code half is
manager-verified (fm PR #61 `5244a1c`, chain `eec6d6af` → … → `805aeaee` with two
independent CI-log anchors, fm `docs/review-queue.md` @ `1afca50`). (3) The kit-shaped
GAP is still open: item 3's WHERE is "build artifacts / instructions in
menno420/pokemon-mod-lab … PRs #4–#7" — no pinned artifact path, no player-visible notes
page, no verdict form is named on ANY manager-visible surface; and fm's own night review
(`docs/findings/night-review-2026-07-10.md` Q4 + recommendation 12 @ `1afca50`)
INDEPENDENTLY prescribes exactly this idea — "one bundled 30–45 min session (patched
Emerald ROM + Lumen Drift + 6-question checklist), prepared entirely by agents … That
preparation session should be ordered now" — yet the ORDER scan finds none: the lane's
relayed orders on fm surfaces are ORDER 002 (hourly wake, roster row) and ORDER 004
(model-attribution relay, lane PR #19 `743525d`, fm status @ `1afca50`), ORDER 003 sat
"unconsumed" at roster gen #1 (fm `control/inbox.md` @ `1afca50`) — no playtest-kit order
is evidenced. Honest caveat carried forward from the capture: the lane tree itself is
DARK — if a lane session already left a kit, only the lane (or fm's authenticated read)
can see it; this probe asserts the MANAGER-VISIBLE gap, not the lane tree's contents.*

**1. What is this really?**
Owner-attention compilation for the fleet's single highest-leverage pending click. The
review-queue's oldest open row (pokemon#8) now hangs ENTIRELY on one taste verdict no
agent can produce, and fm's night review ranks preparing its kit #1–2 on the owner
queue. Since the capture, the ask itself materialized (owner-queue item 3, keep/tune/drop
grammar) — so the idea has NARROWED from "create the ask + bundle" to "make the existing
ask's WHERE real": pin the artifact, name the patches in player-visible terms, attach the
verdict form. The form half gained value since capture: the lane is now actively
DEEPENING QoL+ (Option A, hourly wakes), so per-patch keep/tune/drop reactions are no
longer just a gate verdict — they are live steering data for work already in flight, and
Q-0266 is explicitly "flagged reversible", meaning the sitting can also revoke the
direction cheaply if the form captures it.

**2. What is the possibility space?**
Four axes. **Bundle carrier:** an in-lane `docs/play/` kit page (the gba-homebrew play-kit
shape, already probed park(build-direct) at PR #34 and since realized lane-side as
`dist/lumen-drift.gba` v1.3) vs manager-side prose only (owner-queue item text — no lane
write needed but cannot pin artifacts it cannot see) vs both (lane builds, fm's item 3
WHERE points at it) — both, thinly, dominates. **Artifact form:** committed ROM inside
the private repo (rail-fine while private) vs patch-only (BPS/UPS against a clean base —
REQUIRED for anything leaving the repo per the companion patch-only-egress capture;
inside the repo it is a hygiene choice) — the kit should pin whichever the lane already
builds, plus the sha1 the proof chain anchors (`805aeaee…` at PR #8; later heads extend
it). **Verdict-form transport:** PR comment (item 3's HOW today — zero setup, but
free-prose) vs a committed fill-in form file (machine-consumable, boots the improvement
round from evidence) vs inbox order — form file, with the PR-comment path kept as
fallback. **Scope freeze:** the capture's "12 QoL patches" vs the LIVE tree at sitting
time (already 12+: session-012 slice 2 landed, Option A keeps adding hourly) — the notes
and form MUST be generated from the lane tree at kit-build time, never from this
capture's list; a frozen kit is stale on arrival.

**3. What is the most advanced capability reachable by the simplest implementation?**
The lane's committed proof bundles (`docs/proof/session-00N/`, per the fm review-queue
verification: per-session sha1-chain tables, five bundles for #4–#8) already carry
per-patch identity — so ONE lane PR that generates the notes+form FROM those bundles gets,
nearly free: (a) a player-visible checklist where every line is pinned to its patch,
session, and ROM sha1 (the verdict can name patches, not vibes — the capture's core); (b)
a verdict form whose keep/tune/drop lines are machine-joinable back to the exact commits
to keep, tune, or revert — the improvement round and the live Option A deepening boot
from evidence instead of a chat paraphrase; (c) the ~15-minute owner cost the gba row
priced, because apply+run steps ride the same page. The manager side is one line: item
3's WHERE flips from "build artifacts / instructions … PRs #4–#7" to the kit link.

**4. What breaks it?**
- **The DARK wall (this probe's own bound).** The lane tree may ALREADY carry a kit —
  session 008+ is invisible from here. The capture priced this honestly ("collapses to
  add the verdict form and re-pin the artifact"); the slice's first lane-side step is
  verify-own-tree, and the fm-side WHERE fix is worth shipping in either branch.
- **The window.** EAP closes 2026-07-14; the night review's honesty clock ("if the
  playtest hasn't happened within ~3 days" of 07-10) expires ~07-13 into "stop the
  game-feel patch line". A kit that misses the sitting doesn't decay to zero — the form
  still structures a later verdict — but the unrecoverable part is steering the Option A
  deepening WHILE it runs; every hourly wake past the sitting deepens unverdicted work.
- **Scope drift.** Option A adds patches hourly; a kit enumerating a fixed list is wrong
  by the sitting. Broken by construction unless notes/form are tree-generated (Q2/Q3).
- **The egress trap.** The repo is private and the rail says never publish; a committed
  in-repo ROM is fine, but the kit page and form must not route ROM bytes OUT (email,
  artifact links to third parties) — patch-format only for anything leaving, per the
  companion doctrine capture; the kit PR should state that reading.
- **Routing limbo (the actual observed failure mode).** The night review ORDERED this
  prepared "now" on 2026-07-10; nothing manager-visible did it. An idea parked here
  without the window flag re-creates exactly that — hence the fan-in flag this probe
  routes (below), not just a park.

**5. What does it unlock?**
The last open half of review-queue pokemon#8 (the fleet's oldest open review row)
becomes clickable at its advertised ~15-minute price. The improvement round (Q-0259 r.5)
and the LIVE Option A deepening get machine-consumable steering — including a cheap
reversal path for the Q-0266 decide-and-flag if the owner's reactions say so. The
one-sitting bundled playtest the night review prescribed becomes real: gba-homebrew's
half already exists (Lumen Drift v1.3 artifact + this repo's standing ⚑ OWNER-ACTION),
this kit is the missing Emerald half of the SAME 2026-07-14 sitting. And the fleet gets
its second play-kit datapoint, turning last-mile playtest packaging into a pattern every
finished game inherits.

**6. What does it depend on?**
- The owner sitting still being ahead (hard calendar bound 2026-07-14) — verified ahead
  at probe time; owner-controlled.
- Lane capacity: the lane is AWAKE (hourly fresh-session wakes) and mid-deepening — no
  new capability needed, only routing; the lane owns every input (tree, proof bundles,
  build) — verified reachable BY THE LANE, not from here (the DARK bound).
- The proof-bundle surface existing as fm verified it (five bundles, sha1 chains) — the
  notes/form generator keys on it; manager-verified 2026-07-11 (fm PR #61).
- fm's owner-queue as the ask surface (item 3 lives there; one-line WHERE fix is an fm
  write, not a lane write).
- NO cross-lane build dependency; co-consumer only — the shared sitting with the Lumen
  Drift kit (both feed one owner session; neither blocks the other).

**7. Which lane should build it?**
`menno420/pokemon-mod-lab` builds the bundle — it owns the tree, the proof bundles, and
the build; this repo cannot write lane files (Q-0260) and cannot even read this one.
`fleet-manager` owns the one-line owner-queue WHERE fix and the routing decision (its own
night review already self-prescribed ordering the preparation "now"); with the lane awake
hourly, either an fm ORDER or lane self-serve lands it — the lane-self-served prior is
the measured default for lane-sized heads (×2 in ~24h per this repo's PR #123 notes).
NOT sim-lab: no reproducible-evidence question exists — the kit's validation event is
the owner sitting itself, so no outbox proposal rides this probe.

**8. What is the smallest shippable slice?**
One lane PR + one fm line. Lane PR: (1) verify-own-tree first (if a kit already exists,
collapse to form+re-pin per the capture's caveat); (2) pin the playtest artifact for the
tree at build time — in-repo ROM or patch, WITH the proof-chain sha1 anchor; (3) a
`docs/play/`-shaped one-pager: apply+run steps plus per-patch player-visible notes
GENERATED from the committed proof bundles (12-patch #4–#8 train + session-012 slice 2 +
whatever Option A has landed); (4) a verdict form — keep/tune/drop + one free line per
patch, a deepening-direction line (Q-0266 is reversible — say so on the form), blockers.
fm side: owner-queue item 3 WHERE → the kit link. Done-when: the owner can go from
owner-queue item 3 to playing in ≤15 minutes, and the filled form lands as a committed,
machine-consumable artifact the improvement round consumes.

**Recommendation: park** — build-direct: a lane build slice (pinned artifact +
tree-generated player-visible notes + keep/tune/drop verdict form) plus a one-line fm
owner-queue WHERE fix, proven by the owner sitting rather than any simulator; it is
owner-sitting-bound on the SAME 2026-07-14 window as the Lumen Drift kit, so the manager
should route it NOW (fm order or lane self-serve — the lane wakes hourly) or explicitly
let it lapse with the window.
