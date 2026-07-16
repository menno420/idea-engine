# Session — PROPOSAL 086: round-18 venture slot (series read-through concentrate-vs-spread saturation crossover)

> **Status:** `in-progress`
> **📊 Model:** opus-class · high · idea/planning
>
> *(card born in-progress at 2026-07-16T17:45:09Z as the designed session-gate HOLD — the born-red first commit; flips complete in this PR's final commit after the drafting work lands.)*

## Scope / objective
Draft + land PROPOSAL 086 — the round-18 VENTURE slot (standing ORDER 003 · rotation per ORDER 004 rule 3; round-18 opener P085 was the fleet-backlogs opener, venture is next in the rule-3 rotation) → sim-lab VERDICT 099 (+13 offset). One genuinely new idea, deduped against P001–P085.

## Results
1. HARD-SYNC clean; idea-engine @ 8c83fef, sim-lab @ 5d8a45e; `check --strict` GREEN (exit 0, advisories only). Branch `claude/p086-readthrough-saturation-crossover`.
2. Pipeline: P085 → V098 REJECT closed the round-18 fleet-backlogs opener; P086 fills the venture slot and refills the pipeline toward V099.
3. Idea: a KDP author's fixed quality budget B split across an N=4-book series' read-through funnel — CONCENTRATE (all on book 1) vs SPREAD (even). Claim: a saturation-driven CROSSOVER budget B\* where the optimal allocation flips from concentrate to spread, CAUSED by the entry step hitting the read-through ceiling r_max (the world's stability bound). Four pre-registered gates R1–R4 (R1 reach-regime concentrate wins at B=6, R2 saturation-regime spread wins at B=33, R3 stability r_k∈[0.30,0.85] + monotonicity, R4 crossover B\*∈(11,22] with concentrate FLAT). Grounded firsthand in the venture-lab idea tree @ 8c83fef.
4. Calibrated on a throwaway stdlib dry-sim (seeds [1..5], C=2000, common random numbers; NOT committed): no realized r_k exceeded r_max; R1 margin 29.8σ, R2 margin 156.7σ (both ≫ 3σ); B\* = 22 ∈ (11,22]; CONCENTRATE flat at 4336.6 books across B∈{11,16,22,33}. Disclosed landing ACCEPT.
5. Appended PROPOSAL 086 to control/outbox.md (status: sim-ready) exactly once; SEEDLESS (block 20261730 left untouched).
6. Claim filed; heartbeat status.md refreshed (next-2 baton: (1) VERDICT 099 for P086, (2) sim-lab ORDER-010(c) kit upgrade still parked on owner auth + monitor ASK 005/006).

## Constraints honored
Born-red session-gate HOLD (this card flips complete only in the final commit); append-only outbox (one block); TRUTH bar (r_base/r_max/slope disclosed as stipulated pinned constants, not estimated); V098 lesson embodied (the gate that flips the answer is registered AT the world's stability bound r_max, not above it — the exact anchor-vs-crossover mistake P085 made); guard-fires.jsonl never staged; bootstrap green before push.

## 💡 Session idea
The V098 lesson ("sanity-check any registered gate anchor against the world's own stability bound") generalizes into a REUSABLE drafting checklist item that no card yet names: before registering ANY gate leg at a parameter value, the drafter should locate the world's saturation/stability crossover in closed form (here b\* = (r_max − r_base)/slope = 11) and place the gate legs to STRADDLE it with explicit margins — P085 failed exactly by anchoring "harmless low-load" ABOVE the crossover (ρ=0.70 > the ρ≈0.625 instability). This head does it deliberately (B_lo=6 sits below b\*=11, B_hi=33 well above), but the discipline is worth promoting from a per-head habit to a named drafting-battery gate ("straddle-the-bound") — distinct from this proposal's economics idea. (Logged for a later round, not pursued here.)

## ⟲ Previous-session review
P085 (round-18 fleet-backlogs opener, RR-vs-LQF domain-rotation starvation cliff) → VERDICT 098 REJECT (sim-lab PR #170, merge 5d8a45e), cleanly finalized. V098 fired REJECT at R1: the multi-domain starvation is REAL (R2 backlog divergence + R4 fleet-locality both held) but P085 mis-registered ρ=0.70 as a "harmless low-load" anchor when a fixed 1/N=0.25 round-robin share is already exceeded by the highest-λ fleet domain once ρ·0.40 > 0.25 (ρ>0.625) — so ρ=0.70 sat ABOVE the world's own stability crossover, sinking both R1-low and R3. That is the precise lesson this session embodies: P086 registers its gate legs (B_lo=6 below the b\*=11 saturation point, B_hi=33 above it) explicitly straddling the world's stability bound r_max, and R4 pins the crossover AT that bound rather than assuming a harmless margin. The +13 P→V offset held (P085→V098); this session inherits a green tree and refills the venture slot toward V099. No defects in the predecessor's landing discipline (born-red gate, heartbeat-last, SEEDLESS baton, append-only outbox all followed).
