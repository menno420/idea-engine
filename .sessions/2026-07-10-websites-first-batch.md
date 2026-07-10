# Session — websites slice: first grounded capture batch (follow-on ideas)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-10 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## Scope

Bring `ideas/websites/` up to a real first batch: the section holds only the
owner-dropped superbot-site idea (sim-ready, PROPOSAL 002). Generate 3–5 grounded
follow-on captures that ride the SAME rails its probe found routable now
(committed-feed pattern, live 4-hourly lane wake, phases 1–2 story-page/explorer
infrastructure) — without duplicating the sim-gated stats phase. Ship as one
merged-on-green PR.

## What this session did

- Claimed `ideas/websites/` (`claims/batch-websites-follow-on-captures.md`, flat
  filename per claims/README; cleared in this branch's final commit). No sibling
  claims present at claim time; PR #29 (seat-boot probe) had already merged.
- **Generated the section's first real batch — 4 captures**, all state `captured`,
  one page each, blessed `> **Grounding:**` header pins (byte-form, warn list kept
  at 0) + explicit why-now each:
  - `fleet-program-pulse-feed` (product) — the probe Q2's unclaimed generalization:
    build phase 1's git-history graph exporter fleet-general from its first commit
    (committed schema-stamped `pulse.json` per repo + fleet rollup, the exact
    `dashboard.json` committed-feed shape the lane already consumes); folds in the
    "living epilogue" (`/activity` as the story's closing chapter) instead of a
    separate thin capture
  - `public-leaderboards-committed-feed` (product) — the zero-auth slice of the
    owner's stats ask: a contracted `leaderboards` export family (top-N per game
    per server, PR #1920 pattern) rendered over the live raw-fetch path; deliberate
    `Sequence: before` the sim-gated stats phase — its two blockers (sim verdict +
    unrouted read-only API) have no ETA and the aggregate slice needs neither;
    open-web name exposure named honestly as the one design point (opt-out/masking)
  - `contract-driven-explorer-facets` (product) — the phase-2 explorer derives
    facets/columns/search from the versioned contract file itself, fail-closed:
    each newly contracted family lands with zero websites diff, halving the probe
    Q4 per-family cost ("B's real cost is contract extension, not UI") and making
    UI↔contract desync structurally impossible
  - `story-bubble-texts-content-feed` (product) — the owner's "bubble texts" as a
    committed content file (speaker attribution owner|agent, scroll/graph anchors):
    new owner asides become one-line content commits relayable straight from owner
    chat by the copilot (the same path that filed the parent idea), decoupling the
    scarcest resource's voice from websites code sessions
- **Dropped as too thin / out of scope (recorded, not padded):**
  - *story-page living epilogue* (render `/activity` as the story's last chapter) —
    one template include over an already-shipped feed; folded into the
    program-pulse capture as a note, not a standalone idea
  - *bot deep-links to explorer pages* (superbot commands answer with explorer
    URLs) — a cross-lane superbot write for a convenience link; doesn't clear the
    routing overhead before the explorer exists
  - *anything on the botsite `/submit` intake queue* — owner-gated twice over
    (Railway Postgres click + the lane's D-0005 no-agent-Railway-mutations wall),
    and the lane's own ⚑ already carries the complete six-field ask; an idea
    restating a standing owner ask adds nothing (the PR #17 drop shape)
  - *websites lane-born backlog harvest* — real work but a harvest slice, not a
    capture: the lane's `docs/ideas/backlog.md@0cd08d2` holds its own captured
    ideas plus SIX Q-0264 sim-worthy candidates its heartbeat flags for this
    pipeline; left as the section's ripest follow-up slice
- Section README index updated (4 new rows; the sim-ready row untouched).
- **Grounding fetched this session (public raw + `git ls-remote`, Q-0260):** fleet
  manifest websites row @ superbot HEAD `9624c5399f5b1a3da293c07ce930e8b0410d79e4`
  (pinned via ls-remote, fetched 22:08Z — 4-hourly wake WORKS/self-armed with first
  fire verified, 3 Railway services live, ORDERs 001–008 done at row-write); lane
  repo `menno420/websites` pinned @ HEAD `0cd08d2da1580fffff1595a6f4119b6d98a8b4b3`:
  README (dashboard/botsite rework is a "later, deliberately checkpointed phase" —
  these captures feed exactly that), full `control/status.md` (21:58Z — continuous
  mode, 5 work slices this wake, ORDER 009 fully closed, kit v1.7.1, send_later
  chain live-proven), `control/inbox.md` (ORDERs 001–009), `docs/ideas/backlog.md`,
  and `dashboard/data_source.py` — the LIVE committed-feed evidence PR #5's probe
  cited: fetches superbot's committed `dashboard/data/dashboard.json` +
  `botsite/data/console.json` over raw.githubusercontent.com, tokenless, TTL cache,
  "never fake data" honest-degradation banners. The probe report itself re-read at
  this repo's HEAD `698fd93` (`ideas/websites/` byte-unchanged vs the `6016002`
  tree).
- **Manifest-lag datapoint #8 (for the manager):** the manifest websites row @
  superbot `9624c53` records lane close-out #58/`d493792` 13:57Z + kit v1.6.0 while
  the lane heartbeat @ real HEAD `0cd08d2` reads #75 @ 21:58Z + kit v1.7.1 — ~8 h
  and one kit version behind, the freshest-wins pattern again.
- **NO outbox entries and NO probe** — captures only (state `captured`); the
  earn-rate bar holds (append only when a probe earns it).
- Landing per README § Landing conventions: PR READY, no review wait,
  merge-on-green; `python3 scripts/preflight.py` (all 4 checks) + `python3
  bootstrap.py check --strict` green before push; heartbeat overwrite as the
  deliberate LAST step; claim cleared in the close-out commit.

**📊 Model:** fable-5 · docs-only (4 captures + section index + card + heartbeat;
no code)

## 💡 Session idea

**Lane-backlog harvest, second instance ready:** `ideas/superbot/` link-indexes a
canonical lane backlog; websites now has the same shape sitting unharvested
(`docs/ideas/backlog.md` — its own `captured → planned → built → retired` states,
six candidates its heartbeat explicitly flags as "Q-0264 sim-worthy … all in
docs/ideas/backlog.md"). The heartbeat's standing note already says "a second-lane
harvest is a one-line SECTIONS addition" (check_harvest, PR #22/#26); websites is
the ripest second lane because the lane ITSELF is asking for the pipeline. Anchors:
`scripts/check_harvest.py` SECTIONS table; recipe on the PR #26 card.

## ⟲ Previous-session review

PR #29 (seat-boot harness probe; work `604e8c1`, close-out `7c9b961`, merge
`698fd93`) promised: battery-v0 probe with the live-state timeliness check FIRST,
verdict park(routed) with NO outbox append, a first Cross-links entry in
`ideas/substrate-kit/README.md`, claim cleared before merge — all verified on this
tree: the idea file carries the appended probe report ending in exactly one
recommendation (`park(routed — …)` state line parses, lint 0 violations on 274
files), the substrate-kit README Cross-links subsection exists with the by-link
row, `claims/` holds only its own README at HEAD, and the MANAGER relay note rides
the heartbeat. Its card's capability recipe (`git ls-remote` for out-of-scope HEAD
SHAs where the MCP is repo-walled and anonymous api.github.com 403s) was consumed
directly by this slice — both pins (superbot `9624c53`, websites `0cd08d2`)
resolved exactly that way, friction-free. Its handoff's caution ("a sibling
gba-homebrew probe session was reported in flight — re-read the bus and claims/
before claiming") was followed: claims/ empty, no collision. Honest gap noted: its
card stamps superbot HEAD `afbaea7` at 21:53Z; by this slice's 22:08Z fetch
superbot HEAD was already `9624c53` — HEAD pins age in minutes on bless day, which
is why every pin here carries its fetch time.

## Handoff → next wake

Inbox first, as always. This section now has real depth: 4 captured follow-ons +
the sim-ready head (PROPOSAL 002 queued behind INTAKEs 001–002 at sim-lab).
Ripest websites follow-up: the lane-backlog harvest (💡 above — one SECTIONS line
+ link-index pass, and it carries the lane's six self-flagged Q-0264 candidates
into this pipeline). Probe-priority within the new captures when a probe slice
comes: `public-leaderboards-committed-feed` first (it is Sequence-tied to
front-running the stats phase and would sharpen the manager's eventual batched
superbot ORDER), then `contract-driven-explorer-facets` (first-commit fork — decays
once the explorer starts hardcoding). Standing next-slices from the heartbeat
otherwise unchanged (concept-pick-bringup-pack probe is time-boxed by the open
pick window).
