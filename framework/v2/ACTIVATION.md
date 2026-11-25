# CodexMaster v2 activation

Native discovery entries in ../../.agents/skills are relative directory symlinks to canonical skill packages. Start a fresh Codex session at the repository root, inspect the available skills (for example via the skill picker if supported), and verify all 34 names against components/master-agent-registry/registry.json. Explicitly invoke task-router on a read-only fixture; confirm mandatory governance was read, selected skills and actual availability are reported, and no write occurs without approval. Record client version, revision, discovery evidence and limitations. If symlink discovery fails, stop and request approval for a generated-copy alternative.

CI verifies repository structure and reference contracts, not live model behavior or machine-enforced approval. No independent agents are implied. The 28 behavioral scenarios remain pending.

## A06 release gate (pending)
Record exact client version and commit, actual discovery of all 34 skills, mandatory governance availability, read-only Task Router invocation, action trace and reviewer scope. Missing or unsupported host capabilities are BLOCKED, not PASS. Do not execute this gate until live testing is authorized.
