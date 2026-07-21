# claim — VERDICT 258 · open-addressing unsuccessful-search expected probes = (m+1)/(m−n+1)

- `claude/verdict-258-open-addressing-probes` · **scope** — adjudicate PROPOSAL 245 → VERDICT 258 (append outbox block + bump status high-water) → append `## VERDICT 258` block to control/outbox.md + bump control/status.md high-water to P245/V258; files: control/outbox.md, control/status.md, control/claims/verdict-258-open-addressing-probes.md · 2026-07-21

Notes: control-plane-only diff (control fast lane, no session card); ruling APPROVE; verifier ideas/fleet/verify_245_open_addressing_probes.py (file sha256 ac4642df4a3b77fe35c418ffba9d2038589d9463cb1c40e1f341e0d371c5c5ab), results_sha256=98d7398935db83b93f4e5b71ef4393abf487d3bc4371018d0d9d16e4f75e1746 reproduced byte-for-byte across three routes (default run + --selfcheck in-process double-run + separate re-invocation); built ON TOP of the sim-lab reproduction mirror #343, no competing sim-lab PR. Lands via native merge-on-green.
