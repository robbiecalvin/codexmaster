# Legacy reference — task-router

For active v2 policy use [canonical task-router](../../framework/v2/skills/task-router/SKILL.md). The original text below is retained for historical comparison only; conflicting rules are superseded.

---

# Task Router System

## Purpose

The Task Router is responsible for analyzing incoming tasks and determining:

- Task type
- Complexity level
- Required agents
- Execution path

It ensures that the correct workflow is selected automatically, removing ambiguity and preventing misrouted execution.

---

## Core Principles

1. Every task must be classified before execution.
2. Routing decisions must be explicit and traceable.
3. Complexity determines workflow depth.
4. No task enters the Workflow Engine without routing.

## Task Classification

Each task must be categorized into one primary type:

### 1. Code

- Software development
- Debugging
- System implementation

### 2. Design

- UI/UX
- Architecture planning
- System structure

### 3. Analysis

- Evaluation
- Comparison
- Problem diagnosis

### 4. Content

- Writing
- Documentation
- Messaging

### 5. Strategy

- Planning
- Roadmaps
- Optimization direction

## Complexity Levels

Tasks are assigned a complexity level:

### LOW

- Simple request
- Clear instructions
- Minimal dependencies

### MEDIUM

- Multiple steps
- Some ambiguity
- Requires structured thinking

### HIGH

- Multi-stage workflows
- Multiple agents required
- High risk of failure if misaligned

## Routing Matrix

```plaintext
[ROUTING DECISION]

Type: Code
Complexity: HIGH

Agents:
- Architect
- Critic
- Builder
- Validator
- metrics

Workflow:
- Full pipeline required
```

## Agent Selection Rules

### LOW Complexity

- Builder
- Validator

### MEDIUM Complexity

- Architect
- Builder
- Validator

### HIGH Complexity

- Architect
- Critic
- Builder
- Validator
- metrics
- Optional: Optimizer

## Special Conditions

### Security Risk Detected

- Add: Security Agent
- Enforce stricter validation

### Ambiguity Detected

- Pause routing
- Request clarification, or
- Trigger Critic early

### Repeated Failure

Add:

- Optimizer
- Auditor

## Routing Workflow

### Step 1: Input Analysis

- Read task
- Identify keywords, intent, structure

### Step 2: Classification

- Assign Type
- Assign Complexity

### Step 3: Agent Selection

- Select required agents based on matrix

### Step 4: Workflow Assignment

- Determine execution pipeline

### Step 5: Output Routing Decision

```plaintext
[TASK ROUTE]

Type:
Complexity:
Agents:
Workflow:
Notes:
```

## Failure Modes

- Misclassification -> incorrect execution
- Underestimating complexity -> missing steps
- Overestimating complexity -> inefficiency

## Correction Rules

If routing fails:

- Reclassify task
- Adjust complexity level
- Re-run workflow

## Anti-Patterns

- Skipping classification
- Guessing complexity
- Defaulting everything to HIGH
- Running full pipeline unnecessarily

## Integration Points

Works with:

- [Workflow Engine](./docs/workflow/workflow_engine.md)
- [State Manager](./docs/workflow/state_manager.md)
- [Validation Agent](./docs/workflow/validation_agent.md)

Feeds into:

- Agent execution sequence

## Versioning

Routing rules must evolve based on:

- Failure patterns
- Task diversity
- System scaling

## Final Rule

If the task is not correctly routed, the system will fail before it begins.
