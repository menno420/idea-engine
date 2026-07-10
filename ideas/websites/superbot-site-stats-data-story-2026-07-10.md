# SuperBot site expansion — per-server stats · game-data explorer · the story page

> **State:** sim-ready
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

~~Not yet probed (state: captured).~~ Probed 2026-07-10 — report below. The capture's
weighing held up: smallest slice = the story-page skeleton, biggest unknown = the stats
auth surface, builder = websites lane.

## Probe report (v0, 2026-07-10)

*Grounded in this file @ d91d99b, live fetches of superbot's fleet manifest and round-3
part-4 dispatch brief (public raw, this session), and GitHub code search over
`menno420/superbot` @ bd91da2 (the ref every superbot citation below resolves against).
Where something has not been tried or measured, it says so.*

**1. What is this really?**
Three products under one owner sentence, unified only by the destination ("through the
superbot website you should…", §1). Sorted by trust surface they are: a **narrative
showcase** (C — static, zero auth), a **public dataset browser** (B — read-only public
data), and the fleet's **first authenticated user-facing feature** (A — your own game
data behind Discord login). The capture's real contribution (§3) is noticing that this
is a risk ladder, not a bundle: the owner's one hard condition ("fully tested later to
make sure this is trustworthy", §1) attaches to A alone. So what this *really* is: two
phases of ordinary websites-lane work plus one categorically new trust class that the
owner himself marked as a simulation candidate (§5, "could be simulated later").

**2. What is the possibility space?**
Three axes. **Data source:** committed versioned JSON exports (the live pattern — see
Q3) → a superbot-lane read-only API (§4, required for per-user data) → live production
DB (banned by the capture, correctly: superbot's Postgres is production). **Identity:**
anonymous (C, B) → Discord OAuth `identify`+`guilds` (A, the §5 scope-minimalism floor)
→ richer scopes (banned by §5). **Presentation:** static scrollytelling → faceted
client-side explorer → live personal dashboards → and, adjacent but real, the
Shakes-&-Fidget-style games-web presentation product-forge was just ORDERed to prototype
(superbot `docs/planning/round3-dispatch-part4-brief-2026-07-10.md@dd03e74` §2.2), which
renders the same mining character sheet from a mock of the same contract. Unclaimed by
the capture: the story page (C) doubling as the EAP program's public showcase generalizes
— the git-history-graphs build step would work for any fleet repo.

**3. What is the most advanced capability reachable by the simplest implementation?**
Two, both already pattern-proven in the fleet:
- **C:** a static story page whose graphs are generated at build time from `git log` —
  no backend, no auth, no cross-repo call — yet it yields the program's public showcase
  artifact with authentic, zero-maintenance data (the repo history *is* the dataset).
- **B:** the websites repo **already renders ~12 dashboard pages from superbot's
  committed `dashboard/data/dashboard.json` fetched over the public raw path**
  (`menno420/websites dashboard/data_source.py`, named in superbot
  `dashboard/data/dashboard_data_contract.json@38b2b15`), and the versioned fail-closed
  contract for that feed shipped as superbot PR #1920 (producer
  `scripts/export_dashboard_data.py@ff6e82e`, checker
  `scripts/check_dashboard_data.py@ad56de9`). The explorer is that live pattern pointed
  at the game corpora — the BTD6 fixture tree (towers/heroes/maps/modes/rounds/bloons/
  ct_relics + per-entity stats, `docs/btd6/btd6-data-backends.md@7be26aa`) and the bot's
  own catalogs — plus client-side search. No new server surface at all.
A is explicitly NOT reachable simply: per-user, per-guild data cannot ride committed
exports (privacy + volume), which is exactly why §4 flags the API.

**4. What breaks it?**
- **The OAuth trust gate (A).** One isolation bug shows user A user B's stats; one
  sloppy token store leaks Discord credentials scoped to real servers. The websites
  lane has never shipped an auth surface (not verified — its 3 Railway services are
  live per the fleet manifest websites row, but their auth posture was not inspected
  this session); the owner conditioned the whole feature on trustworthiness. This is
  the break-point that decides the idea, and it is checkable (§5's six-item list) —
  which is what makes it a sim question rather than a hope.
- **The cross-lane API gap (A).** The read-only API now has TWO waiting consumers —
  this idea's stats phase (§4) and product-forge's games-web real-data phase, whose
  ORDER 001 says verbatim "it needs a superbot-lane read-only API — flag it in status,
  don't build it" (`round3-dispatch-part4-brief-2026-07-10.md@dd03e74`). Neither
  consumer lane may build it; no superbot ORDER for it exists yet (not found in the
  part-4 brief's queue). Unrouted, phase 3 deadlocks regardless of the sim verdict.
- **Contract drift (B).** Only families `meta`+`bugs` are contracted at version 1
  (`dashboard_data_contract.json@38b2b15`); the game corpora are not yet contracted
  families at all. An explorer built on un-contracted exports inherits the BUG-0022
  silent-desync class the contract exists to kill — B's real cost is contract
  extension, not UI.
- **Scope creep (C).** Scrollytelling is an unbounded design sink; the §6 bound (2–3
  real graphs, skeleton first) is the guard.

**5. What does it unlock?**
- **C** is the public face of the whole EAP experiment — the artifact the owner can
  point anyone at. Nothing else in the fleet currently plays that role.
- **B** turns the collected corpora into a public asset and forces the #1920 contract
  to grow family-by-family — hardening every other consumer of the same feed for free.
- **A + the read-only API** unlock two product tracks at once (this idea's stats pages
  AND product-forge's games-web real-data phase), and the §5 verification produces the
  fleet's reusable trusted-OAuth pattern — every future personalization feature on any
  lane site inherits it.

**6. What does it depend on?**
- **C:** nothing outside the websites repo but git history. Zero owner clicks.
- **B:** superbot-side export extension + contract families for the game corpora
  (superbot-lane work, small, pattern-established per PR #1920's own "Remaining" note
  in `docs/ideas/pinned-feed-contract-for-dashboard-json-2026-07-09.md@ecd2db1`).
- **A:** a Discord OAuth application (owner click: app + redirect URIs); the
  superbot-lane read-only API (manager-routed ORDER, §4); the §5 trust-gate
  verification (sim-lab); a backend host (websites already runs services on Railway —
  fleet manifest row).
- **All:** manager routing — this repo proposes, it cannot ORDER the websites lane.

**7. Which lane should build it?**
**websites** builds all three phases (it is the target lane, and phases 1–2 are its
established stack: static pages + committed-feed rendering). **superbot** builds the
read-only API and the export/contract extensions — its Postgres, its exporter, via a
manager-routed ORDER when phase 3 approaches (§4, unchanged). **sim-lab** settles the
§5 trust gate before A goes public. **product-forge** is a sibling consumer of the same
API, not a builder here — the manager should scope the eventual superbot API ORDER to
serve both consumers (one contract, two skins).

**8. What is the smallest shippable slice?**
The §6 answer survives the probe: the story-page skeleton with 2–3 real git-history
graphs (e.g. PRs-merged-over-time, test-count growth), graphs generated by a build-time
script into a committed data file — the same committed-feed shape the lane already
renders. Zero auth, zero new dependencies, zero owner clicks; startable by the websites
lane on its next wake once the manager routes it.

**Recommendation: sim-ready** — the ONE question needing reproduced evidence is the §5
OAuth trust gate for the per-server stats phase (A); the other two phases (story page,
data explorer) carry no auth surface, are already pattern-proven in the live
websites↔superbot committed-feed stack, and should be routed to the websites lane by the
manager WITHOUT waiting on the sim verdict — that split is sequencing inside this one
idea (§3's risk ladder), not separate states.

## Sim verdict (2026-07-10)

sim-lab **VERDICT 003 · finalized 22:15Z · needs-more-evidence, ruling
buildable-with-named-changes** (= this repo's PROPOSAL 002 — numbering cross recorded on
`.sessions/2026-07-10-sim-verdicts-fanin.md`). SETTLED: the six §5 controls, implemented
as the spike's reference set, defeat 13 concrete attacks reproducibly across 5 seeds
(scope server-authoritative + fail-closed on over-scoped grant + exact-match redirect
allow-list; Discord token discarded — session holds only user_id+guild_ids+issued_at, no
refresh/offline; server-side single-use state bound to the browser session; code
single-use + PKCE S256; IDOR blocked by session identity + cross-server guild block;
token-bucket rate limit bounded across the full 3×3 sweep). NAMED CHANGES before phase 3
builds: (1) promote §5 from a checklist to that concrete control set, adding
Secure+HttpOnly+SameSite cookies + HSTS + TLS-only; (2) fix HOLE-1 stale guild
membership — a cached session reads a server the user LEFT → per-request membership
re-check or short session TTL; (3) fix HOLE-2 `guilds` over-read — the full guild list is
returned when only the viewed server is needed → check only that server, don't retain the
list; (4) route the §4 superbot read-only API as a superbot-lane ORDER FIRST — it is
UNBUILT AND UNROUTED (the hard blocker: phase 3 deadlocks regardless of this verdict, and
the API needs its own trust verification). LAUNCH LIVE TESTS close the JUDGMENT-ONLY
items (live Discord IdP behavior, TLS/MITM, Railway secrets, pre-auth IP-keying, live
IDOR probes). Phases 1–2 (story page, data explorer) carry NO auth surface and do NOT
wait on this. Source:
[sim-lab `control/outbox.md` VERDICT 003 @ `8713f26`](https://github.com/menno420/sim-lab/blob/8713f261c99634156dd6facda03e396b888a9e8a/control/outbox.md)
(gate PASS on the executed spike claims; evidence: prototype + JUDGMENT-ONLY, rung 2 —
13 attacks, 5 seeds, 268 self-checks; the JUDGMENT-ONLY items are labelled hypotheses,
not evidence). State stays `sim-ready` — the grammar has no post-verdict state;
`historical(<merged PR>)` is a build-time move (post-verdict routing is the manager's).
