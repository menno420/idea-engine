# Session — TOP-5 item 1 probe (golden-recapture-on-bugfix) + schema-growth-ledger verify-and-flip

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~18:10Z (worker slice, coordinator-dispatched
> under continuous-chaining mode per Q-0265)

## Scope

The #194 handoff's two named heads, shipped as one same-section PR (branch
`probe/golden-recapture-pair`; section claim `control/claims/
probe-golden-recapture-pair.md` fast-laned FIRST as PR #196 `e57eb9f`, claims dir
re-read at HEAD — only this claim live; file deleted in this PR):

1. **Verify-and-flip (micro, NO battery)** —
   `ideas/superbot/rebuild-schema-growth-ledger-2026-07-10.md`: PR #194's mint
   priced it built at target (D-0005). VERIFIED at superbot-next pinned live HEAD
   `2f4b2c3dcf4a13f32dd1e758908a886cc5b1d704` (`git ls-remote`, 17:57Z) by reading
   the artifact AND its invocation sites, per-file raw, not just greps:
   `docs/decisions.md:42` (D-0005); `docs/planning/schema-growth-ledger.yml` read
   whole (1143 lines — `baseline:` = the 8 §2.1 seed fields; `entries:` rows each
   with ≥2 `consumers` + `rejected_alternative` + `minted`, actively growing:
   `PanelActionSpec.reply_visibility` :378, `CommandSpec.reply_visibility` :854);
   `tools/check_schema_growth.py` read whole (diffs
   `sb.spec.roles.snapshot_field_roles()` against the ledger, reds on unminted
   field / <2 consumers / stale rows); invocation READ at
   `.github/workflows/named-gates.yml:62-63` ("Schema-growth ledger (A-2)" step in
   the manifest-validate named gate) and `.github/workflows/ci.yml:54` (the
   19-checker fleet loop). State flipped `captured` →
   `historical(built-at-target — D-0005 @ 2f4b2c3)` + verify note appended +
   index re-badge.

2. **Full battery probe (single-pass)** —
   `ideas/superbot/golden-recapture-on-bugfix-2026-07-10.md` (third TOP-5 #1).
   Verdict, exact line on the file: `**Recommendation: park** — routed:` the
   recapture protocol is superbot-next lane protocol/CI work; no sim-shaped
   evidence question survives (drift enumeration is a git-log fact; a protocol
   contract is proven by its own red/green — the #114 precedent). State →
   `parked(routed — …)`, `> **Sequence:** before superbot-next CUT-1` stamped
   (the canonical doc's own window), index re-badged with the live trigger.
   **NO outbox proposal** (verdict is park; outbox tail stays PROPOSAL 009).

## Probe evidence (pins on the idea file)

- N = superbot-next `2f4b2c3` (ls-remote 17:57Z): D-0019 (corpus imported
  byte-identical from superbot @ `7f7628e1`, 465 goldens, reviewed-change
  integrity rule), D-0028 (replay adapter — flips possible, zero flipped
  honestly), D-0050/D-0062 (band rows still pending — window open), D-0071
  (gate 220/220 across **37 ported**; corpus 467 = 465 imported + 2 minted).
- `parity/parity.yml` at N: `source.sha = 7f7628e1…`, `minted_goldens: 2`.
- `parity/README.md:24-32` at N: the integrity rule already LEGALIZES
  "current bot's behavior changed deliberately in PR #N" — permission without
  detection; greps for `recapture|re-capture` over decisions.md and parity.yml:
  ZERO hits (the README's one hit is the harness-normalization clause).
- S = superbot live HEAD `2c7d2de` (ls-remote ~18:05Z) — the drift clock: the
  corpus pin is behind the live bot, so the flip window's drift is real.
- Panel not escalated: process head, reversible park, no
  security/data/spend/public surface (README battery panel rule).

## Verification

Full `python3 scripts/preflight.py` (all 10 checks) + `python3 bootstrap.py
check --strict` green on the final tree immediately before push, run AFTER the
heartbeat overwrite (heartbeat-last rule). `scripts/check_ideas.py` standalone:
OK, 301 files, the same 3 pre-existing advisory legacy warnings. PR number
stamped post-open per the never-guess rule (the #181/#184/#187/#190/#193/#195
follow-up recipe if the enabler's arm-at-open merge exiles the stamp).

**📊 Model:** fable-5 · two same-section idea-file writes (one flip + verify
note, one probe append + park) + two index re-badges + card + heartbeat + claim
clear; no code, no outbox append, no lane-file writes (Q-0260)

## 💡 Session idea

**A verify-and-flip should cite the twin it rode with.** This pair worked
because the micro-flip (schema-growth ledger, D-0005) turned out to be the
EXACT pattern the full probe's Q3 needed (ledger + checker diffing reality
against ledger) — same-PR pairing let the probe cite a just-verified live
artifact instead of a stale summary. Grooming seed: when the coordinator
bundles a verify-and-flip with a probe in the same section, check whether the
flipped artifact is a PATTERN INPUT to the probe's Q2/Q3 before writing them
independently — the pairing is evidence, not just batching.

## ⟲ Previous-session review

Newest prior card: `.sessions/2026-07-11-groom-top5-round3-lightning-round5.md`
(status `complete`; shipped #194 `617e125` + heartbeat stamp #195 `5e36a0d`).
Spot-checked against the tree at `5e36a0d`: the third TOP-5 is on the heartbeat
as promised (5 entries + mint-time exclusions); the V010 fan-in note exists on
`ideas/superbot/settle-once-architecture-guard-2026-07-10.md` (grammar-blessed,
numbering cross = PROPOSAL 009, state stays `sim-ready`); all 8 round-5 💡
encodings are live in the two root READMEs (the probe battery's new
cross-lane/tree-aware verify-first paragraph was APPLIED by this slice's own
work — the mint-time ledger check it encoded is what priced the flip half).
Its handoff named this exact pair (probe item 1 + the schema-growth-ledger
micro-flip) as ripest — dispatch matched. Adopted from it: the re-verify-at-
probe-time-HEAD discipline (its mint pinned N=`870a16c`; this slice re-pinned
N=`2f4b2c3` and re-confirmed both facts rather than carrying the stale pin).
One nuance surfaced, not a correction: its "zero recapture protocol at N"
grep-clean claim VERIFIED, with one precision added — parity/README's
integrity rule does mention re-capture for harness-normalization changes;
the missing thing is bugfix-drift detection, which the probe names exactly.

## Handoff → next wake

- Inbox first, as always. TOP-5 item 1 is CONSUMED (parked/routed this slice);
  the schema-growth-ledger micro-flip is done. **Ripest next: probe TOP-5
  item 2** (`rebuild-release-testing-loop-2026-07-10.md` — name-which-half
  already done at mint: test-mode root BUILT D-0049, the in-server
  announce/coverage/approve loop is the open half).
- Manager sweep flags added by this slice (heartbeat notes): the
  golden-recapture lane routing (superbot-next recapture-disposition
  ledger + warn-first checker; superbot-side checklist one-liner) — ORDER-worthy,
  evidence on the idea file's probe report.
- Standing watches otherwise unchanged (map-before-faucets, RankProvider,
  Rule 6, adoption-record sweep, contract-shape attach, effect-arming
  third-dependent; theme-schema half-fired; superbot-idle V006 guardrails).
- Friction for the ledger: none new — claim fast-lane, raw per-file reads, and
  the MCP PR path all behaved; the arm-at-open stamp exile remains the known
  quirk (follow-up recipe used if fired).
