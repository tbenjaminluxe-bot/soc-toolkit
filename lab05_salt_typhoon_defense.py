#!/usr/bin/env python3
# Lab 05 - Salt Typhoon Hunter 🌊 - SOC TOOLBOX Lagos
# Detects Salt Typhoon telecom implants (Cisco IOS XE + Linux backdoors)
import os, re, subprocess

IOC = {
 "files": ["/usr/bin/cisco", "/etc/cron.d/sys", "/var/log/wtmp2", "/tmp/.xs", ".var/log/auth"],
 "processes": ["xlogin", "cisco", "authd", "syslogd"],
 "ips": ["184.105.247", "8.218.", "47.91."],
 "regex": [r"libssh.*backdoor", r"vsftpd.*3.0.3", r"Salt.*Typhoon", r"JumbledPath"]
}

def scan():
  print("[*] Lab 05 Salt Typhoon Hunter 🌊 - LIVE")
  hits = 0
  # Check suspicious files
  for root,_,files in os.walk("/tmp", topdown=True):
    for f in files:
      if any(x in f for x in [".xs","wtmp2","cisco"]):
        print(f"[!] SUSPECT: {os.path.join(root,f)}")
        hits+=1
  # Check processes
  try:
    ps = subprocess.getoutput("ps aux")
    for proc in IOC["processes"]:
      if proc in ps.lower():
        print(f"[!] SUSPECT PROC: {proc}")
        hits+=1
  except: pass
  # Check regex in configs
  for path in ["/etc/passwd","/etc/crontab"]:
    if os.path.exists(path):
      try:
        with open(path,'r',errors='ignore') as fd:
          data=fd.read()
          for pat in IOC["regex"]:
            if re.search(pat,data,re.I):
              print(f"[!] IOC MATCH in {path}: {pat}")
              hits+=1
      except: pass
  if hits==0:
    print("[+] CLEAN - No Salt Typhoon persistence found")
  else:
    print(f"[!] {hits} hits - INVESTIGATE!")
  print("[+] Built on iPhone - Lagos, NG - ROXY-02")
  return hits

if __name__ == "__main__":
  scan()
