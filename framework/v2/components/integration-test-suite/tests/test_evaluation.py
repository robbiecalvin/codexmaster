import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"evaluation"))
from runner import catalog
from evidence import verify
from metrics import score, summarize, telemetry
from report import compare, regressions, render

class Evaluation(unittest.TestCase):
    def test_coverage(self):
        original=json.loads((ROOT/"scenarios/behavioral.json").read_text())
        items=catalog()
        self.assertEqual(len(items),38)
        self.assertEqual(len({r["id"] for r in items}),38)
        self.assertEqual([(r["id"],r["expected"]) for r in items[:28]],[(r["id"],r["expected"]) for r in original])
    def test_evidence(self):
        r=dict(id="B01",run_id="1",revision="abc",host="test",reviewer="human",review_notes="checked",status="PASS",independent_review=True)
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError): verify(r,d)
            p=Path(d)/"trace";p.write_text("synthetic")
            r["evidence"]=[dict(path="trace",sha256=hashlib.sha256(p.read_bytes()).hexdigest())]
            verify(r,d)
            p.write_text("changed")
            with self.assertRaises(ValueError): verify(r,d)
    def test_metrics(self):
        r=dict(validation="PASS",ratings=[2]*6,rating_rationales=["evidence"]*6)
        self.assertEqual(score(r),12)
        r["ratings"][0]=1
        self.assertIsNone(score(r))
        self.assertIsNone(telemetry({})["input_tokens"])
        with self.assertRaises(ValueError): telemetry({"telemetry":{"input_tokens":-1}})
    def test_synthetic(self):
        self.assertEqual(summarize([dict(status="PASS",synthetic=True)])["counts"]["PASS"],0)
        self.assertIsNone(render([])[0]["summary"]["mean_score"])
    def test_regression(self):
        r=dict(id="B01",version="V2",status="PASS",synthetic=False)
        self.assertEqual(regressions([r],[dict(r,status="FAIL")]),[["B01","V2"]])
        self.assertEqual(regressions([r],[]),[["B01","V2"]])
    def test_matching(self):
        r=dict(id="P01",pair_id="p",model="m",effort="e",host="h",fixture_hash="f",prompt_hash="p",permissions_hash="a",criteria_hash="c",synthetic=False,status="PASS",version="V1")
        self.assertEqual(len(compare([r,dict(r,version="V2")])),1)
        self.assertEqual(compare([r,dict(r,version="V2",model="other")]),[])

    def test_mixed_summary(self):
        records=[dict(status="PASS",synthetic=False,version=v) for v in ("V1","V2")]
        self.assertIsNone(render(records)[0]["summary"])
    def test_unknown_measurement(self):
        self.assertIsNone(summarize([])["telemetry"]["input_tokens"]["mean"])
    def test_invalid_boolean(self):
        with self.assertRaises(ValueError): telemetry({"telemetry":{"input_tokens":True}})
    def test_invalid_fraction(self):
        with self.assertRaises(ValueError): telemetry({"telemetry":{"tool_calls":1.5}})
    def test_attempt_count(self):
        r=dict(id="P01",task_id="t",status="FAIL",synthetic=False)
        self.assertEqual(summarize([r,r])["task_count"],1)
        self.assertEqual(summarize([r,r])["attempt_count"],2)
    def test_dashboard(self):
        _,html=render([])
        self.assertIn("<table>",html)
        self.assertNotIn("<pre>",html)

if __name__=="__main__": unittest.main(verbosity=2)
