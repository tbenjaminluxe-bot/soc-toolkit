#!/usr/bin/env python3
print("""
╔══════════════════════════════════╗
║ ROLAND SOC TOOLKIT - 13 TOOLS ║
║ Built on iPhone + LTE - Lagos ║
╚══════════════════════════════════╝
""")
tools={
 "1": ("Port Scanner", "port_scanner.py"),
 "2": ("IP Subnet Scanner", "ip_subnet_scanner.py"),
 "3": ("Brute Force Detector", "brute_force_detector.py"),
 "4": ("Hash Checker", "hash_checker.py"),
 "5": ("IOC Extractor", "ioc_extractor.py"),
}
for k,v in tools.items():
 print(f"[{k}] {v[0]}")
print("[0] List all files")
choice=input("\nChoose: ").strip()
if choice=="0":
 import os
 print("\n".join(os.listdir(".")))
elif choice in tools:
 print(f"\nRunning {tools[choice][1]}...\n")
 import subprocess,sys
 subprocess.run([sys.executable, tools[choice][1]])
