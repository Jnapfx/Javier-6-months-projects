# Incident Report – Suspicious Login (SSH Brute Force)

**Date:** August 27, 2025  
**Case ID:** SOC-2025-SSH-001  
**Tool/Source:** Wazuh SIEM (Agent: `ParrotOS_2`)  
**Analyst:** J. Mendoza  

---

## 1. Alert Details

**Rule Triggered:** `100202`  
**Description:** SSH brute force: 3 failed SSH logins in 60s from `192.168.1.103` to user `javierssh`  
**Rule Level:** 12 (High)  
**Mapped to MITRE ATT&CK:** T1110 – Brute Force  

**Screenshot of Alert:**  
![SSH Brute Force Alert](./ssh_bruteforce_alert.png)

---

## 2. Supporting Evidence

- **Custom Rule Config (ssh-bruteforce.xml)**  
  This rule detects multiple failed SSH logins within a short timeframe.  
  ![Rule Configuration](./alert_auth_rule.png)

- **Threat Hunting Dashboard (Wazuh)**  
  Shows event distribution and severity breakdown.  
  ![Threat Hunting Dashboard](./incident_classification.png)

---

## 3. Timeline of Events

| Time (EST)       | Event | Action Taken |
|------------------|-------|--------------|
| 15:58:41         | Multiple failed SSH logins from `192.168.1.103` targeting user `javierssh` | Wazuh rule `100202` triggered |
| 15:58:49         | Brute force alert escalated to Level 12 | SOC analyst reviewed logs |
| 16:05            | Analyst investigated source IP (internal subnet `192.168.1.103`) | Confirmed activity originated from lab attacker VM (Kali) |
| 16:15            | Containment: blocked repeated attempts, restricted login attempts to whitelisted IPs | Prevented further brute force |
| 16:30            | Monitoring performed to confirm no additional login attempts | No persistence detected |
| 16:45            | Incident closed | Documentation completed |

---

## 4. Resolution Notes

- **Classification:** True Positive (brute force attempt detected)  
- **Root Cause:** Unauthorized SSH login attempts from `192.168.1.103` (Kali attacker VM).  
- **Actions Taken:**
  - Reviewed Wazuh logs and confirmed rule detection.  
  - Blocked offending IP at firewall level.  
  - Implemented login hardening (rate-limiting, MFA, fail2ban).  
- **Final Outcome:** No successful compromise observed. Account `javierssh` remains secure.  

---

## 5. Lessons Learned / Next Steps

- Enhance detection by expanding Wazuh rules to trigger earlier at lower thresholds.  
- Integrate alerts into case-management (TheHive) for streamlined workflow.  
- Apply additional hardening: disable SSH password auth, enforce key-based login.  

---

**Status:** ✅ Closed – Contained  
