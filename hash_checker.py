import hashlib,os
print("🔍 SOC Tool 12 - File Hash Checker")
print("Used to check if file is malware\n")
fname=input("File to hash (press ENTER to hash this script itself): ").strip()
if not fname:
 fname="brute_force_detector.py"
 print(f"Hashing {fname} as demo\n")
try:
 with open(fname,'rb') as f:
  data=f.read()
 md5=hashlib.md5(data).hexdigest()
 sha1=hashlib.sha1(data).hexdigest()
 sha256=hashlib.sha256(data).hexdigest()
 print(f"File: {fname}")
 print(f"Size: {len(data)} bytes")
 print("="*50)
 print(f"MD5:    {md5}")
 print(f"SHA1:   {sha1}")
 print(f"SHA256: {sha256}")
 print("="*50)
 print("\n🔎 SOC NEXT STEP:")
 print(f"Go to virustotal.com and search:")
 print(f"{sha256}")
 print("\nIf VirusTotal says malicious = malware!")
 print("If 0 detections = clean")
 with open("hashes.txt","w") as out:
  out.write(f"File: {fname}\nMD5: {md5}\nSHA1: {sha1}\nSHA256: {sha256}\n")
 print("\n💾 Saved hashes.txt")
except Exception as e:
 print(f"Error: {e}")
 print("Try: ls to see files")
print("Done!")
