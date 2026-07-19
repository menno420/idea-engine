# PROPOSAL 168 — Condorcet's paradox: rational voters, an irrational majority

> **Status:** `complete`
> 📊 Model: Claude Opus · high · proposal/idea-generation

Born-red HOLD: this card lands first with `Status: in-progress` to hold the PR red on the substrate gate; it flips to `complete` as the final commit, after the outbox block, releasing the landing workflow. A red gate before that flip is the HOLD, not a defect.

## Objective
Author PROPOSAL 168 (round-39 UNRELATED slot) — a stdlib verifier + proposal doc for the Condorcet voting-cycle paradox: transitive (rational) individual preferences compose into an INTRANSITIVE collective majority (no Condorcet winner) at a documented, quantifiable rate. Targets sim-lab VERDICT 181 (+13 offset).

## Constraints honored
- stdlib-only Python 3; SEED=20260717 pinned.
- deterministic in-process double-run + cross-invocation identical.
- >=3 sigma gates incl. a robustness gate under a shifted distribution.
- grounding URL verified live HTTP 200 this session.
- merge-on-green (zero merge calls).
- family model names only; timestamps from `date -u`.

## GROUNDING (verified at HEAD)
`https://en.wikipedia.org/wiki/Condorcet_paradox@1360635422 · fetched 2026-07-19T11:48:46Z` — resolves live HTTP 200 this session; documents (a) transitive individual preferences producing a cyclic majority ("even if every voter's individual preferences are rational and avoid self-contradiction"), and (b) the impartial-culture no-Condorcet-winner probability: 8.690% at n=101, asymptotic 8.77% for m=3, and a candidate-scaling table rising 8.4→16.6→24.2→35.7% for m=3,4,5,7.

## Pre-registered Gate-plan (z_gate=3.0)
- **G1 — head (cycles exist):** impartial culture, m=3, n=101 voters, N=40,000 elections — the share with no Condorcet winner is >=3 sigma above zero; rejects the folk belief that rational individuals compose into a consistent group ranking.
- **G2a — documented magnitude:** the measured m=3 no-Condorcet-winner rate lands within 3 sigma of the documented impartial-culture value 8.690% (source n=101 row).
- **G2b — monotone in candidate count:** the rate strictly increases across m=3<4<5<7 (n=101), each successive step >=3 sigma, matching the documented candidate-scaling trend.
- **G3 — robustness under a shifted distribution:** under a mild popularity tilt (Plackett–Luce weights 1.00/0.85/0.72), cyclic majorities persist >=3 sigma above zero — the paradox is not an artifact of perfect symmetry.
- Decision rule: sim-ready iff G1 ∧ G2a ∧ G2b ∧ G3 all pass; else revise.

## Probe questions
**1. Is "no Condorcet winner" the same as a full 3-cycle?** For m=3 they coincide (no winner ⇒ a top cycle); for m≥4 the verifier gates the documented "no Condorcet winner" quantity, which is exactly what the source measures.
**2. Could pairwise ties inflate the count?** No — n=101 is odd, so every pairwise majority is strict; ties are impossible by construction.
**3. Does the mild tilt secretly still allow a guaranteed winner?** No — weights 1.00/0.85/0.72 keep all three rankings live; G3 measures, not assumes, that cycles persist.
**4. Is the 8.690% target cherry-picked?** It is the source's own n=101 impartial-culture row; the asymptotic 8.77% is disclosed as the large-n limit, and G2a gates the finite-n value actually simulated.
**5. Why not gate m=4,5,7 against absolute documented numbers?** The source's scaling table uses 25 voters while the verifier uses 101, so only the monotone trend is gated, not the absolute values — disclosed.
**6. Is determinism real?** A fresh random.Random(SEED) drives every draw; the harness runs the trial function twice in-process and asserts byte-identical canonical JSON; the digest reproduces cross-invocation.
**7. Does this collide with the committed Condorcet Jury head?** No — the Jury Theorem head is a correlated-accuracy ceiling; this is the paradox of cyclic majority preference (no Condorcet winner). Distinct mechanism, disclosed in Dedup.
**8. What breaks the effect?** Single-peaked / spatial preferences (Black's theorem) collapse the cycle rate toward zero; disclosed as a non-gated crossover, not claimed as robustness.

## Outcome
Landed. Verifier ships all four gates and passes deterministically (in-process double-run byte-identical): G1 head z_vs_zero=61.46; G2a |z_vs_documented|=0.44 (<3, measured m=3 rate 0.086275 vs documented 0.0869); G2b monotone step-z 19.39/11.95/18.63 (each >=3); G3 robustness under the Plackett-Luce tilt z_vs_zero=21.33. Results-JSON sha256 70de2ab46cf482130fa35b051f579d72215efa757dfcf7b5f60e56d85fc08fbe. Grounding Condorcet_paradox@1360635422 resolved live HTTP 200 and documents the cyclic-majority mechanism and the ~8.7% impartial-culture rate. PR #651.

## ⟲ Previous-session review
P167 (MMR/Elo rating deflation, round-39 GAME, sim-ready -> V180) cleanly separated the two point flows: G2's churn-ledger identity nails |residual| to 0.0, proving the drift is 100% churn and 0% game outcome — a genuinely load-bearing mechanism anchor rather than a decorative extra gate. The independent-stream framing for baseline vs. shifted worlds (G3) was honest about conservativeness. Nit: the z-values are enormous (z=-78, z=-131), which reads more like an over-powered N than a delicate effect — a smaller sample would still clear 3 sigma and leave the demonstration less brittle-looking.

## 💡 Session idea
A future unrelated-slot mechanism: the discursive-dilemma / doctrinal-paradox head — majority voting on logically connected propositions (premises vs. conclusion) can return a collectively inconsistent judgment set even when every individual is consistent, the judgment-aggregation analogue of Condorcet's preference cycle. Same "rational parts, irrational whole" spine, disjoint domain (courts/committees), and a clean stdlib majority-aggregation verifier.
