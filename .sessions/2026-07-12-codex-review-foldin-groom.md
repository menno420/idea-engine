# Session — groom slice: fold codex reviews of #264/#265 into the maker venture docs

> **Status:** `complete`

- **📊 Model:** fable-5 · groom slice (fold 17 verified codex P2 review comments
  into the two existing venture-lab maker heads + review-fold-in addenda + this
  card; no new heads, no code, no probes)

**Section-collision flag (dispatch boundary — no claim file):** this slice is
barred from `control/`, so no `control/claims/` entry exists; this card's
born-red first commit carries the `ideas/venture-lab/` collision flag per the
PR #222/#225/#243/#244 workflow convention. Scope: targeted edits to
`ideas/venture-lab/maker-gift-repo-blueprint-2026-07-12.md` and
`ideas/venture-lab/maker-ecosystem-research-2026-07-12.md`, one review-fold-in
addendum appended to each, and this card. No state-line changes, no index
changes.

## What this session did

Post-merge review fold-in per the landing conventions ("Review is post-merge").
codex left P2 line-comment reviews on both maker-gift heads after they landed:
PR #264 (blueprint, review @ bb5a9d6, 5 comments) and PR #265 (research
dossier, review @ fb9039e, 12 comments — codex left twelve, not the announced
eleven). Two read-only verification passes checked every comment against the
tree, the auto-merge-enabler guard code, and external sources — ALL 17
ACCEPTED. This slice applied the accepted fixes in place, appended a
review-fold-in addendum to each file recording per-comment verdicts, and
reacted 👍 on all 17 review comments (accepted ⇒ no replies, no 👎).

Blueprint fold-in (5 + 5 cross-folds): auto-merge owner clicks (slice 1 step 0
+ owner ask); `LICENSE-substrate-kit` carried into the skeleton/§5 row (upstream
LICENSE confirmed at the 0801be9 pin); Day 0 connect-Claude step with
`@claude hello` verification and a chat fallback (+ slice-5 setup page);
project (c) criterion 1 rewritten — Python host sends limits over serial at
connect, firmware clamps to BOTH received limits AND a flashed conservative
safe superset (Uno-class boards have no filesystem); servo supply + fuse +
wiring + confirm-ask in the §7 shopping list. Cross-folds from the #265
review: stall headroom/fusing/e-stop in §2.3 + criterion 4, Pololu Maestro as
the buy-one-part alternative (§3c + §7), `.devcontainer/` skeleton line,
secrets convention in §2, GitHub Pages private-repo caveat in §7.

Dossier fold-in (12): stall-headroom PSU sizing (6 × ~2.5 A ≈ 15 A) + fusing +
e-stop; mesh-validity (ADMesh/trimesh) + PrusaSlicer smoke-slice CI entry;
binary/LFS storage boundary; Maestro alternative bullet; Wokwi **Custom Chips
fixture (I2C Device API)** — hedged, a ready-made PCA9685 chip model was NOT
confirmed; devcontainer/Codespaces entry; secrets convention; download
attribution manifest (`models/ATTRIBUTION.md`); Pages private-repo caveat;
SHA-pinning + minimal-permissions hardening; power-cut layer kept
**HUMAN-TRIGGERED** (blueprint doctrine is alerts-only, never auto-pause);
never-port-forward remote-access rule. Every folded claim carries the
verifier's citation URL.

## Close-out

**Evidence:**

- ideas touched (2): `ideas/venture-lab/maker-gift-repo-blueprint-2026-07-12.md`
  (targeted edits §1/§2/§3c/§6/§7 + `## Review fold-in (2026-07-12, codex
  review @ bb5a9d6)` addendum), `ideas/venture-lab/maker-ecosystem-research-2026-07-12.md`
  (targeted edits §2/§3/§4/§6/TOP 10 + `## Review fold-in (2026-07-12, codex
  review @ fb9039e)` addendum) — state lines untouched (`captured`,
  forward-only respected; fold-in is an append + in-place gap fix, not a
  state move)
- sessions touched (1): this card
- code touched: none · control touched: none (dispatch boundary) — the
  pre-existing unstaged `.substrate/` telemetry noise in the worktree was
  deliberately NOT staged (not this slice's change)
- GitHub: 👍 reaction on all 17 review comments (r3566889627–31 on #264;
  r3566891084/-085/-087/-090/-092/-095/-097/-099/-106/-110/-113/-114 on #265);
  no replies, no 👎 (all verdicts accepted)
- git: branch `groom/codex-review-foldin` off origin/main `fa38a95`, born-red
  card first commit `1fd8a3d`, fold-in commit `42463d4`, card flip last.
- verify: `python3 bootstrap.py check --strict` and
  `python3 scripts/preflight.py` run green before push (born-red hold on this
  card pre-flip is the designed exception).

**Judgment (the half only the session knows):**

- Decisions made, decide-and-flag: (1) the #264 verifier's shopping-list
  proposal said "≥5 A" while the #265 verifier's stall math says ~15 A
  worst-case — the fold-in uses the stall math everywhere (one number, the
  defensible one) rather than shipping two contradictory sizings; (2) the
  power-cut layer is worded human-triggered in the dossier's TOP 10 to stay
  consistent with the blueprint's alerts-only doctrine, exactly per the
  verifier's flagged nuance; (3) the Wokwi edit keeps the hedge ("Custom
  Chips fixture, I2C Device API") because a ready-made PCA9685 chip model was
  not confirmed — the dossier's couldn't-verify honesty norm applied to a fix.
- Next session should know: the fold-in addenda are the canonical record that
  these reviews are consumed — a future groom pass seeing the codex threads
  still unresolved on GitHub should resolve/ignore them, not re-fold.

## 💡 Session idea

Review fold-ins re-derive per-comment verdict lists that already existed in
the verification workers' reports; a tiny convention — verifiers emit their
per-comment table as a fenced block the fold-in slice pastes verbatim into the
addendum — would make the addendum a copy, not a retype, and eliminate
transcription drift on comment IDs.

## ⟲ Previous-session review

previous-session review: both parent capture cards held up.
`.sessions/2026-07-12-maker-gift-repo-blueprint.md` predicted exactly this
slice ("a groom pass after the dossier lands should reconcile") and its
handoff facts checked out: §7 owner ask present and paste-ready, external pins
(`0801be9`) real — the kit LICENSE resolved at that pin during verification.
`.sessions/2026-07-12-maker-ecosystem-research-capture.md` claimed every link
and couldn't-verify flag was preserved — the review verification confirmed the
doc's own honesty flags (e.g. the L180 no-turnkey-gcode-action flag) were
accurate; its one under-claim: the announced "eleven" codex comments were
twelve on fetch, all real. One nit: both cards said preflight "PASS all 10
checks" — still true at this slice's runs.

## Handoff → next wake

Facts for the coordinator heartbeat (NOT written here — control/ is
coordinator-only): codex reviews of #264 (5 comments) and #265 (12 comments)
are fully consumed — all 17 accepted, folded into both maker heads with
addenda, all comments reacted 👍, none replied. The blueprint's owner ask now
includes the two auto-merge setup clicks and the widened shopping list — if
the owner already replied to the OLD six-field ask, the delta (setup clicks,
supply/fuse parts or Maestro) needs a one-line follow-up ask. The codex
review threads on GitHub remain unresolved-by-thread (reactions only) — a
future sweep may resolve them; do not re-fold.
