# Nagios check PON status in OLT Fiberhome

This plugin can test all Fiberhome pon slot with 8 or 16 PONs if PON link status is UP or DOWN

The plugin check if in all PONs of a specific SLOT has customers, if a PON port have one or more customers and PON status is DOWN one alarm is generated.

---
#### Nagios check PON in OLT Fiberhome <br>
Written by Jorge Luiz Taioque <br>
This plugin check status of a PON Slot connected in a specific OLT  <br>
and return if these PON operational state is UP or DOWN <br>


### Dependences
<pre>
apt install libsnmp-dev snmp-mibs-downloader
apt install gcc python-dev
pip3 install easysnmp
</pre>
----- <br>
### Usage: <br>
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
