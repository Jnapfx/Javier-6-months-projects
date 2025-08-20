# 🛡️ Micro-Segmentation Lab (Wazuh + Windows + Parrot)

This project demonstrates **basic host-based micro-segmentation** between a Windows host (running Wazuh Manager in Docker) and a Parrot Security VM agent. The goal is to prevent **lateral movement** while allowing only the **necessary ports** for Wazuh agent communication.

---

## 📌 Lab Environment

- **Windows Host (192.168.1.154)**  
  - Runs Docker + Wazuh Manager/Dashboard  
  - Also has Wazuh Agent installed  

- **Parrot Security VM (192.168.1.212)**  
  - Wazuh Agent installed  

- **WSL (127.0.0.1)**  
  - Local agent (no changes needed)  

---

## 🎯 Segmentation Goals

- **Parrot → Windows (Manager)**  
  - ✅ Allow only Wazuh ports: **1514/UDP** and **1515/TCP**  

- **Block lateral movement**  
  - ❌ Deny access to sensitive Windows services (RDP, SMB, RPC, WinRM)  

- **Windows (Manager)**  
  - ✅ Accept only Wazuh-related ports  
  - ✅ Optionally allow Dashboard (5601/TCP) and API (55000/TCP)  

---

## ⚙️ Configuration Steps

### 1. Windows (Manager) Firewall Rules

Run in **PowerShell (Admin)**:

```powershell
# Allow Wazuh agent communication
New-NetFirewallRule -DisplayName "Wazuh UDP 1514 from LAN" -Direction Inbound -Protocol UDP -LocalPort 1514 -RemoteAddress 192.168.1.0/24 -Action Allow
New-NetFirewallRule -DisplayName "Wazuh TCP 1515 from LAN" -Direction Inbound -Protocol TCP -LocalPort 1515 -RemoteAddress 192.168.1.0/24 -Action Allow

# Optional: Dashboard & API
New-NetFirewallRule -DisplayName "Wazuh Dash 5601 localhost+LAN" -Direction Inbound -Protocol TCP -LocalPort 5601 -RemoteAddress 127.0.0.1,192.168.1.0/24 -Action Allow
New-NetFirewallRule -DisplayName "Wazuh API 55000 from LAN" -Direction Inbound -Protocol TCP -LocalPort 55000 -RemoteAddress 192.168.1.0/24 -Action Allow

# Block sensitive services
New-NetFirewallRule -DisplayName "Block SMB 445"  -Direction Inbound -Protocol TCP -LocalPort 445 -Action Block
New-NetFirewallRule -DisplayName "Block NetBIOS 137-139" -Direction Inbound -Protocol TCP -LocalPort 139 -Action Block
New-NetFirewallRule -DisplayName "Block NetBIOS UDP 137-138" -Direction Inbound -Protocol UDP -LocalPort 137,138 -Action Block
New-NetFirewallRule -DisplayName "Block RPC 135"  -Direction Inbound -Protocol TCP -LocalPort 135 -Action Block
New-NetFirewallRule -DisplayName "Block WinRM 5985-5986" -Direction Inbound -Protocol TCP -LocalPort 5985,5986 -Action Block
New-NetFirewallRule -DisplayName "Block RDP 3389" -Direction Inbound -Protocol TCP -LocalPort 3389 -Action Block
```

---

### 2. Parrot Firewall Rules (UFW)

```bash
sudo apt update && sudo apt install -y ufw

# Strict defaults
sudo ufw default deny incoming
sudo ufw default deny outgoing

# Allow only Wazuh Manager communication
sudo ufw allow out to 192.168.1.154 proto udp port 1514
sudo ufw allow out to 192.168.1.154 proto tcp port 1515

# (Optional) Internet access for updates
sudo ufw allow out 80/tcp
sudo ufw allow out 443/tcp
sudo ufw allow out to 192.168.1.1 proto udp port 53   # adjust DNS IP
sudo ufw allow out proto icmp                        # ping

# (Optional) SSH from Windows Manager
sudo ufw allow from 192.168.1.154 to any port 22 proto tcp

sudo ufw enable
sudo ufw status numbered
```

---

## 🔍 Verification

**From Parrot:**
```bash
nc -vz 192.168.1.154 1515        # should be open
nmap -Pn -p 3389,445,135 192.168.1.154   # should be filtered/closed
```

**From Windows:**
- Open `https://192.168.1.154:5601` → confirm agents are **active**.  
- Trigger activity on Parrot (`sudo apt update`) → check logs in Wazuh dashboard.  

---

## 📸 Evidence (Screenshots to Include)

- Wazuh dashboard → **Agents active (Windows + Parrot)**  
- Parrot: `ufw status numbered`  
- Windows: `Get-NetFirewallRule | ? DisplayName -match "Wazuh|Block"`  
- Terminal output:
  - `nc -vz 192.168.1.154 1515` → success  
  - `nmap -Pn -p 3389,445,135 192.168.1.154` → blocked  
- Dashboard (5601) reachable  

---

## 🔄 Rollback / Adjustments

**Windows (PowerShell):**
```powershell
Get-NetFirewallRule | ? DisplayName -match "Wazuh|Block"
Remove-NetFirewallRule -DisplayName "Block SMB 445"
```

**Parrot:**
```bash
sudo ufw status numbered
sudo ufw delete <n>      # delete rule by number
sudo ufw default allow outgoing   # restore full Internet
```

---

## 🚀 Next Steps (Optional)

- Move Parrot into an **isolated virtual network** in UTM/VirtualBox/VMware.  
- Only allow outbound traffic to Windows Manager on **1514/1515**.  
- This creates stronger isolation while still maintaining Wazuh visibility.  
