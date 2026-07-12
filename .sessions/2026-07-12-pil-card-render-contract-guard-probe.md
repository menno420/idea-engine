# Session — single-pass probe: superbot pil-card-render-contract-guard

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-12 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session did

Single-pass probe (battery v0, no panel triggers) of
`ideas/superbot/pil-card-render-contract-guard-2026-07-10.md` — TOP-5 #2 on the
fourth ledger (`control/status.md` @ `42f9642`): one cross-cutting test that
forces the PIL import to fail and asserts every card renderer in the family
returns `None` instead of raising, replacing per-module bespoke scaffolding.

Verify-first, live: superbot HEAD resolved by `git ls-remote` =
`1ecc21138fe0a1eb672d03b66bd319164c29d55f`; tree scanned via the standing
read-only blobless-clone recipe, files read via raw at the pinned SHA. The
decisive facts: (a) NO cross-cutting guard exists at S — no
`test_card_render_contract.py` in ls-tree; `test_card_render_structure.py` is
a layout golden that `skipif`-skips entirely without Pillow, the wrong axis;
(b) the ledger's timing claim HOLDS and is STRONGER than claimed — the render
family is byte-unchanged `d647b2e`→`1ecc211` (diff over `disbot/utils` +
`disbot/services` + `disbot/cogs/leaderboard_cog.py` + `tests/` touches only
`tests/unit/scripts/test_check_consistency.py` across 21 commits),
`render_leaderboard_image` (image_builders.py:90-96) still has NO avatars
param, and superbot `control/inbox.md` @ S carries ORDER 001 only — the
avatars ORDER is unlanded AND unrouted, window open; (c) the canonical premise
("the gap is a new renderer") ALREADY FIRED: since the 2026-06-22 four-module
census the family grew to 9 modules / ~12 `bytes | None` entrypoints, and 4+
sit outside the without-pillow test net — `character_render` (no such test),
both `image_builders` builders (no unit-test file at all, while the module
docstring :10-11 claims the contract), `btd6/ct_map_render` (gates on
`pillow_available()`, never forces the ImportError).

Verdict: **parked(routed — superbot lane build, ride the
leaderboard-row-avatars ORDER)**, Sequence-pinned `before superbot builds
leaderboard-row-avatars`. No sim question (deterministic test tooling — the
monkeypatch test either reds or passes; the PR #204 avatars-probe precedent).
Best implementation found: explicit `(callable, sample_kwargs)` registry in
`tests/unit/utils/test_card_render_contract.py`, monkeypatch reused verbatim
from `test_welcome_render.py:39-50`, sample kwargs lifted from each module's
existing tests; ~25–40 lines, deletable in one revert. Soft dependency
declared honestly: riding the avatars PR is the cheapest carrier, not a
precondition — the 4 uncovered entrypoints pay for the guard today.

**Section-collision flag (dispatch boundary — no claim file):** this slice is
barred from `control/`, so no `control/claims/` entry exists; the born-red
first commit of this card carried the `ideas/superbot/` collision flag per the
PR #222/#225/#226 workflow convention.

## Close-out

**Evidence:**

- ideas touched (2): `ideas/superbot/pil-card-render-contract-guard-2026-07-10.md`
  (state flip captured→parked(routed) + Sequence pin + probe report append),
  `ideas/superbot/README.md` (index bullet re-badge)
- sessions touched (1): `.sessions/2026-07-12-pil-card-render-contract-guard-probe.md`
- code touched: none · control touched: none (dispatch boundary; READ-ONLY read
  of `control/status.md` @ `42f9642` for the ledger entry)
- git: branch `probe/pil-card-render-contract-guard` off main `a660bc9`,
  born-red card first commit `fbc55bd`, probe+close-out commit follows; draft
  PR flipped ready on green per dispatch instructions.
- verify: `python3 bootstrap.py check --strict` and
  `python3 scripts/preflight.py` run before push (results in the PR).

**Judgment (the half only the session knows):**

- Decisions made: no D-entry — probe verdict only (park, routed, ride-along on
  the avatars ORDER, Sequence-pinned). One evidence-over-claim call, declared:
  the ledger prices the guard as "cheapest riding the avatars PR"; the live
  scan showed the guard pays INDEPENDENTLY (4+ entrypoints already uncovered,
  including the very function the avatars PR will edit), so the park names the
  ride-along as cheapest-carrier, not precondition — if the avatars ORDER
  stalls, the guard should still route.
- Next session should know: when the manager routes the leaderboard-row-avatars
  ORDER (already a carried sweep flag), the guard line must ride it — one
  test-only commit, recipe in the probe Q8. Guard recipe: registry test at
  superbot `tests/unit/utils/test_card_render_contract.py` (new), monkeypatch
  donor `tests/unit/utils/test_welcome_render.py:39-50`, family census in the
  probe Q3 (9 modules, entrypoint line numbers @ `1ecc211`); test target
  `pytest tests/unit/utils/test_card_render_contract.py` on a Pillow-less env.

## 💡 Session idea

A module docstring that DECLARES a contract ("Same contract as X: lazy PIL
import, bytes|None" — image_builders.py:10-11) while nothing tests it is a
strictly worse state than silence: it teaches the next author the contract
exists while leaving them free to break it. A cheap lint shape falls out: any
docstring matching "same contract as" must name a test that pins it — the
claim line is greppable, the guard is the registry entry this probe routes.

## ⟲ Previous-session review

PR #225 (contract-driven-explorer-facets probe): adopted wholesale — (a)
verify-at-live-HEAD-first paid off again: the ledger's `d647b2e` pin was 21
commits stale, and the byte-unchanged diff is what lets every PR #204 finding
carry to `1ecc211` without re-derivation; (b) the born-red-card collision flag
(no claim file under the dispatch boundary) used verbatim; (c) its
same-window-different-rider Sequence cross-naming rule applied here — this
file's Sequence pin names the avatars ORDER, and the avatars index bullet
already names the render seam. Its card was hand-written from the first
commit; same here, no auto-draft correction needed.

- **📊 Model:** fable-5 · single-pass battery (no panel triggers) · docs-only
  probe slice (one probe append + state flip + Sequence pin + index re-badge +
  card; no code)

## Handoff → next wake

The ride-along needs a coordinator heartbeat line so the manager's sweep sees
"avatars ORDER = carry the render-contract guard commit" (this slice could not
write one — dispatch boundary). Re-check trigger on future superbot re-pins:
if `tests/unit/utils/test_card_render_contract.py` appears at a new S, flip
this idea historical(lane-built); if the avatars PR lands WITHOUT the guard,
the park's ride-along leg is dead and the guard should route standalone.
Recipe: `git ls-remote https://github.com/menno420/superbot.git HEAD`, then
ls-tree grep `test_card_render_contract` and the image_builders.py:90
signature at the new SHA.
