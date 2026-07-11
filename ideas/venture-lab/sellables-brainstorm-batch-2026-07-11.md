# Sellables brainstorm — 12 candidates (2026-07-11)

> **State:** captured
> **Class:** venture · **Target:** menno420/venture-lab
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/main/docs/roster.md@6d5e3b3 · fetched 2026-07-11T18:54Z

Owner ask (verbatim, 2026-07-11): "can you come up with ideas for the venture lab, things like games, websites, apps, tools, anything we could use to sell in any way after we created it."

Ground rules applied: every candidate is buildable by this fleet (Python stdlib, static sites, GBA homebrew, Discord bots, CI tooling) and has a real — if small — revenue path; weak candidates were killed rather than kept as padding (kill list at the bottom). Hard rail respected throughout: no account creation or external publishing without an explicit owner click, and Q-0259 r.4 conservative-forecast discipline applies to every money click. The three launch-ready products (membership-kit $49, template-packs $19 PWYW, stripe-webhook-test-kit) and the four parked venture-lab ideas are treated as existing — nothing below duplicates them.

## Shortlist (top 5 — individual capture files in this section)

1. [substrate-kit as a product — agent-fleet starter kit](substrate-kit-agent-fleet-starter-2026-07-11.md) — GitHub sponsorware + license
2. [Webhook test-kit family](webhook-test-kit-family-2026-07-11.md) — new Gumroad SKUs on an existing product
3. [GBA homebrew starter kit](gba-homebrew-starter-kit-2026-07-11.md) — itch.io PWYW
4. [Idle-economy Discord bot + premium themes](idle-economy-bot-premium-themes-2026-07-11.md) — Discord subscriptions
5. [Running-an-AI-agent-fleet playbook](agent-fleet-playbook-ebook-2026-07-11.md) — Gumroad e-book

## All candidates

### 1. substrate-kit as a product — "agent-fleet starter kit" (shortlist #1)
- Concept: package substrate-kit (v1.10.0 here) — the bootstrap that turns any repo into an agent-operated project with claims, heartbeats, check gates, and merge-on-green ceremony — as a public product.
- Leverages: the kit itself, battle-tested across the whole fleet; doctrine docs already written.
- Sell channel: GitHub sponsorware (public repo, sponsor-gated support/extras) + Gumroad one-time license for a pro docs/templates bundle.
- Smallest shippable slice: a public landing README + docs page (websites-lane machinery) with a sponsor link — no kit code changes.
- Effort/plausibility: docs-heavy, low code effort. Agent-orchestration tooling is a live topic in 2026 so interest is plausible, revenue is not: conservative expectation is tens of dollars/month of sponsorship at best without promotion. Owner clicks: repo public + sponsor account.

### 2. Webhook test-kit family (shortlist #2)
- Concept: extend the launch-ready stripe-webhook-test-kit into a family — github-webhook-test-kit and discord-webhook-test-kit — same harness pattern, new fixtures, new SKUs.
- Leverages: existing stripe-webhook-test-kit machinery and its pending listing; Python stdlib.
- Sell channel: Gumroad / Lemon Squeezy, $9–19 each or bundled with the existing SKU.
- Smallest shippable slice: github-webhook-test-kit — fixtures for push/PR/check-run events + signature-verification harness — added as one SKU to the existing listing.
- Effort/plausibility: cheapest marginal effort on this list; the dev-tool niche is real but small. Conservative: single-digit sales/month.

### 3. GBA homebrew starter kit (shortlist #3)
- Concept: extract Lumen Drift's build scaffold (Makefile/CI, sprite pipeline, sha256-provenanced ROM dist) into a clean, documented GBA project template sold to the homebrew scene.
- Leverages: gba-homebrew's finished, working toolchain; Lumen Drift v1.3 as living proof it ships games.
- Sell channel: itch.io PWYW (+ Gumroad mirror); cross-promotes the Lumen Drift listing already owner-gated in the ⚑ 2026-07-14 bundle.
- Smallest shippable slice: template repo with a "hello world + one animated sprite" demo building green in CI, plus a setup guide.
- Effort/plausibility: mostly extraction + docs. The homebrew scene is small but active and buys tooling; PWYW realistically nets a few dollars per paying download at low volume. Rides the same itch.io go/no-go — no new owner account.

### 4. Idle-economy Discord bot with premium themes (shortlist #4)
- Concept: host superbot's idle-economy game (sim-pinned V006 economy; V001/V008 mining/encounter params) as a public Discord bot, monetizing cosmetics via the existing 12-pack theme catalog as a premium tier.
- Leverages: sim-validated game systems + a designed theme catalog — the content and balance work already exist.
- Sell channel: Discord's native premium-app subscriptions; fallback Ko-fi perks.
- Smallest shippable slice: the existing bot running in ONE public community server with 2 free + 2 premium themes wired.
- Effort/plausibility: the honest caveat — this is the only candidate with an always-on hosting + moderation commitment, plus Discord app-review overhead. Highest ceiling in the games track, highest operational drag. Owner clicks: hosting account, app verification, payout.

### 5. "Running an AI agent fleet" playbook (shortlist #5)
- Concept: an e-book distilled from this fleet's real doctrine — claims, heartbeats, merge-on-green ceremony, probe battery, owner-gate discipline — the operational story of an actual autonomous agent fleet.
- Leverages: doctrine already written across fleet-manager/superbot/kit docs; first-hand material very few others have in 2026.
- Sell channel: Gumroad e-book ($15–29); excerpt chapters as free posts on the websites lane for reach.
- Smallest shippable slice: outline + one polished chapter (the claims/merge-on-green ceremony) published free to test pull.
- Effort/plausibility: drafting is fleet-cheap; the owner's voice/edit pass is essential for authenticity, and marketing reach is the binding constraint. Conservative: low tens of sales without an audience.

### 6. Community stats-site template SKU
- Concept: productize the websites lane's leaderboard/stats machinery as a "community stats site" template — drop in a CSV/JSON, get a deployed leaderboard + activity site.
- Leverages: live deployed leaderboard/feed sites (websites lane).
- Sell channel: new SKU inside the existing template-packs listing ($19 PWYW).
- Smallest shippable slice: one generic template extracted from the superbot stats site with sample data.
- Effort/plausibility: low effort; modest demand from gaming/Discord communities. Honest expectation: a handful of sales as part of the existing pack, not standalone volume.

### 7. Trading-journal static-site kit
- Concept: local-first trading journal — a stdlib Python generator that turns broker CSV exports into a private static dashboard (P&L, per-strategy stats). Journal only: no signals, no advice — stays clear of regulated territory.
- Leverages: trading-strategy lane's metrics code + websites-lane static machinery.
- Sell channel: Gumroad, $10–19.
- Smallest shippable slice: CSV → one-page dashboard for a single broker format.
- Effort/plausibility: crowded space with SaaS incumbents; "local-first, no signup, your data stays yours" is the only real edge. Conservative: niche trickle.

### 8. "Build a backtester in pure Python" e-book + code
- Concept: educational package teaching a stdlib-only backtesting framework, using the momentum-family and holdout-reseal work as real worked material.
- Leverages: the trading lane's genuinely disciplined methodology (holdout protocol, conservative stats) — rare honesty in this genre.
- Sell channel: Gumroad e-book + companion repo ($19–29).
- Smallest shippable slice: outline + chapter 1 with the walk-forward harness.
- Effort/plausibility: quant-education demand is real but content-marketing dependent; needs an owner voice pass like #5. Conservative: low tens of sales.

### 9. HTML5 daily-seed arcade game
- Concept: small canvas puzzle/arcade game with a shared daily seed and a shareable result string (wordle-style social loop) — greenfield on websites-lane JS skills.
- Leverages: static-site deploy pipeline; shares daily-seed DNA with [gba seeded cave runs](../gba-homebrew/seeded-cave-runs-2026-07-10.md) on the GBA side.
- Sell channel: itch.io PWYW + web with a donation link.
- Smallest shippable slice: one playable mechanic + daily seed + shareable result string.
- Effort/plausibility: itch.io's arcade shelf is saturated; expected revenue per title near zero. The real value is proving the fleet can ship a complete web game cheaply and feeding the devlog (#12).

### 10. Pixel-art asset pack
- Concept: package Lumen Drift's fleet-made sprites/tiles as an itch.io asset pack (PWYW) with a clear license.
- Leverages: existing art from a finished game.
- Sell channel: itch.io PWYW.
- Smallest shippable slice: one themed tileset + license file.
- Effort/plausibility: only viable if the art is genuinely fleet-original and reads well out of game context — needs an art-quality gate first; small packs earn little. Kill fast if the extraction looks thin.

### 11. Discord server audit report tool
- Concept: read-only script that audits a server's roles, permission overwrites, and webhook exposure and emits a readable security report for admins.
- Leverages: superbot's Discord-API skill; Python stdlib.
- Sell channel: Gumroad one-time ($9), or free + Ko-fi as lead-gen for the bot (#4).
- Smallest shippable slice: permission-matrix report for one server.
- Effort/plausibility: admins mostly expect free tooling — realistic as a funnel/reputation play more than direct revenue.

### 12. Fleet devlog sponsorware
- Concept: public build-log site ("what an autonomous agent fleet shipped this week"), auto-drafted from session cards and heartbeats — the fleet's exhaust as content.
- Leverages: session-card discipline already in place; websites-lane rendering; near-zero marginal content cost.
- Sell channel: GitHub Sponsors / Ko-fi.
- Smallest shippable slice: a static page rendering the last 7 days of session cards, sanitized (publishing is an owner click; needs a no-secrets/no-internal-URL pass).
- Effort/plausibility: an audience-building play, not direct revenue — it attacks the marketing constraint that caps #1, #5, and #8.

## Killed during the pass (honesty record)

- GitHub Actions marketplace packaging — no direct payout path on the marketplace; folded into #1.
- Generic "tiny CLI tools" bundle — no credible willingness-to-pay.
- Prompt/content packs — filler; fails the genuinely-believed bar (Q-0089).
- Stats-as-a-service hosting — ongoing hosting burden with zero validation; the template SKU (#6) must sell first.

## Cross-cutting note

The fleet's binding constraint is distribution, not building: #1, #5, and #12 form a mutually-reinforcing distribution stack (kit → playbook → devlog audience). Every channel above still ends in owner money-clicks (accounts, payouts); the ⚑ 2026-07-14 itch.io go/no-go is the first live gate for the games track (#3, #9, #10).
