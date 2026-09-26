# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML==6.0.3"]
# ///

"""List manual committee addendum keys already identical to scraped data."""

import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def find_redundant_keys(primary, addendum):
    return sorted(key for key, value in addendum.items() if primary.get(key) == value)


def load_yaml(path):
    with path.open() as data_file:
        return yaml.safe_load(data_file)


def run():
    primary = load_yaml(ROOT / "committee-membership-current.yaml")
    addendum = load_yaml(ROOT / "committee-membership-manual-addendum.yaml")
    print(json.dumps(find_redundant_keys(primary, addendum)))


if __name__ == "__main__":
    run()
