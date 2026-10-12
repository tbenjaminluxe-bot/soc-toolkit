#!/usr/bin/env python3
"""
ROXY-02 v2.0 WATCHDOG - Port Scan Detector
Built 100% on iPhone - iSH
Detects: 1 IP scanning many ports in short time
"""
from collections import defaultdict
import time
from datetime import datetime
import os

# Config
SCAN_THRESHOLD = 10 # ports
TIME_WINDOW = 60 # seconds
LOG_FILE = "alerts.log"
BLOCKED_FILE = "blocked_ips.txt"

scans = defaultdict(list)
blocked = set()

def log_alert(ip, ports):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = f"[{timestamp}] 🚨 SCAN DETECTED! IP: {ip} | Ports: {len(ports)} | List: {sorted(list(ports))[:15]}"
    print(msg)
    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")
    # save to blocked
    if ip not in blocked:
        with open(BLOCKED_FILE, "a") as f:
            f.write(f"{ip} - {timestamp} - {len(ports)} ports\n")
        blocked.add(ip)
    # trigger notifier if exists
    try:
        from notifier import send_alert
        send_alert(ip, len(ports), sorted(list(ports))[:10])
    except:
        pass

def detect(ip, port):
    now = time.time()
    scans[ip].append((port, now))
    # keep only last 60 sec
    scans[ip] = [(p,t) for p,t in scans[ip] if now - t < TIME_WINDOW]
    unique_ports = set(p for p,t in scans[ip])
    if len(unique_ports) >= SCAN_THRESHOLD and ip not in blocked:
        log_alert(ip, unique_ports)
        scans[ip] = [] # reset after alert
        return True
    return False

def monitor_log(log_path):
    """Monitor a log file like auth.log or custom log"""
    print(f"[ROXY-WATCHDOG] Monitoring {log_path} | Threshold: {SCAN_THRESHOLD} ports/{TIME_WINDOW}s")
    try:
        with open(log_path, "r") as f:
            f.seek(0,2) # go end
            while True:
                line = f.readline()
                if not line:
                    time.sleep(1)
                    continue
                # parse: expect format "IP PORT" or syslog
                parts = line.strip().split()
                for part in parts:
                    if part.count('.')==3:
                        ip = part
                        port = 22 # default
                        # try find port
                        for p in parts:
                            if p.isdigit() and 1 <= int(p) <= 65535:
                                port = int(p)
                        detect(ip, port)
    except FileNotFoundError:
        print(f"[!] Log file {log_path} not found, running in simulation mode")
        simulate()

def simulate():
    print("[SIMULATION] Injecting fake scan...")
    attacker = "102.89.75.23"
    for port in [21,22,23,25,53,80,110,135,139,443,445,993,995,1723,3306,3389,5900,8080]:
        detect(attacker, port)
        time.sleep(0.2)
    print("[SIM] Done - check alerts.log")

if __name__ == "__main__":
    import sys
    log = sys.argv[1] if len(sys.argv)>1 else "test.log"
    monitor_log(log)
