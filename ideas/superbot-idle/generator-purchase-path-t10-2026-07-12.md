# Generator purchase path — sim-pin the T10 cost curve before the mechanic lands

> **State:** sim-ready
> **Class:** product · **Target:** `menno420/superbot-idle`
> **Grounding:** https://github.com/menno420/superbot-idle/blob/c753bc8f5ace96e4632510f43b53f0ee45e2def5/docs/current-state.md@c753bc8 · fetched 2026-07-12T23:04Z
> *(pin annotation: live HEAD `c753bc8` by `git ls-remote` 22:58Z, re-read via a
> blobless clone 23:04Z. The premise holds at HEAD, in prose AND in the tree:
> `docs/current-state.md` — "**No generator purchase path** — generator counts are
> fixed; target T10 is pre-registered for the future mechanic"; tree-grep over
> `idle_engine/` finds `purchase_upgrade`/`purchase_upgrades` only, no generator
> purchase function anywhere. `docs/design/economy-v1.md` at HEAD still carries the
> T10 row verbatim from the `f11c71a` pin (raw fetch at both pins, identical): "T10 |
> Time-to-second-generator-tier (FUTURE mechanic — no purchase path yet;
> pre-registered ahead of implementation) | 30 min active | 15–45 min" and "T10 is
> registered now so the generator-cost slice inherits a target instead of inventing
> one post hoc". Engine drift since the VERDICT 006 pin, found by diffing the live
> core against sim-lab's byte-copy: milestones landed (`achievements.py`,
> `MILESTONE_OWNED_THRESHOLDS = (10, 100, 1_000)`, `MILESTONE_BONUS_PERCENT = 5`)
> plus the schema-bounded theme pct — the production fold is now `base_rate * count
> * upgrade_pct * prestige_pct * milestone_pct * theme_pct // 100_000_000`.)*
> **Sequence:** after sim-lab VERDICT 006 (the arming event — SIM-001 ruled approve, 10/10 A-criteria, parameter table graduated; the 2026-07-11 first-batch card recorded this exact head as deliberately DROPPED with "natural sequencing is after the SIM-001 verdict anyway" — the verdict has now landed, so the drop's own sequencing rule un-parks it)

**Origin:** drafted this slice under the standing owner ORDER 003 (keep new ideas
coming and tested for each repo) — the superbot-idle content-lane head: the lane's
next economy mechanic, currently blocked on exactly the evidence a sim produces.

## The idea (reasoned to its fuller form — Q-0254 duty)

superbot-idle's economy shipped its first verdict loop by the book: seven parameters
pre-registered with falsifiable pacing targets (T1–T9), SIM-001 executed against the
real engine, VERDICT 006 approved 10/10 and graduated the table. But the doc
pre-registered a TENTH target for a mechanic that does not exist yet: T10,
time-to-second-generator-tier, 30 min active, band 15–45 min — "registered now so
the generator-cost slice inherits a target instead of inventing one post hoc."
The target exists; the cost curve that would hit it does not. The engine is already
multi-generator capable (`owned` maps spec_id → count; production folds `base_rate *
count`), so the purchase path is a thin new surface: a generator cost curve (what
does the Nth copy of tier 1 cost, what does the tier-2 unlock cost) plus a purchase
function shaped like the existing `purchase_upgrade`.

The lane's own newer docs sharpen the stakes. The achievements slice (landed after
the VERDICT 006 pin) pre-registered an `owned` milestone track — 10/100/1,000 total
generators, "+5%/milestone", with rung 1 called "a first-session target once
generator purchase lands" — and its "What the Simulator must pin" list defers three
questions to exactly this sim: rung arrival times per player profile, whether the
milestone fold pushes T2–T7 out of their registered bands, and "whether `owned`
rungs 2–3 are reachable at all under the future generator cost curves
(pre-registered ahead of that mechanic, like T10)." And VERDICT 006's own limits
section flagged the `base_rate=1` floor — integer percent effects on a rate-1
generator make 3 of every 4 early "+25%" purchases inert — as real but un-criterioned.
A tier-2 generator with a higher base_rate is the natural fix; whether the sweep's
winning cell actually delivers non-inert early purchases is measurable.

So the head: sweep candidate generator-cost parameter sets against the REAL engine
at a fresh pin (the VERDICT 006 method — byte-copy `idle_engine/`, drive it
deterministically, stdlib-only, integer-exact) and hand the lane ONE sim-pinned
(tier-2 cost, tier-2 base_rate, per-count growth) row to re-register in
economy-v1.md BEFORE the generator-cost slice lands. The lane keeps its integrity
floor (no tuning without registration); the mechanic arrives with its pacing
evidence already attached — the doc's own promise, honored parameters-first.

**The sim (a parameter sweep on the real engine, all fixtures committed):**
reference world extended to two generator specs (tier1 `base_rate=1` as shipped;
tier2 `base_rate=R2`), neutral theme pct (theme-independent by construction, the
PROPOSAL 006 clause). Grid: tier-2 base cost **C2 ∈ {300, 600, 900, 1800}**
seconds-of-tier-1-output (the `UPGRADE_BASE_COST_SECONDS` unit convention) ×
tier-2 base_rate **R2 ∈ {5, 10, 25}** × per-count cost growth **g ∈ {110/100,
115/100, 120/100}** (the idle-genre count-curve band; exact rationals like the
upgrade curve) — 36 cells. Policies: SIM-001's S2 (check-in N ∈ {0.25, 2, 8, 24} h)
and S3 (optimal) extended with a committed greedy buy rule choosing the highest
marginal production per unit cost among {upgrade level, tier-1 copy, tier-2
unlock/copy}. Scored per cell: **T10** (time-to-first-tier-2 purchase, active
play, band 15–45 min); **A1–A10 regression** (SIM-001's criteria re-scored with
the purchase path present — the mechanic must not break the approved pacing);
**early-inert fraction** (share of first-15-min purchases with zero marginal rate
delta, vs VERDICT 006's measured 3-in-4 baseline); **owned-rung arrival** (which
of 10/100/1,000 total generators are reached, per profile — the achievements doc's
own deferred question). Baseline leg run first: the HEAD engine with NO purchase
path, re-scored on A1–A10 — since milestones and the theme fold landed after the
verdicted pin, the baseline surfaces any drift honestly before the grid runs on
top of it.

## Relations (adjacent heads — deliberately links, not duplication)

- [`idle-economy-sim-kernel-2026-07-11.md`](idle-economy-sim-kernel-2026-07-11.md)
  (**PROPOSAL 006 → sim-lab VERDICT 006**) — the parent, and the sharpest dedup
  line: SIM-001's own text EXCLUDES this ("T10 is out of SIM-001's scope (mechanic
  not yet implemented) and carries no criterion"), and VERDICT 006's limits repeat
  it ("Nothing about T10 … no purchase path exists"). This head consumes the two
  gaps that verdict disclosed and could not rule on: the T10 mechanic and the
  `base_rate=1` inert-purchase floor. Same lane, same engine, disjoint question.
- `.sessions/2026-07-11-superbot-idle-first-batch.md` (drop record) — this exact
  head was considered and deliberately dropped THEN: "generator purchase path (T10)
  — new engine surface the lane deliberately HOLDS … natural sequencing is after
  the SIM-001 verdict anyway." The verdict landed (sim-lab VERDICT 006, approve);
  the recorded arming condition fired; promoting it now is the drop record's own
  plan executing, not a duplicate.
- [`theme-catalog-gallery-read-contract-2026-07-11.md`](theme-catalog-gallery-read-contract-2026-07-11.md)
  / [`theme-schema-plugin-contract-promotion-2026-07-11.md`](theme-schema-plugin-contract-promotion-2026-07-11.md)
  — the lane's other two heads; both are contract/render surfaces (gallery read
  contract, plugin-schema promotion), zero economy numbers, disjoint.
- vs the outbox (001–014): 006 is the nearest neighbor (above). 003/004/008 are
  parameter sweeps for superbot's game economies — different repo, different
  engine, different targets; 013/014 are fleet-process spec sweeps. No proposal
  touches generator purchase, T10, or the superbot-idle engine post-verdict.
- vs `../superbot/idle-game-offline-summary-2026-07-10.md` and superbot's idle
  game — historical(built) at a DIFFERENT repo (superbot's legacy idle cog);
  this head is the standalone idle ENGINE lane. Name-adjacent, disjoint code.
- VERDICT 006's growth-ratio guardrail (growth 1.15 is a near-floor; retunes below
  ~1.04 re-open SIM-001) — inherited as a constraint, not re-litigated: the sweep
  varies the NEW generator-curve knobs only; the seven graduated parameters stay
  pinned.

## Probe report (v0, 2026-07-12)

> Single-pass battery (panel not escalated: content-lane parameter head, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe
> battery). Verify-first ran FIRST, live this slice: (a) **premise at HEAD** —
> superbot-idle `c753bc8` (ls-remote 22:58Z, blobless clone): no generator purchase
> path in `idle_engine/` (tree-grep: `purchase_upgrade`/`purchase_upgrades` only),
> current-state prose concurs; T10 row + post-hoc clause verbatim in
> `docs/design/economy-v1.md` at both `f11c71a` and HEAD. (b) **arming event** —
> sim-lab VERDICT 006 finalized (sims/verdict-006-idle-economy-sim-kernel/REPORT.md
> + outbox entry: approve, 10/10, "hold lifts on this verdict"); the lane's
> current-state still shows roadmap item 3 "BLOCKED (SIM-001)" — a dated snapshot
> predating the verdict relay, which strengthens the case for routing this via the
> manager with the verdict attached. (c) **kill test NOT triggered** — no generator
> cost curve registered anywhere in the lane's docs/design/ (grep at HEAD: the only
> generator-cost mentions are the achievements doc DEFERRING to "the future
> generator cost curves"), no sibling proposal names T10, and the 2026-07-11 batch
> card records the head as dropped-for-sequencing, not rejected.

**1. What is this really?** The lane's next product mechanic — buying generators,
the core loop verb of the idle genre — arriving the way this lane ships economy
surface: parameters registered with evidence BEFORE code. The target (T10) has
existed since PR #12; the achievements slice priced generator-count milestones in
advance; only the cost curve is missing. The sim turns "invent the curve at build
time" into "re-register the sim-pinned row and build."

**2. What is the possibility space?** (i) Build the mechanic and eyeball the curve
— violates the lane's own integrity floor (every number registered with rationale
before tuning). (ii) Register a guessed curve and sim it after — SIM-001's order of
operations, legal, but it burns a build-verdict round trip if the guess misses T10,
and the lane is HOLDING new engine surface anyway, so nothing is lost by evidencing
first. (iii) Sweep first, register the winning row, build once — this head; the
mechanic lands with T10 gaining its criterion on day one. (iv) Never build the
purchase path — leaves T10 permanently criterion-less, the `owned` milestone track
permanently capped at rung 0, and the engine's `count` factor dead weight; the
achievements doc's own asks stay unanswerable.

**3. What is the most advanced capability reachable by the simplest
implementation?** One committed stdlib driver (the VERDICT 006 kernel extended
with a buy rule and a second GeneratorSpec) prices an entire product mechanic
before it exists: 36 cells × three player profiles, deterministic and
integer-exact, expected <10 s total on the VERDICT 006 evidence (its full grid ran
<1 s). The winning cell is directly the lane's registration row PLUS the T10
criterion text PLUS first evidence on three pre-registered achievements questions
— four registered asks answered by one sweep on one fixture.

**4. What breaks it? (assumptions made explicit)** (a) **The buy policy is a
model** — real players are not marginal-rate-greedy; SIM-001 carried the same
abstraction to an approve, but T10 is a first-session number and more
policy-sensitive; the verdict must report T10 under BOTH S3-optimal and S2
check-in policies, and the band edges (15/45 min), not just the 30-min center.
(b) **Engine drift since the verdicted pin** — milestones + theme fold changed the
production formula; the baseline leg (no purchase path, A1–A10 re-scored at the
new pin) isolates drift from mechanic effect; if the baseline itself breaks an
A-band, that is a first-class finding routed to the lane, not silently absorbed.
(c) **Run-scoped `owned`** — the engine wipes generator counts at prestige reset
(documented GameState semantics), so generator spend competes with upgrade spend
inside every run and re-buys after every reset; if no cell hits T10 without
breaking T9's reset cadence, the honest ruling may be that the MECHANIC SHAPE
(run-scoped counts), not the curve, is wrong — a design question the verdict
names and routes to the lane rather than tunes around. (d) **Grid coverage** — 36
cells is a design sweep, not a proof of global optimum; the verdict states the
grid and marks band-edge cells so the lane knows where the cliff walls are.

**5. What does it unlock?** The lane's next build slice with its evidence
pre-attached (registration row + criterion, zero invented numbers); the `owned`
milestone track becomes reachable (rung 1 as the designed first-session target);
first measured relief on the `base_rate=1` inert-purchase floor VERDICT 006
flagged; and the pipeline's first PRODUCT-MECHANIC-BEFORE-CODE verdict — 001/008
tuned mechanics that existed as designs, 006 verdicted parameters already coded;
this pins parameters for a mechanic before its first line lands, the strongest
form of the pre-registration discipline.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing unshipped:
the engine is public-raw readable and already byte-copied once in sim-lab (the
VERDICT 006 method repeats at the new pin); the reference world, grid JSON, and
buy-policy definition are constructible fixture data committed with the sim; the
runtime is stdlib-only, deterministic, no network after fixture capture. Kill
tests, run live: a registered generator curve (NOT found), a purchase path at HEAD
(NOT found), a sibling proposal or intake naming T10 (NOT found). Sim-worthy or
judgment-only: sim-worthy — falsifiable bands, real engine, measurable regression
scorecard; the one judgment question (is run-scoped rebuy fun?) is explicitly
carved out to the lane in Q4(c).

**7. Which lane should build it — and what does it displace or duplicate?**
sim-lab runs the sweep (its own VERDICT 006 fixture method, its harness, its
verdict grammar); `menno420/superbot-idle` builds the mechanic after
re-registering the winning row (Q-0260: the lane writes its own engine and design
docs; this repo writes neither — the verdict routes via the manager as evidence).
Duplicates nothing: swept by name this slice (rg over ideas/ + .sessions/ +
control/ for generator/purchase/T10/tier, bootstrap.py and .substrate excluded;
sim-lab outbox/inbox/docs for the same) — every hit is either the parent proposal
excluding T10, the achievements doc deferring to this, or the drop record
sequencing it here.

**8. What is the smallest shippable slice?** One sim-lab intake dir: `idle_engine/`
byte-copied at `c753bc8`, one stdlib driver (VERDICT 006's kernel + two-spec
reference world + committed greedy buy rule), one committed grid JSON (36 cells),
the baseline leg, and one results table {cell → T10 per policy, A1–A10 scorecard,
early-inert fraction, owned-rung arrivals} ending in ONE recommended registration
row — reproducible from the fixtures alone, byte-identical on re-run, no flags.

**Recommendation: sim-ready** — the target is pre-registered and falsifiable, the
engine is real and pinned, the arming event (VERDICT 006) has fired, the lane's own
docs defer three registered questions to exactly this sweep, and the verdict
changes what the lane builds next (a registered evidence-backed curve vs a guessed
one — or a mechanic-shape rethink if no cell survives). THE ONE QUESTION for the
simulator: *Driving the real `idle_engine/` byte-copied at superbot-idle `c753bc8`
(reference world extended to two generator specs, neutral theme pct, the seven
VERDICT 006-graduated parameters held pinned), which (tier-2 base cost C2 ∈ {300,
600, 900, 1800} seconds-of-tier-1-output × tier-2 base_rate R2 ∈ {5, 10, 25} ×
per-count cost growth g ∈ {110/100, 115/100, 120/100}) cells hit the
pre-registered T10 band (time-to-second-generator-tier 15–45 min active, target
30) under the SIM-001 S2/S3 policies extended with a committed greedy buy rule —
while keeping all ten SIM-001 criteria A1–A10 in PASS state with the purchase path
present (baseline leg first: A1–A10 re-scored at the new pin with NO purchase
path, isolating milestone/theme drift), measurably lowering VERDICT 006's flagged
3-in-4 early-inert-purchase floor, and reporting `owned` milestone rung arrivals
(10/100/1,000) per player profile?* Done-when: the per-cell {T10 per policy,
A1–A10 scorecard, early-inert fraction, owned-rung arrivals} table plus the
baseline leg, ending in ONE recommended (C2, R2, g) registration row with proposed
T10 criterion text for the lane to re-register in economy-v1.md (new doc version,
per its own verdict semantics) BEFORE the generator-cost slice lands — OR an
explicit finding that no cell hits T10's band without breaking a named A-criterion
(the binding criterion stated, band-edge cells marked), meaning the lane
re-registers T10 or reshapes the mechanic (e.g. the run-scoped-counts question,
Q4(c)) before any engine surface lands; the verdict must restate that the seven
graduated parameters and the 1.15 growth-ratio guardrail were held fixed and are
not re-opened by this sweep.
