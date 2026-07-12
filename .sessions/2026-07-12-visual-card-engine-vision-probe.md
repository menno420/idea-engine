# Session — single-pass probe: superbot visual-card-engine-vision (umbrella)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-12 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session did

Single-pass probe (battery v0, no panel triggers) of
`ideas/superbot/visual-card-engine-vision-2026-07-10.md` — TOP-5 #4 on the
fourth ledger (`control/status.md` @ `3eefb13`): the out-visual-Dank-Memer
north star + themeable card-engine strategy/roadmap umbrella. The briefed
question: with the guard (#228) owning the contract seam and the avatars
carrier (#204 probe) owning the flagship feature card, what does THIS
umbrella head still own?

Verify-first, live, per-horizon: superbot HEAD S resolved by `git ls-remote`
= `1ecc21138fe0a1eb672d03b66bd319164c29d55f` (the SAME S the #228 probe
measured — its 9-module/~12-entrypoint family census byte-carries);
superbot-next HEAD N = `cc59a6eabd603df173fad74ede53240c61f63e77`. The
decisive facts: (a) the canonical vision doc is byte-identical `fd638e3`→S
(md5 match) and N's `docs/decisions.md` is byte-identical `d3dba9b`→N —
both the harvest pin and the #223-era decision reads carry; (b) D-0038
deviation (5) STANDS at live N verbatim ("no image cards (leaderboard/rank
Pillow rendering = presentation)") and D-0061's parity ledger classes card
drift as a NAMED "successor-boundary render drift" red class — the
build-twice exposure is ledgered at the rebuild, not invisible; (c) horizon
re-measure at S: H1 shipped (THEMES registry grown to SIX skins,
card_render.py:75-149), H2 done except mining_render (no CardCanvas import;
the doc itself rules the rebase an owner visual-redesign call), H3 started
with ONE new gap found — `/myprofile` still draws `initials_disc`
(profile_render.py:67) though `avatar_disc` shipped 2026-07-01 — H4/H5
unbuilt (export surface to_png/to_jpeg only, card_render.py:462/:467; no
per-user theme surface at the seams read) and owner-gated; (d) the dedup CI
rule `rule_card_engine_helper_duplication` is live
(scripts/check_consistency.py:825); (e) superbot inbox @ S: ORDERs 001+002
both done, neither card-shaped — the avatars ORDER is still unrouted,
window open.

Verdict: **parked(umbrella — children routed or owner-gated)**. Children
NAMED, not forced into one verdict: avatars carrier (routed), contract
guard (routed, rides avatars), NEW micro-child `/myprofile` avatar_disc
adoption (flagged as a second rider on the avatars ORDER — one call-site
commit, pattern donor rank_render.py:97), mining_render redesign + H4 art
pack + H5 animation/premium themes (owner-gated). Nothing sim-shaped —
every open question is owner visual/monetization judgment; NO outbox
proposal, outbox tail unchanged.

**Section-collision flag (dispatch boundary — no claim file):** this slice is
barred from `control/`, so no `control/claims/` entry exists; the born-red
first commit of this card carried the `ideas/superbot/` collision flag per
the PR #222/#225/#226/#228 workflow convention.

## Close-out

**Evidence (auto-draft hand-corrected — the engine's diff base was wrong,
same as the #225/#226 cards):**

- ideas touched (2): `ideas/superbot/visual-card-engine-vision-2026-07-10.md`
  (state flip captured→parked(umbrella…) + probe report append),
  `ideas/superbot/README.md` (index bullet re-badge with the re-open trigger,
  PR #192 card convention)
- sessions touched (1): `.sessions/2026-07-12-visual-card-engine-vision-probe.md`
- code touched: none · control touched: none (dispatch boundary; READ-ONLY
  reads of `control/status.md` @ `3eefb13` for the ledger entry and
  `control/inbox.md` for the ORDER 003+ side check — result: ORDERs 001–002
  only, no ORDER 003+)
- git: branch `probe/visual-card-engine-vision` off main `3eefb13`, born-red
  card first commit `6bde836`, probe+close-out commit follows; draft PR #232
  flipped ready on green per dispatch instructions.
- verify: `python3 bootstrap.py check --strict` and
  `python3 scripts/preflight.py` run before push (results in the PR).

**Judgment (the half only the session knows):**

- Decisions made: no D-entry — probe verdict only (park, umbrella, children
  named). One evidence-over-worry call, declared: the ledger's "each
  unprobed card widens the build-twice cutover cost" dissolved on
  enumeration — at live S NO un-routed agent-buildable card remains under
  this umbrella, and N's own D-0061 ledger already tracks the re-port debt
  as a named red class, so the park stands on bounded-not-runaway exposure.
- Next session should know: the manager-sweep avatars-ORDER flag now carries
  THREE riders — the board card itself, the #228 contract guard, and this
  probe's `/myprofile` avatar_disc micro-child (swap
  `profile_render.py:67` initials_disc → the `rank_render.py:97`
  avatar-then-initials pattern; fetch seam `fetch_avatar_png` exists).

## 💡 Session idea

An umbrella/vision head should be probed LAST in its family, not first: this
probe was cheap precisely because #204 and #228 had already measured the
family's live state, leaving the umbrella a pure disposition question
(enumerate children → route or gate each). A probe-order heuristic falls out:
when a TOP-5 ledger carries a vision head AND its feature/guard children,
consume the children first and let the umbrella's probe be the fan-in — the
reverse order would have re-derived both censuses inside one oversized pass.

## ⟲ Previous-session review

PR #228 (pil-card-render-contract-guard probe): adopted wholesale — (a) its
same-S carry discipline paid directly: S had NOT moved (`1ecc211` still HEAD
at this session's ls-remote), so its family census byte-carried with zero
re-derivation, and the byte-identity checks (canonical doc md5, N
decisions.md diff) turned two staleness risks into carried facts; (b) the
born-red-card collision flag (no claim file under the dispatch boundary)
used verbatim; (c) its Handoff's re-check recipe shape (ls-remote → targeted
grep at the new SHA) reused for this card's re-open triggers. One friction:
the kit auto-drafted a close-out onto this card mid-session against a wrong
diff base (340 "other touched" files) — hand-corrected here; the #226 card
hit the same and the auto-draft base bug remains unfixed kit-side.

- **📊 Model:** fable-5 · single-pass battery (no panel triggers) · docs-only
  probe slice (one probe append + state flip + index re-badge + card; no
  code)

## Handoff → next wake

The avatars-ORDER sweep flag should grow the `/myprofile` rider line so the
manager routes all three (board card + guard + profile avatar swap) as one
carrier — this slice could not write a heartbeat line (dispatch boundary).
Re-open triggers on future superbot re-pins: an owner art pack landing under
`disbot/assets/` (H4 fires → season packs + H5 become buildable), or a new
renderer module appearing off-engine (grep new `disbot/utils/*_render.py`
for `card_render` import at the new SHA). Guard recipe:
`git ls-remote https://github.com/menno420/superbot.git main`, then raw-read
`disbot/utils/profile_render.py` (initials_disc gone = micro-child consumed,
flip toward historical) and `disbot/utils/card_render.py` export surface
(`save_all`/`append_images` appearing = H5 armed); test target
`python3 scripts/preflight.py` here.
