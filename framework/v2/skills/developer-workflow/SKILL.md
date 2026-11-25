---
name: developer-workflow
description: Coordinate human-approved development tasks, change planning, implementation, debugging and pull request preparation.
---
# Developer Workflow v1.0.0

## Procedure
1. DEFINE: capture objective, affected modules (provisional until inspected), constraints and acceptance criteria using task_template.md or the supplied template.
2. PREPARE: discover and read applicable AGENTS.md (including nested scope), model_instructions.md, instruction_priority.md and Guardrails. Respect host instruction hierarchy; report missing required documents, never invent them. Resolve context before implementation.
3. Load architecture.md, repo_map.md and environment.md or authoritative equivalents. Invoke Repository Orientation and Environment Specification when available. Inspect relevant tests and existing changes.
4. PLAN: use change_planning.md or template to identify affected components, steps, risks, dependencies, verification and rollback. Every code modification, including LOW routes, requires developer approval of the scoped plan. A LOW plan is not a separate Architect stage. Read-only investigation may precede approval. Record approval against plan revision; silence is not approval. Material scope or risk changes require rerouting and renewed approval.
5. IMPLEMENT: only within approved scope; follow Code Style and anti_overengineering.md. Preserve unrelated changes. Use Workflow Engine stage order; never bypass required Critic or validation.
6. DEBUG: invoke Debugging Playbook and Failure Handler; isolate root cause, test assumptions, make incremental corrections. Revalidate affected work; pause for changed scope or exhausted recovery.
7. PR-PREPARE: follow pr_rules.md; prepare summary, rationale, affected files, tests actually run, limitations and review notes. Commit, push, open PR or merge only with applicable authorization. Human retains final architectural judgment and review.
8. AUDIT: compare evidence against plan, approvals and required stages. Successful delivery requires Validation PASS and Metrics Accept; otherwise report blockers and remaining work.

## Authority
Automatically investigate, draft plans, prepare review material and execute approved work. Never self-approve, expand scope, change governance, fabricate evidence or bypass safety. Missing approval blocks code writes. Record material milestones through State Manager. Human review remains distinct from automated validation.

See references/integration.md, templates/report.json and applicable adapter.

