Nagios check PON in OLT Fiberhome
---
Wroted by Jorge Luiz Taioque
This plugin check status of all ONUs connected in a specific PON 
and return if these ONUs operational state is UP 


If the most part of ONUs is UP all it's OK
If all ONUs is DOWN the PON port is DOWN
and if the most part of ONUs is DOWN the PON port is WARNING

Usage:
./check_pon_fiberhome [IP_TL1] [IP_OLT] [PON_SLOT-PON_PORT]
Like:
./check_pon_fiberhome 10.10.10.1 10.10.10.2 1-1
put only the slot_number and pon_number


In nagios service.cfg use:
check_command:	check_pon_fiberhome!10.10.10.1!10.10.10.2!1-1

