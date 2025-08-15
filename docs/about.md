---
title: "About Me"
permalink: /about/
layout: single
---

<div style="text-align:center; margin-bottom:2rem;">
  <img src="{{ '/assets/img/javier_headshot.jpeg' | relative_url }}" alt="Javier Napoles" 
       style="max-width:200px; border-radius:50%; box-shadow:0 4px 12px rgba(0,0,0,.15);">
</div>

## My Journey in Cybersecurity 

Hi, I’m **Javier Napoles** — a Cybersecurity student focused on SOC Analysis, blending a decade of design experience with a passion for defending enterprise environments.
I’m **actively developing** my technical skills by building **hands-on labs**, fine-tuning detections, and creating **repeatable playbooks** to enhance blue-team operations. 


Currently pursuing my **Cybersecurity degree at DAE** *(Expected Graduation: October 2025)*, I’m looking for a **SOC Analyst role** where I can **continue learning** and contribute to robust defense systems.  

---

### Core Interests & Expertise  
- **🔍 Threat Modeling** – Analyzing system architectures to identify potential attack vectors and applying countermeasures.  
- **🚨 Incident Response** – Developing and executing response procedures from detection through remediation.  
- **📝 Detailed Documentation** – Creating clear, structured, and visually engaging documentation for SOC workflows, detection rules, and incident response playbooks.  
- **💻 VM & Container Environments** – Building and configuring virtualized and containerized labs using VMs and Docker for testing, training, and simulating security incidents. 
- **🤖 Prompt Engineering**– Designing and refining prompts for AI tools to generate accurate, efficient, and context-aware outputs, supporting security workflows and automation.

---

### Technical Skills  

**Programming (currently developing):**  
- Python *(Security automation, data analysis)*  

**Security Tools & Platforms (gaining hands-on experience):**  
- SIEM Platforms *(Wazuh, Splunk)*  
- Vulnerability Scanners *(Nessus, OpenVAS)*  
- Network Analysis Tools *(Wireshark, tcpdump)* 
- AI & Prompt Engineering: *(Designing prompts for security automation and analysis)* 

---

💼 **Looking for:** SOC Analyst role in a collaborative, growth-oriented team. 

---

*“Combining creativity and analytical thinking to build, document, and improve effective cybersecurity defenses.”*

<div style="text-align:center; margin-top:2rem;">
  <img src="{{ '/assets/img/dae-logo.png' | relative_url }}" alt="DAE Logo" style="height:40px; opacity:0.8;">
</div>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-4NCZMZSGWD"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  // Google Analytics configuration
  gtag('config', 'G-4NCZMZSGWD');

  // --- Active time tracking ---
  let timeOnPage = 0;
  let pageActive = true;

  // Initial state check
  pageActive = document.visibilityState === "visible" && document.hasFocus();

  // Detect when tab visibility changes
  document.addEventListener("visibilitychange", () => {
    pageActive = document.visibilityState === "visible" && document.hasFocus();
  });

  // Detect when window gains/loses focus
  window.addEventListener("focus", () => pageActive = true);
  window.addEventListener("blur", () => pageActive = false);

  // Timer: every 5 seconds, if active, increase counter and send event every 30 sec
  setInterval(() => {
    if (pageActive) {
      timeOnPage += 5;

      if (timeOnPage % 30 === 0) {
        gtag("event", "time_on_page", {
          event_category: "Engagement",
          event_label: "Time in seconds",
          value: timeOnPage
        });
      }
    }
  }, 5000);
</script>
