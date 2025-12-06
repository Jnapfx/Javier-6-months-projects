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

Hi, I’m **Javier Napoles** — a cybersecurity professional focused on SOC Analysis, blending a decade of design experience with a passion for defending enterprise environments.  
I’m **actively developing** my technical skills by building **hands-on labs**, fine-tuning detections, and creating **repeatable playbooks** to enhance blue-team operations.

Having completed my **Cybersecurity Program at DAE (Oct 2025)**, I’m now preparing for the **CompTIA Security+ certification** and looking for a **SOC Analyst role** where I can **continue learning** and contribute to robust defense systems.


---

### Core Interests & Expertise  
- **Threat Modeling** – Analyzing system architectures to identify potential attack vectors and applying countermeasures.  
- **Incident Response** – Developing and executing response procedures from detection through remediation.  
- **Detailed Documentation** – Creating clear, structured, and visually engaging documentation for SOC workflows, detection rules, and incident response playbooks.  
- **VM & Container Environments** – Building and configuring virtualized and containerized labs using VMs and Docker for testing, training, and simulating security incidents. 
- **Prompt Engineering**– Designing and refining prompts for AI tools to generate accurate, efficient, and context-aware outputs, supporting security workflows and automation.

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

**Looking for:** SOC Analyst role in a collaborative, growth-oriented team. 

---

*“Combining creativity and analytical thinking to build, document, and improve effective cybersecurity defenses.”*

<div style="text-align:center; margin-top:2rem;">
  <a href="https://www.mydae.org/" target="_blank" rel="noopener">
    <img src="{{ '/assets/img/dae-logo.png' | relative_url }}" alt="DAE Logo" 
         style="height:40px; opacity:0.8; box-shadow:none;">
  </a>
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
