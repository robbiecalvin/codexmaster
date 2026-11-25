import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"evaluation"))
from schema import validate
from report import regressions,render

class Hardening(unittest.TestCase):
    def setUp(self):
        self.r=dict(schema_version=2,version="V2",revision="a"*40,task_id="t",attempt=1,status="NOT_RUN")
        self.config={"revisions":{"V2":"a"*40}}
    def test_valid(self): validate(self.r,self.config)
    def test_wrong_revision(self):
        with self.assertRaises(ValueError): validate(dict(self.r,revision="b"*40),self.config)
    def test_bad_version(self):
        with self.assertRaises(ValueError): validate(dict(self.r,version="V3"),self.config)
    def test_bad_attempt(self):
        with self.assertRaises(ValueError): validate(dict(self.r,attempt=True),self.config)
    def test_missing_provenance(self):
        with self.assertRaises(ValueError): validate(dict(self.r,telemetry={"input_tokens":1}),self.config)
    def test_duplicate_regression(self):
        r=dict(id="B01",version="V2",status="PASS",synthetic=False)
        with self.assertRaises(ValueError): regressions([r,r],[])
    def test_separate_versions(self):
        r=dict(id="B01",version="V2",status="PASS",synthetic=False)
        data,_=render([r])
        self.assertEqual(data["by_version"]["V2"]["counts"]["PASS"],1)
        self.assertEqual(data["by_version"]["V1"]["counts"]["PASS"],0)
    def test_invalid_nested(self):
        with self.assertRaises(ValueError): validate(dict(self.r,evidence=[1]),self.config)
    def test_invalid_telemetry_container(self):
        with self.assertRaises(ValueError): validate(dict(self.r,telemetry=[]),self.config)
if __name__=="__main__": unittest.main()
