---
name: engineering-task-template
description: Structure routed engineering tasks, plans, safety checks, design scope and verification records.
---
# Engineering Task Template v1.0.0

Modes: DEFINE, STRUCTURE, REVIEW, UPDATE, VERIFY, CLOSE.
After Task Router and Context Resolver, record task type, complexity, route, objective, expected outcome, acceptance criteria, constraints, affected modules/files/services/utilities/tests/configuration, current behavior with evidence, and confirmed root cause for bugs. Unknown root cause blocks corrective edits; use Failure Handler and Debugging Playbook. Use Change Planner for minimal file/function changes, utilities and tests. Record public API, CLI, configuration and backward compatibility impacts; require explicit authorization for interface changes. Obtain developer approval before code edits, even LOW route (concise plan). Follow architecture, code style, guardrails and minimal diff. Record actual implementation and modified files, key logic and new tests.
Testing: run all tests as required by the supplied template; do not silently narrow this requirement under resource efficiency or verification locks. If scope of all tests is ambiguous, resolve with project instructions/owner before completion; unavailable required checks block. Test expected behavior, edge cases and failures; verify original issue and regression evidence. Execute checks before Validation and Metrics despite the template section numbering. Workflow Engine owns order; validation PASS and Metrics Accept required for successful delivery. Record failures and recovery, never fabricate results.
User-facing design: for new interfaces or intentional redesign, define layout, tone, typography, interaction, density and use Design System/Variation Engine/Memory. For targeted UI changes preserve baseline and document relevant decisions. Mixed tasks apply only to affected UI; backend/infrastructure/internal changes without UI impact skip design section. Record design validation accordingly.

## Authority
Follow host controls, System Contract, Guardrails and applicable instruction priority. Automatic analysis and authorized documentation/checks; approval for implementation plans, permanent rules and scope expansion. Never bypass required checks. Read references/integration.md and templates/report.json as needed. Instructional skill, not executable enforcement.
