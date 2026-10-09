import re
from collections import Counter

print("🔍 SOC Tool 11 - Brute Force Detector")
print("Finds hackers trying to login many times\n")

# Sample log if user has no file
sample_logs = """Failed password for root from 185.220.101.5 port 22
Failed password for admin from 185.220.101.5 port 22
Failed password for root from 185.220.101.5 port 22
Failed password for root from 45.33.32.156 port 22
Accepted password for user from 192.168.1.10 port 22
Failed password for root from 185.220.101.5 port 22
Failed password for admin from 185.220.101.5 port 22
Failed password for test from 185.220.101.5 port 22
Failed password for root from 185.220.101.5 port 22
Failed password for root from 198.98.50.5 port 22
Failed password for root from 198.98.50.5 port 22
Failed password for root from 198.98.50.5 port 22
"""

log_data = ""
try:
 fname = input("Log file name (press ENTER to use demo attack log): ").strip()
 if fname:
  with open(fname) as f:
   log_data = f.read()
  print(f"Loaded {fname}\n")
 else:
  log_data = sample_logs
  print("Using DEMO attack log:\n")
  print(log_data)
except:
 log_data = sample_logs
 print("Using DEMO log\n")

# Find all IPs with Failed password
pattern = r"Failed.*from (\d+\.\d+\.\d+\.\d+)"
ips = re.findall(pattern, log_data)
count = Counter(ips)

print("="*50)
print(f"Total failed logins: {len(ips)}")
print("="*50)

attackers = []
for ip, fails in count.most_common():
 if fails >= 3:
  print(f"🚨 ATTACKER: {ip} -> {fails} FAILED attempts")
  attackers.append((ip,fails))
 else:
  print(f"  ok: {ip} -> {fails} fails")

print("="*50)
if attackers:
 print(f"\n🔥 {len(attackers)} ATTACKER(S) DETECTED!")
 print("SOC ACTION: Block these IPs in firewall:")
 for ip,f in attackers:
  print(f"  iptables -A INPUT -s {ip} -j DROP  # {f} fails")
 with open("blocklist.txt","w") as out:
  for ip,f in attackers:
   out.write(f"{ip} # {f} fails\n")
 print("\n💾 Saved blocklist.txt")
else:
 print("\n✅ No brute-force detected")

print("Done!")
