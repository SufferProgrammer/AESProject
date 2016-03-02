#!/usr/bin/python

import sys
import os

print "\nAESPro system installation.\
\nplease input your's root password for install necessary parts\n\
\nupdating your's system,\
and install all necessary parts for use GUI mode.\
\nPlease wait a minute...\n"
os.system("sudo apt-get update")
os.system("sudo python sip.py")
