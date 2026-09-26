#!/usr/bin/env python
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

# "Un-retire" a Member of Congress: Move a Member of Congress
# from the legislators-historical file to the legislators-current file
# and give the Member a new term.
#
# uv run untire.py bioguideID

import sys
import rtyaml
import utils
from collections import OrderedDict

def run():

	if len(sys.argv) != 2:
		print("Usage:")
		print("uv run untire.py bioguideID")
		sys.exit()

	print("Loading current YAML...")
	y = utils.load_data("legislators-current.yaml")
	print("Loading historical YAML...")
	y1 = utils.load_data("legislators-historical.yaml")

	for moc in y1:
		if moc["id"].get("bioguide", None) != sys.argv[1]: continue

		print("Updating:")
		rtyaml.pprint(moc["id"])
		print()
		rtyaml.pprint(moc["name"])

		moc["terms"].append(OrderedDict([
			("type", moc["terms"][-1]["type"]),
			("start", None),
			("end", None),
			("state", moc["terms"][-1]["state"]),
			("party", moc["terms"][-1]["party"]),
		]))

		y1.remove(moc)
		y.append(moc)

		break

	print("Saving changes...")
	utils.save_data(y, "legislators-current.yaml")
	utils.save_data(y1, "legislators-historical.yaml")

if __name__ == '__main__':
  run()
