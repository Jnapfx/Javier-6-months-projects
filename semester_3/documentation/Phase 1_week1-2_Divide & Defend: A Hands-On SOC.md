# 🛡️ Divide & Defend: A Hands-On SOC Lab Project with Micro-Segmentation  
## 📍 Phase 1 – Lab Setup, Attack Simulation, and Micro-Segmentation  
**Author:** Javier  
**Timeline:** July 2025  
**Version:** 1.0  

---

## 📌 Project Summary  
This project simulates the core responsibilities of a SOC Analyst using a home-based virtual lab. The goal is to build and secure a mini-network using open-source tools, run attack simulations, and enforce micro-segmentation policies to limit lateral movement.

---

## ✅ Phase 1 Goals (Weeks 1–4)

### Week 1 – Project Initialization  
- Installed UTM as the virtualization platform  
- Defined tech stack: Windows 10 (Victim), Parrot OS (Attacker), Ubuntu Server (SIEM Host)  
- Created a shared project folder for documentation and screenshots

### Week 2 – Virtual Lab Setup  
- Deployed 3 virtual machines:
  - **Windows 10** – Target/Victim machine  
  - **Parrot OS** – Attack simulation platform  
  - **Ubuntu Server** – Will serve as the SIEM host  
- Configured internal network (Bridged/NAT setup via UTM)  
- Verified connectivity between VMs using `ping` and port checks  
- Screenshots:
  - VM boot confirmations  
  - Successful pings between machines

### Week 3 – Simulated Attacks  
- Launched basic reconnaissance using `nmap` from Parrot OS:
  - Scanned open ports on Windows and Ubuntu  
- Performed brute-force login attempts using `hydra` (against SSH/SMB on test accounts)  
- Documented:
  - Command used  
  - Screenshots of terminal output  
  - Summary of findings (e.g., weak credentials, exposed services)

### Week 4 – Micro-Segmentation Implementation  
- Applied firewall policies:
  - `iptables` and `ufw` on Ubuntu  
  - Windows Defender Firewall rules on Windows  
- Blocked all unnecessary ports (e.g., SMB, RDP, SSH) between machines  
- Tested:
  - `ping` blocked between Parrot OS and Windows ✅  
  - Netcat connection attempts failed ✅  
- Created a table of blocked vs. allowed ports  
- Screenshots:
  - Firewall rules in terminal / control panel  
  - Failed connection attempts

---

## 🖥️ Lab Topology Diagram  
*(Insert diagram image or link here if available – use draw.io or Figma)*

---

## 🧰 Tools Used  
- UTM  
- Parrot OS, Windows 10, Ubuntu Server  
- Nmap, Hydra  
- iptables, ufw, Windows Defender Firewall  

---

## 📸 Evidence Folder  
Include:
- VM boot screenshots  
- Network config screenshots  
- Terminal outputs for Nmap and Hydra  
- Screenshots of firewall rule setup and blocked traffic  

---

## 📒 Notes & Reflections  
- Learned basic segmentation enforcement using built-in firewall tools  
- Identified which ports/services are commonly exposed by default  
- Understood how attackers scan and brute-force login attempts  

---

## 🚧 Next Phase  
➡️ Phase 2: SIEM Setup and Log Ingestion  
- Install Wazuh or ELK on Ubuntu  
- Deploy Winlogbeat and Filebeat  
- Forward logs from Windows and Parrot OS to SIEM  

---
