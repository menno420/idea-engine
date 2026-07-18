# PROPOSAL 138 — usage-based billing variance shock (round-32 VENTURE slot)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card holds the PR red from its first commit until the slice is complete and verified; flipping to `complete` releases the landing workflow.

## Objective

Draft and land round-32 VENTURE-slot PROPOSAL 138 — the usage-based billing variance shock: under consumption pricing a firm's monthly revenue R = Σ Uᵢ is a sum over many independent accounts, so the folk model says the coefficient of variation falls like CV_account/√N. That is FALSE when account SIZES are heterogeneous: independent-but-unequal accounts add in variance weighted by size², so CV(R) = CV_account·√HHI with HHI = Σwᵢ² and effective account count N_eff = 1/HHI, NOT N. With Zipf sizes (mᵢ = 1/i, i=1..400) a 400-account book has N_eff ≈ 26 — revenue is ~4× more volatile than the law of large numbers predicts, a shock the LLN hides because size concentration (Cauchy–Schwarz forces HHI ≥ 1/N), not customer count, sets the variance floor. Ship a markdown-first card, a committed stdlib verifier (SEED=20260717, deterministic size vectors + batch-means SE, three ordered ≥3σ /se gates G1→G2→G3, whole-dict sha256), a real dry-sim, an outbox block (P138 → V151, +13), and a heartbeat update. VERDICT 151 (P138 → V151, +13) is the next independent slice, not written here.

## Constraints honored

- Markdown-first card + committed stdlib verifier (hashlib/json/math/random only), SEED=20260717, three ordered gates on the Herfindahl closed-form anchors computed exactly from the deterministic size vectors.
- Deterministic: byte-identical double run, exit 0, disclosed results-dict sha256 (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture — no results_sha256 key, no on-disk JSON, stdout pretty dump distinct from the compact digest preimage).
- Batch-means (method of independent replications) for a valid distribution-free SE on the CV ratio estimator; B independent batches, one CV estimate per batch.
- Born-red first commit → PR READY at once → flip complete last, after the heartbeat.
- Outbox PROPOSAL 138 block appended once per grammar (+13 offset → V151); did NOT write the verdict.
- Deduped against ideas/ + full outbox history — distinct from P109 correlated-fleet-variance-floor (correlation-driven floor, not size heterogeneity), P134 blended-churn LTV understatement (Jensen convexity in a POINT estimate, not a second-moment RISK result), and P122 NRR composition mirage.
