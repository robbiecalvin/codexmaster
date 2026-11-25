"""Offline evidence checks; reviewer assertions are not runtime enforcement."""
import hashlib
from pathlib import Path

def verify(record, root, criteria=None):
    if record.get("status") not in ("PASS", "FAIL", "BLOCKED", "NOT_RUN"):
        raise ValueError("invalid status")
    if record["status"] == "NOT_RUN":
        return
    for key in ("id", "run_id", "revision", "host", "reviewer", "review_notes"):
        if not isinstance(record.get(key), str) or not record[key].strip():
            raise ValueError("missing " + key)
    evidence = record.get("evidence", [])
    if record["status"] in ("PASS", "FAIL") and not evidence:
        raise ValueError("missing evidence")
    if record["status"] == "PASS" and record.get("independent_review") is not True:
        raise ValueError("PASS requires independent review")
    if record.get("schema_version") == 2 and record["status"] == "PASS":
        assertions = record.get("assertions", [])
        if not assertions or any(a.get("status") != "PASS" or not a.get("criterion") or not a.get("evidence_paths") or not set(a["evidence_paths"]) <= {e["path"] for e in evidence} for a in assertions):
            raise ValueError("missing or unsupported acceptance assertions")
    if criteria is not None and record["status"] == "PASS":
        assertions = record.get("assertions", [])
        by_id = {a.get("criterion"):a for a in assertions}
        if len(by_id)!=len(assertions) or set(by_id)!={c["id"] for c in criteria}:
            raise ValueError("required criteria missing or duplicated")
        kinds = {e["path"]:e.get("kind") for e in evidence}
        for c in criteria:
            if not set(c["evidence_kinds"]) <= {kinds.get(path) for path in by_id[c["id"]]["evidence_paths"]}:
                raise ValueError("required evidence kinds missing")
    root = Path(root).resolve()
    for item in evidence:
        path = (root / item["path"]).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError("invalid evidence path")
        if hashlib.sha256(path.read_bytes()).hexdigest() != item["sha256"]:
            raise ValueError("evidence hash mismatch")
