#!/bin/sh
IP=$1
[ -z "$IP" ] && { printf "Enter IP: "; read IP; }
echo "Checking $IP..."
nslookup $IP 2>&1 | grep -v "socket.c"
