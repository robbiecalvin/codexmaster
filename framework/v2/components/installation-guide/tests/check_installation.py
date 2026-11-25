"""Read-only full-layout verifier. No host enforcement claims."""
import argparse, hashlib, json
from pathlib import Path

def verify(root):
    errors = []
    def read(relative):
        path = root / relative
        if not path.resolve().is_relative_to(root.resolve()) or not path.is_file():
            raise ValueError(f"Missing or escaped path: {relative}")
        return path.read_bytes()
    try:
        registry = json.loads(read('components/master-agent-registry/registry.json'))
        skills = registry['skills']
        ids = [s['id'] for s in skills]
        if len(ids) != 34 or len(set(ids)) != 34:
            errors.append('Expected 34 unique skill IDs')
        mandatory = {'instruction-priority','operational-guardrails','system-contract','model-behavioral-instructions'}
        if {s['id'] for s in skills if s['activation']=='mandatory'} != mandatory:
            errors.append('Mandatory governance mismatch')
        for s in skills:
            try:
                if s['entrypoint'] != f"skills/{s['id']}/SKILL.md":
                    raise ValueError('Unexpected entrypoint')
                if hashlib.sha256(read(s['entrypoint'])).hexdigest() != s['source_sha256']:
                    errors.append(f"Hash mismatch: {s['id']}")
                if not set(s['prerequisite_roles']).issubset(ids):
                    errors.append(f"Unknown prerequisite: {s['id']}")
            except (ValueError, OSError, KeyError) as exc:
                errors.append(f"{s.get('id')}: {exc}")
        for name in ('AGENTS.md','components/agent-workflow/SKILL.md','components/master-agent-registry/SKILL.md'):
            read(name)
        for name in ('access_matrix','application_architecture','application_diagram','application_security','booking_lifecycle','data_model','decisions','deployment','launch_acceptance','next_steps','page_inventory','pricing_and_payments','product_spec','project_context'):
            read(f'codex/project/{name}.md')
    except (ValueError, OSError, KeyError, TypeError) as exc:
        errors.append(str(exc))
    return errors

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    args = parser.parse_args()
    errors = verify(args.root)
    print(json.dumps({'status':'FAIL' if errors else 'PASS','scope':'static full layout and skill hashes; not runtime or template content verification','errors':errors}, indent=2))
    raise SystemExit(bool(errors))
