# 🛡️ Divide and Defend: Mini SOC with Micro-Segmentation  

## 📌 Project Summary  
**Divide and Defend** is a lab project designed to simulate a **Security Operations Center (SOC)** in a controlled environment. The main goal was to **detect, analyze, and respond to cyber threats** while applying the principle of **micro-segmentation** to reduce the attack surface and strengthen defense-in-depth strategies.  

Over three months, a multi-VM infrastructure was built in **UTM**, a **SIEM (Wazuh Manager in Docker on macOS)** was deployed for log collection and correlation, **Threat Intelligence integration with OpenCTI** was configured, **attack simulations were executed with Kali Linux**, and **vulnerability management and incident response practices** were applied.  

---

## ⚙️ Tools and Technologies Used  

### 🔹 Infrastructure and Virtualization  
- **UTM (macOS)** → virtualization platform for VMs:  
  - **3 Parrot OS VMs** → configured as **Wazuh agents**.  
  - **1 Kali Linux VM** → used for attack simulation.  
- **Docker (macOS)** → containers for Wazuh Manager, Elastic, MinIO, and RabbitMQ.  

### 🔹 SIEM and Monitoring  
- **Wazuh SIEM**  
  - **Wazuh Manager** deployed in Docker (macOS).  
  - **3 Wazuh agents on Parrot OS** sending system and authentication logs.  
  - Event visualization in the **Wazuh Dashboard** (Elastic/Kibana).  
  - Creation of **custom detection rules** for:  
    - SSH brute force (3 failed attempts in 60s).  
    - Denial of Service (DoS) attempts.  
    - Suspicious login activity.  

### 🔹 Threat Intelligence  
- **OpenCTI**  
  - Ingestion of **Indicators of Compromise (IOCs)**.  
  - Correlation with SIEM-detected events.  

### 🔹 Micro-Segmentation  
- Configuration of **separated subnets** for each VM.  
- Traffic restrictions between:  
  - **Kali Linux (attacker)**  
  - **Parrot OS (Wazuh agents)**  
  - **Wazuh Manager in macOS (monitoring server)**  

### 🔹 Vulnerability Management  
- **Nmap** → host and service discovery.  
- **OpenVAS** → vulnerability scanning.  
- Documentation of findings with screenshots.  

### 🔹 Incident Response  
- Development of an **Incident Response Plan (IRP)** following the five phases:  
  1. Preparation  
  2. Identification  
  3. Containment  
  4. Eradication  
  5. Recovery  
- Incident classification using a **severity matrix**.  
- Timeline creation with correlated event analysis.  

### 🔹 Attack Simulation  
- **Kali Linux**  
  - SSH brute force.  
  - Denial of Service (DoS).  
  - Validation of alerts in Wazuh Dashboard.  

---

## ✅ Results  
- Deployment of a fully functional **Mini SOC** with 3 Parrot OS agents and a Wazuh Manager running in Docker (macOS).  
- **Detection and documentation of security incidents** through Wazuh.  
- Successful integration of **SIEM + Threat Intelligence**.  
- Practical demonstration of how **micro-segmentation** helps contain attacks.  
- Professional documentation including **README, abstract diagrams, screenshots, and technical reports** prepared for portfolio presentation.  


---
---
---
---
---
---
---
---
---

espanol
# 🛡️ Divide and Defend: Mini SOC with Micro-Segmentation  

## 📌 Resumen del Proyecto  
**Divide and Defend** es un laboratorio diseñado para simular un **Security Operations Center (SOC)** en un entorno controlado. El objetivo fue **detectar, analizar y responder a amenazas** cibernéticas mientras se aplicaba el principio de **micro-segmentación** para reducir la superficie de ataque y fortalecer la seguridad en profundidad.  

Durante tres meses se construyó una infraestructura de múltiples máquinas virtuales en **UTM**, se instaló un **SIEM (Wazuh Manager en Docker sobre macOS)** para la recolección y correlación de logs, se integró **Threat Intelligence con OpenCTI**, se realizaron **simulaciones de ataque con Kali Linux**, y se aplicaron técnicas de **gestión de vulnerabilidades e incident response**.  

---

## ⚙️ Herramientas y Tecnologías Utilizadas  

### 🔹 Infraestructura y Virtualización  
- **UTM (macOS)** → gestor de máquinas virtuales:  
  - **3 VMs Parrot OS** → configuradas como **agentes Wazuh**.  
  - **1 VM Kali Linux** → utilizada para simulación de ataques.  
- **Docker (macOS)** → contenedores para Wazuh Manager, Elastic, MinIO y RabbitMQ.  

### 🔹 SIEM y Monitoreo  
- **Wazuh SIEM**  
  - Instalación de **Wazuh Manager en Docker (macOS)**.  
  - **3 agentes Wazuh en Parrot OS** enviando logs de sistema y autenticación.  
  - Visualización de eventos en el **Wazuh Dashboard** (Elastic/Kibana).  
  - Creación de **reglas personalizadas** para detectar:  
    - SSH brute force (3 intentos fallidos en 60s).  
    - Intentos de DoS.  
    - Accesos sospechosos.  

### 🔹 Threat Intelligence  
- **OpenCTI**  
  - Ingesta de **Indicators of Compromise (IOCs)**.  
  - Correlación con eventos detectados en el SIEM.  

### 🔹 Micro-Segmentation  
- Configuración de **subredes separadas** para cada VM.  
- Restricción de tráfico entre:  
  - **Kali Linux (atacante)**  
  - **Parrot OS (agentes Wazuh)**  
  - **Wazuh Manager en macOS (servidor de monitoreo)**  

### 🔹 Vulnerability Management  
- **Nmap** → descubrimiento de hosts y servicios.  
- **OpenVAS** → escaneo de vulnerabilidades.  
- Documentación de hallazgos con capturas.  

### 🔹 Incident Response  
- Elaboración de un **Incident Response Plan (IRP)** con las fases:  
  1. Preparación  
  2. Identificación  
  3. Contención  
  4. Erradicación  
  5. Recuperación  
- Clasificación de incidentes con **matriz de severidad**.  
- Creación de timelines con correlación de eventos detectados.  

### 🔹 Simulación de Ataques  
- **Kali Linux**  
  - SSH brute force.  
  - Denial of Service (DoS).  
  - Validación de alertas en Wazuh Dashboard.  

---

## ✅ Resultados  
- Construcción de un **Mini SOC funcional** con 3 agentes Parrot OS y un Manager en Docker (macOS).  
- **Detección y documentación de incidentes de seguridad** a través de Wazuh.  
- Integración exitosa de **SIEM + Threat Intelligence**.  
- Demostración práctica de cómo la **micro-segmentación** ayuda a contener ataques.  
- Documentación profesional con **README, diagramas abstractos, capturas y reportes técnicos** listos para portafolio.  
