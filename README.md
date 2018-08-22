# Nagios check PON status in OLT Fiberhome

This plugin can test all Fiberhome pon slot with 8 or 16 PONs verify with PON link status is UP or DOWN check if in that PON has customers, if have more than one customer and PON status is DOWN one alarm is generated.


## SNMP VERSION
---
Nagios check PON in OLT Fiberhome <br>
Written by Jorge Luiz Taioque <br>
This plugin check status of all ONUs connected in a specific PON  <br>
and return if these ONUs operational state is UP or DOWN <br>
----- <br>

### Dependences
<pre>
apt install libsnmp-dev snmp-mibs-downloader
apt install gcc python-dev
pip3 install easysnmp
</pre>
----- <br>
Usage: <br>
./check_pon_fiberhome [IP_OLT] [SLOT] <br>
Like: <br>
./check_pon_fiberhome 10.10.10.1 1 <br>
put only the slot_number and pon_number before and after slash / <br>
<br>
In nagios service.cfg use: <br>
check_command:	check_pon_fiberhome!10.10.10.1!1 <br>


### Configuring nagios

In nagios command.cfg use:<br>
define command{<br>
        command_name    check_pon_fiberhome<br>
        command_line    $USER1$/check_pon_fiberhome $ARG1$ $ARG2$<br>
        }<br>
