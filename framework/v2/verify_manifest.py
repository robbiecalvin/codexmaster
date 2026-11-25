import hashlib,json
from pathlib import Path
r=Path(__file__).resolve().parent
m=json.loads((r/'manifest.json').read_text())
expected=m['files']; actual={p.relative_to(r).as_posix() for p in r.rglob('*') if p.is_file() and p.name!='manifest.json' and '__pycache__' not in p.parts}
errors=[]
for name,h in expected.items():
 p=r/name
 if not p.resolve().is_relative_to(r) or not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=h: errors.append(name)
errors.extend(sorted(actual-set(expected)))
print(json.dumps({'status':'FAIL' if errors else 'PASS','files':len(expected),'errors':errors},indent=2))
raise SystemExit(bool(errors))
