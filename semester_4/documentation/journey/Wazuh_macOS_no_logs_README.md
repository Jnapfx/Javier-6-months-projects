# 🛠️ Guía de Diagnóstico – Wazuh Agent en macOS sin logs en Dashboard (Manager en Windows)

Este documento explica cómo diagnosticar y encontrar la causa cuando un **Wazuh Agent** en macOS aparece como *conectado* pero no muestra eventos/logs en el dashboard de un **Wazuh Manager** (en Windows con Docker).

---

## 1️⃣ Revisar el Agente (macOS)

### 1.1 Verificar estado y reiniciar
```bash
sudo /Library/Ossec/bin/wazuh-control status
sudo /Library/Ossec/bin/wazuh-control restart
```

### 1.2 Revisar logs del agente
```bash
sudo tail -n 30 /Library/Ossec/logs/ossec.log
sudo tail -n 30 /Library/Ossec/logs/wazuh-agent.log
```
Buscar:
- `connected to manager` ✅ (correcto)
- `authentication error` / `invalid key` ❌ (problema de clave)
- `cannot connect` ❌ (problema de red/puerto)

### 1.3 Confirmar configuración del Manager
```bash
grep -nA2 -B2 "<server>" /Library/Ossec/etc/ossec.conf
```
Asegurarse que `<address>` sea la **IP real** del manager y no `localhost`.

### 1.4 Probar conectividad con el Manager
```bash
nc -vz IP_DEL_MANAGER 1514
nc -vz IP_DEL_MANAGER 1515
```
- **1515** → enrolamiento/registro  
- **1514** → envío de eventos

### 1.5 Forzar generación de datos
```bash
sudo /Library/Ossec/bin/syscheck_control -u
sudo /Library/Ossec/bin/syscollector_control -f
```

---

## 2️⃣ Revisar el Manager (Windows con Docker)

### 2.1 Ver si el manager recibe eventos
```powershell
docker exec -it wazuh.manager tail -n 30 /var/ossec/logs/ossec.log
docker exec -it wazuh.manager tail -n 30 /var/ossec/logs/alerts/alerts.json
```
- Si `alerts.json` tiene datos → problema de **indexación**.
- Si no hay datos → problema de comunicación o clave.

### 2.2 Revisar Filebeat / Indexer
```powershell
docker logs --tail=200 wazuh.filebeat
docker logs --tail=200 wazuh.indexer
```

### 2.3 Reiniciar ingesta
```powershell
docker restart wazuh.filebeat
docker restart wazuh.indexer
docker restart wazuh.manager
```

### 2.4 Confirmar índices en el indexer
```powershell
docker exec -it wazuh.indexer bash -lc "curl -s -k https://localhost:9200/_cat/indices?v | grep wazuh-alerts"
```

---

## 3️⃣ Verificar claves de enrolamiento

### En el manager:
```powershell
docker exec -it wazuh.manager cat /var/ossec/etc/client.keys | grep NOMBRE_DEL_AGENTE
```

### En el agente:
```bash
sudo cat /Library/Ossec/etc/client.keys
```

Si es necesario re-enrolar:
```bash
sudo /Library/Ossec/bin/wazuh-control stop
sudo rm -f /Library/Ossec/etc/client.keys
sudo /Library/Ossec/bin/agent-auth -m IP_DEL_MANAGER -p 1515
sudo /Library/Ossec/bin/wazuh-control start
```

---

## 4️⃣ Comprobaciones finales
- El agente debe estar asignado a un **grupo** con módulos activos (Syscollector, Syscheck, etc.).
- Forzar 1.5 y revisar el dashboard → *Security events* o *Inventory*.

---

## 🔍 Interpretación rápida de resultados
- **Eventos en `alerts.json` pero no en dashboard** → revisar Filebeat/Indexer.
- **Sin eventos en `alerts.json`** pero agente dice “connected” → revisar clave o puerto 1514.
- **No se conecta** → problema de IP, firewall o configuración `<server>`.

---

📅 Última actualización: Agosto 2025
