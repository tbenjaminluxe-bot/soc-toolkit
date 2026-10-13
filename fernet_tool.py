from cryptography.fernet import Fernet
import os, sys

KEY_FILE="soc.key"
if not os.path.exists(KEY_FILE):
    open(KEY_FILE,"wb").write(Fernet.generate_key())
    print("[+] key created")
key=open(KEY_FILE,"rb").read()
f=Fernet(key)

def enc(p):
    open(p+".enc","wb").write(f.encrypt(open(p,"rb").read()))
    print(f"encrypted -> {p}.enc")
def dec(p):
    open(p.replace(".enc",".dec"),"wb").write(f.decrypt(open(p,"rb").read()))
    print(f"decrypted")

m=sys.argv[1]; fp=sys.argv[2]
enc(fp) if m=="enc" else dec(fp)
