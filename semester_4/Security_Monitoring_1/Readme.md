# Security Monitoring 1: Wazuh Lab Deployment & Analysis

This project focuses on deploying a real-time security monitoring environment using Wazuh and open-source tools. It simulates the key responsibilities of a Security Monitoring Analyst, from environment setup and log analysis to reporting and dashboarding. The project prioritizes interpretation skills, alert validation, and proper monitoring workflows.

> 🚧 This work is part of my ongoing 4th semester in cybersecurity studies. The project is still expanding as I test new alert rules, refine log analysis techniques, and build more effective dashboards.

---

## Project Breakdown (Security Monitoring 1)

### 1. Monitoring Environment Setup
- Installed and configured Wazuh as the primary SIEM.
- Verified log collection from at least **2 different sources** (e.g., Windows + Linux).
- Created alert rules for **3 different scenarios**:  
  - Authentication activity  
  - File access  
  - Network traffic
- Built an alert routing and notification system.
- Included evidence with dashboard screenshots, config files, and sample log triggers.

### 2. Security Event Analysis
- Interpreted **3 types of security logs** using a consistent analysis methodology.
- Demonstrated **basic correlation** across different log types.
- Documented a complete incident detection timeline with:
  - Severity classification  
  - False positive evaluation  
  - Escalation paths
- Included annotated log excerpts and investigation notes.

### 3. Monitoring Implementation
- Designed a monitoring architecture diagram with data flow visuals.
- Integrated **3+ different data sources** and verified collection success.
- Established baselines for performance monitoring (e.g., CPU, memory, and disk).
- Configured health monitoring for:
  - Collection status  
  - Storage utilization  
  - Processing performance
- Included config files and baseline measurements.

### 4. Security Reporting
- Used a standardized alert documentation template across **3 different alert types**.
- Created a **security summary report** showing:
  - Trends  
  - High-severity events  
  - Actionable recommendations
- Built and documented a real-time dashboard with appropriate visualizations.
- Followed professional reporting standards for organization and clarity.

---

## Tools & Platforms Used
- 🛡️ Wazuh (SIEM & agent management)
- 🐧 Parrot OS + Windows VM (via UTM)
- 📡 Filebeat / Winlogbeat (log shipping)
- 🖥️ Dashboards via Kibana / Wazuh web UI
- 📁 Markdown / Mermaid (documentation & diagrams)

---

## 🚀 Ongoing Improvements
- Fine-tuning log correlation and alert thresholds
- Automating health checks and system diagnostics
- Adding more granular file integrity monitoring
- Enhancing dashboard with better filtering and visualization tools

