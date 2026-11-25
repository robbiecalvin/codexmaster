---
name: debugging-playbook
description: Diagnose reproducible bugs using evidence and minimal authorized fixes.
---
# Debugging Playbook v1.0.0

## Required sequence
1. Obtain Failure Handler classification and task retry budget.
2. Reproduce the failure deterministically before editing; capture sanitized command, inputs, revision, environment and observed result. If impossible, stop and report uncertainty.
3. Examine errors, stack traces, assertions, return values and state transitions.
4. Isolate the failing component; inspect repository and relevant tests.
5. Trace execution and dependencies; distinguish observations from hypotheses.
6. Establish root cause with evidence; test competing hypotheses without speculative production edits. If uncertain, stop and report symptoms, possible causes and missing evidence.
7. Propose the smallest fix, obtain developer approval for the change plan, then implement within scope. Avoid unrelated refactoring; preserve public interfaces.
8. Run original failing tests, related tests and relevant edge cases; add a minimal regression test if absent. Record actual results and unavailable checks. Do not claim absence of all regressions from limited tests.
9. Submit to Validation Agent and then Metrics; do not declare completion without PASS and Accept.
## Modes
REPRODUCE, DIAGNOSE, TRACE, PLAN-FIX, FIX, REGRESSION, AUDIT. Partial modes do not waive prerequisites for a fix.
## Feedback
Checkpoint material evidence through State Manager. Feed verified lessons into change_planning.md and Metrics; invoke Prompt Optimizer only when prompt quality contributed. Repeated failures go to Failure Handler. Never suppress errors merely to hide symptoms. Redact secrets and avoid destructive reproduction; use isolated fixtures where possible.

## Hybrid autonomy
Read, diagnose, classify and report automatically within authorization. Changes require applicable developer approval; never bypass governing rules.

