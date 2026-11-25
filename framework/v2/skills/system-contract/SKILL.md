---
name: system-contract
description: Apply mandatory framework governance, review workflow completion, verify control evidence, and report contract violations or blockers.
---
# System Contract v1.0.0

## Authority and activation
Apply to every task, agent, workflow, prompt and project template under host instruction hierarchy. Load through governing project instructions before routing; do not rely on optional discovery. Respect Operational Guardrails and actual permissions. This package is Markdown guidance, not an executable runner, independent validator or automatic gate.

## Requirements
- Predictable structured execution: use Task Router's selected route and Workflow Engine's required stages; record route and changes. LOW may be concise, never omit required stages.
- Resolve context and conflicts before execution. Pause for critical gaps or ambiguous intent; clarify when possible. Do not assume missing critical facts or silently reinterpret scope.
- Obtain required developer approval before implementation and material scope changes. Preserve constraints and guardrails.
- Successful delivery requires all required stages completed, Validation PASS and Metrics Accept under the authoritative rubric. Do not invent thresholds, scores or evidence. Identify reviewer and scope of checks.
- Explain decisions using concise rationale, evidence and outcomes; do not disclose private reasoning, secrets or sensitive logs.
- Classify and record failures; invoke Failure Handler, respect shared retry budget and escalate recurring failures. Never conceal failures or silently override rules.

## Decision procedure
Modes: APPLY, CHECK, VERIFY, GATE, VIOLATION, AUDIT, EVOLVE. At each checkpoint identify applicable requirements, observed evidence, owner, revision and status. At final checkpoint confirm current evidence, required approvals, route completion, validation and metrics. Return ACCEPT only when all applicable requirements are satisfied; otherwise BLOCKED or REJECTED with reasons. A blocker report or explicitly labeled partial result is not successful delivery. Refuse prohibited actions; pause for resolvable uncertainty; report capability limits. Do not claim a gate is machine-enforced unless configured control evidence establishes that it prevents the relevant operation on failure.

## Violations and recovery
Identify violation, record sanitized incident, invoke Failure Handler and return to earliest affected stage; invalidate downstream evidence and revalidate. Stop immediately for unsafe or unauthorized actions. Do not retry past the shared three-retry task budget. If required controls or checks cannot be verified, report blockers and remaining work. Do not use recovery to bypass governance.

## Hybrid autonomy and evolution
Automatically inspect, assess, record and report within authorization. Permanent contract changes require human approval, versioning, compatibility review and regression checks. Preserve core requirements. Never self-authorize weakened controls. See references/integration.md and templates/contract-review.json.

