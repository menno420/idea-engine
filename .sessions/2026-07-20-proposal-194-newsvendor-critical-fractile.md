# PROPOSAL 194 — newsvendor critical fractile: stock the high-margin product ABOVE its expected demand (round-46 VENTURE slot, P194 → V207, +13)

> **Status:** in-progress
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD.** This card lands `in-progress` on the FIRST commit to hold the proposal PR red on the born-red convention; it flips to `complete` as the LAST commit, after the verifier reproduces byte-identical (results-dict sha256, in-process double-run + separate cross-invocation) and the G1/G2/G3/G4 battery passes green (all_pass=true). Merge-on-green is the only merge path — this session issues zero merge calls.

## 💡 Session idea
The folk rule "order what you expect to sell — set the order quantity to mean demand" is provably wrong for a high-margin product: the profit-maximizing order quantity is the critical-fractile QUANTILE of demand, Q\* = smallest Q with CDF(Q) ≥ (p−c)/(p−s), and for a high-margin good the critical ratio exceeds 1/2, so the optimal stock sits STRICTLY ABOVE the mean. The counterintuitive direction is a lever, not a curiosity: the same closed form says a low-margin good should be stocked BELOW the mean, and only at the exact balance point (critical ratio = 1/2) does the mean/median coincide with the optimum. The mechanism is marginal analysis — the marginal expected value of the (Q+1)-th unit is (p−s)·(critical ratio − CDF(Q)), positive until the CDF crosses the critical ratio — which makes the quantile the exact, provable argmax of expected profit, not an approximation.

## ⟲ Previous-session review
P193 (price of anarchy — selfish two-pool routing costs at most 4/3 of the optimum, tight in the Pigou case; round-46 FLEET opener, lane fleet) landed via claim PR #718 + born-red proposal PR #719 and is queued P193 → V206 (+13) on the outbox ledger; its verifier reproduced byte-identical (results-dict sha256 9fc650416ae0907bddc988addf0ae4cf76d336a062a9bdaa5aef95eea6d5dcda) with G1 exact grid-enumeration ≡ closed form (PoA=4/3), G2 best-response convergence, G3 ≥3σ random-instance, G4 regime-shift control all green. The round-46 rotation (fleet→venture→game→unrelated) advances to the VENTURE slot; this session opens P194 → V207 (+13). Claim PR #721 (control fast-lane) opens before this born-red proposal PR.

## Objective
Author + land PROPOSAL 194 → VERDICT 207 (+13): the newsvendor critical-fractile result (stock a high-margin product above its mean demand; the optimum is a quantile, not the mean), with a stdlib deterministic verifier (SEED=20260717) carrying an exactly-true full-enumeration argmax gate, a ≥3σ paired Monte-Carlo gate, a critical-ratio-shift monotonicity gate, and a second exactly-true marginal-analysis identity gate.

## Constraints honored
- stdlib-only verifier (hashlib, json, math, random, fractions); SEED=20260717; byte-identical across in-process double-run + separate invocation.
- PR opens READY; merge-on-green only (zero agent merge calls); born-red HOLD via this card.
- No model version identifiers; timestamps from `date -u`; external grounding pinned live (Wikipedia "Newsvendor model" raw-wikitext rev sha1).
- DEDUP clean: an author-time grep of ideas/ for newsvendor / "critical fractile" / "critical ratio" / "order quantity" / newsboy returned zero real hits before authoring.

## Pinned world (committed constants, SEED=20260717)
Demand D ~ Binomial(n=40, p=1/2) on integers 0..40 (mean=20, median=20), EXACT pmf C(40,k)/2^40 via `fractions.Fraction`. Economics profit(Q,d) = p·min(Q,d) + s·max(Q−d,0) − c·Q; critical ratio CR=(p−c)/(p−s); critical-fractile Q\* = smallest integer Q∈[0,40] with exact CDF F(Q) ≥ CR. Three cases (all s=0): HIGH margin p=10,c=2 → CR=4/5 → Q\*=23 (ABOVE mean 20); LOW margin p=10,c=8 → CR=1/5 → Q\*=17 (below mean); MID p=10,c=5 → CR=1/2 → Q\*=20 (=median). Z_GATE=3.0; Monte-Carlo T=200000 paired draws; fresh `random.Random(20260717)` at the top of every full run. Digest posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY.

## Gate-plan (pre-registered — frozen, z_gate = 3.0)
- **G1 exactly-true argmax:** for every case, the closed-form critical-fractile Q\* EQUALS the argmax over Q∈[0,40] of the EXACT expected profit E[profit(Q)] (full enumeration over the demand support with Fraction, exact rational argmax, tie→smallest Q). Exact equality, no tolerance.
- **G2 ≥3σ Monte-Carlo:** HIGH-margin case, T=200000 PAIRED demand draws; realized mean profit at Q\* minus at Q=20 (the mean-stocking naive choice); z = mean_diff / (sd_diff/√T) ≥ 3.0 and POSITIVE (stocking above the mean genuinely wins), plus a second ≥3σ on the mean-of-differences vs 0.
- **G3 robustness/shift:** sweep CR over c=0..10 (s=0, p=10); Q\*(CR) monotone non-decreasing in CR AND Q\*>median iff CR>1/2, Q\*<median iff CR<1/2, Q\*=median at CR=1/2 (the counterintuitive direction holds across the whole shift).
- **G4 second exactly-true / marginal-analysis:** the closed-form marginal increment ΔE(Q)=E[profit(Q+1)]−E[profit(Q)] = (p−s)·(CR−F(Q)) equals the enumerated difference for ALL Q in every case (exact Fraction equality), and ΔE>0 for Q<Q\*, ΔE≤0 for Q≥Q\* — proving Q\* is the exact profit argmax analytically.
- all_pass = G1 ∧ G2 ∧ G3 ∧ G4.

## GROUNDING (verified live)
Wikipedia "Newsvendor model" (oldid 1363763252) fetched live this session (action=raw), carrying the critical-fractile formula `q = F^{-1}((p−c)/p)` and the "critical fractile" naming that balances understock cost (p−c) against total over/understock cost; with salvage s=0 the pinned cases' CR=(p−c)/(p−s)=(p−c)/p matches the article's ratio exactly. Rev sha1 ae457d1c0419c2c3f6aa5f911e31f98a8d7b50a0 (MediaWiki-reported revision sha1) pins the wikitext. Honest caveat: the article states the salvage-free (p−c)/p ratio; the general (p−c)/(p−s) with salvage is the standard textbook extension and the pinned verifier uses s=0, so the two coincide exactly for every pinned case. The exact-enumeration G1/G4 gates are the firsthand witness that Q\* is the true argmax.

## Probe questions
**1. Is the head crisp and falsifiable?** Yes — a single closed form (Q\*=smallest Q with F(Q)≥CR) with three pinned cases and a byte-pinned verifier; falsified if enumerated argmax ≠ Q\* for any case.
**2. Is it counterintuitive-but-true?** Yes — "order what you expect to sell" is wrong for a high-margin good; the optimum is a quantile strictly above the mean (Q\*=23 vs mean 20), provably true by exact enumeration.
**3. Is the model clean and fully pinned?** Yes — Binomial(40,1/2) demand with exact rational pmf, three pinned (p,c,s) cases, SEED committed, nothing tunable post-hoc.
**4. Is there an exactly-true gate?** Yes — TWO: G1 (enumerated argmax ≡ Q\* as exact Fractions) and G4 (marginal identity ΔE(Q)=(p−s)(CR−F(Q)) exact for all Q), no sampling.
**5. Is it deterministic and reproducible?** Yes — fresh random.Random(20260717) per run, in-process double-run asserted canonical-identical before hashing, whole-dict sha256 byte-identical across two invocations.
**6. Is the grounding real and external?** Yes — Wikipedia "Newsvendor model" oldid 1363763252 pinned by rev sha1, carrying the critical-fractile quantile formula; honest s=0 caveat disclosed.
**7. Could it collide with a shipped proposal?** No — author-time grep of ideas/ for newsvendor/critical-fractile/critical-ratio/order-quantity/newsboy returned zero; distinct from the ergodicity/Kelly head (single-period order sizing, not multiplicative growth).
**8. What would make sim-lab reject it?** A non-reproducible digest, the enumerated argmax disagreeing with the closed form under reimplementation, or the marginal identity failing exact rational equality.
