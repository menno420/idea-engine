# Settings presets everywhere + AI template advisor — idea capture (2026-06-10) — link index

> **State:** parked(split-priced — built half: Q-0215/D-0025 settings-preset grammar + fences with numeric pickers and D-0071 behavior presets live at superbot-next; open half: `PresetKind.TEXT` has zero consumers (`dm_template` still a bare str @ N `d3dba9b`) = one in-lane slice, and the §2 AI advisor stays owner-gated captured-only; probe 2026-07-12)
> **Class:** product · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/settings-presets-and-ai-template-advisor.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/settings-presets-and-ai-template-advisor.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/settings-presets-and-ai-template-advisor.md)).

Two-part capture: settings presets offered everywhere (the posture is an answered owner decision, Q-0070) and an AI template advisor that recommends a preset from the server's shape (captured only).

## Probe report (v0, 2026-07-12)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/settings-presets-and-ai-template-advisor.md@fd638e3 · fetched 2026-07-12
> *(pin annotation: superbot live HEAD S = `1ecc21138fe0a1eb672d03b66bd319164c29d55f` by `git ls-remote` — the canonical doc is byte-identical at S HEAD vs the `fd638e3` harvest pin (md5 `12e6c507…` both), status still `ideas`. The capture is TWO-part by its own header: §1 posture = ANSWERED owner decision Q-0070 (2026-06-10, owner words verbatim in router §30: presets → preset-then-edit → always-manual, for every setting class incl. authored text); §2 AI template advisor = "captured only, not approved", explicitly "an idea for later" behind the AI per-exposure gates.)*
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-next/d3dba9b53bf87ededee6ed4942a1e7c87e185add/sb/spec/settings.py@d3dba9b · fetched 2026-07-12
> *(pin annotation: superbot-next read as a blobless clone checked out at N = `d3dba9b`; live HEAD `71af879` is one commit ahead (money-race lint checker — unrelated). `PresetKind {none, numeric, text}` (lines 85–91) + `SettingSpec.presets`/`preset_kind` (lines 131/140) cite Q-0070/Q-0215 by name; the Q-0215 compile fence (lines 322–328) reds a str-typed spec whose presets omit `preset_kind=text`, and runs at manifest registration (`sb.kernel.settings.register_manifest_settings` — D-0025) and in CI.)*
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/owner/maintainer-question-router.md@fd638e3 · fetched 2026-07-12
> *(pin annotation: router §30 Q-0070 verbatim (the owner answer this capture preserves) and Q-0215 (2026-07-02, DIRECTED): the posture folded into the rebuild grammar as `preset_kind`, with the scope boundary verbatim — "this decides the **grammar primitive** only — it does not re-open Q-0070's deferred 'AI-suggested template/preset advisor' idea … which stays captured-only behind the AI per-exposure gates.")*

> Single-pass battery (panel not escalated: link-index head over an answered owner
> posture, reversible park, no security/data/spend blast radius — README § probe
> battery). Cross-lane verify-first applied (PR #180 card): the file's `**Target:**`
> is legacy `menno420/superbot`, but the settings surface lives in the rebuild now —
> superbot-next's decision ledger and code were read at N before pricing, and that
> read reshapes the head: the window this probe was minted under (grammar not yet
> decided; PR #223's zero-preset `panels.py` read) is PARTLY CLOSED — band 1 already
> minted and fenced the settings-preset grammar on 2026-07-08 (D-0025), and the nav
> golden's `presets_checked` arm-later leg awaits a DIFFERENT preset sense (Q-0232
> interface/visibility presets), not this head's settings-value presets.

**The three preset senses at N, kept apart (the load-bearing dedup):** legacy
discovery already ruled "preset/template is reinvented ~14× — centralize into one
preset/template FAMILY … a family of three declared kinds (value-seed /
operation-bundle / visibility-bundle) sharing one pick→edit→manual UX" (superbot
`docs/analysis/rebuild-discovery/foundations/runtime-logic-mechanics-2026-07-03.md`
@ fd638e3). At N `d3dba9b`: **value-seed = THIS head's §1** — grammar BUILT
(`PresetKind` + fences, D-0025) with numeric consumers live; **operation-bundle** —
partially built (seven seeded AI behavior presets applying through ONE audited
policy write, D-0071; quick/essential setup presets + `setup_ai_advisor` explicitly
parked as named-successor work, D-0027/D-0048); **visibility-bundle = Q-0232
interface presets** — absent everywhere, and THAT is what `sim/navigation_walk.py:56`
(`presets_checked: bool = False   # arm-later: band-1 preset grammar`) waits on.
A dedicated `SettingsPresetSpec` was proposed and REFUTED
(`docs/planning/rebuild-amendments.yml:108` — "existing presets + kernel
WorkflowRef; 'atomic apply' claim was false"). Section dedup: the only neighbor is
`review-log-frequency-preset-suggestions-2026-07-10.md` (captured — a preset
AUTHORING nudge from recurring questions; related, distinct, not consumed here).

**1. What is this really?** Two ideas fused in one capture. §1 is not an idea at
all — it is Q-0070, an answered owner posture (presets primary → preset-then-edit →
manual always), already mechanized into the rebuild grammar by Q-0215 and built at
band 1 (D-0025): `SettingSpec.presets`/`preset_kind` with a compile fence that reds
decorative presets. §2 (the AI template advisor — recommend the right
template/preset per task/server) is the only actual IDEA here, and the owner's own
words gate it: "captured only, not approved … an idea for later." The capture's
trigger complaint (four live free-text modals) is HALF-served at N: numeric presets
render as picker pages (`sb/domain/ai/settings_widgets.py` — one slot button per
preset, current highlighted, Override→modal keeps manual entry) and
`ai_guild_instruction_profile`'s job moved to the typed behavior-preset catalog
(D-0071); but `moderation.dm_template` is still a bare str with no presets
(`sb/manifest/moderation.py:57-59`) and `warn_timeout_minutes` carries bounds only
(`:41-42`) — the exact settings that sparked Q-0070 are still preset-less.

**2. What is the possibility space?** Along the family axis: finish value-seed TEXT
(curated authored-text presets for the trigger settings), then the operation-bundle
successors (quick/essential setup presets — already ledgered as named-successor
work), then Q-0232 visibility bundles (which is also what arms the nav golden's
fourth leg). Along the §2 advisor axis, a ladder: static per-preset metadata
(exists — `recommended_mode`) → a read-only "suggested preset" line on the existing
pickers → suggest-then-apply through the audited seams → the owner's full "custom
AI design" generation. Every rung composes with the §1 posture (suggest → preset →
edit-from-preset → manual — the advisor adds a recommendation layer, it never
removes the manual path).

**3. Most advanced capability reachable by the simplest implementation?** The TEXT
flip. Grammar, fence, tri-state storage, audited write op, picker pattern, and the
edit-from-preset modal shape ALL exist at N; `rg 'preset_kind=' sb/` returns ZERO
consumers of `PresetKind.TEXT`. One lane slice — author curated `dm_template`
starter presets, declare `preset_kind=text`, extend the widget dispatch with a
text-presets page (pick → prefilled modal → manual) — closes the capture's original
complaint with no new decisions: Q-0215 already decided the rule.

**4. What breaks it?** (a) Nothing forces adoption: the Q-0215 fence fires only
when a str spec DECLARES presets — it cannot red a spec that simply omits them, so
with the rebuild already "through all seven port bands" (N README) the text half can
stall silently unless a slice claims it; the fence enforces honesty, not coverage.
(b) Building §2 now violates an explicit owner boundary — Q-0048's standing lift
covers read-only deterministic tools only, an advisor UI "needs its own lift", and
Q-0215 restated the deferral verbatim. (c) Preset-sense conflation mis-prices
everything downstream: this head neither blocks nor is blocked by the nav golden's
arm-later leg (that leg is Q-0232's), and the settings grammar this probe was raced
against was already minted four days before the race was called.

**5. What does it unlock?** Priced honestly: the section's last "presets" head
de-links from the nav-golden dependency chain (index correction), the §1 remainder
becomes a named one-slice lane target instead of a vague "presets everywhere"
aspiration, and the §2 advisor gets its promotion gates restated against rebuild
reality (per-exposure lift = still owner-only; Q-0063 typed profiles = effectively
converged via the D-0071 catalog; preset infrastructure = numeric done, text
pending).

**6. What does it depend on?** §1 text half: nothing new — one lane slice plus
curated preset CONTENT, which is owner-voice authoring, not engineering. §2
advisor: an owner per-exposure lift (Q-0048 scope), plus text presets existing to
recommend; its Q-0063 typed-profile gate is substantially met at N (the seeded
`ai_instruction_profile` catalog with audited `apply_preset`).

**7. Which lane should build it?** superbot-next — the file's `**Target:**` says
legacy `menno420/superbot`, but the settings surface, the grammar, and both live
preset consumers are rebuild-side; the legacy "settings-audit Phase 4" home named
by Q-0070 is superseded by the band sequence (state-drift noted on the index; the
harvested header stays as harvested). Nothing routes to sim-lab: no parameter
space, no corpus, no deterministic metric — preset content is authoring and the
advisor's promotion is an owner gate, both judgment-only. NO outbox entry.
Forwardable watch (Rule-6, body-exists-is-not-body-wired): when the first
`preset_kind=text` spec lands, verify a text-preset picker actually renders — the
widget dispatch handles `numeric_presets` only today.

**8. Smallest shippable slice?** None here (the link-index stays; this pricing is
the deliverable). At the lane: the §1 text-flip slice from Q3. For §2, the smallest
LATER slice post-lift: a read-only "suggested preset" line on the existing pickers
fed by static catalog metadata — recommendation without a new write surface.

**Recommendation: park** — split-priced: the posture half (§1) is built-at-target
in grammar and fences (Q-0215/D-0025) with numeric pickers and audited behavior
presets live (D-0071), leaving one in-lane TEXT-consumer slice that needs no new
decisions; the advisor half (§2) is explicitly owner-gated captured-only (Q-0070,
restated by Q-0215's scope boundary) — nothing sim-shaped, nothing to route.
