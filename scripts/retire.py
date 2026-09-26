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

# Retire a Member of Congress. Updates the end date of the
# Member's most recent term and moves him/her from the
# current file to the historical file.
#
# uv run retire.py bioguideID termEndDate

import sys
import utils
import rtyaml

def run():
	if len(sys.argv) != 3:
		print("Usage:")
		print("uv run retire.py bioguideID termEndDate")
		sys.exit()

	try:
		utils.parse_date(sys.argv[2])
	except:
		print("Invalid date: ", sys.argv[2])
		sys.exit()

	print("Loading current YAML...")
	y = utils.load_data("legislators-current.yaml")
	print("Loading historical YAML...")
	y1 = utils.load_data("legislators-historical.yaml")

	for moc in y:
		if moc["id"].get("bioguide", None) != sys.argv[1]: continue

		print("Updating:")
		rtyaml.pprint(moc["id"])
		print()
		rtyaml.pprint(moc["name"])
		print()
		rtyaml.pprint(moc["terms"][-1])

		moc["terms"][-1]["end"] = sys.argv[2]

		y.remove(moc)
		y1.append(moc)

		break

	print("Saving changes...")
	utils.save_data(y, "legislators-current.yaml")
	utils.save_data(y1, "legislators-historical.yaml")

if __name__ == '__main__':
  run()
