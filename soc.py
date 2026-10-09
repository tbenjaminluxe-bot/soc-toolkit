import requests, re
from datetime import datetime

def scan_url():
    url = input("Enter suspicious URL: ").strip()
    try:
        r = requests.get(url, timeout=10, allow_redirects=True)
        print(f"\nFinal URL: {r.url}\nStatus: {r.status_code}\nServer: {r.headers.get('Server','Unknown')}")
        if "<form" in r.text.lower():
            print("[!] LOGIN FORM - Phishing likely!")
    except Exception as e:
        print(f"Error: {e}")

def extract_ioc():
    text = input("Paste log/text: ")
    ip_pat = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    url_pat = r'https?://[^\s]+'
    hash_pat = r'\b[a-fA-F0-9]{32,64}\b'
    ips = re.findall(ip_pat, text)
    urls = re.findall(url_pat, text)
    hashes = re.findall(hash_pat, text)
    print(f"IPs: {ips}")
    print(f"URLs: {urls}")
    print(f"Hashes: {hashes}")

def gen_report():
    log = input("Paste alert log: ")
    ip_pat = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    url_pat = r'https?://[^\s]+'
    hash_pat = r'\b[a-fA-F0-9]{32,64}\b'
    ips = re.findall(ip_pat, log)
    urls = re.findall(url_pat, log)
    hashes = re.findall(hash_pat, log)
    risk = 40*bool(urls) + 30*bool(ips) + 30*bool(hashes)
    if risk >= 80:
        level = "CRITICAL"
    elif risk >= 50:
        level = "HIGH"
    else:
        level = "LOW"
    report = f"\n=== SOC REPORT {datetime.now()} ===\nLog: {log}\nIPs={ips} URLs={urls} Hashes={hashes}\nRisk: {risk} - {level}\nAction: BLOCK, Reset MFA, Report CIRT\n================================\n"
    print(report)
    with open("soc_reports.txt","a") as f:
        f.write(report)
    print("[SAVED] to soc_reports.txt")

while True:
    print("\n--- iPhone SOC TOOLKIT ---")
    print("1. Scan URL\n2. Extract IOCs\n3. Generate & Save Report\n4. View Casebook\n5. Exit")
    c = input("Choose 1-5: ")
    if c=="1":
        scan_url()
    elif c=="2":
        extract_ioc()
    elif c=="3":
        gen_report()
    elif c=="4":
        try:
            with open("soc_reports.txt") as f:
                print(f.read())
        except:
            print("No casebook yet - run 3 first")
    elif c=="5":
        break
