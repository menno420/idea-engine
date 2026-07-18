# PROPOSAL 139 — raid team-size coordination overhead: the Ringelmann DPS cliff (round-32 GAME slot)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD released: this card held the PR red from its first commit until the slice was complete and verified; flipping to `complete` here releases the landing workflow.

## Objective

Draft and land round-32 GAME-slot PROPOSAL 139 — raid team-size coordination overhead, the Ringelmann DPS cliff. In a co-op raid each added member contributes nominal single-target DPS but also imposes coordination overhead: per-member uptime decays as the roster grows (mechanic-dodges, movement, target-swaps) and burst-window collisions waste overlapping damage. Model total raid DPS(N) = (Σ_{i=1..N} base_i)·uptime(N)·(1−collision_loss(N)) with uptime(N)=max(FLOOR,1−c(N−1)) and 1−collision_loss(N)=(1−q)^(N−1). The nominal sum grows linearly in N, but the two overhead factors decay, so total raid DPS PEAKS at a roster size N* strictly SMALLER than the max allowed roster NMAX — against an enrage-timer boss (a raw-DPS race) a smaller premade at N* out-clears a full NMAX stack, and "stack more bodies" is negative-EV past N*. This inverts the folk belief "more raiders = more DPS; always bring a full roster." Ship a markdown-first card, a committed stdlib verifier (SEED=20260717, NMAX=8, three ordered ≥3σ /se gates G1→G2→G3, whole-dict sha256), a real dry-sim, an outbox block (P139 → V152, +13), and a heartbeat update. VERDICT 152 (P139 → V152, +13) is the next independent slice, not written here.

## Constraints honored

- Markdown-first card + committed stdlib verifier (hashlib/json/math/random only), SEED=20260717, three ordered gates on the Ringelmann-overhead model computed from the pinned constants.
- Deterministic: byte-identical double run, exit 0, disclosed results-dict sha256 (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture — no results_sha256 key, no on-disk JSON, stdout pretty dump distinct from the compact digest preimage; the P135 game-lane family posture).
- Born-red first commit → PR READY at once → flip complete last, after the heartbeat.
- Outbox PROPOSAL 139 block appended once per grammar (+13 offset → V152); did NOT write the verdict.
- Deduped against ideas/ + full outbox history — distinct from every prior game-lane head; the FIRST group-size / diminishing-per-capita-output (Ringelmann) card.

## What happened

Synced to origin/main HEAD 23c1ad5 (VERDICT 150 mirror — the round-32 FLEET-slot P137 → V150 landed via PR #579; sibling round-32 VENTURE-slot P138 → V151 landed via PR #578 @c02df30; round-31 CLOSED on both sides, proposals P133–P136 / verdicts V146–V149). origin/main stayed at 23c1ad5 through the whole slice — no sibling merge needed (re-fetched before the heartbeat and before the flip). Re-scanned control/claims/ and open PRs for a competing P139 — none (the only other open PR is #527, VERDICT 126). Claimed P139, branched `claude/proposal-139-raid-coordination-overhead`, opened PR #580 READY on the born-red card (commit 40facae). Committed the stdlib verifier + idea card + outbox P139 block + heartbeat (commit 4900351): the real dry run passed all three ordered ≥3σ /se gates (G1 cliff DPS(N*=6)−DPS(NMAX=8) mean=+13.1796 z=+62.61; G2 interior-peak N*=6 interior_fraction=0.85980 one-proportion z=+101.77 vs p0=0.5; G3 no-overhead placebo interior_fraction=0.0 exactly, full-roster-beats mean=+199.4478 z=+399.62), byte-identical across two runs, exit 0, results-dict sha256 16225c9a8e53cc23cfaa6a5df4b9631e5224d36a80ebada7f1a86546606c9fa3 (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture, the P135 game-lane family; stdout pretty indent=2, compact canonical hashed preimage). Pinned world: NMAX=8, base_i~Gamma(K=4, θ=25) (mean 100, CoV 0.5), c=0.06, FLOOR=0.35, q=0.07; mean-model peak N*=6 with DPS(6)=292.189115 > DPS(8)=279.189204. Authored the game-lane card (dedup draws the line vs guild-volunteer-dilemma: public-goods PROVISION / free-riding vs a per-member OUTPUT-decay curve with an interior maximum), appended the outbox PROPOSAL 139 block (+13 → V152, offset cited from the predecessor P138 → V151 depends-ledger row + the status baton), updated the heartbeat (proposal high-water P138 → P139, baton → V152 for P139 then round-32 unrelated-slot P140; routines line unchanged coordinator-bound; inbox untouched), then flipped this card to release the landing workflow. `python3 bootstrap.py check --strict` before the flip failed only on the designed born-red HOLD (claims-duplicate / claims-format / owner-action / seat-digest advisories are never exit-affecting; the check_ideas ↔ outbox gate passes — the P139 idea doc, verifier, and outbox block are consistent).

## ⟲ Previous-session review

The round-32 FLEET-slot P137 → V150 (service-variance wait tax) and the VENTURE-slot P138 → V151 (usage-based billing variance shock) both landed on green — origin/main is HEAD 23c1ad5, and the +13 offset held unbroken (P133→V146, P134→V147, P135→V148, P136→V149 landed on both sides; P137→V150 mirrored, P138→V151 pending sim-side). This slice takes the round-32 GAME slot (rotation venture→game) and inherits the whole-dict / no-self-field / stdout-only digest posture verbatim from the P135 game-lane exemplar. Continuity carried forward: the verdict high-water V150 is non-contiguous — V137 for P124, V132 for P119, and V126 for P113 (idea-engine mirror #527) remain open below it, so V150 must not be read as "all lower verdicts closed on both sides".

## 💡 Session idea

Three game-lane heads now share an "adding units past a sweet spot destroys value" shape by different mechanisms: this P139 raid coordination overhead (an interior DPS-maximizing roster size — Ringelmann per-capita decay), P099 shop-reroll-ruin (optimal stopping — one reroll too many burns the buffer), and the compounding-reward-inequality Gini drift (variance concentrates gains past a point). Candidate follow-up: a single "diminishing-returns / interior-optimum" design playbook that unifies (a) linear-gain × decaying-overhead output curves (roster size, party size, zerg size), (b) optimal-stopping thresholds, and (c) concentration/variance floors — so a systems designer reads one thread from "why more is not better" to "which lever (cut overhead, raise the stop, flatten concentration) moves the optimum," tying the group-size Ringelmann curve to the broader interior-optimum family.

## GROUNDING

- Verifier (firsthand, ground truth): https://github.com/menno420/idea-engine/blob/main/ideas/superbot-games/raid_coordination_overhead.py — results-dict sha256 16225c9a8e53cc23cfaa6a5df4b9631e5224d36a80ebada7f1a86546606c9fa3, SEED=20260717, NMAX=8, K_SHAPE=4, THETA=25, C_UPTIME=0.06, FLOOR=0.35, Q_COLLISION=0.07, TRIALS=20000.
- Idea card: https://github.com/menno420/idea-engine/blob/main/ideas/superbot-games/raid-coordination-overhead-2026-07-18.md
- External reference (reachable): Ringelmann effect — individual productivity falls as group size grows through coordination + motivation loss; https://en.wikipedia.org/wiki/Ringelmann_effect — verified reachable 2026-07-18 (Ingham, Levinger, Graves & Peckham 1974).
- Grounding commit: https://github.com/menno420/idea-engine@23c1ad5 · HEAD at start 23c1ad5ec17bb04de17a0aaced4129b62eb269b2 · fetched 2026-07-18T15:50:54Z. PR: #580.
