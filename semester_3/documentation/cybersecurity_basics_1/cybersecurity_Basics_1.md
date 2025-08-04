# Cybersecurity Basics 1

## Malware Analysis Report: FSP-0991.exe


### 🧾 Introduction

This report provides a comprehensive analysis of a suspicious executable file named **FSP-0991.exe**, identified during routine malware sandbox testing. The file was flagged as a **Dridex-like banking Trojan**, known for stealing credentials, injecting itself into trusted processes, and spreading laterally across networks. The analysis includes detection methods, incident response strategies, encryption usage, compliance with cybersecurity laws, and ethical considerations. This case study is part of a practical assignment for *Cybersecurity Basics 1*.

---

### 1️⃣ Incident Response Plan

- **Detection Method**  
  Detected using sandbox tools (CAPE, Zenbox, VMRay), flagged as Trojan and spreader, matching Dridex banking trojan patterns. Indicators of Compromise (IOCs) include:
  - Malicious file path: `%LocalAppData%\Temp\FSP-0991.exe`
  - Injected processes: `netbtugc.exe`, `UI0Detect.exe`
  - Suspicious command lines

- **Containment Strategy**  
  - Quarantine infected systems  
  - Isolate affected network segments  
  - Disable compromised accounts  
  - Block malicious IPs/domains

- **Eradication & Recovery Steps**  
  - Remove malware and clean registry entries  
  - Run full system scans  
  - Restore from clean backups  
  - Apply OS/software patches  
  - **Implement user awareness training to reduce phishing-related infections**  
  - Monitor logs for anomalies

- **MITRE ATT&CK Reference**  
  Malware behavior aligns with:
  - `T1055.001` – **Process Injection: Dynamic-link Library**
  - `T1003.002` – **Credential Dumping: Security Account Manager**
  - `T1021.002` – **Remote Services: SMB**

- **Attack Type Explained**  
  Trojan (Dridex-like) focused on credential theft, lateral spreading, and persistence through trusted processes.

---

### 2️⃣ Security Policy

- **Key Security Rules/Guidelines**
  1. Enforce least privilege access controls  
  2. Deploy endpoint detection and response (EDR)  
  3. Require multi-factor authentication (MFA)

- **Incident Response Plan Section**
  - Assign incident response team  
  - Follow containment, eradication, recovery steps  
  - Notify stakeholders and legal team if required  
  - Conduct post-incident review and lessons learned

- **Maintaining the CIA Triad**
  - **Confidentiality:** Prevent data leaks  
  - **Integrity:** Validate system/file integrity post-incident  
  - **Availability:** Restore systems and services safely

---

### 3️⃣ Encryption Techniques

- **AES-CBC Encrypted Example**  
  - Encrypted text: `U2FsdGVkX1+0sO3vEybpFQ==`  
  - Decrypted plain text: `Confidential Message`  
  - *Usage:* AES-CBC is widely used to encrypt sensitive files or communication streams, providing confidentiality.

- **Hashing Example**  
  - MD5 (for `hello`): `5d41402abc4b2a76b9719d911017c592`  
  - SHA-256 (for `hello`): `2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824`  
  - *Usage:* Hashing is commonly used for integrity checking or password storage. (Note: MD5 is outdated; prefer SHA-256 or stronger.)

---

### 4️⃣ Legal and Ethical Compliance

- **Relevant Laws/Regulations**
  1. Computer Fraud and Abuse Act (CFAA)  
  2. General Data Protection Regulation (GDPR)

- **Ethical Considerations**
  - Perform analysis with authorized consent  
  - Protect user data privacy during investigation

- **Upholding Compliance**
  - Follow legal guidelines in all remediation steps  
  - Maintain detailed documentation and stakeholder communication

---

✅ **Conclusion**  
FSP-0991.exe is a Trojan malware using evasion techniques and network spreading behavior. This report outlines detection, response, policy, encryption use, and ethical compliance as part of the final project submission for Cybersecurity Basics 1. It also incorporates MITRE ATT&CK alignment, user education recommendations, and encryption best practices.
