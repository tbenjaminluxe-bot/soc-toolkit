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

git clone https://github.com/tbenjaminluxe-bot/soc-toolkit.git
cd soc-toolkit
chmod +x toolbox.sh
./toolbox.sh
