# 🛡️ Mini SOC Implementation with Micro-Segmentation

## 📌 Overview
This 3-month lab project simulates the real-world responsibilities of a Tier 1–2 SOC Analyst through the creation of a home-based SOC environment. Using virtual machines, open-source security tools, and threat simulation techniques, the project emphasizes core SOC duties such as SIEM management, alert triage, network defense, micro-segmentation, threat hunting, and vulnerability assessment.

---

## 📅 Duration
**3 months**  
**Schedule:** Monday to Thursday, 2 hours/day

---

## 🎯 Objectives
- Build a virtual SOC lab environment
- Practice alert detection and incident triage
- Implement micro-segmentation and zero-trust concepts
- Conduct threat hunting and vulnerability assessments
- Develop professional documentation and playbooks

---

## 🔁 Project Structure

### 📁 Month 1: SOC Foundations & Lab Setup
#### Week 1–2: Lab Environment
- Research SOC roles and responsibilities
- Set up virtual machines (Windows 10, Kali Linux, Ubuntu Server)
- Configure internal or bridged networking
- Create a network topology diagram

#### Week 3–4: Micro-Segmentation & Simulated Attacks
- Run port scans and brute-force attacks
- Apply firewall rules (`iptables`, `ufw`, Windows Defender)
- Block and test lateral movement between VMs

### 📁 Month 2: SIEM & Alert Response
#### Week 5–6: SIEM Setup
- Install and configure SIEM (Wazuh / ELK / Splunk Free)
- Collect logs using Winlogbeat, Filebeat, Auditd
- Build dashboards and verify log flow

#### Week 7–8: Detection Rules & Triage
- Create detection rules for failed logins, new users, and suspicious files
- Simulate alerts and analyze results
- Write Tier 1 incident response playbooks

### 📁 Month 3: Threat Intel & Vulnerability Management
#### Week 9–10: Threat Hunting
- Use OTX, MISP, AbuseIPDB to gather IOCs
- Search logs for indicators of compromise
- Document threat-hunting workflow

#### Week 11–12: Vulnerability Scanning & Final Report
- Scan systems using Nmap and OpenVAS
- Identify and prioritize vulnerabilities
- Document mitigation strategies
- Create a final project report and optional presentation

---

## 🧠 Skills Gained

### SOC Operations
- Alert triage, escalation, and documentation
- Incident playbook creation

### Virtualization & Network Defense
- VM configuration and internal network setup
- Micro-segmentation and firewall rule design

### SIEM & Logging
- SIEM deployment and log ingestion
- Detection engineering and rule creation

### Threat Hunting & Intel
- IOC analysis and enrichment
- Structured hunting across logs

### Vulnerability Management
- Risk analysis using CVSS scores
- Patch and hardening recommendations

### Communication & Documentation
- Professional reporting and dashboarding
- Presentation of security findings

---

## 🛠️ Tools Used

| Category             | Tools                          |
|----------------------|--------------------------------|
| Virtualization       | VirtualBox / VMware Player     |
| Operating Systems    | Windows 10, Kali Linux, Ubuntu |
| SIEM                 | Wazuh, ELK Stack, Splunk Free  |
| Log Forwarders       | Filebeat, Winlogbeat, Auditd   |
| Simulation Tools     | Nmap, Hydra, Metasploit (opt)  |
| Firewalls            | iptables, UFW, Win Defender    |
| Threat Intelligence  | OTX, MISP, AbuseIPDB, CyberChef|
| Vulnerability Scans  | Nmap, OpenVAS                  |

---

## 🌐 Optional: SOC Playbook Guide

Build an interactive playbook for:
- Phishing
- Malware
- Ransomware
- Unauthorized access

**Tools:** draw.io, Miro, Notion, or static web pages.

---

## 📁 Deliverables

- ✅ Network topology diagram  
- ✅ Screenshots of VM setup, SIEM dashboards, and alerts  
- ✅ Firewall and segmentation documentation  
- ✅ Alert triage playbooks  
- ✅ IOC report and threat hunting checklist  
- ✅ Vulnerability scan reports  
- ✅ Final project summary report and optional slide deck

---

## 📚 License
This lab project is for educational and portfolio-building purposes only.
