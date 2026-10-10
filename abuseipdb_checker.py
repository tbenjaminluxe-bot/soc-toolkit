#!/usr/bin/env python3
"""
ROXY-02 SOC Toolbox - AbuseIPDB Checker v1.2
Checks IP reputation via AbuseIPDB API
Usage: python3 abuseipdb_checker.py 8.8.8.8
       API_KEY env: export ABUSEIPDB_KEY="your_key"
"""
import os, sys, json, argparse
from datetime import datetime
try:
    import requests
except ImportError:
    print("Installing requests...")
    os.system("pip install requests")
    import requests

API_URL = "https://api.abuseipdb.com/api/v2/check"

def check_ip(ip, api_key):
    headers = {"Key": api_key, "Accept": "application/json"}
    params = {"ipAddress": ip, "maxAgeInDays": 90, "verbose": ""}
    try:
        resp = requests.get(API_URL, headers=headers, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json().get("data", {})
        print(f"\n[ROXY-02] AbuseIPDB Report for {ip}")
        print("-"*45)
        print(f"IP: {data.get('ipAddress')}")
        print(f"Is Whitelisted: {data.get('isWhitelisted')}")
        print(f"Abuse Score: {data.get('abuseConfidenceScore')}%")
        print(f"Country: {data.get('countryCode')} | ISP: {data.get('isp')}")
        print(f"Domain: {data.get('domain')}")
        print(f"Total Reports: {data.get('totalReports')}")
        print(f"Last Reported: {data.get('lastReportedAt')}")
        score = data.get('abuseConfidenceScore', 0)
        verdict = "✅ CLEAN" if score == 0 else "⚠️ SUSPICIOUS" if score < 50 else "🔴 MALICIOUS - BLOCK"
        print(f"\nVerdict: {verdict}")
        if data.get('reports'):
            print(f"\nRecent Reports:")
            for r in data.get('reports', [])[:3]:
                print(f" - {r.get('reportedAt')}: {r.get('comment')[:80]}")
        return data
    except Exception as e:
        print(f"[!] API Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AbuseIPDB IP Checker - ROXY-02")
    parser.add_argument("ip", help="IP address to check")
    parser.add_argument("--key", help="AbuseIPDB API key (or set ABUSEIPDB_KEY env)")
    args = parser.parse_args()
    api_key = args.key or os.getenv("ABUSEIPDB_KEY")
    if not api_key:
        print("[!] Missing API key. Set env: export ABUSEIPDB_KEY='your_key'")
        print("Get free key at: https://www.abuseipdb.com/api")
        sys.exit(1)
    check_ip(args.ip, api_key)
