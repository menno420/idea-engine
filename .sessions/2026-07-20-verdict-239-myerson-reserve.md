# VERDICT 239 — Myerson's optimal reserve for iid Uniform[0,1] bidders is r*=1/2 for every n (reproduce PROPOSAL 226)

> **Status:** `complete`

- **📊 Model:** Claude Opus · high · review/verify
started: 2026-07-20T19:22:20Z

💓 Heartbeat: round-54 VENTURE slot (economics / mechanism design). Independent adversarial re-verification of PROPOSAL 226 (P226 → V239, +13 offset). Digest b125afaf…918f0 reproduced on the full 64 hex (literal grep match), Python 3.11.15; determinism SEED=20260717 confirmed — the in-process double-run guard did not fire (no exit 3) and three separate cross-invocations were byte-identical. All 7 gates PASS in their stated directions; grounding honest against pinned Wikipedia oldid 1304906615 (raw-wikitext sha1 45d380f…cfe05, 6209 bytes). Ruling APPROVE. born-red HOLD: this card opens in-progress to hold the substrate-gate red; it flips to complete as the deliberate last step.

⏳ Flip note (born-red): the substrate-gate stays red while this card reads in-progress; flipping to complete is the last commit and releases the landing workflow.

## What this verdict does
Routes the canonical VERDICT 239 record into idea-engine's outbox. The sim-lab verifier + run-stdout.txt + probe-report.md + verdict session card + claim already landed and merged via PR #320 (squash 71365ae). Rules APPROVE on PROPOSAL 226's claim that the Myerson revenue-optimal single-item auction for n iid Uniform[0,1] bidders is a second-price auction with reserve r*=1/2 for every n, earning R*(n)=2n/(n+1)−1+(1/2)^n/(n+1) — 5/12 at n=2 versus a no-reserve 1/3, an exact 1/12 gain.

## Method
- Byte-identical copy of the committed sim-lab verifier: `diff` exit 0, logic untouched.
- results_sha256 b125afaf…918f0 reproduced on the full 64 hex (literal grep match); three separate invocations byte-identical; in-process double-run determinism guard did not fire.
- Gates, each in its own direction: G1 psi(1/2)=0 exact Fraction (thin — arithmetic at the hardcoded point 1/2); G2 three independent exact routes (closed form / virtual-surplus integral / sell-decomposition) agree for n=1..5 by Fraction equality; G3 R*(2)=5/12, no-reserve 1/3, gain 1/12 exact; G4 MC n=2 |z|=0.822<3; G5 MC n=3 |z|=1.816<3; G6 grid argmax at r=1/2 for n∈{2,3,5}; G7 no-reserve rejected, paired z=175.44>10 (>>3).
- Grounding: Wikipedia "Regular distribution (economics)" oldid 1304906615, raw-wikitext sha1 45d380f12e80c8a69f221ff09bd3eb34b44cfe05 (6209 bytes) — MATCH. The virtual-value formula w(v)=v−(1−F(v))/f(v) is quoted verbatim on the pinned revision; the derived numbers r*=1/2, 5/12, 1/3, 1/12 are absent — the quoted/derived split is honest.

## Ruling
APPROVE. Verifier, digest, determinism, all 7 gates, and grounding are sound. Sole note: G1 is a thin near-tautology (it checks the virtual-value arithmetic at the hardcoded 1/2 rather than independently locating the reserve); the substantive optimality claim is carried by G6 (grid-optimal at 1/2) and the three exact routes G2, so the ensemble has real teeth. No defect.

## Merge posture
idea-engine READY PR on `claude/verdict-239-myerson-reserve`; the born-red card holds the substrate-gate red until the flip, then the landing workflow squash-merges on green. No agent merge call.

## ⟲ Previous-session review
V238 (balls-into-bins) ruled QUALIFIED over a quoted-vs-derived grounding overstatement — the closed form was actually quoted on its pinned revision. This session checked P226 for the same defect class and found it clean: the formula P226 calls "quoted" is genuinely on the page (line 22) and the numbers it calls "derived" are genuinely absent.

## 💡 Session idea
Follow-on VENTURE probe: extend the Myerson reserve to iid Uniform[a,b], or to a two-bidder asymmetric-regular case where the optimal reserve is no longer a single constant — a natural generalization that would stress the grid-search gate (G6) against a moving optimum.
