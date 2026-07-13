# Single-elimination seeding fairness — is the standard 8-team bracket (1v8, 4v5, 3v6, 2v7) actually OPTIMAL for "the best team wins" and "a 1-vs-2 final"?

> **State:** sim-ready
> **Class:** process (pipeline rotation — inbox ORDER 004 rule 3's COMPLETELY-UNRELATED-domain
> slot, round 3; the domain itself is sports statistics / tournament-format design —
> knockout-bracket seeding under a Bradley–Terry win-probability model — fleet-external
> by design and DIFFERENT from round 1's social choice (PROPOSAL 017) and round 2's
> congestion routing (PROPOSAL 024), so the rotation now spans THREE domains) ·
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous pipeline)
and ORDER 004 rule 3 ("Rotate lanes deliberately: … → COMPLETELY UNRELATED domains
(I want those too)") — PROPOSAL 017 opened the unrelated-domain lane with social choice,
PROPOSAL 024 rotated it into congestion routing; this is round 3's head, rotated into a
third fleet-external domain (tournament seeding fairness). **Placement note
(decide-and-flag):** sections are roster-derived and inventing one ad hoc is forbidden
(README § Sections; `check_sections.py` reds an ORPHAN section against the live roster),
and that checker's own carve-out rules that sim-lab-shaped ideas "ride `ideas/fleet/` or
the proposing section" — so this fleet-external head lives here, flagged rather than
silently squatting, exactly as PROPOSALs 017 and 024 did.

## The idea (reasoned to its fuller form — Q-0254 duty)

**The folk belief.** Every sports fan "knows" the standard single-elimination seeding —
in an 8-team bracket, quarterfinals 1v8 and 4v5 in one half, 3v6 and 2v7 in the other —
"protects the best team" and "sets up the 1-vs-2 final". Tournament regulations
worldwide (tennis draws, NCAA regionals, esports playoffs) treat it as the fair default.
What is genuinely NON-OBVIOUS: under an explicit win-probability model, is the standard
assignment actually **optimal among ALL possible bracket assignments** for either stated
goal — (a) maximizing P(the strongest team wins the tournament), and (b) maximizing
P(the final is 1-vs-2)? The classical tournament-design literature has long hinted the
answer is "not always" (no seeding is optimal for every strength matrix), but the folk
belief survives because nobody carries a MEASURED, reproducible gap for concrete
strength profiles. This mirrors the accepted PROPOSAL 017/024 pattern exactly:
the effect (suboptimality) is POSSIBLE in principle — whether it occurs, for WHICH
strength profiles, and by HOW MUCH on a committed family, is the measured unknown. NULL
(the folk belief holds approximately: gaps exist but below every materiality line) is a
live, reportable outcome, not a fudge — and so is REJECT (the folk belief holds
EXACTLY).

**The bracket space (fixed, finite, fully enumerable).** Fix the balanced 8-leaf binary
tree: quarterfinal pairs (L1,L2), (L3,L4), (L5,L6), (L7,L8); semifinal 1 between the
first two pair-winners, semifinal 2 between the last two; one final. A bracket
assignment places the 8 teams on the 8 leaves; two assignments are the SAME bracket iff
related by the tree's automorphism group (swap within any QF pair, swap the two pairs
within a half, swap the two halves — order 2⁷ = 128). Distinct brackets:
8!/2⁷ = **315 exactly**. The sim enumerates all 8! leaf orders, canonicalizes
recursively (a subtree is a nested pair; sort each pair by minimum contained team), and
must find EXACTLY 315 equivalence classes of EXACTLY 128 assignments each — a committed
partition self-check, not an assumption. The standard seeding is the class of
(1,8,4,5 | 3,6,2,7).

**The win-probability model (Bradley–Terry, committed strengths).** Teams are ranked
1..8 by a committed strength vector s (strictly decreasing, integers); in any match,
P(i beats j) = s_i/(s_i + s_j), matches independent, strengths constant across rounds,
no draws. Four committed strength profiles span the shape space, all fixed here BEFORE
any code exists:

- **F1 linear decay:** s = (8, 7, 6, 5, 4, 3, 2, 1) — evenly spaced field.
- **F2 geometric decay:** s = (128, 64, 32, 16, 8, 4, 2, 1) — every rank halves; each
  favorite is a 2:1 winner over the next rank.
- **F3 top-heavy one-star:** s = (100, 8, 7, 6, 5, 4, 3, 2) — one dominant team over a
  compressed field.
- **F4 near-flat:** s = (107, 106, 105, 104, 103, 102, 101, 100) — every match is
  near a coin flip.
- **F0 flat control (reporting-only):** s = (100 × 8) — every bracket must yield
  P(each team wins) = 1/8 EXACTLY and P(a specific pair meets in the final) = 1/16
  exactly when the pair is split across halves, 0 when it shares a half; closed-form
  identities asserted, never a decision input.

**Exact computation — fully deterministic, NO RNG anywhere.** Everything is computed in
exact `fractions.Fraction`; there is no Monte Carlo arm and no seed. (Seed-registry
note, explicit: this sim draws ZERO seeds — the PROPOSAL 027 registry high-water
**20260755** is left unchanged; the next seeded head continues from there.)

- **Arm A (winner-distribution recursion):** for a subtree with halves L and R,
  W_subtree(i) = W_L(i)·Σ_{j∈R} W_R(j)·p_ij + W_R(i)·Σ_{j∈L} W_L(j)·p_ij. Then
  objective (a) is P_best = W_root(team 1) and objective (b) is
  P_12 = W_half1(1)·W_half2(2) + W_half1(2)·W_half2(1) (automatically 0 when teams 1
  and 2 share a half). Cost: 315 brackets × 4 profiles × a few hundred Fraction ops —
  well under a minute.
- **Arm B (independent path enumeration, the structural cross-check):** enumerate all
  2⁷ = 128 complete outcome paths of a bracket (round by round; a path's probability is
  the product of its 7 match probabilities) and read both objectives off the paths.
  Arm B must equal Arm A by EXACT RATIONAL EQUALITY on every (bracket, profile,
  objective) cell — a gate on the ALGORITHM (two structurally different computations of
  the same rational), which is the seedless-exact-sim analogue of the P017/P024
  arm-agreement gate; any inequality invalidates the run.
- **Self-checks (all exact, run invalid on failure):** the 315×128 partition audit;
  Σ_i W_root(i) = 1 on every (bracket, profile); the two-team identity
  p_12 = s1/(s1+s2) on a degenerate fixture; the F0 flat-control closed forms; and
  bracket-relabeling invariance (a non-canonical representative of the standard class
  reproduces the canonical class's numbers exactly).

**Measured quantities (per profile, both exact rationals):**

- **Δ_a = max over all 315 brackets of P_best − P_best(standard)** — how far the
  standard bracket sits below the true optimum for "the best team wins" (Δ_a = 0 iff
  standard is exactly optimal); plus the argmax bracket and the standard's rank among
  315 (ties counted).
- **Δ_b = max over all 315 brackets of P_12 − P_12(standard)** — the same for "the
  final is 1-vs-2".

**Pre-registered decision bands (fixed BEFORE any run — honest guesses, not tuned),
evaluated in this order:**

- **REJECT** ("folk belief EXACTLY right — skip the audit") iff Δ_a = 0 AND Δ_b = 0 in
  ALL four profiles (exact rational equality — the standard bracket is the true argmax
  for both objectives everywhere). Checked FIRST: it is the strictest claim.
- **APPROVE** ("bracket audit warranted — standard seeding measurably suboptimal") iff
  Δ_a ≥ 1/200 (0.5 pp) in ≥ 1 profile OR Δ_b ≥ 1/100 (1.0 pp) in ≥ 1 profile.
- **NULL** (the straddle — a legitimate reportable outcome): anything else, i.e.
  suboptimality exists but every gap is sub-material. The finding is then "the folk
  belief holds APPROXIMATELY: standard seeding is not exactly optimal, and the exact
  per-profile gap table is the citable pin" — neither "standard seeding is provably
  right" nor "standard seeding is broken" may be cited as settled.

**What a reader DOES differently on the verdict (so the ruling is actionable, not
trivia).**

- **APPROVE** → an organizer whose STATED goal is "the best team should win" or "a
  1-vs-2 final" should not default to standard seeding: the per-profile argmax bracket
  table ships with the verdict, and "1v8/4v5/3v6/2v7 protects the best team" may no
  longer be cited as settled for that goal — pick the measured bracket for your
  strength profile (or state a different goal).
- **REJECT** → standard seeding is safe-by-default for BOTH objectives across the
  swept shape space; skip design-time bracket optimization and cite the exact
  optimality.
- **NULL** → the honest middle: gaps are real but below every materiality line; the
  standard bracket is a fine default in practice, exact optimality may not be claimed,
  and the gap table is what gets cited.

**Reporting-only legs (cannot flip the decision):** the full 315-bracket distribution
of both objectives per profile (min / quartiles / max — including the WORST bracket,
i.e. how much adversarial mis-seeding can suppress the favorite or the dream final);
whether objectives (a) and (b) pick DIFFERENT argmax brackets (the two folk goals need
not agree); the F0 flat control; and P(final is 1-vs-2) under the standard bracket as
a plain table (spectator-facing context).

**Grounding / hermeticity.** ZERO network reads at verdict time AND zero repo reads —
the entire world (tree topology, the 315-class enumeration, strength profiles, band
constants) is constructed in-sim from the pinned constants in this file, committed as a
small fixture JSON alongside one stdlib file. All arithmetic exact `fractions.Fraction`;
byte-identical output on re-run is by construction (no floats, no RNG, no environment
reads), platform-independent.

## Relations (adjacent heads — deliberately links, not duplication)

- vs the outbox (001–027): nothing adjacent by DOMAIN — no proposal prices bracket
  seeding, tournament formats, or any Bradley–Terry-model question. Nearest by METHOD
  only: PROPOSAL 017 (social choice) and PROPOSAL 024 (Braess routing) — the same
  pre-registered exact-census + honest-NULL discipline, shared with round 3 wholesale,
  but NO shared domain, fixture, or consumer. Rounds 1–3 of the unrelated-domain lane
  are now voting theory / congestion games / tournament design.
- vs the fleet's own "tournament" content, checked by name because the word collides:
  `ideas/superbot/rps-tournament-service-refactor-2026-07-10.md` is a CODE-refactor
  head (orchestration out of a Discord cog — no seeding, no win-probability model);
  PROPOSAL 009 (settle-once guard) touches blackjack/RPS **tournament settlement
  correctness**, never format fairness; the game-mechanics casino line
  (P020/P023/P027) prices house-edge economics. No fleet lane runs a SEEDED
  elimination bracket anywhere — the domain here is sports-statistics format design
  with no fleet consumer, which is exactly what the rotation slot demands. PROPOSAL
  024's own probe report dropped "tournaments, matchmaking" as its round-2 candidate
  for being game-adjacent; round 3 takes the genuinely fleet-external half of that
  space (seeding fairness under a committed statistical model — knowledge, not a
  matchmaking feature), and the tree-wide sweep confirms the gap: `rg -i
  'bradley|terry|seeding|bracket|knockout|single.elim'` (bootstrap.py and .substrate
  excluded) hits only mechanical uses — "bracketed" as a verb in sim prose, 3D-printed
  mounting brackets in the maker files, repo "seeding" — zero competition-format
  content.
- Runners-up this slice, deduped and dropped: apportionment paradoxes (Alabama-paradox
  frequency, Hamilton vs divisor methods) — clean but PROPOSAL 017 already occupies
  the voting/appointment neighborhood, weakening the "third domain" claim; and
  spaced-repetition interval schedules under exponential forgetting — viable, but its
  natural decision rule compares two families with no folk-belief anchor, so the
  reader-consequence story is weaker than the bracket head's (every organizer already
  ships the folk default).

## Model basis (declared model-dependence — the P024 discipline)

This verdict's numbers are CONDITIONAL on an embedded model, named up front:

- **(1) Behavioral/statistical assumption:** Bradley–Terry pairwise win probabilities
  p_ij = s_i/(s_i+s_j) with strengths COMMITTED per profile, constant across rounds,
  independent matches, no draws. The measured gaps are properties of THIS model on
  THESE four strength shapes — the profiles are dials spanning the shape space, not
  measurements of any real league.
- **(2) Single most-likely-to-flip alternative:** an upset-heavy non-Bradley–Terry
  model (e.g. a floor on upset probability regardless of strength gap, or
  round-dependent strengths — fatigue/momentum), under which the value of "protection"
  changes and the argmax bracket can move; a softer flip is the OBJECTIVE itself — an
  organizer maximizing expected match competitiveness or total spectator value instead
  of (a)/(b) is outside this verdict's registered scope, and the verdict must say so.

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe
> battery). Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide
> competition-format sweep above returned zero domain hits; PROPOSALs 001–027 re-read
> at HEAD `3978df1` before drafting. (b) **kill test NOT triggered** — no prior
> proposal, idea file, or session-card 💡 touches seeding, bracket design,
> Bradley–Terry, or tournament-format fairness; this is round 3's unrelated-domain
> slot and differs from BOTH prior occupants (P017 social choice, P024 routing
> games). (c) **feasibility arithmetic checked** — 315 brackets × 4 profiles × a
> recursion of a few hundred exact-Fraction ops (Arm A), plus 315 × 4 × 128
> outcome paths (Arm B) ≈ 2×10⁵ short products: seconds to low minutes in pure
> CPython, no dependencies.

**1. What is this really?** A pre-registered MEASUREMENT settling whether the
universal folk default of tournament seeding is exactly optimal, approximately optimal,
or measurably suboptimal for its own two stated goals — by exhaustively evaluating ALL
315 possible 8-team brackets under a committed Bradley–Terry model, in exact rational
arithmetic, against bands fixed before any code runs. The sim constructs its entire
world from the pinned constants in this file — the cleanest hermetic shape the
unrelated-domain lane has produced: zero repo reads, zero network, zero RNG, zero
floats.

**2. What is the possibility space?** (i) Don't run it — the round-3 unrelated-domain
slot goes unserved and ORDER 004 rule 3 is dead letter this cycle. (ii) Re-use a prior
round's domain — fails the owner's "rotate" ask (P017 social choice, P024 routing).
(iii) A literature summary ("Horen–Riezman say no seeding is universally optimal") —
not falsifiable here and not the pipeline's product; the open question is the CONCRETE
gap on committed profiles, which only enumeration answers. (iv) Monte-Carlo simulate
the tournament — strictly worse than exact recursion at n=8 (sampling error where a
closed rational exists). (v) This head: exhaustive 315-bracket census × 4 committed
profiles, dual independent exact algorithms, bands registered first. (vi) Over-scope
(16/32 teams, reseeding after each round, best-of-k series, draw-lottery formats) —
16 teams already means 16!/2¹⁵ ≈ 638M brackets (needs argmax search, not census); the
8-team census is exactly where the folk belief is canonical and the answer complete;
extensions are natural follow-up heads if this lands APPROVE.

**3. What is the most advanced capability reachable by the simplest implementation?**
One ~250-line stdlib file: a bracket is a nested pair of pairs; canonicalization is a
recursive min-sort; the census is a set over 8! permutations (self-checked to
315 × 128); the winner-distribution recursion is ~15 lines; Arm B is a 128-path
product loop. That single file yields the EXACT optimality gap of the world's default
seeding policy — a publication-grade quantitative answer (every number a rational, no
error bars at all) to a question folk wisdom has treated as settled for a century,
from a sim a verdict session can run cold in minutes.

**4. What breaks it? (assumptions made explicit)** (a) **The model is a model** —
Bradley–Terry with committed strengths is the standard neutral choice, not a measured
league; that is exactly why FOUR shape-spanning profiles are swept, why the straddle
is a pre-registered NULL, and why the `## Model basis` note names the upset-floor
alternative and the objective-choice flip. (b) **Profile choice could cherry-pick** —
profiles are committed in this file BEFORE any code, span even/geometric/top-heavy/flat
shapes, and the decision bands quantify over ALL of them (REJECT needs exact optimality
in all four; APPROVE needs materiality in ≥ 1 — stated, symmetric, unmovable after
registration). (c) **Ties in the argmax** — Δ uses max-minus-standard, well-defined
under ties; standard's RANK is reported with ties counted, and Δ = 0 (exact) is the
only optimality claim. (d) **Algorithm bugs** — two structurally independent exact
algorithms must agree to rational EQUALITY on every cell, plus the partition audit,
sum-to-1, flat-control closed forms, and relabeling invariance; a single inequality
invalidates the run.

**5. What does it unlock?** The pipeline's THIRD fleet-external verdict and the
rotation lane's proof it spans domains (voting → routing → tournament design); a
measured, citable data point the owner can deploy whenever "the bracket protects the
best team" comes up (it is either exactly true, approximately true with a pinned gap,
or measurably false with a better bracket attached); and on APPROVE a follow-up family
(16-team argmax search, reseeding formats, objective trade-off frontiers) for future
rotation slots.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing external — by
design: no repo, no network, no dataset, no RNG; every fixture (topology, profiles,
bands) is stated in this file and committed as a small JSON alongside the sim. Kill
tests, run live this slice: a prior competition-format head anywhere in the tree (NOT
found — sweep empty); an occupied round-3 slot with THIS domain (NOT found — P017/P024
are different domains); infeasible runtime (NOT found — arithmetic in the preamble,
minutes in pure CPython). Sim-worthy or judgment-only: sim-worthy — the entire question
is a computable set of exact rationals against pre-registered thresholds; the one
judgment question (are 0.5 pp / 1.0 pp the RIGHT materiality lines?) is pinned by
pre-registration and stated as the thing a reader may dispute — about the bands, never
about the measured numbers.

**7. Which lane should build it — and what does it displace or duplicate?** sim-lab
runs it (its harness, its verdict grammar; the sim file + fixture JSON committed in its
sims/ tree per convention). No fleet lane consumes the verdict as a build input — the
consumer is the owner/manager as READERS (plus, incidentally, any future fleet feature
that ever DOES run a seeded bracket, which would inherit the table for free). Duplicates
nothing: the domain sweep found zero prior competition-format art in this tree, and no
sim-lab verdict through the current ledger touches tournament design.

**8. What is the smallest shippable slice?** One sim-lab intake dir: one stdlib file
(canonical bracket census + Bradley–Terry winner-distribution recursion + independent
path-enumeration arm + self-checks), one fixture JSON ({strength profiles F0–F4, band
constants 1/200 and 1/100, tree topology}, values copied verbatim from this file), one
results table {per profile: P_best(standard), max/argmax/rank, Δ_a; P_12(standard),
max/argmax/rank, Δ_b; reporting legs} ending in exactly one of APPROVE / REJECT / NULL
per the pre-registered rule — reproducible from the fixtures alone, byte-identical on
re-run BY CONSTRUCTION (exact rationals, no RNG, no floats, platform-independent), no
flags.

**Recommendation: sim-ready** — the question is crisp and completely computable, the
bands and decision rule are registered above BEFORE any code exists, both genre failure
modes are pre-empted (model-dependence → four committed shape-spanning profiles + the
`## Model basis` declaration + a NULL band; algorithmic error → dual independent exact
algorithms gated on rational equality plus five committed self-checks), and the verdict
changes what a reader may cite in every branch. THE ONE QUESTION for the simulator:
*Under the pinned Bradley–Terry model (p_ij = s_i/(s_i+s_j), committed strictly
decreasing integer strength profiles F1 linear (8..1), F2 geometric (128..1), F3
top-heavy (100,8,7,6,5,4,3,2), F4 near-flat (107..100); matches independent, strengths
round-constant, no draws), is the standard 8-team single-elimination seeding — the
bracket class of (1,8,4,5 | 3,6,2,7) — EXACTLY optimal among ALL 315 distinct bracket
assignments (8!/2⁷, canonical-census self-checked to 315 classes × 128 preimages) for
(a) P(team 1 wins the tournament) and (b) P(the final is 1-vs-2), measured per profile
as exact-rational gaps Δ_a and Δ_b (max over brackets minus standard, computed by the
winner-distribution recursion AND independently by 2⁷-path enumeration with exact
equality required on every cell, zero RNG/floats/seeds — the P027 seed-registry
high-water 20260755 explicitly untouched) — landing (evaluated in this order) REJECT
("folk belief exactly right") iff Δ_a = 0 AND Δ_b = 0 in all four profiles, APPROVE
("bracket audit warranted") iff Δ_a ≥ 1/200 in ≥ 1 profile OR Δ_b ≥ 1/100 in ≥ 1
profile, or NULL (the straddle: suboptimal somewhere but every gap sub-material — the
exact gap table is the citable pin and neither camp may cite "settled")?* Done-when:
the committed stdlib sim + fixture JSON ({profiles, bands, topology}, values verbatim
from this file) reproduce the full per-profile results table {P_best and P_12 for the
standard bracket, the per-objective max/argmax/rank over all 315, Δ_a, Δ_b, the F0
flat-control identities, the reporting legs (worst bracket, objective-argmax
disagreement, distribution quartiles)} byte-identically on re-run (exact rationals,
platform-independent, no CPython version sensitivity), every gate passes (Arm A ≡ Arm B
rational equality on all cells, 315 × 128 partition audit, sum-to-1, flat-control
closed forms, relabeling invariance), and the verdict issues exactly ONE of
APPROVE/REJECT/NULL per the pre-registered rule — stating the model-basis caveat
(Bradley–Terry on committed profiles; the upset-floor model and the objective-choice
flip named) and the n=8-single-elim boundary (reseeding formats and larger fields out
of scope by design, named as follow-ups); honest-null explicit: a NULL lands as a
finalized verdict pinning the exact gap table, not a re-run request.
