# Post-EAP playtest kit — a paste-ready bundle for the owner's pending verdict

> **State:** captured
> **Class:** product · **Target:** `menno420/pokemon-mod-lab`

## Problem

The lane's only pending gate is an owner item: **"playtest verdict"** (manifest row @
53fb5ef), and the owner ruled he will play the builds **after the EAP** (Q-0259 r.5),
whose window closes **2026-07-14** (manifest post-launch note). But nothing in the
lane's visible state names a packaged artifact path for that playtest — the parked
ender predates the ruling, and gba-homebrew's parallel row shows what "ready" looks
like ("owner: play it (~15 min)"). An owner ask that requires the owner to assemble a
build chain himself is a drafting defect by fleet doctrine (Q-0263 rule 2 / kit ORDER
008 class: asks are paste-ready or they don't reach the owner).

## Idea

Ship a **playtest kit** as one lane PR: (1) a pinned patch artifact for the current
12-patch build — patch format only, never a ROM (see the companion patch-only-egress
capture); (2) a one-page "what you'll notice" note listing the 12 QoL patches in
player-visible terms, so the verdict can name patches, not vibes; (3) exact apply+run
steps (patcher + emulator, click-path style); (4) a **verdict form** at the bottom —
3-5 fill-in lines (what felt good / what felt bad / option-board pick / blockers) so
the playtest output arrives machine-consumable and the improvement round (Q-0259 r.5:
"improvement rounds follow") boots from evidence instead of a chat paraphrase. Total
owner cost target: ~15 minutes, matching the gba-homebrew bar.

## Grounding

- Manifest pokemon-mod-lab + gba-homebrew rows and EAP-window note @
  [`53fb5ef`](https://raw.githubusercontent.com/menno420/superbot/53fb5ef9a294ab304b679dedd44ead55849295d5/docs/eap/fleet-manifest.md)
  (fetched 2026-07-10 ~20:35Z): "owner: playtest verdict + concept pick"; gba row
  "owner: play it (~15 min)"; "EAP window: through 2026-07-14".
- Q-0259 r.5 (owner plays after EAP, improvement rounds follow) + Q-0263 rule 2
  (paste-ready-or-nothing owner asks) @
  [`53fb5ef`](https://raw.githubusercontent.com/menno420/superbot/53fb5ef9a294ab304b679dedd44ead55849295d5/docs/owner/maintainer-question-router.md).
- Caveat, stated honestly: the lane repo is private/unreadable from here — if session
  008 already left a packaged artifact, this capture collapses to "add the verdict
  form and re-pin the artifact"; the first-boot session verifies against its own tree.

**Why now:** the EAP ends 2026-07-14 — the playtest becomes possible in days, and a kit
prepared before the owner sits down is the difference between a 15-minute verdict and a
stalled improvement round.
