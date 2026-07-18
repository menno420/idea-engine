# PROPOSAL 139 — raid team-size coordination overhead: the Ringelmann DPS cliff (round-32 GAME slot)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card holds the PR red from its first commit until the slice is complete and verified; flipping to `complete` at the end releases the landing workflow.

## Objective

Draft and land round-32 GAME-slot PROPOSAL 139 — raid team-size coordination overhead, the Ringelmann DPS cliff. In a co-op raid each added member contributes nominal single-target DPS but also imposes coordination overhead: per-member uptime decays as the roster grows (mechanic-dodges, movement, target-swaps) and burst-window collisions waste overlapping damage. Model total raid DPS(N) = (Σ_{i=1..N} base_i)·uptime(N)·(1−collision_loss(N)) with uptime(N)=max(FLOOR,1−c(N−1)) and 1−collision_loss(N)=(1−q)^(N−1). The nominal sum grows linearly in N, but the two overhead factors decay, so total raid DPS PEAKS at a roster size N* strictly SMALLER than the max allowed roster NMAX — against an enrage-timer boss (a raw-DPS race) a smaller premade at N* out-clears a full NMAX stack, and "stack more bodies" is negative-EV past N*. This inverts the folk belief "more raiders = more DPS; always bring a full roster." Ship a markdown-first card, a committed stdlib verifier (SEED=20260717, NMAX=8, three ordered ≥3σ /se gates G1→G2→G3, whole-dict sha256), a real dry-sim, an outbox block (P139 → V152, +13), and a heartbeat update. VERDICT 152 (P139 → V152, +13) is the next independent slice, not written here.

## Constraints honored

- Markdown-first card + committed stdlib verifier (hashlib/json/math/random only), SEED=20260717, three ordered gates on the Ringelmann-overhead model computed from the pinned constants.
- Deterministic: byte-identical double run, exit 0, disclosed results-dict sha256 (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture — no results_sha256 key, no on-disk JSON, stdout pretty dump distinct from the compact digest preimage; the P135 game-lane family posture).
- Born-red first commit → PR READY at once → flip complete last, after the heartbeat.
- Outbox PROPOSAL 139 block appended once per grammar (+13 offset → V152); did NOT write the verdict.
- Deduped against ideas/ + full outbox history — distinct from every prior game-lane head; the FIRST group-size / diminishing-per-capita-output (Ringelmann) card.
