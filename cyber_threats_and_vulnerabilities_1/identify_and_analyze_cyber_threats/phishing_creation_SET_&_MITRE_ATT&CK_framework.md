# Cyber Threat Simulation & APT Mapping Lab

## Introduction

This mini-report demonstrates:
- How to create a phishing template using Social-Engineer Toolkit (SET) in Parrot OS/Kali Linux.
- How to map a real APT campaign to the MITRE ATT&CK framework, highlighting the connection between social engineering and advanced threats.

---

## 1. Phishing Simulation with SET

**Objective:**  
Demonstrate credential harvesting via a phishing page created with SET.

### Steps Performed

1. Open terminal in Parrot OS/Kali Linux.
2. Run SET:
    ```bash
    sudo setoolkit
    ```
3. Navigate:
    - `1) Social-Engineering Attacks`
    - `2) Website Attack Vectors`
    - `3) Credential Harvester Attack Method`
    - `2) Site Cloner`
4. Input the target URL (e.g., `https://login.microsoftonline.com`).
5. Enter local IP.
6. SET clones and hosts the site.
7. Tested the phishing page in a browser and submitted fake credentials.

### Evidence / Screenshots

![SET Main Menu](screenshots/set_main_menu.png)
*SET main menu on Parrot OS.*

![Cloned Phishing Site](screenshots/cloned_login.png)
*Cloned login page as displayed in browser.*

![Captured Credentials](screenshots/captured_credentials.png)
*Credentials captured in terminal by SET.*

**Conclusion:**  
The simulation shows how easy it is to harvest credentials using SET, emphasizing the need for strong user awareness.

---

## 2. Mapping a Real APT Campaign to MITRE ATT&CK

**Objective:**  
Demonstrate how phishing is used by real APTs and map the campaign to MITRE ATT&CK.

### APT Example: APT28 (Fancy Bear)

- **Targets:** Government, military, NGOs
- **Example campaign:** 2016 spearphishing attacks

#### MITRE ATT&CK Mapping

| Stage            | Tactic                  | Technique ID   | Description                      |
|------------------|-------------------------|---------------|----------------------------------|
| Initial Access   | Phishing                | T1566.001     | Spearphishing emails             |
| Execution        | User Execution          | T1204.002     | Weaponized document opened       |
| Persistence      | Office App Startup      | T1137.001     | Macro runs on startup            |
| Credential Access| Credential Dumping      | T1003         | Stealing credentials             |
| Exfiltration     | Exfiltration Over C2    | T1041         | Data sent via HTTP/S             |
| Defense Evasion  | Obfuscated Files/Scripts| T1027         | Script obfuscation               |

*Source: [MITRE ATT&CK – APT28](https://attack.mitre.org/groups/G0007/)*

#### Visual Evidence

![APT28 ATT&CK Matrix](screenshots/apt28_attack_matrix.png)
*Visual mapping of APT28 campaign to MITRE ATT&CK.*

**Conclusion:**  
APT28’s campaigns often begin with spearphishing—just like your SET simulation—demonstrating how basic tactics can be part of advanced threat campaigns.

---

## References

- [MITRE ATT&CK – APT28](https://attack.mitre.org/groups/G0007/)
- [Social-Engineer Toolkit (SET)](https://github.com/trustedsec/social-engineer-toolkit)

---

**Prepared by:**  
[Javier Napoles / future SOC Analyst]  
[7-22-25]
