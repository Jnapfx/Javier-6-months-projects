---
layout: single
title: ""
permalink: /
---

<div style="display:flex; gap:20px; align-items:center; flex-wrap:wrap; margin-bottom:2rem; padding:1.5rem; background:#f8f9fa; border-radius:12px;">
  <img src="{{ '/assets/img/javier_headshot.jpeg' | relative_url }}" alt="Headshot of Javier Napoles" 
       style="max-width:160px; border-radius:12%; box-shadow:0 4px 12px rgba(0,0,0,.15);">
  <div>
    <h1 style="margin:0; color:#2c3e50;">Javier Napoles</h1>
    <p style="margin:.5rem 0; font-size:1.1rem; color:#34495e;">Cybersecurity Student · Graduating Oct 2025</p>
    <p style="margin:.5rem 0; line-height:1.6;">Focused on SOC analysis and blue-team operations — I build labs, tune detections, and write playbooks so threats get confused, frustrated, and eventually give up.</p>
  </div>
</div>


## Welcome to My Portfolio

I'm passionate about building **secure, reliable systems** that help organizations defend against modern threats. My work focuses on:

- 🛡️ **Security Operations**: SOC analysis, incident response, threat hunting
- 📊 **Automation**: Security tooling, detection engineering
- 📚 **Documentation**: Playbooks, procedures, knowledge sharing

### Current Focus

As I approach graduation in **Oct 2025**, I'm seeking opportunities in **SOC Analyst** roles where I can contribute to building robust defense systems and continue learning from experienced security professionals.

---

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
