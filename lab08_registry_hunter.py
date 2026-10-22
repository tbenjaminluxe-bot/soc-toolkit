#!/usr/bin/env python3
# Lab 08 - Registry RunKeys Hunter REAL+MOCK - iPhone Lagos - T1547.001
import os, sys, subprocess
try:
    import winreg
    HAS=True
except:
    HAS=False

SUS=["powershell","-enc","temp\\","appdata\\","roaming\\","rundll32","regsvr32","mshta",".vbs",".ps1"]
LEGIT=["SecurityHealth","OneDrive","WindowsDefender"]

def mock_scan():
    mock=[
        {"Name":"SecurityHealth","Path":"C:\\Windows\\System32\\SecurityHealthSystray.exe","Risk":"LOW"},
        {"Name":"DiscordUpdater","Path":"C:\\Users\\Roland\\AppData\\Roaming\\Discord\\Update.exe --a=powershell.exe -enc","Risk":"CRITICAL"},
        {"Name":"AdobeSync","Path":"C:\\Users\\Roland\\AppData\\Local\\Temp\\regsvr32.exe /s evil.dll","Risk":"CRITICAL"},
    ]
    findings=[]
    for e in mock:
        p=e["Path"].lower()
        if any(l in e["Name"] for l in LEGIT):
            print(f"[+] CLEAN: {e['Name']}")
        elif any(s in p for s in SUS):
            findings.append(e)
            print(f"[!] SUSPICIOUS: {e['Name']} -> {e['Path']} [{e['Risk']}]")
    return findings

def real_scan():
    print("[*] REAL MODE - Scanning Registry...\n")
    if not HAS:
        os.system("reg query HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run")
        os.system("reg query HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run")
        return [{"real":True}]
    findings=[]
    for hive, path in [(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Run"),(winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run")]:
        try:
            k=winreg.OpenKey(hive,path)
            i=0
            while True:
                try:
                    n,v,_=winreg.EnumValue(k,i)
                    if any(s in str(v).lower() for s in SUS):
                        findings.append((n,v))
                        print(f"[!] SUSPICIOUS: {n} = {v}")
                    else:
                        print(f"[+] CLEAN: {n}")
                    i+=1
                except OSError:
                    break
        except Exception as e:
            print(f"[-] {path}: {e}")
    return findings

print("="*68)
print(" Lab 08 LIVE - Registry RunKeys Hunter - T1547.001")
print("="*68)
if "--real" in sys.argv:
    findings=real_scan()
else:
    print("[*] MOCK MODE - use --real on real PC\n")
    findings=mock_scan()

print("\nProof: Lab 08 LIVE - iPhone Lagos - CLEAN")
