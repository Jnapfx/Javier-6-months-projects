# 🛡️ Runbook: SSH Brute Force Detection

## 📌 Alert Summary
- **Alert name:** SSH Brute Force Detected  
- **Rule ID (Wazuh):** 100202  
- **Severity:** High  
- **Triggered by:** 3 failed SSH login attempts within 60s from the same IP  

---

## 🎯 Objective
Provide a step-by-step response plan when a brute force SSH attack is detected in the SOC Lab environment.

---

## 📝 Response Steps

### 1. **Identify**
- Review the alert details in Grafana/Discord:
  - Source IP (`srcip`)
  - Target user (`dstuser`)
  - Affected host (`agent.name`)
  - Timestamp (`StartsAt`)
- Check Wazuh dashboard logs for related failed login attempts.  
- Confirm whether there was a successful login following the brute force.

---

### 2. **Contain**
- If the attack source is external:
  - Block the source IP in the firewall:
    ```bash
    sudo ufw deny from <srcip> to any port 22
    ```
- If the attack is from within the lab (Kali VM):
  - Note the test as successful and stop the Hydra process.

---

### 3. **Eradicate**
- Ensure that no SSH accounts were compromised.  
- Reset credentials for the targeted user if needed.  
- Verify that fail2ban or Wazuh Active Response is running to auto-block repeated offenders.

---

### 4. **Recover**
- Restore SSH service availability if blocked.  
- Validate connectivity for legitimate users.  
- Monitor logs for additional brute force attempts.

---

### 5. **Lessons Learned**
- Document the incident in your SOC project report.  
- Capture screenshots of:
  - Wazuh alert  
  - Grafana visualization  
  - Discord notification  
- Reflect on detection speed and response effectiveness.  

---

## 📚 References
- Wazuh SSH rules documentation: https://documentation.wazuh.com  
- Hydra brute force simulation tool  
- Incident Response Plan (*Divide and Defend SOC Project*):contentReference[oaicite:1]{index=1}  

