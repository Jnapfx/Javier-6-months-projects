# 3rd Semester Summary 
*Author: Javier Napoles* &nbsp;|&nbsp; *Date: July 31, 2025*

This project simulates the core responsibilities of a SOC Analyst by building a functional lab environment using virtual machines and open-source tools. It emphasizes practical skills in threat detection, alert triage, and incident response. A key focus is the use of micro-segmentation as a proactive defense strategy to enhance network security.

---

## 1&nbsp;&nbsp;Lab Foundations

| Area | What I Did | Key Screenshot |
|------|------------|----------------|
| **Virtualization** | Built a dual-VM lab in **UTM**, installing Parrot OS and Kali Linux side-by-side. | ![Parrot OS Desktop](images/Parrot_OS.png) |
| **Networking** | Created an **internal network** so the VMs can ping, scan, and attack each other—my sandbox for every exercise that followed. | *(Add your preferred network-test screenshot here if desired)* |

---

## 2&nbsp;&nbsp;Governance & Policy

| Area | What I Did |
|------|------------|
| **Comprehensive Security Policy** | Wrote a single policy that maps every control back to the **CIA triad**. |
| **Legal & Ethical Compliance** | Added language on data-handling laws and professional codes of conduct. |
| **Incident Response Plan (IRP)** | Drafted a lightweight IRP so every technical exercise ties back to process. |

*(No screenshots needed—policy text lives in `documentation/cybersecurity_basics_1/comprehensive_security_policy/`.)*

---

## 3&nbsp;&nbsp;Core Security Tools & Concepts

| Topic | Hands-On Work | Screenshot |
|-------|---------------|------------|
| **Encryption Refresher** | Practiced AES encryption/decryption and generated MD5 & SHA hashes to compare strengths and weaknesses. | ![AES Example](images/AES_encryption_example.png)<br>![MD5 Hash](images/MD5_hash.png)<br>![SHA Hash](images/SHA.png) |
| **Baseline Scanning** | Ran **Nmap** service-detection scans to fingerprint hosts and spot open ports. | ![Nmap Host Scan](images/Nmap_scan.png) |

---

## 4&nbsp;&nbsp;Threat Analysis & Offensive Practice

| Exercise | What I Learned | Screenshot |
|----------|----------------|------------|
| **Malware Analysis** | Submitted `FSP-0991.exe` to **VirusTotal**, reviewed detections, and documented key IOCs & behaviors. | ![VirusTotal Summary](images/virustotal_summary.png) |
| **Phishing Simulation** | Used the **Social Engineering Toolkit (SET)** to clone a Google login page in lab. | ![Launching SET](1_Launching_SET.png)<br>![Cloned Page](images/5_Site_Cloner.png) |
| **APT Research** | Mapped a real Dridex-style campaign to **MITRE ATT&CK** tactics & techniques. | ![MITRE ATT&CK Mapping](images/MITRE_ATT&CK.png) |

---

## 5&nbsp;&nbsp;Vulnerability Assessment & Risk Management

| Step | Output | Screenshot |
|------|--------|------------|
| **Asset Discovery** | Enumerated hosts/services with an Nmap sweep. | ![Asset Discovery](images/2_asset-discovery_can.png) |
| **OpenVAS Scan** | Generated a detailed vulnerability list with severity ratings. | ![OpenVAS Scan](images/5_vulnerability_scan.png) |
| **Network Mapping** | Produced a quick **network map** to visualize exposure. | ![Network Map](images/4_network_mapping.png) |
| **Risk Treatment** | Flagged two critical risks and proposed patching + segmentation; created a basic risk-monitoring checklist. | *(Checklist lives in the project docs)* |

---

## 6&nbsp;&nbsp;Threat Intelligence Implementation

| Task | Proof-of-Work | Screenshot |
|------|--------------|------------|
| **OpenCTI Deployment** | Brought up **OpenCTI** via Docker Compose and verified successful login. | ![OpenCTI Login](images/opencti_login.png) |
| **Connector Integration** | Enabled two data-feed connectors; containers show healthy state. | ![Docker Containers](images/docker_containers.png)<br>![MITRE/ATLAS Connector Active](images/03_connectors_mitre_atlas_active.png) |
| **IoC Lifecycle** | Parsed two IoCs end-to-end—collection, enrichment, contextual pivoting inside OpenCTI. |

---

### Next Up
1. Finish tuning Wazuh dashboards and add more targeted detection rules.  
2. Begin micro-segmentation experiments to isolate critical lab assets.  
3. Enrich OpenCTI with custom malware-family data and automation scripts.

---

> **How to use:** Clone the repo, keep the `documentation/` folder structure unchanged, and this README will render with all screenshots inline.
