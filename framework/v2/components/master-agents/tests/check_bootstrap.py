from pathlib import Path
import re, sys, json
root = Path(__file__).resolve().parents[1]
text = (root / "AGENTS.md").read_text()
paths = re.findall(r"`((?:skills|components)/[^`]+(?:SKILL\.md|registry\.json))`", text)
assert len([p for p in paths if p.startswith("skills/")]) == 4
for phrase in ("Every code modification", "Validation PASS", "Metrics Accept", "three retries", "Security risk forces HIGH", "all tests"):
    assert phrase in text, phrase
cases = json.loads((root / "tests/scenarios.json").read_text())
assert len({c["id"] for c in cases}) == len(cases)
if len(sys.argv) > 1:
    assembled = Path(sys.argv[1])
    for path in paths + ["components/master-agent-registry/SKILL.md", "codex/project/project_context.md"]:
        assert (assembled / path).is_file(), path
    print("Referenced assembly paths exist")
else:
    print("Assembly path checks not run")
print("Static bootstrap checks passed; behavioral tests not run")
