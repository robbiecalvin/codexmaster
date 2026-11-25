---
name: state-manager
description: Maintain authoritative project checkpoints, decisions and verification evidence; reconcile context and resume unfinished work. Use at milestones, blockers, handoffs and session restoration.
---
# State Manager v1.0.0

## Authoritative state
Use existing project equivalents first. Next Steps owns active goal, progress, blockers, evidence and next action. Decision Register owns material decisions, rationale, owners, pending questions and superseded decisions. Specifications, source, configuration and tests own requirements and implementation facts. Owning framework guides hold reusable lessons. Session holds temporary notes and hypotheses. Link authoritative records rather than duplicate histories. Never create competing records silently.

## Checkpoint procedure
Modes: CHECKPOINT, RESTORE, RECONCILE, VERIFY, CLOSE, INSPECT. Update current-work entry after material milestones, verification results, blockers or before ending unfinished work. Skip routine steps when checkpoint remains accurate. Record objective, acceptance criteria, status, relevant files and revision/environment, last verified result with evidence, outstanding checks, blockers and next concrete action. Link decision IDs. Exclude secrets and sensitive data. Close completed tasks with final verification evidence. If durable storage is unavailable or unauthorized, provide a portable checkpoint and explicitly state it was not persisted.

## Restore and reconcile
Read applicable instructions, latest checkpoint, linked decisions and requirements. Compare current request, files/working tree and revision/environment. Evidence remains applicable only if its scope and inputs match; invalidate affected evidence when inputs change or are unknown. Continue from next unfinished action; recheck affected behavior. Use Context Resolver for conflicts; ask owner when a material unresolved decision is needed. Record and link open decisions where authorized. Update stale records as resolved. Preserve unrelated edits; if concurrent changes conflict, stop and reconcile rather than overwrite.

## Hybrid autonomy
Automatically inspect, checkpoint, reconcile factual state and invalidate stale evidence within authorization. Material decision changes and permanent framework changes require approval. Record observed decisions without inventing approval. Do not claim persistence, verification or access without evidence. Never store secrets. See references/integration.md and templates/checkpoint.md.

