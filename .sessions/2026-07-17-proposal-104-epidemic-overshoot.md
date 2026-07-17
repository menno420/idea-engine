# PROPOSAL 104 — epidemic overshoot (round-23 UNRELATED slot, P104 → V117, +13)

> **Status:** `in-progress`
> 📊 Model: opus-4.8 · high · idea/planning

Born in-progress as this session's first commit (born-red HOLD); flips to complete as the deliberate last step after the heartbeat, releasing the landing workflow.

## Objective
Draft and land the round-23 UNRELATED-slot closer (P104): one genuinely new, counterintuitive, stdlib-simulable mechanism from OUTSIDE the fleet/venture/game domains and distinct from P100 (Kelly/growth-optimal betting), with pre-registered ≥3σ gates and a closed-form anchor, fanned to sim-lab as VERDICT 117 (+13). Executes ORDER 018 (owner's live overnight generate→verify loop directive).

## Constraints honored
- HARD-SYNC to origin HEAD (idea-engine 1423b26) before reading; control/inbox.md@HEAD confirms ORDER 018 (owner overnight directive, verbatim) is the governing order for this slice.
- Claim filed before work; born-red card is the first commit (HOLD); PR opened READY immediately; heartbeat before flip; Status→complete is the last commit.
- `python3 bootstrap.py check --strict` green (exit 0) before push.
- Stochastic Monte Carlo (Reed–Frost chain-binomial SIR) with a pinned SEED=20260717 and ≥3σ gates against a closed-form anchor (Kermack–McKendrick final-size equation); stdlib-only verifier (random, math, json, hashlib), no third-party. Model line family-level (ORDER 012 / PL-004 idea/planning class).

## What happened
- (to be filled at close-out — dry-sim results, digest, PR number, check output)

## ⟲ Previous-session review
Immediate rotation predecessor P103 (round-23 GAME slot, streak-shield variance amplification) landed sim-ready (idea-engine #498, awaiting VERDICT 116); the round-22 UNRELATED closer was P100 (Kelly overbet ruin, information theory / growth-optimal betting) — this slice deliberately picks a DIFFERENT unrelated domain (epidemiology / SIR final-size theory) so the round-23 unrelated closer is not a re-skin of P100. Offset ledger (+13, P104 → V117) and baton confirmed intact in control/status.md before extending the rotation to the unrelated slot.

## 💡 Session idea
"Overshoot past a stopping threshold" is a reusable audit template for any self-limiting cascade with in-flight momentum: a system whose growth stops once a state variable crosses a threshold does NOT settle AT the threshold — the units already committed (infections in flight, orders in transit, retries mid-fanout, tasks already dispatched) keep acting after the crossing and carry the system past it. The transferable audit: never size a cutoff/quota/kill-switch by the threshold at which growth turns negative; size it by the SETTLING point (the fixed point of the full dynamics), which lies strictly beyond. Candidate future heads: retry-storm overshoot past a circuit-breaker trip (the in-flight retries already issued keep hammering after the breaker opens), autoscaler overshoot past a target-utilization threshold, and inventory-reorder overshoot past a stock-out trigger — each a "the in-flight fraction carries you past the stopping line" claim with its own closed-form settling anchor and cohort-contrast σ.

## GROUNDING
idea-engine@1423b26 (HEAD at sync, verified via `git ls-remote origin refs/heads/main` == local `git rev-parse HEAD`). The overshoot result is grounded in the Kermack–McKendrick (1927) final-size equation z=1−e^{−R0·z} and the herd-immunity threshold h*=1−1/R0 (standard textbook epidemiology; no external repo fetched), verified firsthand by the committed stdlib verifier ideas/fleet/epidemic_overshoot.py (stochastic Reed–Frost chain-binomial Monte Carlo under SEED=20260717). Mechanism grounded in the in-flight-transmission argument, not a fabricated external fetch.

📊 Model: opus-4.8 · high · idea/planning
