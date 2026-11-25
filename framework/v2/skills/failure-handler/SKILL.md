---
name: failure-handler
description: Classify failures, coordinate bounded recovery and escalate unresolved issues.
---
# Failure Handler v1.0.0

## Classification and recovery
Record task ID, stage, type, severity LOW/MEDIUM/HIGH, observed evidence, cause (unknown if unproven), impact and recovery strategy. Types and actions:
- Validation: correct defect at earliest affected stage (Builder for minor implementation issues).
- Metrics: refine eligible output or address ineligibility; optimize prompts only with causal evidence.
- Context: re-run Context Resolver and reconcile state.
- Routing: re-run Task Router and restart affected workflow.
- Execution: invoke Debugging Playbook for defects; correct proven cause.
- Systemic: escalate to Auditor or human review.
- Design: resolve generic layout, repetition or weak identity; record evidence-backed anti-pattern in Design Memory.
- Security: stop unsafe execution; escalate without automatic retry.
- Environment: verify runtime/dependencies; obtain authorization for changes.
## Retry contract
Maximum three retries per task after initial attempt. Persist a single task-level counter via State Manager; reserve a retry before corrective execution. Nested loops, design regeneration, rerouting and session resumption share the budget. Do not reset on stage changes. If exhausted, classify systemic and stop automated recovery; report remaining work and escalate. If counter cannot be verified, pause rather than assume zero. Missing authorization, unsafe operations and unrecoverable blockers stop immediately.
## Workflow
Detect, classify, choose strategy, apply authorized correction, return to earliest affected stage, invalidate downstream evidence, repeat required stages, validate and evaluate Metrics. Scope/risk changes return to Routing. No silent retries. Record UTC timestamp, task, type, resolution, outcome, attempt and evidence; sanitize logs. Feed durable lessons to change planning, Metrics, relevant guides and Prompt Optimizer only for prompt-related evidence. Do not invent Auditor availability; report missing capability.
## Modes
CLASSIFY, RECOVER, ESCALATE, LOG, AUDIT.

## Hybrid autonomy
Read, diagnose, classify and report automatically within authorization. Changes require applicable developer approval; never bypass governing rules.

