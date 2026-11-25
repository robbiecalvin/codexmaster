"""Generate escaped, static reports from validated records."""
import json
from html import escape
from metrics import summarize, score, telemetry

MATCH = ("id", "pair_id", "model", "effort", "host", "fixture_hash", "prompt_hash", "permissions_hash", "criteria_hash")

def compare(records):
    groups = {}
    for r in records:
        if r.get("synthetic") is False and r.get("pair_id"):
            groups.setdefault(r["pair_id"], []).append(r)
    pairs = []
    for key, group in sorted(groups.items()):
        if len(group) != 2 or {r.get("version") for r in group} != {"V1","V2"}:
            continue
        a,b = sorted(group, key=lambda r:r["version"])
        if not all(a.get(k) and a[k] == b.get(k) for k in MATCH):
            continue
        x,y = telemetry(a),telemetry(b)
        pairs.append({"pair_id":key,"id":a["id"],"v1_status":a["status"],"v2_status":b["status"],
                      "score_delta":score(b)-score(a) if a["status"] == b["status"] == "PASS" and score(a) is not None and score(b) is not None else None,
                      "telemetry_delta":{k:y[k]-x[k] if x[k] is not None and y[k] is not None else None for k in x}})
    return pairs

def regressions(old, new):
    def index(records):
        result = {}
        for r in records:
            if r.get("synthetic") is not False:
                continue
            key = (r["id"],r.get("version"))
            if key in result:
                raise ValueError("ambiguous regression input")
            result[key] = r
        return result
    baseline,current = index(old),index(new)
    return [list(k) for k,r in baseline.items() if r["status"]=="PASS" and
            (k not in current or current[k]["status"]!="PASS" or
             (score(r) is not None and (score(current[k]) is None or score(current[k]) < score(r))))]

def render(records):
    data = {"summary":summarize(records),"by_version":{v:summarize([r for r in records if r.get("version")==v]) for v in ("V1","V2")},"matched_pairs":compare(records)}
    html = '<!doctype html><meta charset="utf-8"><title>CodexMaster evaluation</title><h1>CodexMaster evaluation</h1><p>Observed records only; missing data is null.</p><pre>'+escape(json.dumps(data,indent=2))+'</pre>'
    return data,html
