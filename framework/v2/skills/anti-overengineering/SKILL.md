---
name: anti-overengineering
description: Prevent speculative complexity and review abstractions, dependencies and minimal solutions.
---
# Anti Overengineering v1.0.0

## Procedure
Modes: REVIEW, SIMPLIFY, JUSTIFY, COMPARE, AUDIT. Inspect requirements, repository patterns and existing utilities. Compare the smallest sufficient implementation against proposed alternatives. Prefer local logic, simple helpers, composition, flat structures and standard library features. Reject wrappers around simple functions, single-use generic frameworks, fixed-behavior configuration systems, deep inheritance and speculative future requirements unless a concrete current requirement justifies them. Extract shared logic when multiple real uses exist and duplication is difficult to maintain or complexity decreases. Ask whether the abstraction makes maintenance easier; record evidence and tradeoffs. Do not remove security boundaries, necessary domain separation or tests in the name of simplicity. Dependencies must meet the stricter Operational Guardrails correctness/security rule and applicable approval. Refactoring preserves behavior and requires approved change plan; no unrelated edits. Return ACCEPT, REVISE or BLOCKED with concrete findings and minimal alternative.

See references/integration.md and templates/report.json. These are instructional controls, not machine enforcement.
