# Upgrade, rollback and troubleshooting
Upgrade: inventory current version, source hashes, local changes and active tasks. Stage new release separately; inspect changes and conflicts; get owner approval for governance, architecture and permissions. Re-run static and host-specific smoke checks. Reconcile checkpoints, invalidated evidence and approvals before resuming. Switch the approved reference to the new version only after checks. Keep the previous distribution and mapping available.

Rollback: stop affected execution, preserve audit evidence and working records, restore prior approved instructions and path mappings without reverting unrelated application work. Recheck hashes and host discovery in a fresh session. Never assume framework rollback reverses application migrations or external effects; those need their own recovery authorization and evidence.

Uninstall: inventory framework-owned files and references, obtain approval before removals, preserve project records, remove only verified framework-owned artifacts and stale references. Recheck host instructions.

Troubleshooting:
- Missing skill: check actual access, path, exact ID, version and registry mapping; never invent availability.
- Duplicate skills: compare hashes and disable stale copies through authorized configuration.
- Conflicting instructions: resolve host hierarchy first; use Instruction Priority; block unresolved protected work.
- Approval prompt missing: stop code edits; verify the external gate instead of relying on a prompt.
- Context limit: load mandatory and route-required instructions first; retrieve optional references on demand; report inaccessible requirements.
- Failed static check: inspect named paths and hashes; restore trusted files rather than editing hashes to fit.
- Stale checkpoint: reconcile current revision, approvals and evidence; do not reset retry counter.
- Missing template link: resolve through approved mapping; preserve master originals until integration changes are authorized.
