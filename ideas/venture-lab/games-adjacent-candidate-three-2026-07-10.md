# Games-adjacent candidate #3 — publish a finished fleet game instead of building anything new

> **State:** parked(build-direct — owner-gated: publish = itch.io account/money click behind the post-EAP playtest go/no-go, window ends 2026-07-14; asset ready at gba-homebrew HEAD)
> **Class:** venture · **Target:** `menno420/venture-lab`
> **Sequence:** after gba-homebrew EAP owner playtest (window ends 2026-07-14) + owner itch.io account click

## Problem

The lane's standing default between orders is "deepen the current top candidate",
and both existing candidates (membership-kit, template-packs) target the same
boilerplate/template buyer through the same marketplace channel — the portfolio has
no second distribution thesis. Q-0259 weights the fleet toward the games completion
wave and the rebuild pace, so any candidate #3 that demands fresh build effort from
a games lane would conflict with the priority ruling. But the fleet already owns a
**finished, legally publishable game**: gba-homebrew's Lumen Drift is SCOPE-COMPLETE
(session 7, close-out #24) and public-by-design — no Nintendo-derived content.

## Idea

Candidate #3 = publish Lumen Drift as a pay-what-you-want itch.io listing (browser
emulator embed + ROM download). Distribution-first: itch.io's homebrew/retro section
is a named, browsable first-ten-customers channel — the storefront IS the audience,
unlike the boilerplate candidates which must bring their own. Cost honesty per
Q-0259: expect ≈$0 direct revenue (PWYW homebrew baseline); the durable value is a
**proven publish pipeline for every future fleet game** plus the lane's first
second-channel distribution data. Sequencing is the point, not a caveat: strictly
post-EAP, behind the owner's playtest (Q-0259 r.5 — the owner plays the builds after
the EAP) and the itch.io account click (lane hard rail); **zero games-lane build
effort is demanded — the artifact already exists**, so the candidate rides the games
wave instead of competing with it.

## Grounding

- Manifest gba-homebrew row: "Lumen Drift SCOPE-COMPLETE (session 7, close-out #24);
  public-by-design (no Nintendo-derived content); owner: play it (~15 min)"
  ([superbot @ `6f283b9`](https://raw.githubusercontent.com/menno420/superbot/6f283b91160546af2864a0fd30b6e2d81b148a8f/docs/eap/fleet-manifest.md), fetched 2026-07-10).
- Q-0259 r.4 (venture mandate: any methods allowed, conservative expectations) +
  r.5 (owner plays after EAP; games program is the priority wave): superbot
  [`docs/owner/maintainer-question-router.md` @ `6f283b9`](https://raw.githubusercontent.com/menno420/superbot/6f283b91160546af2864a0fd30b6e2d81b148a8f/docs/owner/maintainer-question-router.md).
- Lane rails @ [`ce22315`](https://github.com/menno420/venture-lab/tree/ce223152719705e22a386b6fdc6d03508a0661c1):
  README "NO account creation … without an explicit owner action" → itch.io account
  is a queued click, same shape as ⚑B/⚑D.

**Why now:** the sequencing gate is dated — the owner's post-EAP playtest (EAP window
ends 2026-07-14) can double as this candidate's go/no-go if the scored capture exists
before he sits down to play.

## Probe report (v0, 2026-07-11)

Verify-first at live lane HEADs (fetched 2026-07-11T05:23:36Z): NOT overtaken — no Lumen Drift / itch.io ORDER or queued work exists in venture-lab (`control/inbox.md` @ `0ad0ea4` has only ORDERs 001–005, all done; its unfrozen ⚑B/⚑D publish flags are membership-kit and template-packs, not this) or gba-homebrew (`control/inbox.md` @ `31c8672` has ORDERs 001–003, none about publishing). One load-bearing capture fact went STALE in the right direction: the ROM surface now EXISTS — gba-homebrew `dist/lumen-drift.gba` v1.3 (167,996 bytes, sha256 `195a86795e57e2fa0059a96782f1ac7a147cbcebc0cb28a96f353e5d9babae94`, provenance row `dist/README.md` @ `31c8672`, CI rebuilds and re-hashes it on every PR), and its README says the game is playable NOW via that download. Full battery below.

**1. What is this really?** A distribution test wearing a game's clothes — zero build effort converts an already-finished, already-hashed artifact into the fleet's first second-channel storefront listing plus a reusable publish pipeline; the deliverable is the pipeline and the channel datapoint, not the (≈$0 PWYW-honest) revenue.

**2. What is the possibility space?** Minimal: bare PWYW ROM-download listing. Middle: listing + browser-embed emulator + screenshots + devlog post. Max: a standing fleet "games shelf" on itch.io where every completed games-wave title auto-lands, with per-title analytics feeding venture-lab's revenue-ingestion relay. Adjacent: the live page doubles as playtest-distribution surface for future titles.

**3. Most advanced capability reachable by the simplest implementation?** The single bare listing already yields the durable capability: a proven finished-game→live-storefront path the entire games completion wave inherits, one owner sitting per title thereafter.

**4. What breaks it?** (a) The owner click — account creation and external publishing are rail-banned for agents on BOTH lanes (venture-lab README @ `0ad0ea4`: "NO account creation … without an explicit owner action"; gba-homebrew README @ `31c8672`: "External publishing of Track B (itch.io, forums, anywhere) still requires an owner action"), so no slice of the kernel is agent-executable. (b) Sequencing — publishing before the owner's post-EAP playtest (window ends 2026-07-14) inverts Q-0259 r.5. (c) Framing — judged as a revenue candidate instead of a pipeline/channel candidate, ≈$0 PWYW reads as failure-by-design. (d) Queue saturation — venture-lab already has two unfrozen publish clicks (⚑B/⚑D) waiting on the same owner; a third click on a stalled queue risks none landing.

**5. What does it unlock?** First non-marketplace distribution datapoint; a proven publish path for every future finished fleet game; a live revenue source for the revenue-ingestion-owner-relay head (which must exist before first revenue); a playtest-distribution surface.

**6. What does it depend on?** Owner: post-EAP playtest go/no-go on Lumen Drift v1.3, then one sitting — itch.io account → new project → PWYW → upload `dist/lumen-drift.gba` → publish. Asset: DONE at gba-homebrew HEAD (v1.3 + sha256 provenance, CI-verified). Agent-side prep venture-lab CAN self-serve on go-signal: full listing kit (copy, screenshots, conservative-forecast attachment — its own intake template already binds forecast+payback fields). Reachability check passes: the artifact the listing needs exists and is downloadable at HEAD; nothing here is evidence-shaped — the only unknown (does anyone pay for PWYW homebrew) is settled by publishing, not simulating.

**7. Which lane should build it?** venture-lab — it owns the venture surface (intake template, forecast attachment, revenue relay) and the remaining agent work is listing prep; gba-homebrew's part is already done, honoring the zero-games-lane-effort premise.

**8. What is the smallest shippable slice?** venture-lab drafts the complete paste-ready listing kit (title/description/PWYW copy + screenshots + forecast + step-by-step owner checklist) so the owner's post-EAP sitting is a single paste-and-click; the click itself is the un-shippable-by-agents kernel.

**Recommendation: park** — build-direct and owner-gated: the artifact already exists (zero build), everything remaining is an owner account/money click sequenced behind the post-EAP playtest (window ends 2026-07-14), and nothing is evidence-shaped for sim-lab; venture-lab self-serves the listing-kit prep on the owner's go.
