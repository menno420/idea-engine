# Penney's game at longer words — does "never go first" survive word length, and is the folk flip-rule beater exactly optimal?

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 COMPLETELY-UNRELATED-domain
> slot, round 4; the domain itself is recreational probability / sequential pattern-race
> games — Penney's game over fair-coin words — fleet-external by design and DIFFERENT
> from round 1's social choice (PROPOSAL 017), round 2's congestion routing (PROPOSAL
> 024), and round 3's tournament seeding (PROPOSAL 028), so the rotation now spans FOUR
> domains) ·
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/idea-engine@1c79289eddd5730602581d3f4a7591c847fbecee · fetched 2026-07-13T08:13:49Z
> (the dedup-sweep pin — this repo's own tree at drafting HEAD, the only read this head
> takes; the sim itself is fully hermetic: zero repo/network reads at verdict time,
> every fixture constructed in-sim from the pinned constants in this file)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous pipeline —
"continue coming up with new ideas, that is your main purpose") on the rotation ORDER
004 rule 3 established and the morning tally ratified ("Rotate lanes deliberately: … →
COMPLETELY UNRELATED domains (I want those too)") — PROPOSAL 017 opened the
unrelated-domain lane with social choice, PROPOSAL 024 rotated it into congestion
routing, PROPOSAL 028 into tournament-format design; this is round 4's head, rotated
into a FOURTH fleet-external domain (sequential pattern-race probability). **Placement
note (decide-and-flag):** sections are roster-derived and inventing one ad hoc is
forbidden (README § Sections; `check_sections.py` reds an ORPHAN section against the
live roster), and that checker's own carve-out rules that sim-lab-shaped ideas "ride
`ideas/fleet/` or the proposing section" — so this fleet-external head lives here,
flagged rather than silently squatting, exactly as PROPOSALs 017, 024, and 028 did.

## The idea (reasoned to its fuller form — Q-0254 duty)

**The folk belief.** Penney's game (1969; canonized by Gardner's 1974 column) is the
classic two-player coin race: each player commits a word over {H, T} of the same length
L, a fair coin is flipped repeatedly, and whoever's word appears first as a run of
consecutive flips wins. The popularized story has two halves, both told at L = 3:
(1) **"never go first"** — whatever word the first player picks, the responder can pick
a word that beats it, with odds as lopsided as 7:1 (THH over HHH) and never worse than
2:1; (2) **the folk beater rule** — the responder wins by taking the first L−1
characters of the opponent's word and prepending the complement of its second
character: σ(A) = ¬a₂ · a₁a₂…a_{L−1}. Both halves are true and famous at L = 3 — every
popularization prints the same 8×8 table. What is genuinely NON-OBVIOUS is what happens
to the story as the words get longer, which is exactly where casual players go when
they hear the trick ("fine, then we'll use longer words"): does the responder's
GUARANTEED edge — the minimax value V(L) = min over first picks A of max over responses
B ≠ A of P(B appears before A) — stay overwhelming, decay slowly, or collapse toward a
fair coin by L = 5? And does the folk beater rule σ stay EXACTLY optimal beyond the
length the tables were computed for? Nontransitivity itself is a theorem (every word is
beatable at L ≥ 3 — not in question, and deliberately NOT a band here); the measured
unknowns are the exact decay curve {V(3), V(4), V(5)} and the folk rule's optimality
share on the full census — numbers nobody carries, in a domain where every number is an
exact rational a stdlib file can compute. This mirrors the accepted P017/P024/P028
pattern exactly: the effect is settled in principle; its magnitude/shape on a committed
family is the unknown; and REJECT, APPROVE, and NULL are all live.

**The game space (fixed, finite, fully enumerable).** Words of length L over {H, T}:
2^L of them; ordered pairs (A, B) with B ≠ A: 56 at L = 3, 240 at L = 4, 992 at L = 5 —
1,288 decision cells total, plus a 12-cell L = 2 anchor leg (reporting-only). For
distinct equal-length words a tie is impossible (two different length-L words cannot
both complete on the same flip) and the race ends with probability 1, so P(B before A)
is a well-defined exact rational and P(B before A) + P(A before B) = 1.

**Exact computation — fully deterministic, NO RNG anywhere.** Everything is computed in
exact `fractions.Fraction`; there is no Monte Carlo arm and no seed. (Seed-registry
note, explicit: this sim draws ZERO seeds — the PROPOSAL 031 registry high-water
**20260767** is left unchanged; the next seeded head continues from there.)

- **Arm A (Conway leading numbers):** for words X, Y define the correlation
  L(X, Y) = Σ_{k=1..L} δ_k · 2^{k−1}, where δ_k = 1 iff the last k characters of X
  equal the first k characters of Y. Then the odds that B beats A are
  (L(A,A) − L(A,B)) : (L(B,B) − L(B,A)), so P(B before A) =
  (AA − AB) / ((AA − AB) + (BB − BA)) — integer arithmetic, exact by construction.
- **Arm B (independent absorption solve, the structural cross-check):** build the
  two-word prefix automaton (states = the proper prefixes of A and of B plus the empty
  string, ≤ 2L−1 states; the transition on a flip c sends state s to the longest
  suffix of s·c that is a prefix of A or B, full words absorbing) and solve the
  absorption probabilities by first-step analysis — exact Gaussian elimination over
  `fractions.Fraction`. Arm B must equal Arm A by EXACT RATIONAL EQUALITY on every
  ordered-pair cell (all 1,288 + the L = 2 leg) — a gate on the ALGORITHM, the
  seedless-exact analogue of the P017/P024 arm-agreement gate and the same discipline
  P028 ran; any inequality invalidates the run.
- **Self-checks (all exact, run invalid on failure):** the classic published anchors —
  P(TH before HH) = 3/4 (the L = 2 leg), P(THH before HHH) = 7/8, and V(3) = 2/3 (the
  Gardner-table floor: the best L = 3 first picks lose exactly 2:1); complement
  invariance P(B̄ before Ā) = P(B before A) on every cell (flip every bit of both
  words); the antisymmetry identity P(B before A) + P(A before B) = 1 on every
  unordered pair, both sides computed independently, never by definition; strictly
  positive Conway denominators on every cell; the automaton state-count audit
  (≤ 2L−1, absorbing states exactly 2); and σ(A) ≠ A verified on every word (true by
  construction: σ(A) = A would force a₂ = ¬a₂).

**Measured quantities (all exact rationals):**

- **V(L) = min_A max_{B≠A} P(B before A)** for L ∈ {3, 4, 5} — the responder's
  guaranteed win probability under best play by BOTH sides (the first player picks the
  safest word, the responder answers optimally); plus the argmin (safest first-pick)
  words and each argmin's optimal response.
- **O(L)** — the folk-rule optimality share: the fraction of the 2^L first picks A for
  which σ(A) attains max_{B≠A} P(B before A) exactly; and **S(L)** — the worst
  shortfall max_A [max_B P(B before A) − P(σ(A) before A)], the price of trusting the
  popularized rule where it is not optimal.
- **f_{2:1}(L)** — the share of first picks beatable at ≥ 2:1 (P ≥ 2/3), the
  popularization's "never worse than 2:1" claim read against longer words.
- The full 2^L × 2^L exact matrix per L and the trap table (max_B P per A, including
  the famous 7/8 row) — the census everything above is read from.

**Pre-registered decision bands (fixed BEFORE any code exists — honest guesses, not
tuned; evaluated in this order, and the two decision bands are DISJOINT by construction
(13/25 < 3/5), so the order is stated for form, not load-bearing):**

- **REJECT** ("the never-go-first maxim is an L = 3 curiosity — longer words are the
  cheap fairness fix") iff V(5) ≤ 13/25 (52%): by length 5 an informed first player
  concedes at most 2 points against a perfect responder. Checked FIRST.
- **APPROVE** ("the responder edge is structural — first-order at every swept length")
  iff V(L) ≥ 3/5 (60%) at ALL of L ∈ {3, 4, 5}: even the safest first pick loses 3:2
  or worse at every practical word length.
- **NULL** (the straddle — a legitimate reportable outcome): anything else. The finding
  is then the measured decay curve {V(3), V(4), V(5)} itself — the edge persists but
  attenuates (or moves non-monotonically, which would be its own citable surprise) —
  and neither camp's soundbite may be cited as settled.

**What a reader DOES differently on the verdict (so the ruling is actionable, not
trivia).**

- **APPROVE** → any pick-then-respond pattern-race design (a party wager, a classroom
  demo, or any game mechanic where one side commits a target pattern and the other
  responds) must treat PICK ORDER as a first-order fairness lever at every practical
  word length — "just use longer words" may NOT be cited as the fix; fair designs need
  simultaneous/blind picks or a priced pick order, and the folk-rule table ships with
  its measured optimality share.
- **REJECT** → the popularized "never go first" maxim gets a measured LENGTH BOUNDARY:
  the L = 3 tables may no longer be generalized as the game's story, and longer words
  ARE the citable cheap fix (the exact concession at L = 5 attached).
- **NULL** → the honest middle: the exact decay curve is the citable pin, and the
  folk-rule optimality share O(L) still ships as the side finding either way.

**Reporting-only legs (cannot flip the decision):** the L = 2 anchor leg (4 words, the
3/4 classic, plus the fair HT-vs-TH cell); O(L), S(L), and the per-word folk-rule
table; f_{2:1}(L); the trap table and both distributions' quartiles per L; and whether
the safest first pick and the biggest trap are complements/reverses of each other
(pattern-structure context, prose only).

**Grounding / hermeticity.** ZERO network reads at verdict time AND zero repo reads —
the entire world (the word census, both algorithms' inputs, band constants, the three
classic anchor rationals) is constructed in-sim from the pinned constants in this file,
committed as a small fixture JSON alongside one stdlib file. All arithmetic exact
`fractions.Fraction`; byte-identical output on re-run is BY CONSTRUCTION (no floats, no
RNG, no environment reads), platform-independent. Feasibility arithmetic: 1,300 cells ×
two exact algorithms, the heavier arm a ≤ 9×9 rational linear solve per cell — well
under a minute in pure CPython.

## Relations (adjacent heads — deliberately links, not duplication)

- vs the outbox (PROPOSALs 001–031): nothing adjacent by DOMAIN — no proposal prices a
  pattern race, a stopping-time game, word correlations, or any nontransitivity
  question. Nearest by METHOD only: PROPOSAL 028 (the same fully-exact, zero-RNG,
  dual-independent-algorithm census discipline — `fractions.Fraction`, rational-equality
  gate, pre-registered disjoint bands), and PROPOSALs 017/024 (the same pre-registered
  honest-NULL rotation pattern, seeded arms there). No shared domain, fixture, metric,
  or consumer with any of the three.
- vs the fleet's own coin-adjacent content, checked by name because the word collides:
  the casino family P020/P023/P027 → V022/V025/V029 uses an even-money "coinflip
  shape" archetype — but that is BANKROLL-RUIN dynamics under a house edge (stake
  policies, wipe/double probabilities), not a pattern race between words on a fair
  coin: zero shared question, fixture, or measured quantity. PROPOSAL 028's
  Bradley–Terry model is pairwise win probabilities in a TOURNAMENT format — different
  model, different objects. Tree-wide `rg -i "penney|nontransitive|non-transitive|
  coin.?sequence|leading.number|pattern.?race"` over ideas/ + control/ + .sessions/ +
  docs/ (bootstrap.py and .substrate excluded) at the grounding pin returns ZERO hits;
  a secondary sweep for "coin" hits only the casino archetype prose and P028's "near a
  coin flip" simile — mechanical uses, no pattern-race content anywhere in the tree.
- Runners-up this slice, weighed and dropped on merit: **bus bunching on a loop line**
  (deterministic headway dynamics — real domain, but the model needs several invented
  constants (dwell/board rates, loop length) with no committed anchor and no folk
  default as crisp as "never go first"); **elevator dispatch on a small building**
  (exact state enumeration explodes past toy sizes and the reader consequence is weak
  — nobody ships the folk policy because a table said so); **chip-firing/sandpile
  stabilization** (beautiful exact mathematics, but no falsifiable folk belief and the
  weakest what-a-reader-does story of the four); **calendar interval packing** (the
  unweighted greedy is EXACTLY optimal by theorem — the honest question dies at
  pre-registration).

## Model basis (declared model-dependence — the P024 discipline)

This verdict's numbers are CONDITIONAL on an embedded model, named up front:

- **(1) Statistical assumption:** a FAIR i.i.d. coin (p = 1/2 per flip) and both
  players restricted to words of the SAME length L. The measured curve is a property
  of THIS game frame — the frame every popularization uses.
- **(2) Single most-likely-to-flip alternative:** a BIASED coin (p ≠ 1/2), under which
  the whole table deforms — the Conway leading-number arm is fair-coin-specific, while
  the automaton arm generalizes to any p, so "V(L) under bias" is a natural follow-up
  head with one arm already built; a softer flip is the RESPONSE SPACE — allowing the
  responder a SHORTER or LONGER word changes the game (unequal-length races are out of
  this verdict's registered scope, and the verdict must say so).

## Probe report battery (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe
> battery). Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide
> pattern-race sweep above returned zero domain hits at the grounding pin
> (`1c79289`); PROPOSALs 001–031 re-read in full at HEAD before drafting, and the
> three prior rotation occupants (P017 social choice, P024 routing, P028 seeding)
> are all different domains. (b) **kill test NOT triggered** — no prior proposal,
> idea file, or session-card 💡 touches Penney's game, word correlations, or
> nontransitive races. (c) **feasibility arithmetic checked** — 1,288 + 12 cells ×
> (integer correlation sums + one ≤ 9×9 exact-Fraction linear solve each): well
> under a minute in pure CPython, no dependencies.

**1. What is this really?** A pre-registered MEASUREMENT of how the most famous
nontransitive game actually scales: the exact minimax decay curve {V(3), V(4), V(5)}
of the responder's edge in Penney's game, plus the exact optimality share of the
popularized flip-rule beater — every number a rational computed twice by structurally
independent exact algorithms, against bands fixed before any code runs. The sim
constructs its entire world from the pinned constants in this file: zero repo reads,
zero network, zero RNG, zero floats.

**2. What is the possibility space?** (i) Don't run it — the round-4 unrelated-domain
slot goes unserved and the rotation's standing rule is dead letter this cycle.
(ii) Re-use a prior round's domain — fails the owner's "rotate" ask (P017/P024/P028
occupy voting, routing, tournaments). (iii) A literature summary ("the second player
always wins; here is Gardner's table") — retells L = 3, measures nothing, and is not
the pipeline's product; the open question is the exact CURVE and the folk rule's
optimality on the full census, which only enumeration answers. (iv) Monte-Carlo
simulate the races — strictly worse than exact computation where a closed rational
exists (the P028 stance verbatim). (v) This head: full ordered-pair census at
L ∈ {3, 4, 5}, dual independent exact algorithms, bands registered first. (vi)
Over-scope (L = 6+, biased coins, unequal-length responses, k > 2 players) — L = 6
doubles the census to 4,032 pairs and stays feasible but adds no folk-table anchor;
bias and unequal lengths are the named follow-up heads if this lands APPROVE or NULL.

**3. What is the most advanced capability reachable by the simplest implementation?**
One ~200-line stdlib file: words are tuples; the Conway correlation is a two-line
suffix/prefix loop; the automaton arm is a longest-suffix transition table plus a
`fractions.Fraction` Gaussian elimination; the census is two nested loops. That single
file yields the exact scaling law of the world's best-known nontransitive game — a
publication-grade quantitative answer (every number a rational, no error bars at all)
to the question every popularization raises and none measures, from a sim a verdict
session runs cold in under a minute.

**4. What breaks it? (assumptions made explicit)** (a) **The model is the game's own
canon** — fair coin, equal lengths — and the `## Model basis` note names the bias and
response-space flips; the bands quantify only over the swept L. (b) **Band placement
could cherry-pick** — both bands are committed in this file BEFORE any code, are
DISJOINT by construction (no overlap ambiguity), and NULL is a first-class outcome
pinning the curve. (c) **A wrong remembered anchor** — the three classic anchors
(3/4, 7/8, V(3) = 2/3) are the most-reprinted constants in recreational probability;
if any fails, the run is INVALID by its own gate and the discrepancy is the finding —
never silently absorbed. (d) **Algorithm bugs** — two structurally independent exact
algorithms must agree to rational EQUALITY on all 1,300 cells, plus complement
invariance, independently-computed antisymmetry, denominator positivity, and the
automaton state audit; a single inequality invalidates the run. (e) **Ties/degeneracy**
— impossible for distinct equal-length words (stated and asserted), and σ(A) ≠ A holds
by construction (asserted anyway).

**5. What does it unlock?** The pipeline's FOURTH fleet-external verdict and the
rotation lane's proof it spans domains (voting → routing → tournaments → pattern
races); a measured, citable answer the owner can deploy whenever the game comes up
(the trick either survives word length with exact odds attached, or dies at a measured
boundary); the folk-rule optimality share as a standalone side pin; and on APPROVE or
NULL two natural follow-up heads (biased-coin V(L); unequal-length response spaces)
with one algorithm arm already built.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing external — by
design: no repo, no network, no dataset, no RNG; every fixture (the L grid, band
constants, the folk-rule definition, the three anchor rationals) is stated in this
file and committed as a small JSON alongside the sim. Kill tests, run live this slice:
a prior pattern-race head anywhere in the tree (NOT found — sweep empty at
`1c79289`); an occupied round-4 slot with THIS domain (NOT found — P017/P024/P028 are
different domains); infeasible runtime (NOT found — arithmetic in the preamble, under
a minute). Sim-worthy or judgment-only: sim-worthy — the entire question is a
computable set of exact rationals against pre-registered thresholds; the one judgment
call (are 3/5 and 13/25 the RIGHT materiality lines?) is pinned by pre-registration
and stated as the thing a reader may dispute — about the bands, never about the
measured numbers.

**7. Which lane should build it — and what does it displace or duplicate?** sim-lab
runs it (its harness, its verdict grammar; the sim file + fixture JSON committed in
its sims/ tree per convention). No fleet lane consumes the verdict as a build input —
the consumer is the owner/manager as READERS (plus, incidentally, any future game
mechanic that ever runs a commit-then-respond pattern race, which would inherit the
table for free). Duplicates nothing: the domain sweep found zero prior pattern-race
art in this tree, and no sim-lab verdict through the current ledger touches Penney's
game or word-correlation mathematics.

**8. What is the smallest shippable slice?** One sim-lab verdict dir: one stdlib file
(word census + Conway leading-number arm + independent automaton-absorption arm +
self-checks), one fixture JSON ({L grid {3,4,5} + the L = 2 anchor leg, band constants
3/5 and 13/25, the folk-rule definition σ(A) = ¬a₂ · a₁…a_{L−1}, the three classic
anchor rationals 3/4, 7/8, 2/3}, values copied verbatim from this file), one results
table {per L: the full exact matrix, V(L) + argmin words + their optimal responses,
O(L), S(L), f_{2:1}(L), the trap table; the L = 2 anchors; the reporting legs} ending
in exactly one of APPROVE / REJECT / NULL per the pre-registered rule — reproducible
from the fixtures alone, byte-identical on re-run BY CONSTRUCTION (exact rationals, no
RNG, no floats, platform-independent), no flags.

**Recommendation: sim-ready** — the question is crisp and completely computable, the
bands and decision rule are registered above BEFORE any code exists with the two
decision bands disjoint by construction, both genre failure modes are pre-empted
(model-dependence → the game's own canonical frame + the `## Model basis` declaration
+ a NULL band; algorithmic error → dual independent exact algorithms gated on rational
equality plus six committed self-checks), and the verdict changes what a reader may
cite in every branch. THE ONE QUESTION for the simulator: *Under the pinned fair-coin
Penney frame (i.i.d. fair flips; both players commit distinct words of the same length
L over {H,T}; first word to appear as a run of consecutive flips wins — ties impossible
for distinct equal-length words), what is the responder's guaranteed edge
V(L) = min_A max_{B≠A} P(B before A) at L ∈ {3, 4, 5}, computed as exact rationals over
the full ordered-pair census (56/240/992 cells) by Conway leading numbers AND
independently by exact automaton-absorption solves with rational equality required on
every cell (zero RNG/floats/seeds — the P031 seed-registry high-water 20260767
explicitly untouched) — landing (bands disjoint, REJECT stated first) REJECT ("an L = 3
curiosity — longer words are the cheap fix") iff V(5) ≤ 13/25, APPROVE ("the responder
edge is structural at every swept length") iff V(L) ≥ 3/5 at all L ∈ {3, 4, 5}, or NULL
(the straddle: the measured decay curve {V(3), V(4), V(5)} is the citable pin and
neither camp's soundbite may be cited as settled) — with the folk flip-rule beater
σ(A) = ¬a₂ · a₁…a_{L−1} scored reporting-only (optimality share O(L), worst shortfall
S(L), per-word table) alongside f_{2:1}(L), the trap table, and the L = 2 anchor leg?*
Done-when: the committed stdlib sim + fixture JSON reproduce the full results table
byte-identically on re-run (exact rationals, platform-independent, no CPython version
sensitivity), every gate passes (Arm A ≡ Arm B rational equality on all 1,300 cells,
the classic anchors 3/4 / 7/8 / V(3) = 2/3, complement invariance, independent
antisymmetry, denominator positivity, automaton state audit), and the verdict issues
exactly ONE of APPROVE/REJECT/NULL per the pre-registered rule — stating the
model-basis caveat (fair i.i.d. coin, equal-length words; the biased-coin and
unequal-length flips named as follow-ups, the automaton arm already generalizing) and
the L ≤ 5 boundary (L = 6's 4,032-pair census is a follow-up, not a blocker; the swept
range is where the folk tables live); honest-null explicit: a NULL lands as a
finalized verdict pinning the exact decay curve, not a re-run request.
