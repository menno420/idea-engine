# SuperBot site expansion — per-server stats · game-data explorer · the story page

> **State:** captured
> **Class:** product · **Target:** websites (`menno420/websites`; one flagged cross-lane
> dependency on `menno420/superbot` — see §4)
> **Provenance:** owner-dropped live in the superbot round-3 dispatch chat
> (2026-07-10 ~18:5xZ), filed by the dispatch copilot with a review-and-improve pass
> (superbot Q-0254). The owner's phrasing is preserved in §1; §2–§5 are the copilot's
> expansion — verify against the owner's words before overriding them.

## §1 — The owner's ask (as given)

Through the superbot website you should:

1. **Clearly see your stats for the bot, per server.** The Discord auth for this must be
   **fully tested later to make sure this is trustworthy** (owner's explicit condition).
2. **Browse and search through the game data we collected.**
3. See **one page that explains the story behind this project** — the why and how of
   SuperBot — with **visuals, graphs, bubble texts etc., to really bring the reader into
   the story**.

## §2 — Expanded shape (review-and-improve pass)

**Feature A — per-server personal stats.** Discord OAuth login → pick a mutual server →
your live picture: XP/level/rank, coins, mining character (gear paper-doll, skills,
structures, depth records), fishing, creature game, leaderboard positions. The paper-doll
compositor and placeholder sprites already exist in superbot (V-16) — the visual concept
is pre-validated.

**Feature B — game-data explorer.** Faceted browse + search over the collected datasets:
the BTD6 knowledge data (towers/upgrades/paragons/bosses/prices — the corpus the bot's AI
grounds on) and the bot's own game catalogs (mining items/recipes, fish, creatures).

**Feature C — the story page.** A scrollytelling "why and how of SuperBot": the
owner-plus-AI-fleet story told with scroll-triggered visuals, **data-driven graphs from
the repo's own history** (PRs merged over time, test-count growth, fleet size, telemetry —
authentic and zero-maintenance, the data already exists in git), and speech-bubble asides
(the owner's "bubble texts") carrying the voice-of-the-owner / voice-of-the-agent
commentary. Doubles as the public showcase artifact of the whole EAP experiment.

## §3 — Sequencing by risk (the improvement that matters most)

Ship in **reverse order of trust surface**, so value lands early and auth risk lands last:

1. **Story page first** — static, zero auth, zero backend; pure win.
2. **Data explorer second** — build on **versioned static JSON exports** (the superbot
   #1920 dashboard-data-contract pattern: pinned families, schema-version stamp,
   fail-closed checker) + client-side search; no live DB dependency, no auth.
3. **Personal stats last** — the only piece needing OAuth + a backend; gated on §4/§5.

## §4 — Flagged cross-lane dependency (stats phase only)

Per-server stats need a **superbot-side read-only API** (the bot's Postgres is
production): a separate superbot-lane ORDER, not websites work — scoped read-only
service, token-scoped, serving the same versioned contract shape. Route via the manager
when the stats phase approaches; phases 1–2 have zero superbot dependency.

## §5 — The OAuth trust gate (owner's explicit condition, made concrete)

Before the stats feature goes public, a dedicated verification pass: scope minimalism
(`identify` + `guilds` only), session/token lifecycle (no long-lived token storage),
CSRF/state-parameter correctness, per-user data isolation (you can never see another
user's stats), rate limiting, and an abuse-case walkthrough. **Good sim-lab candidate**
(the owner: "this is something that could be simulated later") — an evidence-passed
checklist verdict rather than a hope.

## §6 — Battery status

Not yet probed (state: captured). Probe should weigh: smallest slice = the story page
skeleton with 2–3 real git-history graphs; biggest unknown = the stats API's auth surface;
likely builder = websites lane (phases 1–2 startable with zero owner clicks).
