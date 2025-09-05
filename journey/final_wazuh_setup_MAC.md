
# Wazuh Home Lab Setup Guide (Mac + Parrot OS VMs)

## Overview

This guide documents the installation and configuration of a Wazuh home lab environment on a Mac host using Docker and multiple Parrot OS virtual machines (VMs) as agents. It includes steps for installation, agent registration, and troubleshooting common issues such as duplicate agent names.

---

## Network Configuration

| Host/VM        | IP Address       | Description                  |
|----------------|-----------------|------------------------------|
| Mac Host       | 192.168.1.133   | Wazuh Manager & Dashboard    |
| ParrotOS_1     | 192.168.1.103   | Agent                        |
| ParrotOS_2     | 192.168.1.110   | Agent                        |
| PArrot5_       | 192.168.1.169   | Agent                        |

> Note: Old instances of Parrot 3 were removed to avoid IP conflicts and duplicate agents.

---

## 1️⃣ Install Wazuh Manager & Dashboard (Mac with Docker)

1. Start the Docker containers:

```bash
docker-compose up -d
```

2. Verify running containers:

```bash
docker ps
```

3. Key ports exposed:

- 1514/tcp, 1515/tcp → Agent communication  
- 55000/tcp → Agent registration  
- 443/tcp → Dashboard  

---

## 2️⃣ Install Wazuh Agent on Parrot OS VMs

### 2.1 Install Dependencies

```bash
sudo apt update
sudo apt install netcat-openbsd -y
```

Test TCP/UDP connectivity to the manager:

```bash
nc -vz 192.168.1.133 1514
nc -vz 192.168.1.133 1515
nc -vz 192.168.1.133 55000
```

### 2.2 Download and Install Wazuh Agent

```bash
wget https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.12.0-1_arm64.deb
sudo WAZUH_MANAGER='192.168.1.133' WAZUH_AGENT_GROUP='default' WAZUH_AGENT_NAME='ParrotOS_1' dpkg -i ./wazuh-agent_4.12.0-1_arm64.deb
```

> Repeat for each VM with unique agent names: `ParrotOS_2`, `PArrot5_`.

---

## 3️⃣ Verify Connectivity to Wazuh Manager

```bash
nc -vz 192.168.1.133 1514
nc -vz 192.168.1.133 1515
nc -vz 192.168.1.133 55000
```

All connections should succeed, confirming network access.

---

## 4️⃣ Fixing Duplicate Agent Names

**Problem:**  
ERROR: Duplicate agent name prevents agent from connecting.

**Solution:**  

Edit agent configuration:

```bash
sudo nano /var/ossec/etc/ossec.conf
```

Add or modify `<name>` inside `<client>`:

```xml
<client>
  <server>
    <address>192.168.1.133</address>
  </server>
  <name>UniqueAgentName</name>
</client>
```

Save (Ctrl+O, Enter) and exit (Ctrl+X).  

Restart the agent:

```bash
sudo systemctl restart wazuh-agent
sudo tail -f /var/ossec/logs/ossec.log
```

Confirm log shows connection:

```
Connected to server (192.168.1.133:1514).
```

The Dashboard should now display the agent as active.

---

## 5️⃣ Final Verification

All agents should appear active in Wazuh Dashboard:

| Agent Name   | IP Address       | Status  |
|--------------|-----------------|---------|
| ParrotOS_1   | 192.168.1.103   | Active  |
| ParrotOS_2   | 192.168.1.110   | Active  |
| PArrot5_     | 192.168.1.169   | Active  |

Agent logs confirm successful connection to Manager.

---

## 6️⃣ Best Practices

- Ensure each agent has a unique name in the Manager.  
- Verify all Manager ports are accessible from VMs before registration.  
- Use netcat to test connectivity and troubleshoot issues.  
- If an agent shows “Never connected”, check for duplicates or network/firewall issues.  

✅ This setup ensures a stable Wazuh home lab environment with multiple Parrot OS agents, fully connected to the Manager for monitoring and security analysis.
