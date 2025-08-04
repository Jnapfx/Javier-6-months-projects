
# 📄 **Project Documentation**

## **Project Title**
**Divide & Defend: A Hands-On SOC Lab Project with Micro-Segmentation**  
Version: 1.0  
Date: June 17, 2025

---

## **Overview**

This project simulates the core responsibilities of a Security Operations Center (SOC) Analyst by building a fully functional lab using virtual machines (VMs) and open-source tools. It emphasizes hands-on practice with:

✅ Threat detection  
✅ Alert triage  
✅ Incident response  
✅ Micro-segmentation (to block lateral movement)

The lab enables cybersecurity students, career changers, and junior professionals to **gain Tier 1–2 SOC skills** from home.

---

## **Problem Statement**

Many aspiring SOC analysts **lack practical environments** to learn detection, defense, and response workflows. This project solves that by offering:

- A realistic virtual SOC setup
- Simulated attacks and detections
- Micro-segmentation as an advanced defensive strategy
- Full incident documentation and reporting practice

---

## **Target Users**

- Cybersecurity students & bootcamp participants  
- Career changers entering security roles  
- Junior SOC analysts looking to build confidence  
- Small IT teams prototyping defensive setups

---

## **Project Goals & Objectives**

- Build a realistic SOC lab with **Windows, Kali Linux, and Ubuntu** VMs
- Configure SIEM (Wazuh, ELK, or Splunk Free) to **ingest & analyze logs**
- Apply **firewall and micro-segmentation** to restrict unauthorized access
- Simulate **real-world attacks** (e.g., brute-force, port scans) and detect them
- Perform **alert triage, threat hunting, and vulnerability scanning**
- Document findings in professional-grade reports

---

## **Key Features**

- 🔧 **Virtual SOC Lab Deployment** (VMs + networking)
- 🚨 **Attack Simulation & SIEM Detection**
- 🛡️ **Micro-Segmentation Implementation**
- 📝 **Incident Triage & Reporting**
- 🔍 **Threat Hunting with IOC Enrichment**
- 🔓 **Vulnerability Scanning & Prioritization**

---

## **Tech Stack**

| Category                | Tools / Platforms                                          |
|-------------------------|----------------------------------------------------------|
| Virtualization         | VirtualBox, VMware, UTM                                  |
| Operating Systems      | Windows 10, Kali Linux, Ubuntu Server                    |
| SIEM Platforms        | Wazuh, ELK Stack, Splunk Free                            |
| Log Agents            | Winlogbeat, Filebeat, Auditd                              |
| Firewall Tools       | iptables, UFW, Windows Defender Firewall                  |
| Attack Tools         | Nmap, Hydra, optional Metasploit                          |
| Threat Intel Tools  | OTX, AbuseIPDB, MISP, CyberChef                           |
| Vulnerability Scanners | Nmap, OpenVAS (optional)                                 |
| Documentation Tools | Monday.com, Figma, draw.io, Lucidchart, screenshots        |

---

## **Architecture & Workflow**

1️⃣ **Initialize Lab Environment**  
- Install VirtualBox/VMware/UTM  
- Set up Windows, Kali, Ubuntu VMs  
- Configure networking (bridged or internal)

2️⃣ **Verify Connectivity**  
- Test with `ping` or `traceroute`  
- Check interfaces and adapters

3️⃣ **Configure SIEM**  
- Install SIEM on Ubuntu  
- Deploy Winlogbeat/Filebeat/Auditd on endpoints  
- Validate log flow

4️⃣ **Simulate Attacks**  
- Nmap port scans  
- Hydra brute-force  
- Confirm detections

5️⃣ **Apply Micro-Segmentation**  
- Set firewall rules on Linux (iptables/UFW) & Windows Defender  
- Block lateral moves  
- Test bypass attempts

6️⃣ **Create Detection Rules**  
- Monitor failed logins, user creations, suspicious files  
- Generate SIEM alerts

7️⃣ **Perform Alert Triage**  
- Investigate alerts  
- Flag false positives/true threats  
- Document actions

8️⃣ **Conduct Threat Hunting**  
- Import IOCs from OTX, MISP, AbuseIPDB  
- Search SIEM logs

9️⃣ **Run Vulnerability Scans**  
- Nmap/OpenVAS scans  
- Prioritize fixes

🔟 **Generate Final Report**  
- Include topology, rules, segmentations, IOCs, scan results

---

## **Folder Structure (Recommended)**

```
/SOC-Lab-Project
│
├── README.md                 ← Project overview
├── /diagrams                 ← Network & segmentation diagrams
├── /scripts                  ← Bash, PowerShell, detection scripts
├── /reports
│   ├── Final_Report.pdf      ← Full lab documentation
│   └── /Incident_Reports     ← Individual incident write-ups
├── /screenshots              ← Proof of work (alerts, scans, configs)
└── LICENSE (optional)
```

---

## **Weekly Timeline**

| Week | Focus                                      |
|------|-------------------------------------------|
| 1    | Introduction, lab setup                   |
| 2    | VM deployment, networking                |
| 3    | Simulate attacks                         |
| 4    | Implement micro-segmentation            |
| 5    | SIEM configuration                     |
| 6    | Alert triage (Tier 1 focus)            |
| 7    | Build alert rules                      |
| 8    | Practice incident triage              |
| 9    | Threat hunting, IOC enrichment        |
| 10   | Log searches for real-world threats   |
| 11   | Vulnerability scanning               |
| 12   | Final report & project summary      |

---

## **Risks & Mitigation**

| Risk                                 | Mitigation Strategy                                      |
|--------------------------------------|----------------------------------------------------------|
| VM misconfiguration                  | Use detailed setup checklists; test networking early    |
| SIEM ingestion failures             | Follow official guides; test log events per agent      |
| Attack simulations not triggering   | Validate rule logic with known-good payloads           |
| Alert overload / false positives    | Tune SIEM rules; document normal behavior             |
| Host system performance issues      | Allocate VM resources conservatively; stagger phases  |

---

## **Evaluation Criteria**

✅ All VMs functional & networked  
✅ SIEM detects & logs simulated attacks  
✅ Firewall rules block unauthorized access  
✅ Incident response actions documented  
✅ Final report delivered with clear findings

---

## **Future Enhancements**

- Upgrade OS/tools regularly  
- Expand to cloud-based SOC setup (AWS/Azure)  
- Integrate EDR/XDR solutions  
- Automate lab deployment with scripts
- AI integration

---

## **Creative Delivery Ideas (Optional)**

- Gamified report (“Mission: Secure the Lab”)  
- Interactive Notion portfolio with embedded media  
- Canva/Figma infographic summaries  
- Video walkthrough of lab with commentary  
- GitHub Pages site for public showcase

---

## **Final Deliverables**

✅ README or project summary  
✅ Final report (PDF/Markdown)  
✅ Screenshots of key steps  
✅ Diagrams of network, segmentation, detection flow  
✅ Scripts or configs used  
✅ (Optional) Video demo or portfolio link
