import pathlib
import tomllib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

class GovernanceTests(unittest.TestCase):
    def test_truth_constraints(self):
        config = tomllib.loads((ROOT / "config.toml").read_text())
        for key in ("no_hallucinations", "no_fake_apis", "explicitly_mark_unknowns", "reject_unverifiable_claims"):
            self.assertIs(config["truth"][key], True)

    def test_repository_and_testing_constraints(self):
        config = tomllib.loads((ROOT / "config.toml").read_text())
        self.assertTrue(config["repository"]["read_before_edit"])
        self.assertTrue(config["testing"]["tests_must_be_deterministic"])
        self.assertTrue(config["testing"]["avoid_network_in_tests"])

    def test_reference_documents_exist(self):
        for path in ("docs/AGENTS.md", "docs/development/modular_agents.md", "docs/development/launch_acceptance.md"):
            self.assertTrue((ROOT / path).is_file(), path)
