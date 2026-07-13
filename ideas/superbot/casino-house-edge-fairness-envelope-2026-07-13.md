# Casino fairness envelope — sim-pin the house-edge × max-bet contract before the consolidation invents odds

> **State:** sim-ready
> **Class:** product · **Target:** `menno420/superbot` (the hub's minigame/casino
> consolidation — the World seat's own night-run work; verification target
> `menno420/sim-lab` per the Q-0264 pipeline)
> **Sequence:** before the minigame/casino consolidation pins per-game odds — inbox
> ORDER 004 names "World's balance pins" as arriving tonight (SIM-REQUESTs-first,
> same-wake turnaround), and every consolidated house-banked game needs a (win
> probability, payout) pair the moment it lands; whichever session writes those
> numbers first fixes them by accident, the exact pre-empt pattern PROPOSALs 015/016
> ran for the T10 curve and the encounter cooldown namespace

**Origin:** drafted this slice under standing owner ORDER 003 (continuous pipeline)
+ ORDER 004's seat-cycle item 1 ("SIM-REQUESTs first — … World's balance pins …
will arrive; same-wake turnaround") and rotation rule 3's game-mechanics slot —
PROPOSAL 019 restarted the rotation at fleet backlogs; this head takes the
game-mechanics slot early, deliberately, because its consumer window (tonight's
consolidation) closes before a strict rotation would reach it. In-repo grounding,
no network reads needed: superbot's wager surface is real and already pinned in
this tree — the six audited `game_wager_workflow` ops (`open_pvp_wager`,
`settle_pvp`, `refund_pvp`, `enter_tournament`, `payout_tournament`,
`recover_escrow`) with fees hidden in `utils/tournaments.deduct_fees`
(`ideas/superbot/wager-flow-map-2026-07-10.md`, seam re-verified alive at superbot
`2c7d2de`), and the six-instance double-settlement corpus on those same games
(blackjack PvP, RPS PvP, deathmatch — PROPOSAL 009's fixture list). What does NOT
exist anywhere in this tree, superbot's 237-doc harvested backlog, or sim-lab's 19
verdicts: any measured answer to "what odds should a house-banked minigame run?"

## The idea (reasoned to its fuller form — Q-0254 duty)

A casino consolidation has exactly three balance levers per game: the house edge
`e` (how much of each wagered chip the house keeps in expectation), the payout
shape `k` (even-money grind vs rare-jackpot), and the table rule (max bet). Every
consolidated game will pick all three, tonight, and the failure modes on both
sides are well known and OPPOSITE: odds too fair and the casino becomes an earn
path that out-mints fishing/mining (the farming failure V001/V008 spent two
verdicts fencing on the encounter surfaces — same class, different faucet); odds
too harsh and sessions are joyless chip-shredders nobody plays (the fun failure no
verdict has priced at all). The design question is whether a SINGLE house rule —
one house-edge band plus one max-bet cap, applied to every game in the hub — can
hold three properties at once, or whether the properties are irreconcilable and
the consolidation needs a different lever entirely. Nobody has run the numbers;
they are entirely computable.

Three properties, stated as a player-facing fairness envelope:

- **FUN** — a casual session must be winnable often enough to be worth sitting
  down: P(a 100-bet casual session ends ahead) ≥ 0.25.
- **SAFE** — no swept betting policy (including capped martingale, the policy
  players actually invent) may let a casual session vaporize a bankroll:
  P(losing ≥ 90% of the session bankroll within 100 bets) ≤ 0.05.
- **SINK** — the casino must never be a viable earn path under ANY swept policy:
  P(a grinder doubles the bankroll before halving it) ≤ 0.10, taken adversarially
  as the max over all swept policies.

FUN and SINK pull against each other through `e`; the payout shape `k` moves how
hard they pull (high-variance jackpot games keep sessions winnable at edges that
make even-money games hopeless); the max-bet cap is the only thing standing
between martingale and both SAFE and SINK. Whether a common (e-band, cap) cell
exists across payout shapes is a genuine open question — back-of-envelope
gambler's-ruin arithmetic says even-money games may have an EMPTY envelope (the
edge that stops grinders starts boring casuals), which would itself be the
verdict: even-money games get PvP/rake treatment, house-banked games get pinned
per-shape. Every outcome is a contract row the consolidation can adopt verbatim.

**The sim (fully hermetic — the PROPOSAL 017/018/019 precedent; every fixture is a
pinned constant committed with the sim, zero repo/network reads in the verdict
session):** integer-chip bankroll walks, B₀ = 1,000 chips, min stake 1 chip. A
game archetype is (payout multiplier k; per-bet win probability p = (1−e)/(k+1),
so EV per unit staked = −e exactly): **G1 even-money** (k=1 — blackjack/coinflip
shape), **G2 mid-variance** (k=5 — die-face bet shape), **G3 jackpot** (k=19 —
slots/wheel shape). House-edge grid **e ∈ {0.01, 0.02, 0.05, 0.10}** (+ an e=0
control leg, reporting-only, for the Arm-A cross-checks). Table rule: max single
stake **MAXBET = m·B₀, m ∈ {0.05, 0.25, 1.0}**, clipping every policy. Betting
policies (5, all stakes clipped to [1, MAXBET] and to the current bankroll):
**F-β fixed-fraction** stake = max(1, ⌊β·bankroll⌋), β ∈ {0.01, 0.05, 0.10};
**C constant** stake = ⌊0.05·B₀⌋ = 50; **M capped martingale** base ⌊0.01·B₀⌋ =
10, double after each loss, reset after each win. FUN's reference leg is a sixth,
analytic-only policy: constant stake 10 (1% of B₀), under which a 100-bet session
cannot ruin mid-path, so P(ahead) is an exact binomial tail. Player profiles:
**CASUAL** — one session = 100 bets or stop when bankroll < 1 chip; metrics
P_ahead = P(final > B₀) and P_wipe = P(final ≤ 0.1·B₀). **GRINDER** — play until
bankroll ≥ 2·B₀ (double) or ≤ 0.5·B₀ (halved), hard cap 4,000 bets; metric
P_double; a cap-hit counts as neither and is reported — any decision cell with
> 1% cap-hits is marked indeterminate (a NULL path, never silently absorbed).
**COMPULSIVE** (reporting-only, C policy only) — play to ruin or 20,000 bets;
median bets-to-ruin, the harm-context number. Cells: 3 archetypes × 4 edges × 3
caps = **36 envelope cells**; within each, the 5 policies × profiles. **Arm A
(analytic, seedless):** exact binomial tails via `math.comb` for every FUN
reference cell (all archetypes × edges: ahead iff wins·(k+1) > 100); exact
two-boundary gambler's-ruin closed forms for GRINDER on G1 × C (unit steps of 50:
start 10 units above the lower boundary, span 30); the e=0 control must give
P_double = 1/3 exactly (optional stopping). **Arm S (seeded MC):**
`random.Random(20260721)`, pinned loop order (archetype, then e ascending, then m
ascending, then policy F/C/M with β ascending, then profile casual → grinder →
compulsive; replications sequential); M = 5,000 casual / 2,000 grinder / 500
compulsive sessions per cell-policy. Arm S must agree with Arm A within 1.0
percentage point absolute on every Arm-A-covered cell or the run is invalid. A
decision-stability leg at half M, seed 20260722, must reproduce the same ruling.
Feasibility arithmetic: ≈ 90M casual bet-steps + ≈ 200M grinder steps + ≈ 40M
compulsive steps of integer RNG-compare-add — tens of minutes cold in pure
CPython, no dependencies; results table pins the CPython minor version;
byte-identical on re-run.

**Pre-registered acceptance bands and decision rule** (set BEFORE any code runs;
evaluated in this order):

- Per (archetype g, cap m): **E\*(g, m)** = the set of edges e in the grid where
  FUN (reference leg) ∧ SAFE (max P_wipe over all 5 swept policies ≤ 0.05) ∧ SINK
  (max P_double over all 5 swept policies ≤ 0.10) all hold.
- **REJECT** ("odds cannot do the job") iff in ≥ 2 of the 3 archetypes,
  E\*(g, m) = ∅ for EVERY cap m, in both arms where covered — the fun/sink
  tension is inherent, and the consolidation must reach for a non-odds lever
  (rake-only PvP framing, session comp/stipend, or entry-fee-with-prize shapes);
  the verdict quantifies the gap (the FUN value at the smallest SINK-passing edge,
  per archetype).
- **APPROVE** ("one shared house rule") iff ∃ a cap m\* such that
  ∩_g E\*(g, m\*) contains ≥ 2 CONSECUTIVE grid edges (a band, not a knife-edge)
  and the stability leg reproduces it → recommended row: shared MAXBET = m\*·B₀ +
  the shared house-edge band, per-archetype tables attached.
- **NULL** otherwise — a legitimate reportable outcome, and here a constructive
  one: the per-archetype envelope table IS the deliverable (per-shape odds rows
  instead of one house rule), with the flip axis named via per-axis envelope
  shares (expected candidate: payout multiplier k — the even-money archetype
  emptying while jackpot shapes hold a band). Indeterminate cells (grinder
  cap-hits > 1%) route to NULL, never to APPROVE.

**Consequence:** on APPROVE — the consolidation adopts the sim-pinned row (one
house-edge band + one max-bet rule for every house-banked minigame in the hub);
any game added later declares its (p, k) and a one-line check computes its edge
against the band (the machine-checkable follow-up the wager-flow-map tracer can
carry). On REJECT — tonight's consolidation does NOT tune per-game odds hoping to
reconcile fun with sink-proofing (the sim proves it can't); the named non-odds
levers go to the World seat with the quantified gap. On NULL — the per-archetype
envelope table ships as the pin: even-money games take the PvP/rake lane (the G1
row prices rake directly — even-money PvP with pot-rake r is G1 at e = r for each
symmetric player, an identity stated analytically, no extra sim), jackpot-shaped
games take their measured band. Boundary, stated: all conclusions are
bankroll-RELATIVE (chips normalized to B₀) — nothing here prices the casino sink
against fishing/mining faucet mint in absolute chips/hr; that needs the live
earn-rate baseline whose absence V001 and V008 both named, and their telemetry
caveat applies verbatim. Session psychology is out of scope: FUN's proxy
(P_ahead ≥ 0.25) is a stated, disputable band pinned by pre-registration — the
measured numbers stand even if the owner re-draws the line.

## Relations (adjacent heads — deliberately links, not duplication)

- vs the outbox (PROPOSALs 001–019, re-read at HEAD `f7906e5`): nearest by
  CONSUMER is PROPOSAL 016 (encounter coexistence → VERDICT 018 by sim-lab's own
  offset map — source numbers cited verbatim, never derived): same
  pin-the-contract-before-the-build-fixes-it move on the same hub, but its
  mechanic is encounter PACING (cooldown namespaces, interruptions/hr) and its
  consumers the Q-0186/Q-0198 builds — zero shared fixture, metric, or parameter.
  Nearest by FAMILY are PROPOSALs 003/008 (→ VERDICTs 001/008): rate-fencing of
  reward FAUCETS with farm-unprofitability checks — this head fences a wager
  SINK, where the threat is inverted (the player risks own funds; the failure is
  ruin/exploit, not spawn-rate farming) and no trace model is shared. PROPOSALs
  006/015 (→ VERDICTs 006/017) are the idle lane's deterministic pacing curves —
  no stochastic wager anywhere in them. PROPOSAL 009 (settle-once catch matrix)
  interrogates the SAME wager games but asks a correctness question (double
  settlement), not a balance one — co-consumable, distinct. PROPOSALs 017/018/019
  are method precedent only (hermetic fixtures, dual arms, APPROVE/REJECT/NULL
  bands; zero shared domain). PROPOSAL 018's revenue lottery is a lognormal
  publishing model, not a wager walk.
- vs superbot's own harvested backlog (237 docs link-indexed in this section's
  README): `wager-flow-map` is a TOOLING tracer over the wager seams
  (parked(routed), probe v0 in-tree) — it maps where money moves, never what odds
  should be; `games-economy-faucet-sink-diagnostic` is historical (promoted
  2026-06-15) and observational (measure the live loop), not a pre-registered
  odds question; `competitive-teardown` is reference research. Grep of the index
  for casino/house-edge/odds/ruin/martingale: nothing else.
- vs sim-lab (local clone @ `e5e1bee`, verdicts through 019 + the offset map read
  this slice): no verdict touches wager odds, house edge, bankroll dynamics, or
  bet sizing; V018 (encounter coexistence, approve: per-source clocks + combined
  cap K=4/hr) and V017 (T10 unlock-only reshape at C2=900/R2=5) are the two
  game-mechanics neighbors and both are pacing, not wagering — their questions
  are settled and NOT re-asked here.
- Tree-wide dedup sweep (`rg -g '!bootstrap.py' -g '!.substrate'` for
  casino/house.edge/martingale/gambler/ruin/RTP/max.bet/bankroll over ideas/ +
  .sessions/ + control/ + docs/): zero hits outside this file. The word "casino"
  does not occur in this repository before this head.

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained probability-model
> head, sim is report-only evidence, no spend/publish/irreversible surface —
> README § probe battery). Verify-first ran FIRST, live this slice: (a)
> **grounding** — the wager seam facts are this tree's own pinned probe evidence
> (`wager-flow-map-2026-07-10.md` @ superbot `2c7d2de`; PROPOSAL 009's game
> corpus), re-read locally, not re-fetched — the sim needs NO superbot fact
> beyond "house-banked minigames are being consolidated", which is inbox ORDER
> 004's own verbatim text ("World's balance pins"). (b) **dedup** — the sweeps
> above; the casino/odds/ruin vocabulary is absent from the entire tree and from
> sim-lab's 19 verdicts. (c) **feasibility arithmetic** — in the sim-spec
> preamble; ≈ 330M integer steps ≈ tens of minutes cold CPython, and the two
> heaviest legs carry hard bet-caps with pre-registered indeterminacy handling.

**1. What is this really?** A pre-registered fairness-envelope sweep for
house-banked wager minigames: does any (house-edge band × max-bet cap) cell keep
casual sessions fun (P_ahead ≥ 0.25), bankrolls safe under player-invented
policies including capped martingale (P_wipe ≤ 0.05), and the casino sink-proof
against grinders under their best policy (P_double ≤ 0.10) — swept across three
payout shapes, with a dual analytic arm (exact binomial tails + gambler's-ruin
closed forms) pinning the Monte Carlo, and the PvP-rake identity (rake r ≡ G1 at
e = r) priced for free.

**2. What is the possibility space?** (i) Don't run it — tonight's consolidation
invents per-game odds by vibe, and the first inflation or rigged-feeling game
becomes a live-ops fire. (ii) Copy real-casino edges (1–15% by game) — those are
tuned for revenue extraction against real money, not for a closed play-economy
where the casino must lose to the faucets on net; adopting them unexamined is the
same invented constant with better branding. (iii) Ask the owner — a
structured-choice question with zero evidence attached; strictly worse after this
verdict prices the options (Q-0263.2). (iv) This head: 36-cell envelope grid,
bands registered first, REJECT and NULL both constructive. (v) Over-scope
(skill-based games with strategy-dependent edges, card-counting, multi-player
pot dynamics, comp/stipend design) — natural follow-ups only if this lands;
the i.i.d.-bet three-shape question is the one the consolidation hits tonight.

**3. What is the most advanced capability reachable by the simplest
implementation?** One ~250-line stdlib file: a bankroll-walk kernel (stake rule →
win/lose → clip) reused by all three profiles, exact `math.comb` tails and a
closed-form ruin function as the second arm, and a 36-cell table that turns
"what odds should our casino run?" from taste into a contract row — for every
house-banked game the hub ever adds, not just tonight's batch.

**4. What breaks it? (assumptions made explicit)** (a) **Bets are i.i.d.** — no
skill edge, no card-counting, no strategy-dependent p; blackjack's
strategy-spread edge is folded into the e-grid itself (e is the REALIZED edge
against the table's actual player mix — the grid brackets good and bad play).
(b) **FUN is a proxy** — P_ahead ≥ 0.25 is a defensible, disputable line; it is
pre-registered precisely so the measured numbers survive a re-drawn line, and
the full P_ahead curves ship in the table. (c) **Three archetypes, not every
game** — k ∈ {1, 5, 19} brackets the payout-shape axis; a mixed-payout game
(blackjack's 3:2 naturals, multi-line slots) lands between brackets, and the
verdict states interpolation is on the consumer. (d) **Boundary effects** —
integer chips, stake clipping, and absorbing boundaries are pinned in the loop
order; the e=0 control (P_double = 1/3 exactly) and the Arm-A agreement gate
catch kernel bugs before any cell is believed. (e) **PRNG stability** —
`random.Random(20260721)` pinned, loop order pinned, CPython minor version pinned
in the results table.

**5. What does it unlock?** The hub's first measured wager-balance primitive:
tonight, the consolidation inherits its odds row instead of inventing one; after
tonight, every new casino game is a one-line conformance check against the
pinned band; and the REJECT/NULL arms are just as consumable (rake-lane routing
for even-money games, named non-odds levers) — plus the first quantified
fun-vs-sink trade-off curve any future economy decision (comps, daily bonuses,
tournament prize pools) can cite.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing external
at sim time — every fixture ({B₀, k-grid, e-grid, m-grid, policy constants,
profile stop rules, M per profile, seeds, band constants}) is stated in this file
and committed as a small JSON alongside the sim. Kill tests, run live this
slice: a prior casino/odds/ruin head anywhere in the tree (NOT found — sweeps
above), a sim-lab verdict on wager balance (NOT found — verdicts through 019
read at `e5e1bee`), the consolidation already carrying pinned odds (NOT found —
no odds surface exists in this tree's pinned superbot evidence, and ORDER 004
expects the balance pins to be REQUESTED, not already made), infeasible runtime
(NOT found — arithmetic above, with capped legs). Sim-worthy or judgment-only:
sim-worthy — the entire question is computable ruin/tail arithmetic against
pre-registered thresholds; the one judgment question (are 0.25/0.05/0.10 the
right lines?) is pinned by pre-registration and stated as the disputable bands,
never the measured numbers.

**7. Which lane should build it — and what does it displace or duplicate?**
sim-lab runs it (its harness, its verdict grammar; sim + fixture JSON committed
in its sims/ tree). The verdict's consumer is the superbot World seat's
minigame/casino consolidation (named in the header), with the superbot-games
shared surfaces inheriting the same row if house-banked games land plugin-side.
Duplicates nothing: V001/V008/V018 fence faucet pacing, V006/V017 fence idle
pacing, P009 fences settlement correctness — no verdict or proposal touches
wager odds (dedup section above).

**8. What is the smallest shippable slice?** One sim-lab intake dir: one stdlib
file (bankroll-walk kernel + analytic arm + 36-cell grid), one fixture JSON (all
constants copied verbatim from this file), one results table {P_ahead, P_wipe,
P_double, cap-hit fraction, median bets-to-ruin} × (archetype, e, m, policy) plus
the E\* envelope summary — ending in exactly one of APPROVE/REJECT/NULL per the
pre-registered rule, reproducible from the fixtures alone, byte-identical on
re-run, no flags.

**Recommendation: sim-ready** — the question is crisp and computable, the bands
and decision rule (with stated evaluation order) are registered above BEFORE any
code exists, the genre's failure modes are pre-empted (proxy dispute →
pre-registered bands + full curves shipped; model-dependence → three bracketing
archetypes + axis-naming NULL; MC error → dual analytic arm with a 1.0 pp
agreement gate + e=0 exact control; runaway legs → hard caps with pre-registered
indeterminacy routing), and every outcome hands tonight's consolidation a row it
can adopt verbatim. THE ONE QUESTION for the simulator: *Under the pinned
bankroll-walk model (B₀ = 1,000 integer chips; archetypes G1/G2/G3 with payout
k ∈ {1, 5, 19} and win probability p = (1−e)/(k+1); house-edge grid e ∈ {0.01,
0.02, 0.05, 0.10} + e=0 control; max-bet caps m ∈ {0.05, 0.25, 1.0}·B₀ clipping
all policies; policies F-0.01/F-0.05/F-0.10 fixed-fraction, C constant-50,
M capped-martingale base-10; profiles CASUAL 100-bet session, GRINDER
double-or-half capped at 4,000 bets with >1% cap-hits marking the cell
indeterminate, COMPULSIVE reporting-only; Arm A exact binomial FUN tails +
G1-constant gambler's-ruin closed forms + e=0 P_double = 1/3 control, Arm S
seeded MC `random.Random(20260721)` M = 5,000/2,000/500 with 1.0 pp agreement
gate and a half-M stability leg seed 20260722), for which (e, m) cells do FUN
(reference-leg P_ahead ≥ 0.25), SAFE (max-policy P_wipe ≤ 0.05), and SINK
(max-policy P_double ≤ 0.10) hold simultaneously per archetype — and does the
result land REJECT (E\* empty at every cap in ≥ 2 archetypes → odds cannot
reconcile fun with sink-proofing; the consolidation gets the quantified gap and
the named non-odds levers), APPROVE (some cap m\* gives ≥ 2 consecutive shared
edges across all three archetypes → one house rule: shared max-bet + house-edge
band), or NULL (anything else → the per-archetype envelope table is the pin,
flip axis named — expected: payout multiplier k — with even-money games routed
to the PvP/rake lane via the stated rake ≡ edge identity)?* Done-when: the
committed sim + fixture JSON reproduce the full results table and envelope
summary byte-identically, Arm S passes the Arm-A agreement gate and the e=0
control, the stability leg reproduces the same ruling, and the verdict issues
exactly one of APPROVE/REJECT/NULL per the pre-registered rule (evaluation order
stated) with the bankroll-relative boundary and the V001/V008 earn-rate-baseline
caveat restated verbatim, and the reporting-only legs (compulsive harm context,
e=0 control, PvP-rake identity) stated as legs that cannot flip the decision.
