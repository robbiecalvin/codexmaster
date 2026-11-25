---
name: workflow-engine
description: Orchestrate routed tasks, enforce stage order, validation and metrics gates, recover failures and resume verified checkpoints. Use for execution, recovery, rerouting and workflow audits.
---
# Workflow Engine v1.0.1

## Execution contract
Consume task-router/templates/task-route.yaml; do not redefine routing policy. Verify task ID, route revision, authorization and ordered stages. Routing is mandatory in the custom framework. Resolve context before Architect, Critic or Builder; reroute if scope or risk changes. Pause for critical missing or conflicting context.

## Stage responsibilities
- Routing: record selected route and rationale.
- Context Resolution: load authoritative state, objective, constraints and dependencies.
- Architect (when required): produce structured plan, components and dependencies.
- Critic (when required): review plan, assumptions, risks and security; resolve blocking issues before Builder.
- Builder: produce requested implementation within authorized scope.
- Validation: verify correctness, completeness and constraints; record PASS, FAIL or BLOCKED with evidence.
- Metrics: only after validation PASS, apply the authoritative Metrics eligibility and acceptance rubric. Record Accept, Refine or Ineligible and evidence; do not invent scores or thresholds.
- Final Output: deliver successful result only after all required preceding stages complete and Metrics Accept. Otherwise report partial work, blockers and remaining checks explicitly.

## Execution and recovery
Modes: EXECUTE, RESUME, RECOVER, REROUTE, INSPECT, AUDIT. Stage states: pending, running, passed, failed, blocked, skipped (not required only), invalidated. Execute sequentially; each stage consumes valid upstream outputs. Record stage outputs and evidence in the checkpoint at material milestones. Discover skills through Task Router; roles may be performed locally when delegation is unavailable or unauthorized. On failure use Failure Handler and its retry limits. If Failure Handler is unavailable, block automated retries and report missing policy; stop unsafe or unauthorized work immediately. Return to earliest affected stage, invalidate downstream evidence and repeat required stages. Scope or risk change returns to Routing. Invoke Prompt Optimizer only for evidence-backed prompt failures; a low score alone is not proof. Resume via State Manager; recheck changed inputs. Never loop indefinitely or treat blocked checks as passed.

## Hybrid autonomy
Execute, record, reroute and recover within authorization. Permanent workflow changes, significant production changes and expanded permissions require approval. Never bypass guardrails, instruction priority, required checks or permissions. No fabricated evidence. See references/integration.md and templates/workflow-run.yaml.

