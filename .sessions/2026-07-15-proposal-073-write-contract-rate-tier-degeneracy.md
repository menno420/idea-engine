# Session — PROPOSAL 073: one knob printed twice — the mineverse write contract's two-tier rate limit (burst 10/10 s, sustained 60/min) has equal average rates, so the sustained tier is dead ink under every uniform limiter discipline while the burst tier alone over-admits 7/6 under fixed windows (fleet-backlogs slot, round 15 opener, superbot-mineverse)

> **Status:** `in-progress`
> **Model/time:** fable · 2026-07-15T09:49:49Z (Ideas Lab worker slice — draft the
> round-15 FLEET-BACKLOGS rotation slot opener under standing owner ORDER
> 003/004; round 14 closed fully served (fleet backlogs P069 #432, venture P070
> #434, game mechanics P071 #435, unrelated P072 #436, merged
> 2026-07-15T09:19:39Z by github-actions[bot]), so round 15 REOPENS at fleet
> backlogs per ORDER 004 rule 3. Slot spacing history confirmed: P061, P065,
> P069 → P073 (spacing 4).)

- **📊 Model:** fable-class · high · idea/planning

*(card born in-progress at 2026-07-15T09:49:49Z as the designed session-gate
hold; flips complete in this PR's final commit.)*

## Scope

Draft a genuinely new sim-shaped idea for the FLEET-BACKLOGS rotation slot,
round 15 opener, under standing owner ORDER 003 (continuous pipeline) and
ORDER 004 rule 3. Harvest source: **superbot-mineverse**, the slot's
LEAST-RECENTLY-TAPPED repo source — tap history disclosed per the
P053/P057/P061/P065/P069 repeat-tap precedent: slot rounds 1–14 drew P019
websites, P021 superbot, P025/P029 substrate-kit, P033 superbot, P037
fleet-manager, P041 curious-research, **P045 superbot-mineverse** (round 8 —
the repo's only prior fleet-slot tap, docs/mining-data-contract.md staleness
threshold), P049 curious-research, P053 websites, P057 trading-strategy, P061
superbot, P065 fleet-manager/own-bus rollover, P069 own bus ORDER text. Also
disclosed: P055 (game-mechanics slot, round 10) tapped mineverse's
achievements catalog (COIN_MAGNATE) — different slot, different artifact.
This head's files-of-fact (docs/mining-write-contract.md § Rate limits +
tests/shim/shim_bot.py) share ZERO fixtures with either prior tap.

Head: **the two-tier rate-limit degeneracy.** The WRITE contract commits two
tiers with IDENTICAL average rates — "**Burst**: 10 actions per 10 seconds. /
**Sustained**: 60 actions per minute." (docs/mining-write-contract.md:164-165
@ b9ade33; B·T = S·w = 600 exactly, both 1 action/s) — with the window
DISCIPLINE unstated, while the committed reference implementation (the shim,
"§ Rate limits as an opt-in deterministic mode — SHIM_RATE_LIMIT=10/10",
contract line 333) carries exactly ONE knob, a sliding window
(tests/shim/shim_bot.py:115, 340-366 @ b9ade33), and the real executor is
unbuilt (contract line 37 "to be built in the superbot repo"; superbot
docs/eap/night-review-2026-07-13.md @ f8e2313: blocked on the owner-side
MINING_WRITE_ENDPOINT/MINING_WRITE_SHARED_SECRET pair). Three exact structure
theorems, every registered numeral RAN live at drafting by the drafting
script (the V084 NO-DERIVED-LITERALS lesson; closed forms + independently
written DP/greedy/exhaustive twins, exact agreement): **T1 DEAD TIER** — at
the committed pair, under EVERY standard discipline applied uniformly
(sliding, aligned fixed windows, token bucket) the sustained tier never
rejects: sliding max in any 60 s span = 60 = S exactly, aligned-fixed max =
60 = S exactly (both margin-0 contacts, registered knife-edges), and the
sustained token bucket never drops below exactly 50 tokens. **T2 THE FORK**
— the burst tier ALONE under the two leakier disciplines breaches the
sustained expectation in the worst 60 s span: adversarially-aligned fixed
windows admit 70 (excess 7/6), a token bucket admits 69 (excess 23/20), and
a 2-second boundary straddle carries 20 = 2B under fixed — so the pair's
meaning forks on the unstated discipline. **T3 THE LATTICE POINT** — the
redundancy is exactly boundary-sited (sustained redundant under sliding iff
B·⌈T/w⌉ ≤ S; the committed pair sits at equality 60 = 60): at S = 50 a
separating schedule exists even under sliding (six 10-bursts = 60 > 50), at
w = 7 the redundancy dies by divisibility alone (B·⌈60/7⌉ = 90 > 60), at
S = 70 the pair is doubly slack with ANOTHER exact contact (fixed 70 = 70).

Deliverables this slice: this card (born-red first commit), the claim file,
`ideas/superbot-mineverse/write-contract-rate-tier-degeneracy-2026-07-15.md`
+ the `ideas/superbot-mineverse/README.md` index row, the `control/outbox.md`
PROPOSAL 073 append (append-only, real `date -u`, status sim-ready), and ONE
terminal claim prune (the P072 drafter — PR #436 verified merged at live
GitHub 2026-07-15T09:19:39Z, merged_by github-actions[bot], this session
before deletion). Seeds 20261650–653 — allocated from 20261650 per the
coordinator relay (20261640–643 are P072/V085's registered set; the gap
20261644–649 is the disclosed in-flight buffer). Arm R reporting-only seeded
20261650/651/652, aux 20261653 never read.

## Constraints honored

- control/inbox.md untouched (manager-written); control/status.md untouched
  (coordinator-only heartbeat). Newest inbox ORDER at HEAD is ORDER 015
  (2026-07-15T03:37:08Z, EAP extended to 2026-07-21) — no ORDER newer than
  015 (checked at sync, 2026-07-15T09:36:45Z); the continuous-pipeline duty
  (ORDER 003/004) is the standing authority for this slice.
- Outbox: PROPOSAL 073 appended via shell (append-only, real `date -u`); the
  live file is ~128.3 KB pre-append, under the 200KB rollover threshold — no
  roll this append. Both dated archives untouched (rolled, terminal).
- Claim prune is TERMINAL-only: PR #436 verified merged at live GitHub (mcp
  pull_request_read: merged 2026-07-15T09:19:39Z, merged_by
  github-actions[bot]) before deletion; zero open PRs at drafting
  (list_pull_requests state=open → []).
- Numbering verified at HEAD 412f132: newest PROPOSAL = 072 (live outbox +
  both dated archives swept); `PROPOSAL 073`/`proposal-073` collision-grepped
  clean (0 hits in control/, ideas/, docs/), zero open PRs.
- Grounding FIRSTHAND (Q-0272 git transport): superbot-mineverse shallow
  clone at live HEAD b9ade33ae6019eff45195684fa6fd6f02da4bee0 (fetched
  2026-07-15T09:38:40Z) — every harvested constant quoted verbatim with
  file:line in the idea file; superbot read via GitHub code search pinned at
  ref f8e2313 (executor-unbuilt evidence); pokemon-mod-lab untouched (the
  standing Q-0260 rule-3 carve-out). The verdict session is fully hermetic:
  every constant pinned in the idea file, zero repo/network reads at verdict
  time (the P017–P072 precedent). This repo edits no other repo (Q-0260).
- sim-lab dedup-swept READ-ONLY on a shallow clone @
  237b24a0316572ec521f3fa9811e28da6416e5eb (VERDICT 084 newest, fetched
  2026-07-15T09:42:37Z): no verdict prices a two-tier rate-limit pair, tier
  redundancy, or window-discipline divergence — the sliding-window hits are
  the V018/V046 game-admission lineage and the websites OAuth token-bucket
  control, all argued distinct in the idea file's Dedup section.
- Seed sweep boundary-aware at HEAD 412f132: genuine in-tree high-water
  20261643 (P072/V085's registered set 20261640–643); sim-lab genuine
  high-water 20261633 (V084's set) at 237b24a; the numerals
  20261664/20261833/202670087/2026964142 match the recorded data-not-seed
  discrimination rule (Fraction numerators and results-JSON digit runs).
  Allocation starts at 20261650, strictly above the registered set and the
  disclosed gap 20261644–649.
- Drafting-time verification discipline (the V080 live-verify rule + the
  V084 NO-DERIVED-LITERALS lesson): every numeral registered in the idea
  file was PRODUCED by the drafting script this session (scratchpad
  `draft_p073.py`) — the maxima table (60/70/69, straddle 20), the excess
  ratios 7/6 and 23/20 with band margins ×10/9 and ×23/21, the three dead-
  tier contacts (60=S, 60=S, bucket min level exactly 50), the identity
  B·T = S·w = 600, the separating-schedule triple (committed: none; S=50:
  witness 60; S=70: none), the w=7 divisibility world (90), the full
  4×4 (B,w)×S grid, the granularity-invariance triple (δ ∈ {1, 1/2, 1/5}
  all → 60/70/69), the bucket endpoint-convention pair {69, 70}, the pencil
  world (4/6/5 with exhaustive 4), five exhaustive small-world law checks,
  and the Arm-R previews (seed 20261650: 23270 admitted / 26730 rejected /
  worst-60 s-window exactly 60; seed 20261651: 9183/10817/60; obedient
  Retry-After client: exactly 3600 admits in 3600 s). Zero hand-derived or
  scaled numerals anywhere in the registered set.

*(💡 and ⟲ land with the complete-flip in this PR's final commit.)*
