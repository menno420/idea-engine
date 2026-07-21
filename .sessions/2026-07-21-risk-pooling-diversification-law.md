# PROPOSAL 238 — insurance risk-pooling / diversification variance law: a mutual pool of n members each carrying an INDEPENDENT Bernoulli(p) unit loss has pooled per-member cost L̄=S/n (S~Binomial(n,p)) obeying E[L̄]=p (fair premium, scale-free in n) and Var[L̄]=p(1−p)/n — at p=1/10 a single member's cost sd 0.3 falls to exactly 0.03 across n=100 (√n=10× cut, mean unchanged) — refuting the naive comonotonic belief Var[L̄]=p(1−p) for all n (the ρ=1 no-diversification limit)

> **Status:** in-progress

📊 Model: Claude Opus · high · idea/planning
started: 2026-07-21T01:40:00Z

💓 Heartbeat:
- round/slot: venture · insurance / diversification — risk-pooling variance law (closed-form, ρ=0 baseline)
- lane: P238 → V251 (+13 offset)
- branch: claude/proposal-238-risk-pooling
- verifier: ideas/venture-lab/verify_238_risk_pooling.py (stdlib only: json, hashlib, math, random, fractions)
- SEED: 20260717 · results_sha256: 1e0520c849597c1b6a4135598ee76617488c49659c1820e1841b255b9115cbbb
- determinism: in-process double-run IDENTICAL · separate re-invocation byte-identical
- G1 EXACT — Var[L̄] computed two independent ways via fractions.Fraction (closed form Var(S)/n² vs full-binomial-pmf reconstruction E[(S/n)²]−E[S/n]²), both == 9/10000 with zero error (rational equality); pmf sums to exactly 1 · pass
- G2 MC agreement — 100000 independent pools of n=100 Bernoulli(1/10) members; empirical mean cost vs p and empirical Var[L̄] vs 9/10000, max |z|=1.4513 (<3, Z_ACCEPT=3.0) · pass
- G3 invariance — (i) Var[L̄]·n == p(1−p) exactly across n∈{1,10,100,1000} (the σ²/n law); (ii) coefficient of variation independent of claim severity, CV²=(1−p)/(pn) · pass
- G4 falsifiability — the naive comonotonic Var=9/100 (ρ=1 limit) rejected by the independent pool's empirical Var[L̄] at |z|≈21771.77 (≫8, Z_REJECT=8.0) · pass
- all_pass: true · first_failing_gate: null · decision: PASS

🔴 Born-red HOLD: this card commits FIRST with Status: in-progress to hold the PR red behind the substrate-gate while the idea doc, the verifier, the outbox PROPOSAL 238 block, and this card land in one commit. The HOLD releases only when this badge flips to complete as the deliberate LAST content commit — that clears the born-red hold and releases native squash auto-merge on green.

## What this proposal does
Adds a venture-lab PROPOSAL pinning the exact insurance risk-pooling / diversification variance law. A mutual pool of n members, each carrying an INDEPENDENT Bernoulli(p) unit loss, charges each member the pooled per-member cost L̄ = S/n with S ~ Binomial(n,p). The pool obeys E[L̄] = p (the fair premium is scale-free in n) and Var[L̄] = p(1−p)/n (per-member risk falls as 1/√n). Headline at p = 1/10, n = 100: the fair premium stays 0.1 while a single member's cost standard deviation 0.3 falls to exactly 0.03 — an exact √n = 10× reduction (Var = 9/10000). Ships a stdlib-only firsthand verifier with four gates each in its own direction, SEED = 20260717, deterministic (in-process double-run + separate re-invocation byte-identical), full results_sha256 disclosed. Fills a confirmed gap: the independent-pool p(1−p)/n insurance law and its 0.3 → 0.03 instance are grep-0 across both repos.

## Method
Exact computation over `fractions.Fraction`. G1 computes Var[L̄] two independent ways — the closed form Var(S)/n² and a full-binomial-pmf reconstruction E[(S/n)²]−E[S/n]² summed over k = 0…n — and asserts they are EQUAL rationals (both 9/10000), with the pmf summing to exactly 1. The "why" is two textbook facts composed exactly: Bienaymé (variance of a sum of independent terms is the sum of variances → Var(S) = n·p(1−p)) and scaling (Var(aX) = a²Var(X) with a = 1/n → Var(S/n) = Var(S)/n²). A Monte-Carlo agreement gate (G2) simulates 100000 independent pools of n = 100 Bernoulli(1/10) members and confirms mean cost vs p and Var[L̄] vs 9/10000 at max |z| = 1.4513 (< 3). An invariance gate (G3) checks Var[L̄]·n == p(1−p) across n ∈ {1,10,100,1000} and severity-independence of the coefficient of variation. A falsifiability gate (G4) rejects the naive comonotonic Var = 9/100 (the ρ = 1 no-diversification limit) at |z| ≈ 21771.77 on the same sample.

## ⟲ Previous-session review
The prior session landed PROPOSAL 237 (fleet slot: slotted-ALOHA finite-n throughput ceiling S_max(n)=(1−1/n)^(n−1)→1/e at optimal p*=1/n; idea-engine PR #846 / sim-lab VERDICT 250 mirror) with the born-red + four-gate + full-64-digest choreography. No open blockers were inherited. This slice reuses that contract exactly and extends the shipped set into the insurance / diversification lane, an atom distinct from the shipped heads. The proposal high-water was P237; this slice ADVANCES it to P238 (union-max, no regress). This is the ρ = 0 INDEPENDENT baseline of the diversification family — distinct from the shipped `correlated-fleet-variance-floor` head (the ρ > 0 generalization capping N_eff → 1/ρ; this is its ρ = 0 limit and its comonotonic ρ = 1 foil), from the Kelly/positive-EV growth heads, and from the revenue-equivalence and bilateral-double-auction market heads; grep-0 across both repos for the pooled p(1−p)/n insurance instance.

## 💡 Session idea
Next untaken diversification / risk-transfer atoms surfaced in dedup: (a) the interior ρ ∈ (0,1) equicorrelated pool — Var[L̄] = p(1−p)[ρ + (1−ρ)/n] flooring at ρ·p(1−p), the smooth bridge between this ρ = 0 baseline and the comonotonic ρ = 1 foil; (b) the heterogeneous-p pool where the fair per-member premium is the individual pᵢ but the pooled variance is (1/n²)Σpᵢ(1−pᵢ); (c) the reinsurance / excess-of-loss layer where pooling the body still leaves the tail. All grep-checked today.
