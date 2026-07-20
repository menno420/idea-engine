# VERDICT 247 — put-call parity holds exactly in a no-arbitrage binomial market (independent adjudication of PROPOSAL 234)

> **Status:** `in-progress`

- **📊 Model:** Opus 4.8 · high · review/verify

## Slice
Independent adjudication of idea-engine PROPOSAL 234 (landed #840) — the risk-neutral European call/put satisfy put-call parity EXACTLY C−P=S₀−K·R⁻ⁿ in an n-period no-arbitrage binomial market (reference S₀=K=100, u=2, d=1/2, R=5/4, n=2 ⇒ C=48, P=12, C−P=36=100−64). Ruling → VERDICT 247 APPROVE (+13 offset), appended to control/outbox.md; heartbeat + high-water in control/status.md. No duplicate proposal/idea-doc/verifier authored — those already landed via #840.

## Trail
- Verifier byte-identical to sim-lab #332 mirror (diff exit 0, sha256 fb45a5cc…c8ae).
- results_sha256 637c7b8a…ede4 reproduced firsthand — two separate processes + in-process double-run guard IDENTICAL.
- Four gates each in its own direction — G1 exact Fraction parity 36==36 across a 4-market panel; G2 z=−0.112845; G3 volatility+scale invariance exact; G4 z_naive=246.993214.
- Grounding Wikipedia "Put–call parity" oldid 1304770990 re-fetched firsthand — raw wikitext 15558 bytes, sha1 8457ac93f9e181b278a8f170e3225d2afb5bed5c verified three ways (action=raw + API sha1 + API content re-hash).
- Independent quoted-vs-derived grep BOTH directions — every QUOTED item present (put-call parity 16×, no arbitrage 4×, C−P=S−D·K, C+D·K=P+S, C(t)−P(t)=S(t)−K·B(t,T), B=e^{−r(T−t)}), every DERIVED item absent (binomial numbers, "binomial", "risk-neutral" all grep 0), the single-line composed form correctly flagged composed-not-quoted — split MATCHES P234 self-report with zero seam.
- Independent from-scratch risk-neutral derivation confirms the identity non-circularly.
- Ruling: APPROVE.

## ⟲ Previous-session review

Previous-session review: VERDICT 246 (secretary / optimal-stopping best-choice selection; P233 → V246) landed APPROVE. It reproduced the committed verifier byte-identical, matched the full-64 results_sha256 digest verbatim, passed all four gates each in its own direction, and found the quoted-vs-derived boundary honest with no seam. V247 carries its GATE-POLARITY discipline (each gate read in its own direction — exact identities self-certify, Monte-Carlo z-tests are AGREEMENT gates, the deliberately-wrong model is a FALSIFIABILITY gate at opposite polarity) and its BOTH-DIRECTIONS grounding-grep discipline forward, and here the grounding is genuinely present — unlike a first stale read that mistook the pre-#840 tree for ungrounded, corrected by re-syncing to origin/main and re-grepping the pinned oldid 1304770990 firsthand.

## 💡 Session idea

💡 Session idea: a verdict's grounding integrity depends on adjudicating the proposal as it ACTUALLY landed, not a cached earlier tree. Re-syncing to origin/main before ruling caught that PROPOSAL 234 had landed Wikipedia-grounded (oldid 1304770990) after an earlier read saw only the reproduction mirror and mistook the tree for ungrounded. The honest quoted-vs-derived disposition comes from grepping the pinned revision firsthand in BOTH directions — quoted items present on the page AND derived items absent from it — which here confirmed a clean split, and is exactly why this ruling is APPROVE and not QUALIFIED.

## Status
> **Status:** `in-progress`
