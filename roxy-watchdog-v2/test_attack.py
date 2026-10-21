from watchdog import detect
import time

print("Testing ROXY Watchdog...")
attacker = "45.33.32.156" # fake attacker
ports = [21,22,23,25,53,80,110,135,139,443,445,993,3306,3389,8080,8443]

for p in ports:
    print(f"Packet from {attacker} to port {p}")
    triggered = detect(attacker, p)
    time.sleep(0.1)
    if triggered:
        print(">>> DETECTED & LOGGED!")
        break
