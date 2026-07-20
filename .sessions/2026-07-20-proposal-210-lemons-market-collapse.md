# PROPOSAL 210 — Akerlof lemons market collapse: a fully mutually-beneficial market destroyed by quality uncertainty (round-50 VENTURE slot, P210 → V223, +13)

> **Status:** in-progress
📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD.** This card lands `in-progress` on the FIRST commit to hold the proposal PR red on the born-red convention; it flips to `complete` on the LAST commit of this session, after the verifier reproduces byte-identical and the G1–G4 battery passes green. Merge-on-green is the only merge path — this session issues zero merge calls.

## 💡 Session idea
The folk belief "if every possible trade is win–win, the market will function" is provably wrong. On a uniform quality grid Q = {1,…,1000} with seller reservation q and rational buyer valuation βq at β = 3/2 — so βq > q, EVERY trade strictly benefits both sides, with no transaction cost and no irrationality — a competitive buyer who cannot observe quality prices against the *offered* pool, which self-selects on hidden type: at price p the offered set is {q ≤ p}, mean (p+1)/2, so the buyer pays p iff p ≤ β·(p+1)/2. That interval closes at p* = ⌊β/(2−β)⌋ = 3 out of 1000. Only the 3 worst qualities trade; the destroyed fraction of mutually-beneficial gains is D = 1 − p*(p*+1)/(N(N+1)) ≈ 0.999988. The collapse is driven by β's distance below 2, essentially independent of N — so a LARGER market with more win–win trades available deepens the failure (surviving fraction p*/N → 0). Adverse selection needs no friction; the rational-expectations price on an endogenously-selected pool is the whole cause.

## ⟲ Previous-session review
P209 (Maekawa grid quorums — a √N-size row∪column read/write set of 2k−1 cells on a k×k grid guarantees intersection just as well as a majority, so *structure*, not size, buys mutual exclusion; two random same-size subsets can be disjoint) opened the round-50 FLEET slot and is queued P209 → V222 (+13) on the outbox ledger; its verifier reproduced byte-identical (results-dict sha256 bbc54843f3693815f107f95df069c26d985a3799b2afe2c0f689a38e3659096f) with G1 exhaustive grid-quorum-pair intersection fraction == Fraction(1) at k=6, G2 MC disjoint-rate agreeing with the closed form C(25,11)/C(36,11) at |z|<3, G3 the same disjoint-rate significantly >0 at z=122.5≥3, G4 the k∈{4..10} shift, and G5 determinism all green. The round-50 rotation (fleet→venture→…) advances to the VENTURE slot; this session opens P210 → V223 (+13). Note the head pivoted: an earlier venture candidate slug `bertrand-paradox` was already taken by P196 (an unrelated random-chord card), so this VENTURE slot lands the Akerlof lemons collapse instead (slug `lemons-market-collapse`, zero prior hits in ideas/).

## Objective
Author + land PROPOSAL 210 → VERDICT 223 (+13): the discrete Akerlof lemons-market collapse (a fully mutually-beneficial market destroyed by quality uncertainty; equilibrium price p* = min(N, ⌊β/(2−β)⌋), destroyed fraction D = 1 − p*(p*+1)/(N(N+1))), with a stdlib deterministic verifier (SEED=20260717) carrying an EXACT closed-form-vs-exhaustive-scan p* gate, a ≥3σ Monte-Carlo surprise gate, a robustness/shift monotone-collapse gate, and an EXACT surplus-identity gate.

## Constraints honored
- stdlib-only verifier (hashlib, json, math, random, fractions); SEED=20260717; byte-identical across in-process double-run + two separate cross-invocations.
- PR opens READY; merge-on-green only (zero agent merge calls); born-red HOLD via this card.
- No model version identifiers; timestamps from `date -u`; external grounding pinned live (Wikipedia "The Market for Lemons" revision sha1, independently re-sha1sum-ed).
- DEDUP clean: author-time grep of ideas/ for lemons / adverse-selection / akerlof / market-for-lemons returned zero hits; explicitly distinguished from partner-channel-margin-stacking (double-marginalization) and P206 independent-screens-odds-ladder (screening).

## Pinned world (committed constants, SEED=20260717)
Quality grid Q = {1,…,N} uniform prior; seller reservation(q) = q; buyer valuation(q) = β·q with β a `fractions.Fraction`, 1 < β < 2. Offered set at integer price p is S(p) = {q ≤ p}, E[q|S(p)] = (p+1)/2. Equilibrium max trading price p*(β,N) = max{p∈{0..N} : p ≤ β·(p+1)/2} = min(N, ⌊β/(2−β)⌋) with EXACT `Fraction` floor. Destroyed fraction D(β,N) = 1 − p*(p*+1)/(N(N+1)). Pinned: β = Fraction(3,2), N = 1000 ⇒ p* = 3, predicted trade rate 3/1000, D = 250247/250250 ≈ 0.999988012. Battery: β ∈ {11/10, 5/4, 4/3, 3/2, 5/3, 7/4, 9/5, 19/10}, N ∈ {50, 100, 500, 1000, 5000}. z_gate = 3.0; Monte-Carlo M = 200000 with fresh `random.Random(20260717)` at the top of every full run. Digest posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY.

## Gate-plan (pre-registered — frozen, z_gate = 3.0)
- **G1 EXACT (direction: exact agreement, discrepancies = 0):** over the full (β,N) battery, closed form p*_closed = min(N, ⌊β/(2−β)⌋) EQUALS exhaustive-scan p*_scan (scan p=0..N with the exact `Fraction` willingness test, max willing p). Frozen threshold: discrepancies = 0.
- **G2 SURPRISE (direction: HIGH z, z ≥ 3.0):** pinned world Monte-Carlo, M = 200000; full-info trade always (rate 1), asymmetric-info trade iff q ≤ p*; z = (0.5 − r_hat)/se against H0 = "at least half the mutually-beneficial market survives" (rate 0.5). Frozen threshold: z ≥ 3.0 (measured z = 4077.83).
- **G3 ROBUSTNESS/SHIFT (direction: persistence — monotone + near-total collapse):** full grid D(β,N); (i) D weakly increasing in N for each β; (ii) exact residual |D_measured − D_closed| == 0 everywhere; (iii) min over all β of D(β, N=5000) ≥ 0.99. Frozen thresholds: monotone = true, residual = 0, min-D(N=5000) ≥ 0.99 (measured min-D = 0.999984803 at β=19/10).
- **G4 EXACT identity (direction: exact, discrepancies = 0):** D closed form == 1 − (explicit Σ_{q≤p*} q)/(explicit Σ_{q≤N} q) across the battery. Frozen threshold: discrepancies = 0.
- all_pass = G1 ∧ G2 ∧ G3 ∧ G4. **Measured this run: all_pass = true, first_failing_gate = null; RESULTS_SHA256 = b0251b0aa024e235fa4991c005c1cd3deaa3a04f2fcd2e5d4e041e6e21237539 (byte-identical across in-process double-run + two separate cross-invocations).**

## GROUNDING (verified live)
Wikipedia "The Market for Lemons" (oldid 1358736918) fetched live this session (action=raw), carrying "adverse selection", "asymmetric information", "quality uncertainty", and "market collapse" verbatim — firsthand support for the head. Revision sha1 34c3ec139bfdd21dc2d0a30ddd895bade01f6a3c (40-hex), independently re-computed by `sha1sum` over the raw wikitext this session to the SAME value — a clean, reproducible byte-pin. Honest caveat: the article describes the phenomenon/model qualitatively; the exact collapse threshold p* = ⌊β/(2−β)⌋ and the destroyed-fraction closed form D = 1 − p*(p*+1)/(N(N+1)) are our own discrete instantiation, not lifted from the page. The exact G1/G4 gates are the firsthand witness.

## Probe questions
**1. Is the head crisp and falsifiable?** Yes — closed form p* = min(N, ⌊β/(2−β)⌋) on a byte-pinned battery; falsified if the exhaustive scan disagrees for any (β,N) pair (G1) or the surplus identity fails exact rational equality (G4).
**2. Is it counterintuitive-but-true?** Yes — a market where EVERY trade is win–win collapses to ~0.3% of volume from hidden quality alone, provably by exhaustive scan and surplus identity; G2 puts realized survival 4078σ below the "half survives" folk null.
**3. Is the model clean and fully pinned?** Yes — uniform quality grid, seller reservation q, buyer valuation βq with β = Fraction(3,2), N = 1000, SEED committed; p* and D exact Fractions, nothing tunable post-hoc.
**4. Is there an exactly-true gate?** Yes — TWO: G1 (closed form ≡ exhaustive Fraction scan) and G4 (D ≡ explicit surplus-ratio identity), both 0 discrepancies, no sampling.
**5. Is it deterministic and reproducible?** Yes — fresh random.Random(20260717) per run, in-process double-run asserted canonical-identical before hashing, whole-dict sha256 b0251b0a…21237539 byte-identical across two invocations.
**6. Is the grounding real and external?** Yes — Wikipedia "The Market for Lemons" oldid 1358736918 pinned by the 40-hex revision sha1 34c3ec13…, independently re-sha1sum-ed; honest "threshold is ours" caveat disclosed.
**7. Could it collide with a shipped proposal?** No — author-time grep of ideas/ for lemons/adverse-selection/akerlof returned zero; distinguished from partner-channel-margin-stacking (double-marginalization) and P206 independent-screens-odds-ladder (screening).
**8. What would make sim-lab reject it?** A non-reproducible digest, the exhaustive scan disagreeing with the closed-form p* under reimplementation, the surplus identity failing exact rational equality, or the G2 collapse z falling below 3σ.
