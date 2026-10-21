import os
# Optional telegram - fill later
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT = os.getenv("TELEGRAM_CHAT", "")

def send_alert(ip, count, ports):
    msg = f"🚨 ROXY-WATCHDOG ALERT\nIP: {ip}\nPorts scanned: {count}\nPorts: {ports}\nTime: now"
    print(f"[NOTIFIER] {msg}")
    if TELEGRAM_TOKEN and TELEGRAM_CHAT:
        try:
            import requests
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            requests.post(url, json={"chat_id": TELEGRAM_CHAT, "text": msg})
            print("[TELEGRAM] Sent!")
        except Exception as e:
            print(f"[TELEGRAM FAIL] {e}")
