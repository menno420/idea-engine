# PROPOSAL 104 — epidemic overshoot (round-23 UNRELATED slot, P104 → V117, +13)

> **Status:** `complete`
> 📊 Model: opus-4.8 · high · idea/planning

Born in-progress as this session's first commit (born-red HOLD); flipped to complete as the deliberate last step after the heartbeat, releasing the landing workflow.

## Objective
Draft and land the round-23 UNRELATED-slot closer (P104): one genuinely new, counterintuitive, stdlib-simulable mechanism from OUTSIDE the fleet/venture/game domains and distinct from P100 (Kelly/growth-optimal betting), with pre-registered ≥3σ gates and a closed-form anchor, fanned to sim-lab as VERDICT 117 (+13). Executes ORDER 018 (owner's live overnight generate→verify loop directive).

## Constraints honored
- HARD-SYNC to origin HEAD (idea-engine 1423b26) before reading; control/inbox.md@HEAD confirms ORDER 018 (owner overnight directive, verbatim) is the governing order for this slice.
- Claim filed before work; born-red card is the first commit (HOLD); PR opened READY immediately; heartbeat before flip; Status→complete is the last commit.
- `python3 bootstrap.py check --strict` green (exit 0) before push.
- Stochastic Monte Carlo (Reed–Frost chain-binomial SIR) with a pinned SEED=20260717 and ≥3σ gates against a closed-form anchor (Kermack–McKendrick final-size equation); stdlib-only verifier (random, math, json, hashlib), no third-party. Model line family-level (ORDER 012 / PL-004 idea/planning class).

## What happened
- Idea: reaching the herd-immunity threshold h*=1−1/R0 does NOT stop an epidemic. The herd threshold is the point where transmission stops GROWING (R_eff=1 — the epidemic PEAK), but the infections already in flight at that moment keep transmitting, so the final attack rate z* is the nonzero root of the Kermack–McKendrick final-size equation z=1−e^{−R0·z}, which strictly EXCEEDS h* for every R0>1. The overshoot z*−h* is the fraction of the population infected UNNECESSARILY, past the point the disease was already receding. Epidemiology / SIR final-size theory — a fleet-external pure-mechanism head, deliberately a DIFFERENT unrelated domain from the round-22 closer P100 (Kelly / growth-optimal betting).
- Pinned world SEED=20260717, R0=2.5, N_POP=5000, I0=1, N_EPIDEMICS=4000, MAJOR_CUTOFF=0.10, SIGMA_GATE=3.0. Derived anchors: h*=1−1/R0=0.60, z*=0.892645 (final-size root), overshoot=0.292645. Stochastic Reed–Frost chain-binomial SIR Monte Carlo (exact geometric-gap Binomial sampler, no third-party RNG), conditioned on major outbreaks (n_major=3574, n_minor=426; major_frac=0.8935 = branching major-outbreak prob for R0=2.5, distinct from the naive 1−1/R0).
- Dry-sim (stdlib verifier, exit 0, two runs byte-identical): z_sim=0.892632 (se 0.000101), overshoot_sim=z_sim−h*=0.292632 (matches overshoot_star 0.292645 to 4 decimals), burn_post_threshold=0.194675 (se 0.000869). G1 overshoot z=2883.28σ (z_sim≫h*) PASS; G2 final-size anchor-match |z|=0.13σ (z_sim=0.892632 vs closed z*=0.892645 — reproduces Kermack–McKendrick to 4 decimals) PASS; G3 post-threshold burn z=224.07σ (burn>0) PASS; all_pass=true. Disclosed results-dict sha256 2ecda33ccab80be04904c973478093bb50a51cde8e5964da9d35e1ca4d340c3f.
- One-line design correction (pre-registered): size a cutoff / vaccination target / kill-switch by the SETTLING fixed point of the full dynamics (the final-size root z*), not the growth-stops threshold (herd immunity h*=1−1/R0), and budget for the overshoot — the fraction committed unnecessarily after the line is crossed.
- Files: ideas/fleet/epidemic-overshoot-2026-07-17.md (State: sim-ready) + committed reference verifier ideas/fleet/epidemic_overshoot.py; PROPOSAL 104 block appended to control/outbox.md (P104 ↔ V117, +13); claim control/claims/proposal-104-epidemic-overshoot.md filed; heartbeat control/status.md updated (proposal high-water → P104, baton → V116 for P103 then V117 for P104 then round-24 P105). PR #501. Reconciled a mid-slice `git merge origin/main` taking the UNION after the sibling VERDICT 115 mirror (#500, P102↔V115) landed — proposal high-water P104 + verdict high-water V115. `python3 bootstrap.py check --strict`: the only exit-1 finding was the born-red HOLD (in-progress card), cleared by this flip; the content legs (check_ideas + outbox↔ideas cross-check) pass.

## ⟲ Previous-session review
Immediate rotation predecessor P103 (round-23 GAME slot, streak-shield variance amplification) landed sim-ready (idea-engine #498, awaiting VERDICT 116); the round-22 UNRELATED closer was P100 (Kelly overbet ruin, information theory / growth-optimal betting) — this slice deliberately picks a DIFFERENT unrelated domain (epidemiology / SIR final-size theory) so the round-23 unrelated closer is not a re-skin of P100. Offset ledger (+13, P104 → V117) and baton confirmed intact in control/status.md before extending the rotation to the unrelated slot.

## 💡 Session idea
"Overshoot past a stopping threshold" is a reusable audit template for any self-limiting cascade with in-flight momentum: a system whose growth stops once a state variable crosses a threshold does NOT settle AT the threshold — the units already committed (infections in flight, orders in transit, retries mid-fanout, tasks already dispatched) keep acting after the crossing and carry the system past it. The transferable audit: never size a cutoff/quota/kill-switch by the threshold at which growth turns negative; size it by the SETTLING point (the fixed point of the full dynamics), which lies strictly beyond. Candidate future heads: retry-storm overshoot past a circuit-breaker trip (the in-flight retries already issued keep hammering after the breaker opens), autoscaler overshoot past a target-utilization threshold, and inventory-reorder overshoot past a stock-out trigger — each a "the in-flight fraction carries you past the stopping line" claim with its own closed-form settling anchor and cohort-contrast σ.

## GROUNDING
idea-engine@1423b26 (HEAD at sync, verified via `git ls-remote origin refs/heads/main` == local `git rev-parse HEAD`). The overshoot result is grounded in the Kermack–McKendrick (1927) final-size equation z=1−e^{−R0·z} and the herd-immunity threshold h*=1−1/R0 (standard textbook epidemiology; no external repo fetched), verified firsthand by the committed stdlib verifier ideas/fleet/epidemic_overshoot.py (stochastic Reed–Frost chain-binomial Monte Carlo under SEED=20260717). Mechanism grounded in the in-flight-transmission argument, not a fabricated external fetch.

📊 Model: opus-4.8 · high · idea/planning
