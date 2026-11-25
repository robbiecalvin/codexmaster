"""Strict record and revision validation for offline evaluation."""
import re
from metrics import FIELDS, telemetry

def digest(value):
    return isinstance(value,str) and re.fullmatch(r"[0-9a-f]{64}",value) is not None

def validate(record, config):
    if not isinstance(record,dict) or type(record.get("schema_version")) is not int or record["schema_version"] != 2:
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
    for key in ("telemetry","telemetry_provenance"):
        if not isinstance(record.get(key,{}),dict):
            raise ValueError("invalid "+key)
    for key in ("evidence","assertions","ratings","rating_rationales"):
        if not isinstance(record.get(key,[]),list):
            raise ValueError("invalid "+key)
    ratings=record.get("ratings",[])
    if ratings and (len(ratings)!=6 or any(x is not None and (type(x) is not int or x not in (0,1,2)) for x in ratings)):
        raise ValueError("invalid ratings")
    rationales=record.get("rating_rationales",[])
    if rationales and (len(rationales)!=6 or not all(isinstance(x,str) and x.strip() for x in rationales)):
        raise ValueError("invalid rating rationales")
    if set(record.get("telemetry",{}))-set(FIELDS) or set(record.get("telemetry_provenance",{}))-set(FIELDS):
        raise ValueError("unknown telemetry field")
    telemetry(record)
    for item in record.get("evidence",[]):
        if not isinstance(item,dict) or not isinstance(item.get("path"),str) or not item["path"].strip() or item.get("kind") not in ("review","trace","snapshot","test","artifact") or not digest(item.get("sha256")):
            raise ValueError("invalid evidence item")
    for item in record.get("assertions",[]):
        if not isinstance(item,dict) or not isinstance(item.get("criterion"),str) or item.get("status") not in ("PASS","FAIL","BLOCKED") or not isinstance(item.get("evidence_paths"),list) or not all(isinstance(x,str) for x in item["evidence_paths"]):
            raise ValueError("invalid assertion")
    for key,value in record.get("telemetry",{}).items():
        if value is not None:
            source=record.get("telemetry_provenance",{}).get(key,{})
            if not isinstance(source,dict) or not all(isinstance(source.get(k),str) and source[k].strip() for k in ("source","unit","scope")):
                raise ValueError("missing telemetry provenance")
