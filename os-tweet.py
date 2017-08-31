#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script will tweet your current Raspberry Pi OS version details
# Requires Twython, API credentials set as env vars

import os
import time
from twython import Twython
import twitter_api_creds

# Set Credentials from environment variables
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_KEY = os.getenv("ACCESS_KEY")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

cmd = 'bash os-tweet.sh'
osdetails = os.popen(cmd).readline()
cmd2 = 'date'
time = os.popen(cmd2).readline()

# Get geolocation using IP address
getlat = 'curl -s https://whatismycountry.com/ | sed -n \'s/.*Coordinates \\(.*\\)<.*/\\1/p\' | cut -d \' \' -f1'
getlong = 'curl -s https://whatismycountry.com/ | sed -n \'s/.*Coordinates \\(.*\\)<.*/\\1/p\' | cut -d \' \' -f2'

lat = os.popen(getlat).readline()
long = os.popen(getlong).readline()

lat = lat.strip()
long = long.strip()

# Tweet with OS details, date, time and ip-geolocation
api.update_status(status=osdetails + ' as of ' + time + '', lat=(lat), long=(long))
