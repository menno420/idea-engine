# Session — concept-pick-bringup-pack probe (gba-homebrew): battery v0 → park(build-direct)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-10 (worker slice, dispatched by the coordinator under
> continuous-chaining mode per Q-0265)

## What this session did

- Claimed `ideas/gba-homebrew/` (`claims/probe-gba-homebrew-bringup-pack.md`, flat filename
  per `claims/README.md`; cleared in this branch's final commit).
- **Timeliness check FIRST** (the PR #25 lesson, sharpened by PR #27): this capture is
  Sequence-tied to the lane's open concept-pick window and names its own decay ("worthless
  the session after"). Lane HEAD had MOVED since capture (`git ls-remote` = `16e64d7` vs
  pin `bc73da7`) — so the delta was audited before judging: the only in-between commits are
  lane PR #27's kit upgrade v1.7.0 → v1.7.1 (`979b161`/`962cdfe`/`64a81d8`, 21:49–21:53Z;
  `.substrate/` + `bootstrap.py` + `substrate.config.json` only, verified via a read-only
  blobless clone over the same git endpoint `ls-remote` already uses — the raw path cannot
  enumerate commits, and GitHub MCP is scoped to this repo). The four pick-relevant surfaces
  (`control/status.md`, `control/inbox.md`, `docs/concepts/session-1-concepts.md`,
  `docs/review-queue.md`) are byte-identical between `bc73da7` and `16e64d7` (raw-path
  fetch + `cmp`): no pick ORDER, concept doc still "awaiting owner pick," ⚑ ask still open.
  Residual blindness stated in the report: an unacted PR-comment pick would be invisible
  from here. Window judged OPEN on every readable surface.
- **Probed (battery v0):** `ideas/gba-homebrew/concept-pick-bringup-pack-2026-07-10.md` —
  pre-staged day-0 increment-1 plans per pick arm (Clockwork Courier / Shoal /
  keep-investing options) written while the pick is pending, so the owner signal converts
  to build the same session and the pick itself gets post-scaffolding costs instead of
  session-1 estimates.
- **Verdict: park(build-direct)** — worth building, nothing to simulate: a lane-local docs
  slice the lane's own standing default ("groom the backlog — never idle") already
  authorizes; plan quality has no simulator — its validation event is the post-pick build
  session itself. Smallest slice (Q8): three thin arm pages pinned at the scaffolding sha
  with an at-pick re-verify line + the ⚑ ask updated to point at the pack. State advanced
  forward-only captured → parked(build-direct — …); Grounding (@ `16e64d7`, manifest row:
  behind) + Sequence header lines added in the blessed byte-form; section README index
  updated.
- **No PROPOSAL appended:** not sim-ready — same discipline as PR #25/#27; the manager
  reads the verdict on the idea file and this heartbeat's fan-in note. Sim-lab queue
  position untouched (4 proposals; declared order 003 → 001 → 002, then 004; VERDICT 001
  done on 003).

**📊 Model:** fable-5 · high · docs-only (probe report + index line + card + heartbeat; no code)

## 💡 Session idea

The two gba-homebrew build-direct heads (replay-start-anchor, this pack) race the SAME
owner-gated window and are order-coupled (the pack should cite the anchored harness
contract). Pattern for the manager surface: when two park(build-direct) verdicts target
one lane and one window, the fan-in note should propose them as ONE sequenced routing
(anchor first, pack second — or one joint session) rather than two independent rows.
Encoded in this heartbeat's fan-in note; candidate one-sentence grooming rule for
README § outbox/fan-in if the pattern recurs.

## ⟲ Previous-session review

Consumed the PR #27 card + heartbeat handoff: it named this exact head as ripest
("concept-pick-bringup-pack is Sequence-tied to the same open pick window — probe it
before the pick lands or it decays like PR #25's head") — dispatched and executed before
the pick landed; the window held. Its timeliness-first discipline was extended one step:
PR #27 found HEAD unchanged and could reuse the capture pin, this session found HEAD
MOVED and had to diff the delta — the new trick (blobless `--filter=blob:none` clone for
commit enumeration where raw-path files can't answer "what changed") is worth reusing
alongside its ls-remote trick. Friction inherited and confirmed: `api.github.com`
proxy-walled; GitHub MCP scoped to `menno420/idea-engine` only (a `list_commits` attempt
on the lane repo returned "Access denied: repository not configured for this session" —
captured verbatim, so lane reads stay raw-path + git-endpoint). Manifest-staleness list
grows to eight datapoints (gba-homebrew row @ superbot `9624c53` still records
`b607365`/v1.6.0 while real HEAD is `16e64d7` with a v1.7.1 tree).

## Handoff → next wake

Inbox first (verified still empty at origin/main HEAD `1e93e5b` at claim time). Outbox
depth unchanged (4 proposals; this probe parked, nothing appended). gba-homebrew now
carries TWO build-direct heads racing one open pick window — the fan-in note asks the
manager for one sequenced routing; nothing further for this repo unless the window closes
(then both ideas need no action — they die with the window, states already honest).
Ripest next slices: second-lane harvest (one-line SECTIONS addition + `check_harvest`
sizing), bless-day debt sweep (2 advisory GROUNDING warns, 5-minute micro-slice),
freshest-wins one-liner (grooming round 3), `check_harvest --emit-entries` (PR #26
card 💡).
