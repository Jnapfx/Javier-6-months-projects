# Wazuh Components Overview

Wazuh is a security monitoring platform composed of several core components that work together to collect, process, store, and display security data from monitored systems.  
Understanding the role of each component is essential when deploying or troubleshooting a Wazuh environment.

---

## 1. Wazuh Indexer
**What it is:**  
The component that stores and organizes data so it can be searched and analyzed quickly.  
It is based on **OpenSearch** (formerly Elasticsearch).

**Function:**  
- Stores events and logs sent from agents.  
- Allows queries and filtering in the dashboard.  

**Example:**  
If an agent sends a log stating “5 failed login attempts in Windows,” the **indexer** stores this event in a database optimized for searching. Later, when you type `"failed logon"` in the dashboard, the indexer is what returns the results.

---

## 2. Wazuh Server
**What it is:**  
The “brain” of the system. It processes the information sent by agents and applies detection rules.

**Function:**  
- Receives logs from all agents.  
- Applies detection rules to identify threats or abnormal behavior.  
- Sends alerts to the dashboard and, if configured, to other systems (email, external SIEM, etc.).

**Example:**  
If an agent detects that a critical file has been modified, it sends the event to the **server**. The server checks its rules, identifies it as a “file integrity” event, and generates an alert with a severity level.

---

## 3. Wazuh Dashboard
**What it is:**  
The graphical interface you use in the browser to view and analyze what is happening in your environment.

**Function:**  
- Displays alerts and metrics.  
- Allows searching for events stored in the indexer.  
- Manages rules, agents, and configurations.

**Example:**  
In the dashboard, you can filter “all high-severity alerts from the last 7 days” or view a chart showing failed login attempts per hour.

---

## 4. Wazuh Agent
**What it is:**  
The software you install on each machine you want to monitor (Windows, Linux, or macOS).

**Function:**  
- Collects logs from the system and applications.  
- Sends those logs to the Wazuh Server for analysis.

**Example:**  
You install a **Wazuh Agent** on your Windows laptop. This agent sends security logs (e.g., login attempts) to the **server**, which analyzes them and shows the resulting alerts in the **dashboard**.

---

## Data Flow Summary

```
[Wazuh Agent]  →  [Wazuh Server]  →  [Wazuh Indexer]  →  [Wazuh Dashboard]
(collects data)    (processes rules)   (stores events)    (displays alerts)
```

**Full example:**  
1. The **agent** on a Linux server detects that someone opened `/etc/passwd`.  
2. The **server** receives the event, checks that it is access to a sensitive file, and creates an alert.  
3. The **indexer** stores the event for future searches.  
4. The **dashboard** displays the alert and sends you an email notification.
