# Semester 3
---
# DAE Projects – General Overview

Welcome to the DAE Projects repository! This single README provides a concise summary of each subproject, explains their goals, and outlines usage or key concepts. 

---

# 🛡️ Cybersecurity Project: Basics & Threats Analysis

## 📁 Table of Contents
- [Overview](#overview)
- [Cybersecurity Basics 1](#cybersecurity-basics-1)
  - [Incident Response Plan](#incident-response-plan)
  - [Security Policy](#security-policy)
  - [Encryption Techniques](#encryption-techniques)
  - [Legal and Ethical Compliance](#legal-and-ethical-compliance)
- [Cyber Threats and Vulnerabilities 1](#cyber-threats-and-vulnerabilities-1)
  - [Cyber Threat Analysis](#cyber-threat-analysis)
  - [Vulnerability Assessment](#vulnerability-assessment)
  - [Threat Intelligence Implementation](#threat-intelligence-implementation)
  - [Risk Management Strategies](#risk-management-strategies)
  - [Security Monitoring & Incident Response](#security-monitoring--incident-response)
- [Conclusion](#conclusion)

---

## 🧭 Overview
This project demonstrates a foundational understanding of cybersecurity through practical exercises and documentation. It includes core tasks such as incident response planning, encryption, legal compliance, malware analysis, phishing simulation, threat intelligence integration, and more.

---

## 🧩 Cybersecurity Basics 1

### 🔥 Incident Response Plan

**Detection Method:**
- Network monitoring via SIEM tools (e.g., Wazuh or Splunk)
- Log analysis and anomaly detection

**Containment Strategy:**
- Isolate affected systems from the network
- Disable compromised user accounts

**Eradication & Recovery:**
- Remove malware using antivirus/EDR tools
- Apply security patches
- Restore from backups
- Monitor for recurring threats

**Attack Type Identified:**
- **Phishing:** Deceptive emails used to trick users into revealing sensitive data or installing malware.

---

### 📜 Security Policy

**Security Rules/Guidelines:**
1. Use multi-factor authentication (MFA) on all critical systems.
2. Enforce strong password policies (minimum length, complexity, expiration).
3. Regularly update and patch software and systems.

**Incident Response Plan (Summary):**
- Detection → Containment → Eradication → Recovery → Lessons Learned

**CIA Triad Compliance:**
- **Confidentiality:** Access control and encryption
- **Integrity:** Hash checks and secure backups
- **Availability:** Redundant systems and incident recovery planning

---

### 🔐 Encryption Techniques

**Example using AES (Python):**
- Encrypted Text: `U2FsdGVkX1+Z7op3vS5F9k==`
- Decrypted Plain Text: `CybersecurityRocks!`

**Hashing Example (SHA-256):**
- Input: `CyberSec123`
- Hash Output: `b1cf4f0146d09a69...`

---

### ⚖️ Legal and Ethical Compliance

**Relevant Laws/Regulations:**
1. **GDPR** – Protects EU citizens' data privacy
2. **HIPAA** – Ensures healthcare data security

**Ethical Consideration:**
- Do no harm: No unauthorized access or exploitation of systems during assessments

**Plan Compliance:**
- Logs user consent
- Ensures incident actions respect privacy laws
- Only authorized personnel perform scans or containment

---

## 🧠 Cyber Threats and Vulnerabilities 1

### 🦠 Cyber Threat Analysis

**Malware Sample Analysis:**
- Platform: VirusTotal
- Detection: Flagged by 43 AV engines
- Indicators:
  - Suspicious registry changes
  - C2 server contact
- Potential Impact: Data exfiltration, system slowdown

**Phishing Template (SET - Kali Linux):**
- Spoofed Office365 login
- Collected credentials from test victim

**APT Campaign Mapping:**
- Campaign: APT29 (Cozy Bear)
- MITRE Techniques: `T1566` (Phishing), `T1059` (Command Scripting)

---

### 🔍 Vulnerability Assessment

**Tool Used:** Nmap

**Vulnerability Scan:**
- Scan Flags: `nmap -sV -sC -T4 192.168.1.1/24`
- Findings: Open ports on outdated Apache server
- Classification: High (CVE-2021-41773)

**Asset Discovery:**
- Hosts: 15 devices
- Critical Asset: Domain Controller (DC01)
- Services: AD, DNS, HTTP

---

### 🧠 Threat Intelligence Implementation

**IoC Analysis:**
- Example 1: Malicious IP 45.155.205.233 → Detected in firewall logs
- Example 2: Hash `9f86d081...` → Matches known ransomware

**OpenCTI Platform:**
- Installed via Docker
- Configured Connectors:
  1. MISP (threat sharing)
  2. MITRE ATT&CK matrix
- Screenshot proof of IOC ingestion and entity linking

---

### 🛡️ Risk Management Strategies

**Risk Identification from Nmap:**
1. Apache 2.4.49 RCE (Critical)
2. SMBv1 enabled (High)

**Treatment Recommendations:**
- Patch Apache
- Disable SMBv1, upgrade to SMBv3

**Risk Monitoring Procedure:**
- Weekly vulnerability scans
- Risk dashboard (Excel or ELK) tracking status (Open, Mitigated, Closed)

---

### 🧭 Security Monitoring & Incident Response

**Monitoring Use Case:**
- Rule: Alert if login outside business hours
- Priority: Medium
- Response: User notified, credentials reset

**Incident Response Scenario:**
- Classification: Insider threat
- Action: Account deactivation, forensic review
- Lessons: Implement behavior analytics

---

## ✅ Conclusion

This project provides a hands-on approach to essential cybersecurity principles and practices. From creating incident response plans to executing threat intelligence platforms, it demonstrates practical proficiency and awareness of real-world cyber threats, legal implications, and defense mechanisms.



## Credits & Contact

If you have questions, suggestions, or want to contribute to any subproject, please feel free to reach out:

- **Author:** Javier Napoles  
- **Email:** jnapfx@gmail.com  

We hope you find these resources helpful for learning algorithms, Unix, AI concepts, and building Python-based GUIs for a real-world application. Enjoy exploring the DAE Projects!

## 🔗 Connect With Me

- [💼 LinkedIn](https://www.linkedin.com/in/javier-napoles-3513031a7)  
- [🐙 GitHub](https://jnapfx.github.io/Javier-6-months-projects/)  
- [📄 Resume](https://jnapfx.github.io/Javier-6-months-projects/assets/files/JAVIER_RESUME.pdf)


---


## Special Thanks


Kyley Komschlies

Kakra Detome

Abhinav Piratla

Devanshi Tandel

Sakshi Goenka

