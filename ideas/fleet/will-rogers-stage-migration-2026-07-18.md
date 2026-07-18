# PROPOSAL 148 — The Will Rogers phenomenon (stage migration): reclassifying members across a group boundary can raise the mean of BOTH groups at once while the population mean is EXACTLY unchanged. Move a member from the higher-mean group into the lower-mean group whose average it beats, and the higher group sheds a below-its-mean member while the lower group gains an above-its-mean member — so both subgroup means rise, even though not one member's value changed and the pooled mean is identically conserved. "Every subgroup improved" and "the population improved" are DIFFERENT claims; they coincide only when group membership is fixed.

> **State:** sim-ready
> **Class:** unrelated-domain (round-34 unrelated slot) · classification / measurement artifact — reclassification across a group boundary · PROPOSAL 148
> **Anchor:** the Will Rogers phenomenon — "when the Okies left Oklahoma and moved to California, they raised the average intelligence level in both states"; the serious form is medical STAGE MIGRATION (Feinstein, Sosin & Wells, NEJM 1985): finer diagnostics reclassify borderline patients from an early (better) stage into a late (worse) stage, and the stage-specific survival of BOTH stages rises with no change to any patient's outcome
> **Target:** sim-lab (VERDICT 161, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@b948e5c0a068c94361686480eb4f91d32599aee3 · fetched 2026-07-18
> **Reference (external, reachable):** [Will Rogers phenomenon — Wikipedia](https://en.wikipedia.org/wiki/Will_Rogers_phenomenon) — verified reachable 2026-07-18 via WebFetch ("the mathematical phenomenon whereby moving an element from one set to another can raise the average values of both sets … used in medical stage migration: improved detection of illness leads to the movement of people from the set of healthy people to the set of unhealthy people … statistical processes can produce apparent improvements to both groups without any real change")
> **Verifier (firsthand):** `ideas/fleet/will_rogers_stage_migration.py` · results-dict sha256 `79b7443f3c993d830de4cd9d63c2ce826111e45ec426c3fd8bf17a8c33306470`
> 📊 Model: Claude Opus · high · idea/planning

## Domain

Classification / measurement artifacts — outside the fleet, venture, and game-mechanics domains. The object is the humblest possible one: N members, each with a single FIXED real number (read "normalised survival / quality — higher is better"), split into two groups by a threshold. The question is the one every stage-specific or segment-specific dashboard implicitly asks: *if the average outcome went up in every subgroup, did the population improve?*

## The folk belief

"If the average improves within EVERY subgroup, the population as a whole must have improved — you cannot make every part better without making the whole better. When early-stage survival rises AND late-stage survival rises, care got better; when the low tier's average is up AND the high tier's average is up, the population is up." This is the intuition every stage-specific / cohort / tier dashboard rests on: read subgroup means, and if they all move the same way, attribute a real population change.

## The thesis (reasoned to its fuller form — Q-0254 duty)

Both group means can rise at once while the pooled mean is EXACTLY unchanged — with no member's value changing anywhere — purely because a member was RELABELLED across the boundary. The "all subgroups improved" reading is wrong whenever the group boundaries themselves moved.

The mechanism is **reclassification / stage migration**, not real change:

- Partition N members COARSELY at a threshold into a LOW group (below the threshold) and a HIGH group (at or above it). By construction HIGH's mean exceeds LOW's mean.
- A FINER classifier now migrates the **bottom slice of HIGH** — members whose value sits just above the coarse threshold — DOWN into LOW. Call a migrated member `x`. Because it came from the bottom of HIGH, `x` is BELOW HIGH's mean; because it was above the coarse threshold, `x` is ABOVE LOW's mean. So `LOW_mean < x < HIGH_mean`.
- Removing `x` from HIGH removes a below-HIGH-mean member → **HIGH's mean rises**. Adding `x` to LOW adds an above-LOW-mean member → **LOW's mean rises**. Both go up.
- Nothing but the LABEL changed: the value multiset is identical before and after, so the **pooled mean is identically conserved**. The two partitions are a permutation of the same members.

This is the Will Rogers phenomenon: move a member from the higher-mean set to the lower-mean set whose average it exceeds, and both set averages increase. In medicine it is **stage migration** — better imaging finds micro-metastases in patients previously staged "early", moving the worst-prognosis early patients (who are still better than the average late patient) into the "late" stage, so stage-specific survival rises in BOTH stages with no treatment change (Feinstein, Sosin & Wells, NEJM 1985).

It has an exact **closed form**. For values Uniform[0,1] with a coarse split at 0.5 and a migrated slice [0.5, 0.6): LOW mean 0.25 → 0.30, HIGH mean 0.75 → 0.80 (both +0.05), pooled 0.5 → 0.5 (conserved). The improvements are deterministic quantities, computable by integrating the uniform density over each region — no simulation needed to know the sign or size.

## The trap

Any audit that reads a segmented metric and concludes "the population improved because every segment improved" is measuring the boundary move, not the phenomenon — whenever the segmentation is not held fixed. It will (i) declare a genuinely unchanged population "improved across the board," and (ii) credit a reclassification, a re-bucketing, or a changed inclusion criterion as a real gain. The correct control is the **pooled total on a fixed denominator**, which the relabelling conserves exactly.

## Formal model (committed constants)

N members, each with a value v ~ Uniform[0,1] drawn once and FIXED. Coarse classifier: LOW = {v < T_COARSE}, HIGH = {v ≥ T_COARSE}. Finer classifier: members of HIGH with v < T_FINE migrate into LOW (the bottom slice of HIGH). Per-trial statistics: LOW/HIGH means before and after migration, and the pooled mean computed identically before and after (the value list is never modified). R independent trials share the pinned SEED via a per-trial offset (paired across the before/after contrast by construction — same members). Pinned: SEED=20260717, N=4000, R=40, T_COARSE=0.5, T_FINE=0.6, CONS_TOL=1e-9, SIGMA_GATE=3.0. The **exact** closed-form group means (0.25/0.30 for LOW, 0.75/0.80 for HIGH, pooled 0.5) are reported in the results dict as the reference the Monte-Carlo means land on.

## Pre-registered gates (ordered; each on the /se margin, one pinned SEED)

| Gate | Statistic | Claim | Pass rule |
|---|---|---|---|
| **G1** estimator-agreement | z = (mean_firsthalf − mean_secondhalf) / se_diff | the two independent halves of the R low-group improvements do not disagree (the estimate is stable, not a split artifact) | \|z\| < 3 |
| **G2** conservation control | z = pooled_impr / se; cons_max_rel; count conservation | the POOLED population mean does NOT improve — conservation holds (max relative pooled change ≤ CONS_TOL, counts conserved) and the pooled change is not significantly positive | cons ∧ \|z\| < 3 |
| **G3** head (both subgroups) | z_low, z_high = impr / se; head_z = min(z_low, z_high) | BOTH subgroup means rise significantly at once, even though G2 proved the whole did not move | both impr > 0 ∧ min(z_low, z_high) ≥ 3 |

## Pre-registered decision rule

sim-ready iff G1 ∧ G2 ∧ G3 all pass, in order, at the pinned SEED, with a deterministic double-run reproducing the disclosed results-dict sha256.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)

```
{
  "all_pass": true,
  "closed_form": {
    "high_after": 0.8,
    "high_before": 0.75,
    "high_improvement": 0.05,
    "low_after": 0.3,
    "low_before": 0.25,
    "low_improvement": 0.05,
    "pooled": 0.5
  },
  "count_conserved": true,
  "first_failing_gate": null,
  "g1_agreement": true,
  "g1_half_a_impr": 0.049696,
  "g1_half_b_impr": 0.049445,
  "g1_z": 0.361594,
  "g2_cons_max_rel": 0.0,
  "g2_control": true,
  "g2_pooled_impr": 0.0,
  "g2_z": 0.010159,
  "g3_head": true,
  "g3_head_z": 133.926813,
  "g3_high_impr": 0.049516,
  "g3_high_z": 133.926813,
  "g3_low_impr": 0.049571,
  "g3_low_z": 144.191642,
  "mean_high_after": 0.799861,
  "mean_high_before": 0.750344,
  "mean_low_after": 0.298889,
  "mean_low_before": 0.249318,
  "mean_n_migrated": 395.55,
  "n": 4000,
  "params": {
    "cons_tol": 1e-09,
    "t_coarse": 0.5,
    "t_fine": 0.6
  },
  "proposal": 148,
  "r": 40,
  "seed": 20260717,
  "sigma_gate": 3.0
}
Results-JSON sha256: 79b7443f3c993d830de4cd9d63c2ce826111e45ec426c3fd8bf17a8c33306470
G1 agreement    : PASS (low half_a-half_b, z=+0.36, |z|<3.0)
G2 control      : PASS (pooled impr=+0.000000, cons_max_rel=0.00e+00, z=+0.01, not-sig-positive z<3.0)
G3 head         : PASS (low impr=+0.0496 z=+144.19, high impr=+0.0495 z=+133.93, min z=+133.93>=3.0)
all_pass        : True first_failing_gate: None
```

All three gates PASS in order; exit 0; the second run reproduces the identical sha256. The Monte-Carlo group means land on the closed form (LOW 0.249318 → 0.298889 ≈ 0.25 → 0.30; HIGH 0.750344 → 0.799861 ≈ 0.75 → 0.80), both subgroups rise ~+0.0496 at ≥133σ, and the pooled mean is conserved to floating-point (cons_max_rel 0.0, pooled_impr +0.000000).

## Reproduce

```
python3 ideas/fleet/will_rogers_stage_migration.py
```

Expected: prints the results JSON, `Results-JSON sha256: 79b7443f3c993d830de4cd9d63c2ce826111e45ec426c3fd8bf17a8c33306470`, three `PASS` lines, exit 0. Deterministic: same SEED → identical results dict → identical sha256; exit 0 iff all three gates pass in order.

## Verifier

`ideas/fleet/will_rogers_stage_migration.py` — stdlib only (`hashlib, json, math, random`). Draws N fixed member values, partitions them coarsely, migrates the bottom slice of HIGH into LOW (the finer classifier), and computes per-trial before/after subgroup means and the conserved pooled mean over R trials, then runs the three ordered z-gates (half-vs-half estimator agreement, the conservation control, and the both-subgroups-rise head). Emits the whole results dict (no self-referential sha field; every float rounded to 6 decimals; the compact canonical serialization's sha256 IS the disclosed digest; stdout dumps the pretty indent=2 view — the WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture, P127+ twist). Writes no JSON to disk.

## Fleet relevance

The fleet reads segmented metrics constantly: per-lane pass rates, per-cohort success, per-tier throughput, "green builds by repo," reliability by severity bucket. Any dashboard that concludes "the program improved because every segment improved" is running the Will Rogers estimator whenever the segmentation moved between the two snapshots — a lane reclassified from "active" to "dormant," a task re-bucketed by a new difficulty cut, an inclusion criterion tightened, a stage boundary redrawn. The transferable rule: **when a segmented metric is up in every segment, the population is not proven to have improved unless the segment boundaries are held fixed — a moving boundary can manufacture across-the-board subgroup gains from pure relabelling.** Guard it by carrying the conserved pooled total on a fixed denominator alongside every segmented view; if the pooled total is flat while every segment is up, suspect a boundary move (stage migration), not real progress.

## Why it matters (beyond the fleet)

Stage migration is why "5-year survival by stage improved in every stage" can be true across a decade in which no treatment got better — better imaging simply moved patients between stages. The same artifact drives "our churn improved in both the SMB and Enterprise segments" when the SMB/Enterprise cut was redrawn, "test scores rose in both the passing and failing groups" when the pass mark moved, and "quality is up in both the reviewed and auto-merged buckets" when the review threshold changed. The fix is always the same: hold the classifier fixed, or report the pooled total that relabelling conserves.

## Dedup

Distinct from every prior fleet/unrelated head. The unrelated-domain lane has spanned Kelly overbetting, epidemic overshoot (SIR), regression to the mean, series reliability/MTBF, the arcsine lead illusion, German-tank estimation, Benford, Stein shrinkage, birthday collisions, base-rate / PPV collapse, gambler's ruin, hot-hand streak-selection, variance-blind provisioning, coupon-collector tail, the inspection paradox, the secretary problem, Parrondo's games, Simpson's aggregation reversal, Braess's paradox, and the friendship paradox — none of them is a **reclassification / stage-migration** artifact where both subgroup means rise on a conserved population. Nearest rhyme, disclosed: **Simpson's paradox** (`simpsons-paradox-aggregation-reversal`) is an aggregation reversal on FIXED groups (a trend within every group reverses when pooled); this is the OPPOSITE move — the GROUPS change (a member is relabelled) and both group means rise while the pooled mean is fixed. Simpson's asks "does the pooled trend match the within-group trend"; Will Rogers asks "can every within-group mean rise while the pooled mean is unchanged" — the answer is yes, and only a boundary move produces it. A grep of `ideas/` and `control/outbox.md` at HEAD for "will rogers" / "stage migration" returned zero hits; this head takes an open slot.

## Model basis (declared model-dependence — the P024 discipline)

The result is a theorem about relabelling a member across a group boundary: it holds for ANY value distribution and ANY thresholds under which the migrated slice sits strictly between the two group means (LOW_mean < migrated values < HIGH_mean). It is model-dependent on exactly that condition — if the migrated slice were ABOVE the HIGH mean, moving it down would LOWER the HIGH mean (only one subgroup would rise); if BELOW the LOW mean, adding it would lower the LOW mean. The specific magnitudes (+0.05 each, pooled 0.5) are pinned to Uniform[0,1] with (T_COARSE, T_FINE) = (0.5, 0.6); the SIGN (both rise) holds for the whole interior band. The single declared modelling choice, flagged not hidden: the migration direction is HIGH→LOW (the bottom slice of the higher group moves into the lower group), which is the stage-migration direction (borderline members reclassified into the group whose mean they beat) and the cleanest way to make both means rise at once. The conservation of the pooled mean is exact by construction (the value multiset is never modified), which is precisely what proves the subgroup gains are a relabelling artifact and not real change.

## Probe report (v0, 2026-07-18)

**1. Real or a coding artifact?** Real — it is the Will Rogers phenomenon / medical stage migration (Feinstein, Sosin & Wells, NEJM 1985). The exact closed-form group means (LOW 0.25→0.30, HIGH 0.75→0.80, pooled 0.5) are computed analytically and the Monte-Carlo means land on them (mean_low 0.249318→0.298889, mean_high 0.750344→0.799861).
**2. Could the both-rise result be a seed fluke?** No — 40 trials of N=4000 members (~395 migrated per trial), both subgroup improvements clear at z≥133σ, and the estimate is split-half stable (G1 z=+0.36).
**3. Is this just Simpson's paradox dressed up?** No — Simpson's is an aggregation reversal on FIXED groups; here the GROUPS change (a member is relabelled). Both subgroup means rise while the pooled mean is EXACTLY conserved — a phenomenon of MOVING boundaries, not fixed-group aggregation.
**4. Why does the pooled mean not move?** Because migration only changes a member's LABEL, never its value — the value multiset is identical before and after, so the pooled mean is conserved by construction (cons_max_rel 0.0, count_conserved true). That exact conservation is the whole point: it proves the subgroup gains are relabelling, not real change.
**5. Why N=4000, T_FINE=0.6?** N=4000 makes both subgroup improvements unmistakable (~+0.0496) with tight standard errors while keeping the run instant; T_FINE=0.6 places the migrated slice [0.5,0.6) strictly between the two group means (0.25 and 0.75), the interior band where BOTH means rise. A larger T_FINE past the HIGH mean would flip HIGH's sign (disclosed as model-dependence).
**6. What about members exactly at the threshold?** Continuous Uniform[0,1] draws hit an exact threshold with probability zero; the coarse split uses v < T_COARSE / v ≥ T_COARSE and the migrated slice is T_COARSE ≤ v < T_FINE, a clean partition with counts conserved every trial.
**7. What breaks it?** A migrated slice above the HIGH mean (only one subgroup rises) or below the LOW mean (the other falls); both are disclosed model-dependence. Holding the classifier FIXED removes the artifact entirely — which is exactly the guard.
**8. Actionable?** Yes — any segmented "every subgroup is up" audit in the fleet must carry the conserved pooled total on a fixed denominator; if the pooled total is flat while every segment rises, suspect a boundary move (stage migration), not real progress.

Ship to sim-lab for VERDICT 161 (P148 → V161, +13). One counterintuitive result (both subgroup means rise on a population that did not change), one published anchor (Will Rogers phenomenon / stage migration, Feinstein 1985), an exact closed-form reference, three ordered ≥3σ gates (with a not-significant conservation control), a deterministic committed verifier.

**Recommendation: sim-ready**
