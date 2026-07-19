# PROPOSAL 173 — Decorrelated jitter backoff: adding random jitter to exponential retry backoff cuts total retry work and stops the thundering herd re-forming (P173 → V186, +13)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD (cleared).** This card landed first with `Status: in-progress` to hold the substrate gate red on this PR while the verifier, proposal doc, and outbox block were assembled; this flip to `complete` is the final commit and releases the landing workflow.

## Objective

Round-41 FLEET-slot opener. Author PROPOSAL 173 and its stdlib verifier for a fresh, counterintuitive, quantifiable fleet retry/backpressure mechanism: **decorrelated jitter backoff**. Pairs with sim-lab VERDICT 186 (+13).

Head: when N clients back off after a shared failure using PLAIN exponential backoff (no jitter), their retries stay synchronized — every client that collides in one round reschedules to the same future instant, so the surviving herd re-collides at full strength round after round and total retry work grows super-linearly in N. Adding FULL JITTER (sampling the wait uniformly in [1, window] instead of taking the whole window) decorrelates the retries, smears the herd across the backoff window, collapses per-slot contention toward server capacity, and cuts both total calls and the repeated peak contention. Adding randomness reduces total work.

## Constraints honored

- Stdlib-only verifier (`hashlib, heapq, json, random, statistics`); SEED = 20260717.
- Deterministic: every trial/arm draws from its own integer-seeded RNG, so output is byte-identical in-process and across invocations; run() double-run asserted identical; sha256 of the canonical results dict disclosed (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY).
- Grounding fetched live this session and confirmed to document the specific head (Full Jitter minimizes competing calls / total work vs no-jitter exponential backoff).

## GROUNDING (verified at HEAD)

Marc Brooker, "Exponential Backoff And Jitter," AWS Architecture Blog: https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/ — resolved live this session (HTTP 200, real content). It documents via simulation that Full Jitter minimizes competing calls and total work ("we've reduced our call count by more than half"; "The no-jitter exponential backoff approach is the clear loser. It not only takes more work, but also takes more time").

## Pre-registered gates (match the shipped verifier), z_gate = 3.0

A slotted contention/drain model: N clients each need one success from a shared server clearing at most K requests per slot; over-capacity slots clear K (chosen at random) and the rest reschedule after a capped-exponential backoff window w(f) = min(CAP, BASE·2^f). Strategy "none" retries after the whole window (synchronized); "full" retries after U{1..w} (decorrelated).

- **G1 — work reduction (tight Dirac herd, all N fail at t=0):** full-jitter mean total attempts is ≥3σ below the deterministic no-jitter total, and the reduction fraction 1 − mean_full/total_none ≥ 0.30.
- **G2 — thundering-herd flattening (same regime):** the repeated post-herd peak contention (max attempts in any slot after the unavoidable t=0 herd) is ≥3σ smaller under full jitter than the deterministic no-jitter value (N−K).
- **G3 — robustness under a shifted arrival distribution (≥3σ, paired):** replacing the synchronized herd with an over-dispersed geometric arrival smear, full jitter STILL reduces total work vs no-jitter on the same arrivals; the paired diff (none − full) is ≥3σ positive.

all_pass = G1 ∧ G2 ∧ G3.

## Probe questions

**1.** Does the grounding source document the specific head (jitter reduces total retry work), not just backoff generally? Yes — the AWS post's simulation compares Full/Equal/no jitter and reports Full Jitter cuts call count "by more than half"; confirmed live this session.

**2.** Is the win an artifact of the perfectly synchronized t=0 herd? G3 re-runs under an over-dispersed geometric arrival smear (a different generating distribution) and the work reduction persists at ≥3σ.

**3.** Is the no-jitter baseline a fair comparator, not a strawman? Both strategies use the identical capped-exponential backoff window; they differ ONLY in whether the wait is the whole window or a uniform draw within it.

**4.** Is the significance valid given the no-jitter arm is deterministic? In the Dirac regime the no-jitter drain is an exact constant, so it is a fixed baseline and the z is taken against the full-jitter replication SE; G3 uses a proper paired diff where both arms vary.

## Outcome

Shipped on PR #662. Verifier `ideas/fleet/decorrelated_jitter_backoff.py` runs deterministically (two invocations byte-identical), `all_pass=true`, Results-JSON sha256 `efea8579300ab0806132a48ea68cb8e9030105d8356b6fad51273fa8cb19e2f8`. Gates: G1 full-jitter mean total 784.51 vs deterministic no-jitter 2100 (reduction 0.626424, z=4350.282085); G2 full-jitter mean post-herd peak 116.635 vs no-jitter N−K=190 (z=244.458881); G3 shifted-arrival paired diff 15.8175, z=11.844264. Non-gated: equal jitter 754.49 (a wash with full), no-jitter drain time 958 slots. Verifier commit e6ffc66; proposal doc `ideas/fleet/decorrelated-jitter-backoff-2026-07-19.md`; grounding AWS "Exponential Backoff And Jitter" (HTTP 200, live); outbox PROPOSAL 173 block appended, proposal high-water P172 → P173; claim released.

## ⟲ Previous-session review

P172 (round-40 UNRELATED slot, Berkson's collider paradox) landed sim-ready; this seat opens round-41 in the FLEET slot per the fleet→venture→game→unrelated rotation, targeting VERDICT 186 (+13). No regressions observed in the outbox ledger at HEAD.

## 💡 Session idea

A companion FLEET head: **the retry-budget / token-bucket circuit** — jitter decorrelates WHEN clients retry, but a following proposal could quantify how a client-side retry token budget (retries capped as a fraction of successes) bounds the total amplification factor during a partial outage, closing the metastable-retry-storm loop from the demand side rather than the timing side.
