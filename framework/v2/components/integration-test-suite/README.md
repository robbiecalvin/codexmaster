# Integration Test Suite v1.0.0
Requires Python 3.11+, standard library only. Run from this package:

```sh
python3 tests/test_contract.py
python3 tests/check_framework.py /path/to/assembled/framework
```
The first command tests a small reference contract model, not a deployed runtime. The second checks pinned skill and template hashes, registry metadata, paths and two known compatibility issues. Nonzero means a failed check. Do not waive failures to claim readiness. Baseline updates require approved framework changes and regenerated hashes. This suite is read-only against the target.

Behavioral scenarios are in `scenarios/behavioral.json`. Run each in an isolated host session with authorized fixtures, capture observed actions and compare expected outcomes. Mark PASS/FAIL/BLOCKED/NOT_RUN with evidence, host/version, revision and reviewer. Never use live credentials or destructive production actions. Repeat on each target host. A text response alone cannot prove runtime enforcement. See `compatibility.md` and `results/` for observed checks. Final assembly and live execution remain pending.

## Offline evaluation extension
See [BENCHMARKING.md](BENCHMARKING.md) for the offline runner, evidence records, matched benchmarks, reporting and regression checks. Live tests remain NOT_RUN.
