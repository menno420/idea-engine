# Idea — extend the pinned-feed-contract pattern to `dashboard.json` — link index

> **State:** parked(routed — joins the read-only-API fan-in: build = superbot lane inside the fm ORDER 012/013 providing ORDER, still unrouted/owner-held; this probe's contract-shape line attaches to that relay)
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/pinned-feed-contract-for-dashboard-json-2026-07-09.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/pinned-feed-contract-for-dashboard-json-2026-07-09.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/pinned-feed-contract-for-dashboard-json-2026-07-09.md)).

Extend the pinned-feed-contract pattern (which caught a live consumer defect on console.json) to dashboard.json; the first slice (versioned contract file, slice semantics) shipped in superbot PR #1920, remaining families still uncontracted.

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/e1090dbcfdf63ffd955399dc2325b9ad1a2f8c8d/docs/ideas/pinned-feed-contract-for-dashboard-json-2026-07-09.md@e1090db · fetched 2026-07-11T12:48:09Z
> *(pin annotation: superbot live HEAD S = `e1090dbcfdf63ffd955399dc2325b9ad1a2f8c8d` by `git ls-remote` 12:47:33Z; the canonical doc @ S is BYTE-IDENTICAL to the harvest pin `fd638e3` — diff empty — so the header pin above stays faithful and this recheck pin records live-HEAD freshness.)*
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/e1090dbcfdf63ffd955399dc2325b9ad1a2f8c8d/dashboard/data/dashboard.json@e1090db · fetched 2026-07-11T12:48:39Z
> *(pin annotation: the LIVE feed, 401,222 bytes — reachability check per README § probe battery: what the data actually is, not what the doc says it is.)*
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/7b46bd1577b247e41b8ab0458333e6175bbfcb7a/control/inbox.md@7b46bd1 · fetched 2026-07-11T12:49Z
> *(pin annotation: fm live HEAD F = `7b46bd1` by ls-remote 12:47:46Z — ORDER 012/013 are the routing decision this probe's Q6/Q7 rest on.)*
> **Sequence:** after the fm ORDER 012/013 providing ORDER routes to superbot (decided, verified UNROUTED at superbot `control/inbox.md` @ `e1090db`, fetched 12:48:02Z — the inbox holds exactly ORDER 001 done + ORDER 002 new, no feed/publisher ORDER; apparently owner-held pending the founding-package review, fm ORDER 012 ⚑ OWNER-REVIEW @ `7b46bd1`)

> Single-pass battery (panel not escalated: docs/contract-pattern surface, reversible,
> no security/data/spend/public blast radius — README § probe battery, VERDICT 002
> default). Verify-first grounding all live this probe (2026-07-11 ~12:47–12:50Z),
> pins above; additional live reads cited inline: sim-lab HEAD L = `a05ee3c`
> (ls-remote 12:47:46Z), its `control/outbox.md` @ L byte-identical to the VERDICT 007
> pin `015e28e`; `botsite/data/console.json` @ S families exactly match its contract;
> NO `mining_snapshot` feed file exists anywhere probed (404s at `data/`,
> `dashboard/data/`, `botsite/data/` — pattern-exists is not pattern-can-produce: the
> games feed needs a NEW producer that has not shipped).

**1. What is this really?**
A PROCESS idea: generalize the versioned committed-JSON contract pattern — contract
file + producer parity constants + fail-closed CI checker + raw.githubusercontent
consumption, no live service — from `botsite/data/console_data_contract.json`
(superbot PR #1884, TOTAL-whitelist semantics, 6 families, fully contracted) and
`dashboard/data/dashboard_data_contract.json` (PR #1920, version 1, SLICE semantics,
2 families of 13) to EVERY superbot-published feed family. Since capture it has
quietly become the fleet's DECIDED read-only-API transport: fm ORDER 012 rules "API
placement: superbot lane, contracted committed-JSON feed per #1920's actual pattern …
NOT a live service", fm ORDER 013 confirms "game-state feed stays the superbot-lane
committed-JSON contract feed (#1920, unchanged)", and at least four consumers are
converging on it — websites dashboard pages, botsite console, games-web phase-2
(sim-lab VERDICT 007 change #2 mandates consuming `mining_snapshot.v1` and retiring
the competing self-API), and websites stats/explorer (ORDER 012 names it blocked on
the same API).

**2. What is the possibility space?**
Family-by-family growth of the dashboard contract — 11 of 13 live families are
uncontracted, and THREE of them (`reviews`, `bot_changelog`, `telemetry`) are not
even on the canonical idea's own remaining-list of 8 (catalogue/cogs/settings/
env_usage/ideas/updates/synonyms/access): the live feed has already outgrown the
doc. A born-contracted doctrine for NEW feeds (`mining_snapshot.v1` shipping WITH
its contract file, producer constants, and checker in the same PR). Consumer-side
version pinning + render-time validation (the idea's own endgame: websites pins the
version and validates at render time). And reconciling the TWO live contract
semantics — console's total-whitelist vs dashboard's slice — into one doctrine line
saying when each applies.

**3. Most advanced capability reachable by the simplest implementation?**
Slice semantics already prove incremental growth is cheap: one family = one
`contracted_families` entry + one producer constant + one checker family + one
version bump — no schema big-bang, no migration. Iterating that trivial move to a
fixed point reaches the end state: every fleet read surface on versioned,
fail-closed, committed JSON with ZERO live services to operate — the whole
read-only API as a git-native artifact.

**4. What breaks it?**
The providing ORDER shipping `mining_snapshot.v1` WITHOUT the contract pattern —
born-uncontracted is the exact defect class the pattern caught live on
`console.json`, and no `mining_snapshot` file or producer exists yet (verified
404 above), so the shape is still free to get wrong. Uncontracted families
drifting under consumers that already render them (11 of 13 today, three of them
unlisted anywhere). Version-bump churn if families land without consumer
coordination (each bump forces the pinned consumers to move). And the owner-hold
delaying routing while games-web phase-2 waits on the feed (VERDICT 007's own
sequencing: feed slice first).

**5. What does it unlock?**
games-web phase-2 (VERDICT 007 change #2: consume `mining_snapshot.v1`, retire the
self-API); websites stats/explorer (ORDER 012's named blocked consumer); the
self-API retirement itself (one fewer live service class fleet-wide); and
mineverse-parity read surfaces — any future site reads game state the same
contracted way, with drift caught in CI instead of in production.

**6. What does it depend on?**
The superbot producers (`scripts/export_dashboard_data.py` + the `DASHBOARD_*`
parity constants + the `meta.schema_version` stamp) and their contract files —
all superbot-lane surfaces. The fm ORDER 012/013 providing ORDER, which is
DECIDED but UNROUTED (superbot's inbox @ `e1090db` carries no such ORDER;
fm ORDER 012 sits ⚑ OWNER-REVIEW with the founding packages HELD @ `7b46bd1`) —
see the Sequence pin above. Downstream, websites-side version pinning +
render-time validation to close the loop.

**7. Which lane should build it? (honest routing)**
superbot — the hub owns the producers, both contract files, and the checker; the
build belongs INSIDE the providing ORDER when the manager routes it. NOT
idea-engine (this repo writes no lane files, Q-0260). NOT sim-lab: no genuine
evidence question survives — VERDICT 007 already routes the one measurable axis
(presentation VALUE) to a phase-2 A/B vs the mineverse direct view, and the rest
is deterministic contract engineering, so no outbox proposal ships from this
probe.

**8. Smallest shippable slice?**
One line riding the providing-ORDER relay — the CONTRACT-SHAPE line:
"`mining_snapshot.v1` ships born-contracted (contract file + producer constants +
fail-closed checker in the same PR, slice semantics), and each next
`dashboard.json` family lands as one-family-one-version-bump" — plus the fact the
live feed carries 3 families (`reviews`, `bot_changelog`, `telemetry`) the
canonical idea doesn't list, so the family census must come from the FEED, not
the doc.

**Recommendation: park** — routed: joins the read-only-API fan-in — the build is
superbot-lane work inside the fm ORDER 012/013 providing ORDER, which is decided
but verified still UNROUTED at superbot's inbox @ `e1090db` (12:48Z), apparently
owner-held pending the founding-package review (fm ORDER 012 ⚑ OWNER-REVIEW @
`7b46bd1`); this probe's contract-shape line (Q8) attaches to that relay when the
manager routes it. No outbox proposal — per Q7, no genuine sim question survives.
