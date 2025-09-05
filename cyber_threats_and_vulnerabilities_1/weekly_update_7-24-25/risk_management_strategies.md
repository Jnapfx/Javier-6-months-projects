# Risk Management Strategies
## Mini-SOC Lab – July 2025  
**Prepared by:** _Javier Napoles_  
**Role:** SOC Analyst Candidate  
**Date:** July 23, 2025  

---

## 1. Executive Summary

As part of the “Mini-SOC with Micro-Segmentation” project, a structured vulnerability assessment was conducted to identify and mitigate risks within the internal lab infrastructure. The assessment revealed two critical vulnerabilities related to outdated services—**OpenSSH 7.2p2** and **Apache 2.4.29**—both of which expose the network to high-impact attack vectors including remote code execution (RCE), credential leakage, and privilege escalation. 

This document outlines the identified risks, justifies their severity classification, recommends treatment strategies, and defines a monitoring procedure aligned with industry-standard risk management frameworks (NIST SP 800-30, ISO/IEC 27005, and CIS Controls v8).

---

## 2. Scope and Methodology

### 2.1 Environment Overview
- **Virtualization:** UTM (Universal Turing Machine) on macOS  
- **Operating System:** Parrot Security OS (for red team operations)  
- **Network Range:** 192.168.X.0/24 (lab internal segment)  
- **Assets Scanned:** 6 hosts with mixed services (web, SSH, SMB, etc.)

### 2.2 Tools and Techniques
| Tool     | Purpose                        |
|----------|--------------------------------|
| Nmap     | Asset discovery, version detection, CVE mapping (`-sV --script vuln`) |
| Netdiscover | Layer 2 network reconnaissance |
| Manual Validation | Service interrogation via `telnet`, `curl`, and browser access |

### 2.3 Risk Evaluation Criteria
- **Likelihood:** Based on exploit maturity, service exposure, and patch availability  
- **Impact:** Based on data sensitivity, lateral movement potential, and business function dependency  
- **Severity Rating:** Determined using qualitative matrix (High/Med/Low) mapped to CVSS guidelines  

---

## 3. Identified Critical Risks

| ID  | Affected Service | CVE ID           | Risk Description                                                   | Likelihood | Impact | Severity |
|-----|------------------|------------------|--------------------------------------------------------------------|------------|--------|----------|
| R-01| OpenSSH 7.2p2    | CVE-2016-0777    | Remote key leak via client memory disclosure (Roaming feature)    | High       | High   | **Critical** |
| R-02| Apache 2.4.29    | CVE-2017-15715   | Arbitrary file upload leading to potential RCE via path bypass    | Med-High   | High   | **Critical** |

### 3.1 R-01: OpenSSH 7.2p2 – CVE-2016-0777
- **Vulnerability Details:** A flaw in the Roaming feature allows a malicious server to read arbitrary client memory, including SSH private keys.  
- **Exploit Availability:** Public exploit code and Metasploit module available.  
- **Affected Versions:** OpenSSH 5.4–7.1/7.2p2  

### 3.2 R-02: Apache 2.4.29 – CVE-2017-15715
- **Vulnerability Details:** An attacker can bypass `<FilesMatch>` access controls using crafted requests, enabling unauthorized file uploads (e.g., PHP web shells).  
- **Exploit Availability:** Confirmed exploits and attack vectors documented in OWASP repositories.  
- **Affected Versions:** Apache HTTP Server 2.4.0–2.4.29

---

## 4. Risk Treatment and Mitigation Strategies

### 4.1 R-01: OpenSSH 7.2p2
**Treatment Strategy:** Risk Mitigation  
**Recommended Actions:**  
- [ ] Immediately upgrade to OpenSSH v9.0 or later.  
- [ ] Disable the deprecated Roaming feature in all client configurations (`UseRoaming no`).  
- [ ] Enforce public key authentication and disable password logins.  
- [ ] Apply strict firewall rules and host-based access control lists (ACLs) to restrict SSH access.  
- [ ] Implement multi-factor authentication for all administrative access.  

**Justification:** SSH is a high-value remote access vector. Given the availability of public exploits and the potential for credential theft, patching and hardening are the only viable mitigation routes.

---

### 4.2 R-02: Apache 2.4.29
**Treatment Strategy:** Risk Mitigation  
**Recommended Actions:**  
- [ ] Upgrade Apache HTTP Server to version 2.4.59 or newer.  
- [ ] Enable `mod_security` and deploy OWASP ModSecurity Core Rule Set (CRS).  
- [ ] Disable `.htaccess` overrides unless explicitly needed (`AllowOverride None`).  
- [ ] Audit all enabled HTTP methods; disable PUT, TRACE, and OPTIONS unless required.  
- [ ] Conduct code reviews on any dynamic upload logic to sanitize file names and MIME types.  

**Justification:** Public-facing web servers are primary targets in most cyberattacks. This vulnerability could be exploited to establish persistence or lateral access, especially in environments lacking strict segmentation.

---

## 5. Risk Monitoring and Governance Procedure

| Step | Description | Responsible Role | Frequency |
|------|-------------|------------------|-----------|
| 1 | Execute authenticated vulnerability scans on all critical assets | SOC Tier 2 Analyst | Monthly |
| 2 | Review scan results and update central **Risk Register** | Security Engineer | After each scan |
| 3 | Validate patching and mitigation actions with asset owners | IT Ops / DevOps | Weekly |
| 4 | Rescan mitigated systems to verify closure | Vulnerability Manager | Bi-monthly |
| 5 | Present status reports to CISO & GRC team | Risk Lead | Monthly |

### Key Metrics:
- 🔸 Number of unpatched critical vulnerabilities  
- 🔸 Average time to remediation (MTTR)  
- 🔸 Risk aging statistics (open > 90 days)  
- 🔸 Risk severity trends over time  

**Framework Alignment:** NIST CSF (Identify, Protect, Detect), ISO/IEC 27001 Annex A.12.6, and CIS Control 7 (Continuous Vulnerability Management)

---

## 6. Decision Justification

The decision to mitigate (rather than avoid, transfer, or accept) is driven by:
- **Operational necessity**: Both SSH and HTTP services are essential for system management and application access.  
- **Exploit maturity**: Known PoCs exist; active scanning for these versions is common across threat actor playbooks.  
- **Business impact**: Successful exploitation could result in full system compromise, lateral movement, and data breach.  
- **Feasibility**: Patches and configuration adjustments are readily deployable in the current environment without significant cost or downtime.

---

## 7. Conclusion

This report has demonstrated a structured approach to identifying, analyzing, and managing cybersecurity risks within the Mini-SOC lab environment. By prioritizing the most severe findings and aligning mitigation efforts with global standards, we not only reduce the immediate attack surface but also build a foundation for sustainable risk governance and proactive threat management.


---

_**End of Report**_  
