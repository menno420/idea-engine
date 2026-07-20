# VERDICT 245 — coprime density = 6/π² (independent adjudication of PROPOSAL 232)

> **Status:** `in-progress`

## Slice
Independent adjudication of idea-engine PROPOSAL 232 — the probability that two integers drawn iid uniform on {1,…,N} are coprime is the exact Möbius-inversion density Q(N)=(1/N²)·Σμ(k)⌊N/k⌋² → 6/π² = 1/ζ(2), NOT the naive parity-only 3/4. Ruling → VERDICT 245 (+13 offset), appended to control/outbox.md; heartbeat + high-water in control/status.md.

## Trail
- Byte-identical verifier re-verified vs the sim-lab #328 pre-verdict mirror (diff exit 0).
- results_sha256 754580…840fec reproduced firsthand — two separate process runs (grep -F exit 0 each, full-stdout diff exit 0) + in-process double-run guard IDENTICAL.
- Four gates each evaluated in its own direction — all PASS (G1 Q(6)=23/36; G2 z=+0.774312; G3 partition invariant exact; G4 z_naive=−145.835897).
- Independent quoted-vs-derived grep of pinned Wikipedia oldid 1363371102 (raw wikitext 17251 bytes, sha1 254a5e69…8c4947c) — split accurate, no mislabeling seam.
- Ruling: APPROVE.

## Status
> **Status:** `in-progress`
