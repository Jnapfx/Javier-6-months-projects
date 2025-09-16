# 🛡️ DAE Projects – SOC Analyst Overview

A **SOC Analyst** (Security Operations Center Analyst) is a cybersecurity professional responsible for **monitoring, detecting, investigating, and responding** to security threats in real-time. They are the **first line of defense** within an organization’s cybersecurity infrastructure.

---

## 📌 Table of Contents

1. [Role Overview](#role-overview)
2. [Skills Needed](#skills-needed)
3. [Common Tools](#common-tools)
4. [Recommended Certifications](#recommended-certifications)
5. [Day-to-Day Responsibilities](#day-to-day-responsibilities)
6. [Challenges Faced](#challenges-faced)
7. [Career Goal](#career-goal)
8. [Real-World Project: Phishing Playbook](#real-world-project-phishing-playbook)
    - [Project Title](#project-title)
    - [Objective](#objective)
    - [Context](#context)
    - [Tools & Technologies](#tools--technologies)
    - [Project Tasks](#project-tasks)
    - [Deliverables](#deliverables)
    - [Challenges](#project-challenges)
    - [Outcome](#outcome)
    - [References](#references)

---

## 🔍 Role Overview

SOC Analysts operate in a high-stakes environment where their primary job is to **monitor and respond to cyber threats** using a variety of tools and techniques to protect the organization.

---

## 🧠 Skills Needed

- Understanding of network protocols, firewalls, and operating systems
- Experience with SIEM tools
- Basic scripting (Python, Bash, or PowerShell)
- Knowledge of cyber threats like malware, phishing, DDoS, etc.

---

## 🛠️ Common Tools

| Category              | Tools                                         |
|-----------------------|-----------------------------------------------|
| SIEM                  | Splunk, QRadar, Elastic                       |
| Endpoint Detection    | CrowdStrike, SentinelOne                      |
| Threat Intel Feeds    | VirusTotal, MISP                              |
| Ticketing Systems     | Jira, ServiceNow                              |

---

## 🎓 Recommended Certifications

- **CompTIA Security+** – Great for beginners
- **Certified SOC Analyst (CSA)** – EC-Council
- **Splunk Core Certified User**
- **GCIA** or **GCIH** – Advanced

---

## 📅 Day-to-Day Responsibilities

### 🔁 Morning Review
- Review overnight alerts and incidents
- Investigate critical events from the previous shift

### 👀 Continuous Monitoring
- Monitor logs and network traffic for anomalies using SIEM tools
- Watch for IOC matches and suspicious behavior

### ⚠️ Incident Triage & Investigation
- Determine false positives vs real threats
- Prioritize incidents by severity and impact

### 🚨 Incident Response & Mitigation
- Isolate affected systems
- Apply patches or containment steps
- Collaborate with the IR team to restore operations

### 🧠 Threat Intelligence
- Analyze CVEs and attack patterns
- Stay current using VirusTotal, Shodan, MISP, etc.

### 🤝 Team Collaboration
- Work with IT, legal, HR, and compliance teams
- Escalate critical issues appropriately

### 📝 Documentation
- Maintain detailed reports and logs
- Track incident lifecycle and control performance

### 🔍 Proactive Assessments
- Assist with vulnerability scans, threat hunting, pen testing (Tier 2+)

### 📋 Compliance Oversight
- Ensure alignment with NIST, CIS Controls, HIPAA, GDPR, etc.

---

## ⚠️ Challenges Faced

- **Alert Fatigue** – Managing a high volume of alerts daily
- **Time Pressure** – Swift response during live threats
- **Evolving Threats** – Adapting to new vulnerabilities and tactics

---

## 🎯 Career Goal

> Ensure the **security and resilience** of an organization’s digital environment by **detecting and responding** to threats before they cause harm.

---

# 📍 Real-World Project: Phishing Email Detection and Response Playbook

---

## 📌 Project Title
**Develop and Implement a SOC Playbook for Phishing Email Incidents**

---

## 🎯 Objective

Design and document a **repeatable incident response process** for detecting and responding to phishing emails within a SOC.

---

## 🧠 Context

The organization has seen a **spike in phishing attempts**. As a SOC Analyst, the goal is to build a structured playbook that enables early detection, consistent response, and minimal impact.

---

## 🛠️ Tools & Technologies

| Category            | Tools Used                                 |
|---------------------|---------------------------------------------|
| SIEM                | Splunk, Wazuh, Azure Sentinel               |
| Email Security      | Microsoft Defender for Office 365, Proofpoint |
| Threat Intelligence | VirusTotal, AbuseIPDB, URLScan.io          |
| EDR/AV              | CrowdStrike, SentinelOne                    |
| Ticketing System    | Jira, ServiceNow                            |
| Scripting           | Python, PowerShell                          |
| Frameworks          | MITRE ATT&CK, NIST IR Framework             |

---

## ✅ Project Tasks

### 1. Email Monitoring Integration
- Ingest logs from email gateways into SIEM
- Build detection rules for:
  - Suspicious senders and domains
  - Malicious attachments
  - Known phishing URLs and IOCs

### 2. Alert Triage Workflow
- Develop a checklist:
  - Header analysis
  - Sender verification
  - User engagement review

### 3. Threat Intel & IOC Analysis
- Extract IOCs (IPs, URLs, hashes)
- Use tools like VirusTotal and Hybrid Analysis
- Map to MITRE ATT&CK (e.g., T1566.001)

### 4. Response & Containment
- Quarantine emails
- Block malicious indicators (IPs, URLs)
- Isolate affected devices
- Reset user credentials

### 5. Playbook Development
- Document all response steps
- Include:
  - Flowcharts
  - Communication matrix
  - Escalation tree
  - Screenshots and sample ticket data

### 6. Training & Simulation
- Run simulated phishing attacks
- Measure:
  - MTTD (Mean Time to Detect)
  - MTTR (Mean Time to Respond)
  - Tier 1 accuracy in escalation

---

## 📄 Deliverables

- `phishing-playbook.pdf` – Step-by-step incident response guide
- `ioc-checklist.xlsx` – IOC tracking and validation template
- `alert-queries.conf` – SIEM queries and detection rules
- `simulation-report.md` – Metrics and insights from phishing drills

---

## 🚧 Project Challenges

- Reducing false positives in alerting
- Keeping IOC libraries and feeds current
- Standardizing Tier 1 responses across shifts

---

## 🏁 Outcome

A robust and repeatable phishing playbook that:
- Increases SOC efficiency
- Reduces response time
- Enhances analyst readiness

---

## 📚 References

- [MITRE ATT&CK T1566](https://attack.mitre.org/techniques/T1566/)
- [NIST Incident Handling Guide SP 800-61](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf)
