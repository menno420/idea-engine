# Games program: theme-engine architecture + website-first provisioning — link index

> **State:** parked(routed — the owner/manager architecture decisions are all made (Q-0267 frame + fm conformed mapping's four details) and every §-item is either consumed at a live lane HEAD or already carried by a dedicated tracked head in this tree; the one probe-shaped kernel the harvest flagged (§6 idle-economy) was consumed by PROPOSAL 006 → sim-lab VERDICT 006 approve; per-§ fan-in ledger in the probe report)
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

## Probe report (v0, 2026-07-11)

*Single-pass battery per the README panel default (sim-lab VERDICT 002): this head is a
decided owner directive whose remaining question is dispositional (what is LEFT vs what
lanes consumed), with no irreversible/high-blast-radius surface, and the verify-first
sweep did not disagree with itself. The harvest's own ripeness note bound this probe's
shape: it deferred the battery "until the idle seat exists and pre-registers economy
params" — both since happened AND were themselves consumed (the idle seat exists,
pre-registered, and got its verdict), so the honest battery here assesses residue, not
merit. Every load-bearing claim below was re-fetched at LIVE HEADs this probe
(2026-07-11T10:22:09Z ls-remote batch), never inherited from the capture. The canonical
doc is byte-identical `41899e1` → live superbot HEAD `c77ee0d` (diffed this probe), so
§-references below cite the harvest pin.*

### Verify-first ledger — per-§: consumed / frozen / still open (the probe's core)

| § | Status | Where it lives now (live-pin citation) |
|---|---|---|
| §1 core/skin seam (themes = validated data) | **CONSUMED** | Seat B built it: `schema/theme.schema.json` + `tools/theme_gate.py` + `docs/theme-schema.md` @ superbot-idle `1e2c9f6` (depth-1 clone this probe); gate-green = mergeable data PR is the lane's shipped product property. Seat A adopting it live: theme-leaks R2 cleared — mining grid/market/taxonomy nouns → data tables keyed on neutral ids, audit tally 19✅·9⚠️·2❌ (superbot-games `control/status.md` @ HEAD `e62818a`, raw-fetched this probe). Remaining ⚠️/❌ rows are Seat A's own audit roadmap, not an idea-engine head. |
| §2 egg farm = first theme of an idle ENGINE | **CONSUMED, exceeded** | `themes/` @ `1e2c9f6` = `egg-farm.yaml` flagship + 11 sibling packs (12 total — §2 asked for "2–3 more proving the seam"); five of §2's own candidate list shipped near-verbatim (space-colony · potion-brewery · cyber-city · royal-bakery · wizard-tower). |
| §3 website-first provisioning — write path | **FROZEN (contract-complete)** | SETUP-CODE FORMAT v1 is `binding` @ `1e2c9f6`: `docs/provisioning.md` names encoder = websites lane, decoder = superbot-next plugin, machine twin `idle_engine/provisioning.py` (`encode_setup`/`decode_setup`/`validate_against_catalog`), doc-honesty test + 150 cross-language vectors. Exactly §3's phase-1 shortcut, shipped. |
| §3 website-first provisioning — consumer/UI | **STILL OPEN (sequenced, not stalled)** | websites @ HEAD `f0e7710` (depth-1 clone this probe): zero selector/gallery/encoder surface — `superbot-idle` appears only as a fleet-registry row (`app/config.py:251`). Deliberate: fm conformed mapping §4 sequences the selector LAST-shippable ("website-first is the user flow, not the build order"). The read-path contract that unblocks it is already a tracked head: `../superbot-idle/theme-catalog-gallery-read-contract-2026-07-11.md`, parked(build-direct), window re-verified open at `f0e7710` this probe. |
| §4 plugin-seam convergence | **DECIDED + PARTLY CONSUMED; arming HALF-FIRED (this probe's find)** | The plugin contract doc EXISTS and is binding: superbot-next `docs/game-plugin-contract.md` @ live HEAD `8b55d95` (D-0056; 200 this probe — and 200 at BOTH earlier pins `4a32f61` and `4c8c5b0`, so the sibling promotion head's "all contract-doc paths 404" grounding was a path-keyed false negative on exactly the failure mode its own Q4 named; the fm mapping cited the doc 2026-07-10). Schema drafted in Seat B per the decided split; promotion tracked at `../superbot-idle/theme-schema-plugin-contract-promotion-2026-07-11.md` parked(awaiting-arming-event) — whose event-keyed un-park condition's FIRST disjunct ("contract doc fetchable anywhere superbot-next publishes") now reads satisfied. Second disjunct NOT fired: ORDER 002 still `status: new` @ `8b55d95` inbox; `superbot-plugin-hello` still EMPTY (ls-remote zero refs, raw README 404 this probe). Manager relay flagged on this slice's heartbeat. |
| §5 seat mapping + first shippables | **CONSUMED** | Both seats live and FRESH (fm roster gen #5 @ fleet-manager `3150f0e`, generated 04:28Z): Seat A shipped fishing on mining's substrate (44 fishing-core + 20 fishing-inventory-adapter tests in its 257-test suite @ `e62818a`); Seat B's whole first-shippable column shipped (core loop → schema v1 + gate → egg-farm → 11 more themes → setup-code v1; lane self-reports 48 PRs merged-on-green, 827 tests, STEADY-STATE HOLD @ `1e2c9f6`). The mapping's four left-to-manager details (API split · contract home · repo name · sequencing) are all filled: fm `docs/proposals/games-program-mapping-conformed-2026-07-10.md` @ `3150f0e`. |
| §6 sim-lab (idle-economy numeric consumer) | **CONSUMED** | The exact kernel the harvest deferred this probe FOR: pre-registered T1–T10/A1–A10 relayed as this repo's PROPOSAL 006 → sim-lab VERDICT 006 approve, finalized 2026-07-11T05:09:53Z, 7-param table PROVISIONAL → SIM-PINNED (sim-lab `control/outbox.md` @ `d89303e`; full note on `../superbot-idle/idle-economy-sim-kernel-2026-07-11.md`). Residue is LANE work, not probe work: the follow-up tuning PR carrying the verdict's two guardrails — and the lane has not consumed the lift yet (its heartbeat @ `1e2c9f6`, updated 10:11:04Z, still lists "economy tuning (SIM-001)" as a blocker). |
| §6 websites synergy (selector + gallery) | **STILL OPEN** | Same item as §3-consumer above — one open surface, counted once. |
| §6 idea-engine synergy (theme-concept intake) | **OPEN-STANDING (by design)** | Q-0266's never-dry backlog: the lane holds `catalog wave 4+ ON-DEMAND` in its own QUEUE and grew the catalog to 12 without intake help; theme-concept capture stays a standing valid slice here, no dedicated head needed. |
| §7 four decided-and-flagged items | **ALL DECIDED; executed or tracked** | (1) plugin-native/no-old-bot-port — consumed by construction (Seat B is plugin-native, adapter PLUG-001 held pending upstream); (2) setup-code before join-time — consumed (write path frozen, §3 row); (3) drafted-in-idle-promoted-later — draft done, promotion tracked (§4 row); (4) `superbot-idle` name — consumed (the repo exists under that name; owner's click, taken). |
| (adjacent, §3's "read twin") game-state read feed | **OPEN, ROUTED ELSEWHERE** | Not this doc's own item (part-4d relay): fm mapping §1(a) keeps it a superbot-lane committed-JSON feed; not built at superbot `c77ee0d` (three candidate paths 404 this probe — not measured beyond that); the projection-fan-in question is already probed/parked at `../product-forge/games-web-mineverse-scope-seam-2026-07-11.md` (parked(routed)) with `../superbot-mineverse/mining-projection-single-source-2026-07-11.md` folded into it. superbot-mineverse itself carries ZERO theme/setup-code surface (clone-grep empty @ `2f2d33a`) — it consumed the web↔bot CONTRACT-FAMILY discipline (snapshot schema + HMAC write endpoint), not the theme seam. |

**1. What is this really?**
A decided owner directive that FINISHED ROUTING — not an idea awaiting evaluation. At
harvest (PR #38 window) it was "decided mid-dispatch, open items routed via Q-0240";
eleven-ish hours later every §-item is consumed at a live lane HEAD, frozen as a binding
contract, or carried by a dedicated head in this tree with its own disposition (ledger
above). The only probe-shaped kernel it ever contained (§6 idle-economy) was armed,
relayed (PROPOSAL 006), and verdicted (VERDICT 006 approve) before this battery ran.
What remains for THIS file is bookkeeping honesty: recording that the directive's
residue is lane builds and manager relays, with pointers, so no future wake re-probes a
consumed directive.

**2. What is the possibility space?**
Dispositions only — the design space was owner-closed at birth ("decided, not
proposed") and the mapping's four manager details are filled. (a) park(routed) with the
fan-in ledger — records where every open item lives; (b) leave captured — the README's
stale-grounding trap: a captured head invites a future battery to re-recommend on
owner-decided questions, the exact failure the harvest note warned against; (c)
sim-ready — requires a surviving evidence question: none survives (the ledger's open
items are a sequenced UI build, a lane tuning PR, and a manager relay — none simulable);
(d) needs-more-grooming — nothing is ungroomed; the doc's open choices were routed
through Q-0240 and have landed; (e) reject — absurd against seven consumed sections.
The space collapses to (a).

**3. What is the most advanced capability reachable by the simplest implementation?**
One state flip + one ledger table turns this index head from a re-probe hazard into the
games program's fan-in map: any wake (or the manager's :30 sweep) gets, in one read,
what shipped where (with live pins), which three surfaces remain open, and which
tracked head or lane owns each — including one find no other file records yet (the §4
arming event's doc-half fired; the sibling park's 404 grounding was path-keyed
false-negative). Zero new coordination surface invented; three existing heads do the
carrying.

**4. What breaks it?**
- **Ledger rot** — this table is a snapshot of five moving lanes; mitigated because
  every open item is carried by a surface with its own freshness discipline (the two
  parked superbot-idle heads carry event-keyed un-park/Sequence conditions; the
  selector build is sequenced by the fm mapping the manager owns; the tuning PR is the
  lane's own blocker line), so the ledger going stale strands nothing.
- **The §4 relay not happening** — the half-fired arming event is only flagged here and
  on this slice's heartbeat; if the manager sweep misses it, the promotion keeps
  waiting on a condition that already reads satisfied. Cheapest mitigation shipped:
  heartbeat ⚑-note naming the exact citation (`8b55d95` 200 vs the park's 404 list).
- **Misreading "consumed" as "done forever"** — Seat A's remaining audit rows (9⚠️·2❌)
  and world-themes-later are real future work; the ledger deliberately classes them as
  lane roadmap, not open idea-engine items. A future world-theme capture is legitimate
  NEW work, not this head reopening.

**5. What does it unlock?**
Probe-order hygiene: the superbot section's last games-program `captured` head stops
competing for battery passes with genuinely-open work. The manager's sweep gets a
one-read fan-in of the whole games directive (three open surfaces, each with an owner).
And the §4 finding unlocks the theme-schema promotion relay — the decided §7-item-3
move whose tracker was parked on an event that half-fired invisibly.

**6. What does it depend on?**
Nothing forward — a park has no build dependencies. The ledger's load-bearing reads,
all fetched this probe at the pins named above: superbot `c77ee0d` (doc byte-identical
from `41899e1`; feed paths 404), superbot-idle `1e2c9f6` (tree + heartbeat 10:11:04Z),
superbot-games `e62818a` (raw status), superbot-next `8b55d95` (contract doc 200,
ORDER 002 new; plus historical 200s at `4a32f61`/`4c8c5b0`), superbot-plugin-hello
(zero refs), websites `f0e7710` (clone-grep), superbot-mineverse `2f2d33a` (clone-grep),
fleet-manager `3150f0e` (roster gen #5 + conformed mapping), sim-lab VERDICT 006 @
`d89303e`. Cross-check consumed: the roster's superbot-idle/superbot-games/websites
rows agree with the lane heartbeats read directly (freshest-wins never needed —
no layer disagreed this probe).

**7. Which lane should build it?**
No lane — nothing here is buildable BY this repo, and each open item already has its
owner: websites builds the selector/gallery when its sequence arrives (fm mapping §4,
after the read-contract head's build-direct slice, which superbot-idle owns);
superbot-idle ships the VERDICT-006 tuning PR (its own blocker line); the MANAGER
relays the §4 promotion (the parked head's own prescription — this repo writes no
other repo's files, Q-0260). Not sim-lab: no reproduced-evidence question survives —
the directive's numeric kernel is already verdicted.

**8. What is the smallest shippable slice?**
This PR: the state flip + this report + the section-README echo, plus the heartbeat
⚑-note flagging the half-fired §4 arming event for the manager sweep. No outbox entry
(nothing sim-ready). Explicitly NOT in the slice: un-parking the sibling promotion
head (its un-park prescribes a MANAGER relay, and it lives in the superbot-idle
section outside this slice's claim) and any world-theme pre-capture for Seat A (its
audit is mid-flight lane work; capturing now would race the lane's own roadmap).

**Recommendation: park** — routed: every architecture decision was owner/manager-made
before this probe could ask anything (Q-0267 frame; fm conformed mapping's four details
all filled @ `3150f0e`), the directive's one evidence question (§6 idle-economy) was
consumed by PROPOSAL 006 → VERDICT 006 approve, and the three surfaces still open
(websites selector — sequenced LAST by design; the lane's VERDICT-006 tuning PR; the §4
promotion relay whose arming event half-fired at superbot-next `8b55d95`) each already
have a tracked head or named owner — nothing survives for a simulator, so the honest
disposition is the fan-in ledger above.
