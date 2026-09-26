# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "lxml==6.1.3",
#   "pyflakes==4.0.0",
#   "PyYAML==6.0.3",
#   "pytz==2026.4",
#   "requests==2.34.2",
#   "rtyaml==1.0.0",
#   "scrapelib==0.10.1",
#   "SPARQLWrapper==2.0.0",
#   "termcolor==3.3.0",
# ]
# ///

"""Run the repository's CI-equivalent Python checks."""

import subprocess
import sys


COMMANDS = (
    (sys.executable, "test/workout.py"),
    (sys.executable, "-m", "unittest", "discover", "-s", "test", "-p", "test_*.py"),
    (sys.executable, "-m", "pyflakes", "."),
    (sys.executable, "test/are_files_linted.py"),
    (sys.executable, "test/validate.py"),
)


for command in COMMANDS:
    subprocess.run(command, check=True)
