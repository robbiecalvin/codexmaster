"""Read-only checks of assembled framework; no live agent execution."""
import argparse, hashlib, json, re
from pathlib import Path
BASE=json.loads((Path(__file__).resolve().parents[1]/'fixtures/baseline.json').read_text())
def check(root):
    results=[]
    def record(name,ok,detail=''):
        results.append(dict(check=name,status='PASS' if ok else 'FAIL',detail=detail))
    def read(rel):
        f=root/rel
        if not f.resolve().is_relative_to(root.resolve()): raise ValueError('Escaped path')
        return f.read_bytes()
    try:
        reg=json.loads(read('components/master-agent-registry/registry.json'))
        ids=[s['id'] for s in reg['skills']]; expected={s['id'] for s in BASE['skills']}
        record('registry identity',len(ids)==34 and set(ids)==expected)
        record('mandatory governance',{s['id'] for s in reg['skills'] if s['activation']=='mandatory'}=={'instruction-priority','operational-guardrails','system-contract','model-behavioral-instructions'})
        for s in BASE['skills']:
            try:
                b=read(s['entrypoint']); record('skill '+s['id'],hashlib.sha256(b).hexdigest()==s['source_sha256'])
            except (OSError,ValueError) as e: record('skill '+s['id'],False,str(e))
        record('registry metadata baseline',reg['skills']==BASE['skills'])
        record('prerequisites',all(set(s['prerequisite_roles'])<=expected for s in reg['skills']))
        for t in BASE['templates']:
            try: record('template '+t['path'],hashlib.sha256(read(t['path'])).hexdigest()==t['sha256'])
            except (OSError,ValueError) as e: record('template '+t['path'],False,str(e))
        for f in ['AGENTS.md','components/agent-workflow/SKILL.md','components/master-agent-registry/SKILL.md']:
            record('entry '+f,bool(read(f)))
        master=read('AGENTS.md').decode(); engine=read('skills/workflow-engine/SKILL.md').decode()
        record('fallback policy consistency','block automated retries' in master and 'If Failure Handler is unavailable, block automated retries' in engine and 'stop after a failed recovery attempt' not in engine,'Both instructions must block automated retries when handler unavailable')
        ref=root/'codex/workflow/state_manager.md'
        record('template external state reference',ref.is_file() and bool(re.search(r'^#+ +Save a checkpoint\s*$',ref.read_text(),re.M|re.I)) and '../../skills/state-manager/SKILL.md#checkpoint-procedure' in ref.read_text() and '## Checkpoint procedure' in read('skills/state-manager/SKILL.md').decode(),'Compatibility target and authoritative checkpoint link required')
    except (OSError,ValueError,KeyError,TypeError) as e: record('layout readable',False,str(e))
    return results
if __name__=='__main__':
    a=argparse.ArgumentParser(); a.add_argument('root',type=Path); args=a.parse_args(); r=check(args.root)
    print(json.dumps(r,indent=2)); raise SystemExit(any(x['status']=='FAIL' for x in r))
