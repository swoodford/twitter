#!/usr/bin/env python

# This script will tweet an image from the output of the df command along with the current date and time and IP-based geolocation
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

# Get report on file system disk space usage and generate image
cmd = "df -Th --exclude-type=tmpfs --exclude-type=devtmpfs | sed 's/%/\\%/g' | convert -size 800x100 -fill green -background black label:@- df.png"
console = os.popen(cmd).readline()

# Open the image
image = open('df.png', 'rb')

# Get geolocation using IP address
getlat = 'curl -s https://whatismycountry.com/ | sed -n \'s/.*Coordinates \\(.*\\)<.*/\\1/p\' | cut -d \' \' -f1'
getlong = 'curl -s https://whatismycountry.com/ | sed -n \'s/.*Coordinates \\(.*\\)<.*/\\1/p\' | cut -d \' \' -f2'

lat = os.popen(getlat).readline()
long = os.popen(getlong).readline()

lat = lat.strip()
long = long.strip()

# Tweet with image and geolocation
api.update_status_with_media(media=image, status='#RaspberryPi #Linux #filesystem #disk #usage #freespace #Twython ' + time.strftime("%c"), lat=(lat), long=(long))
