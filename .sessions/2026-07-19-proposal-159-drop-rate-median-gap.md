# PROPOSAL 159 — drop-rate median gap: the "expected N kills" loot anchor is the ~63rd percentile and the typical grind is ~69% of it (P159 → V172, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card lands first with `Status: in-progress` to hold the PR red on the substrate gate; it flips to `complete` as the final commit, after the heartbeat, releasing the landing workflow. A red gate before that flip is the HOLD, not a defect.

## Objective
Author round-37's GAME-slot PROPOSAL 159: a fresh, counterintuitive, quantifiable mechanism from game economies / loot design. Head: for an i.i.d. loot roll with per-attempt drop probability p, the attempts-until-first-drop T is Geometric(p) with mean 1/p but median only ~ln2/p (~0.693/p) and mode 1 — so the "expected N tries" players anchor on is the ~63rd percentile, not the typical grind. Three scale-free landmarks: median/mean → ln2 ≈ 0.6931, P(T ≤ mean) → 1 − 1/e ≈ 0.6321, tail P(T > 3/p) → e^−3 ≈ 0.0498, all independent of p. Deliver a stdlib-only deterministic verifier (SEED pinned, three ≥3σ gates including a scale-free robustness gate under a shifted drop rate) plus a proposal doc a VERDICT 172 session can check independently. Hand to VERDICT 172 at +13 offset.

## Constraints honored
- stdlib-only Python 3 verifier; SEED=20260717 pinned; in-process double-run determinism assert; results dict + sha256 printed (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY, floats 6 dp).
- three ordered z-gates (z_gate=3.0): G1 median-below-mean (right-skew) + closed-form ratio match, G2 mean-is-majority-percentile + closed-form P(T≤mean) match, G3 scale-free robustness under a shifted (rarer) drop rate.
- +13 offset (P159 → V172). Outbox append-only + dedupe. Proposal high-water take-max, never regress. Born-red HOLD; merge-on-green landing.
- Grounding cites a reachable real-world source; memorylessness "due" crossover disclosed honestly. Family model names only; timestamps from `date -u`.

## GROUNDING (verified at HEAD)
- Offset + high-water lineage: `control/outbox.md` at HEAD (round-37 VENTURE-slot P158 → V171 tail; proposal high-water pre-P159, +13 offset). Verify live before the outbox append.
- External phenomenon (reachable): geometric / exponential distribution — mean vs median skew and the CDF-at-the-mean value 1 − 1/e. https://en.wikipedia.org/wiki/Geometric_distribution — Wikipedia "Geometric distribution"; mean 1/p, median ⌈−1/log2(1−p)⌉; and https://en.wikipedia.org/wiki/Exponential_distribution CDF at the mean = 1 − 1/e ≈ 0.632.

## Probe questions
**1.** Is the median genuinely below the mean, or an MC artifact? — Geometric(p) has exact mean 1/p and exact median ⌈ln2/−ln(1−p)⌉; G1 measures (mean−median)/mean > 0 at ≥3σ and matches the closed-form ratio within a 0.05 relative-error ceiling.
**2.** Is the "expected count" really a majority outcome? — G2 measures the fraction of grinds finishing by the true mean 1/p, gates it > 0.5 at ≥3σ, and matches the exact 1 − (1−p)^⌊1/p⌋ within a 0.05 ceiling (→ 1 − 1/e ≈ 0.6321).
**3.** Is the skew scale-free or a one-rate artifact? — G3 re-measures both landmarks at a rarer shifted rate p′=0.005 and confirms median/mean ≈ 0.69 and mean-percentile ≈ 0.63 both hold at ≥3σ — the skew is a property of the geometric law, not of one tuned rate.
**4.** Crossover, not the claim: the memoryless "due after k misses is a fallacy" reading and the PRD/pity engineered cures. Are they disclosed as crossovers, not asserted as the head? — disclosed as crossovers; the verified head is the geometric mean/median/percentile skew (PRD and pity are the deliberate cures for exactly this skew — a dedup contrast, not this claim).

## Outcome
Pending the born-red flip — filled from the committed verifier's dry-sim at the final commit.

## ⟲ Previous-session review
Round-37 opened at the FLEET slot (P157 bullwhip → V170) and its VENTURE slot (P158 marketplace take-rate → V171); both landed on three ≥3σ gates with the whole-dict digest and a shifted-distribution robustness gate. That verifier discipline — exact closed-form gates, scale-free/robustness gate, honest crossover disclosure — carries forward here into the round-37 GAME slot P159 → V172 (+13).

## 💡 Session idea
Named, not authored: the "pity/PRD variance-compression dividend" — quantify how much a pity counter or a Warcraft-III-style PRD ramp shrinks the median/mean gap and the e^−3 unlucky tail relative to the plain geometric, trading a lower jackpot ceiling for a tighter, fairer grind distribution. A clean multi-mechanism verifier contrasting geometric vs PRD vs hard-pity tails.
