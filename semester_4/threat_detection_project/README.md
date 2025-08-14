# Threat Detection Principles

## 1. Detection Rule Mechanisms
Detection rules are logic-based configurations within a SIEM or security monitoring tool designed to identify suspicious activity based on predefined patterns, thresholds, or behaviors.

- **Signature-Based Detection**: Matches known malicious patterns.
- **Behavioral/Anomaly-Based Detection**: Flags deviations from baseline.
- **Heuristic/Rule-Chained Detection**: Correlates multiple related events.

## 2. Three Detection Scenarios
**Scenario 1: Brute Force Attack**  
Logic: ≥10 failed login attempts from a single IP within 5 minutes.  
Mitigation: Block IP, review account.

**Scenario 2: Malicious File Execution**  
Logic: File hash matches malicious MD5 in TI feed.  
Mitigation: Isolate endpoint, remove file.

**Scenario 3: Data Exfiltration Attempt**  
Logic: Outbound >500MB to untrusted domain outside business hours.  
Mitigation: Terminate connection, investigate.

## 3. Threat Indicator Categories
| Category | Description | Example |
|----------|-------------|---------|
| File Hashes | Unique file identifiers | 44d88612fea8a8f36de82e1278abb02f |
| IP Addresses | Malicious IPs | 45.33.32.156 |
| Domain Names | C2 hostnames | evilserver.cn |

## 4. Threat Analysis Methodology
1. Detection
2. Triage
3. Investigation
4. Containment
5. Eradication
6. Recovery
7. Lessons Learned

## 5. Alert Investigation Exercise
Scenario: Multiple failed logins followed by success from unusual IP.  
Conclusion: Confirmed brute force attack leading to compromise.  
Remediation: MFA enabled, IP blocked.
