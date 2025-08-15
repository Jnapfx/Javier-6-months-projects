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

<div style="text-align:left; margin-top:2rem;">
  <a href="https://www.mydae.org/" target="_blank" rel="noopener">
    <img src="{{ '/assets/img/dae-logo.png' | relative_url }}" alt="DAE Logo" style="height:40px; opacity:0.8;">
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
