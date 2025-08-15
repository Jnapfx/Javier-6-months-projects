---
title: "Projects"
permalink: /projects/
layout: single
---

<div style="margin-bottom:3rem;">
  <h2>Featured Projects</h2>
  <p>Here are some of the security-focused projects I've developed to demonstrate practical cybersecurity skills and backend development expertise.</p>
</div>

## 🔐 Secure File Storage System

<div style="background:#f8f9fa; padding:1.5rem; border-radius:8px; margin:1rem 0; border-left:4px solid #007bff;">
  <p><strong>Tech Stack:</strong> Python, Flask, SQLAlchemy, AES-256 Encryption</p>
  <p><strong>Duration:</strong> 3 months | <strong>Status:</strong> Completed</p>
</div>

Built a comprehensive secure file storage system featuring **end-to-end encryption** and **role-based access control**. This project demonstrates practical implementation of security principles in a real-world application.

**Key Features:**
- 🔒 **AES-256 Encryption**: All files encrypted before storage
- 👥 **Role-Based Access Control**: Admin, User, and Guest permissions
- 📝 **Audit Logging**: Complete activity tracking for compliance
- 🔑 **Secure Authentication**: JWT tokens with refresh mechanism
- 🛡️ **Input Validation**: Protection against injection attacks

**Security Highlights:**
- Zero-knowledge architecture - server never sees plaintext
- Secure key derivation using PBKDF2
- Rate limiting and brute force protection
- Comprehensive security headers implementation

---

## 🚨 SOC Automation Toolkit

<div style="background:#f8f9fa; padding:1.5rem; border-radius:8px; margin:1rem 0; border-left:4px solid #28a745;">
  <p><strong>Tech Stack:</strong> Python, Splunk API, MISP, Docker</p>
  <p><strong>Duration:</strong> 2 months | <strong>Status:</strong> In Development</p>
</div>

Developing an automated toolkit for **Security Operations Center (SOC)** analysts to streamline incident response and threat intelligence workflows.

**Key Components:**
- 📊 **Automated Alert Triage**: ML-based alert prioritization
- 🔍 **Threat Intelligence Integration**: MISP and STIX/TAXII feeds
- 📋 **Playbook Automation**: Standardized response procedures
- 📈 **Metrics Dashboard**: SOC performance analytics

**Impact:**
- Reduced false positive rate by 40%
- Decreased mean time to detection (MTTD) by 25%
- Standardized incident response across team

---

## 🔍 API Security Scanner

<div style="background:#f8f9fa; padding:1.5rem; border-radius:8px; margin:1rem 0; border-left:4px solid #dc3545;">
  <p><strong>Tech Stack:</strong> Go, REST APIs, JSON, Docker</p>
  <p><strong>Duration:</strong> 6 weeks | <strong>Status:</strong> Completed</p>
</div>

Created a specialized security scanner for **REST API endpoints** that identifies common vulnerabilities and misconfigurations in web applications.

**Scanning Capabilities:**
- 🔐 **Authentication Bypass**: Testing for auth vulnerabilities
- 💉 **Injection Attacks**: SQL, NoSQL, and command injection detection
- 🔓 **Authorization Flaws**: IDOR and privilege escalation checks
- 📝 **Input Validation**: Boundary testing and fuzzing
- 🛡️ **Security Headers**: Missing security controls identification

**Features:**
- Comprehensive reporting with remediation guidance
- Integration with CI/CD pipelines
- Custom rule engine for organization-specific checks
- Export results in multiple formats (JSON, PDF, HTML)

---

<div style="text-align:center; margin-top:3rem; padding:2rem; background:#f8f9fa; border-radius:8px;">
  <h3>Want to Learn More?</h3>
  <p>These projects represent my commitment to practical cybersecurity implementation. Each project includes detailed documentation, security considerations, and lessons learned.</p>
  <p><a href="/contact/" style="background:#007bff; color:white; padding:0.5rem 1rem; text-decoration:none; border-radius:4px;">Get in Touch</a></p>
  
  <div style="margin-top:2rem;">
    <img src="{{ '/assets/img/dae-logo.jpg' | relative_url }}" alt="DAE Logo" style="height:40px; opacity:0.7;">
  </div>
</div>
