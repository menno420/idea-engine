# Public server leaderboards on the committed feed — the zero-auth slice of the stats ask

> **State:** parked(routed — the producer is production-DB egress, not exporter extension: no committed feed carries game runtime data, so the `leaderboards` family is the natural zero-auth FIRST RUNG of the batched superbot read-only-API ORDER; websites page build-direct once the family lands — see probe report)
> **Class:** product · **Target:** `menno420/websites` (one small cross-lane dependency on `menno420/superbot`: a new contracted export family — same class as PROPOSAL 002 phase 2's, NOT the read-only API)
> **Grounding:** https://raw.githubusercontent.com/menno420/idea-engine/698fd93869f8a05200f26fde45bbd71596323e6a/ideas/websites/superbot-site-stats-data-story-2026-07-10.md@698fd93 · fetched 2026-07-10T22:08Z
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/9624c5399f5b1a3da293c07ce930e8b0410d79e4/docs/eap/fleet-manifest.md@9624c53 · fetched 2026-07-10T22:08Z
> **Sequence:** before the PROPOSAL 002 stats phase — it deliberately front-runs the OAuth sim verdict and the unrouted superbot read-only API by shipping only what needs neither

## Problem

The owner's stats ask ("clearly see your stats for the bot, per server", idea §1)
is double-blocked: the OAuth trust gate awaits a sim-lab verdict (PROPOSAL 002,
still queued behind INTAKEs 001–002), and the superbot read-only API it needs is
an unrouted cross-lane ORDER with two waiting consumers (probe Q4: "unrouted,
phase 3 deadlocks regardless of the sim verdict"). Meanwhile a large slice of
that value is not personal at all: leaderboards — top miners, depth records, XP
ranks per server — which the bot already displays publicly in-channel to anyone
who types the command.

## Idea

Ship the trust-free slice first: a new contracted export family `leaderboards`
(top-N per game per server: XP/level, coins, mining depth, fishing, creature
game — small, bounded rows), produced by superbot's existing exporter per the
PR #1920 versioned fail-closed pattern, rendered by websites over the exact raw
fetch path `dashboard/data_source.py` uses today. Zero OAuth, zero backend, zero
new server surface — per-user *private* views stay behind the sim gate where they
belong. One real design point, named honestly: publishing in-server display names
on the open web is wider exposure than in-channel display, so the family should
carry a per-server opt-out and/or name masking — a data-shape decision, not an
auth surface. Bonus: this is the same family-extension muscle the phase-2
explorer needs (probe Q4: "B's real cost is contract extension, not UI") —
exercised once on the smallest family.

**Why now:** the stats phase's two blockers have no ETA, and the manifest row
confirms the lane is live and hungry (3 services on Railway, 4-hourly wake
verified) — this converts the stats ask's demonstrable 80% into routable
phases-1–2-class work instead of leaving ALL stats value parked behind the
slowest dependency.

## Probe report (v0, 2026-07-10)

> **Grounding:** https://raw.githubusercontent.com/menno420/websites/98ce6c097e438f97d8efc943132e631309a99903/dashboard/data_source.py@98ce6c0 · fetched 2026-07-10T23:55Z
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/7c6278ec990d9230aac439cb748465bf23bcec56/dashboard/data/dashboard_data_contract.json@7c6278e · fetched 2026-07-10T23:55Z
> **Grounding:** https://raw.githubusercontent.com/menno420/sim-lab/8713f261c99634156dd6facda03e396b888a9e8a/control/outbox.md@8713f26 · fetched 2026-07-10T23:54Z
> **Sequence:** after the batched superbot read-only-API providing ORDER's first rung — this probe REVERSES the capture's front-run premise (the producer cannot dodge the fan-in); only the websites-side contract-pin + fixture work is order-independent

*Timeliness verified live FIRST (the PR #25 lesson). Transport-verified via `git
ls-remote refs/heads/main` at probe time (23:50Z): websites HEAD
`98ce6c097e438f97d8efc943132e631309a99903` (moved from PR #40's `8dc5ec2f`), superbot
HEAD `7c6278ec990d9230aac439cb748465bf23bcec56` (moved from the heartbeat's `c5f501e`),
sim-lab HEAD `036860049a55f435d32bd8d6226574c2691ab30f` (moved from `8713f26`; VERDICT
003 re-read raw at the pinned `8713f26` — unchanged, ruling buildable-with-named-changes,
named changes (1) §5 checklist → the spike's concrete control set + Secure/HttpOnly/
SameSite + HSTS + TLS-only, (2) HOLE-1 stale guild membership, (3) HOLE-2 `guilds`
over-read, (4) route the §4 read-only API as a superbot-lane ORDER FIRST — "UNBUILT AND
UNROUTED", phase 3 deadlocks regardless of the verdict). The decisive live finding, at
superbot HEAD `7c6278e`: BOTH committed feeds are repo-derived with ZERO game runtime
data — `dashboard/data/dashboard.json` (meta.build `c5f501e4`, 13 top-level families:
catalogue/ideas/bugs/reviews/updates/bot_changelog/telemetry/env_usage/cogs/settings/
access/synonyms; `telemetry` is AGENT-SESSION telemetry, not game data) and
`botsite/data/console.json` (sessions/ideas/bugs/bot_changelog/telemetry); the contract
pins only `["meta","bugs"]` at version 1; `dashboard/data/leaderboards.json` 404s at
HEAD; and the producer `scripts/export_dashboard_data.py@7c6278e` is a pure-stdlib
STATIC REPO SCAN (sources: AST-parsed registry, docs markdown, `.sessions/` — "all
read-only, never imported"; it never touches the bot's Postgres). websites' consumption
seam is live as described: `dashboard/data_source.py@98ce6c0` raw-fetches both feeds
anonymously with the never-fake-data envelope and a render-time contract-version pin.*

**1. What is this really?**
Not what the capture priced. The capture says "produced by superbot's existing exporter
per the PR #1920 pattern" — but the existing exporter is a static repo scan with no
database access, and NO committed feed at superbot HEAD carries a single row of game
runtime data (verified above; leaderboard rows — top-N XP/coins/depth per server — live
in the production Postgres). So this is really TWO different-shaped halves fused by one
premise error: (a) a websites-side render slice that genuinely is pattern-proven,
zero-auth committed-feed work, and (b) a superbot-side producer that is NOT "family
extension" but the fleet's first PRODUCTION-DATA EGRESS to a committed file — the same
DB-read capability the §4 read-only API needs, minus auth and per-user scoping. The
capture's "family, not API" distinction dissolves on contact with the live tree: the
family needs the API's core plumbing.

**2. What is the possibility space?**
- **Producer mechanism (the open axis):** a bot-runtime scheduled job that commits
  `leaderboards.json` back to the repo · a credentialed CI job reading the DB · or
  folding the export into the read-only API service as its "materialize to file" mode.
  None exists today; none was found committed at HEAD (not exhaustively enumerable from
  this seat — raw path only — but both known feeds and the one obvious filename were
  checked). Which mechanism is a superbot-lane design call inside the providing ORDER.
- **Data shape:** top-N bounded rows per game per server (XP/level, coins, mining depth,
  fishing, creature game), family-versioned per the #1920 slice semantics — small and
  cacheable by construction.
- **Privacy dial:** in-server display names on the open web is WIDER exposure than
  in-channel display; the capture's per-server opt-out and/or name masking is the right
  design point, and superbot's own two-site split doctrine already says the public
  `site.json` "physically cannot contain … any per-guild value — redaction by
  construction" (exporter docstring @ `7c6278e`) — a public per-guild leaderboards feed
  is a DELIBERATE doctrine carve-out, an owner data-shape decision, not a sim question.
- **Consumer skins:** the websites page first; product-forge's games-web (ORDER 001)
  renders the same rows; the story page (phases 1–2) can quote them.

**3. What is the most advanced capability reachable by the simplest implementation?**
For websites: a live public leaderboards page for the cost of ONE page module — the
whole transport already exists (`data_source.py`'s anonymous raw fetch + TTL cache +
honest-degrade envelope + render-time contract pin, all live at `98ce6c0` serving ~12
pages). For superbot: rung 1 of the read-only API for free — a committed top-N feed
proves the production-DB egress path, the contract-family growth ritual (version bump +
producer parity + fail-closed checker), and the privacy masking rule ONCE, zero-auth,
before the token-scoped per-user API stacks auth on the same plumbing. The simplest
implementation of THIS idea is the de-risking first slice of the HARD dependency, not a
way around it.

**4. What breaks it?**
- **The premise error (decisive):** treating the producer as "existing exporter work"
  ships a websites page against a feed that cannot exist — the exporter has no DB
  access, and giving the static-scan CI job production credentials is a new security
  surface nobody has designed. The producer belongs inside the batched providing ORDER.
- **Doctrine collision:** the public-artifact "no per-guild value" redaction rule (Q2)
  — an unexamined leaderboards family quietly reverses it; needs the explicit opt-out/
  masking decision recorded.
- **Staleness:** repo-derived feeds regenerate when the repo changes; game data changes
  continuously — a committed feed needs a cadence (and the page's `fetched_at`/honest
  banner already handles gaps; no invention risk on the websites side).
- **Un-contracted shipping:** rendering an un-contracted family re-opens the BUG-0022
  silent-desync class the #1920 contract exists to kill — the family MUST land in
  `dashboard_data_contract.json` with a version bump before the page trusts it.

**5. What does it unlock?**
The demonstrable ~80% of the owner's stats ask ("clearly see your stats… per server")
with zero auth surface, live BEFORE the OAuth phase; the production-DB egress path +
privacy masking rule that phase 3's API then inherits pre-proven; a second consumer for
product-forge's games-web ORDER 001 mock-to-real switch; and the contract's first
GAME-DATA family — the same family-growth muscle the phase-2 explorer needs (parent
probe Q4: "B's real cost is contract extension, not UI").

**6. What does it depend on?**
The explicit fan-in split (this feeds the manager's batched-ORDER decision):
- **Needs the batched superbot read-only-API ORDER (cannot proceed without it):** the
  producer — production-Postgres read + commit-back mechanism (Q2's open axis), the
  `leaderboards` contract-family entry + version bump + checker parity, the export
  cadence, and the per-server opt-out/masking rule. This is a strict subset of the
  API's own DB-read surface: same per-server player rows, no auth, no per-user
  filtering, public bounded top-N only — which is exactly why it should be RUNG 1 of
  that ONE batched ORDER (consumers: this idea + PROPOSAL 002 phase 3 per VERDICT 003's
  named change 4 + product-forge games-web ORDER 001), not a separate work item.
- **Already in hand with committed feeds alone (order-independent):** everything
  websites-side — the render seam, cache, honest-degrade banner, contract-pin check
  (`data_source.py@98ce6c0`, live), plus fixture-backed page development and the
  version-pin against the family's agreed shape. No owner click anywhere except the
  masking/opt-out data-shape decision.

**7. Which lane should build it?**
**superbot** builds the producer + contract family — inside the manager's batched
read-only-API providing ORDER as its zero-auth first rung (the ORDER VERDICT 003 already
demands routing FIRST). **websites** builds the page build-direct once the family lands
(or fixture-first anytime — lane-sized, its established stack). **product-forge** stays
a consumer (same rows, games-web skin). **Not sim-lab:** no reproduced-evidence question
exists — the producer mechanism is a design call inside the providing ORDER, and the
name-exposure dial is an owner taste/policy decision; simulating either would
manufacture evidence nobody needs (honesty norm: "not measured" beats invention).

**8. What is the smallest shippable slice?**
The `leaderboards` contract-family definition itself — the schema (top-N bounded rows
per game per server), the masking/opt-out flag, and the version bump — shipped as the
batched superbot ORDER's rung-1 deliverable together with the producer's first committed
`leaderboards.json`; the websites page (one module on the existing seam, honest-degrade
until the feed exists) is the natural same-week follow-on. What must NOT ship: a
websites page pointed at a family no producer writes, or a producer whose DB credentials
ride the existing static-scan CI job without the providing ORDER's own trust
verification (VERDICT 003 named change 4: the API surface "needs its own trust
verification" — the committed-feed rung inherits that bar for its egress mechanism).

**Recommendation: park** — no simulator question exists (the two opens — producer
egress mechanism and name-exposure policy — are a design call inside the batched
superbot providing ORDER and an owner data-shape decision respectively), and the
capture's front-run premise is reversed by the live tree: no committed feed carries
game data, so the producer is the zero-auth FIRST RUNG of the batched superbot
read-only-API ORDER (route ONE ORDER, three consumers: this + PROPOSAL 002 phase 3 +
product-forge games-web ORDER 001), with the websites page build-direct once the
family lands.
