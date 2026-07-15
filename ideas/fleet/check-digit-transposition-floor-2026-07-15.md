# The check digit's exact blind spot: no position-wise mod-10 scheme catches every adjacent swap — the floor is exactly 2 of 90 ordered pairs (one-line certificate: 0 ≠ 5 mod 10; Luhn attains it on precisely 09↔90) — and the ISBN-10 → EAN-13 migration strictly WEAKENED transposition detection (0 → 10/90 adjacent, 0 → 90/90 at distance 2)

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 COMPLETELY-UNRELATED-domain slot, round 15 closer; a FIFTEENTH fleet-external domain: algebraic error detection — check-digit design over decimal identifiers (Luhn / weighted mod-10 / ISBN-10 mod-11 / the Damm quasigroup), disjoint from the fourteen prior occupants — social choice (P017), congestion routing (P024), tournament seeding (P028), pattern races (P032), optimal stopping (P036), spatial self-organization (P040), queue discipline (P044), stochastic ratchets (P048), occupancy & collection (P052), random incidence (P056), repeated-game reciprocity (P060), information cascades (P064), two-sided matching (P068), group testing / screening design (P072) — and deliberately NOT adjacent to the last three unrelated slots' domains: no signals, no beliefs, no sequential inference and no herd (vs P064's cascades); no two sides, no preferences, no market (vs P068's matching); no probability, no prevalence, no subset queries and no test economy (vs P072's group testing — that head priced a STOCHASTIC screening design against an exogenous defect rate; this head is DETERMINISTIC algebra on a single codeword, and its decision arms contain no random variable at all))
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264 pipeline; routing is the manager's per Q-0260, this repo never edits sim-lab files)
> **Grounding:** https://github.com/menno420/idea-engine@87bbb39ac3ba245169dd39628c9fd45fe8f03c82 · fetched 2026-07-15T11:15:03Z
> (the dedup-sweep HEAD, the only read this head takes; every model constant below is invented-but-pinned in this file, and the DECISION arms are exact seedless integer arithmetic with zero repo/network reads at verdict time — the P017–P072 hermetic precedent; sim-lab dedup-swept READ-ONLY on a shallow clone @ d6610dc090671b606be3fa0a2f55a51ba3c3f595, VERDICT 087 newest, fetched 2026-07-15T11:22:09Z)
> **Origin:** standing ORDER 003 (continuous new ideas per repo) under ORDER 004 rule 3 (deliberate lane rotation, "COMPLETELY UNRELATED domains — I want those too"); round 15 opened at fleet backlogs (P073 #437), served venture (P074 #438) and game mechanics (P075 #439, merged 2026-07-15T11:09:44Z), so this head is the round-15 UNRELATED closer. Slot spacing history P060, P064, P068, P072 → P076 (spacing 4) confirms the placement.

**Placement note (decide-and-flag):** this fleet-external pure-mechanism head lives in `ideas/fleet/` per the `check_sections` carve-out for cross-cutting heads — flagged rather than silently squatting, exactly as PROPOSALs 017 through 072 did.

## The folk belief

"Slap a check digit on it and typos are handled — any standard scheme catches the errors that matter; and the newer standard is at least as strong as the one it replaced." This is the instinct behind every identifier with a trailing digit: card numbers (Luhn), book numbers (ISBN), retail barcodes (EAN/UPC), account and container numbers, license keys, order IDs. The instinct has three load-bearing halves, none of them priced: (1) that "validates" means "detects the human error classes" — single mistyped digits and swapped neighbours, the two dominant transcription slips; (2) that schemes are interchangeable ("it's all just a checksum"); (3) that standards migration is monotone — the 2007 move of the world's book numbers from ISBN-10 to ISBN-13/EAN-13 surely did not make error detection WORSE. All three are false in an exactly measurable way, and the third is false in the most uncomfortable direction: the migration traded a code that catches EVERY single error and EVERY transposition at ANY distance for one that misses 10 of 90 adjacent swaps and ALL 90 distance-2 swaps.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

Fix the alphabet Z10 and a codeword d_1…d_n. A **position-wise mod-10 scheme** validates by Σ_i σ_i(d_i) ≡ 0 (mod 10), each σ_i a permutation of Z10 — this family contains every classic decimal check: plain weighted sums (σ_i(y) = w_i·y), Luhn (σ_i = the doubling fold L(y) = 2y, digit-summed: L = [0,2,4,6,8,1,3,5,7,9], on alternate positions), and their mixtures. Three exact structure theorems, each verified live at drafting by enumeration (`draft_p076.py`, 50/50 checks PASS, exit 0). **T1 — the FLOOR.** An adjacent swap at boundary i (…a,b… → …b,a…) escapes iff σ_i(a) + σ_{i+1}(b) ≡ σ_i(b) + σ_{i+1}(a), i.e. iff the difference map τ(y) = σ_i(y) − σ_{i+1}(y) mod 10 collides at a, b. Detection of ALL swaps at the boundary would need τ injective — impossible by a one-line certificate: Σ_y τ(y) ≡ Σσ_i − Σσ_{i+1} ≡ 0 (mod 10), while any permutation of Z10 sums to 45 ≡ 5, and 0 ≠ 5. So EVERY boundary of EVERY position-wise mod-10 scheme misses at least one unordered pair. The census is exact and fully enumerated: the boundary's miss count depends only on the quotient permutation π = σ_i ∘ σ_{i+1}⁻¹ (lemma, enumeration-verified), and over ALL 3,628,800 quotients the minimum number of undetected ORDERED pairs is **2** — attained by exactly **46,400** quotients, with the maximum 90 attained by exactly the **10** rotations (τ constant). Luhn's quotient is L itself: its τ collides only at {0, 9} — Luhn misses **exactly the two ordered pairs (0,9) and (9,0)** per boundary and nothing else. Luhn sits ON the floor: among ALL position-wise mod-10 schemes, none does better, only equally well. **T2 — the LINEAR ESCAPE.** For plain weights, catching all SINGLE errors forces every w_i to be a unit mod 10, and the units {1, 3, 7, 9} are all ODD — so every boundary difference w_i − w_{i+1} is EVEN, and the swap pairs with a − b ≡ ±5 escape: (w_i − w_{i+1})(a − b) ≡ even·5 ≡ 0 (mod 10). Enumerated over the full 10 × 10 weight grid: exactly **16** cells catch all singles; the **4** diagonal cells (equal weights) miss all **90** ordered pairs; the **12** off-diagonal cells miss exactly **10** each (precisely the |a − b| = 5 pairs). Nonlinearity (Luhn's fold) buys a 5× reduction (10 → 2) but the T1 certificate caps it above zero. **T3 — the MIGRATION REGRESSION and the two exits.** ISBN-10 validates Σ (10−i)·d_i ≡ 0 mod **11**: every weight and every weight DIFFERENCE is a unit mod the prime 11, so the census is **0** undetected singles and **0** undetected transpositions at EVERY distance — complete, at the price of an 11th symbol (the 'X'). EAN-13 (which absorbed ISBN in 2007) validates with weights alternating 1, 3 mod 10: singles complete, but each adjacent boundary misses **10/90** (the |a − b| = 5 pairs) and each distance-2 pair of positions — SAME weight — misses **90/90**; over the full 13-digit code that is 12 × 10 = **120** adjacent escape patterns and 11 × 90 = **990** distance-2 escape patterns where ISBN-10 had zero. The second exit needs no 11th symbol: the pinned **Damm quasigroup table** (10 × 10, rows and columns permutations, zero diagonal — all verified live) digests sequentially, c ← T[c][d], and its state census is **0/900** undetected singles and **0/900** undetected adjacent swaps on the same ten digits — the T1 barrier is a fact about ABELIAN-LINEAR checks, not about the alphabet; the exit is non-associative algebra, not more symbols. (Honesty row, enumerated: Damm's distance-2 state census is **958/9000** undetected — completeness at every distance is ISBN-10's alone among the pinned schemes.) The drafting surprise worth the head: the impossibility is ONE LINE (0 ≠ 5 mod 10 — the same parity obstruction, note, that no abelian group of even order with a unique involution admits a complete mapping), yet the folk belief survives everywhere because nobody prices the miss SET — and the miss sets are tiny, structured, and named: Luhn = {09↔90}, EAN = {05↔50, 16↔61, 27↔72, 38↔83, 49↔94} adjacent plus EVERYTHING at distance 2.

## Pinned model (committed constants — all invented-but-pinned, exact integers)

- Alphabet Z10 = {0..9}; codeword positions indexed from the check digit. Error classes priced (the classic transcription taxonomy, pinned as the model): **SUB** = single-digit substitution (ordered pairs a → b, a ≠ b: 90 per position), **ADJ** = adjacent transposition (ordered pairs (a, b), a ≠ b, at a boundary: 90), **D2** = distance-2 transposition (90 per position pair). Jump/twin/phonetic errors: named follow-ups, never decision.
- Schemes pinned: **LUHN** (fold L(y) = 2y digit-summed = [0,2,4,6,8,1,3,5,7,9] on alternate positions, identity elsewhere; check = digit making the fold sum ≡ 0 mod 10); **LINEAR(w1, w2)** over the full 10 × 10 weight grid at one boundary; **ISBN-10** (length 10, weights 10, 9, …, 1, mod 11, symbols 0..10); **EAN-13** (length 13, weights alternating 1, 3, mod 10); **ALL-ONES** (every weight 1 — the naive digit-sum control); **DAMM** (the pinned 10 × 10 table below, digest c₀ = 0, c ← T[c][d], valid iff final c = 0). The Damm table, row-major (row = state, column = digit): `[[0,3,1,7,5,9,8,6,4,2],[7,0,9,2,1,5,4,8,6,3],[4,2,0,6,8,7,1,3,5,9],[1,7,5,0,9,8,3,4,2,6],[6,1,2,3,0,4,5,9,7,8],[3,6,7,4,2,0,9,5,8,1],[5,8,6,9,7,2,0,1,3,4],[8,9,4,5,3,6,2,0,1,7],[9,4,3,8,6,1,7,2,0,5],[2,5,8,1,4,3,6,7,9,0]]` — its required properties (rows permutations, columns permutations, zero diagonal, 0/900 state censuses) are GATES, not assumptions.
- Census definitions (all exact integer counts): boundary census U(π) = #{(a, b) : a ≠ b, τ(a) = τ(b)} for τ(y) = π(y) − y mod 10, where π is the boundary's quotient permutation; position-pair censuses for SUB/ADJ/D2 per scheme; word-level censuses by FULL enumeration of every valid length-4 codeword (10³ = 1000 valid words per mod-10 scheme; 11³ = 1331 for the 11-ary mini-code) × every error instance.
- Arm A (the DECISION arm, seedless): the complete 10! quotient census (histogram of U over all 3,628,800 permutations); the quotient-reduction lemma verified on the pinned 6-permutation spot set (36 pairs, direct count vs U(quotient)); the 10 × 10 linear weight grid; the ISBN-10 / EAN-13 / ALL-ONES position-pair censuses; the Damm state censuses (900-cell SUB and ADJ, 9000-cell D2 reporting). Byte-identical across process runs.
- Arm B (twin, seedless, INDEPENDENTLY-WRITTEN): full word-level enumeration at length 4 for LUHN / EAN-style (weights 1,3,1,3) / the 11-ary mini-code (weights 4,3,2,1) / DAMM — valid-word counts and undetected-error counts must equal the Arm-A position censuses through the typed must-equal contacts: **word-ADJ = boundaries × ordered-escape-census × 10** (each ordered digit pair at a boundary sits in exactly 10 valid words — LUHN 60 = 3 × 2 × 10, EAN 300 = 3 × 10 × 10, EAN-D2 1800 = 2 × 90 × 10, mini-mod-11 0, DAMM 0), and word-SUB = 0 across all four.
- Arm R (seeded, REPORTING-ONLY): random 16-digit Luhn identifiers and 13-digit EAN codes, one random ADJ and one random D2 injection each, N = 20,000 episodes on `random.Random(20261680)` with draw counts counted and asserted (drafting: 600,000 draws exactly); stability leg `random.Random(20261681)` at N = 8,000; presentation shuffle 20261682. NO statistical gate rides Arm R — the measured miss rates sit beside the exact censuses as a trace, never a ruling.
- Aux seed: 20261683, reserved, never read by any leg (the P054–P075 aux convention).
- Seeds 20261680–683 allocated from 20261680 per the coordinator relay: 20261670–673 are P075's registered set and the gap 20261674–679 is the disclosed in-flight buffer, so 20261680 is the next free index — strictly above both. Boundary-aware sweep — regex `(^|[^0-9])2026[0-9]{4,6}([^0-9]|$)` over this tree at HEAD 87bbb39 maxes at genuine 20261673, and the sim-lab clone READ-ONLY at d6610dc maxes at genuine 20261663 (V087's 20261660–663); the standalone numerals 20261664 / 20261833 / 202670087 / 2026964142 are digit-substrings (Fraction numerators, results-JSON decimals), data not seeds — the P046–P075 sweep-recipe trap re-confirmed.
- Runtime disclosure: the 10! census is the only heavy leg — 3,628,800 permutations, ~10 s in CPython at drafting; every other leg is ≤ 10⁵ operations.

## Pre-registered decision rule (evaluation order: REJECT first)

- **REJECT** — "a check digit is a designed instrument with an exact, named blind spot, not generic validation: full mod-10 swap coverage is IMPOSSIBLE (floor 2, Luhn already optimal), the famous standards migration was a strict detection DOWNGRADE, and complete coverage is available — one symbol away (mod 11) or one algebra away (Damm) — so scheme choice must be priced by census, never by vibes or recency": **(R1, the floor)** over all 3,628,800 quotient permutations, min U = 2 exactly (with 0 excluded by the Σ-certificate 0 ≠ 5 checked symbolically AND by the census containing no U = 0 cell), Luhn's boundary census = 2 with miss set exactly {(0,9),(9,0)}, and the best all-singles LINEAR cell = 10 (5× the floor); **(R2, the regression)** ISBN-10 censuses 0 SUB and 0 transpositions at EVERY distance, while EAN-13 misses exactly 10/90 per adjacent boundary and 90/90 per distance-2 pair (120 + 990 escape patterns over the full 13-digit code) — strict weakening in both transposition classes with SUB coverage preserved; **(R3, the exits are real)** the pinned Damm table passes all three property gates and scores 0/900 SUB and 0/900 ADJ on the same 10-symbol alphabet, and the 11-ary mini-code word-enumerates to 0/0 — i.e. the blind spot is a CHOICE, not a law of digits. (Checked FIRST because the costly direction is fleet-wide: every hand-copied identifier surface — order numbers, license keys, coupon codes, the venture lane's own EAN-13 book ISBNs — inherits whichever miss set its scheme ships, and "it has a check digit" as a doctrine line silently blesses the 90/90 distance-2 blindness of the modern default.)
- **INVALID** (controls misbehaving — report, no ruling): any F1–F6 gate failure below.
- **APPROVE** — "the folk belief holds: standard schemes catch all the swaps that matter and the migration was monotone": some quotient permutation achieves U = 0 (arithmetically excluded by R1's certificate — mutually exclusive with REJECT), or EAN-13's adjacent census = 0 and distance-2 census = 0.
- **NULL** — anything else; pre-registered axes: **census-contact mismatch** (an Arm-B word-level count fails its typed must-equal contact while both arms internally reproduce — the drafter's multiplicity law is wrong; the corrected contact is the finding, and the drafting-run correction disclosed below makes this axis genuinely live); **floor-value surprise** (min U ≠ 2 or the minimizer count ≠ 46,400 without any gate failure — the drafter's census is wrong and the corrected histogram is the finding); **Damm-table failure** (any property gate fails in the verdict session — the pinned table is wrong, R3 falls back to the 11-ary exit alone, and the corrected/dropped clause is the finding); twin-arm disagreement surviving the INVALID diagnosis.

GATE POWER, computed at registration for a correct implementation (the V065/V067 lesson, applied): the sim is FULLY DETERMINISTIC — every decision clause and every F-gate is an exact integer census, a symbolic certificate, a table-property assertion, or a byte comparison; the only seeded arm is reporting-only with NO statistical gate (its sole gates are the draw-count sentinel and exact reproducibility, pass probability 1 for a correct implementation); JOINT pass probability across all gates for a correct implementation = 1 EXACTLY (the P059–P072 no-stochastic-gate precedent: determinism proven by byte-identical re-run, not estimated), and decision separation is noise-free exact counting. MARGIN LEDGER, disclosed (the V083 practice): every REJECT clause is an exact-equality census — the margin concept degenerates to theorem-vs-not, and the ledger instead names the three registered EQUALITY cells a verdict session must land on exactly: Luhn's U = 2 sits ON the R1 floor (margin ×1.00 BY CONSTRUCTION — optimality, not clearance); the EAN distance-2 census 90/90 is a saturated cell (the maximum possible — no room above); and the Damm ADJ census 0/900 is a zero cell (the minimum possible — no room below). A census landing anywhere off these exact values is INVALID-or-NULL by the pre-registered axes, never a "close enough".

## Gates (run INVALID on any failure)

- **F1 — model identities:** the Luhn fold list equals [(2d if d < 5 else 2d − 9) for d in 0..9] and is a permutation; units mod 10 enumerate to {1, 3, 7, 9}, all odd; valid-word counts exactly 10³ per mod-10 scheme at length 4 and 11³ for the 11-ary mini-code; the Damm digest determinism (same word → same state); the Σ-certificate arithmetic (any permutation of Z10 sums to 45; 45 mod 10 = 5 ≠ 0).
- **F2 — the three structure theorems, exact:** (a) FLOOR — the certificate excludes U = 0 for every π (symbolic + census: no U = 0 bin); the full 10! histogram totals 3,628,800 with min 2 (count 46,400) and max 90 (count exactly 10 = the rotations); the quotient-reduction lemma on the pinned 36-pair spot set. (b) LINEAR ESCAPE — the 10 × 10 grid: 16 all-singles cells partitioning {4 diagonal → 90, 12 off-diagonal → 10}; the escape set at weights (1, 3) is exactly the ten ordered |a − b| = 5 pairs; the linear-cell ↔ quotient-census cross contact on all 16 unit cells (multiplicative quotient π(y) = w₁w₂⁻¹y reproduces the grid count). (c) REGRESSION + EXITS — ISBN-10 position-pair censuses 0/0 (10 × 110 SUB checks, 45 × 110 transposition checks, every distance); EAN adjacent 10/90 and distance-2 90/90 with the full-code pattern counts 120/990; the Damm property gates (rows, columns, diagonal) and state censuses 0/900, 0/900.
- **F3 — census anchors (reference values, exact):** min U = 2 · minimizer count 46,400 · rotation count 10 at U = 90 · Luhn miss set {(0,9),(9,0)} · linear floor 10 · EAN escape set {05,16,27,38,49}±ordered · word-level LUHN {1000 valid, 0 SUB, 60 ADJ} · EAN-style {1000, 0, 300 ADJ, 1800 D2} · 11-ary {1331, 0, 0} · DAMM {1000, 0, 0} · Damm D2 reporting 958/9000 · ALL-ONES 0 SUB / 90 ADJ per boundary at every distance.
- **F4 — the hand worlds (pencil):** (a) weights (1, 1), length 2: a swap never changes the sum — 90/90 undetected, by inspection; (b) Luhn on the two-digit words 09 and 90 with the left digit doubled: 0 + L(9) = 9 and 9 + L(0) = 9 — same digest, the famous miss, by pencil; (c) the certificate itself: 0+1+…+9 = 45, 45 mod 10 = 5, and Στ ≡ 0 — three lines.
- **F5 — degeneracy controls:** a weight-0 position misses all 90 ordered SUB pairs (the "check digit that checks nothing" pole); the identity quotient π = id (equal maps across a boundary) gives constant τ and U = 90; ALL-ONES misses every transposition at every distance while catching every SUB — the "sorted-digits validator" pole.
- **F6 — battery:** Arm B word-level counts equal Arm A position censuses through the FOUR typed must-equal contacts (60 = 3 × 2 × 10 · 300 = 3 × 10 × 10 · 1800 = 2 × 90 × 10 · 0 = 0), with the multiplicity law (each ordered pair at a boundary sits in exactly 10 valid words) asserted directly; twin independently-written decision evaluators agree on the ruling token; Arm-R draw-count sentinel (drafting: exactly 600,000 draws at N = 20,000) and exact reproducibility; presentation seed 20261682 read by presentation legs only; aux seed 20261683 never read; stdout + results.json byte-identical across two process runs (Arms A/B pure integer arithmetic, platform-independent; Arm R pinned to a stated CPython minor).

## Expected landing (DISCLOSED per the P048–P075 exact-arm norm)

REJECT on all three conjuncts, at the drafter's exact values (the sim re-derives everything from scratch and must not trust these; every number below was computed live at drafting, 50/50 checks PASS, exit 0): **R1** — min U = 2 over the full 10! census (46,400 minimizers; no U = 0 bin; histogram total 3,628,800; max 90 on exactly the 10 rotations), Luhn = 2 with miss set {(0,9),(9,0)}, linear best = 10; **R2** — ISBN-10 0/0 at every distance vs EAN-13 10/90 adjacent and 90/90 distance-2 (120/990 full-code patterns); **R3** — Damm passes rows/columns/diagonal and scores 0/900 + 0/900 (word-level 1000/0/0), the 11-ary mini-code word-enumerates 1331/0/0. Falsifiability is real and named on three axes: (i) the **eleventh-symbol world** — one extra symbol dissolves the entire impossibility (ISBN-10's censuses are zero at every distance): the floor is alphabet-exact, and a reader who thinks the theorem is about "digits being few" is refuted one symbol away; (ii) the **non-abelian world** — the Damm table hits 0/900 on the SAME ten digits, so any claim that "10 symbols force misses" is falsified by the head's own R3 arm — the registered impossibility names its true scope (position-wise abelian mod-10 checks) and would be FALSE one algebra away; (iii) the **drafting-run correction, disclosed** — the drafter's first hand-derived word-level contacts (30/150/900, the unordered counts) were WRONG by the ordered-pair factor: the enumeration returned 60/300/1800 and corrected the multiplicity law before registration (each ORDERED pair sits in 10 valid words; the unordered count double-hides the swap's two directions) — the census-contact NULL axis exists because exactly this class of error is live, and a verdict session reproducing 30/150/900 would be finding a real drafter regression, not noise. Disclosed sharpenings, reporting-only: the full U histogram (bins 2 through 90, only even values, support {2, 4, …, 36, 40, 42, 44, 56, 58, 90} with the curious gap structure above 44); Damm's distance-2 honesty row 958/9000; the Arm-R preview at seed 20261680 (Luhn ADJ measured 412/17954 ≈ 0.022948 vs exact 2/90 ≈ 0.022222; EAN ADJ 1948/18026 ≈ 0.108066 vs 10/90 ≈ 0.111111; EAN D2 17966/17966 = 1.0 vs 90/90; 600,000 draws counted); and the scale row — over a 13-digit EAN code the miss surface is 120 adjacent + 990 distance-2 patterns where the code it replaced had zero.

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

Fleet-external head: no lane CONSUMER; the deliverable is a citable measured verdict feeding the rotation lane's domain-coverage proof (a fifteenth domain) plus a transferable identifier-integrity correction. REJECT → "a check digit means typos are handled" retires with numbers and the correction ships in three lines: (1) a check digit is a designed instrument with an exact miss SET — when adopting or migrating one, enumerate the census first (the whole audit is < 10⁶ integer operations for any decimal scheme; the drafting kernel is ~200 lines of stdlib); (2) never assume the newer standard is stronger — the world's book numbers are the counterexample (ISBN-10 → EAN-13 traded complete transposition detection for 10/90 + 90/90 blindness), so "modern default" is not a detection argument; (3) if swap coverage matters, the exits are priced: one extra symbol (mod 11, ISBN-10-style) buys completeness at every distance, one table lookup (Damm) buys single+adjacent completeness on pure digits — and staying mod-10 means accepting a floor of 2 that Luhn already attains (there is nothing to tune; any "improved mod-10 scheme" claim is refutable by the certificate). APPROVE → the interchangeability default gains a measured basis and the census machinery ships as the priced non-fix. NULL → the named axis ships with the full histogram and censuses. Follow-ups named, none in scope: twin errors (aa → bb) and jump transpositions (the classic taxonomy's minor classes — Verhoeff's D5 scheme prices them differently from Damm); phonetic errors (13 ↔ 30, language-bound); burst errors and length errors (insertion/deletion — a different invariant family); weighted error PRIORS (a frequency-weighted expected-miss objective needs empirical keystroke data — deliberately excluded so the decision stays exact); alphanumeric alphabets (mod 36/37 — the certificate's parity obstruction vanishes for odd-order groups, a directional boundary stated, not priced).

## Dedup

Tree-wide `rg -i 'luhn|verhoeff|damm|check.?digit|ean.?13|isbn|mod.?11|quasigroup|error.?detect'` (bootstrap.py/.substrate excluded) at HEAD 87bbb39: ZERO domain hits (the `transposition` companion sweep hits only P066/V073's owner-queue attention head — adjacent transpositions of a SORT ORDER in an exchange argument, sequencing not error detection — and this file). Companion sweep `rg -i 'checksum'`: word collisions only — the gba-homebrew lane's ROM/artifact integrity prose (`ideas/gba-homebrew/seeded-cave-runs-2026-07-10.md`, `lumen-drift-owner-play-kit-2026-07-10.md`: a pinned-toolchain checksum manifest and a checksummed .gba artifact — file-integrity hashing of a build product, no scheme design, no error-class censuses). sim-lab READ-ONLY dedup-swept the same way on a shallow clone at d6610dc (VERDICT 087 newest, fetched 2026-07-15T11:22:09Z): word collisions only — `verdict-050`'s `gl_save_checksum` mirror (a game save-file integrity word inside a survival-ceiling sim) and `verdict-073`'s exchange-argument "transpositions"; zero hits for Luhn / Damm / check digit / ISBN / quasigroup / mod-11 in either tree. No recorded drop of this domain exists on any card. No proposal P001–P075 and no verdict V001–V087 prices error-detecting codes, check-digit schemes, or an algebraic-impossibility census. Nearest priors argued distinct: **P072 → group testing** (the nearest-sounding neighbour, and the reason this head argues adjacency explicitly: Dorfman screening LOCATES defective items via subset tests under a PREVALENCE prior — a stochastic test-economy design whose decision object is an expected cost curve; here nothing is located, there is no prior, no pool, no expectation — the object is a deterministic algebraic invariant of a single codeword and its exact miss census; the shared word "detection" is the entire overlap); **P032 → pattern races** (Penney's game prices WAITING TIMES of stochastic symbol patterns — here there is no process, no race, no probability in any decision arm); **P052 → occupancy** (collection completion under uniform sampling — no codes, no errors); **P064 → cascades** (sequential Bayesian inference — no signals or beliefs here); **P068 → matching** (two-sided preferences — no sides here); **P044/P069** (queue/flow mechanics — no service system here). Method kin only: the P028/P032/P048/P060/P072 fully-exact zero-RNG census discipline (exact counting + a twin arm + no stochastic gate), reused as machinery on a new object — this head's own additions to the battery: a COMPLETE 10!-space census as a decision leg (3,628,800 cells, the pipeline's first exhaustive search over a function space), a one-line SYMBOLIC impossibility certificate gated beside its own exhaustive confirmation, and a disclosed drafting-run correction (the ordered/unordered multiplicity factor) pre-registered as its own NULL axis.

## Model basis (declared model-dependence — the P024 discipline)

Four modeling commitments carry the verdict, each pinned and directional: (1) the ERROR TAXONOMY is the classic transcription pair (substitutions + transpositions at distances 1 and 2) with uniform treatment inside each class — no empirical keystroke frequencies (a frequency-weighted objective is a named follow-up requiring data this hermetic head refuses to invent); the censuses are therefore class-exact, not risk-weighted, and say so. (2) POSITION-WISE schemes only — the impossibility theorem's scope is Σ σ_i(d_i) mod 10; digest schemes (Damm) sit OUTSIDE the scope and are priced as the exit, which is exactly the point: the theorem names its boundary and the head verifies life on both sides. (3) LENGTH-4 word enumerations stand in for full-length codes via the position-census reduction (detection depends only on the boundary/position algebra, verified by the typed contacts); full-length pattern counts (120/990 for EAN-13) are products of per-boundary censuses and boundary counts — an identity, not an approximation. (4) MOD-10/11 arithmetic exactly — no symbol restrictions beyond the pinned alphabets (real ISBN-10 bodies exclude 'X' from non-check positions; detection on a sub-alphabet is inherited monotonically from the full-alphabet census, stated not re-enumerated). The Damm table is a pinned CONSTANT whose properties are gates — a wrong table fails F2(c) as INVALID at the sim, and the Damm-failure NULL axis prices the drafter-table risk explicitly.

## Probe report (v0, 2026-07-15)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide sweep
> `rg -i 'luhn|verhoeff|damm|check.?digit|ean.?13|isbn|mod.?11|quasigroup|error.?detect'`
> (bootstrap.py/.substrate excluded) at the grounding pin `87bbb39` returned zero
> domain hits (word collisions cited: gba ROM-integrity "checksum" prose, P066's
> exchange-argument "transpositions"), and the sim-lab READ-ONLY sweep at `d6610dc`
> returned word collisions only (verdict-050's save-file checksum mirror). (b) **kill
> test NOT triggered** — no prior proposal P001–P075, idea file, or session-card 💡
> prices error-detecting codes or check-digit design; no recorded runner-up drop of
> this domain exists. (c) **feasibility + liveness arithmetic checked LIVE** — every
> registered numeral ran this session by enumeration (the V080 lesson): the complete
> 10! census (~10 s), the Σ-certificate, the 36-pair quotient-reduction spot set, the
> 10 × 10 weight grid, the ISBN/EAN/ALL-ONES position censuses, all four length-4
> word-level enumerations with their typed contacts, the Damm property + state
> censuses, the pencil worlds, and the seeded Arm-R preview with its draw-count
> sentinel; expected landing DISCLOSED (REJECT) rather than hidden, all rulings
> reachable under the pre-registered rule, the eleventh-symbol and non-abelian
> falsifiability worlds both named, one drafting-run hand-fact correction disclosed
> (ordered vs unordered word-level multiplicity — 30/150/900 corrected to
> 60/300/1800 by the enumeration), and the INVALID controls gated.

**1. What is this really?** A pre-registered EXACT MEASUREMENT of the check-digit folk
belief — "any standard scheme catches the typos that matter, and newer standards are
stronger" — taken where the belief actually lives: the position-wise decimal check
family, priced against three exact structure facts the belief denies: a one-line
impossibility certificate (the ten boundary differences sum to 0 mod 10; a permutation
would sum to 5) with its complete 3,628,800-cell census (floor 2, Luhn optimal at
exactly {09↔90}), the linear-escape law (all-singles weights are odd units, so |a−b| = 5
swaps escape — best linear cell 10, 5× the floor), and the migration regression
(ISBN-10's 0/0-at-every-distance traded for EAN-13's 10/90 + 90/90). All decision
arithmetic is seedless exact integer counting judged against bands fixed before any
code (REJECT first: floor + regression + the two priced exits; APPROVE: a U = 0
quotient or a clean EAN census; NULL otherwise on named axes), byte-identical across
two runs, with the seeded identifier careers demoted to reporting-only.

**2. What is the possibility space?** (i) Don't run it — the round-15 unrelated closer
goes unserved and the rotation lane's coverage claim stalls at fourteen domains.
(ii) Re-use a prior round's domain — fails the owner's "rotate" ask; the three most
recent occupants (cascades, matching, group testing) are the specific adjacencies this
slot must avoid, and the adjacency argument against P072 is made explicitly in the
Dedup. (iii) A literature summary ("Luhn misses 09/90, use Verhoeff — see Wikipedia")
— retells folklore, measures nothing against a pre-registered band, and misses what
the exact treatment uniquely gives: the COMPLETE quotient-space census (the floor is
2 because all 3,628,800 cells were counted, not because a textbook says so), the
certificate gated beside its own exhaustive confirmation, and the typed word-level
contacts that caught a real drafter error at drafting time. (iv) An MC-only sim —
leaves every decision number seed-noisy when the whole object is finite and countable
(the V065/V067 lesson): the decision cells are exact integer censuses, MC is demoted
to the identifier-career trace. (v) This head: exact counting as the ruling,
REJECT-first bands on floor + regression + exits, INVALID on the F1–F6
identity/theorem/anchor/pencil/degeneracy/battery gates, falsifiability via the
eleventh-symbol world, the non-abelian world, and the disclosed drafting correction.
(vi) Over-scope (twin/jump/phonetic errors, insertion/deletion, frequency-weighted
objectives, alphanumeric alphabets) — each named as a follow-up, none in scope.

**3. What is the most advanced capability reachable by the simplest implementation?**
One ~200-line stdlib file: a τ-collision counter, one `itertools.permutations` loop,
a weight-grid scan, four length-4 word enumerations, and ten table-property asserts —
that single kernel yields the complete quotient-space histogram (an EXHAUSTIVE search
over a 3.6-million-cell function space in ~10 s), the impossibility floor with its
attaining set counted, the named miss sets of the world's two most deployed decimal
schemes, the exact price of the 2007 book-number migration, both priced exits, and
the seeded career traces — from a sim a verdict session runs cold in under a minute.

**4. What breaks it? (assumptions made explicit)** (a) **The error taxonomy is a
choice** — uniform within-class treatment, no keystroke priors; a frequency-weighted
objective could rank schemes differently in expectation and is a named data-requiring
follow-up; the class-exact censuses themselves are prior-free facts. (b) **The
impossibility's scope is position-wise abelian mod-10** — the head's own R3 arm lives
outside that scope (Damm) and thrives, so the theorem is registered WITH its boundary;
a reader over-generalizing it to "all digit schemes" is refuted by the head itself.
(c) **The Damm table is a pinned constant** — a transcription error in the drafter's
table fails the property gates as INVALID and the Damm-failure NULL axis prices
exactly that; R2 and R1 stand independent of R3's table. (d) **Band placement could
cherry-pick** — every band is an exact-equality census committed before the sim, the
expected landing is DISCLOSED (REJECT), and the falsifiability worlds are structural:
one symbol dissolves the floor, one algebra evades it, and the drafter's own corrected
multiplicity error is pre-registered as a live NULL axis rather than buried.
(e) **Length-4 enumeration could hide length effects** — the position-census reduction
is verified by typed must-equal contacts (multiplicity law asserted directly), and
full-length counts are boundary-count products (an identity); a contact failure is a
named NULL, not a silent extrapolation.

**5. What does it unlock?** The pipeline's FIFTEENTH fleet-external verdict and the
rotation lane's domain-coverage proof extended (voting → routing → tournaments →
pattern races → stopping → spatial self-organization → queueing → ratchets →
occupancy → random incidence → reciprocity → observational learning → two-sided
matching → group testing → algebraic error detection); a measured, citable answer to
"what does a check digit actually catch" with three standalone pins (the floor-2
certificate and its complete census; the Luhn-optimality fact with the named 09↔90
miss; the ISBN-10 → EAN-13 regression priced at 120 + 990 escape patterns); and a
transferable identifier-integrity correction for every fleet surface that mints or
copies coded identifiers — including the venture lane's own book ISBNs, which live
on the weak side of the priced migration.

**6. What is the cheapest experiment that decides it?** The whole head IS the cheapest
deciding experiment: Arm A settles every decision number exactly in seconds with no
seed. The single cheapest probe if a reader doubts a specific leg is three lines of
pencil: the boundary differences of ANY two digit maps sum to 0 mod 10; a permutation
of Z10 sums to 45 ≡ 5; 0 ≠ 5 — so some swap always escapes. And the famous miss by
hand: with the left digit doubled, 09 digests to 0 + L(9) = 9 and 90 to 9 + L(0) = 9
— identical, undetected.

**7. What would make this a mistake to run?** If the exact treatment were unavailable
(it is not — the whole decision surface is finite integer counting, exhaustively
enumerable including the 10! space), if the domain duplicated a prior head (it does
not — zero domain hits in both trees, no recorded drop, and the P072 adjacency is
argued and dismissed explicitly: stochastic screening economics vs deterministic
codeword algebra), or if the disclosed REJECT made the run theater. It does not: the
value is the independent hermetic re-derivation of the complete quotient census (the
floor and its 46,400-cell attaining set are counted facts a wrong implementation
would miss), the Damm table's properties re-verified from the pinned constant, the
typed contacts re-checked against exactly the multiplicity error the drafter actually
made once, and both non-REJECT rulings genuinely reachable (APPROVE is one certificate
error away; the census-contact and Damm-failure NULLs are one real mistake away).

**8. How will we know it worked?** A committed sim-lab report with: the complete U
histogram over all 3,628,800 quotients (bins, counts, total), the floor and its
attaining count, Luhn's miss set, the 16-cell linear grid partition, the ISBN-10 /
EAN-13 / ALL-ONES / Damm censuses with the full-code pattern counts 120/990, all four
word-level enumerations with their typed must-equal contacts, the F1–F6 gate results,
the verdict token against the pre-registered bands, Arm R's measured miss rates
beside the exact censuses (reporting-only, draw counts asserted), and a byte-identity
note (two process runs identical). A clean run reproduces the drafter's disclosed
reference values (min U = 2 at 46,400; Luhn {(0,9),(9,0)}; EAN 10/90 + 90/90; Damm
0/900 + 0/900; contacts 60/300/1800/0) from scratch, or — the more interesting
outcome — DISAGREES and pins the drafter's error, which the pre-registered rule then
rules on honestly (the census-contact and Damm-failure NULL axes exist for exactly
that).

**Recommendation: sim-ready**
