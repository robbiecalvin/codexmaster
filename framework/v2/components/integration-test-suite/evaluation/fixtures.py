"""Materialize deterministic, disposable fixture inputs; never invoke a model."""
import hashlib
import json
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def material(item):
    library=json.loads((ROOT/"fixtures/library.json").read_text())
    files=dict(library[item["family"]])
    scenario=item["id"]
    overrides={"B16":{"attempts":None},"B17":{"handler_available":False},"B13":{"ratings":[2,1,1,1,1,2]},"B14":{"ratings":[2,2,1,1,1,2],"stages_complete":True},"B26":{"cause":"broken dependency"}}
    if scenario in overrides:
        name="retry.json" if scenario in ("B16","B17") else "history.json"
        data=json.loads(files[name]);data.update(overrides[scenario]);files[name]=json.dumps(data,sort_keys=True)+"\n"
    files["scenario.json"]=json.dumps({"id":scenario,"setup":item.get("setup",item.get("prompt"))},sort_keys=True)+"\n"
    hashes={name:hashlib.sha256(content.encode("utf-8")).hexdigest() for name,content in sorted(files.items())}
    prompt=item["prompt"]+"\nFixture setup: "+item.get("setup",item.get("acceptance",""))+"\nInspect supplied fixture files. Follow actual host permissions."
    metadata={"id":item["id"],"files":hashes,"fixture_hash":hashlib.sha256(json.dumps(hashes,sort_keys=True).encode()).hexdigest(),"prompt":prompt,"prompt_hash":hashlib.sha256(prompt.encode()).hexdigest(),"criteria":item["criteria"]}
    metadata["criteria_hash"]=hashlib.sha256(json.dumps(item["criteria"],sort_keys=True).encode()).hexdigest()
    return files,metadata

def provision(item,parent=None):
    files,metadata=material(item)
    root=Path(tempfile.mkdtemp(prefix="codexmaster-",dir=parent))
    for name,content in sorted(files.items()):
        target=(root/name).resolve()
        if not target.is_relative_to(root.resolve()):
            raise ValueError("unsafe fixture path")
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_bytes(content.encode("utf-8"))
    return root,metadata
