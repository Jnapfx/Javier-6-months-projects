# 🕵️ 🦖Velociraptor Integration in Divide and Defend SOC Project  

## What is Velociraptor?  
Velociraptor is an **open-source endpoint forensics and threat hunting platform** developed by Rapid7.  
It allows SOC analysts to **query endpoints in real time** using its query language (**VQL**) to collect forensic evidence, detect suspicious activity, and hunt for adversaries across the environment.  

---

## Key Features  
- **Real-Time Endpoint Hunting** → Query processes, files, and network connections.  
- **Forensic Collection** → Gather artifacts (command history, hashes, registry, persistence mechanisms).  
- **Custom Queries with VQL** → Write your own hunting rules.  
- **Incident Support** → Investigate alerts from SIEM with endpoint evidence.  

---

## Role in the SOC Project  
In the *Divide and Defend* Mini SOC, Velociraptor enhances the existing Wazuh-based SIEM:  

- **Wazuh (SIEM)**  
  - Detects brute force, DoS, and suspicious login attempts.  
  - Generates alerts from logs sent by Parrot OS agents.  

- **Velociraptor (Forensics & Hunting)**  
  - Deployed as a **server** in Docker on macOS.  
  - **Agents** installed on Parrot OS VMs.  
  - Executes hunts after Wazuh raises an alert to confirm the impact.  

---

## Value for the Project  
- Adds an **endpoint forensics layer** beyond log analysis.  
- Enables **threat hunting workflows** (proactive searches).  
- Provides **incident validation**: Was the brute force just noise, or did the attacker gain access?  
- Strongly increases the **professional depth** of the SOC project for portfolio presentation.  

---

## Example Use Cases  
- **Brute Force Detected in Wazuh**  
  → Velociraptor queries for new user accounts or recent authentication tokens.  
- **Suspicious Process Activity**  
  → Collects process trees and hashes → compare with threat intelligence feeds.  
- **Incident Timeline**  
  → Correlates Wazuh alerts with forensic artifacts from Velociraptor.  

---

## Updated SOC Architecture with Velociraptor  

flowchart LR
    subgraph SOC_Environment [SOC Environment]
        A[Parrot OS Agents] -->|Logs| B[Wazuh Manager (Docker)]
        B -->|Alerts & Events| C[Elasticsearch]
        C -->|Dashboards| D[Wazuh Dashboard (Kibana)]
        C -->|Visualization| E[Grafana]

        A -->|Forensic Data| F[Velociraptor Server (Docker)]
        F -->|Hunting Queries| A
    end
