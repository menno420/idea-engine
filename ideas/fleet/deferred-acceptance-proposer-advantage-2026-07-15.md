# Who asks, wins: the deferred-acceptance proposer advantage is not a tie-break, it is a market-size-born rank tax the receiving side pays — and it lives entirely on the markets with more than one stable outcome

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 COMPLETELY-UNRELATED-domain slot, round 13 closer; a THIRTEENTH fleet-external domain: two-sided matching / the Gale–Shapley deferred-acceptance mechanism (cooperative market design), disjoint from the twelve prior occupants — social choice (P017), congestion routing (P024), tournament seeding (P028), pattern races (P032), optimal stopping (P036), spatial self-organization (P040), queue discipline (P044), stochastic ratchets (P048), occupancy & collection (P052), random incidence (P056), repeated games & reciprocity (P060), information cascades (P064) — and deliberately NOT adjacent to the last unrelated slot's cascades/observational-learning domain (P064): this head prices a cooperative one-shot mechanism with no signals, no sequential inference, and no herd)
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264 pipeline; routing is the manager's per Q-0260, this repo never edits sim-lab files)
> **Grounding:** https://github.com/menno420/idea-engine@1f304b0b163832191271a6be0f86bc9be7c83756 · fetched 2026-07-15T06:40:20Z
> (the dedup-sweep HEAD, the only read this head takes; every model constant below is invented-but-pinned in this file, and the DECISION arms are a full exact census with zero repo/network reads at verdict time — the P017–P064 hermetic precedent)
> **Origin:** standing ORDER 003 (continuous new ideas per repo) under ORDER 004 rule 3 (deliberate lane rotation, "COMPLETELY UNRELATED domains — I want those too"); round 13 served fleet backlogs (P065 #428), venture (P066 #429) and game mechanics (P067 #430, merged 06:26:58Z), so this head is the round-13 UNRELATED closer. Slot spacing history P056, P060, P064 → P068 (spacing 4) confirms the placement.

**Placement note (decide-and-flag):** this fleet-external pure-mechanism head lives in `ideas/fleet/` per the `check_sections` carve-out for cross-cutting heads — flagged rather than silently squatting, exactly as PROPOSALs 017, 024, 028, 032, 036, 040, 044, 048, 052, 056, 060 and 064 did.

## The folk belief

"Once you insist on a STABLE outcome, the market is essentially pinned — a stable matching is a stable matching, and it doesn't much matter how you get there or which side runs the process. Requiring stability treats both sides symmetrically, so being the one who 'asks' versus the one who 'is asked' is at most a tie-break." This is the intuition behind treating deferred acceptance as a neutral clearing procedure: college admissions, residency matches, kidney exchange, dating-app rankings, job markets, even fleet task-to-worker assignment all invoke "we just find a stable matching" as though the requirement determines the result. The popular reading quietly assumes what it needs to prove: that the stable set is (almost always) a single point, so that no degree of freedom survives for the algorithm to spend.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

It is not a single point, and the freedom that survives is spent ENTIRELY in the proposing side's favor. Let n agents on each side (call them proposers and receivers) hold strict complete preferences over the other side. The stable matchings of such a market do not form a shapeless set: they form a DISTRIBUTIVE LATTICE (Conway/Knuth), and its two extreme points are exactly opposed — the proposer-optimal stable matching gives EVERY proposer their best achievable stable partner and simultaneously gives EVERY receiver their WORST, and the receiver-optimal one flips both. Gale–Shapley deferred acceptance run with a given side proposing lands EXACTLY on that side's optimal corner. So the "neutral clearing procedure" is a choice of corner, and the corners are as far apart as the lattice allows. Three consequences make this a MECHANISM problem and not a footnote. (1) POLARIZATION — the proposing side's gain is the receiving side's loss, agent by agent, in ordinal rank; there is no Pareto ambiguity in the choice of side. (2) The advantage is MARKET-SIZE-BORN, not constant — averaged over uniform random preferences the mean proposer-partner rank and mean receiver-partner rank pull apart as n grows (the classic asymptotic: a uniform-random market gives proposers an expected partner around their ln n-th choice and receivers around their n/ln n-th), so a bigger market makes the side you are on matter MORE, not less. (3) The advantage is SELF-ENFORCING on one side only: deferred acceptance is strategy-proof for the PROPOSING side (Dubins–Freedman / Roth — no proposer can ever gain by misreporting), but NOT for the receiving side (Roth's impossibility: no stable mechanism is strategy-proof for both), so the receiving side is both worse off AND exposed to manipulation. Drafting found three hand-checkable structure facts that the sim must confirm as gates and that are the whole story of WHERE the advantage lives: (i) POLARIZATION as above — an exact per-profile identity checked against every stable matching; (ii) GAP-LOCALIZATION — on the markets with a UNIQUE stable matching the side-advantage is EXACTLY ZERO (both procedures return the same matching, so the folk belief is precisely, exactly right there), and the entire averaged advantage is concentrated on the markets with two or more stable matchings — a knife-edge: the mechanism has leverage ONLY off the singleton set; (iii) STRATEGY-PROOFNESS ASYMMETRY — proposer-side manipulation count is exactly ZERO over the whole census, receiver-side is strictly positive, and the receiver-side manipulability is itself market-size-born (zero at n = 2, positive at n = 3). Whether the shipped "stability pins it, side is a tie-break" reading is actually true (the market IS almost always a single point, gap ≈ 0), and if not, how big the proposer's tax is and where it physically lives — all of it is exactly computable: the whole object is a finite exact census over strict preference profiles, every metric an exact `fractions.Fraction`, no simulation error, no seed. The always-clean surprise from drafting: the ENTIRE averaged gap is a conditional-expectation-times-a-frequency product — advantage(n) = P(multiple stable matchings at n) × (mean advantage GIVEN multiplicity) — with the first factor the folk belief's own blind spot and the second a near-constant "one full choice-level" at n = 3.

## Pinned model (committed constants — all invented-but-pinned, exact rationals)

- A market is (n, men-prefs, women-prefs): n "men" (proposers) and n "women" (receivers), each with a STRICT COMPLETE ranking of the other side (1 = top choice). "Men propose" is the labelled proposing side; the census is symmetric under the men↔women relabelling, and an in-sim SYMMETRY gate certifies every published aggregate is relabelling-invariant.
- Uniform profile space: at size n each side-agent's ranking is one of the n! permutations, all (n!)^(2n) profiles equally weighted. Decision cell **n = 3** (full exhaustive census, 6^6 = 46,656 profiles); control cells n = 1 (degenerate) and n = 2 (full 16-profile hand census); growth cells n ∈ {4, 5, 6} (Arm R, reporting-only — the profile space (n!)^(2n) is astronomical, so these are sampled, never gated).
- Gale–Shapley: men-proposing deferred acceptance returns the man-optimal stable matching μ_M; women-proposing returns the woman-optimal μ_W. The full stable set S is obtained INDEPENDENTLY by exhaustive stability testing of all n! perfect matchings (a matching is stable iff no (m, w) pair mutually prefers each other to their assigned partners) — never via GS, so GS's optimality is a checked claim, not an assumption.
- Partner rank: for an agent matched to partner x, rank = 1-indexed position of x in the agent's ranking (1 = top). Random-partner baseline rank = (n + 1)/2 (= 2 at n = 3).
- Metrics, all exact `Fraction`: proposer-side mean rank P̄(n) = E[man rank in μ_M] (= E[woman rank in μ_W] by symmetry); receiver-side mean rank R̄(n) = E[woman rank in μ_M] (= E[man rank in μ_W]); the SIDE-GAP Δ(n) = R̄(n) − P̄(n) ≥ 0; the MULTIPLICITY fraction f(n) = P(|S| ≥ 2); the expected stable-set size E|S|(n); the conditional gaps Δ(n | unique) and Δ(n | multi); proposer-side manipulation fraction M_prop(n) = P(some proposer has a profitable misreport under men-proposing DA, others fixed); receiver-side manipulation fraction M_recv(n) likewise; the independent-market benchmark (mean rank if each agent were assigned a uniform-random partner = (n + 1)/2, reporting-only).
- Arm A (the DECISION arm, seedless): exhaustive exact-`Fraction` census at n = 1, 2, 3 — for every profile: men-proposing GS → μ_M, women-proposing GS → μ_W, full stability enumeration → S, all metrics accumulated as exact rationals; byte-identical across process runs. Runtime bounded: the full n = 3 census is ~6 s single-threaded, stdlib only (measured at drafting).
- Arm B (twin, seedless): an INDEPENDENTLY-WRITTEN recomputation of every n = 3 metric — the extremal stable matchings taken as the lattice bottom/top of the ENUMERATED stable set (min/max by the men's rank vector), never by running GS; must reproduce every Arm-A number EXACTLY; plus the algorithm-free hand census: exhaustive enumeration of all 16 profiles at n = 2, equal to both arms exactly.
- Arm R (seeded, REPORTING-ONLY): Monte-Carlo over n ∈ {4, 5, 6} — per episode: draw 2n uniform-random rankings (pinned draw order: all n men then all n women, each a Fisher–Yates shuffle), run GS both ways plus a bounded stability enumeration (n ≤ 6 → ≤ 720 matchings), estimate Δ(n), f(n), M_recv(n); 200,000 episodes per size on `random.Random(20261600)`; stability leg `random.Random(20261601)` at 40,000; presentation shuffle 20261602. Draw counts (2n shuffles per episode) counted and asserted. NO statistical gate rides Arm R — an MC estimate of the GROWTH trend is a named finding, never a ruling; the decision lives entirely at the exact n ≤ 3 cells.
- Aux seed: 20261603, reserved, never read by any leg (the P054–P067 aux convention).
- Seeds 20261600–603 allocated from 20261600 per the coordinator relay: 20261590–593 are P067/V080's registered set and the gap 20261594–599 is the disclosed in-flight buffer, so 20261600 is the next free index — strictly above both. Boundary-aware sweep — regex `(^|[^0-9])2026[0-9]{4,6}([^0-9]|$)` over this tree at HEAD 1f304b0 confirms the standalone numerals 20261664 / 20261833 / 202670087 are digit-substrings (Fraction numerators, results-JSON decimals), data not seeds — the P046–P067 sweep-recipe trap re-confirmed.

## Pre-registered decision rule (evaluation order: REJECT first)

- **REJECT** — "stability does NOT pin the outcome: which side proposes materially decides partners, the proposing side captures a systematic ordinal advantage the receiving side pays, and the receiving side is additionally exposed to manipulation the proposing side is not — so codifying deferred acceptance as a 'neutral clearing procedure' hides a directional, market-size-born tax": at the decision cell (n = 3), Δ(3) ≥ 1/5 exact, AND f(3) ≥ 1/5 exact, AND the strategy-proofness asymmetry has bite — M_prop(3) = 0 EXACTLY and M_recv(3) ≥ 1/100 exact. (Checked FIRST because the costly direction is fleet-wide: any surface that "just finds a stable/consistent assignment" and treats the running side as neutral — worker-to-task assignment, reviewer-to-PR matching, any two-sided clearing — silently hands the running side the optimal corner and the other side the pessimal one, and calling it neutral ships a directional bias as fairness.)
- **INVALID** (controls misbehaving — report, no ruling): any F1–F6 gate failure below.
- **APPROVE** — "the folk belief holds: the stable set is essentially a point, side is a tie-break": Δ(3) ≤ 1/20 AND f(3) ≤ 1/20. (Mutually exclusive with REJECT by arithmetic on both clauses.)
- **NULL** — anything else; pre-registered axes: band-straddle (Δ(3) ∈ (1/20, 1/5), or f(3) ∈ (1/20, 1/5), or the manipulation-asymmetry clause alone fails — the finding is the exact P̄/R̄/f/manip numbers with the decision cell named); polarization-theorem failure without gate failure (some stable matching beats μ_M for a man, or beats μ_W's pessimality for a woman, while F1–F6 pass — the drafter's lattice claim is wrong and the corrected structure is the finding); gap-localization failure without gate failure (Δ(3 | unique) ≠ 0 exactly — the "leverage lives only off the singleton set" claim is wrong, corrected law is the finding); strategy-proofness-asymmetry failure (M_prop(3) > 0, contradicting Dubins–Freedman — the model or claim is mis-specified, the corrected count is the finding); twin-arm disagreement surviving the INVALID diagnosis.

GATE POWER, computed at registration for a correct implementation (the V065/V067 lesson, applied): the sim is FULLY DETERMINISTIC at every decision cell — every decision clause and every F-gate is an exact-rational identity, an exhaustive-census count, or a byte comparison; the only seeded arm is reporting-only with NO statistical gate (its sole gates are the draw-count sentinel and exact reproducibility, pass probability 1 for a correct implementation); JOINT pass probability across all gates for a correct implementation = 1 EXACTLY (the P059–P064 no-stochastic-gate precedent: determinism proven by byte-identical re-run, not estimated), and decision separation is noise-free exact arithmetic — the disclosed landing clears the Δ band at 1.30×, the f band at 1.31×, and the M_recv band at 1.85×, so the ruling cannot move except via a mis-implemented model, which the anchor gates catch as INVALID.

## Gates (run INVALID on any failure)

- **F1 — GS & stability identities:** the stability test re-derived in-sim (a matching is stable iff it admits no blocking pair); GS output is stable at every profile; the men↔women relabelling SYMMETRY gate (the relabelled census reproduces every published aggregate); every rank ∈ [1, n]; the random-partner baseline = (n + 1)/2 exactly.
- **F2 — the three structure theorems, exact at every census cell:** (a) POLARIZATION — for every profile and every stable matching μ: every man weakly prefers μ_M to μ (rank_m(μ_M) ≤ rank_m(μ)) AND every woman weakly prefers μ to μ_M (rank_w(μ) ≤ rank_w(μ_M)); symmetrically for μ_W; hence μ_M = men-optimal + women-pessimal, μ_W its mirror. (b) GAP-LOCALIZATION — Δ(n | unique) = 0 EXACTLY (on |S| = 1 profiles μ_M = μ_W and the side-means coincide by symmetry) and the total gap equals f(n) · Δ(n | multi) exactly. (c) STRATEGY-PROOFNESS ASYMMETRY — M_prop(n) = 0 exactly at every census cell (Dubins–Freedman), M_recv(2) = 0 and M_recv(3) > 0 (Roth, market-size-born). Hand proofs pinned in the mechanism section.
- **F3 — closed-form / census anchors (reference values, exact):** at n = 3 — P̄ = 35/24, R̄ = 371/216, Δ = 7/27, f = 131/486, E|S| = 5027/3888, Δ(3 | multi) = 126/131, unique fraction = 355/486, M_prop = 0, M_recv = 1/54; at n = 2 — P̄ = 5/4, R̄ = 11/8, Δ = 1/8, f = 1/8 (= 2/16), E|S| = 9/8, M_prop = M_recv = 0; at n = 1 — Δ = 0, f = 0, E|S| = 1 (a single agent per side, the one matching, no freedom).
- **F4 — the hand world:** the two n = 2 multi-stable profiles named and walked by hand — men (w0 > w1, w1 > w0), women (m1 > m0, m0 > m1) has exactly two stable matchings {(m0,w0),(m1,w1)} and {(m0,w1),(m1,w0)}, men-proposing lands the first (each man's top), women-proposing the second (each woman's top) — plus its relabel-mirror, giving f(2) = 2/16 = 1/8 by a pinned pencil count over all 16 profiles.
- **F5 — the common-preference degeneracy:** if all men share one identical ranking OR all women share one identical ranking, the stable matching is UNIQUE (serial dictatorship of the agreed order) — Δ = 0 and f = 0 on that profile slice exactly; a control that the gap is a preference-DIVERSITY effect, not an artefact of the metric.
- **F6 — battery:** Arm B reproduces every Arm-A number exactly; the 16-profile exhaustive census at n = 2 equals both arms exactly; μ_M / μ_W equal the enumerated stable set's men-rank min / max at every n = 3 profile (GS-lands-the-corner, checked not assumed); twin independently-written decision evaluators agree on the ruling token; Arm-R draw-count sentinels (2n shuffles per episode) counted and asserted; aux seed 20261603 never read; stdout + results.json byte-identical across two process runs (Arms A/B platform-independent exact rationals; Arm R pinned to a stated CPython minor).

## Expected landing (DISCLOSED per the P048–P064 exact-arm norm)

REJECT, at the drafter's exact census values (the sim re-derives everything from scratch and must not trust these; these were computed at drafting by a full stdlib census, both arms agreeing): decision cell **n = 3** — P̄ = 35/24 ≈ 1.458333, R̄ = 371/216 ≈ 1.717593, so the SIDE-GAP Δ(3) = 7/27 ≈ 0.259259 ≥ 1/5 (1.30×); multiplicity f(3) = 131/486 ≈ 0.269547 ≥ 1/5 (1.31×); manipulation asymmetry M_prop(3) = 0 EXACTLY and M_recv(3) = 1/54 ≈ 0.018519 ≥ 1/100 (1.85×) — all three REJECT clauses clear. The gap-localization discovery: Δ(3 | unique) = 0 exactly and Δ(3 | multi) = 126/131 ≈ 0.961832, so the ENTIRE averaged advantage is the product f(3) · Δ(3 | multi) = (131/486)·(126/131) = 7/27 — on a market with a unique stable matching (355/486 ≈ 73.0% of all n = 3 markets) the folk belief is EXACTLY right and side is genuinely immaterial; on the 27.0% with multiple stable matchings the proposer's advantage is nearly a FULL choice-level (0.96 rank positions). The market-size story, two EXACT points: Δ(2) = 1/8 = 0.125 < Δ(3) = 7/27 ≈ 0.259 and f(2) = 1/8 < f(3) = 131/486 and M_recv(2) = 0 < M_recv(3) = 1/54 — the advantage, the multiplicity, and the receiver-side manipulability ALL grow from n = 2 to n = 3, and Arm R is expected to continue the rise toward the classic ln n vs n/ln n asymptotic (reporting-only). Falsifiability is real on every clause: the **n = 2** cell lands Δ = 1/8 ∈ (1/20, 1/5) AND f = 1/8 ∈ (1/20, 1/5) AND M_recv = 0 (asymmetry clause fails) — one market-size step DOWN and the ruling is band-straddle NULL, the advantage is genuinely market-size-born; and APPROVE was arithmetically LIVE until the census existed — 73% of n = 3 markets ARE side-neutral, so the averaged gap could have fallen below 1/20 (it does not, but the folk belief being right on nearly three-quarters of markets is exactly why "stability pins it" is a plausible-but-false intuition). Disclosed sharpenings, reporting-only: the independent-market benchmark — a uniform-random partner scores mean rank 2 at n = 3, so BOTH sides beat random (matching adds value), but the proposer's 1.458 is materially better than the receiver's 1.718; the polarization corollary — there is no profile where the proposing side helps a receiver on net, the choice of side is a pure ordinal transfer; the strategy vulnerability — a receiver's profitable misreport is always a truncation/reorder that triggers a different stable matching, never available to a proposer.

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

Fleet-external head: no lane CONSUMER; the deliverable is a citable measured verdict feeding the rotation lane's domain-coverage proof (a thirteenth domain) plus a transferable mechanism-design correction. REJECT → the "neutral clearing procedure" framing retires with numbers and the correction ships in two lines: (1) any two-sided clearing surface that runs a deferred-acceptance-style procedure and calls the result "the" stable outcome is spending a real degree of freedom in the RUNNING side's favor — name the side, and if fairness across sides is the goal, either alternate the proposing side, use a median/egalitarian stable matching, or disclose the directional advantage rather than laundering it as neutrality; (2) the running side is strategy-proof and the other side is not, so the other side's reports are gameable — do not treat both sides' submitted preferences as equally trustworthy signal. The GAP-LOCALIZATION theorem is the transferable design lens: the mechanism's entire leverage lives OFF the singleton set — where the stable outcome is unique the choice of side is provably free, so an audit should first measure P(multiple stable outcomes) before pricing any side-neutrality claim; a market that is almost always single-valued (highly correlated preferences) genuinely IS side-neutral, and one that is not is not, and the crossover is exactly f(n). APPROVE → the neutral-clearing default gains a measured basis and the side-alternation machinery ships as the priced non-fix. NULL → the named axis ships with the exact P̄/R̄/f/manip curves. Follow-ups named, none in scope: ties and incomplete lists (weak-stability variants, and rural-hospitals biting nontrivially when sides are unequal); correlated / common-value preferences (they shrink the stable set toward the singleton and shrink the gap — the F5 degeneracy is the extreme case); many-to-one markets (hospitals/residents — capacity changes the strategy-proofness details); cardinal-welfare re-weighting of the same matchings; the egalitarian/median stable matching as an explicit third mechanism.

## Dedup

Tree-wide `rg -i 'stable.match|gale.shapley|deferred.accept|matching.market|marriage.problem|roommate|two.sided|proposer|blocking.pair|lattice.of.stable'` (bootstrap.py/.substrate excluded) at HEAD 1f304b0: ZERO domain hits — every match is a word collision (`marriage.problem` appears ONLY inside the P036 secretary-problem dedup regex `ideas/fleet/secretary-rule-cardinal-regret-2026-07-13.md:206`; `proposer`/`matching` appear as ordinary prose in outbox summaries, never as this domain). sim-lab was READ-ONLY dedup-swept the same way in the P064 sweep this pipeline (same regex family) with no two-sided-matching content anywhere. No recorded drop of this domain exists on any card. No proposal P001–P067 and no verdict prices two-sided matching, deferred acceptance, stable-set structure, blocking pairs, or a market-clearing mechanism with opposed sides. Nearest priors argued distinct: **P064 → the cascade head** (the immediately-prior UNRELATED slot, deliberately avoided-adjacent: cascades price SEQUENTIAL Bayesian inference from observed ACTIONS under uncertainty about a hidden state — here there is NO hidden state, NO signals, NO sequential inference and NO learning; agents have fixed known preferences and the priced object is the CORNER a cooperative mechanism selects from a lattice), **P017 → the social-choice head** (aggregation RULES over fixed ballots — one-sided, no matching, no blocking-pair stability; the cascade-of-preferences-into-one-winner problem, not a two-sided assignment), **P044 → queue discipline** (waiting-time systems, no preferences, no two-sidedness), **P028 → tournament seeding** (a bracket over a fixed strength order — one-sided ranking, no market), **P036 → optimal stopping / secretary** (ONE decision-maker timing ONE hire on its own stream — the only place `marriage.problem` even appears, and it is the "secretary problem" nickname, a stopping rule with zero two-sided structure), **P060 → repeated reciprocity** (dyadic STRATEGIC payoff coupling in a repeated stage game — here the game is one-shot, cooperative, and the payoff is match rank against fixed preferences, no strategy space in the core object). Method kin only: the P028/P032/P036 fully-exact zero-RNG census discipline (exhaustive enumeration + exact rationals + a twin arm), reused as machinery on a new object (a stable-set census with a lattice-corner metric and a manipulation-asymmetry count — this head's own additions).

## Model basis (declared model-dependence — the P024 discipline)

Four modeling commitments carry the verdict, each pinned and directional: (1) STRICT COMPLETE preferences on EQUAL sides — the clean lattice and the polarization/gap-localization theorems take their exact form here; ties yield weak-stability variants (the extremal matchings need not be unique) and incomplete lists / unequal sides make the rural-hospitals theorem bite nontrivially (which agents go unmatched becomes the invariant) — both named follow-ups, and the theorems are stated as complete-strict-conditional. (2) UNIFORM profile weighting — the census weights all profiles equally; correlated / common-value preferences shrink the stable set toward a singleton (the F5 common-preference degeneracy is the extreme: f → 0, Δ → 0), so this head prices the DIVERSE-preference regime and says so — a market whose participants mostly agree genuinely is side-neutral, and the gap is a preference-diversity effect. (3) ORDINAL (rank) welfare — partner rank as payoff; cardinal-utility welfare re-weights the SAME matchings (a reporting flavor, never the decision — the polarization is ordinal and survives any monotone re-weighting). (4) ONE-TO-ONE (marriage) matching — many-to-one (hospitals/residents, schools/students) preserves proposer-side strategy-proofness but changes the receiving side's manipulation structure and the lattice details; named follow-up. The polarization theorem (F2a) is robust to (2), (3) and (4) — it is a lattice fact about the stable set of any strict-preference market, not a distributional or welfare fact.

## Probe report (v0, 2026-07-15)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide sweep
> `rg -i 'stable.match|gale.shapley|deferred.accept|matching.market|marriage.problem|roommate|two.sided|proposer|blocking.pair'`
> (bootstrap.py/.substrate excluded) at the grounding pin `1f304b0` returned zero
> domain hits (word collisions only: `marriage.problem` inside the P036 secretary
> dedup regex; `proposer`/`matching` as outbox prose). (b) **kill test NOT
> triggered** — no prior proposal P001–P067, idea file, or session-card 💡 prices
> two-sided matching, deferred acceptance, or stable-set structure; no recorded
> runner-up drop of this domain exists. (c) **feasibility + liveness arithmetic
> checked LIVE** — the n = 3 exhaustive census (46,656 profiles × GS both ways ×
> full stability enumeration) ran in ~6 s stdlib at drafting, both a forward-GS arm
> and an enumerate-then-take-lattice-extremes twin agreeing on every exact rational;
> expected landing DISCLOSED with its exact drafting-time values (REJECT, Δ = 7/27,
> f = 131/486, Δ|multi = 126/131, M_recv = 1/54) rather than hidden, all rulings
> reachable under the pre-registered rule, the n = 2 straddle NULL edge and the live
> APPROVE region (73% of markets side-neutral) both named, and the INVALID controls
> gated.

**1. What is this really?** A pre-registered EXACT MEASUREMENT of the folk claim
"stability pins the outcome — which side runs the clearing procedure is a tie-break",
taken where the claim actually lives: a two-sided market with strict preferences whose
stable matchings form a lattice, priced against the cheapest thing the folk belief
denies exists — a systematic, market-size-born ordinal advantage the proposing side
captures and the receiving side pays. On exact `fractions.Fraction` census arithmetic
the side-gap Δ(n), the multiplicity f(n), the conditional gaps, and the manipulation
asymmetry are all exact at every n ≤ 3 cell, judged against bands fixed before any
code (REJECT first: Δ(3) ≥ 1/5 AND f(3) ≥ 1/5 AND M_prop = 0 with M_recv ≥ 1/100;
APPROVE: Δ(3) ≤ 1/20 AND f(3) ≤ 1/20; NULL otherwise with named axes), byte-identical
across two runs, with the seeded growth trace demoted to reporting-only.

**2. What is the possibility space?** (i) Don't run it — the round-13 unrelated
closer goes unserved and the rotation lane's coverage claim stalls at twelve domains.
(ii) Re-use a prior round's domain — fails the owner's "rotate" ask; and re-using the
LAST unrelated slot's cascades domain would be the specific adjacency the coordinator
called out to avoid. (iii) A literature summary ("deferred acceptance favours the
proposing side — see Gale–Shapley 1962, Roth 1982") — retells the direction, measures
nothing against a pre-registered band, and misses what the exact treatment uniquely
gives: the GAP-LOCALIZATION theorem (the advantage is EXACTLY zero off the multi-
stable set) and the exact f · Δ|multi decomposition. (iv) An MC-only sim — leaves
every decision number seed-noisy when the n ≤ 3 object is exactly enumerable (the
V065/V067 lesson): the decision cells are a full exact census, MC is demoted to the
growth trend. (v) This head: exact census as the ruling, REJECT-first bands on gap +
multiplicity + manipulation asymmetry, INVALID on the F1–F6 identity/theorem/anchor/
degeneracy/battery gates, robustness disclosed via the n = 2 straddle edge and the
73%-side-neutral live APPROVE region. (vi) Over-scope (ties, incomplete lists, many-
to-one, correlated preferences, egalitarian stable matchings) — each named as a
follow-up, none in scope.

**3. What is the most advanced capability reachable by the simplest implementation?**
One ~220-line stdlib file: a blocking-pair stability test, a Gale–Shapley loop, and a
full-profile census loop — that single kernel yields the exact side-gap Δ(n), the
exact multiplicity f(n) and expected stable-set size, the conditional-gap
decomposition, all three structure theorems verified as THEOREM CHECKS rather than
estimates, the manipulation-asymmetry counts, and the independent-market benchmark —
from a sim a verdict session runs cold in seconds.

**4. What breaks it? (assumptions made explicit)** (a) **Strict complete preferences
are a choice** — ties and incomplete lists change the stable-set structure; the head
prices the strict-complete regime and names the variants as follow-ups; every theorem
is stated strict-complete-conditional. (b) **Uniform weighting is a choice** —
correlated preferences shrink the stable set toward the singleton and shrink the gap
(the F5 degeneracy is the extreme); the head prices the diverse-preference regime and
says so. (c) **Band placement could cherry-pick** — the 1/5 and 1/20 clauses on both
Δ and f, and the 1/100 manipulation clause, are committed BEFORE the sim, the expected
landing is DISCLOSED (REJECT), and the falsifiability is two-sided: the n = 2 cell
lands all three REJECT clauses UNDER threshold (Δ = f = 1/8 straddle, M_recv = 0), and
APPROVE was arithmetically live because 73% of n = 3 markets are genuinely side-
neutral. (d) **GS-lands-the-corner is a claim, not an axiom** — the sim takes the
extremal matchings from the ENUMERATED stable set independently and checks GS equals
them (F6), so a GS bug becomes an INVALID, not a silent wrong number. (e) **An
arithmetic slip in the drafter's hand facts** — the sim re-derives everything; all
three theorems are F2 gates AND carry their own theorem-failure-without-gate-failure
NULL axes, so a wrong hand claim becomes a finalized finding (the corrected law), not
a silent bad gate.

**5. What does it unlock?** The pipeline's THIRTEENTH fleet-external verdict and the
rotation lane's domain-coverage proof extended (voting → routing → tournaments →
pattern races → stopping → spatial self-organization → queueing → ratchets → occupancy
→ random incidence → reciprocity → observational learning → two-sided matching); a
measured, citable answer to "is a stable clearing procedure side-neutral, and what
does running it cost the other side" with three standalone side pins (the exact
f · Δ|multi decomposition showing the advantage lives ENTIRELY off the singleton set;
the market-size-born growth of gap, multiplicity, and receiver-manipulability across
two exact points; the strategy-proofness asymmetry as an exact census count); and a
transferable mechanism-design correction for anywhere the fleet "just finds a stable
assignment" and calls it neutral — name the running side, measure P(multiple stable
outcomes) first, and don't trust the non-strategy-proof side's reports as clean signal.

**6. What is the cheapest experiment that decides it?** The whole head IS the cheapest
deciding experiment: Arm A settles every decision number exactly in seconds with no
seed. The single cheapest probe if a reader doubts a specific leg is the n = 2 hand
census by pencil (16 profiles, exactly 2 of them multi-stable — the fully-opposed
configuration and its relabel-mirror — giving f(2) = 1/8, Δ(2) = 1/8, and both sides'
manipulation zero because a 2×2 market is too small to game), which anchors the census
machinery against a three-line hand count.

**7. What would make this a mistake to run?** If the exact census were unavailable (it
is not — the n = 3 space is 46,656 profiles, a few seconds), if the domain duplicated a
prior head (it does not — the sweep returned zero domain hits and no recorded drop
exists, and the domain is deliberately non-adjacent to the prior unrelated slot's
cascades), or if the disclosed REJECT made the run theater. It does not: the value is
the independent hermetic re-derivation of three known theorems PLUS the parts no
textbook states in this form — the exact f · Δ|multi decomposition, the exact
multiplicity 131/486 and conditional gap 126/131 at n = 3, and the market-size-born
growth across two exact points — and both non-REJECT rulings are genuinely reachable
(APPROVE was live at 73% side-neutral; the n = 2 cell is an actual NULL straddle one
size-step away).

**8. How will we know it worked?** A committed sim-lab report with: the exact P̄(n),
R̄(n), Δ(n), f(n), E|S|(n) at n = 1, 2, 3 (Fractions + float renderings), the
conditional gaps Δ(n | unique) = 0 and Δ(n | multi), the manipulation-asymmetry counts
M_prop = 0 / M_recv, the three theorem verifications, the independent-market benchmark,
the F1–F6 gate results, the verdict token against the pre-registered bands, Arm R's
n = 4/5/6 growth estimates beside the exact curves (reporting-only), and a byte-identity
note (two process runs identical). A clean run reproduces the drafter's disclosed
reference values (Δ = 7/27, f = 131/486, Δ|multi = 126/131, M_recv = 1/54) from scratch,
or — the more interesting outcome — DISAGREES and pins the drafter's error, which the
pre-registered rule then rules on honestly (the theorem-failure NULL axes exist for
exactly that).

**Recommendation: sim-ready**
