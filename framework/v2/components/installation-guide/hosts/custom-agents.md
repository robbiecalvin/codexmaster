# Custom agent system setup
This guide is vendor-neutral; no runtime service is supplied. Implement a trusted loader, explicit permission policy, state store, and workflow controller in your chosen runtime.

1. Pin an approved distribution and registry hash. Resolve paths within a trusted root; reject path escapes and untrusted instructions. Load mandatory governance into the host's appropriate instruction channel, subordinate to host policy.
2. Implement registry lookup and actual capability checks; registered is not installed. Read only applicable skill instructions and supporting references. Do not execute bundled scripts merely because a manifest mentions them.
3. Implement Workflow Engine transitions and Agent Workflow handoff validation. Use stable task IDs, artifact revisions and idempotency keys. Single-role simulation is acceptable if accurately labeled; separate agents require authorization.
4. Enforce tool permissions outside the model. Require revision-bound approval tokens for protected actions, reject stale tokens, and block unauthorized writes, deployment or delegation. Use least privilege, secret stores, isolated test environments and redacted logs.
5. Persist retry reservations atomically before attempting corrections. Prevent concurrent duplicate effects, reject stale handoffs, and invalidate downstream results on relevant changes. Block recovery if the counter is unknown.
6. Enforce success gates using observed test evidence, Validation PASS and eligible Metrics acceptance; do not allow model-generated status alone to authorize production effects. Provide blocker/partial delivery paths.
7. Test using mocks and disposable fixtures before enabling any external side effects. Confirm restart recovery, approval denial, failure of governance loading, duplicate deliveries and retry exhaustion. Configure periodic audit only if a real scheduler and authorization exist.

If using OpenAI API skill facilities, consult https://developers.openai.com/api/docs/guides/tools-skills for supported attachment and sandbox mechanisms. A custom controller is still required for framework-specific enforcement.
