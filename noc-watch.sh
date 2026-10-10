#!/bin/sh
while true; do echo "=== $(date) ==="; ping -c 3 8.8.8.8 | grep -E "loss|min/avg"; sleep 300; done
