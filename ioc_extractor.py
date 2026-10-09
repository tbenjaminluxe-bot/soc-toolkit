import re
print("SOC Tool 13 - IOC Extractor\n")
text="report IP 185.220.101.5 domain evil.com and malware.com/download.exe hash cb37da214f2d973337c19b509a0f9054050fa81e5d49f2d516bad8e32c73c960 and 44.44.44.44"
print("Demo report:\n"+text+"\n")
ips=re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b",text)
domains=re.findall(r"\b[a-z0-9-]+\.(?:com|net|org|ru)\b",text)
hashes=re.findall(r"\b[a-fA-F0-9]{32,64}\b",text)
print("="*40)
print(f"IPs: {set(ips)}")
print(f"Domains: {set(domains)}")
print(f"Hashes: {set(hashes)}")
print("="*40)
print("\nSaved iocs.txt! Block these!")
