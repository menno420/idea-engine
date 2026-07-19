# PROPOSAL 180 — Typical-set "mode mirage": the most-probable sequence is the one you never see (round-42 UNRELATED slot, P180 → V193, +13)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD.** This card lands on the FIRST commit with `Status: in-progress`, holding the substrate-gate red while the verifier is authored and proven. The final commit flips it to `complete`, releasing merge-on-green. Gate-red before the flip is the born-red exception, not a defect.

## Objective
Show, with a deterministic stdlib simulation, that for n i.i.d. Bernoulli(p) symbols with p ≠ ½ the single most-probable sequence (the mode — the all-majority-symbol string) is essentially never observed, while every observed sequence carries per-symbol surprisal concentrated at the Shannon entropy H(p) and is therefore individually far LESS probable than the mode nobody sees. Probability mass concentrates AWAY from the probability maximum — Shannon's Asymptotic Equipartition Property (the typical set).

## Constraints honored
- stdlib-only (`random, math, json, hashlib, sys`); Python 3.
- SEED = 20260717 pinned; fully deterministic.
- In-process double-run determinism asserted (`compute()` run twice, dicts must be identical).
- WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest: sha256 of the compact-canonical results dict IS the digest; the dict is not self-referential; pretty dump to stdout, floats 6 dp; no on-disk JSON.
- Pre-registered ordered gates G1→G2→G3 at z_gate = 3.0, matching the shipped verifier exactly.
- Grounding URL returns HTTP 200 and documents the specific head.
- Timestamps from `date -u`.

## Gate-plan (pre-registered — must match the shipped verifier)
Base distribution: Bernoulli p = 0.7, n = 1000 symbols, M = 4000 sequences. Shifted (robustness): p = 0.9, same n, M.
- **G1 — Typical concentration.** Mean empirical entropy-rate m₀ = mean over M of ĥ = −(1/n)·log₂P(seq) sits at H(0.7) = 0.881291 bits: |m₀ − H(0.7)| ≤ ε (ε = 0.10 bits) AND the in-band fraction (|ĥ − H| ≤ ε) ≥ 0.99.
- **G2 — Mode is a mirage (≥3σ).** Observed per-symbol surprisal exceeds the mode's surprisal s = log₂(1/0.7) = 0.514573 bits by ≥ 3σ: z_sep = (m₀ − s)/se ≥ 3.0, AND the exact modal (all-heads) sequence occurs 0 times in M draws. Observed sequences are each ~2^{n·(m₀−s)} times LESS probable than the never-observed mode.
- **G3 — Robustness under a shifted distribution (≥3σ).** Repeat at p = 0.9: |m₁ − H(0.9)| ≤ ε (H(0.9) = 0.468996) AND in-band ≥ 0.99 AND z_sep₁ = (m₁ − log₂(1/0.9))/se ≥ 3.0 AND the modal sequence occurs 0 times. Concentration and the mirage both survive the distribution shift.

all_pass = G1 ∧ G2 ∧ G3.

## GROUNDING (verified at HEAD)
Shannon's Asymptotic Equipartition Property / typical set: observed long i.i.d. sequences are typical (per-symbol probability ≈ 2^{−nH}) and the typical set excludes the single most-probable sequence. Verified live 2026-07-19T18:32:26Z (HTTP 200): https://en.wikipedia.org/wiki/Asymptotic_equipartition_property@78b633eddfc34ed73d8a1a7250cc1ceb38bc1d52 — the page states individual outcomes can have higher probability than any typical-set member while observations still come from the typical set. Cover & Thomas, *Elements of Information Theory*, ch. 3 (AEP).

## Probe questions
**1.** Does the mean entropy-rate land within ε of H(p) for both p = 0.7 and p = 0.9, and does the in-band fraction clear 0.99?
**2.** Is the exact modal sequence observed 0 times in M = 4000 draws at both p values?
**3.** Is z_sep ≥ 3σ (in fact ≫) at both p, confirming observed surprisal sits far above the mode's?
**4.** Does the cross-invocation double run reproduce the results-dict sha256 byte-for-byte under SEED = 20260717?
**5.** Does the in-process double-run assertion hold (determinism)?
**6.** Does the grounding URL resolve live (HTTP 200) and document the typical-set / most-probable-sequence-is-atypical head?
**7.** Does the shifted-distribution gate (p = 0.9) preserve both concentration and the mirage?
**8.** Are the pre-registered gates here identical to the gates the verifier ships?

## Outcome
Verifier `ideas/fleet/typical-set-mode-mirage-2026-07-19.py` passes all gates under SEED = 20260717; cross-invocation double run IDENTICAL.
- Results-dict sha256: `1479479100edba6509b0275d31717a2f44b4504d6051023feffc5f13395b8c36`
- G1 concentration: mean ĥ = 0.881064 vs H = 0.881291 bits, in-band 1.0 → pass
- G2 mode mirage: base z_sep = 1308.85σ, mode_count = 0 → pass
- G3 robustness (p = 0.9): shift z_sep = 671.93σ, in-band 0.999, mode_count = 0 → pass
- all_pass = true
- PR #676; targets sim-lab VERDICT 193 (+13).

## ⟲ Previous-session review
PROPOSAL 179 (Swiss-system Buchholz tiebreak luck amplifier, round-42 GAME slot, sim-ready, targets V192, PR #673): a strong game-lane head — Buchholz "strength-of-schedule" tiebreak, meant to reward tougher pairings, instead amplifies luck because opponent strength is itself luck-correlated under Swiss pairing. Grammar clean, gates pre-registered, +13 offset consistent, no blocker seen. This UNRELATED-slot P180 continues the round-42 rotation (FLEET P177 → VENTURE P178 → GAME P179 → UNRELATED P180).

## 💡 Session idea
Companion UNRELATED head for a future slot: **the wrong-code coding penalty** — a prefix code matched to distribution q instead of the true source p pays exactly the Kullback–Leibler divergence D(p‖q) extra bits per symbol, no matter how "close" q looks; quantify the gap for a plausibly-mis-estimated source and gate the excess at ≥3σ. Clean, groundable (Kraft inequality / cross-entropy), and stdlib-checkable.
