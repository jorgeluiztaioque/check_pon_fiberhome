#!/usr/bin/python
#-----------------------------------------------------------------------
# Nagios check PON in OLT Fiberhome
# Written by Jorge Luiz Taioque
# This plugin check status of all ONUs connected in a specific PON 
# and return if these ONUs operational state is UP 
#
# ----
# If the most part of ONUs is UP all it's OK
# If all ONUs is DOWN the PON port is DOWN
# and if the most part of ONUs is DOWN the PON port is WARNING
#
# -----
# Usage:
# ./check_pon_fiberhome [IP_TL1] [IP_OLT] [PON_SLOT-PON_PORT]
# Like:
# ./check_pon_fiberhome 10.10.10.1 10.10.10.2 1-1
# put only the slot_number and pon_number
#
#
# In nagios service.cfg use:
# check_command:	check_pon_fiberhome!10.10.10.1!10.10.10.2!1-1
#-----------------------------------------------------------------------

__author__ = 'Jorge Luiz Taioque'
__version__= 0.1

import time
import sys
from socket import *

tl1host = sys.argv[1]
tl1port = 3337

oltip = sys.argv[2]
oltport = 'NA-NA-'+sys.argv[3]
datas = []

#connecting socket on TL1 service
s = socket(AF_INET, SOCK_STREAM)    
s.connect((tl1host, tl1port))
s.send('LOGIN:::CTAG::UN=1,PWD=1;')
time.sleep(4)
s.send('LST-ONUSTATE::OLTID='+oltip+',PONID='+oltport+':CTAG::;')
time.sleep(4)
data = s.recv(80000)
s.send('LOGOUT:::CTAG::;')
time.sleep(4)
s.close()

for line in data.splitlines():
	fields = line.split()
	if len(fields) >= 7:
		datas.append(fields[2])

time.sleep(4)
datas.pop(0)

time.sleep(4)
compare = len(datas)

count = 0
for test in datas:
	if test == 'LOS':
		count = count + 1

if compare == 0 and compare == count:
        print 'PON is Unconfigured'
        sys.exit(3)

if compare >= 1 and compare == count:
        print 'PON is Down'
        sys.exit(2)

if  compare >= 1 and count >= compare/2:
        print 'PON is Warning'
        sys.exit(1)

if  compare >= 1 and count <= compare/2:
        print 'PON is Up'
        sys.exit(0)
