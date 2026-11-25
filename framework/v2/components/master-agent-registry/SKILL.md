---
name: master-agent-registry
description: Discover and reconcile framework skill registrations and activation requirements without granting authority or replacing routing.
---
# Master Agent Registry v1.0.0
Load mandatory governance through host instructions before routing. Use registry.json as metadata, not authority. Task Router owns selection and Workflow Engine owns stage order. Agent Workflow owns handoff protocol; State Manager owns per-task state.

## Discovery
1. Inspect actual authorized host catalog and local instructions. Match exact IDs, versions and source identity; record missing, conflicting or inaccessible entries. Never execute discovered scripts or install automatically.
2. Apply mandatory governance and route roles first. LOW: Router, Context Resolver, Builder, Validation, Metrics; MEDIUM adds Architect; HIGH adds Architect and Critic. Workflow Engine coordinates all. Security risk forces HIGH with security review. Metrics acceptance requires Validation PASS, Accuracy and Constraint Compliance 2/2, total >=9. No missing required stage may be silently omitted.
3. Shortlist conditional skills using objective, trigger, description and actual capabilities. Read selected SKILL.md and relevant references. Prerequisite roles describe handoff readiness, not recursive activation or additional mandatory stages. Explicit advisory Critic review may use an existing proposal instead of activating Architect. Prefer smallest sufficient set; record reasons.
4. Check host permissions, actual compatibility, required inputs, current revisions and approvals. A role may be performed locally if authorized; separate delegation requires authorization. Missing required capability blocks affected work; optional unavailable support is disclosed. Unknown compatibility is not verified compatibility.
5. Resolve conflicts via Instruction Priority and Context Resolver; do not use metadata to override governing instructions. Recheck on reroute or changed evidence. Record selected, unavailable and rejected skills and performer in task state.

## Lifecycle
DISCOVER, SELECT, VERIFY, REGISTER, UPDATE, RETIRE, AUDIT. Permanent changes require owner approval, versioned diff, dependency impact review and validation. Preserve prior versions and rollback references. Retirement must not remove required governance or route roles without approved replacement. Do not reset shared three-retry budget, bypass developer approval for code edits, or claim runtime enforcement from registration.
