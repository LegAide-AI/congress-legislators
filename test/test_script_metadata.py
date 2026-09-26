# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

"""Ensure maintained command-line scripts remain directly runnable with uv."""

import tomllib
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_LIBRARY_FILES = {"utils.py"}


def inline_metadata(path):
    lines = path.read_text().splitlines()
    start = lines.index("# /// script")
    end = lines.index("# ///", start + 1)
    return tomllib.loads("\n".join(line.removeprefix("# ") for line in lines[start + 1:end]))


class TestScriptMetadata(unittest.TestCase):
    def test_all_runnable_scripts_have_pinned_inline_dependencies(self):
        scripts = sorted((ROOT / "scripts").glob("*.py"))

        for script in scripts:
            if script.name in SCRIPT_LIBRARY_FILES:
                continue
            with self.subTest(script=script.name):
                metadata = inline_metadata(script)
                self.assertEqual(metadata["requires-python"], ">=3.11")
                self.assertTrue(
                    all("==" in dependency for dependency in metadata["dependencies"]),
                    "direct dependencies must be pinned",
                )


if __name__ == "__main__":
    unittest.main()
