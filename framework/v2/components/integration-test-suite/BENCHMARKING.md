# Offline evaluation
No model calls are made by this package. Native discovery must be verified first.
Use Python 3.11+. From this directory:
```sh
python evaluation/runner.py catalog
python evaluation/runner.py prompt --id B01
python tests/test_evaluation.py
python evaluation/runner.py report --records /tmp/records.json --evidence-root /tmp/evidence --output /tmp/report
```
Create a JSON array of run records using templates/run-record.json. Use unique run IDs and append records after each isolated session to resume. Keep sanitized evidence outside the repository; hash each artifact with SHA-256 and record its relative path. Review actual actions and before/after artifacts, not merely model claims. PASS requires independent reviewer attestation; the offline tool checks integrity, not truth of that attestation. Fixtures are setup recipes requiring manual provisioning, not executable environments. Do not expose credentials or production systems.

Pin V1 to 4d1fbad3873ac27f34db0f3048133e462fa8dd80 and record the approved V2 revision. Match model, effort, host version, fixture, prompt, permissions and criteria hashes. Use fresh sessions, alternate version order, separate V2-specific compliance from common engineering quality. Start with P01/P04/P09 after approval; expand only after reviewing pilot costs. Record actual telemetry or null. Never equate tokens with weekly allowance. Report sample sizes and blocked/failed runs. No causal or longitudinal claims from a single pair. Synthetic records are excluded from real reports. For regression checks use one approved comparable record per scenario/version in each input file; missing previously passing records are flagged. No automatic baseline promotion.
