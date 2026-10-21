# SOC L1 Incident Report - Malware Traffic Analysis

**Analyst:** @tbenjaminluxe-bot  
**Date:** 2026-10-19  
**Source:** malware-traffic-analysis.net [PCAP]  
**Tool:** roxy-watchdog-v2 + Manual Analysis  
**Severity:** HIGH  
**Status:** Investigated - IOCs Extracted

### 1. Executive Summary
Identified malicious executable download via HTTP during routine PCAP review. Traffic pattern matches common malware delivery (Emotet / IcedID style). No laptop needed - analyzed via mobile SOC workflow.

### 2. What I Saw
- **Initial vector:** HTTP GET to suspicious domain
- **Payload:** `.exe` download (Windows executable)
- **Pattern:** User-Agent anomaly + low reputation domain
- **Detection:** roxy-watchdog-v2 flagged outbound HTTP

### 3. IOCs (Indicators of Compromise)
> Note: I extracted these on phone - full SHA256 in next update

### 4. MITRE ATT&CK Mapping
- T1566 - Phishing
- T1105 - Ingress Tool Transfer
- T1204.002 - Malicious File

### 5. SOC L1 Actions Taken
1. Flagged traffic as malicious
2. Extracted IOCs for blocklist
3. Documented for L2 escalation
4. Added detection to roxy-watchdog-v2

### 6. Recommended Containment
- Block domain/IP at firewall
- Block SHA256 hash at endpoint
- Hunt for same User-Agent in logs
- User awareness training

### 7. What I Learned (Phone SOC)
Built this entire analysis on mobile while caring for family. SOC mindset > equipment.

---
**Repo:** github.com/tbenjaminluxe-bot/soc-toolkit  
**Clones:** 114 unique | 226 total | 117 views  
**Next:** Adding full SHA256 + Wireshark screenshot (when accessible)
