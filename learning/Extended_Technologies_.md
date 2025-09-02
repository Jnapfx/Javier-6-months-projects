# 🚀 Extended Technologies in *Divide and Defend* SOC Project

This document provides an overview of additional technologies integrated into the **Divide and Defend: Mini SOC with Micro-Segmentation** project.  
Each tool enhances detection, analysis, and response capabilities of the SOC environment.

---

## 📊 Grafana Integration

### What is Grafana?
Grafana is an **open-source monitoring and visualization platform**. It allows analysts to build **interactive dashboards** that present SOC data in a clear, visual way. Instead of reading raw logs, alerts can be displayed as **graphs, charts, and tables**, making patterns easier to identify.

### Key Features
- Custom dashboards (line charts, tables, heatmaps).
- Real-time alerts via email, Slack, or Teams.
- Multi-source support (Elasticsearch, Prometheus, SQL, etc.).
- Filters and drill-down by host, IP, or timeframe.
- Community dashboards for security monitoring.

### Role in the SOC Project
- **Wazuh (SIEM):** Collects, correlates, and stores security logs in Elasticsearch.
- **Grafana (Visualization):** Connects to Elasticsearch, builds dashboards for incident trends, attacker IPs, and host activity.
- Provides a professional interface for **reporting and presentations**.

### Value
- More advanced visualization than Kibana.
- Ability to combine Wazuh alerts with data from other tools (e.g., OpenVAS).
- Portfolio-ready dashboards attractive for recruiters.

---

## 🕵️‍♂️🦖 Velociraptor Integration

### What is Velociraptor?
Velociraptor is an **open-source endpoint forensics and threat hunting platform** developed by Rapid7.  
It enables SOC analysts to **query endpoints in real time** with its query language (**VQL**) to collect forensic evidence and detect suspicious activity.

### Key Features
- Real-time endpoint hunting (processes, files, connections).
- Forensic artifact collection (command history, hashes, registry).
- Custom hunting rules with VQL.
- Incident support by validating SIEM alerts with endpoint evidence.

### Role in the SOC Project
- **Wazuh (SIEM):** Detects brute force, DoS, and suspicious logins.
- **Velociraptor:** Deployed as a Docker server on macOS with agents on Parrot OS VMs.  
  Executes hunts after Wazuh raises an alert to validate impact.

### Value
- Adds an **endpoint forensics layer** beyond log analysis.
- Supports **proactive threat hunting workflows**.
- Provides **incident validation**: determines if alerts are real compromises.
- Strengthens professional depth of the SOC project.

### Example Use Cases
- **Brute Force Alert:** Query for new accounts or tokens created post-attack.
- **Suspicious Process:** Collect process tree and hash for threat intel check.
- **Incident Timeline:** Correlate Wazuh alerts with forensic evidence.

---

## 🐝 TheHive + Cortex Integration

### Overview
**TheHive** and **Cortex** extend the project as a **Security Incident Response Platform (SIRP)** and **analysis engine**.  
- Wazuh generates alerts.  
- TheHive organizes them into **cases** with investigation workflows.  
- Cortex enriches observables (IOCs) and performs **automated responses**.

### Components
- **TheHive:** Case management, tasks, timelines, observables.
- **Cortex:** Analyzers (VirusTotal, AbuseIPDB, Shodan) and responders (block IPs, export indicators).

### Workflow
1. Wazuh detects an incident (e.g., SSH brute force).
2. TheHive creates a case with observables (attacker IP).
3. Cortex enriches the IP with external reputation checks.
4. Cortex responder blocks the IP or exports to Wazuh for active response.
5. All steps documented in TheHive timeline.

### Benefits
- Structured incident management with cases and tasks.
- Automated IOC enrichment and response.
- Collaboration for SOC analysts.
- Strong integration with Wazuh and OpenCTI.

### Example in Context
- Wazuh alert → TheHive case created → Cortex confirms IP is malicious → Responder blocks IP → Case documented and closed.

---

## ✅ Summary of Value
- **Grafana:** Professional visualization and reporting layer.  
- **Velociraptor:** Endpoint forensics and proactive hunting.  
- **TheHive + Cortex:** Structured incident response with enrichment and automation.  

Together, these technologies transform the *Divide and Defend* Mini SOC into a more **enterprise-grade SOC environment** with advanced visibility, validation, and response capabilities.

