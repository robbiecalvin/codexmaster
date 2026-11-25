---
name: environment-specification
description: Discover and enforce target runtime, dependency, configuration, build and test constraints. Use when planning, writing, building or validating software.
---
# Environment Specification v1.0.0

## Procedure
1. Resolve target environment separately from the current execution host. Inspect authorized manifests, lockfiles, CI, containers, version files and project instructions. Record declared versus observed versions, commands and evidence. Do not assume access or silently substitute runtimes.
2. Default target baseline unless explicitly overridden: Python 3.11, PHP 8.2, JavaScript Node 18, Bash, SQL (discover dialect); POSIX-compatible shell, Linux-like filesystem, UTF-8. Bash-specific syntax requires Bash explicitly. Flag unsupported or end-of-life versions (including Node 18); propose upgrades without changing the baseline.
3. Prefer npm, pip and Composer respectively. Use pnpm, yarn, poetry or pipenv only if configured or explicitly authorized. Prefer standard library and built-ins; justify dependencies for security, correctness or interoperability. Respect lockfiles; do not install or change dependencies without applicable authorization.
4. Discover actual test commands; typical defaults npm test, pytest, phpunit are candidates, not proof of availability. Use noninteractive deterministic tests and reproducible clean builds without undocumented global tools or machine configuration. Record command, environment, exit status and relevant sanitized evidence; mark unavailable checks BLOCKED, not PASS.
5. Avoid shell injection, dynamic execution, unsafe reflection and eval-style execution. Pass arguments safely; do not interpolate untrusted shell input. Use relative project paths, explicit version-controlled nonsecret configuration and documented environment variables. Never store secrets in source, logs or reports.
6. Store timestamps in UTC and convert to local time for display. Control clocks, randomness and external dependencies in tests; use explicit seeds where randomness is required. Do not replace cryptographically secure randomness with deterministic seeds in production.
7. Report compatibility, dependencies, build/test readiness, deviations and blockers to Context Resolver, Architect, Builder and Validation. Reroute via Task Router when risk or scope changes. Persist verified evidence through State Manager; invalidate when inputs change.

## Modes
DISCOVER, VERIFY, COMPATIBILITY, BUILD-CHECK, TEST-CHECK, AUDIT.

## Hybrid autonomy
Inspect and run authorized safe checks automatically. Runtime upgrades, dependency changes, expanded access and permanent policy changes require applicable approval. Never fabricate results or expose secrets. Do not treat host capabilities as target verification.

## Integration
Read references/integration.md and the applicable adapter. Use templates/report.json.

