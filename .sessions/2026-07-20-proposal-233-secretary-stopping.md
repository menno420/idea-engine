# Session — PROPOSAL 233 (secretary optimal-stopping → VERDICT 246)

> **Status:** in-progress
> Born-red HOLD: this card lands `in-progress` on the first commit to hold the PR red through the substrate-gate, and flips to `complete` as the deliberate last commit once the idea doc, verifier, outbox block, and claim are in place and the paired sim-lab reproduction is verified green. Merge is by native squash auto-merge on all-green.

## 💡 Session idea
Cross-cutting FLEET slot (optimal stopping / selection mechanism over a candidate fleet). PROPOSAL 233: for n candidates of distinct qualities arriving in uniformly random order, observed ONLY by relative rank, the threshold rule "reject the first r−1, then take the first candidate better than every one seen so far" selects the overall best with probability EXACTLY P(r,n)=((r−1)/n)·Σ_{i=r}^{n} 1/(i−1) (P(1,n)=1/n); the optimal cutoff r*(n) is the smallest r≥1 with Σ_{k=r}^{n−1} 1/k ≤ 1, and P(r*(n),n)→1/e≈0.36787944117144233 as n→∞ — provably beating the naive take-first rule (win prob exactly 1/n). Paired reproduction mirror in sim-lab under sims/verdict-246-secretary-optimal-stopping/ (offset +13); the canonical independent ruling is a separate coordinator-driven VERDICT 246 slice.

## ⟲ Previous-session review
P232 (FLEET, coprime density = 6/π² → VERDICT 245) landed. This slice stakes the coordinator-assigned P233 (secretary / best-choice optimal stopping, an untaken selection-mechanism atom; distinct from P198 Gittins bandits and P229 derangement). This slice does not touch control/status.md (coordinator-owned) and does not author a VERDICT block or advance the verdict high-water; proposal high-water advances P232 → P233.

## 🫀 Heartbeat
Verifier ideas/fleet/verify_233_secretary_stopping.py authored firsthand; born-red card holds the PR through the substrate-gate until the deliberate final flip. Verified green: exit 0, all four gates PASS, results_sha256 048261949a65653b7ad49d90c4968780cc5af2cb77705c9292d409743da68cac byte-identical across in-process double-run + separate re-invocation (SEED=20260717, stdlib-only, Python 3.11.15). G1 EXACT via Fraction — brute over ALL n! orderings == closed form for every r, all n∈{4,5,6,7}; argmax_r == r*(n) (r*={4:2,5:3,6:3,7:3}); P(1,n)=1/n; P(r*,n)=11/24,13/30,77/180,29/70. G2 MC n=100 r*=38 N=200000 z_optimal=−0.247895 (p̂=0.370775 vs p0≈0.371042778712643, near 1/e≈0.36787944117144233). G3(a) EXACT independent forward record-indicator DP == closed form all r,n; G3(b) rank-only invariance MC (quality=U³, independent seed) z_invariance=0.798199 (p̂=0.371905). G4 falsifiability — naive take-first consistent with its own 1/100 (z_naive_self=−0.40452) yet REJECTS the optimal target at z_naive_vs_optimal=−334.317693 (|z|≥6). A byte-identical copy is carried in the paired sim-lab reproduction PR (branch claude/proposal-233-secretary-mirror); the canonical independent ruling is a separate coordinator-driven VERDICT 246 slice.

> **📊 Model:** Claude Opus · high · idea/planning

## Decisions made
- Chose the exact finite-n closed form P(r,n)=((r−1)/n)Σ_{i=r}^{n}1/(i−1) with brute-force over ALL n! orderings as the empirical route — a self-certifying identity, not a restatement; every equality checked with fractions.Fraction (no float tolerance).
- G3's exact teeth is an independent forward record-indicator DP that multiplies the RAW factors (1−1/s) and never the telescoped closed form, so agreement certifies the telescoping rather than restating it; G3(b) adds a rank-only MC invariance draw (quality=U³) on an independent seed.
- G4 falsifier is the naive "take the first candidate" (r=1) rule: shown statistically consistent with its OWN exact 1/n as a sanity anchor, then shown to REJECT the optimal target P(r*,n) at |z|≈334 — opposite polarity to G2's agreement.
- Grounding pinned to the "Secretary problem" revision, which states the 1/e asymptotic win probability, the 37% figure, and the reject-first-n/e-then-pick-next-best rule literally; the exact finite-n closed form, the specific r*(n) integers, every Monte-Carlo z-value, the results_sha256, and the 1/n naive falsifier are honestly labelled derived firsthand.
- Did not author a VERDICT block or advance the verdict high-water, and did not touch control/status.md — the canonical VERDICT 246 ruling is a dedicated slice.

## Next session should know
- The paired sim-lab reproduction mirror lands the byte-identical verifier under sims/verdict-246-secretary-optimal-stopping/; the canonical independent VERDICT 246 ruling is still pending its dedicated coordinator-driven slice.
- No edits were made to control/status.md.
