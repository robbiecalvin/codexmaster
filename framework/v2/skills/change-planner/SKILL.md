---
name: change-planner
description: Create revision-aware minimal change plans, dependency maps, impact assessments and verification plans before code edits.
---
# Change Planner v1.0.0

## Procedure
Modes: PLAN, MAP, IMPACT, REVIEW, REVISE, VERIFY, AUDIT. Follow System Contract, Workflow Engine, Guardrails and Architecture. Resolve objective, constraints and acceptance criteria; inspect relevant files, imports, callers, interfaces, utilities and tests through Repository Orientation. Identify all potentially affected files and distinguish confirmed from inferred impact. Produce minimal file-level change map, ordered steps, risks, rollback where applicable and verification plan. Preserve public interfaces unless explicitly authorized; if authorized, update all dependent paths consistently. Large rewrites require explicit request. For bug work classify via Failure Handler and establish reproduced root cause through Debugging Playbook before corrective edits. For performance/refinement work identify actual Metrics baseline, target and measurement method; report missing baseline rather than invent it. For user-facing work assess presentation and interaction against existing interface baseline and applicable design requirements. New features use acceptance criteria rather than invented failure history. Obtain developer approval for every code modification, including LOW routes; approval binds plan revision and scope. Material changes invalidate approval and affected downstream evidence; reroute when needed. Hand approved plan to Builder only after required Architect/Critic stages. After edits verify imports, interfaces, targeted and related tests, regression coverage, Validation PASS and Metrics Accept. Record unavailable checks and blockers. No implementation or self-approval by Change Planner.

See references/integration.md and templates/report.json. These are instructional controls, not machine enforcement.
