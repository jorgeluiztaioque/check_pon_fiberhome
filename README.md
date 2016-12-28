Nagios check PON status in OLT Fiberhome
---

SNMP VERSION
---
Nagios check PON in OLT Fiberhome <br>
Written by Jorge Luiz Taioque <br>
This plugin check status of all ONUs connected in a specific PON  <br>
and return if these ONUs operational state is UP or DOWN <br>
----- <br>
Usage: <br>
./check_pon_fiberhome [IP_OLT] [PON_SLOT/PON_PORT] <br>
Like: <br>
./check_pon_fiberhome 10.10.10.1 1/8 <br>
put only the slot_number and pon_number before and after slash / <br>
<br>
In nagios service.cfg use: <br>
check_command:	check_pon_fiberhome!10.10.10.1!1/8 <br>


Configuring nagios
----
In nagios command.cfg use:<br>
define command{<br>
        command_name    check_pon_fiberhome<br>
        command_line    $USER1$/check_pon_fiberhome $ARG1$ $ARG2$<br>
        }<br>


TL1 VERSION
---
Written by Jorge Luiz Taioque<br>
This plugin check status of all ONUs connected in a specific PON <br>
and return if these ONUs operational state is UP <br>
<br>
<br>
How plugin the compare nagios status?<br>
If the most part of ONUs is UP all it's OK<br>
If all ONUs is DOWN the PON port is DOWN<br>
and if the most part of ONUs is DOWN the PON port is WARNING<br>
<br>
<br>
Usage:<br>
./check_pon_fiberhome [IP_TL1] [IP_OLT] [PON_SLOT-PON_PORT]<br>
Like:<br>
./check_pon_fiberhome 10.10.10.1 10.10.10.2 1-1<br>
put only the slot_number and pon_number<br>
<br>
In nagios service.cfg use:<br>
check_command:	check_pon_fiberhome!10.10.10.1!10.10.10.2!1-1<br>

Configuring nagios
----
In nagios command.cfg use:<br>
define command{<br>
        command_name    check_pon_fiberhome<br>
        command_line    $USER1$/check_pon_fiberhome $ARG1$ $ARG2$ $ARG3$<br>
        }<br>




