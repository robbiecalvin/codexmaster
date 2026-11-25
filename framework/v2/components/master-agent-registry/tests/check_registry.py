import json
from pathlib import Path
r=json.loads((Path(__file__).resolve().parents[1]/'registry.json').read_text())
s=r['skills']; ids={x['id'] for x in s}
assert len(s)==len(ids)==34
assert {x['id'] for x in s if x['activation']=='mandatory'}=={'instruction-priority','operational-guardrails','system-contract','model-behavioral-instructions'}
for x in s:
 assert set(x['prerequisite_roles'])<=ids
 assert x['availability']=='unknown'
 assert len(x['source_sha256'])==64
 assert x['entrypoint']==f"skills/{x['id']}/SKILL.md"
 assert x['description'] and x['activation']
print('PASS: 34 unique registrations, governance, references and metadata checks')
