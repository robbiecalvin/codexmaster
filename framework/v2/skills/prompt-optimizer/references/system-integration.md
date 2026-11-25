# Integration contracts
Resolve paths relative to the existing repository, not this skill directory. Inspect actual contracts before changes.
- Task Router: workflow/task_router.md — mode and routing.
- Workflow Engine: workflow/workflow_engine.md — execution and retries.
- State Manager: workflow/state_manager.md#where-state-lives — persistence and version pointers.
- Metrics: metrics.md — score and evidence.
- Validation Agent: workflow/validation_agent.md — mandatory gates.
- task_template.md — task structure.
- design/design_memory.md and design/design_variation_engine.md — design patterns and variation gaps.
- workflow/agent_workflow.md and ProjectTemplates — downstream verified patterns.
Suggested adapter input: prompt ID, version, text, runtime, trigger, evidence, constraints, test cases. Suggested output: candidate, issue/evidence map, test results, risk, approval status, rollback pointer. Deduplicate events by prompt version and failure fingerprint; prevent recursive optimization. Actual event hooks and storage must be wired by the host. Never assume an integration is active.
