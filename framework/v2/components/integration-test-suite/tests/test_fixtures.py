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
    def test_benchmark_sources(self):
        from fixtures import material
        items={r["id"]:r for r in catalog()}
        for scenario,name in (("P02","caller.py"),("P04","auth.py"),("P07","test_parser.py"),("P09","unrelated.py")):
            self.assertIn(name,material(items[scenario])[0])
    def test_unknown_retry(self):
        from fixtures import material
        item=next(r for r in catalog() if r["id"]=="B16")
        self.assertIsNone(json.loads(material(item)[0]["retry.json"])["attempts"])
    def test_specific_inputs(self):
        from fixtures import material
        items={r["id"]:r for r in catalog()}
        for scenario,name in (("B01","arithmetic.py"),("B07","critic.json"),("B11","required-check.json"),("B19","release-check.py"),("B27","host-requirements.json")):
            self.assertIn(name,material(items[scenario])[0])
    def test_benchmark_prompt_excludes_acceptance(self):
        from fixtures import material
        item=next(r for r in catalog() if r["id"]=="P01")
        self.assertNotIn(item["acceptance"],material(item)[1]["prompt"])
if __name__=="__main__": unittest.main()
