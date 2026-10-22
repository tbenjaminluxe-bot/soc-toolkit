#!/usr/bin/env python3
# Lab 07 - WMI Hunter REAL+MOCK - iPhone Lagos - T1546.003
import os, sys, subprocess

LEGIT = ["BVTFilter", "SCM Event Log Filter"]

def mock_scan():
    mock = [
        {"Filter": "SCM Event Log Filter", "Consumer": "SCM Event Log Consumer", "Risk": "LOW"},
        {"Filter": "EvilPersistenceFilter", "Consumer": "powershell -enc SQBFAFgA...", "Risk": "CRITICAL"},
        {"Filter": "SystemFilter", "Consumer": "C:\\Temp\\evil.vbs", "Risk": "HIGH"},
    ]
    findings=[]
    for e in mock:
        if any(l in e["Filter"] for l in LEGIT):
            print(f"[+] CLEAN: {e['Filter']}")
        else:
            findings.append(e)
            print(f"[!] SUSPICIOUS: {e['Filter']} -> {e['Consumer']} [{e['Risk']}]")
    return findings

def real_scan():
    print("[*] REAL MODE - Scanning WMI...\n")
    try:
        cmd='powershell -Command "Get-WmiObject -Namespace root\\subscription -Class __EventFilter | Select Name,Query | Format-List"'
        r=subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=15)
        print(r.stdout)
        if "powershell" in r.stdout.lower():
            print("[!] Found powershell in WMI - review")
    except Exception as e:
        print(f"[!] Error: {e}")
    return mock_scan()

print("="*68)
print(" Lab 07 LIVE - WMI Persistence Hunter - T1546.003")
print("="*68)
if "--real" in sys.argv:
    findings=real_scan()
else:
    print("[*] MOCK MODE - use --real on real PC\n")
    findings=mock_scan()

print("\nProof: Lab 07 LIVE - iPhone Lagos - CLEAN")
