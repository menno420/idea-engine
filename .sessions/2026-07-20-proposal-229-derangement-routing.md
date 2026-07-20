# Session 2026-07-20 — PROPOSAL 229 Derangement routing: P(no agent to its home task) = D_N/N! → 1/e (round-54 FLEET slot)

> **Status:** `in-progress`
>
> Born-red HOLD: this card lands born-red (`in-progress`) on the FIRST commit to hold the PR red until the slice is genuinely done. It flips to `complete` as the deliberate LAST commit — after the idea doc + verifier + outbox block land and `python3 bootstrap.py check --strict` plus the outbox check go green. LEFT RED until the flip; the landing workflow arms native squash auto-merge once green + card flipped.

## 💡 Session idea
Derangement-routing invariant, framed for the fleet. Route N agents to N tasks by a uniformly-random permutation (a random bijection: each agent gets a distinct task). The probability that NO agent lands on its own "home" task is exactly the derangement ratio

    p_N = D_N / N! = sum_{k=0}^{N} (-1)^k / k!   ->   1/e = 0.3678794…   as N -> infinity,

where D_N is the subfactorial. The counterintuitive edge: this "nobody-home" probability does NOT decay to 0 as the fleet grows — it settles at ~36.8% forever — and it is NOT the naive independence guess q_N=(1−1/N)^N. Verifier proves the identity two exact ways (subfactorial recurrence vs alternating sum, Fraction, n=1..12), confirms it by Monte-Carlo at N=7 (|z|<3), holds the exact invariants (second recurrence D_n=n·D_{n−1}+(−1)^n, 0<p_n<1, alternating straddle of 1/e), and rejects the naive model at z≈82. Disclosed results-dict sha256 = `1f68c3d1cb6003f6ede1bc1d47e18f27a996bea9fa716f759d38fc2c3832365a`.

## ⟲ Previous-session review
Round-54 rotation is fleet → venture → game → unrelated. Prior slots: FLEET P225 (balls-into-bins collision count → V238 QUALIFIED), VENTURE P226 (Myerson reserve → V239 APPROVE), GAME P227 (Hex never-a-draw → V240 APPROVE), and P228 (random-walk no-return → V241 APPROVE, sim-lab). This takes the next FLEET slot as PROPOSAL 229 (P229 → VERDICT 242, +13 offset). Proposal high-water advances P228 → P229 (union-max, no regress).

## 🫀 Heartbeat
control/status.md refreshed as the deliberate LAST content commit (neutral facts + pointers): proposal high-water P229, offset P229→V242.

> 📊 Model: Claude Opus · high · idea/planning

## Decisions made
- Head: derangement-routing "nobody-home" probability p_N = D_N/N! = Σ(−1)^k/k! → 1/e, framed as fleet permutation routing. Chosen as the round-54 FLEET slot — a clean closed-form invariant, exactly true and reproducible stdlib-only, distinct from the existing hat-check card (P204/V217, which pins the fixed-point COUNT as Poisson(1) with mean/variance 1); this slice pins the k=0 atom p_N as a RATIO with a two-route exact identity and an explicit naive-independence falsifier.
- 4 pre-registered gates, each in its own direction: G1 EXACT identity two ways (subfactorial recurrence vs alternating sum, Fraction, n=1..12); G2 Monte-Carlo agreement N=7, T=2,000,000 (|z|<3); G3 exact invariants (second recurrence D_n=n·D_{n−1}+(−1)^n, 0<p_n<1, alternating straddle of 1/e); G4 falsifiability — naive independence q_N=(1−1/N)^N rejected on the SAME MC sample (|z_naive|>8).
- Verifier ships firsthand in idea-engine: `ideas/fleet/verify_229_derangement_routing.py` (stdlib only; SEED=20260717; single seeded RNG; in-process double-run + separate re-invocation byte-identical; whole-dict sha256, no self-field).

## Next session should know
PROPOSAL 229 → VERDICT 242 (+13 offset). Verifier: `ideas/fleet/verify_229_derangement_routing.py`, disclosed results-dict sha256 `1f68c3d1cb6003f6ede1bc1d47e18f27a996bea9fa716f759d38fc2c3832365a`. Gate results: G1 PASS (exact two-route identity), G2 z_exact=−1.151504 (|z|<3, phat=0.3674645 over 734929/2,000,000), G3 PASS (exact invariants + straddle), G4 z_naive=82.246356 (>8, naive (6/7)^7=0.339917 REJECTED). Grounding pins Wikipedia "Derangement" oldid 1364530247 (raw-wikitext sha1 ba6f5759199b761a56d50342132212bbc99ed505); split HONEST — the core identity D_n=n!·Σ(−1)^k/k!, both recurrences, and the 1/e derangement-probability limit are QUOTED literally from the pinned revision; the fleet-routing framing, the specific p_7=1854/5040 ratio, the MC z-values, and the naive-independence falsifier q_N=(1−1/N)^N are DERIVED firsthand. This card is LEFT RED (in-progress) until the deliberate final flip; the landing workflow arms native squash auto-merge once green + card flipped.
