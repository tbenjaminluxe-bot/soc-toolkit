import socket,concurrent.futures
TOP={22:"SSH",21:"FTP",23:"Telnet",25:"SMTP",53:"DNS",80:"HTTP",110:"POP3",443:"HTTPS",445:"SMB",3306:"MySQL",3389:"RDP",8080:"HTTP-ALT",135:"RPC",139:"NetBIOS",5900:"VNC"}
def grab_banner(ip,port):
 try:
  s=socket.socket()
  s.settimeout(2)
  s.connect((ip,port))
  if port in [80,8080]:
   s.send(b"GET / HTTP/1.0\r\n\r\n")
  b=s.recv(1024).decode(errors='ignore').strip()
  s.close()
  return b.split("\n")[0][:80] if b else "OPEN"
 except:
  return "OPEN - no banner"
def check_port(ip,port):
 try:
  s=socket.socket()
  s.settimeout(1)
  r=s.connect_ex((ip,port))
  s.close()
  if r==0:
   return (port,"OPEN",grab_banner(ip,port))
  return (port,"CLOSED","")
 except:
  return (port,"CLOSED","")
print("SOC Port Scanner + Banner")
t=input("IP/host: ").strip() or "scanme.nmap.org"
try:
 ip=socket.gethostbyname(t)
 print(f"Target {t} -> {ip}\n")
except:
 ip=t
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as ex:
 futs=[ex.submit(check_port,ip,p) for p in TOP]
 for f in concurrent.futures.as_completed(futs):
  port,st,ban=f.result()
  svc=TOP.get(port,"")
  if st=="OPEN":
   print(f"✅ OPEN {port} / {svc} -> {ban}")
  else:
   print(f"❌ CLOSED {port} / {svc}")
print("Done!")
