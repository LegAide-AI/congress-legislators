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

# Update current cspan IDs using NYT Congress API.

import json, urllib.request, urllib.parse, urllib.error
from utils import load_data, save_data

def run():
    # load in current members
    y = load_data("legislators-current.yaml")
    for m in y:
        # retrieve C-SPAN id, if available, from ProPublica API
        # TODO: use utils.download here
        response = urllib.request.urlopen("https://projects.propublica.org/represent/api/v1/members/%s.json" % m['id']['bioguide']).read()
        j = json.loads(response.decode("utf8"))
        cspan = j['results'][0]['cspan_id']
        if not cspan == '':
            m['id']['cspan'] = int(cspan)
    save_data(y, "legislators-current.yaml")

if __name__ == '__main__':
  run()
