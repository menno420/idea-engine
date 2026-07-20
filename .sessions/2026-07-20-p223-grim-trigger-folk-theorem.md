# Session 2026-07-20 — PROPOSAL 223 Grim trigger / folk-theorem threshold δ*=(T−R)/(T−P) (round-53 GAME slot)

> **Status:** `complete`

## 💡 Session idea
Grim trigger / folk theorem: in an infinitely-repeated symmetric Prisoner's Dilemma with stage payoffs `T > R > P > S`, the grim-trigger strategy (cooperate until any defection, then defect forever) sustains mutual cooperation as a SUBGAME-PERFECT equilibrium iff the discount factor `δ ≥ δ*` with the EXACT closed form `δ* = (T − R)/(T − P)` — derived by the one-shot-deviation principle (`V_C = R/(1−δ)`, `V_D = T + δP/(1−δ)`, indifference at δ*). Canonical PD `(5,3,1,0) → δ* = 1/2`. Six SEED=20260717 gates (two exact-`Fraction` equality, two Monte-Carlo agreement at N_MC=200000, two beyond-6σ falsifiability) all PASS; disclosed results-dict sha256 = `7f00cea0bd40b2133ae9e91110c5112e8d5bf16bbcd90809a91911015215334f`. Round-53 GAME slot; pairs with VERDICT 236 (+13). The paired verifier is ALREADY MERGED in sim-lab (PR #316, merge SHA 41d3bb8).

## ⟲ Previous-session review
Round-53 rotation: VENTURE P222 (revenue equivalence, first=second price = (n−1)/(n+1)) → V235 landed (idea-engine #810, sim-lab #315); FLEET P221 (reservoir sampling) held by a sibling → V234; this opens the GAME slot as P223. DEDUP: grepped all lanes (`grim|trigger|folk|repeated|discount|subgame|cooperat|prisoner|tit.for.tat|axelrod|friedman`) across fleet, superbot-games, venture-lab. Prior game-theory cards: Penney, Efron dice, correlated equilibrium, Stackelberg, Vickrey, Nim/Sprague-Grundy, Blotto, all-pay, Nash bargaining, revenue equivalence. No grim-trigger / folk-theorem / repeated-PD threshold card exists in any lane → distinct. Proposal high-water advances P222 → P223.

## 🫀 Heartbeat
Left to the coordinator per the single-writer rule (control/status.md is coordinator-owned; not touched here). Claim bundled into commit 1: control/claims/2026-07-20-proposal-223-grim-trigger-folk-theorem.md. Born-red: this card opened `in-progress` to hold the substrate-gate RED through the idea-card + outbox-block commits, and is now flipped `complete` (the only RED across the build was the intended HOLD; `python3 bootstrap.py check --strict` exits 0 on this flipped tree).

> **📊 Model:** agent · high · idea/planning

## Decisions made
- Head: grim-trigger cooperation threshold `δ* = (T − R)/(T − P)` for the infinitely-repeated symmetric PD, stated as a SUBGAME-PERFECT (not merely Nash) condition since `(D,D)` is a credible stage-Nash punishment (`S < P`). Chosen because it is exactly true, reproducible stdlib-only, and un-built (no prior repeated-game / grim-trigger card in any lane).
- 6 pre-registered gates: G1 exact indifference `(5,3,1,0)` `δ*==1/2`, gap `V_C−V_D==0/1`; G2 exact grid `{1/2,1/4,3/4,1/8}` all gaps `0/1`, interior; G3 MC agreement at δ*=0.5 z=1.404082 (|z|<3); G4 MC grid max|z|=1.150506 (<3); G5 falsify wrong formula `δ_wrong=(T−R)/(T−S)=2/5` exact `E[D]=−2/3`, z=−140.372466 REJECT; G6 falsify below threshold at `δ*/2=1/4` exact `E[D]=−4/3<0`, z=−448.661725 REJECT.
- Grounding pinned to Wikipedia "Grim trigger" oldid 1292515670 (raw-wikitext sha1 beb2798d4ee3752cda422e6192a02e0ca3ea7926); caveat scoped: the revision states the grim-trigger strategy, the SPE condition `δ ≥ 1/2` for its normalized PD, `(D,D)` as the unique-Nash credible punishment, and the one-shot-deviation argument — but NOT the general `(T−R)/(T−P)` closed form, which is verifier-established firsthand.

## Next session should know
P223 → VERDICT 236 (+13 offset). Paired verifier already merged in sim-lab: `sims/verdict-236-grim-trigger-folk-theorem/grim-trigger-folk-theorem.py` (PR #316, merge SHA 41d3bb8). Next live slot in the round-53 rotation: UNRELATED (P224). Ledger contiguous through P223; proposal high-water P223.
