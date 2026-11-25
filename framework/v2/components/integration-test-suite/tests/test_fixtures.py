import sys
import json
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"evaluation"))
from fixtures import provision
from runner import catalog
class Fixtures(unittest.TestCase):
    def test_coverage(self):
        self.assertEqual(len(catalog()),38)
        self.assertEqual(len({r["family"] for r in catalog()}),8)
    def test_reproducible(self):
        with tempfile.TemporaryDirectory() as parent:
            for item in catalog():
                a,x=provision(item,parent)
                b,y=provision(item,parent)
                self.assertNotEqual(a,b)
                self.assertEqual(x,y)
                self.assertTrue(x["files"])
    def test_isolation(self):
        with tempfile.TemporaryDirectory() as parent:
            a,x=provision(catalog()[0],parent)
            b,y=provision(catalog()[0],parent)
            name=next(iter(x["files"]))
            (a/name).write_text("changed")
            self.assertNotEqual((a/name).read_bytes(),(b/name).read_bytes())
if __name__=="__main__": unittest.main()
