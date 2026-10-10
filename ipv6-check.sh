#!/bin/bash
echo "=== MTN NG IPv6 NOC Check ==="
echo "Date: $(date)"
echo ""
echo "[1] Public IP:"
curl -6 -s ifconfig.co || curl -4 -s ifconfig.co
echo -e "\n"
echo "[2] Local IPv6 Addresses:"
ifconfig | grep inet6
echo ""
echo "[3] Latency Test (IPv6 Google DNS):"
ping6 -c 3 2001:4860:4860::8888 2>&1 | tail -3 || ping -c 3 8.8.8.8 | tail -3
echo ""
echo "Result: If you see /66 = Hotspot shared, /64 = Direct MTN data. Both NORMAL."
