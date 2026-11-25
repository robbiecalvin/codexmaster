---
name: task-router
description: Classify incoming tasks, assess complexity and risk, dynamically discover relevant available skills, resolve context and assign traceable execution stages. Use for routing, reclassification, decomposition, escalation and routing audits.
---
# Task Router v1.0.1

Route every task entering the custom workflow before execution. In ChatGPT and Codex, apply this when invoked or configured by the host; do not claim global interception.

## Procedure
1. Identify intent and one primary type: Code, Design, Analysis, Content, Strategy. Record optional secondary types.
2. Assign LOW for clear low-risk work with minimal dependencies; MEDIUM for multiple steps or meaningful ambiguity; HIGH for multi-stage, high-risk or critical-review work. Security risk forces HIGH. Explain the choice without invented confidence scores.
3. Discover skills using the host's available skill catalog. Read relevant skill instructions before selection. Follow references/discovery.md and the applicable adapter. Never invent availability.
4. Assign the ordered stages below. Resolve context before building; ask only when missing information prevents safe progress. Record dependencies, approval requirements and blockers. Reassess complexity when new facts emerge.
5. Emit the route using templates/task-route.yaml. Hand it to the Workflow Engine if available; otherwise perform authorized responsibilities locally. Routing is not execution authorization.

| Complexity | Ordered stages |
|---|---|
| LOW | Routing → Context Resolution → Builder → Validation → Metrics → Final Output |
| MEDIUM | Routing → Context Resolution → Architect → Builder → Validation → Metrics → Final Output |
| HIGH | Routing → Context Resolution → Architect → Critic → Builder → Validation → Metrics → Final Output |

Roles are responsibilities, not a requirement to spawn agents. Security risks require security review in Critic and stricter validation. Repeated failures follow the Failure Handler; if unavailable, block automated retries and report the blocker.

## Modes
ROUTE: classify and assign. RECLASSIFY: correct a route. DECOMPOSE: route dependent subtasks without losing parent constraints. ESCALATE: increase depth when warranted. AUDIT: inspect routing evidence. OPTIMIZE: propose rule improvements using verified results and Prompt Optimizer when available.

## Hybrid autonomy
Automatically classify, discover, select, decompose, and reroute within authorized scope. Permanent routing-rule changes and architecture changes require approval. Never bypass security, validation, permissions or higher-priority instructions. Do not install skills or delegate without authorization. Preserve prior decisions and rationale on reroute.

## Integration
See references/integration.md. Record observed failures and metrics; a score below 10 triggers investigation, not automatic prompt replacement. Do not invent metrics or claim tests were run when they were not. Use the existing state owner rather than creating competing state.
