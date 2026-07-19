# PROPOSAL 161 — Palm's theorem / M/G/∞ repair-pipeline insensitivity: spares depend on mean repair time, not its variance (P161 → V174, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card lands first with `Status: in-progress` to hold the PR red on the substrate gate; it flips to `complete` as the final commit, after the heartbeat, releasing the landing workflow. A red gate before that flip is the HOLD, not a defect.

## Objective
Author round-38's FLEET-slot PROPOSAL 161 (rotation fleet→venture→game→unrelated; round-38 opens at the FLEET slot with P161 → V174). Head: in an M/G/∞ repair pipeline — Poisson unit-failure arrivals at rate λ, each unit independently in repair for an i.i.d. time S — the stationary number of units in repair N is Poisson with mean λ·E[S], INSENSITIVE to the shape of the repair-time distribution beyond its mean (Palm's theorem, 1938; the basis of Sherbrooke's METRIC spares model). So the pipeline you must stock spares against is fixed by the offered load λ·E[S] alone: cutting repair-time VARIABILITY while holding the mean fixed buys zero reduction in required spares — only the MEAN repair time (or the failure rate) moves the pipeline. Three scale-free landmarks: E[N] = λ·E[S] (Little's law for the pipeline), the index of dispersion Var(N)/E[N] = 1 (Poisson) for every repair law, and the same pipeline for a deterministic, an exponential, and a heavy-tailed lognormal repair time of equal mean. Deliver a stdlib-only deterministic verifier (SEED pinned, three ≥3σ gates including a distribution-shift robustness gate) plus a proposal doc a VERDICT 174 session can check independently. Hand to VERDICT 174 at +13 offset.

## Constraints honored
- stdlib-only Python 3 verifier; SEED=20260717 pinned; in-process double-run determinism assert; results dict + sha256 printed (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY, floats 6 dp, compact canonical payload hashed).
- three ordered z-gates (z_gate=3.0): G1 pipeline-is-load (E[N] matches λ·E[S]), G2 variance-insensitivity (high-CV repair still gives dispersion 1), G3 distribution-free robustness across deterministic / exponential / lognormal repair laws of equal mean.
- +13 offset (P161 → V174). Outbox append-only + dedupe. Proposal high-water take-max, never regress. Born-red HOLD; merge-on-green landing.
- Grounding cites a reachable real-world source; the M/G/1 wait-tax contrast (variance DOES tax a waiting line) disclosed honestly as the folk-belief anchor, not the head. Family model names only; timestamps from `date -u`.

## GROUNDING (verified at HEAD)
- Offset + high-water lineage: `control/outbox.md` at HEAD (round-37 UNRELATED-slot P160 → V173 tail; proposal high-water pre-P161, +13 offset). Verify live before the outbox append.
- External phenomenon (reachable): the M/G/∞ queue / Palm's theorem — the stationary number in system is Poisson with mean λ·E[S], independent of the service-time distribution beyond its mean. https://en.wikipedia.org/wiki/M/M/infinity_queue — Wikipedia "M/M/∞ queue" (states "The stationary distribution of the M/G/∞ queue is the same as that of the M/M/∞ queue" — service-distribution insensitivity)

## Probe questions
**1.** Is the pipeline count really Poisson, or an artifact of the sampler? — M/G/∞ insensitivity is an exact result (Poisson displacement/marking theorem): each Poisson failure arrival is "present" over [arrival, arrival+S), so the count at any instant is a Poisson thinning with mean λ·E[S]; G1 gates E[N] against λ·E[S] and G2 gates the index of dispersion against the Poisson value 1.0 at ≥3σ.
**2.** Does repair-time VARIANCE really not matter? — G2 draws repair times from a heavy lognormal (CV=3) and confirms the dispersion index stays 1.0 within a 0.05 ceiling at ≥3σ, while the readout reports the M/G/1 wait tax (1+CV²)/2 = 5× the same CV would impose on a WAITING line — the pipeline shows none of it.
**3.** Is the insensitivity distribution-free or a one-law artifact? — G3 runs deterministic (CV=0), exponential (CV=1), and lognormal (CV=3) repair laws of identical mean and confirms the pipeline mean AND dispersion index agree across all three within 0.05 at ≥3σ.
**4.** Crossover, not the claim: for a WAITING line (finite servers, M/G/1, M/G/c) repair-time variance DOES inflate wait (Pollaczek-Khinchine); and if the mean repair time or failure rate moves, the pipeline moves. Are these disclosed as crossovers, not asserted as the head? — disclosed as crossovers; the verified head is the ample-server (M/G/∞) pipeline insensitivity to repair-time SHAPE at fixed mean.

## Outcome
_Pending — filled at the flip commit with the reproduced results-dict sha256, the three gate z-scores, and the headline; born-red HOLD holds the PR red until then._

## ⟲ Previous-session review
_Pending — filled at the flip commit._

## 💡 Session idea
_Pending — filled at the flip commit._
