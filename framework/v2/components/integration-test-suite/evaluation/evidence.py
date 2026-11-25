"""Offline evidence checks; reviewer assertions are not runtime enforcement."""
import hashlib
from pathlib import Path

def verify(record, root):
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
    root = Path(root).resolve()
    for item in evidence:
        path = (root / item["path"]).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError("invalid evidence path")
        if hashlib.sha256(path.read_bytes()).hexdigest() != item["sha256"]:
            raise ValueError("evidence hash mismatch")
