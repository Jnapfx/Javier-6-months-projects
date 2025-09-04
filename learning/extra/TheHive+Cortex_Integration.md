# 🐝 TheHive + Cortex Integration

## 📌 Overview  
To extend the **Divide and Defend SOC Project**, TheHive and Cortex were introduced as a **Security Incident Response Platform (SIRP)** and **analysis engine**.  
- **Wazuh** detects and generates alerts.  
- **TheHive** organizes alerts into **cases** with investigation workflows.  
- **Cortex** enriches these cases by analyzing observables (IOCs) and performing automated responses.  

This integration adds an **enterprise-level workflow** for incident handling: detection, investigation, enrichment, response, and documentation.  

---

## ⚙️ Components  

### 🔹 TheHive (SIRP Platform)  
- Manages **incidents as cases**.  
- Provides dashboards for:  
  - Incident timeline.  
  - Tasks and assignments.  
  - Case resolution tracking.  
- Cases contain **observables** (IPs, domains, file hashes) extracted from alerts.  

### 🔹 Cortex (Analysis & Response Engine)  
- Executes **analyzers** to enrich observables:  
  - VirusTotal → malware/hash lookups.  
  - AbuseIPDB → IP reputation checks.  
  - Shodan → open services on suspicious IPs.  
- Provides **responders** for automated actions:  
  - Blocking IPs.  
  - Exporting indicators to Wazuh for active response.  

---

## 🔄 Workflow  

1. **Detection in Wazuh**  
   - Example: Wazuh detects SSH brute force attempt on Parrot OS VM.  
   - Alert details: attacker IP, log source, number of attempts.  

2. **Case Creation in TheHive**  
   - Analyst opens a new case:  
     - Title: *SSH Brute Force Detected on Parrot-VM1*.  
     - Description: *3 failed login attempts within 60s*.  
     - Observable: Attacker IP `192.168.1.110`.  

3. **IOC Analysis via Cortex**  
   - From TheHive, analyst sends attacker IP to Cortex analyzers.  
   - Example output:  
     - VirusTotal → IP flagged in malware campaigns.  
     - AbuseIPDB → Confidence score 95% malicious.  

4. **Response Actions**  
   - Cortex responder pushes IP back to Wazuh for **active response**.  
   - Alternatively, IP is added to a blocklist (firewall/IDS).  

5. **Documentation in TheHive**  
   - Timeline shows all actions: detection, analysis, response.  
   - Case can be closed once incident is contained.  

---

## 📊 Benefits  

- **Structured Incident Management** → cases, tasks, timelines.  
- **Automation** → IOC enrichment and response with Cortex.  
- **Collaboration** → SOC analysts can share notes and workflows.  
- **Integration** → Works alongside Wazuh (detection) and OpenCTI (threat intel).  

---

## ✅ Example in Project Context  

- **Wazuh Alert**: SSH brute force on Parrot-VM1.  
- **TheHive Case**: Created with attacker IP as observable.  
- **Cortex Analyzer**: Confirms IP reputation as malicious.  
- **Cortex Responder**: Sends attacker IP to Wazuh active response → blocked.  
- **Outcome**: Incident detected, analyzed, contained, and documented using an enterprise SOC workflow.  

---

## 🔗 References  
- [TheHive Project](https://thehive-project.org/)  
- [Cortex Documentation](https://www.strangebee.com/cortex/)  
- [Wazuh Integration Docs](https://documentation.wazuh.com/)  
