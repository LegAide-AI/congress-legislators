# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "lxml==6.1.3",
#   "PyYAML==6.0.3",
#   "pytz==2026.4",
#   "rtyaml==1.0.0",
#   "scrapelib==0.10.1",
# ]
# ///

# Just loads and saves each .yaml file to normalize serialization syntax.
#
# uv run lint.py
# ... will lint every .yaml file in the data directory.
#
# uv run lint.py file1.yaml file2.yaml ...
# ... will lint the specified files.

import glob, sys
from utils import yaml_load, yaml_dump, data_dir

def run():
    for fn in glob.glob(data_dir() + "/*.yaml") if len(sys.argv) == 1 else sys.argv[1:]:
        print(fn + "...")
        data = yaml_load(fn, use_cache=False)
        yaml_dump(data, fn)

if __name__ == '__main__':
  run()
