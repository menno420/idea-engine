# Session 2026-07-20 — PROPOSAL 217 consistent-hashing max-gap (H_n/n imbalance) (round-52 FLEET slot)

> **Status:** in-progress

## 💡 Session idea
Uniform random hashing is lopsided: n independent uniform points on a unit circle cut it into n arcs, and the EXPECTED largest arc equals H_n/n — a factor H_n ≈ ln n above the fair share 1/n. That imbalance is exactly why consistent hashing needs virtual replicas. The exact combinatorial core is the alternating identity Σ_{k=1}^n (-1)^(k+1) C(n,k)/k = H_n, proven firsthand by exact Fraction equality, exhaustive discrete-ring enumeration, and seeded Monte-Carlo. Disclosed results-dict sha256 = 41394b56e4ebec3d14eb340fbfbd896db530d794fcea2ca495212948f74184ac.

## ⟲ Previous-session review
Prior slot in rotation was P216 (round-51 UNRELATED slot, Kaprekar's-constant universal funnel — unrelated domain to this networking/combinatorics head). Boot outbox proposal high-water P216; sim-lab at V229. Dedup grep across all lanes: no consistent-hashing / max-arc / max-gap / H_n-imbalance card exists (`grep -rilE 'consistent.hashing|max.gap' ideas/` returned nothing). Distinct from the five nearest neighbours (two-choices-routing-cliff, grid-quorum-sqrt-intersection, birthday-collision-sqrt-n, coupon-collector-tail, littles-law-distribution-free) — see the doc's Dedup section. High-water advanced P216 → P217 (union-max). P217 opens round-52 FLEET (fleet→venture→game→unrelated rotation).

## 🫀 Heartbeat
Left to the coordinator per the single-writer rule (control/status.md is coordinator-owned; not touched here). Claim bundled into commit 1 of this branch: control/claims/claude-p217-consistent-hashing-max-gap.md; the claim file names the P217 doc and verifier under lane ideas/fleet/.

> 📊 Model: Claude Opus · high · idea/planning

## Decisions made
- Head chosen: consistent-hashing max-gap = H_n/n (FLEET domain: distributed systems / combinatorial probability), because it is exactly true (exact Fraction identity + exhaustive enumeration), reproducible stdlib-only, and un-built. The counterintuitive claim: the busiest node owns H_n/n of the ring — a factor H_n ≈ ln n above its fair share 1/n.
- Five pre-registered gates: G1 exact alternating identity A(n)==H_n/n (Fraction ==); G2 exhaustive discrete-ring enumeration with monotone convergence to H_n/n; G3 ≥3σ Monte-Carlo for n=32,64; G4 invariance (exact ratio n·A/H_n==1 + shifted-circumference MC match); G5 falsifiability (naive 1/n and dropped-sign survival both REJECTED).

## Next session should know
P217 → VERDICT 230 (+13 offset). Next slice: P218 opens round-52 VENTURE slot. Grounding pins a Wikipedia revision of the "Consistent hashing" article; caveat scoped to what that revision states (motivates virtual nodes to reduce load variance/skew) vs the firsthand H_n/n identity the verifier proves.
