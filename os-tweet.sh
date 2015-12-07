#!/bin/bash
# Gather operating system details


OS1=$(cat /etc/os-release | grep 'NAME="' -m1 | cut -d '"' -f2)
OS2=$(cat /etc/os-release | grep 'VERSION="' -m1 | cut -d '"' -f2)

OS3=$(echo $OS2 | cut -d ',' -f1)
OS4=$(echo $OS2 | cut -d ',' -f2 | tr -d ' ')

echo "This #RaspberryPi is running #Linux #distro #"$OS1 $OS3 "#"$OS4
