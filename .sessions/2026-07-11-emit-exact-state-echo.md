# Session — build: writer-side exact-state echo in check_harvest emit path

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 (worker slice, dispatched by the coordinator)

## Scope — the slice plan

The PR #163 card's 💡 executed: make `scripts/check_harvest.py`'s bullet-minting
path echo the linked local idea file's EXACT state line (full reason string,
never the bare family token) at write time, so the reader-side reason-presence
lint (the STATE-ECHO leg `check_ideas.py` grew in 12a6241) only ever fires on
true post-write drift — the writer-side origin of the 41-bullet bare-`historical`
echo rot that slice hand-fixed.

Verify-first overlap check (mandatory, done before writing code): the
reader-side leg (#163, `check_state_echoes()` + the `STATE_ECHO_RE` optional
`(\()` group in `scripts/check_ideas.py`) is CHECK-time only — it warns on
committed rot, it mints nothing. The ONLY minting path in `check_harvest.py` is
`emit_entry_stub()` (called solely from `check_section`'s `--emit-entries`
branch, for NEW upstream docs), which hardcoded bare `captured` in BOTH minted
state lines. `--re-badge` and `--states` are print-only suggesters;
`--write-pins` writes only `.harvest-pin.json` — no other writer of index rows
exists. Verdict: no overlap, no parallel check — fix the one writer.

Claim ritual honored: `control/claims/fix-emit-exact-state-echo.md` fast-laned
FIRST as PR #164 (merged 09a6704 — substrate-gate green in ~8s, control-only
short-circuit; REST squash after the enabler skipped), claims dir re-read at
HEAD post-merge — empty except README.md and this claim. Claim file deleted in
this PR's close-out.

## What this session did

- **`scripts/check_harvest.py` — `local_state_line()` + single-source `state`
  in `emit_entry_stub()`**: a new stdlib helper (the PR #163 card 💡) returns
  the exact full state string from an existing local idea file's
  `> **State:**` line via a new `FULL_STATE_RE` (whole rest of line — NOT
  `STATE_RE`, whose first-token capture is `--re-badge`'s family compare and
  deliberately unsuitable for exact echo); missing file or missing state line →
  `captured`, the mint default for a genuinely new capture. `emit_entry_stub()`
  computes `state` ONCE and uses it for both the stub's `> **State:** {state}`
  line and the index row's `— {state} ·` echo — the two minted lines can never
  disagree, and a re-emit against an existing file echoes its reasoned state
  verbatim.
- **Stub header prose** — one clause added: any state advance must be applied
  to BOTH the file state line and the index-row echo identically (exact echo,
  the PR #163 reason-presence leg).
- **Emit-time only, hermeticity held**: `--emit-entries` still prints to
  stdout and never writes files; no retro rewrite of existing index rows; no
  new modes, no flag changes, no preflight/CI membership (the Q4 rule); the
  default run's network legs unchanged — the helper reads one LOCAL file.
- **Extension note appended to
  `ideas/fleet/harvest-freshness-checker-2026-07-10.md`** (its third — same
  format as the first two; probe report and state untouched).

## Smoke tests (planted file — fired, plant removed)

Direct-seam smoke: planted `ideas/fleet/emit-echo-smoke-2026-07-11.md` with
state line `> **State:** parked(routed — smoke)`, imported the module via
importlib (standard `__main__` guard — import is side-effect-free), called
`emit_entry_stub('ideas/fleet', 'menno420/superbot', 'docs/ideas',
'emit-echo-smoke-2026-07-11.md', 'a'*40)`. Verbatim key output lines:

```
> **State:** parked(routed — smoke)
```

```
- [`emit-echo-smoke-2026-07-11.md`](emit-echo-smoke-2026-07-11.md) — parked(routed — smoke) · [[fill:one-line gist]] (canonical: superbot `docs/ideas/emit-echo-smoke-2026-07-11.md` @ `aaaaaaa`)
```

— BOTH minted lines carry the planted reasoned state verbatim. Default smoke
(same call, nonexistent `no-such-file-2026-07-11.md`):

```
> **State:** captured
```

```
- [`no-such-file-2026-07-11.md`](no-such-file-2026-07-11.md) — captured · [[fill:one-line gist]] (canonical: superbot `docs/ideas/no-such-file-2026-07-11.md` @ `aaaaaaa`)
```

— new-capture minting unchanged (regression held). Cross-check vs the reader
leg: the case-(a) index row reads `— parked(routed — smoke) ·` — `STATE_ECHO_RE`
matches the family token `parked` with its `(` IMMEDIATELY following, so the
optional `(\()` group captures and the reason-presence leg counts it as a
reasoned echo: a freshly minted row can never fire the #163 warning. Plant
deleted same session; `git status` shows only intended changes.

## Close-out

**Evidence (verified, this tree):** full `python3 scripts/preflight.py` — ALL
TEN checks PASS — and `python3 bootstrap.py check --strict` exit 0, run
immediately before push AFTER the heartbeat overwrite (verbatim tails below,
from the final passing run on the final tree):

```
preflight: OK — all 10 checks green
```

```
check: session log .sessions/2026-07-11-emit-exact-state-echo.md complete.
check: all checks passed.
```

(strict exit code 0, checked explicitly.)

Ceremony held: `bootstrap.py reflect --mine` ran at wake (R-0042 mined;
re-mined after the post-claim `reset --hard` discarded the working-tree copy —
same 10-line diff shape); inbox read FIRST at origin/main HEAD 12a6241 and
re-read post-claim at 09a6704 (ORDER 001's standing rule satisfied by this
card's 📊 Model line; ORDER 002 done by #158 — no new orders, nothing
re-claimed); claim landed on main BEFORE build (PR #164, merged 09a6704);
claims dir re-read at HEAD post-merge; claim file deleted in this close-out.

**Judgment:**

- Decisions made: fix the WRITER, not another checker (the overlap verdict —
  the reader leg already exists, a second lint would be duplicate machinery);
  new `FULL_STATE_RE` beside `STATE_RE` rather than repurposing it
  (`--re-badge`'s family compare NEEDS first-token semantics — `\S+` — and
  exact echo needs the whole line; one regex serving both would break one
  consumer); `captured` fallback on unparseable state line (a stub must always
  mint a valid grammar line; the harvester's full raw read catches the rest).
- Next session should know: guard recipe — the seam is `local_state_line()` +
  `FULL_STATE_RE` + the single `state =` assignment in `emit_entry_stub()`
  (`scripts/check_harvest.py`); test = the importlib direct-seam smoke on this
  card (plant a reasoned state, assert both minted lines echo it verbatim).

**📊 Model:** fable-5 · one emit-path writer fix (helper + single-source state
in check_harvest.py) + docs (idea-file extension note, card, heartbeat, claim
clear)

## 💡 Session idea

The current call seam makes the fix latent, not live: `check_section` only
calls `emit_entry_stub` for `new` names — docs with NO local file — so today
every live emit still mints `captured` (correctly). The class that would
exercise the echo path is UNMARKED entries (local file exists, no
machine-readable canonical marker — `check_harvest.py`'s honest-classification
split): a `--emit-entries` variant that also emits for UNMARKED names would
hand the harvester a ready-to-paste GRAMMAR UPGRADE stub whose state line and
index row already echo the existing file's reasoned state verbatim — the
exact re-plant scenario the #163 card feared, now safe by construction. Cheap:
the emit loop is two lines from `for name in new:` to `for name in new +
unmarked:` behind a flag; the state-echo machinery this slice built is the
hard part, already done.

## ⟲ Previous-session review

PR #163 (`.sessions/2026-07-11-index-echo-reason-drift.md`, squash `12a6241`,
the newest card at this wake) holds up on this tree: its 41 exact-echo
re-badges are live in `ideas/superbot/README.md` (zero bare `— historical ·`
rows remain; spot-checked line 35 `automod-spam-detection-gaps` carries
`historical(shipped in superbot same day, 2026-07-07)` verbatim), its claim
`build-index-echo-reason-drift.md` is gone at HEAD (claims dir = README.md +
this slice's claim only), its heartbeat overwrite happened (11:44:43Z stamp,
monotonic past #161's 11:27:30Z) and stamped the prior slice's number-less
`last-shipped` as #161 per the #72/#79 precedent, and this tree's
`check_ideas` run is back to exactly the 3 deliberate SIM-VERDICT legacy
advisories its card promised. Adopted from it directly: its 💡 IS this slice —
and its named co-edit anchor (`check_harvest.py` emit path) was where the fix
landed; its second anchor (the mirroring sentence at
`ideas/superbot/README.md:18`) needed no edit — the convention prose already
says exact-form `historical(...)`.

## Outcomes

Verdict: the harvest-freshness-checker idea extended in place — third
extension note; `ideas/fleet/harvest-freshness-checker-2026-07-10.md` state
stays `historical(#22)` (extension notes never advance state, the
probe-report-lint lineage). Landed per README § Landing conventions (PR READY;
`fix/*` may miss the enabler's branch patterns — REST merge-on-green fallback
per the #164 precedent this same session). Claim file deleted in this
close-out commit.

## Handoff → next wake

- The writer-side hole named by the #163 handoff is closed: minted stubs and
  index rows echo the linked file's exact state line from one source; the
  reader-side leg (preflight CHECKS entry 2) now only fires on true
  post-write advances.
- This card's 💡 (emit-for-UNMARKED behind a flag) is the natural next
  harvest-tooling slice — the echo machinery is built, the loop change is two
  lines.
- Standing ripest unchanged from the #163 heartbeat: websites re-harvest queue
  (moved HEAD + CHANGED backlog + one ACK-pending state-drift line, sized by
  the #149 card) and the manager sweep flags on the heartbeat notes line.
