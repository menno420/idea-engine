# Claim — claude/proposal-233-secretary-stopping

- `branch: claude/proposal-233-secretary-stopping`
- `scope: PROPOSAL 233 secretary optimal-stopping verifier + outbox block`
- `date: 2026-07-20`

**Detail** — PROPOSAL 233 (cross-cutting FLEET slot — optimal stopping / selection mechanism over a candidate fleet): for n candidates of distinct qualities arriving in uniformly random order, observed ONLY by relative rank, the threshold rule "reject the first r−1, then take the first candidate better than every one seen so far" selects the overall best with probability EXACTLY P(r,n)=((r−1)/n)·Σ_{i=r}^{n} 1/(i−1) (P(1,n)=1/n); the optimal cutoff r*(n) is the smallest r≥1 with Σ_{k=r}^{n−1} 1/k ≤ 1, and P(r*(n),n)→1/e≈0.36787944117144233 as n→∞, provably beating the naive take-first rule (win prob exactly 1/n). Files: `ideas/fleet/verify_233_secretary_stopping.py`, `ideas/fleet/run-stdout-233.txt`, `ideas/fleet/secretary-optimal-stopping-2026-07-20.md`, `control/outbox.md` PROPOSAL 233 block, this session card `.sessions/2026-07-20-proposal-233-secretary-stopping.md`; sim-lab `sims/verdict-246-secretary-optimal-stopping/`.

Notes: PROPOSAL 233 -> VERDICT 246 (+13 offset); cross-cutting FLEET slot (optimal stopping / best-choice selection mechanism). Paired sim-lab reproduction mirror `sims/verdict-246-secretary-optimal-stopping/` (branch `claude/proposal-233-secretary-mirror`); the canonical independent VERDICT 246 ruling is deferred to a dedicated coordinator-driven slice. No edits to `control/status.md` (coordinator-owned) or any other lane, and no `## VERDICT` block or verdict high-water advance. Claim bundled into the first (born-red) commit on this branch; released after landing.
