# PROPOSAL 136 — base-rate PPV collapse at low prevalence (round-31 UNRELATED slot)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD released: this card held the PR red from its first commit until the slice was complete and verified; flipping to `complete` here releases the landing workflow.

## Objective

Draft and land round-31 UNRELATED-slot PROPOSAL 136 — base-rate neglect / positive-predictive-value (PPV) collapse at low prevalence: the folk belief that "a 99%-accurate test that comes back positive means ~99% chance you have it" is wrong by Bayes — PPV = (sens·prev)/(sens·prev + (1−spec)·(1−prev)), so at sens=spec=0.99 and prevalence 1% the posterior is exactly 0.5 (a coin flip), and at prevalence 0.1% it collapses to ~9.0%, because true positives (∝prev) are swamped by false positives (∝1−prev). Ship a markdown-first card, a committed stdlib verifier (SEED=20260717, three ordered ≥3σ gates G1→G2→G3, whole-dict sha256), a real dry-sim, an outbox block (P136 → V149, +13), and a heartbeat update. VERDICT 149 (P136 → V149, +13) is the next independent slice, not written here.

## Constraints honored

- Markdown-first card + committed stdlib verifier (hashlib/json/math/random only), SEED=20260717, three ordered ≥3σ gates on independently-computed closed-form anchors (PPV0=0.5 exactly, posrate=0.0198, PPV0_B=0.0901639).
- Deterministic: byte-identical double run, exit 0, disclosed results-dict sha256 (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture — no results_sha256 key, no on-disk JSON, stdout pretty dump distinct from the compact digest preimage; plus an in-process double-run assertion run()×2 compact-hashed equal).
- Born-red first commit → PR READY at once → flip complete last, after the heartbeat.
- Outbox PROPOSAL 136 block appended once per grammar (+13 offset → V149); did NOT write the verdict.
- Deduped against ideas/ + full outbox history — cites P072 (pooled-screening-prevalence-wall) and draws the line: P072 = how many tests to run (test economy, PERFECT tests); P136 = what a single positive result MEANS (posterior/PPV, IMPERFECT tests); P072 named exactly this sensitivity/specificity<1 follow-up.

## What happened

Synced to origin/main HEAD 5296576 (PROPOSAL 135 the balance-triangle pick-rate inversion just landed, #572; round-31 GAME slot). Re-scanned control/claims/ and open PRs for a competing P136 — none (the "136" hits are VERDICT 136 snipe-clearing-leak, unrelated; the only open PR is #527, VERDICT 126). Claimed P136, branched `claude/proposal-136-base-rate-ppv-collapse`, opened PR #574 READY on the born-red card. Committed the stdlib verifier; the real dry run passed all three ordered gates (G1 posterior=0.5 empirical PPV(prev=0.01)=0.497746 vs exact 0.5 z=−0.898, G2 positive-rate empirical 0.019856 vs exact 0.0198 z=+0.563, G3 collapse-deepens empirical PPV(prev=0.001)=0.092466 vs exact 0.0901639 z=+1.188), byte-identical across two runs plus the in-process double-run assertion, exit 0, results-dict sha256 89c4bd02969e51bfed210680af0d73869f93fde23149f1cc238ba77b895faac8. Authored the fleet-lane card (dedup cites P072 and draws the count-vs-posterior / perfect-vs-imperfect line, and notes P072 named exactly the sensitivity/specificity<1 follow-up), appended the outbox PROPOSAL 136 block (+13 → V149, offset cited from the P135 → V148 predecessor row + the status baton), updated the heartbeat (proposal high-water P135 → P136, round-31 proposals COMPLETE; verdict high-water held honest at V147 with V146/V148 noted pending; baton → V149 for P136 then round-32 fleet-slot P137; routines line unchanged coordinator-bound), then flipped this card to release the landing workflow. `python3 bootstrap.py check --strict` before the flip failed only on the designed born-red HOLD (all claims/owner-action/seat-digest warnings are "never exit-affecting").

## ⟲ Previous-session review

The round-31 GAME slot (P135 balance-triangle pick-rate inversion, PR #572; V148 the next slice) landed clean on the whole-dict / no-self-field / stdout-only digest posture and the +13 offset held unbroken (P133→V146 and P135→V148 pending, P134→V147 landed). This slice inherits that posture verbatim and CLOSES round-31 on the proposal side by taking the unrelated slot (rotation fleet→venture→game→unrelated). No regressions observed; the born-red HOLD behaved exactly as designed — the substrate session gate stayed red until the flip, and the only exit-affecting check finding was that designed hold. One continuity note carried forward: the verdict side of round-31 is non-contiguous (V147 landed, V146 for P133 and V148 for P135 still pending), so the V147 high-water must not be read as "all lower verdicts closed".

## 💡 Session idea

Base-rate neglect and P108 regression-to-the-mean are the same error wearing two coats: both are "the intuitive conditional is not the one you asked for" (P(disease|positive)≠P(positive|disease); E[true|observed]≠observed). Candidate follow-up: a single "converse-conditional trap" playbook card that unifies the diagnostic posterior (P136), regression to the mean (P108), and the prosecutor's fallacy under one operator checklist — "before you act on a conditional, name the base rate and the converse you actually want" — with a shared decision rule (compute the posterior at the deployed base rate; never read a forward likelihood as a posterior). It would also seed a natural round-32+ head: the MULTI-test version, where two independent positives multiply the likelihood ratio sens/(1−spec) again — quantifying exactly how much confirmation drags the posterior back up as a function of base rate, the operational cure this card only names.

## GROUNDING

- Verifier (firsthand, ground truth): https://github.com/menno420/idea-engine/blob/main/ideas/fleet/base_rate_ppv_collapse.py — results-dict sha256 89c4bd02969e51bfed210680af0d73869f93fde23149f1cc238ba77b895faac8, SEED=20260717, N=2,000,000, sens=spec=0.99, prev A=0.01 & B=0.001, three ordered ≥3σ gates PASS on the Bernoulli /se margin (G1 z=−0.898, G2 z=+0.563, G3 z=+1.188), deterministic double-run byte-identical + in-process double-run assertion, exit 0.
- Idea card: https://github.com/menno420/idea-engine/blob/main/ideas/fleet/base-rate-ppv-collapse-2026-07-18.md
- External reference (reachable): Positive and negative predictive values — Wikipedia, https://en.wikipedia.org/wiki/Positive_and_negative_predictive_values (PPV = sens·prev/(sens·prev+(1−spec)(1−prev)); "the PPV is not intrinsic to the test — it depends also on the prevalence"; low-prevalence PPV-collapse worked example) — verified reachable 2026-07-18; anchor Bayes' theorem for a binary test under a Bernoulli disease indicator.
- Grounding commit: https://github.com/menno420/idea-engine@5296576 · HEAD at start 5296576e6e668a36093d9fd12ef55e3ba0f86f29 (blob https://github.com/menno420/idea-engine/blob/5296576e6e668a36093d9fd12ef55e3ba0f86f29/control/outbox.md verified reachable 2026-07-18). PR: #574.
