# IRV monotonicity in close races — how often does raising the winner make it lose?

> **State:** sim-ready
> **Class:** process (pipeline rotation — inbox ORDER 004 rule 3's COMPLETELY-UNRELATED-domain
> slot; the domain itself is social choice theory, fleet-external by design) ·
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous pipeline)
and ORDER 004 rule 3 ("Rotate lanes deliberately: … → COMPLETELY UNRELATED domains
(I want those too)") — PROPOSALs 013/014 were fleet-meta, 015/016 game mechanics; this
is the rotation's first unrelated-domain head. **Placement note (decide-and-flag):**
sections are roster-derived and inventing one ad hoc is forbidden (README § Sections;
`check_sections.py` reds an ORPHAN section against the live roster), and that checker's
own carve-out rules that sim-lab-shaped ideas "ride `ideas/fleet/` or the proposing
section" — so this fleet-external head lives here, flagged rather than silently
squatting.

## The idea (reasoned to its fuller form — Q-0254 duty)

Instant-runoff voting (IRV, "ranked-choice voting" in US usage) fails the monotonicity
criterion: there are elections where a group of voters, by RAISING the winner on their
ballots and changing nothing else, would cause that winner to LOSE (the "more-is-less"
paradox — promoting W to the top of some ballots strips first-round votes from the
voter's old favourite, changes who gets eliminated, and W then loses the new final
pairing). That this CAN happen is a theorem and is not in question. What is genuinely
contested is how OFTEN: defenders of IRV point at real-election audits and call
non-monotonicity a vanishing curiosity (documented real cases are rare — Burlington
2009 being the canonical specimen); critics' theory papers put the rate in COMPETITIVE
three-way races at 10%+ under standard voter models. Both camps are informed; they are
conditioning on different things (all elections vs close ones) and modeling voters
differently (impartial culture vs anonymous-profile counting). A smart reader can
honestly believe either "≪5% even when close — a footnote" or "double digits when it
matters — a first-order objection". This sim pre-registers the thresholds FIRST and
then measures both voter models on both conditionings, deterministically, in stdlib
Python — with an explicit intermediate band where the honest answer is "the claim is
model-dependent; neither side may cite this as settled".

**The sim (fully hermetic — every fixture is constructed by the sim itself, nothing
external):** three candidates {A,B,C}, six strict ballot types; an election is a
6-vector of type counts summing to n. IRV rule, pinned: round 1 eliminates the
candidate with the fewest first-place votes; the winner is the pairwise majority
winner of the remaining two on the full ballots; any exact tie (round-1 lowest tie or
final pairwise tie) EXCLUDES the election from numerator and denominator, counted and
reported separately (no tie-break artifacts). Upward-violation test, pinned: election
with IRV winner W exhibits a violation iff there exist a candidate X ≠ W, a ballot
type t ∈ {X≻W≻Z, X≻Z≻W} (Z the third candidate), and an integer k with
1 ≤ k ≤ count(t), such that converting exactly k ballots of type t to W≻X≻Z (raising
W to the top, preserving X≻Z) changes the IRV winner away from W — searched
exhaustively over X, t, k. Two arms: **Arm E (exhaustive, IAC)** — enumerate ALL
anonymous profiles (compositions of n into 6 parts, each equally likely) at n=25
(C(30,5)=142,506 profiles) with n=13 (8,568) as a size anchor; exact fractions, no
randomness at all. **Arm S (seeded Monte Carlo, IC)** — each voter's ballot uniform
over the 6 types: (n=99, M=200,000 elections, seed 20260713) primary; (n=1,001,
M=20,000, seed 20260714) size leg; `random.Random(seed)`, ballots drawn per-voter via
`rng.randrange(6)` in a pinned loop order; results table pins the CPython minor
version; byte-identical on re-run. A breakpoint-only k-scan optimization is permitted
iff it agrees with the exhaustive k-scan on a 1,000-election spot check (seed
20260715). Conditioning, pinned: **close** := round-1 elimination margin
(second-lowest minus lowest first-place tally) ≤ 5% of n. Metrics: V_all (violation
fraction, all non-tied elections), V_close (among close ones), tie fraction, and a
per-(X,t) breakdown of where violations are found.

**Pre-registered acceptance bands and decision rule** (set BEFORE any code runs; the
consequence of each outcome stated so the verdict is actionable, not trivia):

- **APPROVE** ("monotonicity risk is material in close races") iff V_close ≥ 0.10 in
  BOTH arms (Arm E at n=25 AND Arm S at n=99) AND V_all ≥ 0.01 in both.
- **REJECT** ("edge-case curiosity even when close") iff V_close < 0.05 in both arms.
- **NULL** otherwise (bands straddled, or the two arms disagree across a threshold) —
  a legitimate, reportable outcome: the finding is then "the material-risk claim is
  voter-model-dependent", stated with the per-arm numbers, and NO ruling issues.
- Size legs (n=13, n=1,001) are sensitivity reporting only — they cannot flip the
  decision, but a sign-flip across sizes must be flagged in the verdict.

**Consequence:** on APPROVE, any future memo, explainer, or venture-lab writeup that
touches ranked-choice adoption must carry non-monotonicity as a first-order QUANTIFIED
objection for competitive races, citing these rates; on REJECT, that objection is
demoted to a footnote (measured < 5% exactly where it was supposed to concentrate) and
may not be presented as a practical argument against IRV without new evidence; on
NULL, neither camp's soundbite may be cited as settled — the model-dependence itself
becomes the citable finding.

## Relations (adjacent heads — deliberately links, not duplication)

- vs the outbox (001–016): nothing adjacent by domain — 001–011 and 015–016 are fleet
  product/game-mechanics heads, 012–014 fleet-meta process sweeps. Nearest by METHOD
  only: PROPOSAL 012 (policy grid over traces, stdlib, deterministic) and 015
  (parameter sweep against pre-registered bands) — this head reuses the pre-registered
  band discipline but shares no domain, no fixture, no consumer with either. A tree-wide
  sweep (`rg -i 'voting|election|ballot|runoff|monotonicit|apportion'`, bootstrap.py and
  .substrate excluded) finds zero prior social-choice content anywhere in ideas/,
  .sessions/, or control/.
- The two shortlist runners-up this slice deduped and dropped: Hamilton-apportionment
  Alabama-paradox frequency (also clean, but its control arm is paradox-free by
  THEOREM, so half the sweep is a foregone conclusion) and bus-bunching
  headway-control (method-adjacent to PROPOSAL 012's policy-grid-over-traces shape —
  the weakest "completely unrelated" claim of the three).

## Probe report (v0, 2026-07-13)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe
> battery). Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide
> domain sweep above returned zero hits; PROPOSALs 001–016 re-read at HEAD `c99852c`
> before drafting. (b) **kill test NOT triggered** — no prior proposal, idea file, or
> session-card 💡 touches social choice, elections, or any non-fleet knowledge domain;
> this is the ORDER 004 rule-3 slot's first occupant. (c) **feasibility arithmetic
> checked** — Arm E is 142,506 profiles × ≤ ~100 O(1) IRV evaluations; Arm S primary is
> 200,000 × ≤ ~400 evaluations; both are minutes in pure CPython, no dependencies.

**1. What is this really?** A pre-registered measurement settling which of two live,
contradictory soundbites about IRV survives contact with exhaustive enumeration: "the
paradox basically never happens" vs "it happens in double digits exactly when races
are close". The sim constructs its entire world (ballot combinatorics) from integers —
the cleanest possible test of the pipeline's unrelated-domain rotation: zero repo
reads, zero network, zero fleet coupling in the eventual verdict session.

**2. What is the possibility space?** (i) Don't run it — the rotation slot goes
unserved and ORDER 004 rule 3 is dead letter this cycle. (ii) Pick a domain closer to
home (tournaments, matchmaking) — game-adjacent, and P015/P016 just covered game
mechanics; fails the owner's "completely unrelated" ask. (iii) A literature summary
instead of a sim — not falsifiable, not the pipeline's product, and the two camps'
numbers differ precisely because their models differ; only running both models under
one pre-registration resolves it. (iv) This head: one sweep, two voter models, two
conditionings, bands registered first. (v) Over-scope (4+ candidates, downward
paradoxes, truncated ballots) — each multiplies the state space; 3-candidate upward is
where the literature fight actually is, and extensions are natural follow-up proposals
if this verdict lands in the APPROVE band.

**3. What is the most advanced capability reachable by the simplest implementation?**
One ~200-line stdlib file: an election is 6 integers; IRV evaluation is a handful of
comparisons; the violation search is a bounded triple loop; Arm E's enumeration is
`itertools`-shaped compositions. That single file yields exact IAC fractions (no
sampling error at all in Arm E) plus seeded IC estimates with M large enough that the
band edges (5%/10%) sit many standard errors from plausible outcomes — a
publication-grade quantitative answer to a genuinely contested question, from a sim a
verdict session can run cold in minutes.

**4. What breaks it? (assumptions made explicit)** (a) **Voter models are models** —
IC and IAC are the two standard neutral cultures, not electorates; that is exactly why
BOTH arms must clear a band for a ruling, and why the straddle outcome is a
pre-registered NULL, not a judgment call. (b) **Single-type uplift definition** — the
violation search raises W on blocs of ONE ballot type at a time (the standard paradox
construction); mixed-type coalition raises could only find MORE violations, so V is a
lower bound and the verdict must say so (an APPROVE is safe; a REJECT rules on the
standard definition only — stated in the verdict). (c) **Tie handling** — exclusion is
pre-registered to avoid tie-break artifacts; the tie fraction is reported so a reader
can see what was excluded. (d) **PRNG stability** — `random.Random` sequences are
stable for a pinned CPython minor version; the results table pins it, and Arm E is
seedless by construction, so the headline IAC numbers are platform-independent exact
rationals.

**5. What does it unlock?** The pipeline's first fleet-external verdict — proof the
PROPOSAL→VERDICT loop produces citable knowledge with no repo coupling at all (the
purest test yet of the sim-lab harness); a measured, pre-registered data point the
owner can actually cite in any ranked-choice conversation; and, on APPROVE, a natural
follow-up family (4-candidate rates, downward paradoxes, real-ballot replays) for
future unrelated-domain rotation slots.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing external —
that is the design: no repo, no network, no dataset; every fixture (enumeration
bounds, seeds, M, n, band constants) is stated in this file and committed as a small
JSON alongside the sim. Kill tests, run live this slice: a prior social-choice head
anywhere in the tree (NOT found — domain sweep empty), an occupied ORDER 004 rule-3
slot (NOT found — 013/014 fleet-meta, 015/016 game mechanics), infeasible runtime
(NOT found — arithmetic in the preamble, minutes in pure CPython). Sim-worthy or
judgment-only: sim-worthy — the entire question is a computable fraction against
pre-registered thresholds; the one judgment question (are the 5%/10% thresholds the
RIGHT materiality line?) is pinned by pre-registration and stated as the thing a
reader may dispute — about the bands, never about the measured numbers.

**7. Which lane should build it — and what does it displace or duplicate?** sim-lab
runs it (its harness, its verdict grammar; the sim file + fixture JSON are committed
in its sims/ tree per its convention). No fleet lane consumes the verdict as a build
input — the consumer is the owner/manager as READERS, plus venture-lab IF its
writing-products ever want a worked example of pre-registered simulation (a
possibility, not a dependency). Duplicates nothing: the domain sweep found zero prior
art in this tree, and no sim-lab verdict through the current ledger touches any
non-fleet domain.

**8. What is the smallest shippable slice?** One sim-lab intake dir: one stdlib file
(election evaluation + violation search + both arms), one fixture JSON ({n, M, seed}
per arm + band constants, all values copied from this file), one results table
{V_all, V_close, tie fraction, per-(X,t) breakdown} × {Arm E n=13/25, Arm S
n=99/1,001} ending in exactly one of APPROVE / REJECT / NULL per the pre-registered
rule — reproducible from the fixtures alone, byte-identical on re-run, no flags.

**Recommendation: sim-ready** — the question is crisp and computable, the bands and
decision rule are registered above BEFORE any code exists, both failure modes of the
genre are pre-empted (model-dependence → dual-arm requirement + NULL band;
definition-dependence → lower-bound statement), and the verdict changes what a reader
may cite either way. THE ONE QUESTION for the simulator: *Under the pinned 3-candidate
IRV rule (plurality-loser elimination, pairwise final, exact ties excluded and
counted), what fraction of elections exhibit an upward monotonicity violation (∃ X≠W,
t ∈ {X≻W≻Z, X≻Z≻W}, 1 ≤ k ≤ count(t) such that moving k ballots of type t to W≻X≻Z
dethrones winner W) — measured as V_all and V_close (close := round-1 elimination
margin ≤ 5% of n) in BOTH Arm E (exhaustive IAC: all compositions at n=25, anchor
n=13 — exact fractions) and Arm S (seeded IC: n=99, M=200,000, seed 20260713 primary;
n=1,001, M=20,000, seed 20260714 size leg) — and does the result land APPROVE
(V_close ≥ 0.10 AND V_all ≥ 0.01 in both arms), REJECT (V_close < 0.05 in both), or
NULL (anything else — reported as model-dependence, no ruling)?* Done-when: the
committed sim + fixture JSON reproduce the results table {V_all, V_close, tie
fraction, per-(X,t) breakdown} across all four (arm, n) legs byte-identically, the
spot-check (seed 20260715) passes if the breakpoint optimization is used, the verdict
issues exactly one of APPROVE/REJECT/NULL per the pre-registered rule with the
lower-bound caveat (single-type uplift) and the CPython version pin stated, and the
size legs are reported as sensitivity with any sign-flip flagged.
