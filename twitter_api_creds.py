#!/usr/bin/env python
# This script sets Twitter API credentials

import os

os.environ["CONSUMER_KEY"] = "YOUR KEY HERE"
os.environ["CONSUMER_SECRET"] = "YOUR KEY HERE"
os.environ["ACCESS_KEY"] = "YOUR KEY HERE"
os.environ["ACCESS_SECRET"] = "YOUR KEY HERE"

if os.environ["CONSUMER_KEY"] == "YOUR KEY HERE":
    print "You failed to configure your Twitter API credentials in the file twitter_api_creds.py!"
    exit()
else:
    pass
