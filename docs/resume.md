---
title: "Resume"
permalink: /resume/
layout: single
---

<div style="text-align:center; margin-bottom:2rem; padding:1.5rem; background:#f8f9fa; border-radius:8px;">
  <h1 style="margin:0; color:#2c3e50;">Javier Napoles</h1>
  <p style="margin:0.5rem 0; font-size:1.1rem; color:#34495e;">Cybersecurity Student & Graphic designer</p>
  <p style="margin:0; color:#7f8c8d;">📧 jnapfx@gmail.com | 🔗 LinkedIn: /JavierNapoles | 🐙 GitHub: /jnapfx</p>
</div>

## 🎓 Education

**District Arts & Education (DAE)**  
*Cybersecurity Program*  
*Expected Graduation: Oct 2025*  

**Faculty of Arquitecture and Design (FAD)**
*Graphic Design*
*(2010-2015)*


**Relevant Coursework:**
*Google Cybersecurity Certificate (2024)*


---

## 💼 Experience

## 🧪 Technical Projects

### Divide & Defend: A Hands-On SOC Lab Project with Micro-Segmentation  
**2025 – Capstone Lab Project**  
- Built a home-based SOC lab with VMs simulating attacker, victim, and SIEM nodes.  
- Simulated attacks using Nmap and Hydra; configured detection rules in Wazuh.  
- Implemented micro-segmentation with UFW, iptables, and Windows Firewall.  
- Parsed logs from Windows and Linux agents to identify brute-force attacks, new user creation, and unauthorized access.  
- Conducted incident triage, threat hunting (OTX, MISP, AbuseIPDB), and vulnerability scans with Nmap/OpenVAS.  
- Produced a professional final report with IOC analysis, detection maps, and remediation plans.  

---

## 💼 Professional Experience

### Photographer & Graphic Designer  
**SSNUS – Norwalk, CT | 2020 – Present**  
- Maintained organized digital asset management with secure FTP workflows.  
- Launched SEO-optimized product site with structured metadata.  
- Applied disciplined file versioning and naming conventions to large digital libraries.  

### Freelance Graphic Designer & Video Editor  
**Fiverr | 2016 – Present**  
- Delivered cross-platform design assets for branding, UI/UX, and marketing campaigns.  
- Edited videos and animations for campaigns while maintaining consistency and quality.  
- Maintained communication and secure file delivery through cloud collaboration tools.  

### Post-Production Editor  
**Aventura TV – Venezuela | 2015 – 2017**  
- Edited TV and digital content end-to-end, including color grading and sound syncing.  
- Coordinated with producers to align deliverables with campaign goals.  
- Ensured quality control and technical accuracy in all final releases.  


---

## 🛠️ Technical Skills

### Programming Languages
- **Python** - Security automation, data analysis
- **TypeScript/JavaScript** - Frontend security implementations
- **SQL** - Database design, query optimization, injection prevention

### Security Tools & Platforms
- **SIEM**: Splunk, Wazuh
- **Vulnerability Assessment**: Nessus, OpenVAS, Burp Suite
- **Network Security**: Wireshark, Nmap, pfSense
- **Incident Response**: MISP, TheHive, Volatility

### Development & DevSecOps
- **Version Control**: Git, GitHub Actions, GitLab CI/CD

---

## 🏆 Certifications & Training

**In Progress:**
- CompTIA Security+ (Scheduled: November 2025)
- AWS Certified Security - Specialty (Scheduled: September 2025)

**Completed:**
- Google Cybersecurity Course (2024)


---

## 🎯 Professional Interests

- **Security Operations**: SOC analysis, threat hunting, incident response
- **Application Security**: Secure coding, vulnerability assessment
- **Cloud Security**: Infrastructure protection, compliance automation

---

<div style="text-align:center; margin-top:2rem; padding:1rem; background:#e8f4fd; border-radius:8px;">
  <p style="margin:0; font-style:italic; color:#2c3e50;">"Combining creativity and analytical thinking to build, document, and improve effective cybersecurity defenses."</p>
  
  <div style="margin-top:1rem;">
    <img src="{{ '/assets/img/dae-logo.png' | relative_url }}" alt="DAE Logo" style="height:30px; opacity:0.7;">
  </div>
</div>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-4NCZMZSGWD"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){ dataLayer.push(arguments); }
  gtag('js', new Date());
  gtag('config', 'G-4NCZMZSGWD');

  // --- Active time tracking (GA4-ready) ---
  if (!window.__timeOnPageTrackerInitialized) {
    window.__timeOnPageTrackerInitialized = true;

    let seconds = 0;
    const TICK_MS = 5000;          // count every 5s
    const SEND_EVERY_SEC = 30;     // send every 30s
    const IDLE_MS = 60000;         // consider idle after 60s without input

    let pageActive = document.visibilityState === "visible" && document.hasFocus();
    let lastActivity = Date.now();

    const setActive = (state) => {
      pageActive = state;
      if (state) lastActivity = Date.now();
    };

    document.addEventListener("visibilitychange", () => {
      setActive(document.visibilityState === "visible" && document.hasFocus());
    });
    window.addEventListener("focus",  () => setActive(true));
    window.addEventListener("blur",   () => setActive(false));

    // Update lastActivity on user input
    ["mousemove","keydown","mousedown","touchstart","scroll"].forEach(ev => {
      window.addEventListener(ev, () => { lastActivity = Date.now(); }, { passive: true });
    });

    const sendEvent = () => {
      gtag("event", "time_on_page", {
        time_on_page_sec: seconds,       // <-- create a GA4 custom metric for this
        transport_type: "beacon"
        // send_to: "G-4NCZMZSGWD"       // uncomment if you have multiple GA properties configured
      });
    };

    const intervalId = setInterval(() => {
      const idle = Date.now() - lastActivity > IDLE_MS;
      if (pageActive && !idle) {
        seconds += TICK_MS / 1000;
        if (seconds % SEND_EVERY_SEC === 0) sendEvent();
      }
    }, TICK_MS);

    // Flush on page exit
    const flush = () => { if (seconds > 0) sendEvent(); };
    window.addEventListener("pagehide", flush);
    window.addEventListener("beforeunload", flush);
  }
</script>
