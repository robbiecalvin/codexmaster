"""Existing six-category rubric; no inferred telemetry."""
from statistics import mean
import math

FIELDS = ("input_tokens", "output_tokens", "cached_tokens", "reasoning_tokens",
          "tool_calls", "file_inspections", "unique_files", "corrections",
          "elapsed_seconds", "human_interventions")

def score(record):
    ratings = record.get("ratings", [])
    if (record.get("validation") != "PASS" or len(ratings) != 6
        or any(type(x) is not int or x not in (0, 1, 2) for x in ratings)
        or ratings[0] != 2 or ratings[5] != 2
        or not all(isinstance(x, str) and x.strip() for x in record.get("rating_rationales", []))
        or len(record.get("rating_rationales", [])) != 6):
        return None
    return sum(ratings)

def telemetry(record):
    result = {}
    for key in FIELDS:
        value = record.get("telemetry", {}).get(key)
        if value is not None and (type(value) not in (int, float) or not math.isfinite(value) or value < 0 or (key != "elapsed_seconds" and type(value) is not int)):
            raise ValueError("invalid telemetry: " + key)
        result[key] = value
    return result

def summarize(records):
    real = [r for r in records if r.get("synthetic") is False]
    scores = [s for r in real if r["status"] == "PASS" and (s := score(r)) is not None]
    measurements = [telemetry(r) for r in real]
    return {"counts": {s: sum(r["status"] == s for r in real) for s in ("PASS","FAIL","BLOCKED","NOT_RUN")},
            "eligible_count": len(scores), "mean_score": mean(scores) if scores else None,
            "telemetry": {k: {"count": len(v), "mean": mean(v) if v else None}
                          for k in FIELDS if (v := [m[k] for m in measurements if m[k] is not None]) is not None}}
