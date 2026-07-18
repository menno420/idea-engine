# PROPOSAL 144 — Hot-hand streak-selection bias: in a FINITE sequence of N fair coin flips, the expected fraction of heads on flips that immediately follow a run of k heads is strictly BELOW 0.5 — a memoryless fair process looks anti-streaky under the natural "what happens after a streak?" estimator (Miller & Sanjurjo, round-33 UNRELATED slot)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card is committed FIRST with an `in-progress` status so in-flight work is visible to parallel sessions; it deliberately holds the PR's `substrate-gate` red until the slice is complete and verified. The flip to `complete` is the LAST commit and is what releases the landing workflow. No gate is bypassed; a red gate AFTER the flip is a real defect, not the HOLD.

## Objective

Draft and land round-33 UNRELATED-slot PROPOSAL 144 — the hot-hand streak-selection bias (Miller & Sanjurjo, Econometrica 2018). Folk belief: "a fair, memoryless coin has no memory, so the fraction of heads on the flips that come right after a streak of heads must be exactly 0.5." Counterintuitive claim: in a FINITE sequence of N fair coin flips, if you select every flip that immediately follows a run of k consecutive heads and average the per-sequence fraction-of-heads across sequences, the EXPECTED value is strictly BELOW 0.5 — not 0.5 — because conditioning on "the previous k flips were heads" and averaging the ratio within finite sequences induces a negative selection/sampling bias. Ship a markdown-first card, a committed stdlib-only verifier (SEED=20260717, exact enumeration reference + Monte-Carlo, three ordered gates), a deterministic double-run, an outbox block (P144 → V157, +13), and a heartbeat update. VERDICT 157 (P144 → V157, +13) is the next independent slice, NOT written here.

## Constraints honored

- Markdown-first card + committed stdlib-only verifier (`random, math, json, hashlib` only), SEED=20260717, exact finite-sequence expectation via exhaustive 2^N enumeration as the closed-form reference, Monte-Carlo estimate over M random sequences, three ordered z-gates against SIGMA_GATE=3.0.
- Deterministic: byte-identical double run (two CLI runs, diff exit 0), exit 0, disclosed results-dict sha256 (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture — no results_sha256 key inside the hashed dict, no on-disk JSON, every float rounded to 6 dp, stdout pretty indent=2 dump distinct from the compact hashed preimage; the P127+ TWIST).
- Born-red first commit (claim + card) → pushed at once → PR opened READY → flip complete last, after the heartbeat.
- Outbox PROPOSAL 144 block appended once per grammar (+13 offset → V157); did NOT write the verdict.
- Deduped against ideas/ + the full outbox history — distinct from every prior fleet/unrelated head; the hot-hand was a named runner-up dropped on merit in the secretary-rule-cardinal-regret card and has never been proposed.

## What happened

_(pending — filled at the complete flip)_

## ⟲ Previous-session review

_(pending — filled at the complete flip)_

## 💡 Session idea

_(pending — filled at the complete flip)_

## GROUNDING

_(pending — filled at the complete flip)_
