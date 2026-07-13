# Entry-fee ticket envelope — price the structure lever VERDICT 022 routed after rejecting odds

> **State:** sim-ready
> **Class:** product · **Target:** `menno420/superbot` (the hub's minigame/casino
> consolidation — the World seat's own night-run work; verification target
> `menno420/sim-lab` per the Q-0264 pipeline)
> **Sequence:** after VERDICT 022 (casino fairness envelope, reject — "odds cannot
> do the job", finalized this night) and before the World seat picks among the
> three non-odds levers that verdict routed with the quantified gap — the verdict's
> own "Named follow-ups" list calls this head out verbatim: "an entry-fee/prize-table
> envelope sim (the SAFE-band successor question)"

**Origin:** drafted this slice under standing owner ORDER 003 (continuous
pipeline) + ORDER 004 rule 3's rotation — the GAME-MECHANICS slot, round 2
(round 1: PROPOSAL 020 → VERDICT 022; round 2 so far: 021 fleet-backlogs, 022
venture-trading). The head is the direct child of its round-1 parent: VERDICT 022
(sim-lab local clone @ `fda94d0`, `sims/verdict-022-casino-fairness/REPORT.md`)
REJECTED the odds lever — E\*(g, m) = ∅ in all 36 cells, SAFE failing 36/36
because "wipe risk within 100 bets is variance, not edge" and SINK unreachable by
odds on high-variance shapes (worst-policy P_double 0.195–0.323 at EVERY edge and
cap) — and routed exactly three non-odds levers to the World seat: rake-only PvP
(already priced free by the verdict's rake ≡ edge identity), session
comp/stipend, and **entry-fee-with-prize** — "both turn the SAFE failure from a
bankroll event into a bounded fee, the one thing no in-grid cell could do"
(REPORT.md, recommendation block). That sentence is a structural HYPOTHESIS the
verdict states but could not test: its grid had no fee axis. Nobody has run the
successor numbers; they are entirely computable, entirely in-tree (zero network
reads — the parent verdict's committed report + fixtures are in the sim-lab
clone, and the consumer window is inbox ORDER 004's own text, "World's balance
pins").

## The idea (reasoned to its fuller form — Q-0254 duty)

VERDICT 022 proved WHERE the odds lever dies: SAFE and SINK are
variance-dominated, and the variance is player-controlled — stake sizing (flat
5% stakes, fixed fractions, capped martingale) is what turns a 100-bet session
into a bankroll event. The entry-fee-with-prize structure attacks exactly that
axis: the house sells play only as a **fixed-price ticket** (price F, a table
constant) resolving against a pinned prize schedule. A player cannot escalate a
stake — the only freedom left is HOW MANY tickets to buy per round, and b
simultaneous tickets resolve as b INDEPENDENT draws, so per-round volatility
grows like √b, not b (a single escalated stake grows like b). The open question
is whether that structural taming is ENOUGH: a greedy re-buyer at a high take
rate still compounds toward ruin ((1−t)^rounds), a chase policy can still double
ticket COUNT after losing rounds (a weaker martingale — recovery is no longer
guaranteed by one win), and the FUN band still pulls against the take rate
exactly as it pulled against the edge. So the successor question has the same
three-way envelope shape as the parent, with the house levers transposed:
(house-edge e × max-bet m) becomes (take rate t × per-round ticket cap c), and
the swept player policies become re-buy policies instead of stake policies.

Three properties, same pre-registered bands as VERDICT 022 (deliberately — the
chained comparison is cell-addressable only if the bands match):

- **FUN** — P(a 100-round single-ticket session ends ahead) ≥ 0.25.
- **SAFE** — max over swept re-buy policies of P(losing ≥ 90% of the session
  bankroll within 100 rounds) ≤ 0.05.
- **SINK** — max over swept re-buy policies of P(a grinder doubles the bankroll
  before halving it) ≤ 0.10.

Every outcome is decision-grade for the World seat: APPROVE hands the
consolidation ONE house frame (ticket price + per-round cap + take band) that
every house-banked game adopts by declaring a prize table; REJECT strikes the
second of the three routed levers with measured numbers, leaving comp/stipend
design and rake-only PvP as the only survivors — the World seat stops spending
design effort on fee/prize shapes that cannot work; NULL ships the per-shape
envelope table as the pin.

**The sim (fully hermetic — the PROPOSAL 017–022 precedent; every fixture is a
pinned constant committed with the sim, zero repo/network reads in the verdict
session):** integer-chip bankroll walks, B₀ = 1,000 chips. Ticket price pinned
at **F = 0.01·B₀ = 10 chips** (the parent's SAFE rider — "pin MAXBET ≤ 0.05·B₀"
— motivates a small fixed quantum; the fee-size axis is absorbed by the
per-round cap below, keeping 36 decision cells like the parent). A prize
schedule pays multiples of F with probabilities scaled by (1−t) so E[prize] =
(1−t)·F exactly — take rate t is the per-ticket analog of the parent's edge e:
**T1 double-up** (prize 2F w.p. (1−t)/2 — the even-money shape; its FUN leg is
the IDENTICAL binomial to VERDICT 022's G1 reference leg, a pre-registered
cross-verdict identity check), **T2 tiered** (prizes {8F, 3F, 1F} w.p.
(1−t)·{0.05, 0.10, 0.30} — mid-variance, per-ticket variance 3.4·F² at t=0),
**T3 jackpot** (prizes {25F, 5F} w.p. (1−t)·{0.024, 0.08} — per-ticket variance
16·F² at t=0; the three schedules bracket the payout-shape axis as the parent's
k ∈ {1, 5, 19} did). Take grid **t ∈ {0.01, 0.02, 0.05, 0.10}** + t=0 control
(reporting-only). House table rule: **per-round ticket cap c ∈ {5, 25, 100}** —
max per-round spend c·F ∈ {5%, 25%, 100%}·B₀, the exact mirror of the parent's
m-grid, so every (shape, take, cap) cell has a named parent cell. Re-buy
policies (4 swept; b always ≤ c and ≤ ⌊bankroll/F⌋; a round's b tickets are b
independent draws; round net = Σ prizes − b·F): **R1** b=1; **R5** b=min(5, ·);
**RG greedy** b=max affordable (the compounding all-in); **MC chase** b =
min(2^L, ·) where L = consecutive net-losing rounds, reset on a net-winning
round (ticket-count martingale — the escalation shape that survives the fee
frame). Profiles (mirror the parent): **CASUAL** — 100 rounds or bankroll < F;
P_ahead = P(final > B₀), P_wipe = P(final ≤ 0.1·B₀). **GRINDER** — to ≥ 2·B₀ or
≤ 0.5·B₀, hard cap 4,000 rounds; P_double; cap-hits counted separately, > 1% in
a decision cell marks it indeterminate (a NULL path, never silently absorbed —
expected on T1×R1 low-take cells, the parent's F-0.01 precedent; measured
P_double stays a LOWER bound so SINK failures stand regardless). **COMPULSIVE**
(reporting-only, R1) — to bankroll < F or 20,000 rounds; median rounds-to-ruin.
Cells: 3 shapes × 4 takes × 3 caps = **36 decision cells**. **Arm A (analytic,
seedless, exact rationals):** FUN for ALL 36 cells — T1 via `math.comb` binomial
tails (must REPRODUCE VERDICT 022's committed G1 reference values, e.g. 0.2738
at 0.05 — same binomial, the cross-verdict identity), T2/T3 via exact
integer-support DP convolution (100 steps, support ≤ 2,500 units of F,
`fractions.Fraction`); GRINDER on T1×R1 via two-boundary gambler's-ruin closed
forms (unit steps of F: span 150, start 50 above the lower boundary); CASUAL
P_wipe on T1×R1 via exact bounded-support DP (the parent had NO analytic wipe
leg — this arm covers one); the t=0 control must give T1×R1 P_double = 1/3
exactly (optional stopping — the parent's identical control). **Arm S (seeded
MC):** `random.Random(20260730)`, pinned loop order (shape, then t ascending,
then c ascending, then policy R1/R5/RG/MC, then profile casual → grinder →
compulsive; replications sequential; one `rng.random()` per ticket); M = 5,000
casual / 2,000 grinder / 500 compulsive per cell-policy. Arm S must agree with
Arm A within 1.0 percentage point absolute on every Arm-A-covered cell or the
run is invalid. A half-M decision-stability leg, seed 20260731, must reproduce
the same ruling. A per-round AGGREGATED draw (per-prize-level counts from the
same rng stream) is permitted iff it reproduces the per-ticket-draw results on a
pre-registered spot check (1,000 rounds, seed 20260732) — the PROPOSAL 017
breakpoint-clause precedent. Aux self-check stream seed 20260733 (never read by
any decision number). Feasibility arithmetic: the heavy legs are RG at c=100
(casual ≈ 5,000 × 100 × ≤100 ticket draws per cell) — ≈ 400–900M per-ticket
draws total WITHOUT the aggregation clause, ≈ 10–20M aggregated rounds with it;
integer RNG-compare-add either way, tens of minutes cold CPython, no
dependencies; results table pins the CPython minor version; byte-identical on
re-run.

**Pre-registered acceptance bands and decision rule** (set BEFORE any code runs;
evaluated in this order):

- Per (shape g, cap c): **E\*(g, c)** = the set of take rates t in the grid
  where FUN (R1 reference leg, analytic) ∧ SAFE (max P_wipe over the 4 swept
  policies ≤ 0.05) ∧ SINK (max P_double over the 4 swept policies ≤ 0.10) all
  hold, determinate cells only.
- **REJECT** ("the fee frame cannot do it either") iff in ≥ 2 of the 3 shapes,
  E\*(g, c) = ∅ for EVERY cap c, in both arms where covered — the second routed
  lever falls to the same variance arithmetic as the first; the verdict
  quantifies the residual gap per shape (the failing band's value at that
  shape's best cell) and the World seat's remaining levers are comp/stipend and
  rake-only PvP alone.
- **APPROVE** ("the ticket frame is the one house rule") iff ∃ a cap c\* such
  that ∩_g E\*(g, c\*) contains ≥ 2 CONSECUTIVE take-rate grid points (a band,
  not a knife-edge) and the stability leg reproduces it → recommended row:
  ticket price 0.01·B₀ + per-round cap c\* + the shared take band; any game
  added later declares its prize schedule and a one-line check computes its
  take against the band.
- **NULL** otherwise — a legitimate reportable outcome: the per-shape (c, t)
  envelope table IS the pin, with the flip axis named via per-axis envelope
  shares (expected candidates: the cap c — RG's compounding at c=100 recreating
  exactly the wipe the parent measured, while c=5 tames it — or the prize shape
  via T3's tail). Indeterminate cells route to NULL, never to APPROVE.

**Chained anchors (reporting-only, cannot flip the decision):** (i) the parent's
near-miss — VERDICT 022's (G1, e=0.05, m=0.05) passed FUN 0.2738 and SINK 0.0895
and died ONLY on SAFE at 0.1358 (2.7× the band); the transposed cell here is
T1 (t=0.05, c=5), and whether its worst-policy P_wipe crosses under 0.05 is the
single most legible measurement of what the structure lever buys. (ii) the
parent's SINK wall — T2/T3 P_double vs the measured 0.195–0.323 range at every
edge and cap. (iii) the t=0 control and the T1-FUN ≡ G1-FUN identity. (iv) the
expected-loss price tag, E[casual session net loss]/B₀ per cell (the "expected
loss bounded" claim, measured not asserted).

**Consequence:** on APPROVE — the consolidation adopts the ticket frame as the
house rule for every house-banked minigame (fee quantum + per-round cap + take
band), and the per-game balance question permanently reduces to "declare your
prize table, pass the one-line take check". On REJECT — the World seat strikes
the entry-fee lever from VERDICT 022's routed list with the quantified residual
gap; comp/stipend and rake-only PvP are the only levers left standing, and
tonight's consolidation does not spend design effort on fee/prize shapes. On
NULL — the per-shape envelope table ships as the pin (e.g. tiered/jackpot
schedules hold a band at tight caps while double-up does not, inheriting the
parent's PvP/rake routing for even-money shapes). Boundary, stated: all
conclusions are bankroll-RELATIVE (chips normalized to B₀) — nothing here prices
the casino sink against fishing/mining faucet mint in absolute chips/hr; the
live earn-rate baseline whose absence V001/V008 named (and VERDICT 022 restated)
stays walled, the telemetry caveat applies verbatim. Tickets are i.i.d. — no
skill edge; a game's strategy spread folds into the take grid as the REALIZED
take. FUN's proxy (P_ahead ≥ 0.25) is the parent's pre-registered, disputable
band, held fixed here BY DESIGN so the two verdicts compare cell-for-cell; the
full curves ship so a re-drawn line re-reads, never re-runs. Comp/stipend design
is NOT simulated here (it remains a routed lever — the natural third head if
this one rejects).

## Relations (adjacent heads — deliberately links, not duplication)

- vs the outbox (PROPOSALs 001–022, re-read at HEAD `1c6313c`): nearest by every
  axis is **PROPOSAL 020 → VERDICT 022** (offset per sim-lab's own
  `finalizes-as` lines, never derived): same consumer (the minigame/casino
  consolidation), same three bands (deliberately, for chained comparability) —
  but a DIFFERENT house lever and a different model family. The parent swept
  (edge × max-bet) over player-chosen STAKES and answered its question: REJECT,
  settled, not re-asked here. This head sweeps the (take × ticket-cap) frame
  its own REJECT consequence routed and its "Named follow-ups" list requested
  verbatim ("an entry-fee/prize-table envelope sim — the SAFE-band successor
  question"). No code path, fixture, or measured number is shared; the parent's
  numbers appear only as pinned comparison anchors, quoted from its committed
  REPORT.md. PROPOSAL 009 (settle-once) touches the same wager seams
  (`enter_tournament`/`payout_tournament` — proof the entry-fee PLUMBING
  exists) but asks correctness, never balance. PROPOSALs 015/016 → VERDICTs
  017/018 are the other game-mechanics verdicts — pacing curves, zero wager
  surface, settled and untouched. PROPOSALs 017–019/021/022 are method
  precedent only (hermetic dual-arm pre-registration; zero shared domain).
- vs superbot's harvested backlog (237 docs, this section's README):
  `wager-flow-map` maps where money moves (parked(routed)) — never what a
  ticket should cost; `giveaway-competitive-teardown` is FREE-entry giveaway
  research, not paid-ticket balance; `games-economy-faucet-sink-diagnostic` is
  observational and historical. Grep of the index for
  entry-fee/ticket/prize/lottery/raffle: nothing else.
- vs sim-lab (local clone @ `fda94d0`, verdicts through V023 finalized + V024 in
  flight for PROPOSAL 022): no verdict besides V022 touches wager balance, and
  V022's grid contains no fee, ticket, prize-schedule, or re-buy axis — its
  README's own follow-up line is this head's request. The V024-in-flight head is
  trading-lane selection inference, unrelated.
- Tree-wide dedup sweep (`rg -g '!bootstrap.py' -g '!.substrate'` for
  entry.fee / ticket / prize / lottery / raffle / re-buy over ideas/ +
  .sessions/ + control/ + docs/): hits are the parent head's own lever list
  (PROPOSAL 020 text + VERDICT 022 report), the P009/wager-flow-map tournament
  ops, venture-lab pricing prose (books, unrelated), and the giveaway teardown
  — no prior ticket-structure balance question anywhere.

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained probability-model
> head, sim is report-only evidence, no spend/publish/irreversible surface —
> README § probe battery). Verify-first ran FIRST, live this slice, zero network
> reads: (a) **grounding** — the parent verdict is committed evidence in the
> local sim-lab clone (`sims/verdict-022-casino-fairness/REPORT.md` @ `fda94d0`:
> ruling `reject`, the three routed levers, the near-miss row 0.2738/0.0895/
> 0.1358, the SINK wall 0.195–0.323, the "bounded fee" hypothesis sentence, and
> the follow-ups line naming this sim); the consumer window is inbox ORDER 004's
> own verbatim text ("World's balance pins"). (b) **dedup** — the sweeps above.
> (c) **feasibility arithmetic** — in the sim-spec preamble; the one heavy leg
> (RG at c=100) carries the pre-registered aggregation clause with a seeded
> spot-check gate.

**1. What is this really?** A pre-registered successor-envelope sweep for the
entry-fee-with-prize structure VERDICT 022 routed: does any (take-rate band ×
per-round ticket cap) cell keep casual ticket sessions fun (P_ahead ≥ 0.25),
bankrolls safe under re-buy policies including greedy compounding and
ticket-count chase (P_wipe ≤ 0.05), and the casino sink-proof under a grinder's
best policy (P_double ≤ 0.10) — across three prize-schedule shapes, with a dual
analytic arm (exact binomial + DP tails, ruin closed forms, a cross-verdict FUN
identity against the parent's committed values) pinning the seeded MC.

**2. What is the possibility space?** (i) Don't run it — the World seat picks
among the three routed levers by feel, and the one structural hypothesis the
parent stated ("turns the SAFE failure into a bounded fee") stays untested while
a consolidation ships against it. (ii) Trust the hypothesis without numbers —
but the parent's own arithmetic warns that re-buy compounding may recreate the
wipe it was routed to fix; a lever adopted on an untested sentence is the same
invented constant the parent existed to kill. (iii) Ask the owner — zero
evidence attached, strictly worse after a verdict prices the lever (Q-0263.2).
(iv) This head: 36 transposed cells, parent-matched bands, REJECT and NULL both
decision-grade. (v) Over-scope (comp/stipend design, mixed fee+odds hybrids,
prize pools funded by player entry across players — pari-mutuel) — natural
follow-ups; the single-player house-banked ticket is the shape the routed lever
names.

**3. What is the most advanced capability reachable by the simplest
implementation?** One ~300-line stdlib file: a ticket-round kernel (b draws →
net → bankroll) reused by all profiles, exact `math.comb`/`Fraction` DP tails
and ruin closed forms as the second arm, and a 36-cell table that upgrades a
routed design lever from hypothesis to measured contract row — plus the first
cell-addressable comparison between two chained verdicts (every cell here names
its parent cell).

**4. What breaks it? (assumptions made explicit)** (a) **Tickets are i.i.d.**
— no skill, no strategy-dependent take; realized take folds into the t-grid.
(b) **Three prize schedules, not every game** — {2F}, {8F,3F,1F}, {25F,5F}
bracket the shape axis; a real mixed table lands between brackets,
interpolation on the consumer. (c) **The re-buy policy set is finite** — R1/R5/
RG/MC bracket unit, bounded, greedy-compounding, and loss-chasing behavior; a
policy outside the set (e.g. fractional-Kelly ticket counts) is bounded between
R1 and RG by construction of the cap, stated not proven. (d) **Boundary
effects** — integer chips, F-quantized buys, absorbing boundaries pinned in the
loop order; the t=0 optional-stopping control, the T1-FUN ≡ G1-FUN identity,
and the 1.0 pp agreement gate catch kernel bugs before any cell is believed.
(e) **PRNG stability** — `random.Random(20260730)` pinned, loop order pinned,
CPython minor pinned; seeds 20260730–33 fresh against the registry 20260713–29
(swept across PROPOSALs 017–022 this slice, the P020-flagged 20260723 collision
included).

**5. What does it unlock?** The World seat's lever choice stops being taste:
either the consolidation inherits a complete house frame (APPROVE), or a
measured strike-out narrows three routed levers to two (REJECT), or the
per-shape table pins which prize shapes are house-bankable at all (NULL). Plus
the program's first chained verdict pair — parent and successor sharing bands
and cell addresses — a shape any future "lever A failed, try lever B" question
can reuse.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing external
at sim time — every fixture ({B₀, F, prize schedules, t-grid, c-grid, policy
constants, profile stop rules, M per profile, seeds, band constants}) is stated
in this file and committed as JSON alongside the sim. Kill tests, run live this
slice: a prior ticket/prize balance head anywhere in the tree (NOT found —
sweeps above), a sim-lab verdict already covering the fee lever (NOT found —
V022's grid has no fee axis and its follow-ups line REQUESTS this sim), the
consolidation having already picked a lever (NOT found — V022 finalized this
same night; the levers rode to the World seat unpriced), infeasible runtime
(NOT found — arithmetic above with the aggregation clause). Sim-worthy or
judgment-only: sim-worthy — bounded-walk tail arithmetic against pre-registered
thresholds; the judgment question (are the bands right?) was settled by the
parent's pre-registration and is inherited unchanged, which is itself the
comparability contract.

**7. Which lane should build it — and what does it displace or duplicate?**
sim-lab runs it (its harness, its verdict grammar; sim + fixture JSON committed
in its sims/ tree, the verdict-022 dir as the sibling precedent). The verdict's
consumer is the superbot World seat's minigame/casino consolidation, with
superbot-games inheriting the row if house-banked games land plugin-side (the
V018 shared-surface precedent). Duplicates nothing: V022 killed the odds lever;
this prices the structure lever its REJECT routed — successor, not re-run.

**8. What is the smallest shippable slice?** One sim-lab intake dir: one stdlib
file (ticket-round kernel + analytic arm + 36-cell grid), one fixture JSON (all
constants copied verbatim from this file), one results table {P_ahead, P_wipe,
P_double, cap-hit fraction, expected session loss, median rounds-to-ruin} ×
(shape, t, c, policy) plus the E\* envelope summary and the four chained
anchors — ending in exactly one of APPROVE/REJECT/NULL per the pre-registered
rule, reproducible from the fixtures alone, byte-identical on re-run, no flags.

**Recommendation: sim-ready** — the question is crisp and computable, the bands
and decision rule (with stated evaluation order) are registered above BEFORE any
code exists, the parent verdict itself requested the head, and every outcome
hands the World seat a lever decision it currently lacks. THE ONE QUESTION for
the simulator: *Under the pinned ticket-frame model (B₀ = 1,000 integer chips;
ticket price F = 0.01·B₀ = 10; prize schedules T1 double-up {2F w.p. (1−t)/2},
T2 tiered {8F, 3F, 1F w.p. (1−t)·{0.05, 0.10, 0.30}}, T3 jackpot {25F, 5F w.p.
(1−t)·{0.024, 0.08}} — E[prize] = (1−t)·F exactly; take grid t ∈ {0.01, 0.02,
0.05, 0.10} + t=0 control; per-round ticket caps c ∈ {5, 25, 100} tickets;
re-buy policies R1/R5/RG-greedy/MC-chase with b ≤ c and b ≤ ⌊bankroll/F⌋, b
tickets resolving as b independent draws; profiles CASUAL 100-round session,
GRINDER double-or-half capped at 4,000 rounds with > 1% cap-hits marking the
cell indeterminate, COMPULSIVE reporting-only; Arm A exact FUN tails for all 36
cells — T1 binomial required to reproduce VERDICT 022's committed G1 reference
values — plus T1×R1 ruin closed forms, an exact T1×R1 wipe DP, and the t=0
P_double = 1/3 control; Arm S seeded MC `random.Random(20260730)` M =
5,000/2,000/500 with the 1.0 pp agreement gate, half-M stability leg seed
20260731, aggregation spot-check seed 20260732, aux stream seed 20260733), for
which (t, c) cells do FUN (R1 reference P_ahead ≥ 0.25), SAFE (max-policy
P_wipe ≤ 0.05), and SINK (max-policy P_double ≤ 0.10) hold simultaneously per
prize shape — E\*(g, c) — and does the result land REJECT (E\* empty at every
cap in ≥ 2 of 3 shapes → the fee frame falls to the same variance arithmetic as
the odds lever; the World seat's remaining levers are comp/stipend and
rake-only PvP, with the residual gap quantified per shape), APPROVE (some cap
c\* gives ≥ 2 consecutive shared take-rate points across all three shapes → one
house frame: ticket price 0.01·B₀ + per-round cap c\* + shared take band, each
game declaring its prize table for a one-line take check), or NULL (anything
else → the per-shape envelope table is the pin, flip axis named via per-axis
envelope shares — expected candidates: the cap c, with RG compounding at c=100
recreating the parent's measured wipe, or the T3 jackpot tail)?* Done-when: the
committed sim + fixture JSON reproduce the full results table, envelope summary,
and the four chained anchors (the parent's near-miss cell T1 (t=0.05, c=5) vs
its measured 0.2738/0.0895/0.1358 row; the T2/T3 SINK wall vs 0.195–0.323; the
t=0 control; the expected-loss price tag) byte-identically, Arm S passes the
Arm-A agreement gate, the T1-FUN ≡ G1-FUN cross-verdict identity, and the t=0
control, the stability leg reproduces the same ruling, and the verdict issues
exactly one of APPROVE/REJECT/NULL per the pre-registered rule (evaluation
order stated) with the bankroll-relative boundary and the V001/V008
earn-rate-baseline caveat restated verbatim, and the reporting-only legs
(compulsive harm context, t=0 control, chained anchors, expected-loss table)
stated as legs that cannot flip the decision.
