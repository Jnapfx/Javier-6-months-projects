# Implement Security Monitoring and Incident Response

**Analyst:** Javier Napoles  
**Date:** July 23, 2025  
**Environment:** Parrot OS (UTM virtual lab)  
**Tools Used:** CyberFortress, Nmap, VirusTotal, Hybrid Analysis, Social-Engineer Toolkit (SET)

---

## 1. Introduction

This report demonstrates the implementation of basic security monitoring and execution of an incident response scenario based on observed malware activity within a controlled lab environment.  
The objective is to detect, prioritize, and respond to suspicious activity using threat intelligence, detection rules, and structured response procedures.

---

## 2. Security Monitoring Setup

### 2.1 Monitoring Architecture

- **Host OS:** Parrot Security OS (running on UTM)
- **Monitored Subnet:** 192.168.1.0/24
- **Tools & Logs Monitored:**
  - System logs (syslog)
  - Malware behavior from sandbox reports
  - Network traffic (via pcap and analysis)
  - Process execution events
  - MITRE ATT&CK mappings for detection logic

### 2.2 Use Case: Malicious Process Masquerading

**Objective:** Detect processes that imitate legitimate system processes but execute from abnormal paths.

#### Detection Rule Example:

```pseudo
IF process_name = "svchost.exe"
AND NOT file_path CONTAINS "C:\Windows\System32\"
THEN alert("Masquerading Process Detected")
```

#### Triggered Alert:

- **Host:** 192.168.1.12  
- **Executable:** `FSP-0991.exe` → spawned `svchost.exe` from `C:\Users\Public\`  
- **Malware Family:** Formbook  
- **MITRE Techniques:** T1036 (Masquerading), T1055 (Process Injection)

---

## 3. Alert Prioritization Process

All alerts were triaged based on severity, asset criticality, and threat behavior alignment with known MITRE ATT&CK techniques.

| Alert ID | Host           | Description                             | Severity | Justification                                             |
|----------|----------------|-----------------------------------------|----------|-----------------------------------------------------------|
| A-001    | 192.168.1.12   | Masquerading process (Formbook)         | High     | Matches known malware pattern with credential theft       |
| A-002    | 192.168.1.7    | Apache version exposure (2.4.29)        | Medium   | May aid adversary reconnaissance                          |
| A-003    | 192.168.1.10   | SMB signing disabled                    | Low      | Insecure config, but no active exploitation observed      |

---

## 4. Incident Response Scenario

### 4.1 Overview

- **Incident ID:** IR-2025-07-22-A  
- **Type:** Malware Execution (Credential Theft)  
- **Detection Source:** Alert A-001 (svchost.exe anomaly)  
- **Initial IOC:** `FSP-0991.exe` – confirmed Formbook sample  
- **Tactics/Techniques Used:**
  - T1055 – Process Injection
  - T1036 – Masquerading
  - T1056.001 – Keylogging
  - T1071.001 – C2 over HTTP
  - T1573 – Encrypted C2

### 4.2 Response Actions

| Step | Description                                                                 |
|------|------------------------------------------------------------------------------|
| 1    | Isolated infected VM from internal network                                  |
| 2    | Terminated active processes (`FSP-0991.exe`, fake `svchost.exe`)            |
| 3    | Captured memory dump and full process tree for forensic analysis            |
| 4    | Removed malware artifacts (`aut9DD0.tmp`, `dump.pcap`)                      |
| 5    | Reset all user credentials from infected endpoint                           |
| 6    | Blocked all known C2 domains/IPs in host and network firewall               |
| 7    | Performed full network scan to rule out lateral movement                    |
| 8    | Reviewed registry changes (auto-start entries) and cleaned persistence keys |

---

## 5. Evidence of Incident

### 5.1 IOCs

| Type       | Value                                                              |
|------------|--------------------------------------------------------------------|
| SHA256     | `63d2e9f885c7b2df3fc23658a5c13d3df968fbe205d9c973f4f42c775bd787af` |
| File Path  | `C:\Program Files\Common Files\FSP-0991.exe`                       |
| Injected   | `svchost.exe` (user directory)                                     |
| C2 Domains | `www.3xfootball.com`, `kasegitai.tokyo`, `goldenjade-travel.com`   |
| C2 IPs     | `206.119.72.86`, `116.50.37.244`, `1.1.1.1`                         |

### 5.2 Visual Indicators (Available in project folder)

- **Process Tree Screenshot:** FSP-0991.exe spawning svchost.exe  
- **Network Traffic Evidence:** C2 communication over HTTP(S)  
- **Keylogging Output:** Captured credentials via sandbox emulation

---

## 6. Lessons Learned

| Observation                          | Improvement Strategy                                 |
|-------------------------------------|------------------------------------------------------|
| Malware evaded detection initially  | Deploy real-time behavior-based endpoint monitoring  |
| DNS traffic was unfiltered          | Implement DNS filtering for known C2 domains         |
| Static rules were too narrow        | Expand rules to include anomaly detection logic      |
| Flat network architecture           | Enforce network segmentation and micro-perimeters    |
| No credential reuse controls        | Enforce 2FA and credential vaulting on critical apps |

---

## 7. Conclusion

## 7. Conclusion

This project provided a comprehensive simulation of a real-world security operations workflow, showcasing the successful integration of detection, alert triage, and incident response within a monitored lab environment.

The **malicious execution of `FSP-0991.exe`**, a known Formbook variant, triggered a high-fidelity detection rule based on behavioral indicators such as process masquerading and injection techniques. By leveraging sandbox analysis, MITRE ATT&CK mapping, and log-based correlation, the security monitoring setup was able to flag the intrusion at an early stage—before exfiltration or lateral movement could escalate.

The incident response phase demonstrated a methodical approach: from isolating the affected host and terminating malicious activity, to analyzing IOCs, remediating system changes, and resetting compromised credentials. The use of structured triage and classification enabled prioritization of threats based on severity, impact potential, and relevance to known threat actor behaviors.

This hands-on scenario emphasized several key security principles:

- **Detection precision** is enhanced when rules incorporate both file characteristics and behavioral context (e.g., execution path, parent process).
- **Rapid containment** depends on visibility and automation in log collection, alerting, and response execution.
- **Threat intelligence integration** (e.g., MITRE mappings, IOC correlation) significantly improves decision-making in live response situations.
- **Continuous monitoring and iteration** are critical—response is not a one-time event, but a cycle of learning, refinement, and resilience-building.

In a production setting, the techniques demonstrated here would help reduce dwell time, contain breaches faster, and guide remediation with actionable intelligence.  
Ultimately, this project affirms the value of combining tactical detection rules with strategic response frameworks to achieve a proactive security posture.


---

## 8. References

- [CyberFortress Report](https://cyber-fortress.com/docs/result/index.php?id=686cdf90900df8e7f86874e6)  
- [MITRE ATT&CK – Formbook](https://attack.mitre.org/software/S0417/)  
- [VirusTotal Malware Sample](https://www.virustotal.com/gui/file/6d0875ec12b1e0fb5b2b3cc6c9e056d0fda67ec570ec4be0294568b80c87f576)  
- [Malpedia – Formbook](https://malpedia.caad.fkie.fraunhofer.de/details/win.formbook)  

---

**Prepared by:**  
**Javier Napoles**  
SOC Analyst Candidate | July 2025
