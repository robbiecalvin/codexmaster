# Proposed distribution layout
- AGENTS.md: root governing entry point.
- skills/<id>/SKILL.md: 34 standalone skills, matching registry entries.
- components/master-agent-registry/: registry and selection instructions.
- components/agent-workflow/: handoff protocol.
- codex/project/: immutable master templates; working copies must be separate.

The registry's component paths are preserved. The registry's own location is proposed here. Resolve host mappings and existing project equivalents before execution. The original template link `../workflow/state_manager.md#save-a-checkpoint` resolves through the compatibility reference in codex/workflow/. Do not rewrite original templates silently.

Missing Failure Handler: both bootstrap and Workflow Engine block automated retries (owner-approved INT-001). Engineering Task Template's all-tests requirement remains binding where applicable; efficiency does not narrow it.
