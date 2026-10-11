#!/usr/bin/env python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "lxml==6.1.3",
#   "PyYAML==6.0.3",
#   "pytz==2026.4",
#   "requests==2.34.2",
#   "rtyaml==1.0.0",
#   "scrapelib==0.10.1",
#   "SPARQLWrapper==2.0.0",
#   "termcolor==3.3.0",
# ]
# ///

import sys
import glob
import os
import importlib

sys.path.append("scripts")

scripts = glob.glob("scripts/*.py")
scripts.sort()

for script in scripts:
    module = os.path.basename(script).replace(".py", "")
    print("Importing %s..." % module)

    try:
        importlib.import_module(module)
    except Exception as exc:
        print("Error when importing %s!" % module)
        print()
        raise exc

exit(0)
