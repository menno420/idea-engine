# Session 2026-07-20 — PROPOSAL 231 Shapley value of the airport cost-sharing game (game slot)

> **Status:** `complete`
>
> Born-red HOLD released: this card landed born-red (`in-progress`) on the FIRST commit and flips to `complete` here as the deliberate LAST commit — the idea doc + firsthand verifier + outbox PROPOSAL 231 block + claim all landed and `python3 bootstrap.py check --strict` reduces to the by-design in-progress HOLD only (now cleared) plus pre-existing advisory warnings. The flip re-runs the enabler via `synchronize` and arms native squash auto-merge gated on substrate-gate.

## 💡 Session idea
The Shapley VALUE of the airport cost-sharing (cooperative COST) game. An airport runway must be long enough for the most demanding plane; player i needs runway cost c_i, and a coalition S needs cost

    v(S) = max_{i in S} c_i.

The Shapley value splits the grand cost v(N) = max c_i among the planes: sort the costs ascending c_(1) <= ... <= c_(n), and share each runway segment c_(k) - c_(k-1) equally among the (n - k + 1) planes that still need at least that length, so the player at rank j pays

    phi_j = sum_{k=1}^{j} (c_(k) - c_(k-1)) / (n - k + 1),   c_(0) = 0.

Equivalently, phi_i is the average over uniformly random join-orders of player i's marginal cost contribution max(0, c_i - max_{j before i} c_j). The counterintuitive edge: the fair split is NOT equal shares of the total cost — for costs (1,2,4,8) the Shapley vector is (1/4, 7/12, 19/12, 67/12), which sums exactly to the grand cost 8, while the naive equal split would give 2 each. Verifier proves the closed form equals the exact n! average for n=4 and n=5 (Fraction), confirms the top player's value by Monte-Carlo (|z|<3), holds efficiency + symmetry exactly, and rejects the equal-split allocation at large |z|. Disclosed results-dict sha256 = `9cbd3c4ec0026187cd64a20bbb79167209f071adbd9a21ecade0787b55d0f4f2`.

## ⟲ Previous-session review
Round-54 rotation is fleet → venture → game → unrelated. Recent slots: FLEET P229 (derangement routing → 1/e, V242), UNRELATED P228 (random-walk no-return, V241). This takes the GAME slot as PROPOSAL 231 (P231 → VERDICT 244, +13 offset). Distinct from the already-built Shapley–Shubik power index card (P203 → V216, voting-power-not-weight — a simple VOTING game): the object there is a per-voter power number from pivotal swings; here it is a cost-allocation vector from a max-cost characteristic function. Different game, different object.

> 📊 Model: Claude Opus · high · idea/planning

## Decisions made
- Head: the cooperative Shapley VALUE of the airport COST game v(S)=max_{i∈S} c_i, with the Littlechild–Owen segment-equal-sharing closed form and the average-marginal-contribution-over-random-join-orders identity. Chosen as the round-54 GAME slot — a clean exact cost-allocation invariant, reproducible stdlib-only, explicitly distinct from the built Shapley–Shubik power index (different characteristic function and different object).
- 4 pre-registered gates, each in its own direction: G1 EXACT (Fraction) closed form == the exact average over ALL n! orderings for n∈{4,5}, every player; G2 Monte-Carlo agreement — sampled random-order mean marginal for the top player matches its exact Shapley value (|z|<3); G3 invariance (exact) — efficiency (values sum exactly to v(N)) and symmetry (two equal-cost players get exactly equal value); G4 falsifiability — the sampled top-player mean rejects the naive equal-split v(N)/n at large |z|.
- Verifier ships firsthand in idea-engine: `ideas/superbot-games/verify_shapley_airport.py` (stdlib only: json, hashlib, math, random, fractions; SEED=20260717; single seeded RNG in the MC pass; in-process double-run + separate re-invocation byte-identical; whole-dict sha256, no self-field).
- control/status.md is NOT touched (coordinator-owned heartbeat).

## Next session should know
PROPOSAL 231 → VERDICT 244 (+13 offset). Verifier: `ideas/superbot-games/verify_shapley_airport.py`, disclosed results-dict sha256 `9cbd3c4ec0026187cd64a20bbb79167209f071adbd9a21ecade0787b55d0f4f2`. Gate results: G1 PASS (closed form == n! enumeration for n=4 and n=5, e.g. main (1/4,7/12,19/12,67/12)); G2 z=−1.311312 (|z|<3, top player rank-max, mean 5.57834 vs target 67/12≈5.5833333); G3 PASS (efficiency sum 8/1 == grand cost 8, symmetric pair 3/2==3/2 on costs (2,5,5,9)); G4 z=939.716932 (>6, naive equal split 2/1 REJECTED). Grounding pins Wikipedia "Shapley value" oldid 1364397219 (raw-wikitext sha1 c557fc821d4fab14d90c3f7434e1120e6e9cf020) as primary and "Airport problem" oldid 1312709389 (raw-wikitext sha1 cc179b50972d2bf70492e5099ad242273874258a) as secondary; split HONEST — the average-marginal-contribution-over-orderings formula φ_i=(1/n!)Σ_R[v(P∪i)−v(P)] and efficiency Σφ=v(N) are QUOTED from the Shapley page, and the segment-equal-sharing rule plus the "landing charges are the Shapley value" identity are QUOTED from the Airport page; the specific Shapley vectors for (1,2,4,8)/(1,2,4,8,16)/(2,5,5,9), all z-values, the equal-split falsifier, and the digest are DERIVED firsthand. This card is LEFT RED (in-progress) until the deliberate final flip.
