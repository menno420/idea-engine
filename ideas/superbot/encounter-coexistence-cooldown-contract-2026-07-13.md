# Encounter coexistence — sim-pin the shared engine's cooldown-namespace contract before the first build fixes it

> **State:** sim-ready
> **Class:** product · **Target:** `menno420/superbot`
> **Grounding:** https://github.com/menno420/superbot/blob/0f991a8442690c765037d48b37fefcbd95bfa0ee/docs/ideas/wild-encounters-activity-spawning-2026-06-20.md@0f991a84 · fetched 2026-07-13T00:31Z
> *(pin annotation: live HEAD `0f991a8` by `git ls-remote` 00:29Z, tree read via a
> blobless clone 00:31Z. The window is verified OPEN at HEAD: NO Encounters cog,
> NO activity-spawn engine, NO grid-encounter slice anywhere in the tree — a
> full-tree name scan finds only the pure creature-game catch roll
> (`disbot/utils/creatures/encounters.py`, "no Discord, no DB") plus the two idea
> docs; neither sim-pinned build has landed, so neither has "fixed" the shared
> engine yet. Second pin, the shared seam itself: superbot-games HEAD `64b3371`
> ships `games/shared/encounter/interface.py` whose docstring rules "One
> resolution core serves all three Q-0186 encounter triggers (grid roaming,
> explore actions, chat activity)" — and a grep of that interface for
> cooldown/rate/throttle/debounce returns NOTHING: the pacing layer is
> uncontracted at the seam both consumers will share.)*
> **Sequence:** before the first encounter-consumer build lands (the Q-0186 BUILD-FIRST Encounters cog or the Q-0198 grid slice — VERDICT 008's own coupling clause is "shares the encounter-resolution engine with VERDICT 001 … whichever build lands first fixes it", and the fix-by-accident is exactly what this head pre-empts; window verified open at superbot `0f991a8`)

**Origin:** drafted this slice under the standing owner ORDER 003 (keep new ideas
coming and tested for each repo) — the superbot content-lane head: two landed
verdicts left one measured contract row missing, and the window to pin it closes
at the first build.

## The idea (reasoned to its fuller form — Q-0254 duty)

sim-lab has now tuned BOTH encounter surfaces the superbot hub is about to build —
separately. VERDICT 001 pinned wild encounters (CHAT_ACTIVITY): threshold=24
messages, debounce=30 s, **cooldown=900 s per-claimer**, enforced server-side at
the Claim callback, hard-capping any account at 4 claims/hr. VERDICT 008 pinned
grid encounters (GRID_ROAM): depth threshold=15, chance=0.02, **cooldown=600 s
per-player**, analytically capping everyone at 6 enc/hr. Each verdict proved its
shape — rare-but-visible, farm-unprofitable in RATE terms — for a player who
plays ONLY that surface. But the two surfaces resolve through one shared engine
(V008's own recommendation line; the superbot-games interface docstring rules
"one resolution core serves all three triggers"), and that engine's contract has
NO rule for where per-player cooldown state lives. Nobody decided the namespace;
whichever build lands first will decide it silently.

The namespace choice is not bookkeeping — it moves the pinned numbers by 2.5×.
Per-source clocks (each surface keeps its own 900 s / 600 s timer) give a player
who does both a combined interruption ceiling of 4 + 6 = **10/hr**; one shared
per-player clock gives 3600/900 = **4/hr** and lets either surface's claim lock
the other out. Neither verdict's Q-0087 never-mandatory interruption bound was
measured for the combined player, and per-source clocks open a channel neither
solo sim could see: **cross-surface cooldown arbitrage** — a farmer who fills the
grid cooldown's dead time with chat-spam toward the next wild spawn (and vice
versa) runs both caps in parallel, where each verdict's farm-unprofitability
proof (V001: fast spam yields ZERO extra; V008: reward-per-action collapses)
bounded only its own surface. Combined encounter mint from one player across two
surfaces was likewise never measured, even in the relative terms both verdicts
used.

So the head: compose the two verdicts' OWN committed trace models into joint
player profiles and sweep the cooldown-namespace contract — (a) per-source
clocks at the pinned defaults, (b) one shared per-player clock, (c) per-source
clocks plus a combined per-player hourly cap — scoring every cell against BOTH
verdicts' pinned shapes simultaneously. The output is one contract row (namespace
rule + combined-rate guardrail + which pinned defaults survive vs re-pin) handed
to the shared engine BEFORE the first consumer build hard-codes an answer nobody
evidenced — or an explicit measured finding that coexistence effects are
negligible and the solo-tuned defaults stand as-is.

**The sim (a contract sweep on the two verdicted trace models, all fixtures
committed):** joint player profiles composed from V001's channel-activity tiers
(low/med/high + paced-spam farmer) and V008's grid playstyles (casual roamer,
deep-runner, `!fastmine` grinder): chat-only and grid-only **regression legs
first** — each must reproduce its verdict's solo headline rates (V001: 0.93 /
3.00 / 4.38 spawns per active-hour, 4-claims/hr farmer cap; V008: ~0.2 / ~2.8 /
~5.2 enc/hr, 6/hr cap) before any joint cell runs, the VERDICT 017 baseline-leg
discipline — then mixed-casual, mixed-deep, and a cross-surface arbitrage farmer
that switches surfaces whenever one cooldown blocks it. Contract grid: **(a)**
per-source clocks (900 s / 600 s as pinned) · **(b)** shared per-player clock,
c ∈ {600, 900} s · **(c)** per-source clocks + combined per-player hourly cap,
K ∈ {4, 6, 8}. Scored per cell and profile: per-surface spawn/encounter rates vs
each verdict's solo bands (wild rare-but-visible per traffic tier under the
5.22/hr debounce×threshold ceiling; grid zero-above-threshold,
rare-but-present at depth); combined interruptions/hr vs the stricter solo
ceiling; arbitrage-farmer vs honest-mixed combined encounter-RATE ratio vs the
two solo farmer bounds; combined encounter-mint share in rate/fraction terms
only (the reward-VALUE wall both verdicts named is restated, not re-attempted).
Deterministic seeds, stdlib-only, traces + grid JSON committed.

## Relations (adjacent heads — deliberately links, not duplication)

- [`wild-encounters-activity-spawning-2026-07-10.md`](wild-encounters-activity-spawning-2026-07-10.md)
  (**PROPOSAL 003 → sim-lab VERDICT 001**) — parent #1, single-surface by its own
  text: its question sweeps spawn/debounce/cooldown for channel-activity traces
  alone; its verdict's cap math (4 claims/hr) is per-surface. This head holds its
  pinned defaults fixed and asks only the question it could not see: what happens
  when its player is ALSO V008's player.
- [`mining-grid-encounters-2026-07-10.md`](mining-grid-encounters-2026-07-10.md)
  (**PROPOSAL 008 → sim-lab VERDICT 008**) — parent #2, same relation; its
  recommendation line is where the coupling debt is RECORDED ("shares the
  encounter-resolution engine with VERDICT 001 … whichever build lands first
  fixes it") without being priced. This head prices it.
- [`../superbot-games/shared-encounter-engine-consumer-contract-2026-07-10.md`](../superbot-games/shared-encounter-engine-consumer-contract-2026-07-10.md)
  — the semantics half of the same seam (per-trigger payload keys, kind
  vocabulary, reward routing), parked build-direct with "no parameter question
  left for sim-lab" — true WITHIN its scope, which is contract prose an executable
  conformance suite can check. The cooldown namespace is the parameter question a
  contract doc cannot settle by writing: it needs a measured answer, and this
  verdict supplies the row that head's CONTRACT.md slice should carry. Links, not
  duplication: that head names WHO the surface serves; this one pins HOW OFTEN it
  may fire per player across consumers.
- [`explore-hub-federated-world-2026-07-10.md`](explore-hub-federated-world-2026-07-10.md)
  (**PROPOSAL 004 → VERDICT 004**) — the XP-split layer above all game loops;
  disjoint question (reward trickle, not encounter pacing).
- vs the outbox (001–015): 003 and 008 are the nearest neighbors (above), each
  explicitly solo-surface; no other proposal touches encounter pacing. 006/015
  are the other-repo idle engine; 013/014 fleet-process sweeps. No proposal and
  no verdict runs a joint trace or asks cooldown scoping — checked against the
  sim-lab verdict ledger through VERDICT 017 (read at sim-lab `2e28767` this
  slice).
- The third trigger, EXPLORE_ACTION (superbot-games quest beats), inherits the
  namespace RULE by contract but is out of this sweep: its pacing is pinned by
  the lane's own balance sim, and its consumer lives in another repo's tree.

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: content-lane parameter head, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe
> battery). Verify-first ran FIRST, live this slice: (a) **window at HEAD** —
> superbot `0f991a8` (ls-remote 00:29Z, blobless clone): no Encounters cog, no
> spawn engine, no grid-encounter slice; the only encounter code in the tree is
> the pure creature-game catch roll. (b) **seam at HEAD** — superbot-games
> `64b3371`: `games/shared/encounter/interface.py` names all three triggers,
> rules one resolution core, and carries zero cooldown/rate/throttle/debounce
> surface (grep empty). (c) **kill test NOT triggered** — no cooldown-namespace
> rule registered anywhere (superbot tree, superbot-games shared seam, both
> parent ideas, sim-lab outbox through VERDICT 017); neither verdict's sim ran a
> joint trace (V001: 4×5 spawn sweep on activity traces; V008: traversal traces —
> both committed in sim-lab `sims/`, re-read this slice); no sibling proposal
> names coexistence, arbitrage, or namespace.

**1. What is this really?** The missing third verdict of a two-verdict family:
001 and 008 each answered "is this surface safe alone?" and both wrote down —
without pricing it — that they share one engine. This head is the interaction
term: one sweep that decides whether the two solo-tuned default sets compose,
and pins the contract row (cooldown namespace + combined-rate guardrail) that
the shared engine needs before its first consumer hard-codes an accident.

**2. What is the possibility space?** (i) Do nothing — whichever build lands
first fixes the namespace silently (V008's own clause), and the second consumer
inherits either a 10/hr combined interruption ceiling nobody approved or a
shared clock that halves its verdicted rates; the retrofit lands in a
claim-first shared path where interface changes cost a both-lanes announcement.
(ii) Rule it by prose in the CONTRACT.md slice — picks a namespace with zero
evidence; exactly the invent-at-build-time move the pipeline exists to prevent.
(iii) Sweep first, pin the row, then build — this head; both builds inherit a
measured rule. (iv) Re-open both verdicts' defaults jointly — over-scoped: the
solo shapes are settled evidence; only the composition is unmeasured, so the
sweep holds solo defaults fixed except where a coexistence cell itself names a
breach.

**3. What is the most advanced capability reachable by the simplest
implementation?** One committed stdlib driver composing two ALREADY-VERDICTED
trace models prices a cross-surface design rule neither sim could see alone:
~13 contract cells × 5 profiles, deterministic, expected seconds (V001's full
sweep ran 946 self-checks; V008's cap is closed-form — the regression legs have
analytic anchors). The winning cell is directly the contract row for
superbot-games' parked CONTRACT slice AND the pacing spec for the Q-0186
Encounters-cog build — two lanes' build inputs from one sweep on fixtures that
already exist as committed precedent.

**4. What breaks it? (assumptions made explicit)** (a) **The mixed-player model
is a model** — how much a real player interleaves chat and mining is unknown;
the sweep brackets it (mixed-casual vs mixed-deep vs arbitrage-optimal) and the
verdict must report the bracket, not a point. (b) **Trace fidelity to the
parents** — the joint driver re-implements two committed trace models;
regression legs must reproduce each verdict's solo headline numbers BEFORE any
joint cell counts (the VERDICT 017 B0 discipline; a miss is a first-class
finding, not a tuning knob). (c) **Reward VALUE stays walled** — no live
earn-rate baseline exists (both parents' verdicts, verbatim); every mint
conclusion here is RATE/fraction-only, and the verdict restates the caveat and
extends the named telemetry list with the combined per-player fields instead of
pretending the wall moved. (d) **The engine may never be shared in code** —
Q-0186's cog builds in the hub, which cannot import `games/shared/` (the
consumer-contract probe's honest scope note); the namespace rule still binds as
a mirrored schema/contract either way, and the verdict should say so.

**5. What does it unlock?** The Q-0186 BUILD-FIRST Encounters cog lands with a
combined-player guardrail instead of a solo-only one; the grid slice lands
second WITHOUT a retrofit; superbot-games' CONTRACT.md slice gains its one
missing measured row; the gen-2 production-resolver swap conforms to a pacing
contract instead of an accident; and the pipeline gets its first
interaction-term verdict — 001/008 pinned surfaces alone, this pins their
composition, closing the family.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing
unshipped: both parent verdicts are finalized with committed sims (sim-lab
`sims/intake-003-wild-encounter-spawn-tuning/`,
`sims/verdict-008-mining-grid-encounters/` — the trace models and cap math are
the fixture precedent, composed not re-invented); the contract grid and joint
profiles are constructible fixture JSON committed with the sim; runtime is
stdlib-only, deterministic, no network after fixture capture. Kill tests, run
live this slice: an existing namespace rule (NOT found — interface grep empty),
either build landed (NOT found at `0f991a8`), a joint-trace verdict or sibling
proposal (NOT found through VERDICT 017). Sim-worthy or judgment-only:
sim-worthy — falsifiable per-cell criteria against two sets of already-pinned
bands; the one judgment question (is 10/hr combined interruption acceptable
even if bounded?) is explicitly carved to the owner via the recommended
guardrail's cap parameter.

**7. Which lane should build it — and what does it displace or duplicate?**
sim-lab runs the sweep (its own two committed trace models, its harness, its
verdict grammar); `menno420/superbot` builds the Encounters cog / grid slice
against the pinned row, and `menno420/superbot-games` carries the row in its
shared-engine CONTRACT slice (Q-0260: this repo writes neither lane's files —
the verdict routes via the manager as evidence, bundling naturally with the
parked consumer-contract head's gen-2 routing). Duplicates nothing: swept by
name this slice (rg over ideas/ + .sessions/ + control/ for
coexist/arbitrage/namespace/combined-trace, bootstrap.py and .substrate
excluded; sim-lab outbox + sims/ for the same) — every hit is a parent verdict
recording the coupling or the consumer-contract head scoping it out.

**8. What is the smallest shippable slice?** One sim-lab intake dir: one stdlib
driver (both parents' trace models composed + the cooldown-state machine per
contract), committed grid JSON (~13 contract cells × 5 profiles + 2 regression
legs), committed seeds, and one results table {per-surface rates vs solo bands,
combined interruptions/hr, arbitrage-vs-honest ratio, combined mint share}
ending in ONE recommended contract row — reproducible from the fixtures alone,
byte-identical on re-run, no flags.

**Recommendation: sim-ready** — both parents are finalized evidence, the
coupling debt is recorded in a verdict's own text but priced nowhere, the window
is verified open at live HEAD (no consumer build landed, no namespace rule
anywhere), and the verdict changes what two lanes build next (a measured
namespace + guardrail row vs a silent accident of build order). THE ONE QUESTION
for the simulator: *Under joint traces composing the two verdicted player models
— VERDICT 001's channel-activity tiers (low/med/high + paced-spam farmer) and
VERDICT 008's grid playstyles (casual roamer, deep-runner, `!fastmine` grinder)
into single-player profiles (chat-only and grid-only regression legs FIRST, each
reproducing its verdict's solo headline rates, then mixed-casual, mixed-deep,
and a cross-surface arbitrage farmer that fills either surface's cooldown dead
time with the other surface's actions), which cooldown-namespace contract — (a)
per-source clocks at the pinned defaults (CHAT_ACTIVITY 900 s / GRID_ROAM 600 s,
combined per-player ceiling 10/hr), (b) one shared per-player clock (c ∈ {600,
900} s), (c) per-source clocks plus a combined per-player hourly cap (K ∈ {4, 6,
8}) — keeps BOTH verdicts' pinned shapes simultaneously true (wild:
rare-but-visible per traffic tier under the 5.22/hr debounce×threshold ceiling;
grid: zero above depth threshold, rare-but-present at depth; farming
unprofitable in RATE terms on each surface) while bounding the combined
per-player interruption rate at or under the stricter solo ceiling (the Q-0087
never-mandatory bound), and does cross-surface cooldown arbitrage buy the farmer
a combined encounter-rate yield materially above the honest mixed profiles' — i.e.
do the two solo-tuned default sets survive coexistence unchanged, or does a
named default or the namespace rule itself need re-pinning before the first
build fixes the engine?* Done-when: the regression legs reproducing V001's
0.93/3.00/4.38 spawns-per-active-hour + 4-claims/hr cap and V008's
~0.2/~2.8/~5.2 enc/hr + 6/hr cap, plus the per-contract per-profile table
{per-surface rates vs solo bands, combined interruptions/hr,
arbitrage-vs-honest-mixed rate ratio, combined mint share in rate terms},
ending in ONE recommended contract row (cooldown namespace + combined-rate
guardrail + which pinned defaults survive vs re-pin) for the shared engine —
handed to the superbot-games CONTRACT slice and the Q-0186 Encounters-cog build
before either lands — OR an explicit finding that coexistence effects under
per-source clocks are negligible (bounds stated), so both builds proceed
solo-tuned with a one-line contract note; the verdict must restate the parents'
reward-VALUE caveat verbatim (no live earn-rate baseline — rate terms only) and
extend their named telemetry lists with the combined per-player fields, must
hold both verdicts' solo defaults not-re-opened except where a coexistence cell
itself names the breach, and must state that EXPLORE_ACTION inherits the
namespace rule by contract, not by this sweep.
