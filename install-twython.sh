#!/bin/bash
# This script installs Twython on Raspberry Pi
# https://github.com/ryanmcgrath/twython

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install -y python-setuptools python3-oauth python3-oauth2client python3-oauthlib python3-requests-oauthlib
sudo easy_install pip
sudo pip install --upgrade twython

python -c "import twython" && echo "Twython Installed." || echo "Failure installing Twython."
