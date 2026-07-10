# claims/ — one file per claim

Before working a section (or any shared surface), create `claims/<branch>.md` — one
bullet: `branch · section/scope · expected files · date` — and delete it at session
close. Flatten `/` in branch names to `-` for the claim filename (the PR #1 card's
guard recipe, consumed by every claim since). One file per claim, never a shared list (the superbot Q-0195 measured result:
per-file claims ≈ 0% merge-conflict rate vs ~98% for a shared append ledger). Parallel
workers claim **disjoint sections**; a claimed section is off-limits until the claim
clears.

Pre-resolved at seed (blueprint §1): kit adoption, `.substrate/`, `control/`, and the
section tree were seeded in one pass by the dispatch copilot (2026-07-10) — no claim
races on shared ground remain from birth.
