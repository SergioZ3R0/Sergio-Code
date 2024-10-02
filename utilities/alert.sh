#!/bin/bash

LOG_FILE="/var/log/syslog"
ALERT_EMAIL="ejemplo@falso.eje"
SUBSPICIOUS_IPS="/tmp/suspicious_ips"
THRESHOLD=5

#Search for suspicious IPs connecting to the server on $LOG_FILE

grep "Failed password" $LOG_FILE | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr | awk -v threshold=$THRESHOLD '$1 > threshold {print $2}' > $SUSPICIOUS_IPS

if [ -s $SUSPICIOUS_IPS ]; then
    cat $SUSPICIOUS_IPS
    #Check if IP complete the threshold
    while read IP; do
      count=$(grep $IP $LOG_FILE | wc -l)
      ip=$(grep $IP $LOG_FILE | head -n 1 | awk '{print $(NF-3)}')
      geoIP=$(geoiplookup $IP)
      if [ "$count" -gt "$THRESHOLD" ]; then
        geoiplookup $IP
      fi
      if [ "$count" -gt "$THRESHOLD" ]; then
        mail -s "Alerta IP encontrada: $IP ($count intentos de acceso)" $ALERT_EMAIL <<< $geoIP
      fi
    done < $SUSPICIOUS_IPS
fi

