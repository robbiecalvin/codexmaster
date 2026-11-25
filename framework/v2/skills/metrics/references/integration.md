# Integration
## Procedure
Consume the Validation Report for the current task and revision. Record reviewer, evidence references and validation status PASS/FAIL/BLOCKED. Rate each category only with evidence; unknown ratings are null, not zero or assumed passing.

| Category | 0 | 1 | 2 |
|---|---|---|---|
| Accuracy | Incorrect | Partially correct | Fully correct |
| Completeness | Major gaps | Minor gaps | Complete |
| Clarity | Confusing | Acceptable | Clear and structured |
| Efficiency | Inefficient | Acceptable | Optimized |
| Reliability | Unreliable | Inconsistent | Consistent |
| Constraint Compliance | Violated | Partial | Fully compliant |

Assess accuracy against expected behavior and tests; completeness against requirements and edge cases; clarity against usability and structure; efficiency against justified complexity and redundant work; reliability against relevant repeatability and regression evidence; compliance against constraints, guardrails and instruction priority. Record rationale per rating. Do not claim longitudinal reliability from a single test.

## Eligibility and decisions
Only PASS plus Accuracy=2 and Constraint Compliance=2 permits aggregate scoring; all six ratings must be supported before calculating a total. Otherwise leave total and tier null, record reason and route FAIL/BLOCKED via Workflow Engine; prerequisite ratings below 2 return to validation for correction. Missing evidence blocks scoring until resolved. Eligible totals: 4–5 Unacceptable, 6–8 Needs Improvement (both Refine and revalidate), 9–10 Solid, 11–12 Excellent (both Accept). Never accept incomplete mandatory requirements even if aggregate is high; reconcile inconsistent validation evidence. Repeat affected stages using shared Failure Handler budget. No fabricated scores.

## Trends and feedback
Track eligible totals only in averages; record sample count, task/revision, rubric version, failures including ineligible outcomes, frequency and common categories. Distinguish attempts from tasks and avoid double counting. Use existing State Manager records. Feed evidenced weaknesses to Change Planner, Debugging Playbook and workflow review; invoke Prompt Optimizer only for prompt-attributable issues (its rubric is separate). For new interfaces or intentional redesigns assess uniqueness versus available recent designs, identity, layout differentiation and component originality; report unknown history and use findings for refinement without changing the 12-point rubric. Version rubric changes with approval and preserve historical comparability.

Modes: SCORE, TREND, REFINE, AUDIT. Ratings are evidence-informed judgments, not necessarily objective measurements. Record limitations.
Use System Contract evidence rules, State Manager records and authorized host capabilities. No automatic installation or enforcement.
