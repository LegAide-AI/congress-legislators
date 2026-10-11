# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML==6.0.3"]
# ///

"""Tests for the authoritative redundant-addendum pre-check."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from redundant_addendum_keys import find_redundant_keys


class TestRedundantAddendumKeys(unittest.TestCase):
    def test_only_identical_overrides_are_redundant(self):
        primary = {"AA": [{"rank": 1}], "BB": [{"rank": 2}], "CC": []}
        addendum = {"AA": [{"rank": 1}], "BB": [{"rank": 3}], "DD": []}

        self.assertEqual(find_redundant_keys(primary, addendum), ["AA"])


if __name__ == "__main__":
    unittest.main()
