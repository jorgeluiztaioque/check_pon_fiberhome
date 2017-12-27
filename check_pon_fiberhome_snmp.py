#!/usr/bin/env pythons
#-----------------------------------------------------------------------
# Nagios check PON in OLT Fiberhome
# Written by Jorge Luiz Taioque
# This plugin check status of all ONUs connected in a specific PON 
# and return if these ONUs operational state is UP or DOWN
#
# ----
# -----
# Usage:
# ./check_pon_fiberhome [IP_OLT] [PON_SLOT/PON_PORT]
# Like:
# ./check_pon_fiberhome 10.10.10.1 1/8
# put only the slot_number and pon_number before and after slash /
#
#
# In nagios service.cfg use:
# check_command:	check_pon_fiberhome!10.10.10.1!1/8
#-----------------------------------------------------------------------

#PON NAME
#--  1.3.6.1.4.1.5875.800.3.9.3.4.1.2
#		-- 1.3.6.1.4.1.5875.800.3.9.3.4.1.2
#		oltPonName OBJECT-TYPE
#			SYNTAX OCTET STRING
#			MAX-ACCESS read-only
#			STATUS current
#			DESCRIPTION
#				"Column Description"
#			::= { oltPonInfoEntry 2 }

#PON STATUS
#--  1.3.6.1.4.1.5875.800.3.9.3.4.1.5
#		-- 1.3.6.1.4.1.5875.800.3.9.3.4.1.5
#		oltPonOnlineStatus OBJECT-TYPE
#			SYNTAX Integer32
#			MAX-ACCESS read-only
#			STATUS current
#			DESCRIPTION
#				"Column Description:
#				1:occupied(1)
#				2:empty(0)"
#			::= { oltPonInfoEntry 5 }					

#PON STATUS
#--  1.3.6.1.4.1.5875.800.3.10.1.1.11
#		-- 1.3.6.1.4.1.5875.800.3.10.1.1.11
#		onuStatus OBJECT-TYPE
#			SYNTAX Integer32 (0..1)
#			MAX-ACCESS read-only
#			STATUS current
#			DESCRIPTION
#				"Description:
#				1:offonline/fiber cut/power failure(0)
#				2:online(1)"
#			::= { authOnuListEntry 11 }

#ONU LIST BY PON
#--  1.3.6.1.4.1.5875.800.3.10.1.1.3
#		-- 1.3.6.1.4.1.5875.800.3.10.1.1.3
#		authOnuListPon OBJECT-TYPE
#			SYNTAX Integer32
#			MAX-ACCESS read-only
#			STATUS current
#			DESCRIPTION
#				"Column Description"
#			::= { authOnuListEntry 3 }

__author__ = 'Jorge Luiz Taioque'
__version__= 0.1

import os
import commands
import netsnmp
import sys

olt_ip = sys.argv[1]
olt_port = sys.argv[2]

pon_name = commands.getoutput("snmpwalk -Os -c adsl -v 1 "+olt_ip+" 1.3.6.1.4.1.5875.800.3.9.3.4.1.2")

pon_name_list =  pon_name.split()

indices = 0
for i, elem in enumerate(pon_name_list):
	if olt_port in elem:
		indice = i

mib =  pon_name_list[indice-4]
mib_port = mib[-9:]

mib_status = "1.3.6.1.4.1.5875.800.3.9.3.4.1.5"

readport = commands.getoutput("snmpwalk -Os -c adsl -v 1 "+olt_ip+" "+mib_status+"."+mib_port+"")

status = readport[-1:]

status = int(status)

if status == 0:
        print 'PON is Down'
        sys.exit(2)

if  status == 1:
        print 'PON is Up'
        sys.exit(0)

	
