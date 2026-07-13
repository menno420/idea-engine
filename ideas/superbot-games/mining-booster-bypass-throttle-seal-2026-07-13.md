# The booster bypass — can a committed-shape lever make the mining energy throttle bind again?

> **State:** sim-ready
> **Class:** game-mechanics · **Target:** `menno420/superbot-games` (mining lane —
> owner of the shop constants and the shared energy pool; V042's own
> recommendation routes this row "sim-first") with `menno420/superbot-idle` /
> fleet ledger as caveat consumers; verification target `menno420/sim-lab` per
> the Q-0264 pipeline
> **Grounding:** https://github.com/menno420/sim-lab@afe18f3efda0b02a4cc786c4873d89175033ca61 · fetched 2026-07-13T12:09:45Z
> (local clone at drafting; every anchor machine-read from the parent's
> committed `sims/verdict-042-mining-economy/{results,fixtures}.json` at that
> pin — exact fractions, never prose transcription; second pin: the parent's
> own packet pin `menno420/superbot-games@57f69be34785afb427d608b207e7369025166e94`,
> whose engine files ride byte-copied + sha256-manifested INSIDE the parent's
> committed subtree, so this head needs zero fresh clones)

**Origin:** drafted under standing owner ORDER 003 (continuous pipeline —
"continue coming up with new ideas, that is your main purpose"). The ORDER 003
GAME-MECHANICS rotation slot, round 5: rounds 1–3 were the casino fairness
triage (P020 → V022 reject, P023 → V025 reject, P027 → V029 null — closed),
round 4 was P031 → V033 (explore pacing null: quest progress carved out of
admission-gating). Round 5 follows the slot's NEWEST verdict line for the first
time: the fresh SIM-REQUEST wave (V042 mining · V043 fishing · V044 escort ·
V045 exploration, all finalized at `afe18f3`) ratified every packet constant —
and V042's own FLAGS section measured, reporting-only, the one surface its
ratify deliberately did not rule: **the booster economy is a coin-profitable
×4.45 bypass of the lane's only pacing control.** The successor-move precedent
(P023 ← V022, P026 ← V024, P029 ← V027, P031 ← V018, P033 ← V023, P034 ← V024)
applied to the game slot's SIM-REQUEST wave for the first time.

## The finding this head prices (V042's own flag, quoted at the pin)

V042 (approve = ratify all mining constants) measured at packet pin `57f69be3`:
rations (20 coins → 25 energy) and energy drinks (40 → 50) both price energy at
**4/5 coins per dig — below the faucet at EVERY depth** (the four committed
depth-row values: 32/7 ≈ 4.571 fresh floor · 848/175 ≈ 4.846 surface roam ·
2703/440 ≈ 6.143 cavern · 8427/1150 ≈ 7.328 deep). So boosted active play runs
~1,800 digs/h (the INT-1 2 s interaction floor) netting **270252/23 ≈ 11,750
coins/h** at the P3 deep profile vs 303372/115 ≈ 2,638 throttled — Forge I in
≈ 15.8 min boosted vs 1.09 h throttled. V042's verbatim flag: "the throttle is
a pacing suggestion, not a cap, for anyone who buys food; to make it bind,
ration > ~183 coins — flagged, possibly intended per the shop's own comment",
and its recommendation (3): "decide whether the booster bypass is intended …
price rations above the marginal dig value … or shrink restore values, **again
sim-first**."

Why it matters beyond one shop row: the energy pool is SHARED (V043's fishing
verdict keys its entire sell-curve calibration to "coins per energy,
at-or-below mining parity"), and every pacing number the wave just ratified —
V042's sword/Forge goal ladder, V043's 4.42–10.20 coins/energy fishing ledger,
V045's quest-loop 15× energy headroom — is stated against the 360/h throttle
the booster voids for anyone holding coins. An unsealed bypass silently
converts four verdicts' sustained-rate ledger into a lower bound for the poor.
The intent question ("is it a deliberate catch-up lane?") is the seat's/owner's
to decide — exactly like V044's packet filed its ask — so this head does what
V041 did for pricing and V044 did for the escort guard: **price the committed
lever menu so the intent decision becomes a table lookup**, never decide intent
by fiat.

## The idea (reasoned to its fuller form — Q-0254 duty)

Sweep the two committed-shape lever families that could make the throttle bind
again, on the parent's own byte-copied engine, against three pre-registered
bands, with the drafting-time liveness arithmetic (the P034-card lesson,
applied as method) already reshaping the design once:

- **REPRICE (reporting-only, excluded by registered arithmetic):** V042's own
  "> ~183 coins" suggestion generalizes to e = price/restore coins-per-energy.
  Sealing at the committed BEST value row (the diamond-tool depth-4 hand-pin
  755/56 ≈ 13.482 coins/energy, reproduced in both V042 and V043) needs
  e ≥ 15·(755/56)/16 = 11325/896 ≈ 12.64 (ration ≥ ~316 coins) — while keeping
  one full-bar emergency refill affordable (≤ 15 min of fresh-floor throttled
  income, 2880/7 ≈ 411.4 coins) needs e ≤ 48/7 ≈ 6.857 for any restore size
  dividing the 60-energy bar. 12.64 > 6.86: **no price-only cell can pass both
  bands** — a pre-computable exclusion (the P033 ρ=1.0 precedent), registered
  and shipped as the reason the second family exists, not discovered mid-run.
- **CAP (the decision family):** cap purchased energy per player per window at
  C ∈ {60, 75, 100, 125} energy/h × window semantics ∈ {sliding-3600 s,
  fixed-hour} = 8 decision cells, at committed prices (refill affordability
  untouched by construction). Closed-form boosted/throttled ratio
  ρ(row, C) = 1 + C·(E − 4/5)/(360·E): at the binding ceiling row 755/56 the
  cells land 1.157 (C=60) / 1.196 (C=75) / **1.261 FAIL** (C=100) / 1.327
  (C=125) against the 5/4 seal band — so the closed form leaves {60, 75} live,
  kills {100, 125} at the ceiling row (C=100 still passes the P3 row at
  1.2475 — knife-edge, disclosed), and the genuinely open number is the
  **engine premium**: how much the real adversary (full-bar burst transients,
  fixed-hour boundary gaming, ration/drink mix, depth targeting, forge-run
  interleaving) adds on top of the closed form, per semantics. That premium is
  the one decision-relevant quantity no drafting arithmetic pins — V018's
  sliding-window art measured exactly this class of gap for encounter caps.

**Bands (registered before any code):**
- **SEAL** — the throttle binds again: engine-measured best-policy boosted net
  coins/h ≤ 5/4 × the same row's throttled coins/h, at EVERY committed value
  row ({P0…P3} + the 755/56 ceiling row; fishing's 18-cell grid rides
  reporting-only — less binding by arithmetic, max 10.199 < 755/56).
- **REFILL** — the booster's committed convenience purpose survives: the cap
  admits ≥ one full-bar emergency refill per window (C ≥ 60) AND that refill
  at committed prices costs ≤ 2880/7 coins (committed: 60 coins — passes; the
  REPRICE exclusion arithmetic is the reason this band exists).
- **PACE** — the ratified goal ladder survives: engine-measured boosted NP-1
  times ≥ 0.8 × V042's committed throttled anchors (Forge I 4476179765/1146072
  ≈ 3905.67 s, Forge II 17222779765/1146072 ≈ 15027.66 s).

**Liveness (each ruling reachable, the P034-card row):** APPROVE — sliding
{60, 75} clear every closed form with ≥ 0.054 margin at the binding row;
REJECT — reachable iff the measured engine premium exceeds that margin on BOTH
semantics at every C (the fragile direction is APPROVE, so REJECT is checked
first); NULL — the expected candidate axis is the semantics fork itself
(fixed-hour gaming premium is the open number: a fixed-hour cap is the cheap
build, and if only sliding seals, that conditional IS the citable finding).

## Alternatives weighed for the round-5 slot (on the actual evidence, then passed)

- **V042's other flag — amount-inert pickaxe tiers** (×1.13/×1.25 grant zero
  extra ore under BASE_ROLL_MAX=2 + round(); rewards.py's "a better tool still
  pays" measured FALSE for 2 of 5 tiers): real, but a tool-FEEL redesign whose
  lever (fractional-carry vs probabilistic bonus) is the seat's design taste,
  stakes are two low tiers' feltness, and it shares no cross-verdict ledger
  consequence. Named runner-up; its constants ride here as grounding context.
- **V038's min-visible-delta floor** (superbot-idle feel): V038's own
  recommendation says "build it engine-side … and give it its own sim before
  registering" — the floor MECHANISM does not exist at pin `d992c568`, so a
  sim now would price a sketch, not committed constants. Parked until the fold
  hook ships.
- **V044's post-guard loopability census of other dnd bundles:** the one-shot
  guard has not landed (recommendation only), and V044's committed path-census
  scripts make this a cheap seat-side audit, not a pre-registered balance sim.
- **V045's capability-gap reconciliation:** NULL by construction until
  superbot's survival P0 bands ship (D-0008's named upstream artifact);
  scoring is lookup on V045's committed tables — nothing to sim.

## Sim spec (pre-registered)

**Machinery (hermetic, zero fresh clones).** The parent's committed engine
subtree `sims/verdict-042-mining-economy/engine/` @ sim-lab `afe18f3` (13
files byte-copied from packet pin `57f69be3`, sha256 MANIFEST re-verified
before import — the V043/V028 byte-reuse precedent); every anchor machine-read
from the parent's committed `results.json`/`fixtures.json` at the same pin
into this head's fixture JSON.

**Arms.** Arm A (exact): Fraction closed forms for every cell — ρ(row, C), the
REPRICE exclusion pair (11325/896 vs 48/7), refill costs, ladder-time
predictions. Arm S (engine): seeded event-driven runs of the byte-copied
engine under an injected booster-admission layer implementing each (C,
semantics) cell — policies: THROTTLED control (never buys), HONEST-CASUAL
(≤ one full-bar refill/h, 30-min sessions), BOOST-FARMER (greedy adversary:
optimizes depth row incl. the diamond-d4 surface, ration/drink mix, purchase
timing, full-bar burst scheduling, and fixed-hour boundary gaming), and the
NP-1 ladder runs (boosted Forge I/II) per cell; 8 h horizon, M = 400
replications per (cell, policy), decision on measured means under familywise
SE-calibrated tolerances pre-checked in the fixture (the V027/V031 pipeline
lesson at design time).

**Seeds.** 20261281 main / 20261282 stability (half-M, must reproduce the
ruling) / 20261283 reporting / 20261284 aux — allocated strictly above the
fleet high-water 20261280 (V043's robustness leg, re-read at the sim-lab
ledger @ `afe18f3`, not from any dispatch brief).

**Gates (run invalid on any failure).** B0 reproduces the parent's committed
anchors EXACTLY before any lever cell runs (the four depth-row fractions ·
4/5 coins/energy · digs_per_hour_INT1 = 1800 · net/dig 7507/1150 · bypass
270252/23 · Forge I 1005258865/2292144 digs / 4476179765/1146072 s · Forge II
3554578865/2292144 digs / 17222779765/1146072 s · ration 20/25, drink 40/50,
MAX_ENERGY 60, REGEN_SECONDS 10 · the 755/56 hand-pin as V043 reproduced it);
C=0 cell ≡ the throttled control exactly; C=∞ at e=4/5 ≡ the parent's bypass
anchor; Arm-S agreement with Arm A on every unbounded closed form under the
pre-checked familywise tolerances; an independent sliding-window re-audit of
admitted purchased energy (the V018 audit art); the drink-mix invariance check
(cap accounting in energy units — mix changes purchase-action count only);
twin independently-written decision evaluators; stdout + results.json
byte-identical across two process runs; CPython minor pinned.

**Decision rule (pre-registered order, REJECT checked first).**
- **REJECT** ("no committed-shape cap seals the sink — redesign, not retune"):
  NO decision cell passes SEAL+REFILL+PACE, stability-reproduced. Consequence:
  the rescue family is named with its own future sim (diminishing restore /
  boost-fatigue — a mechanism change, out of this head's registered scope);
  until then the V042/V043/V045 ledger carries the measured boosted-column
  caveat, and the seat's intent call gets the full priced table.
- **APPROVE** ("cap it — the throttle binds again"): ≥ 2 decision cells within
  ONE window semantics pass all three bands, stability-reproduced (a band, not
  a knife-edge point — the P031 two-consecutive-cells rule). Consequence: the
  cheapest-diff passing cell is recommended (expected sliding C=75 by closed
  form — disclosed, must survive the engine premium); the seat decides
  intended-vs-not from the menu; on "intended", the same table ships as the
  ledger's boosted column instead.
- **NULL** (anything else — semantics-conditional or single-cell passes): the
  conditional rule is the citable finding (expected: sliding-only seals — the
  cheap fixed-hour cap is insufficient, with the measured boundary-gaming
  premium as the number), and the cheapest LIVE probe is named: shop telemetry
  (booster purchases/player/h + purchase-time energy level) locating the real
  k and waste rate at zero new tooling before the seat commits a cell.

**Boundaries (stated in the verdict).** Intent is NOT ruled — this head prices
the lever menu (the V041 frontier form; V044's packet-files-intent-as-owner-call
posture; V042's "possibly intended per the shop's own comment" restated
verbatim). Fun/retention and multiplayer/trade out of scope (the parent's own
LIMITS inherited). The amount-inert pickaxe row is the OTHER V042 flag, out of
scope, named runner-up. INT-1 (2 s) is a registered assumption inherited from
V042 — flip axis disclosed, with the cap family's structural advantage stated:
once C binds, sustained digs/h = 360 + C regardless of the interaction floor,
so cap conclusions are INT-1-robust where the ∞-cell bypass numbers are not.
Fishing rows ride reporting-only (max 10.199 coins/energy < the 755/56 binding
row by arithmetic). Cross-session cap persistence is host territory (the V044
per-session scope precedent).

## Dedup (explicit, against outbox 001–034 + verdicts V001–V045)

- **V042 (the parent, deliberately):** its answered question — ratify the
  descend gate and the 60/3,000/8,000 sink ladder — is settled and not
  re-asked; its FAUCET-BYPASS row was REPORTING-ONLY by its own registration
  ("flagged, not ordered"), its recommendation names this exact head ("register
  … with their own sims if wanted", "again sim-first"), and its committed
  engine + anchors become this head's machinery and regression gates.
- **V043 (fishing):** consumer, not overlap — its parity ledger is keyed to the
  throttle this head seals; its rows enter as reporting-only value surfaces.
- **V044/V045:** escort mint guard and exploration bands — different faucets,
  zero shared lever/band/metric; V045's quest loop never touches the energy
  gradient (its own GB5 15× headroom finding).
- **P031 → V033:** quest-beat admission under the encounter K-window — a
  different shared-resource cap (encounter admissions, not purchased energy);
  its sliding-window audit art is imported as method, its question not re-asked.
- **The casino family (P020/P023/P027 → V022/V025/V029):** wager-sink ruin
  dynamics, zero shared fixture/metric; V017/V038 are the OTHER repo's idle
  engine (V038's floor thread weighed and passed above).
- Tree-wide `grep -rniE "booster|ration|energy.drink|throttle.?bypass"` over
  `ideas/ .sessions/ control/` (bootstrap.py/.substrate excluded) at drafting
  HEAD `8218d66`: every "ration" hit is a "registration" substring; zero
  booster/bypass hits. The same sweep over the sim-lab clone @ `afe18f3` hits
  only V042's own flag and its outbox echo. No proposal 001–034 and no verdict
  V001–V045 sweeps consumable pricing, restore caps, or any energy-throttle
  seal.

## Probe report battery (v0, 2026-07-13)

> Single-pass battery (panel not escalated: a modeling head chained to a
> committed parent verdict's own machinery and flag, sim is report-only
> evidence, no spend/publish/irreversible surface). Verify-first ran FIRST,
> live this slice: (a) **anchors** — V042's committed `results.json` parsed at
> the local sim-lab clone @ `afe18f3`; every fraction quoted in this file
> (32/7 · 848/175 · 2703/440 · 8427/1150 · 7507/1150 · 270252/23 · 4/5 · 1800
> · the Forge dig/second fractions) machine-read, not transcribed. (b)
> **liveness arithmetic** — the closed-form ρ table computed at drafting for
> every (row, C) cell; it killed the REPRICE family as a decision arm (the
> 11325/896 vs 48/7 exclusion) and pinned the open engine-premium question.
> (c) **dedup** — the sweeps in the Dedup section, both trees, zero prior hits
> on the head's axes. (d) **feasibility** — the parent's engine-driven legs
> ran in seconds at M ≥ 400; this adds one admission layer and three policies
> over 8 decision + ~10 reporting cells — well under a minute stdlib CPython.

**1. What is this really?** The seal for the mining lane's only pacing
control: V042 ratified every constant but measured (reporting-only) that 0.8
coins-per-energy boosters make the 360/h throttle voluntary for anyone
holding coins; this head sweeps the two committed-shape levers (reprice —
excluded by registered arithmetic; restore-rate cap × window semantics) on
the parent's own byte-copied engine so the seat's intent decision becomes a
priced lookup.

**2. What is the possibility space?** (i) Do nothing — the ledger the
V042–V045 wave just cross-pinned stays keyed to a throttle that does not bind,
and the fishing parity design ("slower, calmer faucet") is voided by a coin
purchase. (ii) Let the seat pick a ration price by feel — V042's own flag
shows the intuitive fix (~183+ coins) prices the emergency refill out of
casual reach at the committed value ceiling; the seat's fishing lane already
has a "never hand-edit a weight" rule for exactly this class. (iii) Declare
it intended — legitimate, but that decision deserves the measured boosted
column, not a guess. (iv) This head: pre-register the bands, run the engine
adversary, hand over the menu.

**3. What is the most advanced capability reachable by the simplest
implementation?** One stdlib file over the parent's already-committed engine
subtree: an admission layer (~a windowed counter), three policies, and
Fraction closed forms — yielding the full (cell × policy × row) ρ table, the
measured fixed-hour gaming premium (a number nothing else in the fleet pins),
the boosted goal-ladder times, and the REPRICE exclusion proof, byte-identical
on re-run.

**4. What breaks it? (assumptions made explicit)** (a) INT-1 is a registered
assumption — disclosed, with the cap family's INT-1-robustness stated (once C
binds, digs/h = 360 + C); (b) the adversary is greedy-registered, not
exhaustive — the sliding-window audit and closed-form ceilings bound what any
policy can extract, and the fixed-hour premium is measured against the best
REGISTERED gamer (stated as a lower bound on gaming); (c) the bands (5/4,
0.8×, 15-min refill) are registered judgment lines — full tables ship so a
re-drawn line re-reads, never re-runs (the parent's own discipline); (d)
intent is the seat's — every ruling leaves the intended-vs-not fork open and
priced; (e) cross-session persistence of a cap is host territory (V044
precedent), stated.

**5. What does it unlock?** The throttle either binds again (with a measured,
cheapest-diff cap cell) or its bypass becomes a deliberate, priced design
choice; the V042/V043/V045 shared-energy ledger gains its boosted column
either way; and the admission-layer + gaming-premium kernel is reusable art
for every future consumable/cap head (fishing boosters, idle rebuy, any
buy-energy surface).

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing
external at sim time — machinery and anchors are already committed in
sim-lab's own tree (byte-reuse precedent), constants quoted verbatim in this
file and copied into fixture JSON. Kill tests, run live this slice: a prior
booster/cap sweep anywhere (NOT found — dedup above); a committed cap surface
already in the engine (NOT found — the parent's flag says "the throttle is a
pacing suggestion, not a cap"); a seat-side registration of this row (NOT
found — V042's recommendation leaves it "the seat's to register … if
wanted"); infeasible runtime (NOT found — the parent's M-seeded engine legs
ran in seconds).

**7. Which lane should build it — and what does it displace or duplicate?**
sim-lab runs it (the engine copy, MANIFEST, and every anchor live in its own
committed tree — zero fresh clones). Consumers: superbot-games (the shop/cap
decision + the intent call), the fleet ledger (V043 parity, V045 coherence),
and the manager's relay per Q-0264. Duplicates nothing: V042 is chained
(regression gates), never re-run; V044's guard and V033's carve-out are
different faucets.

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one
stdlib file (admission layer + three policies + Fraction closed forms +
gates), one fixture JSON (constants verbatim from this file, seeds
20261281–84, bands, decision rule, liveness table), one results table
{net coins/h, ρ, refill cost, ladder times, premium} × (18 cells × 3 policies
× 5 value rows) plus regression and stability legs, ending in exactly one of
APPROVE/REJECT/NULL per the pre-registered rule — reproducible from the
fixtures alone, byte-identical on re-run, no flags.

**Recommendation: sim-ready** — the question is crisp and computable on
machinery already committed in sim-lab's own tree, the bands and decision rule
are registered above BEFORE any code exists with REJECT checked first and
every ruling's liveness shown by drafting arithmetic (the P034-card lesson
applied as method — it already reshaped this head once), the parent verdict
itself routes the row "sim-first", and every outcome changes what the seat
ships (a measured cap cell, a priced intended-bypass column, or the
semantics-conditional rule with the gaming premium as the number). Seeds
20261281–84, strictly above the fleet high-water 20261280.

## Pinned constants (quoted at drafting — fixture JSON copies these verbatim)

- sim-lab @ `afe18f3efda0b02a4cc786c4873d89175033ca61`,
  `sims/verdict-042-mining-economy/results.json` (machine-read): depth-row
  E[coins/dig] = 32/7 (P0 fresh floor) · 848/175 (P1 surface) · 2703/440 (P2
  cavern) · 8427/1150 (P3 deep); `faucet_bypass_leg`: coins_per_dig_cost 4/5,
  digs_per_hour_INT1 1800, net_coins_per_dig_P3 7507/1150,
  net_coins_per_hour_boosted_P3 270252/23; NP-1: Forge I 1005258865/2292144
  digs / 4476179765/1146072 s, Forge II 3554578865/2292144 digs /
  17222779765/1146072 s; `fixtures.json`: GEAR_SHOP ration 20 / energy_drink
  40, energy MAX_ENERGY 60 / REGEN_SECONDS 10 / 360 digs/h sustained, INT-1
  2 s (registered assumption, inherited).
- sim-lab @ `afe18f3`, `sims/verdict-043-fishing-economy/` (cross-pins): the
  mining hand-pin 755/56 (diamond-tool depth-4 ceiling row) and the fishing
  coins/energy grid max 10.199 (reporting-only rows); V043's byte-reuse +
  never-hand-edit-a-weight discipline.
- Parent engine: `sims/verdict-042-mining-economy/engine/` @ `afe18f3` (13
  files byte-copied from `menno420/superbot-games@57f69be3`, sha256 MANIFEST —
  re-verified before import at verdict time).
- Derived at drafting (Arm-A pre-registrations): REPRICE exclusion pair
  11325/896 vs 48/7; ρ(row, C) closed-form table incl. ceiling-row cells
  1.157/1.196/1.261/1.327 at C = 60/75/100/125; bypass ratios 37535/8427
  (V042 accounting) and 38455/8427 (regen-credited); refill bar 2880/7.
