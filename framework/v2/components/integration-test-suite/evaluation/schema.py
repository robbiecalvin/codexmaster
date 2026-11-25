"""Strict record and revision validation for offline evaluation."""
import re

def digest(value):
    return isinstance(value,str) and re.fullmatch(r"[0-9a-f]{64}",value) is not None

def validate(record, config):
    if not isinstance(record,dict) or record.get("schema_version") != 2:
        raise ValueError("unsupported record schema")
    version=record.get("version")
    if version not in ("V1","V2"):
        raise ValueError("unsupported framework version")
    pin=config.get("revisions",{}).get(version)
    if not isinstance(pin,str) or not re.fullmatch(r"[0-9a-f]{40}",pin) or record.get("revision") != pin:
        raise ValueError("revision mismatch")
    if not isinstance(record.get("task_id"),str) or not record["task_id"].strip():
        raise ValueError("missing task ID")
    if type(record.get("attempt")) is not int or record["attempt"] < 1:
        raise ValueError("invalid attempt")
    if record.get("status") not in ("PASS","FAIL","BLOCKED","NOT_RUN"):
        raise ValueError("invalid status")
    if record.get("status") != "NOT_RUN":
        for key in ("fixture_hash","prompt_hash","permissions_hash","criteria_hash"):
            if not digest(record.get(key)):
                raise ValueError("invalid "+key)
        for key in ("host","model","effort"):
            if not isinstance(record.get(key),str) or not record[key].strip():
                raise ValueError("missing "+key)
    if record.get("validation") not in (None,"PASS","FAIL","BLOCKED"):
        raise ValueError("invalid validation")
    for key,value in record.get("telemetry",{}).items():
        if value is not None:
            source=record.get("telemetry_provenance",{}).get(key,{})
            if not all(isinstance(source.get(k),str) and source[k].strip() for k in ("source","unit","scope")):
                raise ValueError("missing telemetry provenance")
