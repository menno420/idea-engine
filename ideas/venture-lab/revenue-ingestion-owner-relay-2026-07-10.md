# Revenue-ingestion owner relay — close the return-on-agent-labor loop before the first sale

> **State:** parked(build-direct — lane doc slice: venture-lab self-serves the docs/ledger convention; slot verified open at lane HEAD 9b504e8, flagged ORDER-worthy via fan-in)
> **Class:** process · **Target:** `menno420/venture-lab`
> **Sequence:** before first owner revenue paste is due (kill-clocks start at the ⚑B/⚑D + itch.io publish clicks; the clicks themselves need not wait — marketplace CSV exports are retro-recoverable)

## Problem

The lane's mission metric is measurable return-on-agent-labor: every candidate
carries a running token-cost line (candidate #1 ≈1.x build sessions, #2 ≈1,
packaging/distribution ≈1 — banked in the heartbeat), and Q-0259's venture mandate
demands conservative, never-overstated economics. But the **revenue side of that
ledger has no ingestion path**: sales will happen entirely inside owner-owned
marketplace accounts (Gumroad / Lemon Squeezy, per ⚑B/⚑D), which agents can neither
create nor read (lane hard rail: no account creation). The heartbeat already flags
the gap — "return-on-agent-labor pending first sale (owner-gated on ⚑B/⚑D)". The
day the listings go live, the ledger goes silently stale and the lane is blind on
its own scoreboard.

## Idea

Define the relay protocol BEFORE first revenue: a `docs/ledger/` sales-inbox
convention where the owner periodically pastes the marketplace's sales CSV export
(or receipt summaries) — one paste per period, zero new accounts, zero spend. The
lane parses it into per-candidate revenue lines sitting next to the token-cost
lines, **net of marketplace fees**, so return-on-agent-labor becomes a computed
number instead of vibes. Includes the empty-period entry ("0 sales this week") so
absence of data is a recorded observation, not a gap — Q-0259: expect bad results,
report them honestly.

## Grounding

- Lane reality @ [`ce22315`](https://github.com/menno420/venture-lab/tree/ce223152719705e22a386b6fdc6d03508a0661c1):
  `control/status.md` token-cost line + "return-on-agent-labor pending first sale";
  README hard rails (no account creation → agents cannot poll the marketplace);
  ⚑B/⚑D publish asks name Gumroad / Lemon Squeezy as the channels.
- Venture mandate Q-0259 r.4 — profitable to fund the fleet, conservative
  expectations, never overstate (superbot
  [`docs/owner/maintainer-question-router.md` @ `6f283b9`](https://raw.githubusercontent.com/menno420/superbot/6f283b91160546af2864a0fd30b6e2d81b148a8f/docs/owner/maintainer-question-router.md), § Q-0259).
- Q-0259 fit: lane-internal ledger doctrine; no games/rebuild resources touched.

**Why now:** the format is cheapest before sales exist — defined after launch, the
first weeks of revenue history get reconstructed from owner memory or lost.

## Probe report (v0, 2026-07-11)

Verify-first at live lane HEAD `9b504e8` (ls-remote 2026-07-11T05:40:19Z; the lane moved 4 merges past the capture's pin `ce22315` and the last fan-in sighting `9f1b616` — #29 heartbeat, #30/#31 ORDER-005, #32 kit v1.9.0, none ledger-shaped): NOT overtaken — the slot is OPEN. No `docs/ledger/` exists (the only ledger-named file, `docs/research/venture-ledger.md`, is a per-candidate build/status record); a tree-wide grep for sales/CSV/payout/export ingestion finds nothing inbound (the single CSV hit is a product feature, `candidates/cc-cost-lens/INTAKE.md:6`); the PR #25 intake template is forecast-only (`candidates/stripe-webhook-test-kit/INTAKE.md:22-24` — Conservative-revenue, Payback-time, Token-cost; no recording mechanism); no inbox ORDER covers ingestion (ORDERs 001–005 @ `9b504e8`); the unfrozen ⚑B/⚑D click scripts end at "test purchase shows zip delivered" with zero post-publish reporting step (`docs/launch/membership-kit/owner-actions.md` @ `9b504e8`); "Return-on-agent-labor pending first sale" still sits at `control/status.md:132`. The self-serve pattern (five prior datapoints) did NOT fire here: the lane self-reports "idling on backpressure — frontier owner-gated" (`control/status.md:12`) — it cannot see this head as agent-doable work. Full battery below.

**1. What is this really?** An evidence-channel definition, not a revenue feature. The lane's no-accounts rail (`README.md:28-30` @ `9b504e8`) makes the owner the only legal path for marketplace truth to enter the repo; this defines that ONE ingress so sales, fees, and zeros become committed evidence. It is the missing half of a metric the lane already carries — token-cost lines exist on the heartbeat and in venture-ledger.md, revenue lines have nowhere to land.

**2. What is the possibility space?** Minimal: a `docs/ledger/README.md` convention — paste inbox + one entry grammar (period · source · gross · fees · net · per-candidate rows) + the empty-period rule ("0 sales this period" is a recorded observation). Middle: per-source normalization notes (Gumroad / Lemon Squeezy / itch.io exports differ), per-candidate rollups beside venture-ledger.md's token-cost sections, a computed return-on-agent-labor line on the lane heartbeat. Max: a parse script + CI check, intake kill-clock integration (the "first paid sale in 14 days" signals read the ledger), fleet-level revenue rollup for the manager's sweep.

**3. Most advanced capability by the simplest implementation?** The bare convention doc buys the whole mission metric: with revenue entries landing next to existing token-cost lines, return-on-agent-labor becomes arithmetic and the intake kill-clocks gain an evidence channel — one markdown file, zero code.

**4. What breaks it?** (a) Owner non-compliance — a paste ritual that never happens; mitigate by making the empty-period entry a ten-second paste and binding the ask to sittings the owner already takes (the ⚑B/⚑D and itch.io publish sittings are natural anchors). (b) Format drift — three marketplaces, three export shapes; the convention must accept raw exports verbatim (the lane normalizes) and never demand owner-side reshaping — Q-0263.2's paste-ready doctrine, applied in reverse. (c) Fee invention — net-of-fees must come from the export's own fee columns, never derived from published fee schedules ("not measured" beats invention, Q-0259). (d) Attribution ambiguity — one export spanning products needs the product column preserved; the lane now has THREE candidates (Stripe Webhook Test Kit ⚑E queued, `control/status.md:107-108`), not two. Reachability (battery Q4/Q6 discipline): the consumer side is trivially reachable (a lane agent reading a committed file); the producer side — owner-facing CSV/sales export on Gumroad, Lemon Squeezy, and itch.io dashboards — is behind owner login and unreachable across the rail from here, NOT re-verified; the capture already hedges with "or receipt summaries" as the fallback, and the convention should keep that hedge.

**5. What does it unlock?** Computed return-on-agent-labor (the lane's scoreboard, Q-0259 r.4 conservative economics); evidence-fed kill/scale decisions — the intake validation-signal clocks (`candidates/stripe-webhook-test-kit/INTAKE.md:19`) currently have NO evidence channel, so without this they fire on vibes; honest zero-records; day-one capture of the Lumen Drift itch.io datapoint (itch.io is unreferenced in the lane tree — 0 grep hits @ `9b504e8` — despite the #97 OWNER-ACTION making it a live third source); the fleet's first revenue-reporting surface.

**6. What does it depend on?** Owner: a periodic paste — the only cross-rail channel (rail verified at `README.md:28-30`). Lane: one doc slice it can land NOW while idle. No cross-lane dependency, no code. The sequencing constraint is SOFT: the publish clicks need not wait (marketplace sales history and exports are retro-downloadable, so pre-relay sales stay recoverable), but the convention should exist before the first paste is due — the kill-clocks start at publish.

**7. Which lane should build it?** venture-lab — it owns every surface this binds to (intake template, token-cost lines, kill rules, owner-actions click scripts); idea-engine defines nothing lane-internal (Q-0260/Q-0264). Routed via the heartbeat fan-in, flagged ORDER-worthy: the lane's backpressure-idle self-report proves it will not self-discover this head.

**8. What is the smallest shippable slice?** One venture-lab PR, zero code: `docs/ledger/README.md` (paste path, entry grammar, empty-period rule, one worked example with fake numbers) + one line per candidate INTAKE.md binding its validation-signal kill-clock to the ledger + a post-publish step appended to the owner-actions click scripts ("after publish: paste the sales export into docs/ledger/ each period"). Parse tooling waits until real pastes exist.

**Recommendation: park** — build-direct (lane doc slice): the slot is verified open at lane HEAD `9b504e8`, the entire kernel is one lane-internal markdown convention the currently-idle lane can land immediately, and nothing is evidence-shaped for sim-lab (a protocol definition has no hypothesis to settle; its one unknown — will the owner paste — is settled by asking, not simulating). Flagged ORDER-worthy in the fan-in so the manager's sweep routes it; the owner's publish clicks stay un-gated.
