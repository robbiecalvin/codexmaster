import sys
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"evaluation"))
from evidence import verify
class Evidence(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        (self.root/"trace").write_text("fixture trace")
        self.r=dict(id="B01",run_id="r",revision="a"*40,host="test",reviewer="reviewer",review_notes="checked",status="PASS",independent_review=True,schema_version=2,evidence=[dict(path="trace",kind="trace",sha256=hashlib.sha256((self.root/"trace").read_bytes()).hexdigest())],assertions=[dict(criterion="outcome",status="PASS",evidence_paths=["trace"])])
    def test_valid(self): verify(self.r,self.root)
    def test_missing_assertion(self):
        self.r["assertions"]=[]
        with self.assertRaises(ValueError): verify(self.r,self.root)
    def test_wrong_reference(self):
        self.r["assertions"][0]["evidence_paths"]=["absent"]
        with self.assertRaises(ValueError): verify(self.r,self.root)
    def test_wrong_kind(self):
        with self.assertRaises(ValueError): verify(self.r,self.root,[dict(id="outcome",evidence_kinds=["review"])])
    def test_duplicate_criterion(self):
        self.r["assertions"]*=2
        with self.assertRaises(ValueError): verify(self.r,self.root,[dict(id="outcome",evidence_kinds=["trace"])])
    def test_tampered(self):
        (self.root/"trace").write_text("changed")
        with self.assertRaises(ValueError): verify(self.r,self.root)
    def test_no_independent_review(self):
        self.r["independent_review"]=False
        with self.assertRaises(ValueError): verify(self.r,self.root)
    def test_missing_file(self):
        (self.root/"trace").unlink()
        with self.assertRaises(ValueError): verify(self.r,self.root)
    def test_duplicate_evidence(self):
        self.r["evidence"]*=2
        with self.assertRaises(ValueError): verify(self.r,self.root)
    def test_snapshot_check(self):
        path=self.root/"snapshot"
        criteria=[dict(id="outcome",evidence_kinds=["snapshot"],check="unchanged_snapshot")]
        self.r["assertions"][0]["evidence_paths"]=["snapshot"]
        for changed in (False,True):
            path.write_text(json.dumps({"before":{"a":"a"*64},"after":{"a":("b" if changed else "a")*64}}))
            self.r["evidence"]=[dict(path="snapshot",kind="snapshot",sha256=hashlib.sha256(path.read_bytes()).hexdigest())]
            if changed:
                with self.assertRaises(ValueError): verify(self.r,self.root,criteria)
            else: verify(self.r,self.root,criteria)
if __name__=="__main__": unittest.main()
