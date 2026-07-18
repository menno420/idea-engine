# PROPOSAL 136 — base-rate PPV collapse at low prevalence (round-31 UNRELATED slot)

> **Status:** `in-progress`

Born-red HOLD: this card is the session's FIRST commit and carries `in-progress` so the substrate-gate stays red and the PR cannot merge until the deliberate flip to `complete` at close-out. In-flight work is visible to parallel sessions while red; the flip is the last step of the slice.

## Objective

Draft and land round-31 UNRELATED-slot PROPOSAL 136 — base-rate neglect / positive-predictive-value (PPV) collapse at low prevalence: the folk belief that "a 99%-accurate test that comes back positive means ~99% chance you have it" is wrong by Bayes — PPV = (sens·prev)/(sens·prev + (1−spec)·(1−prev)), so at sens=spec=0.99 and prevalence 1% the posterior is exactly 0.5 (a coin flip), and at prevalence 0.1% it collapses to ~9.0%, because true positives (∝prev) are swamped by false positives (∝1−prev). Ship a markdown-first card, a committed stdlib verifier (SEED=20260717, three ordered ≥3σ gates G1→G2→G3, whole-dict sha256), a real dry-sim, an outbox block (P136 → V149, +13), and a heartbeat update. VERDICT 149 (P136 → V149, +13) is the next independent slice, not written here.

## Constraints honored

- Markdown-first card + committed stdlib verifier (hashlib/json/math/random only), SEED=20260717, three ordered ≥3σ gates on independently-computed closed-form anchors (PPV0=0.5 exactly, posrate=0.0198, PPV0_B=0.0901639).
- Deterministic: byte-identical double run, exit 0, disclosed results-dict sha256 (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture — no results_sha256 key, no on-disk JSON, stdout pretty dump distinct from the compact digest preimage).
- Born-red first commit → PR READY at once → flip complete last, after the heartbeat.
- Outbox PROPOSAL 136 block appended once per grammar (+13 offset → V149); did NOT write the verdict.
- Deduped against ideas/ + full outbox history — cites P072 (pooled-screening-prevalence-wall) and draws the line: P072 = how many tests to run (test economy, PERFECT tests); P136 = what a single positive result MEANS (posterior/PPV, IMPERFECT tests); P072 named exactly this sensitivity/specificity<1 follow-up.

## What happened

[[fill: at flip]]

## ⟲ Previous-session review

[[fill: at flip — review the P135 balance-triangle slice]]

## 💡 Session idea

[[fill: at flip]]

## GROUNDING

[[fill: at flip — verifier firsthand w/ sha256+SEED, idea card, external reference reachable, grounding commit @sha + PR #]]
