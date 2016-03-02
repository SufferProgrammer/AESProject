#!/usr/bin/python

import os
import sys

print "update system repository and running apt-get update please wait a momment..."
os.system("sudo apt-get update")
os.system("sudo apt-get install php5 phpmyadmin mysql-server")
