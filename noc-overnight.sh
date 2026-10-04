#!/bin/sh
# NOC Overnight Monitor - Roland Benjamin - MTN Nigeria
# Built on iPhone iSH

LOGFILE="NOC-REPORT-Sep30-overnight-$(date +%H%M).txt"

echo "=== NOC OVERNIGHT MONITOR START ===" | tee $LOGFILE
echo "Engineer: Roland Benjamin | ISP: MTN Nigeria | Location: Lagos, NG" | tee -a $LOGFILE
echo "Start: $(date)" | tee -a $LOGFILE
echo "-----------------------------------" | tee -a $LOGFILE

while true; do
  TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
  PING=$(ping -c 3 8.8.8.8 | tail -1 | awk '{print $4}' | cut -d '/' -f 2)
  if [ -z "$PING" ]; then
    PING="TIMEOUT - DOWN"
  fi
  echo "[$TIMESTAMP] MTN Latency: ${PING}ms" | tee -a $LOGFILE
  sleep 300
done
