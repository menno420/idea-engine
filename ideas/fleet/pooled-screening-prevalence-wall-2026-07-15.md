# The pool test is not free: Dorfman batched screening has an exact prevalence wall (p\* = 1 − 3^(−1/3) ≈ 0.3066) above which every batch size loses to one-at-a-time testing — and the cautious pair-pool is dominated everywhere, so either batch ≥ 3 or don't batch at all

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 COMPLETELY-UNRELATED-domain slot, round 14 closer; a FOURTEENTH fleet-external domain: screening design / combinatorial group testing — Dorfman two-stage pooled testing (test economics against prevalence), disjoint from the thirteen prior occupants — social choice (P017), congestion routing (P024), tournament seeding (P028), pattern races (P032), optimal stopping (P036), spatial self-organization (P040), queue discipline (P044), stochastic ratchets (P048), occupancy & collection (P052), random incidence (P056), repeated games & reciprocity (P060), information cascades (P064), two-sided matching (P068) — and deliberately NOT adjacent to the last two unrelated slots' domains: no signals, no hidden state, no sequential inference and no herd (vs P064's cascades/observational learning), no two sides, no preferences and no market (vs P068's matching) — this head prices a one-shot test-economy DESIGN decision against an exogenous defect rate)
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264 pipeline; routing is the manager's per Q-0260, this repo never edits sim-lab files)
> **Grounding:** https://github.com/menno420/idea-engine@e17ebe7d733ecc431556b0e8e3d6788b27783b34 · fetched 2026-07-15T09:01:53Z
> (the dedup-sweep HEAD, the only read this head takes; every model constant below is invented-but-pinned in this file, and the DECISION arms are exact seedless arithmetic with zero repo/network reads at verdict time — the P017–P068 hermetic precedent; sim-lab dedup-swept READ-ONLY on a shallow clone @ bf398f91da63133d222c5afabcc15ac354e1e72c, VERDICT 083 newest, fetched 2026-07-15T09:08:22Z)
> **Origin:** standing ORDER 003 (continuous new ideas per repo) under ORDER 004 rule 3 (deliberate lane rotation, "COMPLETELY UNRELATED domains — I want those too"); round 14 opened at fleet backlogs (P069 #432), served venture (P070 #434) and game mechanics (P071 #435, merged 2026-07-15T08:55:30Z), so this head is the round-14 UNRELATED closer. Slot spacing history P056, P060, P064, P068 → P072 (spacing 4) confirms the placement.

**Placement note (decide-and-flag):** this fleet-external pure-mechanism head lives in `ideas/fleet/` per the `check_sections` carve-out for cross-cutting heads — flagged rather than silently squatting, exactly as PROPOSALs 017, 024, 028, 032, 036, 040, 044, 048, 052, 056, 060, 064 and 068 did.

## The folk belief

"Batching always saves work: pool the samples, test the pool, and only drill into the positives — one cheap test clears a whole batch. And if you're unsure about the defect rate, hedge with SMALL pools; a pair is the safest batch." This is the instinct behind every drill-down screening design: pooled blood tests, batched hardware QA, aggregate CI checks that bisect on red, grouped retests of flaky suites, one lint pass over a directory with per-file re-runs on failure. The instinct treats the pool test itself as approximately free ("it's just one more test") and treats batch size as a monotone dial — smaller is safer, bigger saves more when defects are rare. Both halves are load-bearing and neither is priced: if pooling always saves, batching needs no prevalence measurement first, and if a pair is the safe hedge, batch-of-2 is the natural cautious default.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

The two-stage cost law prices both halves exactly, and both are false in a structured way. Items are defective i.i.d. with prevalence p (q = 1 − p); a test on any subset reports perfectly whether the subset contains ANY defective. Dorfman two-stage screening with pool size n spends one test per pool, clears the whole pool on a negative, and retests all n members individually on a positive. Expected tests PER ITEM: **T(n, p) = 1/n + 1 − q^n** (individual testing is T(1) = 1 exactly). Everything this head registers flows from three exact structure theorems, each verified live at drafting. **T1 — the WALL.** Pooling at size n beats individual testing iff T(n, q) < 1 iff q^n > 1/n iff q > n^(−1/n). So the most forgiving pool size is the n minimizing n^(−1/n) — and on integers that minimum is n = 3, certified entirely by INTEGER-POWER comparisons (n^(−1/n) < m^(−1/m) ⟺ n^m > m^n): 3² = 9 > 8 = 2³, 3⁴ = 81 > 64 = 4³, 3⁵ = 243 > 125 = 5³, and (n+1)^n < n^(n+1) for every n ≥ 3, so n^(−1/n) is strictly increasing from n = 3 on. Hence pooling — at ANY size — helps iff q > 3^(−1/3), i.e. iff **p < p\* = 1 − 3^(−1/3) ≈ 0.306566**. Above the wall every pool size strictly loses (q < n^(−1/n) for all n forces T(n) > 1 for all n). The wall is not asymptotic hand-waving: at a rational prevalence the certificate is "is 3q³ > 1?", one exact multiplication. **T2 — the PAIR is never the answer.** The exact polynomial identity **T(2, q) − T(3, q) = (q − 2/3)²(q + 1/3) + 1/54** (verified at drafting by exact coefficient match AND by enumeration) says the pair-pool is strictly dominated by the triple at EVERY prevalence, with minimum gap exactly 1/54 attained exactly at q = 2/3 (p = 1/3) — a named knife-edge equality cell. The "cautious small batch" is never right: either batch ≥ 3 or don't batch at all. **T3 — the 2–4 DEGENERACY.** The companion identity **T(2, q) − T(4, q) = (q² − 1/2)²** says pool 4 weakly dominates pool 2 everywhere, with a genuine MARGIN-0 knife-edge at q² = 1/2 — and at that same point BOTH pools break even against individual testing simultaneously (q₂\* = q₄\* = 2^(−1/2), because 2⁴ = 4² — the unique integer coincidence in the n^(1/n) family). Anyone A/B-testing batch-of-2 against batch-of-4 near the break-even prevalence is measuring an exact zero. Below the wall the savings are real and large — at p = 1/100 the optimal pool is n\* = 11 and the cost is T\* ≈ 0.1956 tests/item (a 4/5 discount), with the small-p scaling T\* ≈ 2√p (reporting) — and the whole design collapses to one measurable number: the prevalence. The drafting surprise that makes this a mechanism head and not a formula recital: **the entire wall lives in the pool test's own 1/n cost** — delete that one term (the accounting slip the batching instinct actually makes: "the pool test is basically free") and T̃(n, p) = 1 − q^n < 1 for every n and every p < 1, so pooling looks like a free win everywhere and the wall vanishes. The folk belief is exactly the p → 0 limit of the true law plus one dropped term, which is why it feels self-evident and fails above p\*.

## Pinned model (committed constants — all invented-but-pinned, exact rationals)

- Items defective i.i.d. Bernoulli(p), prevalence p exact-rational; q = 1 − p. Tests are PERFECT (no false negatives/positives, no dilution) and report "does this subset contain ≥ 1 defective?".
- Protocol: Dorfman TWO-STAGE — stage 1: one test per disjoint pool of size n; negative pool clears all n items; positive pool sends all n items to individual retest (n further tests). Cost metric: T(n, p) = expected TESTS PER ITEM = 1/n + 1 − q^n for n ≥ 2; T(1) = 1 (individual baseline). Test count is the only cost (latency/sample-splitting named reporting, never decision).
- Grids: pool grid n ∈ {1..64} (practical sub-grid {2..8} for the damage clause); prevalence grid p ∈ {1/100, 1/50, 1/20, 1/10, 1/5, 1/4, 3/10, 1/3, 2/5, 1/2, 2/3, 9/10}; identity grid q ∈ {k/100 : k = 0..100} ∪ {2/3} (the appended point is the T2 equality cell). Decision cells: **p = 2/5** (wall cell) and **p = 1/100** (savings cell), plus the all-q identity clauses.
- Arm A (the DECISION arm, seedless): closed-form exact `fractions.Fraction` T(n, p) over the full grid; T1 wall certificates by exact integer-power comparison (3² > 2³, 3⁴ > 4³, 3⁵ > 5³, 2⁴ = 4², (n+1)^n < n^(n+1) for n ∈ {3..64}); T2/T3 identities by exact polynomial-coefficient expansion AND grid enumeration; optimal-n\* search by direct exact comparison. Byte-identical across process runs.
- Arm B (twin, seedless): an INDEPENDENTLY-WRITTEN outcome-tree recomputation — T(n, p) = (1/n) · Σ_{k=0..n} C(n, k) p^k q^(n−k) · cost(k) with cost(0) = 1 and cost(k ≥ 1) = 1 + n — must equal every Arm-A number EXACTLY on the full grid; plus an independent optimal-n\* search and an independent wall check (q^n vs 1/n directly, no certificate reuse).
- Arm R (seeded, REPORTING-ONLY): Monte-Carlo screening careers — populations of N = 100,000 items per cell at (p, n) ∈ {(1/100, 11), (1/10, 4), (2/5, 3)}, simulate the two-stage protocol, count actual tests, report beside the exact expectation; main leg `random.Random(20261640)`; stability leg `random.Random(20261641)` at N = 40,000; presentation shuffle 20261642. Draw counts (n Bernoulli draws per pool) counted and asserted. NO statistical gate rides Arm R — the MC trace is a named finding, never a ruling; the decision lives entirely in the exact seedless arms.
- Aux seed: 20261643, reserved, never read by any leg (the P054–P071 aux convention).
- Seeds 20261640–643 allocated from 20261640 per the coordinator relay: 20261630–633 are P071/V084's registered set and the gap 20261634–639 is the disclosed in-flight buffer, so 20261640 is the next free index — strictly above both. Boundary-aware sweep — regex `(^|[^0-9])2026[0-9]{4,6}([^0-9]|$)` over this tree at HEAD e17ebe7 maxes at genuine 20261633, and the sim-lab clone READ-ONLY at bf398f9 maxes at genuine 20261623 (V083's 20261620–623); the standalone numerals 20261664 / 20261833 / 202670087 / 2026964142 are digit-substrings (Fraction numerators, results-JSON decimals), data not seeds — the P046–P071 sweep-recipe trap re-confirmed.
- Print discipline (the P071 hazard, inherited): exact rationals at the p = 1/100 cell carry ~23-digit numerators (well under CPython's 4300-digit int-print default) — no large-rank hazard here, but the fixture still gates by in-memory `Fraction` equality first and prints second, per the P071 pinned practice.

## Pre-registered decision rule (evaluation order: REJECT first)

- **REJECT** — "batching is a THRESHOLDED instrument, not a free win: above an exact prevalence wall every pool size strictly loses, the cautious pair-pool is dominated at every prevalence, and the savings below the wall are real — so 'pool first, ask questions later' ships waste whenever nobody measured the defect rate first": **(R1)** at p = 2/5: T(n, 2/5) > 1 for EVERY n ∈ {2..64} (the strict wall clause) AND min over the practical grid n ∈ {2..8} of T(n, 2/5) ≥ 21/20 (every practical pool wastes ≥ 5%); **(R2)** T(2, q) − T(3, q) ≥ 1/54 at every q on the identity grid, with the identity T(2,q) − T(3,q) = (q − 2/3)²(q + 1/3) + 1/54 verified by exact coefficient match (equality attained ONLY at the appended grid point q = 2/3 — the named knife-edge); **(R3)** at p = 1/100: T\*(1/100) ≤ 1/4 (pooling saves ≥ 75% where the folk belief lives). (Checked FIRST because the costly direction is fleet-wide: batched verification surfaces — aggregate checks with drill-down, pooled retests, bisect-on-red — inherit the wall, and shipping "batching always saves" as doctrine wastes tests exactly where failure rates are high, which is exactly when the pipeline is already hurting.)
- **INVALID** (controls misbehaving — report, no ruling): any F1–F6 gate failure below.
- **APPROVE** — "the folk belief holds: pooling is a free win and pair-pools are fine": min over n ∈ {2..64} of T(n, 2/5) ≤ 1 AND T(2, q) ≤ T(3, q) at some identity-grid q. (Mutually exclusive with REJECT by arithmetic on both clauses.)
- **NULL** — anything else; pre-registered axes: wall-straddle (R1 holds but R3 fails, or R3 holds but R1's ≥ 21/20 clause fails while the strict clause holds — the wall exists but shallower/the savings thinner than banded; the finding is the exact T surface with the binding cell named); identity failure without gate failure (the T2 or T3 polynomial identity fails coefficient match — the drafter's algebra is wrong and the corrected law is the finding); margin-erosion (min over {2..8} of T(n, 2/5) ∈ (1, 21/20) — wall real but the practical damage under-banded); twin-arm disagreement surviving the INVALID diagnosis.

GATE POWER, computed at registration for a correct implementation (the V065/V067 lesson, applied): the sim is FULLY DETERMINISTIC at every decision cell — every decision clause and every F-gate is an exact-rational comparison, an integer-power comparison, a polynomial-coefficient match, or a byte comparison; the only seeded arm is reporting-only with NO statistical gate (its sole gates are the draw-count sentinel and exact reproducibility, pass probability 1 for a correct implementation); JOINT pass probability across all gates for a correct implementation = 1 EXACTLY (the P059–P068 no-stochastic-gate precedent), and decision separation is noise-free exact arithmetic. MARGIN LEDGER, disclosed (the V083 practice): R1's ≥ 21/20 clause clears at ×1.0641 (min = 419/375 at n = 3); R1's strict clause is a theorem (no margin concept — strict for every n, with the honest disclosure that T(n, 2/5) → 1⁺ as n → ∞, grid-tail value 1 + 1/64 − (3/5)^64 ≈ 1.015625 at n = 64, so the INFIMUM over unbounded n is 1 and the quantified clause is grid-bounded BY DESIGN); R2 attains its 1/54 floor WITH EQUALITY at the single appended grid point q = 2/3 (margin ×1.00 there — a registered knife-edge equality, not an accident: the identity makes the floor exact); R3 clears at ×1.2783 (T\* ≈ 0.195571 vs 1/4). T3's margin-0 cell (q² = 1/2) is certified symbolically (equality iff q² = 1/2, irrational — no rational grid point lands on it), and named in the margin ledger as the family's one true zero.

## Gates (run INVALID on any failure)

- **F1 — model identities:** T(1) = 1 exactly; probability normalization Σ_k C(n, k) p^k q^(n−k) = 1 exactly at every grid cell; the cost accounting law (stage-1 test ALWAYS counted — the 1/n term present in every T; its deletion is the named falsifiability world, never a code path); T(n, p) = 1 + 1/n − q^n rearrangement identity.
- **F2 — the three structure theorems, exact at every cell:** (a) WALL — the integer-power certificate chain (3² > 2³, 3⁴ > 4³, 3⁵ > 5³, 2⁴ = 4², (n+1)^n < n^(n+1) for n ∈ {3..64}) establishing min over the grid of n^(−1/n) at n = 3; the wall statement at every rational grid p: pooling helps at p for some n ∈ {2..64} iff 3q³ > 1 (drafting: helps at p ∈ {1/100 … 3/10}, fails at p ∈ {1/3, 2/5, 1/2, 2/3, 9/10}); the boundary law T(3, q) = 1 ⟺ 3q³ = 1 (symbolic). (b) PAIR-DOMINANCE — the identity T(2, q) − T(3, q) = (q − 2/3)²(q + 1/3) + 1/54 by exact coefficient match AND on the identity grid, equality exactly and only at q = 2/3. (c) 2–4 DEGENERACY — the identity T(2, q) − T(4, q) = (q² − 1/2)² by exact coefficient match AND on the identity grid; break-even coincidence q₂\* = q₄\* = 2^(−1/2) certified via 2⁴ = 4²; the margin-0 knife-edge named. Hand proofs pinned in the mechanism section.
- **F3 — census anchors (reference values, exact):** n\*(1/100) = 11 with T\* = 21512792031541191037911/110000000000000000000000 (≈ 0.195571; neighbours T(10) ≈ 0.1956179, T(12) ≈ 0.1969485 — the step structure is tight: n = 10 loses by < 5 × 10⁻⁵); n\*(1/50) = 8 with T\* = 10712381930399/39062500000000 (≈ 0.274237); n\*(1/20) = 5 with T\* = 1363901/3200000 (≈ 0.426219); n\*(1/10) = 4 with T\* = 5939/10000 (Dorfman's classic cell); n\*(1/5) = 3 with T\* = 308/375; n\*(1/4) = 3 with T\* = 175/192; n\*(3/10) = 3 with T\* = 2971/3000 (≈ 0.990333 — the last helping grid cell, a 0.97% saving in the wall's shadow); at p = 1/3: min over n ∈ {2..64} is 28/27 at n = 3 (> 1, above the wall — and q = 2/3 is simultaneously the T2 equality cell: p = 1/3 is the head's double knife-edge, named); at p = 2/5: min over {2..8} = 419/375 at n = 3, grid-tail min over {2..64} = 1 + 1/64 − (3/5)^64 at n = 64.
- **F4 — the hand world:** p = 1/2, n = 2 by pencil — pool outcomes: both clean prob 1/4 → 1 test; else → 3 tests; E = (1/4)·1 + (3/4)·3 = 5/2 per pool = 5/4 per item, so T(2, 1/2) = 5/4 exactly, matching both arms.
- **F5 — degeneracy controls:** p = 0 → T(n) = 1/n exactly (one test clears everything — pooling maximal); p = 1 → T(n) = 1 + 1/n exactly (every pool positive, pooling pure waste at every n — the wall's far shore); T(n, p) strictly increasing in p at fixed n on the identity grid.
- **F6 — battery:** Arm B reproduces every Arm-A number exactly (outcome tree vs closed form, independent n\* search, independent wall check); twin independently-written decision evaluators agree on the ruling token; Arm-R draw-count sentinels (n Bernoulli draws per pool) counted and asserted; presentation seed 20261642 read by presentation legs only; aux seed 20261643 never read; stdout + results.json byte-identical across two process runs (Arms A/B platform-independent exact rationals; Arm R pinned to a stated CPython minor).

## Expected landing (DISCLOSED per the P048–P071 exact-arm norm)

REJECT, at the drafter's exact values (the sim re-derives everything from scratch and must not trust these; every number below was computed live at drafting, closed form and outcome tree agreeing exactly on a 12 × 64 grid): **R1** — at p = 2/5, T(n) > 1 for every n ∈ {2..64} (strict; q = 3/5 < 3^(−1/3) certified by 3q³ = 81/125 < 1), and the practical-grid min is T(3, 2/5) = 419/375 ≈ 1.1173 ≥ 21/20 (×1.0641) — the BEST batch above the wall wastes 11.7%; **R2** — the identity holds with floor 1/54 attained exactly at q = 2/3 (×1.00 at the named knife-edge, strictly above 1/54 everywhere else on the grid); **R3** — T\*(1/100) = 21512792031541191037911/110000000000000000000000 ≈ 0.195571 ≤ 1/4 (×1.2783) at n\* = 11. Falsifiability is real and named on three axes: (i) the **free-pool-test world** — delete the 1/n term (the accounting slip: "the pool test is basically free") and T̃(n, p) = 1 − q^n < 1 for every n ≥ 2 and every p < 1, the wall VANISHES and the verdict flips to APPROVE outright — the entire mechanism lives in one term; (ii) the **one-step-down world** — at p = 3/10, one grid step below the wall cell's side, pooling already helps again (T(3) = 2971/3000 < 1, by 0.97%) — R1 is a genuine region, not a universal, and the wall's shadow (thin savings just below p\*) is a live NULL-straddle edge; (iii) the **unbounded-n tail** — T(n, 2/5) → 1⁺, so an unbounded damage quantifier would be FALSE (infimum 1); the registered clause is grid-bounded and says so. Disclosed sharpenings, reporting-only: the small-p scaling T\* ≈ 2√p with n\* ≈ 1/√p (drafting: T\*(1/400) ≈ 0.0988 at n\* = 21, T\*(1/2500) ≈ 0.0398 at n\* = 51); the double knife-edge at p = 1/3 (above-wall AND the T2 equality cell); the Arm-R preview (seed 20261640, p = 1/10, n = 4, 100,000 items: 0.591920 measured vs 5939/10000 exact).

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

Fleet-external head: no lane CONSUMER; the deliverable is a citable measured verdict feeding the rotation lane's domain-coverage proof (a fourteenth domain) plus a transferable test-economy correction. REJECT → "batching always saves" retires with numbers and the correction ships in three lines: (1) any drill-down verification surface (aggregate check + per-item retest on failure: batched CI legs, pooled lint passes, grouped flaky-suite retests, bisect-on-red over commit batches) has an exact prevalence wall — MEASURE THE FAILURE RATE FIRST; above ~30.7% batching of ANY size is pure waste, and the waste is largest exactly when the pipeline is already red-heavy; (2) never batch in pairs — the triple dominates the pair at every prevalence by an exact identity (≥ 1/54 tests/item), so the cautious-small-batch instinct is a theorem violation, not a preference: either batch ≥ 3 or go one-at-a-time; (3) don't A/B batch-of-2 against batch-of-4 near break-even — they tie EXACTLY there (the 2⁴ = 4² degeneracy), and the measured zero is structure, not noise. APPROVE → the batching default gains a measured basis and the wall machinery ships as the priced non-fix. NULL → the named axis ships with the exact T(n, p) surface. Follow-ups named, none in scope: imperfect tests (sensitivity/specificity < 1 — pooled false negatives shift the wall and break the perfect-test conditional); adaptive multi-stage protocols (halving/binary splitting, Sterling — a different T functional with a different wall); correlated defects (clustering concentrates positives in fewer pools and helps pooling — the i.i.d. boundary is directional); unequal/optimized pool-size mixtures; the information-theoretic floor (counting bound H(p) as the reporting benchmark for how far two-stage sits from optimal).

## Dedup

Tree-wide `rg -i 'group.?test|dorfman|pool(ed)?.?test|pooled.?screen|batch.?screen|prevalence|two.?stage.?test|sample.?pooling'` (bootstrap.py/.substrate excluded) at HEAD e17ebe7: ZERO domain hits. Companion sweep `rg -i 'screening'`: one word collision — `ideas/fleet/secretary-rule-cardinal-regret-2026-07-13.md:331` "candidate screening", a search-then-commit selection phrase in P036's consequence prose (optimal stopping), not pooled testing. sim-lab READ-ONLY dedup-swept the same way on a shallow clone at bf398f9 (VERDICT 083 newest, fetched 2026-07-15T09:08:22Z): zero hits for every domain term including `prevalence`. No recorded drop of this domain exists on any card. No proposal P001–P071 and no verdict V001–V083 prices group testing, pooled screening, two-stage test economics, or a prevalence threshold. Nearest priors argued distinct: **P052 → occupancy & collection** (coupon collector prices COLLECTION COMPLETION TIME under uniform sampling — here nothing is collected, there are no types or bins, and the priced object is a two-stage TEST-COUNT economy against an exogenous defect rate); **P044 → queue discipline** (waiting-time reordering of a service line — no tests, no prevalence, no design dial); **P036 → optimal stopping** (ONE decision-maker TIMING a commit on a sequential stream — the only place "screening" even appears, and it is candidate-search prose; here the design is one-shot, nothing arrives sequentially, and there is no stopping rule); **P064 → information cascades** (sequential Bayesian inference from observed ACTIONS under a hidden state — here test outcomes are EXACT, there are no beliefs, no inference, no herd); **P068 → two-sided matching** (two sides with preferences and a lattice of stable outcomes — here there are no sides, no preferences, no market, only a cost curve and its minimum); **P056 → random incidence** (length-biased OBSERVATION of ongoing intervals — no intervals, no observer bias); **P069 → the CONWIP cap/floor pair** (closed-loop flow with circulating WIP — no loop, no tokens; a one-shot design decision). Method kin only: the P028/P032/P036/P068 fully-exact zero-RNG census discipline (exact rationals + a twin arm + no stochastic gate), reused as machinery on a new object — this head's own additions to the battery: the INTEGER-POWER wall certificate (a threshold proven by comparing 3² to 2³), TWO exact polynomial dominance identities as gates, and a registered MARGIN-0 knife-edge cell disclosed in the margin ledger rather than discovered by the verdict session.

## Model basis (declared model-dependence — the P024 discipline)

Four modeling commitments carry the verdict, each pinned and directional: (1) PERFECT TESTS — no false negatives/positives, no dilution effect at any pool size; real assays degrade with pool size and a pooled false negative is a MISSED defective, which changes the objective from cost to cost-plus-risk; the wall p\* = 1 − 3^(−1/3) is perfect-test-conditional and stated so; imperfect tests are the first named follow-up. (2) i.i.d. Bernoulli DEFECTS — correlation/clustering concentrates positives in fewer pools and makes pooling strictly better (the boundary is directional: the wall can only MOVE UP under positive correlation); this head prices the independent regime and says so. (3) TWO-STAGE DORFMAN retest-all — adaptive protocols (halving, binary splitting) have different T functionals and different walls; the registered theorems are protocol-conditional; named follow-up. (4) TEST COUNT as the only cost — latency (two sequential rounds vs one), sample-splitting overhead, and retest logistics are not priced; the latency asymmetry (pooling always costs a round) is named reporting. The T2/T3 dominance identities are robust to (2) only through the per-pool law — they are exact facts about the committed T functional, and survive any cost rescaling (they are differences of T at fixed p); the WALL location is the model-dependent quantity, and its entire sensitivity is the 1/n term (the falsifiability world).

## Probe report (v0, 2026-07-15)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide sweep
> `rg -i 'group.?test|dorfman|pool(ed)?.?test|pooled.?screen|batch.?screen|prevalence|two.?stage.?test|sample.?pooling'`
> (bootstrap.py/.substrate excluded) at the grounding pin `e17ebe7` returned zero
> domain hits (one word collision cited: P036's "candidate screening" prose,
> secretary-rule file line 331), and the sim-lab READ-ONLY sweep at `bf398f9`
> returned zero hits including `prevalence`. (b) **kill test NOT triggered** — no
> prior proposal P001–P071, idea file, or session-card 💡 prices group testing,
> pooled screening, or a prevalence threshold; no recorded runner-up drop of this
> domain exists. (c) **feasibility + liveness arithmetic checked LIVE** — every
> registered theorem ran this session by exact enumeration (the V080 lesson): the
> closed-form/outcome-tree twin agreement on a 12 × 64 grid, the integer-power
> wall certificates, both polynomial identities by exact coefficient match plus
> 101-point grid enumeration with the q = 2/3 equality cell, all nine F3 census
> anchors, the F4 pencil world, the F5 degeneracies, the three REJECT margins
> (×1.0641 / ×1.00-at-the-named-knife-edge / ×1.2783), and an Arm-R seeded preview
> (0.591920 vs exact 0.593900 at p = 1/10, n = 4); expected landing DISCLOSED
> (REJECT) rather than hidden, all rulings reachable under the pre-registered
> rule, the free-pool-test APPROVE world and the p = 3/10 NULL-straddle edge both
> named, and the INVALID controls gated.

**1. What is this really?** A pre-registered EXACT MEASUREMENT of the batching folk
belief — "pooling always saves; small pools are the safe hedge" — taken where the
belief actually lives: the Dorfman two-stage cost law T(n, p) = 1/n + 1 − (1 − p)^n,
priced against the three exact structure facts the belief denies: an integer-power-
certified prevalence WALL (p\* = 1 − 3^(−1/3)) above which every pool size strictly
loses, an exact dominance identity making the pair-pool never optimal (floor 1/54 at
q = 2/3 exactly), and a margin-0 degeneracy tying pools 2 and 4 at their common
break-even (2⁴ = 4²). All decision arithmetic is seedless exact `fractions.Fraction`
judged against bands fixed before any code (REJECT first: the strict wall clause +
practical damage ≥ 21/20 at p = 2/5, the 1/54 dominance floor, savings ≤ 1/4 at
p = 1/100; APPROVE: pooling still helps at p = 2/5 or the pair beats the triple
somewhere; NULL otherwise on named axes), byte-identical across two runs, with the
seeded screening careers demoted to reporting-only.

**2. What is the possibility space?** (i) Don't run it — the round-14 unrelated
closer goes unserved and the rotation lane's coverage claim stalls at thirteen
domains. (ii) Re-use a prior round's domain — fails the owner's "rotate" ask; and
re-using cascades (P064) or matching (P068) would be the specific adjacency this
slot was told to avoid. (iii) A literature summary ("group testing saves tests at
low prevalence — see Dorfman 1943") — retells the direction, measures nothing
against a pre-registered band, and misses what the exact treatment uniquely gives:
the INTEGER-POWER wall certificate, the two dominance IDENTITIES (not inequalities
— exact polynomial factorizations with named equality cells), and the free-pool-test
one-term flip. (iv) An MC-only sim — leaves every decision number seed-noisy when
the whole object is closed-form exact (the V065/V067 lesson): the decision cells
are seedless rationals, MC is demoted to the career trace. (v) This head: exact
arithmetic as the ruling, REJECT-first bands on wall + dominance + savings, INVALID
on the F1–F6 identity/theorem/anchor/degeneracy/battery gates, robustness disclosed
via the free-pool-test APPROVE world, the p = 3/10 straddle edge, and the honest
grid-bounding of the damage quantifier. (vi) Over-scope (imperfect tests, adaptive
splitting, correlated defects, pool-size mixtures, the entropy floor) — each named
as a follow-up, none in scope.

**3. What is the most advanced capability reachable by the simplest implementation?**
One ~150-line stdlib file: the closed-form T, the outcome-tree twin, an integer-power
comparator, and a polynomial-coefficient expander — that single kernel yields the
exact cost surface over a 12 × 64 grid, the wall certificate, both dominance
identities verified as THEOREM CHECKS rather than estimates, the optimal-pool-size
step function with its exact break-evens, the margin ledger with its named
knife-edges, and the seeded career traces — from a sim a verdict session runs cold
in under a second.

**4. What breaks it? (assumptions made explicit)** (a) **Perfect tests are a
choice** — dilution and false negatives change the objective from cost to
cost-plus-risk and move the wall; the head prices the perfect-test regime, states
every theorem perfect-test-conditional, and names the imperfect-test follow-up.
(b) **i.i.d. defects are a choice** — clustering helps pooling, so the wall is a
WORST CASE for the batching instinct only in the independent regime; directional
statement pinned in the model basis. (c) **Band placement could cherry-pick** —
the 21/20, 1/54, and 1/4 clauses are committed BEFORE the sim, the expected landing
is DISCLOSED (REJECT), and the falsifiability is three-axis: the free-pool-test
world flips to APPROVE outright, the p = 3/10 cell is a genuine straddle edge one
grid step down, and the unbounded-n tail would falsify a universal damage claim
(infimum 1 — the registered clause is grid-bounded and says so). (d) **The
identities are claims, not axioms** — both are verified by exact coefficient match
AND enumeration, and each carries its own identity-failure-without-gate-failure
NULL axis, so a wrong hand factorization becomes a finalized corrected law, not a
silent bad gate. (e) **The knife-edges could hide fragility** — they are the
opposite: registered AS knife-edges in the margin ledger (R2's ×1.00 equality at
q = 2/3; T3's true zero at q² = 1/2), so the verdict session inherits them as
disclosed structure, not surprises.

**5. What does it unlock?** The pipeline's FOURTEENTH fleet-external verdict and
the rotation lane's domain-coverage proof extended (voting → routing → tournaments
→ pattern races → stopping → spatial self-organization → queueing → ratchets →
occupancy → random incidence → reciprocity → observational learning → two-sided
matching → group testing); a measured, citable answer to "when does batched
drill-down verification actually save work" with three standalone pins (the exact
wall p\* = 1 − 3^(−1/3) with its integer-power certificate; the pair-never-optimal
identity with its 1/54 floor; the 2–4 break-even degeneracy with its margin-0
cell); and a transferable test-economy correction for every fleet surface that
batches checks and drills down on failure — measure the failure rate first, never
batch in pairs, and don't A/B pool sizes across a degeneracy.

**6. What is the cheapest experiment that decides it?** The whole head IS the
cheapest deciding experiment: Arm A settles every decision number exactly in
milliseconds with no seed. The single cheapest probe if a reader doubts a specific
leg is the p = 1/2, n = 2 pencil world — both clean with probability 1/4 costs one
test, anything else costs three, E = (1/4)·1 + (3/4)·3 = 5/2 per pool = 5/4 per
item — which anchors the whole cost law against a three-line hand count; and the
wall's heart is one multiplication: at q = 3/5, is 3q³ = 81/125 > 1? No — so no
pool size can win at p = 2/5.

**7. What would make this a mistake to run?** If the exact treatment were
unavailable (it is not — the whole decision surface is closed-form rational
arithmetic), if the domain duplicated a prior head (it does not — the sweep
returned zero domain hits in both trees, no recorded drop exists, and the domain
is deliberately non-adjacent to both P064's cascades and P068's matching), or if
the disclosed REJECT made the run theater. It does not: the value is the
independent hermetic re-derivation of a classic threshold PLUS the parts no
textbook states in this form — the integer-power wall certificate, the two exact
dominance FACTORIZATIONS with named equality cells, the margin ledger with a
registered ×1.00 cell and a registered true zero, and the one-term free-pool-test
flip — and both non-REJECT rulings are genuinely reachable (APPROVE is one deleted
term away; the p = 3/10 straddle edge is one grid step away).

**8. How will we know it worked?** A committed sim-lab report with: the exact
T(n, p) surface at every grid cell (Fractions + float renderings), the optimal
n\*(p) step function with exact break-evens, the wall certificate chain, both
dominance identities verified by coefficient match and enumeration, the margin
ledger (×1.0641 / ×1.00-at-q = 2/3 / ×1.2783, plus T3's symbolic zero), the F1–F6
gate results, the verdict token against the pre-registered bands, Arm R's career
traces beside the exact expectations (reporting-only), and a byte-identity note
(two process runs identical). A clean run reproduces the drafter's disclosed
reference values (min-practical T(3, 2/5) = 419/375; floor 1/54 at q = 2/3;
T\*(1/100) ≈ 0.195571 at n\* = 11) from scratch, or — the more interesting outcome
— DISAGREES and pins the drafter's error, which the pre-registered rule then rules
on honestly (the identity-failure NULL axes exist for exactly that).

**Recommendation: sim-ready**
