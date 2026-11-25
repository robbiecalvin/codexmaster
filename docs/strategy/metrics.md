# Legacy reference — metrics

For active v2 policy use [canonical metrics](../../framework/v2/skills/metrics/SKILL.md). The original text below is retained for historical comparison only; conflicting rules are superseded.

---

# metrics & Performance Evaluation System

## Purpose

This document defines how system performance is measured, tracked, and improved over time.

The goal is to replace subjective judgment with objective evaluation across all outputs and workflows.

---

## Core Principles

1. What is not measured cannot be improved.
2. metrics must reflect real-world usefulness, not theoretical quality.
3. Measurement must be consistent across all tasks.
4. metrics drive refinement, not vanity.

## Metric Categories

### 1. Accuracy

Measures correctness of output.

- Was the solution correct?
- Were there logical errors?
- Did validation pass cleanly?

Score:

- 0` = Incorrect
- 1` = Partially correct
- 2` = Fully correct

### 2. Completeness

Measures whether all requirements were fulfilled.

- Were all requested components delivered?
- Were edge cases addressed?
- Were instructions fully followed?

Score:

- 0` = Major gaps
- 1` = Minor gaps
- 2` = Complete

### 3. Clarity

Measures readability and usability.

- Is the output understandable?
- Is structure clean and logical?
- Is it immediately usable?

Score:

- 0` = Confusing
- 1` = Acceptable
- 2` = Clear and structured

### 4. Efficiency

Measures unnecessary complexity.

- Is the solution over-engineered?
- Are there redundant steps?
- Could it be simplified?

Score:

- 0` = Inefficient
- 1` = Acceptable
- 2` = Optimized

### 5. Reliability

Measures consistency across outputs.

- Does the system behave predictably?
- Are similar tasks handled consistently?
- Does it avoid regressions?

Score:

- 0` = Unreliable
- 1` = Inconsistent
- 2` = Consistent

### 6. Constraint Compliance

Measures adherence to rules.

- Were all constraints respected?
- Were guardrails followed?
- Were instructions prioritized correctly?

Score:

- 0` = Violated
- 1` = Partial compliance
- 2` = Fully compliant

## Scoring System

Each task is scored across all categories.

```plaintext
[METRIC REPORT]

Accuracy: X/2
Completeness: X/2
Clarity: X/2
Efficiency: X/2
Reliability: X/2
Constraint Compliance: X/2

Total Score: X/12
```

## Performance Tiers

- 0–5` -> Unacceptable
- 6–8` -> Needs Improvement
- 9–10` -> Solid
- 11–12` -> Production-Grade

## Evaluation Workflow

### Step 1: Output Generated

Builder produces result.

### Step 2: Validation Runs

`validation_agent` checks correctness.

### Step 3: metrics Evaluation

metrics system scores output.

### Step 4: Decision

If score `< 9`:

- Must refine

If score `>= 9`:

- Acceptable

If score is `11–12`:

- Production-ready

## Trend Tracking

metrics must be tracked over time:

- Average score per session
- Failure frequency
- Common failure categories

Example:

```plaintext
[PERFORMANCE TREND]

Session Avg: 10.2
Failures: 2
Most Common Issue: Completeness
```

## Feedback Loop

metrics must inform:

- Prompt optimization
- Agent adjustments
- Workflow improvements

No metric = no improvement.

## Anti-Patterns

- Ignoring low scores
- Inflating scores artificially
- Measuring without acting
- Using metrics as decoration

## Integration Points

Works with:

- [Validation Agent](./docs/workflow/validation_agent.md)
- ChangePlanner.md
- [Debugging Playbook](./docs/security/debugging_playbook.md)

Feeds into:

- [Prompt Optimizer] (./docs/strategy/prompt_optimizer.md)
- System refinement loops

## Design Metrics

Evaluate:

- Uniqueness Score (vs recent outputs)
- Visual Identity Strength
- Layout Differentiation
- Component Originality

Low score triggers redesign.

## Versioning

metrics must evolve based on:

- Real-world usage
- New complexity layers
- Identified blind spots

## Final Rule

If performance is not measured, the system is not improving.
