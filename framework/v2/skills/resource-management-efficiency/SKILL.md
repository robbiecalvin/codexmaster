---
name: resource-management-efficiency
description: Allocate engineering effort proportionately, reuse verified work, manage verification locks, prevent duplicate work, and preserve resumable checkpoints without bypassing required controls.
---
# Resource Management & Efficiency v1.0.0

Apply throughout authorized engineering work. Read references/resource-policy.md for the complete source policy. Host controls, System Contract, Guardrails, required route stages, developer approval and mandatory checks take precedence. No assumed quotas or reset times.

## Procedure
1. TRIAGE: read applicable instructions and existing status, decisions and evidence. Identify completion state, objective, acceptance criteria and impact. Use Task Router complexity; LOW uses concise planning, not skipped required approvals or stages.
2. REUSE: inspect only relevant files and existing implementations; reuse current evidence and decisions. Revisit only for changed requirements, inputs, risks or credible failures.
3. IMPACT: identify changed behavior, dependencies, interfaces and affected locks. Choose focused tests first, relevant integration checks next, broader checks at milestones or when required. Required release/security checks always run.
4. BATCH: group compatible changes and independent tool calls; respect prerequisites. Delegate only when authorized and useful. Avoid redundant research, setup, agents, logs and retries. Justify expensive operations by risk, requirements or expected benefit.
5. LOCK: record sufficiently verified behavior with acceptance criteria, evidence, revision/environment, dependency boundaries and reopen triggers in existing State Manager records. A lock is evidence reuse, not a guarantee or write restriction. Do not claim a test was rerun when reused.
6. REOPEN: invalidate affected locks on relevant code/config/data/dependency/interface changes, changed criteria, credible defects or stale/unknown evidence. Preserve unrelated locks. Revalidate affected behavior and record actual results.
7. CHECKPOINT: when interrupted or constrained, stop optional work, complete a safe meaningful unit, prioritize essential checks and record resumable state. Never evade limits or reset shared retry counts. Use authoritative product indicators only.
8. COMPLETE: park unrelated issues in existing backlog; expand scope only with applicable authorization or stop for immediate risk. Stop polishing when criteria, required validation and metrics are satisfied. Report completed, changed, verified, not tested, remaining. Blocked work is not successful delivery.
9. AUDIT: identify duplicated effort, stale locks and missing checks; propose evidence-based improvements without changing permanent policy independently.

## Authority
Automatic: targeted inspection, evidence reuse, impact analysis, lock bookkeeping, proportionate checks and authorized execution. Approval required: material scope/architecture changes, permanent policy changes, code implementation plans under Developer Workflow, new permissions. Never skip mandatory checks, fabricate evidence, evade restrictions or self-approve. State Manager owns persistence; Failure Handler owns retries; Validation Agent and Metrics own their respective completion decisions. See references/integration.md.
