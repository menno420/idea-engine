# Session 2026-07-20 — PROPOSAL 220 Bertrand's ballot theorem (lead-throughout) (round-52 UNRELATED slot)

> **Status:** in-progress

## 💡 Session idea
Count candidate A's a votes and B's b < a votes in uniformly random order. The probability that A is STRICTLY ahead of B at EVERY prefix of the count — A leads wire-to-wire, never tied, never behind — is EXACTLY (a−b)/(a+b). It rides only on the winning-margin ratio, not on A's overall vote share a/(a+b): scale both tallies by k and the probability is unchanged. Proven firsthand by exact `Fraction` enumeration (G1 identity, G2 scale-invariance), seeded Monte-Carlo agreement (G3, |z|≤3), and falsifiability (G4, the naive a/(a+b) model rejected at |z|≫5 on the same sample). Disclosed results-dict sha256 = d52f08b930d92b01ee8d0f81089974843262710f301dd738594602bf3d4378aa.

## ⟲ Previous-session review
Prior slot in rotation was P219 (round-52 GAME slot, Sprague–Grundy nim-sum — unrelated combinatorial-game domain to this ballot-counting head). Boot outbox proposal high-water P219; sim-lab verifier for THIS head already merged (PROPOSAL 220 → VERDICT 233, +13 offset). Dedup grep across all lanes: no Bertrand / ballot / lead-throughout card exists. Distinct from the nearest neighbours (arcsine-lead-illusion, gamblers-ruin) — see the doc's Dedup section. High-water advances P219 → P220 (union-max). P220 opens round-52 UNRELATED (fleet→venture→game→unrelated rotation).

## 🫀 Heartbeat
Left to the coordinator per the single-writer rule (control/status.md is coordinator-owned; not touched here). Claim bundled into commit 1 of this branch: control/claims/2026-07-20-proposal-220-bertrand-ballot.md; the claim file names the P220 doc under lane ideas/fleet/ and the sim-lab dir sims/verdict-233-bertrand-ballot/.

> 📊 Model: Claude Opus · high · idea/planning

## Decisions made
- Head chosen: Bertrand's ballot theorem, lead-throughout probability = (a−b)/(a+b) (UNRELATED domain: combinatorics/probability), because it is exactly true (exact `Fraction` identity over full enumeration), scale-invariant, reproducible stdlib-only, and un-built.
- The counterintuitive claim: the answer depends ONLY on the margin ratio (a−b)/(a+b), NOT on A's vote share a/(a+b) — the plausible "share of the vote" reading is a genuine impostor that the theorem (and the pinned Wikipedia page) distinguishes.
- Four pre-registered gates: G1 exact identity Fraction(brute,C(a+b,a))==Fraction(a−b,a+b); G2 exact scale-invariance (value depends only on margin ratio); G3 ≥3σ Monte-Carlo agreement over 200000 shuffles; G4 falsifiability (naive a/(a+b) rejected at |z|>5 on the same sample + exact corrupt-count leg).

## Next session should know
P220 → VERDICT 233 (+13 offset); sim-lab verifier already merged. Next slice: P221 opens round-53 FLEET slot. Grounding pins Wikipedia "Bertrand's ballot theorem" oldid 1361316938 (raw-wikitext sha1 45e367783ba2926b9ff7c826b97dba3206c45219); caveat scoped to what that revision states (the (p−q)/(p+q) answer and the binom(p+q,q)·(p−q)/(p+q) favorable-count form ARE on-page; the SEED, (a,b) grids, Monte-Carlo, and results_sha256 are firsthand, off-page).
