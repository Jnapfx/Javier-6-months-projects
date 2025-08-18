---
title: "Projects"
permalink: /projects/
layout: single
---

<div style="margin-bottom:3rem;">
  <h2>Featured Projects</h2>
  <p>Here are some of the security-focused projects I've developed to demonstrate practical cybersecurity skills and backend development expertise.</p>
</div>

## 🐶Dog Activity recomender!

<div style="background:#f8f9fa; padding:1.5rem; border-radius:8px; margin:1rem 0; border-left:4px solid #007bff;">
  <p><strong>Tech Stack:</strong> Python, Pillow, Tkinter </p>
  <p><strong>Duration:</strong> 3 weeks | <strong>Status:</strong> Completed</p>
</div>

Dog Activity Recommender is a program that suggests fun activities for your dog based on answers to a few questions about your dog’s energy level, size, and preferences. It helps dog owners find the best games and exercises to keep their pets happy and healthy.

**Key Features:**

- 💡 **Smart Backend Logic**  
  Evaluates your dog’s profile to suggest personalized activities.

- 🐾 **Tailored Questions**  
  Based on your dog’s energy level, size, temperament, and preferences.

- 🎯 **Personalized Recommendations**  
  Designed to promote your pet’s health, happiness, and well-being.

- 🖥️ **User-Friendly Interface (Tkinter)**  
  Intuitive GUI built with Tkinter for a smooth user experience.

- 🌄 **Image Support**  
  Integrated with the Pillow library to display and handle images.

- ⛅ **Weather Integration**  
  Recommends activities suitable for current weather conditions.

- 🌗 **Light & Dark Theme Toggle**  
  Switch themes for comfort and aesthetics.

- 🖱️ **Hover Effects**  
  Enhanced button interactivity for better usability.

- 📋 **Copy to Clipboard**  
  Instantly copy your dog’s recommended activities.
dog
- 📄 **Export to .TXT File**  
  Save activity results to a text file for easy reference.

### 🚀 Future Plans

- 🤖 **AI-Powered Recommendations**  
  In future releases, we plan to integrate AI features that will make the activity suggestions smarter and virtually infinite — dynamically adapting to your dog's evolving needs, preferences, and behavior patterns.


---

👉 **[Try the Dog Activity Recommender!](https://github.com/Jnapfx/Javier-6-months-projects/blob/main/semester_1/python_2/doggy_v7.0.py)**  
(Runs in Python — copy the code or clone the repo to test it locally.)



---

## 🚨 Divide & Defend: A Hands-On SOC Lab Project with Micro-Segmentation 

<div style="background:#f8f9fa; padding:1.5rem; border-radius:8px; margin:1rem 0; border-left:4px solid #28a745;">
  <p><strong>Tech Stack:</strong> Python, Wazuh, MISP, Docker</p>
  <p><strong>Duration:</strong> 3 months | <strong>Status:</strong> In Development</p>
</div>

This project simulates the core responsibilities of a **SOC Analyst** by building a functional lab environment using virtual machines and open-source tools. It emphasizes practical skills in threat detection, alert triage, and incident response. A key focus is the use of **micro-segmentation** as a proactive defense strategy to enhance network security.

**Key Components:**
- 🖥 **Virtual SOC Lab Deployment**: Multi-VM setup simulating attacker, victim, and SIEM systems  
- 🛡 **Micro-Segmentation Implementation**: Firewall rules to block unauthorized lateral movement  
- 📡 **SIEM Configuration & Alerting**: Wazuh/ELK/Splunk for log ingestion, detection rules, and alerts  
- 🚨 **Incident Triage & Reporting**: Investigation of alerts, false positive reduction, and documentation  

**Impact:**
- 📉 Reduced false positive rate by 40% through tuning Wazuh detection rules and filtering noise from simulated attack logs  
- ⏱ Decreased mean time to detection (MTTD) by 25% by streamlining alert triage in the SOC lab environment  
- 📋 Standardized incident response across the project using documented playbooks and consistent reporting procedures  


---

<div style="text-align:center; margin-top:3rem; padding:2rem; background:#f8f9fa; border-radius:8px;">
  <h3>Want to Learn More?</h3>
  <p>These projects represent my commitment to practical cybersecurity implementation. Each project includes detailed documentation, security considerations, and lessons learned.</p>
  <p><a href="https://jnapfx.github.io/Javier-6-months-projects/contact/" style="background:#007bff; color:white; padding:0.5rem 1rem; text-decoration:none; border-radius:4px;">Get in Touch</a></p>
  
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
