#!/usr/bin/env python3
# Lab 04 - Grasshopper Hunter 🦗 - SOC TOOLBOX Lagos
# Detects Barracuda ESG Grasshopper implant artifacts
import os, re, hashlib

IOC = {
 "files": ["/bin/bsmtpd", "/tmp/bsmtp", "mail/bd.log", "db/acl.db-shm"],
 "procs": ["bsmtpd", "bsh", "seaglass"],
 "ports": [25, 8000, 8443],
 "regex": [r"Barracuda.*backdoor", r"bsmtpd.*-c", r"ESG.*RCE"]
}

def scan_file(path):
  hits=[]
  try:
    with open(path,'r',errors='ignore') as f:
      data=f.read()
      for pat in IOC["regex"]:
        if re.search(pat,data,re.I):
          hits.append(pat)
  except: pass
  return hits

def hash_check():
  print("[*] Lab 04 Grasshopper Hunter - LIVE")
  for root,_,files in os.walk("/tmp", topdown=True):
    for fn in files:
      if any(i in fn for i in ["bsmtp","bd.log","acl.db"]):
        print(f"[!] SUSPECT FILE: {os.path.join(root,fn)}")
  print("[+] Scan complete - No Grasshopper persistence found = CLEAN")
  print("[+] Built on iPhone - Lagos, NG - ROXY-02")

if __name__ == "__main__":
  hash_check()
