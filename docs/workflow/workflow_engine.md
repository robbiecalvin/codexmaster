# Legacy reference — workflow-engine

For active v2 policy use [canonical workflow-engine](../../framework/v2/skills/workflow-engine/SKILL.md). The original text below is retained for historical comparison only; conflicting rules are superseded.

---

# Workflow Engine System

## Purpose

The Workflow Engine defines the exact execution order, lifecycle, and orchestration of all agents and processes within the framework.

It ensures that tasks are executed consistently, completely, and without skipping critical stages.

---

## Core Principles

1. No task skips defined stages.
2. Execution order is enforced, not optional.
3. Each stage must complete before the next begins.
4. Outputs must flow cleanly between stages.
5. The system prioritizes correctness over speed.

Agents do not execute independently.

All agent execution must occur within:
- [Workflow Engine](./docs/workflow/workflow_engine.md)

Agents must not bypass defined execution stages.

## Standard Execution Pipeline

Every task follows this sequence:

```plaintext
1. Context Load (state_manager + context_resolver)
2. Task Routing (task_router)
3. Architecture (Architect Agent)
4. Critical Review (Critic Agent)
5. Implementation (Builder Agent)
6. Validation (Validation Agent)
7. metrics Evaluation (metrics System)
8. Optimization (Prompt Optimizer if needed)
9. Final Output
```

---

## Stage Definitions

### 1. Context Load

- Load project state
- Resolve active context
- Confirm current objective

Failure Condition:

- Missing or conflicting context -> pause execution

### 2. Task Routing

- Classify task type (code, design, analysis, etc.)
- Determine required agents
- Set execution complexity level

### 3. Architect Stage

- Define system structure
- Break task into components
- Identify dependencies

Output:

- Structured plan

### 4. Critic Stage

- Analyze architecture
- Identify risks, flaws, inefficiencies
- Challenge assumptions

Output:

- Issues + recommendations

### 5. Builder Stage

- Implement based on approved structure
- Follow all constraints
- Produce complete output

Output:

- Full implementation

### 6. Validation Stage

- Verify correctness
- Check completeness
- Confirm constraint compliance

Decision:

- PASS` -> proceed
- FAIL` -> return to Builder with corrections

### 7. metrics Evaluation

- Score output across defined metrics
- Identify weak areas

Decision:

- Score `< 9` -> refinement required
- Score `>= 9` -> acceptable

### 8. Optimization Stage

Triggered only if needed.

- Improve prompt structure
- Refine clarity and constraints
- Re-run workflow if necessary

### 9. Final Output

- Deliver validated, scored, optimized result

## Execution Rules

- No stage may be skipped
- No stage may override another silently
- All outputs must be explicit and structured
- Each stage must respect constraints and guardrails

## Loop Handling

If failure occurs:

```plaintext
Validation FAIL -> Builder
metrics LOW -> Optimizer -> Re-run
Context unclear -> Pause + Resolve
```

Loop must terminate when:

- Validation passes
- metrics reach acceptable threshold

## Fast Path (Controlled Shortcut)

Allowed only when:

- Task is simple
- No ambiguity exists
- No constraints risk

Pipeline:

```plaintext
Context -> Builder -> Validation -> Output
```

## Anti-Patterns

- Skipping Critic stage for speed
- Delivering unvalidated outputs
- Ignoring metrics results
- Running agents out of order
- Allowing silent failures

## Integration Points

Works with:

- [State Manager](./docs/workflow/state_manager.md)
- [Task Router](./docs/workflow/task_router.md)
- [Validation Agent](./docs/workflow/validation_agent.md)
- [Metrics] (./docs/strategy/metrics.md)
- [Prompt Optimizer] (./docs/strategy/prompt_optimizer.md)

Aligns with:

- Guardrails
- instruction_priority

## Versioning

Workflow must evolve based on:

- Failure patterns
- System complexity
- New agent integrations

## Final Rule

If the workflow is not enforced, the system is not reliable.
