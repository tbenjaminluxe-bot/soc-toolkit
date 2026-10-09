#!/usr/bin/env python3
# ip_subnet_scanner.py - Scan /24 subnet, find alive hosts
# Built 100% on iPhone - iSH

import ipaddress
import socket
import concurrent.futures
import time
from datetime import datetime

def is_alive(ip, timeout=1):
    # Try 3 methods to detect alive host
    ip = str(ip)
    # Method 1: Fast socket connect to common ports 80, 443, 135, 445
    for port in [80, 443, 135, 445, 22, 53]:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            s.connect((ip, port))
            s.close()
            return True, port
        except:
            pass

    # Method 2: Try hostname reverse (often works even if ports closed)
    try:
        socket.gethostbyaddr(ip)
        return True, "dns"
    except:
        pass

    return False, None

def scan_subnet(cidr_or_ip):
    print(f"\n📡 Scanning: {cidr_or_ip}")
    print(f"⏰ Started: {datetime.now().strftime('%H:%M:%S')}")
    print("-" * 50)

    # Parse input: if user enters 192.168.1.0 or 192.168.1.0/24 or 192.168.1.1
    try:
        if '/' not in cidr_or_ip:
            # If user gives 192.168.1.5 -> convert to 192.168.1.0/24
            ip = ipaddress.ip_interface(cidr_or_ip)
            network = ipaddress.ip_network(f"{cidr_or_ip}/24", strict=False)
        else:
            network = ipaddress.ip_network(cidr_or_ip, strict=False)
    except Exception as e:
        print(f"❌ Invalid IP/Network: {e}")
        print("Examples: 192.168.1.0 or 192.168.1.0/24 or 10.0.0.1")
        return

    hosts = list(network.hosts())
    # Limit to 254 hosts max for /24
    if len(hosts) > 254:
        print(f"⚠️ Too large ({len(hosts)} hosts). Limiting to first 254 for iPhone")
        hosts = hosts[:254]

    print(f"🎯 Target: {network} | Hosts to scan: {len(hosts)}")
    print(f"Scanning...\n")

    alive = []
    dead_count = 0
    start = time.time()

    # Fast scan with threads (20 at a time - iPhone friendly)
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        future_to_ip = {executor.submit(is_alive, ip): ip for ip in hosts}
        for i, future in enumerate(concurrent.futures.as_completed(future_to_ip)):
            ip = future_to_ip[future]
            try:
                alive_flag, port = future.result()
                if alive_flag:
                    alive.append((str(ip), port))
                    print(f"✅ ALIVE: {ip} (port {port} open)")
                else:
                    dead_count += 1
                    # print(f"❌ dead: {ip}") # uncomment to see dead too
            except Exception as e:
                dead_count += 1

            # Progress
            if (i+1) % 50 == 0:
                print(f"... {i+1}/{len(hosts)} scanned")

    elapsed = time.time() - start
    print("\n" + "="*50)
    print(f"📊 SCAN COMPLETE in {elapsed:.1f}s")
    print(f"✅ Alive: {len(alive)}/{len(hosts)}")
    print(f"❌ Dead/Filtered: {dead_count}")
    print("="*50)

    if alive:
        print("\n🎯 ALIVE HOSTS:")
        for ip, port in alive:
            print(f" {ip} -> port {port}")

        # Save to casebook
        with open("alive_hosts.txt","w") as f:
            for ip, port in alive:
                f.write(f"{ip}:{port}\n")
        print(f"\n💾 Saved to alive_hosts.txt")
    else:
        print("\nNo alive hosts found (ports may be filtered).")

if __name__ == "__main__":
    print("🔍 iPhone SOC - Subnet Scanner (/24)")
    print("Examples: 192.168.1.0 | 10.0.0.0/24 | 8.8.8.0/24")
    while True:
        target = input("\nEnter IP/Network (or q to quit): ").strip()
        if target.lower() in ['q','quit','exit']: break
        if not target: continue
        scan_subnet(target)
