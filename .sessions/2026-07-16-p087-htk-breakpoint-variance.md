# Session — PROPOSAL 087: round-18 game-mechanics slot (hits-to-kill breakpoint-variance comb — consistency beats raw power)

> **Status:** `complete`
> **📊 Model:** opus-class · high · idea/planning
>
> *(card born in-progress at 2026-07-16T18:59:30Z as the designed session-gate HOLD — the born-red first commit; flips complete in this PR's final commit at 2026-07-16T19:37:10Z after the drafting work lands.)*

## Scope / objective
Draft + land PROPOSAL 087 — the round-18 GAME-MECHANICS slot (standing ORDER 003 · rotation per ORDER 004 rule 3: round-18 opener P085 = fleet-backlogs, P086 = venture, so game is next) → sim-lab VERDICT 100 (+13 offset). One genuinely new idea, deduped against P001–P086 and the full ideas/ game lanes.

## Results
1. HARD-SYNC clean; idea-engine @ 6c36e66, sim-lab @ ce3dace; `check --strict` GREEN at boot (exit 0, advisories only). Branch `claude/p087-htk-breakpoint-variance`.
2. Pipeline: P086 → V099 ACCEPT closed the round-18 venture slot; P087 fills the game slot and refills the pipeline toward V100.
3. Idea: two equal-cost damage builds — TIGHT (per-hit Uniform[100,110], mean 105, low variance) vs WILD (Uniform[75,165], mean 120, high variance) — against an enemy killed by cumulative damage ≥ H. Claim: the LOWER-mean, low-variance build kills in FEWER hits when enemy HP sits at a hits-to-kill breakpoint (variance spills a roll below the breakpoint and costs a whole extra hit), and the advantage RECURS on a comb at multiples of the tight build's damage floor, reversing only once the higher mean saves a full hit. Four pre-registered gates R1–R4. Grounded firsthand in the game-mechanics idea tree @ 6c36e66.
4. Calibrated on a throwaway stdlib dry-sim (seeds [1..5], C=4000, common random numbers; NOT committed): R1 (H=100) TIGHT 1.00000 < WILD 1.27850, +0.2785, 74.90σ; R2 (H=500) WILD 4.69050 < TIGHT 5.00000, −0.3095, 110.60σ; R3 floor+monotonicity hold; R4 sign comb [+,+,−,+,−] over H∈{80,100,140,300,500} (each ≥40σ, all-seeds-consistent) + deterministic control (variance removed) has WILD ≤ TIGHT everywhere. Disclosed landing ACCEPT.
5. Appended PROPOSAL 087 to control/outbox.md (status: sim-ready) exactly once; SEEDLESS (block 20261730 left untouched).
6. Housekeeping: pruned the terminal claims control/claims/p086-round18-venture-readthrough.md and control/claims/2026-07-16-v099-readthrough-mirror.md (both PRs #460/#461 merged/terminal, verified live).
7. Claim filed; heartbeat status.md refreshed (next-2 baton: (1) VERDICT 100 for P087, (2) sim-lab ORDER-010(c) kit upgrade still parked on owner auth + monitor ASK 005/006).

## Constraints honored
Born-red session-gate HOLD (this card flips complete only in the final commit); append-only outbox (one block); TRUTH bar (the damage distributions, H grid, C, seeds are disclosed as stipulated pinned constants, not estimated); the V098/P086 calibrate-against-the-world lesson embodied — the FIRST R4 registration (d stays negative above the crossover) was FALSIFIED by the dry-sim's H=300 recurrence and corrected to the true discreteness-comb pattern BEFORE registering, so the sim (not a guess) sets the gate; guard-fires.jsonl never staged; bootstrap green before the flip.

## 💡 Session idea
Enemy HP tuned to round numbers (100, 300, 500…) is near-universal in game content, and this head shows those round numbers silently reward low-variance damage builds — a hidden balance lever. The reusable drafting-battery item this surfaces (distinct from this proposal's mechanic): before registering any gate on a metric that passes through a CEILING or FLOOR function (ceil/floor/round — HTK here, the read-through cap in P086), sweep the input across a full lattice period, not a single point, because a ceiling metric produces PERIODIC (comb) reversals a single-point registration misreads as monotone — exactly the trap that falsified this head's first R4. Worth promoting from a per-head catch to a named "sweep-the-lattice-period" battery gate. (Logged for a later round, not pursued here.)

## ⟲ Previous-session review
P086 (round-18 venture slot, series read-through concentrate-vs-spread saturation crossover) → VERDICT 099 ACCEPT (sim-lab PR #171, idea-engine mirror #461), cleanly finalized. All four gates passed (R1 29.81σ, R2 156.67σ, R3 well-posed, R4 crossover B*=22 at the r_max ceiling). The +13 P→V offset held (P086→V099). No defects in the predecessor's landing discipline (born-red gate, heartbeat-last, SEEDLESS baton, append-only outbox all followed). This session inherits a green tree and refills the game slot toward V100. P086's explicit lesson — register gate legs against the world's OWN stability bound, calibrated on a dry-sim — is carried forward and, notably, EARNED its keep here: the dry-sim falsified this head's naive first R4 and forced the corrected comb registration, the calibrate-against-reality discipline working as designed.
