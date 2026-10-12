
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import time

def read_log(f, n=25):
    try:
        lines = open(f).read().strip().splitlines()
        return "\n".join(lines[-n:])
    except:
        return "No data yet"

def count_lines(f):
    try:
        return len([l for l in open(f).read().splitlines() if l.strip()])
    except:
        return 0

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if "icon" in self.path:
            try:
                fn = "apple-touch-icon.png" if "apple" in self.path else "icon.png"
                data = open(fn,"rb").read()
                self.send_response(200)
                self.send_header("Content-type","image/png")
                self.end_headers()
                self.wfile.write(data)
                return
            except:
                pass
        ts = str(int(time.time()))
        now = datetime.now().strftime("%H:%M:%S %d-%m-%Y")
        alerts = read_log("alerts.log", 20)
        blocked = read_log("blocked_ips.txt", 20)
        a = count_lines("alerts.log")
        b = count_lines("blocked_ips.txt")

        html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>ROXY SOC</title>
<link rel="apple-touch-icon" href="/apple-touch-icon.png?v={ts}">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#020617;color:#e2e8f0;font-family:monospace;padding:16px}}
.header{{background:#0f172a;border:2px solid #22c55e;border-radius:20px;padding:20px;text-align:center;margin-bottom:16px}}
h1{{color:#22c55e;font-size:20px}}
.time{{color:#64748b;font-size:11px;margin-top:6px}}
.stats{{display:flex;gap:10px;justify-content:center;margin-top:14px}}
.stat{{background:#1e293b;border:1px solid #334155;border-radius:10px;padding:10px 14px;min-width:80px;text-align:center}}
.stat b{{color:#22c55e;font-size:18px;display:block}}
.card{{background:#0f172a;border:1px solid #334155;border-radius:14px;padding:14px;margin-bottom:12px}}
.card h2{{color:#22c55e;font-size:13px;margin-bottom:8px}}
pre{{background:#020617;padding:10px;border-radius:8px;white-space:pre-wrap;font-size:11px;color:#86efac}}
</style></head><body>
<div class="header">
<div style="font-size:50px">🛡️</div>
<h1>ROXY SOC v7.3</h1>
<div class="time">{now} • Cache {ts}</div>
<div class="stats">
<div class="stat"><b>{a}</b>ALERTS</div>
<div class="stat"><b>{b}</b>BLOCKED</div>
<div class="stat"><b style="color:#22c55e">●</b>LIVE</div>
</div>
</div>
<div class="card"><h2>ALERTS LOG</h2><pre>{alerts}</pre></div>
<div class="card"><h2>BLOCKED IPs</h2><pre>{blocked}</pre></div>
</body></html>"""
        self.send_response(200)
        self.send_header("Content-type","text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode())

print("ROXY SOC v7.3 FIXED - Running on 8000")
HTTPServer(("0.0.0.0",8000),Handler).serve_forever()
