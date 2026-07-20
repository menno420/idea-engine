# PROPOSAL 193 — price of anarchy: selfish two-pool routing costs at most 4/3 of the optimum, exactly 4/3 in the tight Pigou case (round-46 FLEET opener, P193 → V206, +13)

> **Status:** complete
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD (cleared).** This card landed `in-progress` on the first commit to hold the PR red on the born-red convention; it flips to `complete` here as the last commit, after the verifier reproduced byte-identical (results-dict sha256 9fc650416ae0907bddc988addf0ae4cf76d336a062a9bdaa5aef95eea6d5dcda across an in-process double-run and separate cross-invocations) and the G1/G2/G3/G4 battery passed green (all_pass=true).

## 💡 Session idea
Selfish routing across load-dependent server pools is not a rounding error away from optimal — it is off by a bounded, exact constant, and that constant (4/3 for affine latencies, the price of anarchy) is a *lever*, not a curse: it vanishes when the alternative pool is expensive enough (PoA = 1) and maxes at 4/3 when pools are closely matched, so the same closed form tells a fleet exactly when a coordinator or congestion toll pays for itself and when greedy dispatch is already optimal. The dedup twist that produced this head: the assigned Braess head and its designated fallback (power-of-two-choices) were BOTH already shipped, so the genuinely un-built neighbour in the same selfish-routing family — the tight 4/3 efficiency ratio and its Pigou witness, which the Braess docs themselves flagged as a follow-up — became the proposal.

## ⟲ Previous-session review
P192 (100 prisoners, cycle-following survival ≈ 31%, round-45 UNRELATED slot) landed via claim #713 + born-red proposal #715, and was already ruled APPROVE at VERDICT 205 (mirror commit a58d265, sim-lab PR #280) by the time this session woke — the round-45 rotation is closed and round-46 re-opens at the FLEET slot per the outbox `loop:` ledger. No open ORDER in control/inbox.md at HEAD 70ecdf9 (the sync point) requires action; the proposal loop runs live. This session opens P193 → V206 (+13). Claim PR #718 (control fast-lane) opens before this born-red proposal PR.

## Objective
Author + land PROPOSAL 193 → VERDICT 206 (+13): the price-of-anarchy 4/3 bound with its tight Pigou two-pool witness, with a stdlib deterministic verifier (SEED=20260717) carrying an exactly-true grid-enumeration gate, a closed-form-vs-best-response gate, a ≥3σ random-instance gate, and a regime-shift control gate.

## Constraints honored
- stdlib-only verifier (hashlib, json, math, random, fractions); SEED=20260717; byte-identical across in-process double-run + separate invocation (sha256 9fc650416ae0907bddc988addf0ae4cf76d336a062a9bdaa5aef95eea6d5dcda).
- PR opens READY; merge-on-green only (zero agent merge calls); born-red HOLD via this card.
- No model version identifiers; timestamps from `date -u`; external grounding pinned live (Wikipedia "Price of anarchy" raw wikitext sha1).
- DEDUP-pivot disclosed: Braess (three docs) and power-of-two-choices (two docs) already shipped → pivot to the un-built PoA/Pigou head in the same family.

## Pinned world (committed constants)
Two affine server pools, unit demand. PIGOU = top (a=1,b=0)=x, bottom (a=0,b=1)=1 → selfish 1, optimal 3/4, PoA 4/3 (tight witness, G1). INTERIOR = top (1,0), bottom (1,1/2) → eq flow 3/4, avg latency 3/4, PoA 24/23 (G2). SEED=20260717; Z_GATE=3.0; GRID=12; K_QUANTA=4000; BR_TRIALS=50; TRIALS=20000.

## Gate-plan (pre-registered — frozen, z_gate = 3.0)
G1 exact-enumeration: grid {k/12} minimizers ≡ closed forms; PoA = 4/3 exactly (eq flow 1, opt flow 1/2, selfish 1, optimal 3/4). G2 closed-form-vs-best-response: 50 random-start best-response runs on INTERIOR converge to unique k\*=3000, avg latency 3/4 exact. G3 ≥3σ random-instance (paradox band 0<c<a): frac_within_4/3_bound=1.0, frac_positive=1.0, z=229.325562, max_poa=1.328904. G4 regime-shift control (c≥2a): frac_efficient_poa_1=1.0, max_loss=0. all_pass=true.

## GROUNDING (verified live)
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Price_of_anarchy&oldid=1360730011@41ef002fa41f05716003462cc43eb203775b5604 · fetched 2026-07-20

Wikipedia "Price of anarchy" (oldid 1360730011) states the theorem "the pure PoA of any generalized routing problem (G,L) with linear latencies is ≤ 4/3" and "w(f) ≤ (4/3)·min w(f\*)"; sha1 41ef002fa41f05716003462cc43eb203775b5604 pins the raw wikitext (21804 bytes), fetched live 2026-07-20 via action=raw. Honest caveat: the sha1 is over the wikitext SOURCE, not the rendered HTML; the specific Pigou witness (1 vs 3/4) is the textbook tight instance, established firsthand by the G1 enumeration gate.

## Probe questions
**1. Is the head crisp and falsifiable?** Yes — a single exact ratio (4/3) with closed forms and a byte-pinned verifier.
**2. Is it counterintuitive-but-true?** Yes — greedy local routing is off by a provable constant; selfish pays exactly 4/3 of optimal at Pigou.
**3. Is the model clean and fully pinned?** Yes — two affine pools, unit demand, PIGOU/INTERIOR instances, SEED committed, nothing tunable post-hoc.
**4. Is there an exactly-true gate?** Yes — G1 grid enumeration matches the closed forms exactly (PoA = 4/3 as an exact Fraction), no sampling.
**5. Is it deterministic and reproducible?** Yes — sha256 9fc65041…d5dcda byte-identical across two processes.
**6. Is the grounding real and external?** Yes — Wikipedia "Price of anarchy" oldid 1360730011 pinned by raw-wikitext sha1, stating the ≤4/3 bound; Pigou witness firsthand (honest caveat disclosed).
**7. Could it collide with a shipped proposal?** No — no PoA/Pigou head exists; distinct from the three Braess heads and two power-of-two-choices heads (see doc Dedup).
**8. What would make sim-lab reject it?** Non-reproducible digest, a gate failing under reimplementation, or closed forms disagreeing with an independent equilibrium/optimum solver.
