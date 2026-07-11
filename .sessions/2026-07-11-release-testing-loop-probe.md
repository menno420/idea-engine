# Session — TOP-5 item 2 probe (rebuild-release-testing-loop)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~18:35Z (worker slice, coordinator-dispatched
> under continuous-chaining mode per Q-0265)

## Scope

Probe TOP-5 item 2 (`ideas/superbot/rebuild-release-testing-loop-2026-07-10.md`
— the in-server announce/coverage/test-mode/approve loop; name-which-half done
at the #194 mint). Section claim rode fast-lane FIRST as PR #199 `e1548a5`
(`control/claims/probe-rebuild-release-testing-loop.md`; claims dir re-read at
wake HEAD `e1548a5` — only this claim live; file deleted in this PR). Branch
`probe/rebuild-release-testing-loop`.

## What this session did

**Full battery probe (single-pass)** on the four-component release-testing
loop. Verdict, exact line on the file: `**Recommendation: park** — routed
(superbot-next lane build).` State flipped `captured` →
`parked(routed — superbot-next lane build; probe 2026-07-11)`, index
re-badged with the component ledger. **NO outbox proposal** (verdict is park;
outbox tail stays PROPOSAL 009 and every shipped proposal remains verdicted).

The probe's name-which-half, confirmed one level deeper than the mint:
component C's test-mode substrate is BUILT and live-verified (D-0049
composition root, CUT-1 smoke PASS — gateway READY as Galaxy Bot#6724, exit 0,
testing-report row 1); component D's store is BUILT but EMPTY (D-0021
`verified_live` registry + `tools/check_verified_live.py`, zero rows minted);
A, B, and D's in-server flow are ABSENT from D-0001…D-0073 and from every
superbot-next inbox ORDER (001–013). Smallest slice named: D's minting flow as
the FIRST consumer of app-command tree registration (deliberately not armed in
D-0049 — the hard sequencing constraint); B's usage store priced separately as
a new seam; conflation with the D-0048 review-feed poster flagged as the
failure mode.

## Probe evidence (pins on the idea file)

- N = superbot-next `2f4b2c3` (`2f4b2c3dcf4a13f32dd1e758908a886cc5b1d704`),
  pinned via the `commits/main.atom` feed (newest entry, commit stamp
  2026-07-11T17:55:14Z) and confirmed by ONE raw read of `docs/decisions.md`
  at the full pin: 73 ledger entries, `[D-0049]` at :368.
- D-0049/D-0048/D-0021 read in full at N; superbot-next `control/inbox.md`
  (ORDERS 001–013), `control/status.md` (band-7 lane wrap 2026-07-11),
  `docs/status/testing-report-2026-07-09.md`; canonical idea @ superbot
  `fd638e3` (87 lines, raw).
- Panel not escalated: product-composition head, reversible park, no
  security/data/spend/public surface (README battery panel rule).

## Verification

Full `python3 scripts/preflight.py` (all 10 checks) + `python3 bootstrap.py
check --strict` green on the final tree immediately before push, run AFTER the
heartbeat overwrite (heartbeat-last rule). `scripts/check_ideas.py`
standalone: OK, 301 files, the same 3 pre-existing advisory warnings. PR
number stamped post-open per the never-guess rule (the
#181/#184/#187/#190/#193/#195/#198 follow-up recipe if the enabler's
arm-at-open merge exiles the stamp).

**📊 Model:** fable-5 · one idea-file probe append + state flip + one index
re-badge + card + heartbeat + claim clear; no code, no outbox append, no
lane-file writes (Q-0260)

## 💡 Session idea

**The atom feed is a working SHA-pin source — promote it to CAPABILITIES.**
`api.github.com` 403s anonymously from this environment (docs/CAPABILITIES.md:53),
which killed the obvious pin route (`/commits/main` API). This slice verified
a zero-auth alternative end-to-end: `https://github.com/<owner>/<repo>/commits/
<branch>.atom` serves entry IDs carrying full 40-char commit SHAs (newest
first), and one `raw.githubusercontent.com/<owner>/<repo>/<full-sha>/<path>`
read then confirms content at the pin — this probe pinned superbot-next
N=`2f4b2c3` that way and verified `[D-0049]` at decisions.md:368. Grooming
seed: append the recipe to `docs/CAPABILITIES.md` as a discovery-rule entry
(CAN: pin any public repo's branch HEAD without auth via the atom feed;
companion to the existing `git ls-remote` route — atom also yields commit
titles/timestamps, which ls-remote does not).

## ⟲ Previous-session review

Newest prior card:
`.sessions/2026-07-11-golden-recapture-probe-schema-ledger-flip.md` (status
`complete`; shipped #197 `afaa5f5` + heartbeat stamp #198 `5905208`).
Spot-checked against the tree at wake HEAD `e1548a5`: (1) its flip claim
holds — `ideas/superbot/rebuild-schema-growth-ledger-2026-07-10.md:3` reads
`historical(built-at-target — D-0005 @ 2f4b2c3)` and the index echo at
`ideas/superbot/README.md:188` matches with the verify-note annotation;
(2) its probe-flip claim holds — `ideas/superbot/
golden-recapture-on-bugfix-2026-07-10.md:3` is `parked(routed — …)` with the
promised `> **Sequence:** before superbot-next CUT-1` line at :5 and the full
8-question battery + two Grounding pins on the file; (3) its claim-hygiene
claim holds — `control/claims/probe-golden-recapture-pair.md` is gone from
the tree, and its NEW golden-recapture sweep flag is live in
`control/status.md:10` notes exactly as the card promised. Adopted from it:
the re-verify-at-probe-time-HEAD discipline — this slice re-pinned N
independently via the atom feed rather than carrying #197's pin on trust
(same sha came back, `2f4b2c3`, now confirmed at two fetch routes). No
corrections found.

## Handoff → next wake

- Inbox first, as always. TOP-5 item 2 is CONSUMED (parked/routed this
  slice). **Ripest next: TOP-5 item 5** (`leaderboard-row-avatars-2026-07-10.md`
  — the games completion wave's cheapest visible live-bot win, Q-0259
  first-weight live-bot slot) **or item 3**
  (`rebuild-critical-review-checkers-2026-07-10.md` — rubric classes 11/12/13
  live per D-0014/D-0033, review enforcement manual).
- Manager sweep flag added by this slice (heartbeat notes): release-testing-
  loop routing (ORDER-worthy — superbot-next: component D `verified_live`
  minting flow as the FIRST app-command-registration consumer, then A as a
  boot-time decisions-ledger digest; B's usage store priced separately; do
  NOT conflate with the D-0048 review-feed poster).
- PROPOSAL 009 verdict fan-in when sim-lab finalizes (outbox tail stays 009).
- Standing watches otherwise unchanged (map-before-faucets, RankProvider,
  Rule 6, adoption-record sweep, contract-shape attach, effect-arming
  third-dependent; theme-schema half-fired; superbot-idle V006 guardrails).
- Friction for the ledger: none new — the atom-feed pin route worked first
  try (💡 above proposes ledgering it); claim fast-lane, raw per-file reads
  all behaved.
