"""Materialize deterministic, disposable fixture inputs; never invoke a model."""
import hashlib
import json
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def provision(item, parent=None):
    library=json.loads((ROOT/"fixtures/library.json").read_text())
    root=Path(tempfile.mkdtemp(prefix="codexmaster-",dir=parent))
    files=library[item["family"]]
    hashes={}
    for name, content in sorted(files.items()):
        target=(root/name).resolve()
        if not target.is_relative_to(root.resolve()):
            raise ValueError("unsafe fixture path")
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_bytes(content.encode("utf-8"))
        hashes[name]=hashlib.sha256(target.read_bytes()).hexdigest()
    prompt=item["prompt"]+"\nFixture setup: "+item.get("setup",item.get("acceptance",""))+"\nInspect supplied fixture files. Follow actual host permissions."
    metadata={"id":item["id"],"files":hashes,"fixture_hash":hashlib.sha256(json.dumps(hashes,sort_keys=True).encode()).hexdigest(),"prompt":prompt,"prompt_hash":hashlib.sha256(prompt.encode()).hexdigest(),"criteria":item["criteria"]}
    return root,metadata
