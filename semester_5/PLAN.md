# learning/PLAN.md

## Student commitment

- **Name:** Javier Napoles  
- **Date created:** 2025-09-02  

I commit to treat this plan as my personal roadmap: I will keep dates realistic, finish each small task, capture evidence of success, and update this file if anything changes.  

---

## Chosen technology

- **Technology name:** Grafana  
- **Technology version (if applicable):** Latest stable  

### Why I chose this technology  
Grafana will be integrated into the *Divide and Defend* SOC project as a **visualization layer**. While Wazuh already collects and correlates logs, Grafana provides **advanced dashboards and real-time visual analytics**. This enhances detection insights, makes reporting more professional, and produces **portfolio-ready SOC dashboards** attractive for recruiters.  

Coming from a **creative background**, I value clear and visually appealing interfaces. Grafana’s design flexibility allows me to build dashboards that are not only functional but also engaging, making analysis and presentation easier for me and more impactful for others.  


---

## First-day actions

1. Finalize chosen technology (Grafana) and integration goal.  
2. Draft three integration tasks with realistic dates.  
3. Commit this plan file to the repo.  
4. Start Task 1 from my local workspace.  

---

## My three integration tasks (small, testable, dated)

**Task 1 — Connect Grafana to Elasticsearch**  
- **Description:** Configure Grafana to use Elasticsearch (already storing Wazuh alerts) as a data source.  
- **Start date:** 2025-09-02  
- **Target completion date:** 2025-09-05  
- **Success criterion:** Grafana can query and display Wazuh alert data from Elasticsearch.  
- **Proof method:** Screenshot of Grafana data source settings + a sample query result dashboard.  
- **Where I will start Task 1:** local branch `feature/grafana-elasticsearch`  

**Task 2 — Build SOC Dashboards**  
- **Description:** Create custom dashboards to visualize failed logins, attacker IPs, and DoS attempts detected by Wazuh.  
- **Start date:** 2025-09-06  
- **Target completion date:** 2025-09-12  
- **Success criterion:** Dashboards show dynamic data with filters for IP, host, and timeframe.  
- **Proof method:** Screenshots of dashboards saved to `learning/README.md`.  

**Task 3 — Integrate Multi-Source Data**  
- **Description:** Add OpenVAS vulnerability scan results as an additional Grafana panel, combining SIEM alerts with vulnerability data.  
- **Start date:** 2025-09-13  
- **Target completion date:** 2025-09-19  
- **Success criterion:** A single Grafana dashboard panel shows both Wazuh alerts and OpenVAS vulnerability metrics.  
- **Proof method:** Screenshot of final integrated dashboard + explanation in `learning/REFLECTION.md`.  

---

## Risks, assumptions, and blockers

- Requires correct Elasticsearch endpoint from Wazuh setup.  
- Grafana container must run without port conflicts.  
- OpenVAS export format must be compatible with Grafana.  

---

## My weekly timeline

- **Week 1:** Commit this PLAN and start Task 1 (Grafana + Elasticsearch).  
- **Week 2:** Build first SOC dashboards (login attempts, attacker IPs, DoS).  
- **Week 3:** Integrate OpenVAS with Grafana.  
- **Week 4:** Finalize dashboards, take screenshots, and document results in README + Reflection.  
