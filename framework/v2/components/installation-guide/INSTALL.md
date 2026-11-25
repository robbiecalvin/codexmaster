# Common installation procedure
## Prerequisites
Authorized filesystem or project access, trusted copies of the framework packages, a backup location, a known target host and version, and Python 3.11+ for the optional verifier. No elevated permissions or dependencies are required for the verifier. Check host-specific requirements separately.

## Stage and inspect
- Inventory existing root and nested instructions, skills, project records, permissions and uncommitted changes. Do not overwrite them. Record an approved merge plan and rollback target.
- Inspect archive entries before extraction: reject absolute paths, traversal, symlinks and unexpected executable content. Extract to an empty staging directory; never run bundled scripts automatically.
- In the final distribution, root AGENTS.md comes from master-agents; each of 34 skill directories belongs under skills/; registry and agent-workflow directories go under components/; the 14 master documents go under codex/project/. Preserve source bytes and versions. Do not flatten multiple SKILL.md files into one directory.
- The final distribution includes the assembled layout. For manual staging of the earlier packages, copy their contents into these destinations only after reviewing collisions. Compare source instruction hashes against the registry and verify the template manifest. Do not treat matching hashes as proof of trusted provenance.
- Run the read-only verifier. Failures block full-installation claims. A selective installation must document omitted features and keep all mandatory controls and route prerequisites; the verifier intentionally checks the full layout only.

## Adopt
Choose the appropriate host guide. Keep master templates read-only by convention or filesystem permissions; copy only missing project working documents into an agreed separate location. Reuse existing equivalents. Record path mappings and resolve references, including the Next Steps link to State Manager, before relying on them. Do not silently rewrite source templates.

## Governance and readiness
Load four mandatory governance skills before routing; use registry discovery, then Task Router, Context Resolver and Workflow Engine. Security risk forces HIGH; code changes require scoped developer approval, including LOW; no successful delivery without Validation PASS and eligible Metrics acceptance (accuracy and constraint compliance both 2/2, total at least 9/12). One shared budget of three retries after initial attempt; block automated retry if counter or Failure Handler is unavailable. Mandatory tests override efficiency locks. The owner-approved fallback correction is included in this distribution; verify the integrated revision.

## Verify
Run tests/SMOKE-TESTS.md on a disposable project. Record actual host/version, instruction loading, paths, access, revision, observed outcomes, limitations and rollback target. Distinguish static, behavioral, and machine-enforced evidence. Do not mark ready if mandatory instructions, permissions, or checks are missing.
