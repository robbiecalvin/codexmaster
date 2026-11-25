# Integration and evidence
Task Router owns route selection; Context Resolver owns context reconciliation; Workflow Engine owns stage execution; State Manager owns durable checkpoints; Developer Workflow owns human approval; Validation Agent owns correctness review; Metrics owns acceptance rubric; Failure Handler owns recovery; Security Agent and Guardrails own security checks; Auditor independently reviews only when actually separate and authorized.

Evidence types (not a ranking): instruction-defined, agent-reviewed, independently-reviewed, machine-verified, machine-enforced, unverified. Record mechanism, scope, revision, observed result and reviewer. A local passing test proves only covered behavior; CI is a gate only if configuration prevents the relevant operation on failure. Independent review requires actual reviewer separation. Missing or stale evidence is unverified. Never infer enforcement from documentation. Use sanitized references rather than secrets.

Host adapters must load mandatory governance before routing. No automatic hooks are supplied. Missing required skills/checks block successful completion; report limitations. Existing workflow packages need integration updates for mandatory loading and approval gates.

