# Lab 02: IOC Hunter - extracts evil domains/IPs from PCAP text
import re

def hunt_iocs(text):
    ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)
    domains = re.findall(r'[a-z0-9-]+\.com/[a-z0-9/.-]+', text)
    return set(ips), set(domains)

if __name__ == "__main__":
    sample = "evil-malware.com/gate.php -> 185.234.218.12"
    ips, doms = hunt_iocs(sample)
    print(f"[+] IPs: {ips}\n[+] Domains: {doms}")
py
PY
