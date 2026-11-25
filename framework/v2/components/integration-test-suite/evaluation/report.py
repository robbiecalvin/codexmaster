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
    data = {"summary":summarize(records) if len({r.get("version") for r in records if r.get("synthetic") is False})<=1 else None,"by_version":{v:summarize([r for r in records if r.get("version")==v]) for v in ("V1","V2")},"matched_pairs":compare(records)}
    def cell(value):
        return escape("Unknown" if value is None else str(value))
    html = '<!doctype html><html lang="en"><meta charset="utf-8"><title>CodexMaster evaluation</title><style>body{font:16px system-ui;margin:2rem;max-width:1000px}table{border-collapse:collapse;width:100%;margin-bottom:2rem}td,th{border:1px solid #888;padding:.5rem;text-align:left}caption{text-align:left;font-weight:bold}meter{width:8rem}</style><h1>CodexMaster evaluation</h1><p>Observed records only. Unknown measurements are not zero. Synthetic records excluded.</p>'
    for version,summary in data["by_version"].items():
        html += '<h2>'+version+'</h2><table><caption>Outcomes and quality</caption><tr><th>Measure</th><th>Value</th></tr>'
        for k,v in {**summary["counts"],**{k:summary[k] for k in ("task_count","attempt_count","eligible_count","ineligible_count","mean_score")}}.items():
            html += '<tr><td>'+cell(k)+'</td><td>'+cell(v)+'</td></tr>'
        html += '</table><table><caption>Telemetry</caption><tr><th>Measure</th><th>Samples</th><th>Mean</th></tr>'
        for k,v in summary["telemetry"].items():
            html += '<tr><td>'+cell(k)+'</td><td>'+cell(v["count"])+'</td><td>'+cell(v["mean"])+'</td></tr>'
        html += '</table>'
    html += '<h2>Matched comparisons</h2><table><tr><th>Pair</th><th>Scenario</th><th>V1</th><th>V2</th><th>Score delta</th></tr>'
    for pair in data["matched_pairs"]:
        html += '<tr>'+''.join('<td>'+cell(pair[k])+'</td>' for k in ("pair_id","id","v1_status","v2_status","score_delta"))+'</tr>'
    html += '</table></html>'
    return data,html
