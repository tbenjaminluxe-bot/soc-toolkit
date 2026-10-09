# Fix toolkit.py
open('toolkit.py','w').write('''#!/usr/bin/env python3
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
choice=input("\\nChoose: ").strip()
if choice=="0":
 import os
 print("\\n".join(os.listdir(".")))
elif choice in tools:
 print(f"\\nRunning {tools[choice][1]}...\\n")
 import subprocess,sys
 subprocess.run([sys.executable, tools[choice][1]])
''')

# Fix README.md
open('README.md','w').write("""# 🛡️ Roland SOC Toolkit - 13 Tools Built on iPhone

> Built entirely on iPhone using iSH + LTE in Lagos. No laptop needed.

## 🔥 Tools
1. **Port Scanner** - Found scanme.nmap.org:80 OPEN, 8.8.8.8:53 DNS + 443 HTTPS OPEN
2. **IP Subnet Scanner** - Discovers alive hosts
3. **Brute Force Detector** - Detected 2 attackers: 185.220.101.5 (7 fails) -> generates iptables block
4. **File Hash Checker** - MD5/SHA256 for malware + VirusTotal check
5. **IOC Extractor** - Pulls IPs/domains/hashes from threat reports

Evidence: blocklist.txt, hashes.txt, iocs.txt, alive_hosts.txt

## 💻 How Built
- Device: iPhone + iSH app
- Network: LTE
- Battery: Tools 11-13 built on 9% -> 6%!

## 🎯 SOC Skills
Port scanning, Log analysis, Malware analysis, Threat Intel, Firewall

Built by Roland - Aspiring SOC L1, Lagos.
#SOC #CyberSecurity #Python
""")
print("FIXED! toolkit.py and README.md created!")
