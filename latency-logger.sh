#!/bin/sh
LOGFILE="mtn-latency.log"
echo "=== Starting MTN Latency Logger ==="
echo "Logging to $LOGFILE every 60 secs. Press Ctrl+C to stop."
while true; do
  TIME=$(date "+%Y-%m-%d %H:%M:%S")
  PING=$(ping -c 1 8.8.8.8 | grep time= | cut -d'=' -f4 | cut -d' ' -f1)
  if [ -z "$PING" ]; then PING="FAIL"; fi
  echo "$TIME - $PING ms" | tee -a $LOGFILE
  sleep 60
done
