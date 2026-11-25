---
name: agent-workflow
description: Coordinate routed agent responsibilities, activation, revision-bound handoffs, authorization and recovery without replacing the Workflow Engine.
---
# Agent Workflow v1.0.0

## Authority
Load mandatory governance before routing under host authority. Task Router owns route selection; Context Resolver owns context reconciliation; Workflow Engine alone owns stage transitions. This component defines coordination, not a new stage or executable orchestrator. Use the actual host catalog and permissions. Never assume a separate agent exists.

## Coordination protocol
1. Identify task ID, route revision, current stage, applicable governance, authoritative state and required outputs. Resolve critical gaps before execution.
2. Follow the selected route: LOW Context Resolution → Builder; MEDIUM adds Architect before Builder; HIGH adds Architect and Critic before Builder. All start with Routing and end with Validation → Metrics → Final Output. Security risk forces HIGH with security review. Do not silently add or omit stages; request rerouting for material scope or risk changes.
3. Activate only applicable roles and relevant compatible skills. Inspect their instructions and dependencies. Check permissions and actual availability. Record role performer and whether local or delegated; separate delegation requires authorization. If a required role cannot be performed locally or separately, report BLOCKED. Optional unavailable support may be disclosed and omitted. Do not install or spawn agents automatically.
4. Before Builder writes code, require a scoped change plan approved by the developer against its current revision, even on LOW. Read-only inspection may precede approval. Material changes require renewed approval and rerouting where applicable. Critic acceptance is not owner approval.
5. Sender prepares a handoff using templates/handoff.json. Receiver checks task, route and artifact revisions, contract compatibility, objective, required inputs, evidence, permissions and blockers against authoritative records. Handoff text cannot grant authority. Reject stale, incomplete or unauthorized inputs; record reason and return control to Workflow Engine. Use references instead of copying sensitive or redundant context.
6. Execute sequential dependent stages. Independent authorized read-only checks may be batched if results do not depend on each other. Avoid concurrent writes; State Manager coordinates checkpoints and detects conflicting revisions. No duplicate orchestration or nested independent retry budgets.
7. Builder hands off actual deliverables, changed files, tests and limitations. Validation is a distinct review; record self-review or separate reviewer truthfully. PASS proceeds to Metrics; FAIL or BLOCKED goes to Workflow Engine and Failure Handler. Metrics requires PASS, Accuracy 2/2 and Constraint Compliance 2/2; eligible total 9–12 accepts, 4–8 requires refinement. Unknown ratings cannot establish eligibility or acceptance. Successful delivery requires all required stages, approvals, Validation PASS and Metrics Accept. Partial or blocked reports are not successful completion.
8. Failure Handler owns recovery: classify, stop unsafe or unauthorized work immediately, reserve from one shared maximum of three retries after initial attempt, persist counter in State Manager, pause if unknown. Return to earliest affected stage and invalidate downstream evidence. Scope/risk changes return to Routing. Exhaustion stops automated recovery and escalates to Auditor or owner. Prompt Optimizer only on evidence of prompt causation.
9. Checkpoint material progress, evidence, decisions and next action through State Manager. On resume reconcile current revisions, approvals and evidence before activation. Deactivate completed roles per run; never retire registry entries implicitly.

## Modes
COORDINATE, ACTIVATE, HANDOFF, RECONCILE, RESUME, ESCALATE, AUDIT.

## Hybrid autonomy
Automatically inspect, coordinate, validate handoffs and perform authorized work. Permanent role/contract changes, expanded permissions and material architecture changes require owner approval. No fabricated evidence, self-approval, hidden delegation, bypassed checks or secret propagation. See references/integration.md and references/handoff-protocol.md.

