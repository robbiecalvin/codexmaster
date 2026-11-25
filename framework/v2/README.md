# Master AI Agent Development Framework v1.0.0

34 standalone skills, 14 master templates and all six integration components. Start with AGENTS.md and components/installation-guide/INSTALL.md. Select the host guide in components/installation-guide/hosts/. Keep master templates separate from project working copies. Do not overwrite existing instructions or automatically execute scripts.

## Verify from the extracted distribution root

```sh
python3 verify_manifest.py
python3 components/installation-guide/tests/check_installation.py .
python3 components/integration-test-suite/tests/check_framework.py .
python3 components/integration-test-suite/tests/test_contract.py
```

Python 3.11+; standard library only. Registry paths are relative to this root. Codex native discovery and ChatGPT source access require host-specific setup. No automatic installer, executable production orchestrator, or live host enforcement is included. All 28 behavioral scenarios remain NOT_RUN. See RELEASE-NOTES.md and components/integration-test-suite/results/ for evidence. Historical results are retained separately. Hashes establish consistency, not trusted provenance.
