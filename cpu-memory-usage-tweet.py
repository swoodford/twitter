#!/usr/bin/env python

# This script will tweet an image from the output of the top command along with the current date and time and IP-based geolocation
# Requires ImageMagick, Twython, API credentials set as env vars

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

# Get report from top with cpu and memory usage and generate image
cmd = "top -b -n 1 | head -n 5 | sed 's/%/\\%/g' | convert -size 600x100 -fill green -background black label:@- top.png"
console = os.popen(cmd).readline()

# Open the image
image = open('top.png', 'rb')

# Get geolocation using IP address
getlat = 'curl -s http://whatismycountry.com/ | sed -n \'s/.*Coordinates \\(.*\\)<.*/\\1/p\' | cut -d \' \' -f1'
getlong = 'curl -s http://whatismycountry.com/ | sed -n \'s/.*Coordinates \\(.*\\)<.*/\\1/p\' | cut -d \' \' -f2'

lat = os.popen(getlat).readline()
long = os.popen(getlong).readline()

lat = lat.strip()
long = long.strip()

# Tweet with image and geolocation
api.update_status_with_media(media=image, status='#RaspberryPi #Linux #cpu #memory #usage #uptime #Twython ' + time.strftime("%c"), lat=(lat), long=(long))
