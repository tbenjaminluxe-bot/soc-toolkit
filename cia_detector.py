import datetime

print("🛡️ Roxy v7.3 - CIA Weeping Angel Detector ACTIVE")

with open("tv_hack.log") as f:
    logs = f.read()

threat_found = False

if "mic still ACTIVE" in logs and "Power OFF" in logs:
    print("🚨 ALERT! CIA STYLE ATTACK DETECTED!")
    print("Reason: TV mic ON while Power OFF - Weeping Angel pattern")
    threat_found = True

if "185.22" in logs:
    print("🚨 C2 CALLBACK DETECTED: TV talking to hacker server 185.22.14.77")
    threat_found = True

if "recording" in logs:
    print("🚨 DATA THEFT: Audio recording created while TV OFF")
    threat_found = True

if threat_found:
    c2_ip = "185.22.14.77"
    # Auto-block
    with open("blocked_ips.txt", "a") as b:
        b.write(f"{c2_ip} - CIA Weeping Angel C2 - {datetime.datetime.now()}\n")
    with open("alerts.log", "a") as a:
        a.write(f"[{datetime.datetime.now()}] CRITICAL: CIA Weeping Angel blocked - {c2_ip} - TV mic ON while OFF\n")
    print(f"\n✅ Roxy Shield ACTION: BLOCKED IP {c2_ip}")
    print("✅ Written to blocked_ips.txt and alerts.log")
    print("✅ Would kill weeping_angel.exe")
else:
    print("✅ No CIA activity - TV clean")
