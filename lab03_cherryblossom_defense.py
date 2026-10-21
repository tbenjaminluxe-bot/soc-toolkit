import re
from collections import Counter

def scan(lines):
    alerts=[]
    for i,l in enumerate(lines):
        if "192.168" in l and ".onion" in l:
            alerts.append(f"[CRIT] L{i}: Router hijack - {l}")
    # beacon check
    pkts=[l for l in lines if "size=342" in l]
    if len(pkts)>=3:
        alerts.append(f"[HIGH] Beacon x{len(pkts)}: router phoning home")
    # firmware
    for i,l in enumerate(lines):
        if "firmware" in l.lower() and "POST" in l:
            alerts.append(f"[MED] L{i}: FW upload - {l}")
    return alerts

sample=[
"192.168.1.1 -> 8.8.8.8 size=342 time=00:00:01 DNS evil.onion",
"192.168.1.1 -> 8.8.8.8 size=342 time=00:01:01 DNS evil.onion",
"192.168.1.1 -> 8.8.8.8 size=342 time=00:02:01 DNS evil.onion",
"192.168.1.5 -> 192.168.1.1 firmware POST size=4567"
]

print("ROXY-02 Lab03 - CherryBlossom Defense")
for a in scan(sample):
    print(a)
print("Scan done - Defensive only")
