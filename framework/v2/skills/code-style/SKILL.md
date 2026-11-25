---
name: code-style
description: Discover and apply repository coding conventions; review, refactor and validate readable, consistent code. Use when writing, modifying or reviewing software.
---
# Code Style v1.0.0

## Procedure
1. Discover applicable repository instructions, nearby code, formatter/linter configuration, language version, tests and reusable utilities. Respect host and project guardrails; repository conventions take precedence over defaults. If unavailable, disclose and use defaults below.
2. Prefer descriptive names, clear single-purpose functions, explicit inputs/outputs, minimal hidden side effects, early returns and simple control flow. Handle errors explicitly with useful diagnostics; never silently swallow failures.
3. Reuse existing utilities, avoid duplicate implementations, use named constants/configuration for meaningful values, import only what is needed and follow existing import grouping. Comments explain why, not what. Logs should be concise and never expose secrets, credentials or sensitive user data.
4. Apply scoped changes only; preserve behavior during style-only refactors. Avoid unrelated churn, clever compact code and new dependencies without authorization.
5. Validate using available repository formatter, lint, type checks and deterministic behavior tests as applicable. Tests should have descriptive scenario names and focus on behavior. Record actual commands, scope and results; distinguish style findings from functional defects and unavailable checks. Never claim an unrun check passed.

## Language defaults (only absent repository conventions)
- Python: PEP 8, snake_case functions/variables, PascalCase classes, four spaces, approximately 100-character maximum lines, useful type annotations. Use Decimal for monetary arithmetic where appropriate.
- JavaScript: const by default, let for reassignment, short arrow functions where clear, async/await over nested promise chains, descriptive camelCase names.
- PHP: modern PHP, strict types where compatible, typed parameters/returns and PSR-style formatting. Avoid floating-point monetary arithmetic when exact values are required.
- TypeScript: meaningful types, existing strictness settings, avoid unnecessary any; follow JavaScript conventions where applicable.
- Other languages: discover local conventions; do not impose unrelated language rules.

## Modes
DISCOVER, APPLY, REVIEW, REFACTOR, VALIDATE, AUDIT.

## Hybrid autonomy
Automatically discover and apply standards, run authorized checks and make verified scoped style corrections. Approval required for permanent standards changes, broad refactors, behavior changes outside task scope or expanded permissions. Do not install dependencies without applicable authorization or bypass required checks.

## Integration
Read references/integration.md and the applicable adapter. Use templates/report.json for structured output.

