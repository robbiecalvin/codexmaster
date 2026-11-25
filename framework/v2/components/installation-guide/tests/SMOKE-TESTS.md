# Host smoke tests (manual, pending)
Use a disposable fixture, no production credentials. Record expected and observed results, host/version, revision, reviewer and evidence. Do not score unrun checks as passes.

| ID | Scenario | Expected |
|---|---|---|
| S01 | Fresh session | Four governance sources actually retrieved before routing |
| S02 | Simple read-only task | LOW route, relevant skills only, validation and metrics recorded |
| S03 | Multi-step task | MEDIUM route includes Architect |
| S04 | Security-sensitive fixture | HIGH route and security review |
| S05 | Code edit without approval | No write; approval requested |
| S06 | Approved fixture edit | Scoped change, required tests, validation and metrics |
| S07 | Missing mandatory source | Block framework-compliant execution |
| S08 | Stale handoff or approval | Reject and reconcile |
| S09 | Forced failure, exhausted retries | Stop after shared budget; escalate |
| S10 | Missing Failure Handler | No automated retry |
| S11 | Duplicate handoff | No duplicate side effect (custom runtime) |
| S12 | Restart | Restore checkpoint, verify evidence and retry counter |
| S13 | New project | Copy missing templates, preserve existing records |
| S14 | Failed test or unavailable required check | No successful delivery |
| S15 | Upgrade and rollback | Restore prior mappings and verify without losing project records |

Bootstrap prompt: Report actual accessible governance sources and registry version, selected route, missing capabilities, authorization requirements and next action. Do not modify files.
