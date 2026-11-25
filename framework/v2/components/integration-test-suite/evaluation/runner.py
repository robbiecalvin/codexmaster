"""Offline CLI. Never launches a model or executes fixture instructions."""
import argparse
import json
from pathlib import Path
from evidence import verify
from schema import validate
from fixtures import provision, material
from metrics import telemetry
from report import render, regressions

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads(Path(path).read_text())

def catalog():
    return load(ROOT/"scenarios/behavioral-fixtures.json")+load(ROOT/"scenarios/benchmarks.json")

def checked(path, evidence_root, config):
    records = load(path)
    seen = set()
    attempts = set()
    ids = {r["id"] for r in catalog()}
    for r in records:
        if r.get("id") not in ids or type(r.get("synthetic")) is not bool:
            raise ValueError("unknown scenario or missing synthetic flag")
        if not r.get("run_id") or r["run_id"] in seen:
            raise ValueError("missing or duplicate run ID")
        seen.add(r["run_id"])
        validate(r,config)
        key = (r["id"],r["version"],r["task_id"],r["attempt"])
        if key in attempts:
            raise ValueError("duplicate task attempt")
        attempts.add(key)
        item=next(item for item in catalog() if item["id"]==r["id"])
        if r["status"]!="NOT_RUN":
            _,prepared=material(item)
            for field in ("fixture_hash","prompt_hash","criteria_hash"):
                if r.get(field)!=prepared[field]:
                    raise ValueError("prepared input mismatch: "+field)
        verify(r,evidence_root,item["criteria"])
        telemetry(r)
    return records

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command",choices=["catalog","prompt","prepare","report","regression"])
    parser.add_argument("--id")
    parser.add_argument("--records")
    parser.add_argument("--config")
    parser.add_argument("--baseline")
    parser.add_argument("--evidence-root",default=".")
    parser.add_argument("--output")
    args = parser.parse_args()
    if args.command == "catalog":
        print(json.dumps(catalog(),indent=2))
    elif args.command == "prepare":
        item = next(r for r in catalog() if r["id"]==args.id)
        root,metadata=provision(item,args.output)
        print(json.dumps({"directory":str(root),**metadata},indent=2))
    elif args.command == "prompt":
        item = next(r for r in catalog() if r["id"]==args.id)
        print(material(item)[1]["prompt"])
    else:
        config = load(args.config)
        records = checked(args.records,args.evidence_root,config)
        if args.command == "regression":
            failures = regressions(checked(args.baseline,args.evidence_root,config),records)
            print(json.dumps(failures))
            return int(bool(failures))
        data,html = render(records)
        if args.output:
            output = Path(args.output)
            output.mkdir(parents=True,exist_ok=True)
            (output/"report.json").write_text(json.dumps(data,indent=2)+"\n")
            (output/"report.html").write_text(html)
        print(json.dumps(data,indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
