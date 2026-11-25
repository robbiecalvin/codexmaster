import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
V2 = ROOT / "framework/v2"

class Activation(unittest.TestCase):
    def test_native_entries(self):
        registry = json.loads((V2 / "components/master-agent-registry/registry.json").read_text())
        ids = [s["id"] for s in registry["skills"]]
        self.assertEqual(len(set(ids)), 34)
        native = ROOT / ".agents/skills"
        self.assertEqual({p.name for p in native.iterdir()}, set(ids))
        for name in ids:
            p = native / name
            self.assertTrue(p.is_symlink())
            self.assertEqual(p.resolve(), (V2 / "skills" / name).resolve())
            self.assertTrue((p / "SKILL.md").is_file())

    def test_negative_integrity(self):
        import shutil
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "v2"
            shutil.copytree(V2, copy)
            def check():
                return subprocess.run([sys.executable, str(copy / "verify_manifest.py")], capture_output=True).returncode
            self.assertEqual(check(), 0)
            p = copy / "MIGRATION.md"
            original = p.read_bytes()
            p.write_bytes(original + b"tampered")
            self.assertNotEqual(check(), 0)
            p.unlink()
            self.assertNotEqual(check(), 0)

    def test_bootstrap(self):
        self.assertIn("framework/v2/AGENTS.md", (ROOT / "AGENTS.md").read_text())
        for path, name in [("docs/workflow/task_router.md", "task-router"), ("docs/workflow/workflow_engine.md", "workflow-engine"), ("docs/strategy/metrics.md", "metrics")]:
            self.assertIn("historical comparison only", (ROOT / path).read_text())
            self.assertIn("framework/v2/skills/" + name + "/SKILL.md", (ROOT / path).read_text())

if __name__ == "__main__":
    unittest.main()
