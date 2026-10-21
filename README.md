![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Clones](https://img.shields.io/badge/Clones-313%2B-brightgreen)
![iSH Ready](https://img.shields.io/badge/iSH-iPhone%20Compatible-black)
## Lab 03 LIVE - CherryBlossom Hunter 🌸
Defensive detector for router implant + firmware persistence
## 🔥 Lab 02 LIVE - IOC Hunter
# ROXY-02 SOC TOOLBOX 🧰
Built entirely on iPhone - Lagos, NG

One toolbox to monitor, investigate, and respond.

## Lab 01: PCAP Forensics (iSH Fix)
When tools fail on iOS:
- Download -> `ASCII text, 14 bytes` HTML block
- Scapy -> `OSError: [Errno 22] Invalid argument`
- Fix: Pure Python writer with `struct` + `inet_aton`

**Results:**
- `sample.pcap 9.7K` - 50x GET example.com (clean)
- `malware.pcap` - IOC: `evil-malware.com /gate.php` POST to `185.234.218.12`
### IOCs Extracted (Lab 01)
- **Domain:** evil-malware.com
- **URI:** /gate.php
- **Method:** POST
- **C2 IP:** 185.234.218.12
- **File:** malware.pcap
- **Detection:** 50x GET clean vs POST to C2 = malicious beacon
  
## Quick Start
```bash
git clone https://github.com/tbenjaminluxe-bot/soc-toolkit.git
cd soc-toolkit
chmod +x toolbox.sh
./toolbox.sh
```


## Lab 03 LIVE - CherryBlossom Defense 🌸
- Router implant detector + firmware persistence hunter
- File: lab03_cherryblossom_defense.py
## Lab 04 LIVE - Grasshopper Hunter 🦗
- Barracuda ESG backdoor CVE-2023-2868
