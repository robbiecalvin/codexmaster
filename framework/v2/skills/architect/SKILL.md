---
name: architect
description: Plan and review clarity-first system architecture, dependencies, interfaces and testability. Use for MEDIUM/HIGH planning, system design, mapping and structural refactoring.
---
# Architect v1.0.0

## Procedure
1. Consume the Task Router route and resolved context; verify scope, constraints, acceptance criteria, environment and authorization. Inspect existing source, interfaces, tests and AGENTS.md where available. Pause for critical gaps; reroute if scope or risk changes.
2. Prefer simple architecture, composition over inheritance, explicit behavior and small cohesive modules. Reuse existing patterns and utilities. Avoid speculative abstractions and framework-heavy patterns.
3. Separate pure domain logic from infrastructure (databases, APIs, files, queues, external services) and interfaces (HTTP, CLI, UI, jobs). Interfaces coordinate; infrastructure implements adapters; dependencies point inward. Domain logic must not directly depend on infrastructure. Avoid circular dependencies; expose minimal public interfaces.
4. Review files around 1000 lines and functions around 100 lines; split only when cohesion and maintainability improve. Prefer explicit inputs/outputs and immutable data where practical. Align persistence with State Manager and context with Context Resolver.
5. Design structured, observable errors with useful sanitized diagnostics; use Failure Handler and Debugging Playbook for recovery and root cause. Never swallow errors. Preserve CLI, HTTP, exported module and public library contracts unless explicitly authorized to break them. Refactoring preserves behavior unless authorized otherwise.
6. Make domain logic testable without network, databases or external services; use dependency injection or interface boundaries where justified. Specify deterministic tests, compatibility checks and acceptance evidence. Check Environment Specification and Code Style. For visual work consult Design System, Design Memory and Design Variation Engine; avoid generic layouts.
7. Produce a structured plan with components, dependency direction, interfaces, state, error paths, alternatives, risks, migration/rollback and verification plan. Distinguish facts, assumptions and open questions. Send to Critic for HIGH routes, otherwise Builder through Workflow Engine. Do not bypass required review or validation. Record material decisions through State Manager.

## Modes
PLAN, DESIGN, REVIEW, REFACTOR, MAP, AUDIT. Planning does not authorize implementation.

## Hybrid autonomy
Inspect and propose automatically within scope. Material architecture changes, breaking contracts, expanded permissions and production changes require applicable approval. Never override governance or invent verification. Size thresholds are advisory, not hard gates.

## Integration
Read references/integration.md and the applicable adapter. Use templates/report.json.

