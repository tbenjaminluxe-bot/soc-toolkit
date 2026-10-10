#!/bin/sh
clear
echo "=============================="
echo "  ROXY-02 SOC TOOLBOX 🧰"
echo "  Built on iPhone - 10% Gang"
echo "=============================="
echo "1) ip_checker.sh - Check suspicious IP"
echo "2) ipv6-check.sh - MTN IPv6 check"
echo "3) latency-logger.sh - Log latency"
echo "4) noc-check.sh - Quick health"
echo "5) noc-watch.sh - Live watch"
echo "6) noc-overnight.sh - Overnight log"
echo "7) brute_force_detector.py"
echo "8) ioc_extractor.py"
echo "9) port_scanner.py"
echo "10) List all files"
echo "0) Exit"
echo "------------------------------"
printf "Choose number: "
read n
case $n in
  1) printf "Enter IP: "; read ip; sh ip_checker.sh $ip;;
  2) sh ipv6-check.sh;;
  3) sh latency-logger.sh;;
  4) sh noc-check.sh;;
  5) sh noc-watch.sh;;
  6) sh noc-overnight.sh;;
  7) python3 brute_force_detector.py;;
  8) python3 ioc_extractor.py;;
  9) python3 port_scanner.py;;
  10) ls -1 *.sh *.py;;
  0) exit;;
  *) echo "Invalid";;
esac
