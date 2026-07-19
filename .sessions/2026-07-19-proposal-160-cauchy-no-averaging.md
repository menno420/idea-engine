# PROPOSAL 160 — Cauchy no-averaging: the law of large numbers fails for infinite-variance data (P160 -> V173, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card lands first with `Status: in-progress` to hold the PR red on the substrate gate; it flips to `complete` as the final commit, after the heartbeat, releasing the landing workflow. A red gate before that flip is the HOLD, not a defect.

## Objective
Author round-37's UNRELATED-slot PROPOSAL 160: a fresh, counterintuitive, quantifiable mechanism from probability / heavy-tailed statistics. Head: for i.i.d. draws from a standard Cauchy distribution the sample mean X̄_n is itself standard Cauchy for every n — averaging never concentrates, so the law of large numbers fails and X̄_n has the same spread as a single draw, no matter how large n grows. Three scale-free landmarks: the sample mean's interquartile spread is invariant in n (IQR(X̄_n)/IQR(X₁) → 1), the sample median by contrast concentrates as ~ π/(2√n), and the Cauchy quartiles sit at ±1 so IQR = 2 independent of any sample. Deliver a stdlib-only deterministic verifier (SEED pinned, three ≥3σ gates including a scale-free robustness gate under a shifted Cauchy scale) plus a proposal doc a VERDICT 173 session can check independently. Hand to VERDICT 173 at +13 offset.

## Constraints honored
- stdlib-only Python 3 verifier; SEED pinned; in-process double-run determinism assert; results dict + sha256 printed (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY, floats 6 dp).
- three ordered z-gates (z_gate=3.0): G1 mean-does-not-concentrate (IQR of X̄_n matches IQR of a single draw, ratio ≈ 1, invariant in n) + closed-form match, G2 median-does-concentrate (spread shrinks as ~π/(2√n)) + closed-form match, G3 scale-free robustness under a shifted (wider) Cauchy scale.
- +13 offset (P160 → V173). Outbox append-only + dedupe. Proposal high-water take-max, never regress. Born-red HOLD; merge-on-green landing.
- Grounding cites a reachable real-world source; the undefined-mean / infinite-variance caveat disclosed honestly. Family model names only; timestamps from `date -u`.

## Outcome
pending — content lands on this branch
