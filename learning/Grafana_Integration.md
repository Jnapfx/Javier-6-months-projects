# 📊 Grafana Integration in Divide and Defend SOC Project  

## What is Grafana?  
Grafana is an **open-source monitoring and visualization platform**. It allows analysts to build **interactive dashboards** that present SOC data in a clear and professional way. Instead of viewing raw logs, Grafana transforms alerts into **graphs, charts, and tables**, making detection trends easier to interpret.  

---

## Key Features  
- **Custom Dashboards** → Line charts, tables, and heatmaps for SOC data.  
- **Real-Time Alerts** → Notifications through email, Slack, or Teams.  
- **Multi-Source Support** → Can connect to ElasticSearch, Prometheus, SQL, and more.  
- **Filters & Variables** → Drill down into events by host, IP, or timeframe.  
- **Community Dashboards** → Ready-to-use templates for security monitoring.  

---

## Role in the SOC Project  
In the *Divide and Defend* project, **Wazuh** remains the **SIEM**, while **Grafana** is added as a complementary visualization layer.  

- **Wazuh (SIEM)**  
  - Collects and correlates security logs from Parrot OS agents.  
  - Detects brute force, DoS, and suspicious login attempts.  
  - Stores alerts and events in **Elasticsearch**.  

- **Grafana (Visualization)**  
  - Connects to Elasticsearch, reusing the data already processed by Wazuh.  
  - Builds **dashboards** for incident trends, attacker IPs, and host activity.  
  - Provides a **clear and professional interface** for reporting and presentations.  

---

## Value for the Project  
Adding Grafana provides:  
- **Advanced visualization** beyond Kibana dashboards.  
- Ability to **combine SIEM alerts** with other tools (e.g., OpenVAS, Suricata).  
- **Portfolio-ready SOC dashboards** that are attractive to recruiters and easy to present.  

---

## Updated SOC Architecture  
Below is the updated flow with Grafana integrated:  

```mermaid
flowchart LR
    A[Parrot OS Agents] -->|Send logs| B[Wazuh Manager (Docker)]
    B -->|Indexes alerts & events| C[Elasticsearch]
    C -->|Dashboards| D[Wazuh Dashboard (Kibana)]
    C -->|Dashboards & Reports| E[Grafana]

    subgraph SOC Environment
        A
        B
        C
        D
        E
    end
