# Games program: theme-engine architecture + website-first provisioning — link index

> **State:** captured
> **Class:** product · **Target:** `menno420/superbot`
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/41899e15899516fda0093718ccb91a51961c5fe3/docs/ideas/games-theme-engine-website-first-2026-07-10.md@41899e1 · fetched 2026-07-10T22:53Z

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/games-theme-engine-website-first-2026-07-10.md`](https://github.com/menno420/superbot/blob/41899e15899516fda0093718ccb91a51961c5fe3/docs/ideas/games-theme-engine-website-first-2026-07-10.md)
— harvested 2026-07-10 by the drift re-harvest slice, pinned @ superbot `41899e1`
([raw](https://raw.githubusercontent.com/menno420/superbot/41899e15899516fda0093718ccb91a51961c5fe3/docs/ideas/games-theme-engine-website-first-2026-07-10.md)).

Owner-raised and owner-shaped (round-3 dispatch part-4e; provenance Q-0267, framed
"decided, not proposed"): the gen-2/gen-3 games program splits into TWO seats — a World
Games seat on the existing `superbot-games` (exploration + mining + fishing on shared
world systems) and a new Idle Engine seat (suggested `superbot-idle`) built
template-first — with a core/skin split as the load-bearing seam: game cores are code,
themes are validated data packs (`themes/<name>.yaml` against a theme-manifest schema +
theme-gate CI), making the egg farm the flagship *theme* of an idle ENGINE rather than
a game, and theme production the fleet's best volume-first fit (Q-0266: "produce 10
more themes" is always a valid slice). Website-first onboarding is the write-path twin
of the read-only data API: a versioned server provisioning manifest (features + theme
per game), phase-1 as a signed setup code (`!setup apply <code>`) with no hosted
backend. §4 converges everything onto superbot-next's existing plugin contract
(feature selection = per-guild plugin enable set; theme = plugin param); §7 carries
four decided-and-flagged items (Q-0240, owner veto at the mapping react), including
plugin-native/no-old-bot-port for the idle game. §6 names sim-lab as the numeric
consumer for idle-economy balance — the pipeline's first fully-numeric game consumer.

**Probe-ripeness (recorded at harvest, not a probe):** NOT ripe for a v0 probe now —
this is a decided owner directive mid-dispatch (the doc is the declared input to two
games founding packages and the manager's conformed mapping, with its open choices
already routed through Q-0240 decide-and-flag), so a probe battery here would
re-recommend on questions the owner has decided or reserved for the mapping react. The
probe-shaped kernel inside it (idle-economy balance curves, §6) becomes probeable once
the idle seat exists and pre-registers economy params — revisit at that point.
