# CodexMaster 2.0 migration — phase A

Baseline: `4d1fbad3873ac27f34db0f3048133e462fa8dd80` on main. Target: v2-development only.

## Approved policy
Every code modification, including LOW complexity, requires developer approval of a scoped change plan tied to the current revision. Read-only inspection, planning and authorized checks may proceed automatically. Material scope or risk changes require renewed approval. No self-approval. Preserve existing safety constraints. This policy supersedes conflicting legacy implicit routine-edit authorization on this branch.

## First integration commit
Change only root AGENTS.md and docs/AGENTS.md to establish the approved policy; add this migration record. Preserve all other existing files, including MeetDiscreet requirements, decisions, progress records, website, configuration, tests and CI. Do not merge to main.

## Next integration stage
Import the verified portable distribution into framework/v2/ without replacing existing project files. Reconcile legacy workflow references and native skill discovery before claiming v2 activation. Preserve existing CI and add separate framework verification. Run manifest, installation, static integration and reference contract checks; then execute live behavioral scenarios and matched v1/v2 benchmarks in disposable environments.

## Acceptance
Only the three planned paths change in this commit; main remains at the baseline; existing project documents remain unchanged. Runtime enforcement and behavioral performance are not established by this policy commit.


## Activation phase
Approved baseline: `e59dcf32e06670a5d072137e19bc2c1b9ed4a9f9`. Native discovery, bootstrap, legacy policy reconciliation and deterministic CI are introduced. Live discovery and behavioral testing remain pending; no main merge or deployment authorized.
