# Session — TOP-5 item 5 probe (leaderboard-row-avatars)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~18:55Z (worker slice, coordinator-dispatched
> under continuous-chaining mode per Q-0265)

## Scope

Probe TOP-5 item 5 (`ideas/superbot/leaderboard-row-avatars-2026-07-10.md`
— per-row avatar thumbnails on the `!leaderboard` image card, the games
completion wave's cheapest visible live-bot win, Q-0259 live-bot slot).
Section claim rode fast-lane FIRST as PR #202 `926c091`
(`control/claims/probe-leaderboard-row-avatars.md`; claims dir re-read at
wake HEAD `926c091` — only this claim live; file deleted in this PR). Branch
`probe/leaderboard-row-avatars`.

## What this session did

**Full battery probe (single-pass)** on the row-avatars visual. Verdict,
exact line on the file: `**Recommendation: park** — routed (superbot lane
build).` State flipped `captured` →
`parked(routed — superbot lane build; probe 2026-07-11)`, index re-badged
with the verified ledger. **NO outbox proposal** (verdict is park; outbox
tail stays PROPOSAL 009 and every shipped proposal remains verdicted).

The probe's verify-first, read at invocation sites not doc claims:
**NOT built at S HEAD** — `render_leaderboard_image`
(disbot/utils/ux_patterns/image_builders.py:90) takes
`rows/title/value_texts/theme` only, no avatar parameter; the row loop
(:133-180) draws rank/name/bar/value, no disc; no avatar LRU anywhere. The
shipped seams the canonical note names are real and live-proven
(`avatar_disc` card_render.py:425; `fetch_avatar_png` xp_helpers.py:35; the
single-user rank card already composites avatar-then-initials at
rank_render.py:97). TWO honest corrections to the canonical note: (1)
"every needed piece already exists" overclaims — `RankEntry`
(rank_providers.py:39-60) carries NO `user_id` (all 12 providers hold
`row["user_id"]` in scope but the structured projection drops it); (2) "the
layout already leaves room" is stale — `_LB_NAME_X = _LB_PAD + 46` needs a
name-column shift. superbot-next explicitly DEFERS image cards (D-0038
deviation 5 "no image cards … = presentation"; D-0061 classes card render
drift as successor-boundary), so routing to the rebuild would forfeit the
visible-now value; build-twice cost at cutover named on the file.

## Probe evidence (pins on the idea file)

- S = superbot `d647b2e` (`d647b2e9a75700439d6c194f7778972892f6bd45`) and
  N = superbot-next `ab1e916` (`ab1e9162596f897000a43d085f2b6aa3f78090ad`),
  both pinned as blobless-clone HEADs at probe time (clone via
  `git clone --filter=blob:none`, the ledgered route).
- Read at S: image_builders.py render body + constants, rank_providers.py
  projection + all 12 providers, leaderboard_cog.py invocation site, the
  three seams, `docs/decisions/` (8 ADRs) + `control/inbox.md` (zero
  leaderboard/avatar hits), fleet-review row (superbot = KEEP, the live
  product; `docs/planning/fleet-review-2026-07-11.md:69`). Canonical idea
  file byte-unchanged since its creation commit `8c9eb3d1` — the `fd638e3`
  harvest pin content IS the HEAD content.
- Read at N: `docs/decisions.md` D-0038/D-0061, `parity/parity.yml:88`
  (leaderboard: ported — the HEADLESS provider registry, not the image
  card), `control/inbox.md` (no order touches leaderboard visuals).
- Panel not escalated: product-composition head, reversible park, no
  security/data/spend/public surface (README battery panel rule).

## Verification

Full `python3 scripts/preflight.py` (all 10 checks) + `python3 bootstrap.py
check --strict` green on the final tree immediately before push, run AFTER
the heartbeat overwrite (heartbeat-last rule). `scripts/check_ideas.py`
standalone: OK, 301 files, the same 3 pre-existing advisory warnings. PR
number stamped post-open per the never-guess rule (the
#181/#184/#187/#190/#193/#195/#198/#201 follow-up recipe if the enabler's
arm-at-open merge exiles the stamp).

**📊 Model:** fable-5 · one idea-file probe append + state flip + one index
re-badge + card + heartbeat + claim clear; no code, no outbox append, no
lane-file writes (Q-0260)

## 💡 Session idea

**The TOP-5 is nearly spent — the next-next slice is a re-rank, and the
grooming input is already on file.** After this slice only items 3
(rebuild-critical-review-checkers) and 4 (rebuild-design-cite-checker)
remain OPEN, both superbot-next-checker-shaped heads. When they consume, the
re-rank slice should weigh: the 4 captured websites heads (ranked below
superbot per Q-0259 + fm ORDER 012/013 sequencing — re-check whether that
sequencing has since fired), the mint-time exclusions whose named triggers
may have fired (rebuild-navigation-completeness-check "price which half
remains"; rebuild-invocation-ladder-centralization behind Q-0228), and the
routing flags already relayed. Grooming seed, not a promise.

## ⟲ Previous-session review

Newest prior card: `.sessions/2026-07-11-release-testing-loop-probe.md`
(status `complete`; shipped #200 `0b630ea` + heartbeat stamp #201 `0a682a3`).
Spot-checked against the tree at wake HEAD `926c091`: (1) its probe-flip
claim holds — `ideas/superbot/rebuild-release-testing-loop-2026-07-10.md:3`
reads `parked(routed — superbot-next lane build; probe 2026-07-11)` with the
full 8-question battery + Grounding pin on the file; (2) its re-badge claim
holds — `ideas/superbot/README.md:187` carries the component ledger
(C BUILT / D BUILT-empty / A-B-D-flow absent) exactly as promised; (3) its
claim-hygiene claim holds — `control/claims/probe-rebuild-release-testing-loop.md`
is gone from the tree; (4) its NEW release-testing routing flag is live in
`control/status.md` notes and is carried forward by this slice's overwrite.
Its 💡 (promote the commits/main.atom SHA-pin recipe to CAPABILITIES) is
STILL-OPEN grooming — `docs/CAPABILITIES.md` carries no atom-feed entry at
this wake; flagged again rather than silently dropped. Adopted from it: the
re-verify-at-probe-time-HEAD discipline — this slice pinned S and N fresh
via blobless clones rather than carrying the `fd638e3` harvest pin on trust
(the canonical file proved byte-identical; the TREE around it did not — the
seams moved from "built this PR" claims to live-proven invocation sites).
No corrections found.

## Handoff → next wake

- Inbox first, as always. TOP-5 item 5 is CONSUMED (parked/routed this
  slice). **Ripest next: TOP-5 item 3**
  (`rebuild-critical-review-checkers-2026-07-10.md` — rubric classes
  11/12/13 live per D-0014/D-0033, review enforcement manual) **or item 4**
  (`rebuild-design-cite-checker-2026-07-10.md` — zero cite validation at N);
  they are the last OPEN TOP-5 heads, the slice after them re-ranks (💡
  above names the grooming input).
- Manager sweep flag added by this slice (heartbeat notes):
  leaderboard-row-avatars routing (ORDER-worthy — superbot lane build, one
  pure-additive PR: RankEntry `user_id` growth + optional `avatars` render
  param + bounded-gather fetch in the cog; the avatar LRU rides along;
  evidence pins S=`d647b2e` / N=`ab1e916`).
- PROPOSAL 009 verdict fan-in when sim-lab finalizes (outbox tail stays 009).
- Standing watches otherwise unchanged (golden-recapture + release-testing
  routing, map-before-faucets, RankProvider parity-guard, Rule 6,
  adoption-record sweep, contract-shape attach, effect-arming
  third-dependent; theme-schema half-fired; superbot-idle V006 guardrails).
- Friction for the ledger: local main had diverged at wake (a stray
  pre-force-push seed commit `df64aab` flagged will-show-Unverified by a
  repo hook) — preserved on `backup/local-seed-df64aab`, main realigned via
  `git reset --keep` after a classifier denial on `reset --hard`; otherwise
  clean — blobless clones, fast-lane claim, and the raw per-file reads all
  behaved.
