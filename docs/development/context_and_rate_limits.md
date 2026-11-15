# MeetDiscreet — Context and Rate-Limit Efficiency

## 1. Purpose

Use Codex’s available context, tools, and execution capacity efficiently
while preserving correctness and continuity.

Prioritize useful completed work over framework ceremony.

Do not assume fixed message, token, tool, or account limits.
Use limits and warnings actually exposed by the environment.

Do not claim to know the remaining allowance unless it is available.

Efficiency must not weaken authorization, financial integrity,
privacy, or required verification.

## 2. Core Strategy

For each task:

1. Load the minimum sufficient authoritative context.
2. Inspect the relevant implementation.
3. Resolve only decisions required for that work.
4. Complete a coherent, reviewable increment.
5. Run appropriate checks.
6. Save a concise handoff when necessary.

Do not reload the entire framework for every small task.

Do not reduce the agreed product scope merely to conserve usage.
Sequence the work and preserve deferred requirements explicitly.

## 3. Context Entry Points

At the beginning of a new session or after losing relevant context,
start with:

- Root AGENTS.md.
- docs/project_context.md.
- Current-work section of docs/next_steps.md.

Inspect repository status before editing.

Then load only the documents relevant to the task.

Read README.md when needed for orientation or setup.
Do not repeatedly read unchanged overview documents when their relevant
contents are already available in the current context.

Applicable instructions must still be followed.

## 4. Task-Based Reading Guide

| Task | Primary documentation |
|---|---|
| New page design | Design system, page inventory, current page brief, relevant product requirements |
| Existing visual edit | Current page brief, relevant shared design rules |
| Profile or restricted media | Access matrix, relevant product rules, security requirements |
| Listing or boost | Listing requirements, pricing/allowance rules, access matrix |
| Subscription or billing | Pricing and payments, access matrix, integration architecture |
| Booking | Booking lifecycle, pricing and payments, relevant permissions |
| Messaging or calls | Relevant product rules, access matrix, integration configuration |
| Database change | Data model, affected domain rules, permissions |
| Deployment | Deployment guide, environment, relevant launch checks |
| Bug fix | Relevant source, tests, and requirements |
| Documentation edit | Supplied document and directly related authoritative files |

This guide is not permission to skip a document needed to resolve
a concrete dependency or conflict.

## 5. Progressive File Inspection

Explore before reading large amounts of content.

Prefer:

1. Directory or filename inventory.
2. Targeted text search.
3. Relevant sections.
4. Full affected files before editing when required by project instructions.
5. Related callers, contracts, and tests.

Use fast repository search tools such as rg when available.

Avoid:

- Dumping the entire repository.
- Reading every Markdown file for a CSS edit.
- Printing huge generated files.
- Loading lockfiles or build output without a specific reason.
- Repeated searches with equivalent queries.

When a search returns excessive output, narrow it.

## 6. Reuse Current Context

Within an active session, reuse information already read when:

- Its source is known.
- It remains relevant.
- It has not changed.
- The required detail is still available.

Re-read when:

- The file changed.
- Context was lost or compressed.
- A precise detail is missing.
- A conflict appears.
- The current task affects a different section.

Do not treat remembered summaries as a substitute for inspecting
current source before an edit.

## 7. Separate Orientation From Execution

Do not reproduce the framework pipeline in every response.

For routine work, a short objective and completion report are sufficient.

Use detailed planning for consequential changes, not every adjustment.

Examples:

- Small spacing edit: inspect, change, preview.
- Shared component edit: inspect consumers, change, check affected pages.
- Payment change: inspect policies, integration, data effects, and tests.

Keep the depth proportional to the actual consequences.

## 8. Coherent Work Units

Choose increments that can be completed and reviewed meaningfully.

Examples:

- One designed page.
- One reusable component and its consumers.
- One endpoint with authorization and tests.
- One booking transition.
- One payment-event handler.
- One verified bug fix.

Do not split tightly coupled work into artificial fragments that leave
the application broken.

Do not begin several unrelated features when one complete feature
would provide a better result.

Larger authorized tasks may span several increments.
Continue until completed or genuinely blocked.

## 9. Efficient Design Questions

For a new page:

- Read existing visual decisions first.
- Ask one focused batch of relevant questions.
- Offer concrete options.
- Reuse answers on later pages where applicable.

Do not repeatedly ask about settled colours, fonts, or navigation.

For clear edit requests, implement without restarting design discovery.

Record meaningful answers in the page brief so later sessions
do not need to ask again.

Do not interpret missing answers as approval of consequential choices.

## 10. Tool-Call Efficiency

Batch independent reads or searches where supported.

Keep dependent operations sequential.

Examples:

- Read several independent relevant documents together.
- Search related identifiers in one focused operation.
- Inspect a file before deciding how to edit it.
- Apply a migration only after the required review and authorization.

Do not parallelize conflicting writes.

Use the smallest output sufficient to assess the result.

Do not repeatedly poll a running operation when an appropriate
completion notification or longer supported wait is available.

Tool efficiency must follow the actual tool instructions.

## 11. External Documentation

Use official documentation when current provider behaviour,
API syntax, version compatibility, or service eligibility matters.

Prefer focused lookups over broad repeated searches.

Record durable integration decisions and relevant references.

Do not:

- Invent APIs to avoid a lookup.
- Recheck unchanged facts without a reason.
- Copy entire documentation pages into project files.
- Treat cached knowledge as current when freshness matters.

Provider credentials and customer data must not appear in searches.

## 12. Verification Efficiency

Run checks that meaningfully address the change.

Suggested progression:

1. Focused check for the changed behaviour.
2. Related regression checks.
3. Broader checks when dependencies or risk justify them.
4. Required release checks before deployment.

Do not rerun an unchanged passing suite repeatedly without a reason.

Recheck when:

- Code or configuration changed.
- A previous failure remains unresolved.
- Integration conditions changed.
- Earlier evidence does not cover the current revision.

Never skip authorization or financial checks merely to conserve usage.

Report what was not tested.

## 13. Output Discipline

Keep normal reports concise:

- What changed.
- What was verified.
- Important limitations.
- Next action.

Do not repeatedly restate the product specification.

When editing files directly:

- Apply changes to the repository.
- Summarize the result.
- Avoid pasting entire large files unless requested.

When Robbie needs to copy a file manually:

- Provide complete contents.
- Provide its intended path.
- Do not replace required sections with placeholders.

Match output length to the actual deliverable.

## 14. Avoid Documentation Churn

Update only authoritative files affected by meaningful work.

Examples:

- Page brief for a page decision.
- Design system for a shared visual rule.
- Decision register for a material choice.
- Roadmap for progress.
- Environment guide for changed setup.

Do not rewrite every document after every task.

Do not create:

- A second roadmap.
- Duplicate specifications.
- Repetitive session logs.
- A new memory file with competing facts.
- Formal records for every minor CSS change.

Use repository history for detailed revisions.

## 15. Context Compression

When context becomes crowded:

1. Preserve the current objective.
2. Preserve explicit user corrections.
3. Preserve unresolved decisions.
4. Preserve relevant financial and access constraints.
5. Preserve current implementation and verification status.
6. Reference detailed source files.
7. Remove repeated discussion.

A compact summary should point to authoritative files,
not attempt to reproduce them all.

Do not remove details essential to safe continuation.

## 16. Handling Rate Limits and Service Errors

Distinguish:

- Model/account usage limits.
- Tool-service rate limits.
- Temporary network errors.
- Authentication failures.
- Invalid requests.
- Provider outages.

Respond to the actual reported condition.

For a tool rate limit:

- Follow an exposed retry interval where supported.
- Use bounded backoff.
- Avoid repeated immediate retries.
- Continue independent work if possible.

Do not retry authentication or validation failures as if they were
temporary rate limits.

Do not evade limits using alternate accounts, connections,
or repeated equivalent calls.

Do not promise an automatic resume unless a real supported mechanism
has been configured.

## 17. Low-Capacity Handoff

When a limit is reported, context is nearly exhausted, or continued
work cannot proceed reliably:

1. Finish the current atomic edit if feasible.
2. Avoid starting unrelated work.
3. Preserve coherent files.
4. Record incomplete integration honestly.
5. Update the current-work section in docs/next_steps.md.
6. State the next concrete action.

Do not claim the whole task is complete merely because the current
session must stop.

If unable to save a handoff, provide a concise copyable continuation
summary.

## 18. Handoff Contents

Record:

- Current objective.
- Relevant source revision or working-tree status.
- Files changed.
- Last completed action.
- Checks run and results.
- Unfinished work.
- Pending decisions.
- Known failures.
- Exact next action.
- References to authoritative documents.

Exclude secrets and private customer information.

Do not automatically commit or push merely to create a handoff.
Follow the authorization established for the workflow.

## 19. Resuming Efficiently

On continuation:

1. Read the root instructions and current handoff.
2. Inspect repository status.
3. Verify relevant files have not changed unexpectedly.
4. Load only missing task-specific context.
5. Continue from the recorded next action.

Do not restart completed discovery or regenerate approved pages.

A handoff is an orientation aid, not proof that the implementation
matches its description.

## 20. Multiple Agents

Do not create separate agents merely because framework stages
have names such as Architect, Builder, or Validator.

Use additional agents only when authorized by applicable instructions
and when the work genuinely benefits from delegation.

Consider coordination and duplicated-context costs.

Do not claim parallel review occurred unless actual agents performed it.

A single agent can plan, implement, and validate a focused task.

## 21. Completion Standards

Efficiency does not change the definition of completion.

Do not:

- Drop requested features silently.
- Hide failing checks.
- Invent verification.
- Skip required decisions.
- Weaken backend controls.
- Treat a prototype as a production integration.
- Substitute a summary for an implementation request.

If blocked, explain the specific limitation and preserve a useful
continuation point.

## 22. Final Rule

Read selectively.
Work in coherent increments.
Reuse current context.
Verify proportionally.
Save precise handoffs.

Spend capacity on completing MeetDiscreet, not repeatedly
reciting its framework.