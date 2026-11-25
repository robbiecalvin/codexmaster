---
name: pull-request-rules
description: Prepare focused commits and reviewable pull requests with truthful CI and safety evidence.
---
# Pull Request Rules v1.0.0

## Procedure
Inspect repository instructions, branch, status, diff, existing PR conventions and authorized scope. Preserve unrelated changes; do not stage indiscriminately. One logical change per PR: bug fix, feature, scoped refactor or tests. Split large changes when practical without breaking dependencies. Keep diffs small; avoid unrelated formatting. Commits atomic, logically grouped and descriptive: `<type>: <short description>` (fix, feat, refactor, test). Prepare commits only within authorization; do not push, publish, merge, force push or rewrite history without applicable permission.

## Review package
Describe what changed, why necessary and how implemented. Bug fixes include evidenced root cause, correction and regression tests; extend existing tests when possible. Refactors preserve behavior and explain motivation. Logic changes cover expected behavior and relevant edge cases. Explicitly disclose public API, database schema, authentication and authorization impacts; identify compatibility, migration and rollback implications when relevant. Do not make unauthorized interface changes.

## Verification
Run applicable required tests, builds, compilation and lint; inspect actual results and CI status if available. Distinguish local checks from remote CI and configured merge gates. Report unavailable checks, failures, skipped checks and reasons; never claim CI passed without evidence. Do not label blocked work ready to merge. Follow Validation Agent, Metrics, System Contract and Developer Workflow approval requirements. Prepare review summary even when blocked, clearly labeled. Use existing PR templates where compatible.

Modes: INSPECT, PREPARE, REVIEW, VERIFY, AUDIT. Human review and merge authorization remain separate.
