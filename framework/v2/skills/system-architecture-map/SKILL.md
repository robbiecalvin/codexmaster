---
name: system-architecture-map
description: Map and audit framework layers, execution routes, integration contracts and feedback loops. Use for architecture documentation, tracing and consistency reviews.
---
# System Architecture Map v1.0.0

## Procedure
1. Discover available framework documents, skill manifests, implementation and tests through authorized tools. Record source paths and revisions; distinguish documented, implemented and verified runtime behavior. Never infer enforcement from a diagram.
2. Map governance (Guardrails, instruction_priority, model_instructions, System Contract); input/context (Task Router, Context Resolver, State Manager); execution (Workflow Engine, Agent Workflow, task_template, change_planning); validation (Validation Agent, Metrics); recovery (Failure Handler, Debugging Playbook); optimization (Prompt Optimizer); engineering standards (Architecture, Code Style, anti_overengineering, repo_map, environment). Include Design Layer when relevant. Governance and standards apply throughout, not as sequential stages.
3. Read the authoritative routing matrix rather than redefining it. Trace task input → Routing → Context Resolution → route-specific Architect/Critic/Builder → Validation → Metrics → Final Output. Validation PASS and Metrics Accept are required for successful delivery. Failed, blocked or ineligible checks enter recovery or blocker reporting. Follow Failure Handler limits; retry earliest affected stage and invalidate downstream evidence; reroute on scope/risk change. Invoke Prompt Optimizer only for evidence-backed prompt failures.
4. Compare contracts, stage names, dependencies, permissions, state ownership and evidence requirements across sources. Identify contradictions, missing components, cycles and unsupported enforcement claims. Record severity, source evidence, impact and recommended correction.
5. Produce a map (Mermaid or text), trace or audit report with evidence and unknowns. Link authoritative records instead of duplicating them. Propose changes to owning guides; material workflow or governance changes require approval. Update documentation only within authorization.

## Modes
MAP, EXPLAIN, TRACE, AUDIT, VERIFY, UPDATE.

## Hybrid autonomy
Discover, inspect, map and report automatically. Do not execute workflows merely to diagram them. Approval required for permanent contract, routing, governance or architecture changes. Never bypass validation, fabricate runtime evidence or claim machine enforcement without verification.

## Integration
Read references/integration.md and applicable adapter; use templates/report.json.
