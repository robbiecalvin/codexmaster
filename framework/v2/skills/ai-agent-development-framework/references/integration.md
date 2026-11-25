# Integration
## Operating model
Closed loop: Route → Resolve → Execute → Validate → Measure → Improve/Recover when indicated. Load mandatory governance before routing; use Task Router matrix, Context Resolver before execution, Workflow Engine for stage sequencing. No parallel competing runner. Successful delivery requires applicable stages, Validation PASS and Metrics Accept; blocked reports are not successful delivery. Failure Handler classifies and recovers with shared retry budget; invalidate downstream evidence and reroute on scope/risk change. Prompt optimization requires evidence of prompt-related failure.

## Layers and ownership
- Governance: Operational Guardrails, Instruction Priority, Model Behavioral Instructions, System Contract; host authority always prevails.
- Input/context: Task Router, Context Resolver, State Manager.
- Execution: Workflow Engine, task template, Change Planner, Architect/Critic/Builder as routed; Developer Workflow owns human approval.
- Validation: Validation Agent and Metrics; Auditor reviews independently only when actually available.
- Recovery: Failure Handler, Debugging Playbook, Security Agent.
- Optimization: Prompt Optimizer and Resource Management & Efficiency.
- Engineering/design: Code Style, Anti-Overengineering, Environment Specification, Repository Orientation, Design System/Memory/Variation, Pull Request Rules.
- Modular Agents defines registration and handoffs; System Architecture Map documents relationships.

## Integration
Discover only relevant compatible specialized skills; mandatory governance must be explicitly loaded by host/project configuration. Roles may be local rather than independent agents; disclose actual reviewer and capabilities. Verify availability of required guides, tools, permissions and dependencies; missing critical requirements block successful delivery. Do not invent task templates or instruction priority policies. Preserve human approval before code edits and material architecture decisions. Reuse existing state and evidence only while applicable. Record route, context, approvals, stage outputs, validation, metrics, recovery and limitations in existing records. Maintain versioned contracts and propose changes for approval.

## Enforcement
This is a Markdown instruction framework, not an executable controlled environment. Distinguish instruction-defined, agent-reviewed, independently reviewed, machine-verified and machine-enforced controls; claim enforcement only with observed mechanism evidence. Reliability, clarity and correctness outrank speed or novelty. Modes: ORIENT, INTEGRATE, AUDIT, MAP, EVOLVE.
Use System Contract evidence rules, State Manager records and authorized host capabilities. No automatic installation or enforcement.
