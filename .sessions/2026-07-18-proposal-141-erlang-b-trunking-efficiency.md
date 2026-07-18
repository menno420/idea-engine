# PROPOSAL 141 — Erlang-B trunking efficiency: fragmenting a loss-system fabric into small independent pools at the same offered-load-per-server MULTIPLIES blocking (round-33 FLEET slot OPENER)

> **Status:** in-progress
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card holds the PR red from its first commit until the slice is complete and verified; it will flip to `complete` in the deliberate LAST commit to release the landing workflow. No gate is bypassed; a red gate AFTER the flip is a real defect, not the HOLD.

## Objective

Draft and land round-33 FLEET-slot PROPOSAL 141 — Erlang-B trunking efficiency. Each pool is an M/M/c/c loss system (Poisson arrivals rate λ, exponential service rate μ, c servers, NO queue, blocked-calls-cleared); offered load a=λ/μ Erlangs; by PASTA the blocking probability is the exact Erlang-B loss formula B(c,a)=(a^c/c!)/Σ_{k=0}^{c}(a^k/k!), computed by the stable recursion B(0,a)=1, B(k,a)=a·B(k−1,a)/(k+a·B(k−1,a)). The counterintuitive headline: at a FIXED offered-load-per-server ρ=a/c, B(c,cρ) FALLS steeply as c grows (trunking efficiency) — same utilization, dramatically less blocking as the pool grows — so fragmenting one pooled 100-server fabric into 50 independent 2-server pools at the same ρ=0.8 lifts the drop rate from ~0.4% to ~33%. Ship a markdown-first card, a committed stdlib verifier (SEED=20260717, three ordered ≥3σ /se gates CFG_SMALL → CFG_MED → CFG_HEAD, whole-dict sha256), a real dry-sim, an outbox block (P141 → V154, +13), and a heartbeat update. VERDICT 154 (P141 → V154, +13) is the next independent slice, NOT written here.

## Constraints honored

- Markdown-first card + committed stdlib verifier (hashlib/json/random only), SEED=20260717, a single `random.Random(SEED)` drawn sequentially in the fixed config order, three ordered gates on the exact Erlang-B loss law computed from the pinned constants.
- Deterministic: byte-identical double run (in-process + cross-invocation), exit 0, disclosed results-dict sha256 (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture — no results_sha256 key, no on-disk JSON, stdout pretty indent=2 dump distinct from the compact hashed preimage; the P136+ fleet-lane family posture).
- Born-red first commit → PR READY at once → flip complete last, after the heartbeat.
- Outbox PROPOSAL 141 block appended once per grammar (+13 offset → V154); did NOT write the verdict.
- Deduped against ideas/ + the full outbox history — distinct from every prior queueing head (service-variance-wait-tax P137 M/G/1 WAIT, checkout-pooling Erlang-C DELAY, variance-blind-provisioning, two-choices-routing-cliff placement); this is a multi-server LOSS system (Erlang-B blocking).

## What happened

(filled at flip)

## ⟲ Previous-session review

(filled at flip)

## 💡 Session idea

(filled at flip)

## GROUNDING

(filled at flip)
