#!/bin/bash
# Gather operating system details

OS=$(cat /etc/os-release)

OS1=$(echo "$OS" | grep ^NAME= | cut -d '"' -f2)
OS2=$(echo "$OS" | grep 'VERSION="' -m1 | cut -d '(' -f2 | rev | cut -d ')' -f2 | rev)
OS3=$(echo "$OS" | grep ID_LIKE= | cut -d '=' -f2)

echo "This #RaspberryPi is running #Linux #distro #"$OS1 "#"$OS2 "#"$OS3
