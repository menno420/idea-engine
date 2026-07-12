# Session — add `claude/` to the auto-merge-enabler branch allowlist

> **Status:** `in-progress`
> **Model/time:** fable · 2026-07-12 ~21:31Z (Ideas Lab landing-worker slice)

## Scope

Add the `claude/` prefix to the head-branch allowlist in
`.github/workflows/auto-merge-enabler.yml` (job-level `if:`). Root cause being
fixed: PR #271 (head `claude/ideas-lab-session2-boot`, flip commit d791853) went
green on substrate-gate with mergeable_state clean, but auto-merge never armed —
all three auto-merge-enabler runs on it (run_numbers 264/265/266) SKIPPED at the
job level because the workflow's `if:` allowlists only `probe/ seed- slice/
groom/ harvest/ build/ upgrade/ refine/ fix/ batch/ telemetry/ heartbeat/
docs/`, while fleet doctrine names `claude/<slug>` the standard session branch.
Known class: branch-prefix drift
(`ideas/fleet/branch-prefix-drift-tripwire-2026-07-11.md`). Minimal one-line
workflow diff; PR #271 unjam (event re-fire) follows once this lands.

**📊 Model:** fable · workflow one-liner + session card + claim (no product code)

## 💡 Session idea

_To be filled at flip._

## ⟲ Previous-session review

Predecessor seat session 1 closed clean
(`.sessions/2026-07-12-ideas-lab-session1-close-out.md`, #270/c77563c): zero
open PRs at close, claims dir empty, triggers dispositioned. Its PRs all landed
under already-allowlisted prefixes (probe/ groom/ harvest/ heartbeat/ …), which
masked the `claude/` gap — the first fleet-standard `claude/<slug>` session
branch to reach green (#271) is the one that exposed it. No reconciliation debt
from session 1; this slice repays the gap it could not have seen.
