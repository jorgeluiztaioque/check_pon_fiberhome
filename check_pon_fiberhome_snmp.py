#!/usr/bin/env python3
#-----------------------------------------------------------------------
# Nagios check PON in OLT Fiberhome
# Written by Jorge Luiz Taioque
# This plugin check status of all ONUs connected in a specific PON
# and return if these ONUs operational state is UP or DOWN
#
# ----
# -----
# Usage:
# ./check_pon_fiberhome [IP_OLT] [SLOT]
# Like:
# ./check_pon_fiberhome 10.10.10.1 1
#
#
# In nagios service.cfg use:
# check_command:	check_pon_fiberhome!10.10.10.1!1
#-----------------------------------------------------------------------

__author__ = 'Jorge Luiz Taioque'
__version__= 1.0

from easysnmp import Session
import sys

olt_ip = sys.argv[1]
olt_port = sys.argv[2]

#Alarm only PON ports that has more than this value (variable [alarm] value)
alarm = 2

snmpSession = Session(hostname=olt_ip, community='adsl', version=2)

mib_status = "1.3.6.1.4.1.5875.800.3.9.3.4.1.5"
mib_onu_pon_num = "1.3.6.1.4.1.5875.800.3.9.3.4.1.12"

pon_name_list = snmpSession.walk('1.3.6.1.4.1.5875.800.3.9.3.4.1.2')

indice = []
for j in range(1,17):
	for i, elem in enumerate(pon_name_list):
		if olt_port+"/"+str(j)+"\'" == str(elem).split()[2]:
			indice.append(i)

key = 0
result = {}
for i in indice:
	key = key+1
	mib_port = str(pon_name_list[i]).split()[3][41:][:-2]
	readport = snmpSession.get(mib_status+"."+mib_port)
	ponNumOnu = snmpSession.get(mib_onu_pon_num+"."+mib_port)

	status_pon = str(readport).split()[1][-2:-1]
	numOnu = str(ponNumOnu).split()[1][7:-1]
	result.update({key:[status_pon,numOnu]})

port_down = []
for i in range(1,len(result)+1):
        if int(result[i][0]) == 0 and int(result[i][1]) > alarm:
                port_down.append(i)

if len(port_down) >= 1:
        print ("Slot "+olt_port+" PONs "+str(port_down)+" Down")
        sys.exit(2)

if not port_down:
        if not indice:
                print ("Slot not exist")
        else:
                print ("Slot "+olt_port+" PONs is Up")
                sys.exit(0)
