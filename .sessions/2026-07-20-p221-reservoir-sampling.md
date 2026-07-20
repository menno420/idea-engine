# Session 2026-07-20 — PROPOSAL 221 reservoir sampling Algorithm R uniform k/n inclusion law (round-53 FLEET slot)

> **Status:** `in-progress`
>
> Born-red HOLD: this card lands born-red (`in-progress`) to hold the PR red on the first commit. It flips to `complete` as the last commit, after the verifier reproduces a byte-identical results-dict sha256 and all gates pass.

## 💡 Session idea
Reservoir sampling (Algorithm R, Waterman/Knuth/Vitter): a single streaming pass over n distinct items into a reservoir of size k — fill the first k, then for each arrival i>k pick j uniform in [1,i] and if j<=k replace slot j — leaves EVERY item in the reservoir with probability exactly k/n, independent of stream order. The inclusion probability, computed as a literal `fractions.Fraction` product looped over the stream (never hardcoded to the telescoped k/n), equals `Fraction(k,n)` for every item; Monte-Carlo (80000 trials) agrees within |z|<3; all C(6,3)=20 k-subsets are equiprobable (χ²=15.0832<43.8); and the unconditional-replace bug is rejected at z=400.0. Disclosed results-dict sha256 = `721cabd10d50672c6ddae8a893c0cc773c727fdb9f6d789e27aa8e7ad7dd0190`.

## ⟲ Previous-session review
Round-52 closed with P220 (Bertrand ballot theorem, UNRELATED slot → V233, +13). The rotation is fleet → venture → game → unrelated; this opens round-53 in the FLEET slot as P221 (P221 → V234, +13). DEDUP: grepped all lanes (`reservoir|sampling|stream|algorithm.r|waterman|vitter|uniform.inclusion`) across fleet, venture-lab, superbot-games, etc. Nearest neighbours — coupon-collector-tail (P052; time-to-cover-all, not per-item inclusion), consistent-hashing-max-gap (P217; max of uniform spacings, not stream sampling), two-choices-routing-cliff (P113; load balancing) — are all distinct. No reservoir-sampling / Algorithm-R / streaming-uniform card exists → distinct. High-water advance P220 → P221.

## 🫀 Heartbeat
Left to the coordinator per the single-writer rule (control/status.md is coordinator-owned; not touched here). Claim bundled into commit 1: control/claims/claude-p221-reservoir-sampling.md.

> 📊 Model: Claude Opus · high · idea/planning

## Decisions made
- Head: reservoir sampling Algorithm R uniform k/n inclusion law + subset-uniformity. Chosen because it is exactly true, reproducible stdlib-only, and un-built (no prior reservoir/streaming-sampling card in any lane).
- 4 pre-registered gates: G1 exact `Fraction` inclusion product == `Fraction(k,n)` for every item i across (40,8) and (25,5); G2 Monte-Carlo agreement |z|<3 (max |z|=0.760140 and 1.175565, 80000 trials); G3 robustness — shuffled arrival order max |z|=2.306936<3 and subset-uniformity χ²=15.0832<43.8 (df=19, all 20 subsets seen); G4 falsifiability — unconditional-replace bug rejected at max |z|=400.0 plus the first-k-naive model rejected.

## Next session should know
P221 → VERDICT 234 (+13 offset). sim-lab verifier already landed: `sims/verdict-234-reservoir-sampling/reservoir-sampling-uniform.py`, PR #313, merge SHA 872a84763f1aed1e0a56a6a9a47ddee148976c59. Grounding pins Wikipedia "Reservoir sampling" oldid 1365118921 (sha1 daf21f648c352d230e4640de6a7574aaf9ac83fc); caveat scoped — the revision describes Algorithm R and proves the uniform property by induction (step-wise k/i, k/(i+1)) but states it as step-wise probabilities rather than the literal "k/n" phrase, and also covers weighted (A-Res/A-ExpJ) and Algorithm L. Next slice: P222 opens round-53 VENTURE slot.
