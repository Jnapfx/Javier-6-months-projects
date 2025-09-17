


## 1 Verify Suricata installation

En macOS (cuando instalas con brew install suricata), los archivos suelen estar en:

Configuración: ```/usr/local/etc/suricata/suricata.yaml```

Reglas: ```/usr/local/etc/suricata/rules/```

Logs: ```/usr/local/var/log/suricata/```

Confírmalo con:

```bash
brew list suricata
ls /usr/local/etc/suricata/rules/
```
![Suricata installation path](screenshots/1_verify_suricata-installation-path.png)


## 2 Crea la carpeta de reglas en la ruta correcta:

```bash
sudo mkdir -p /opt/homebrew/Cellar/suricata/8.0.0/.bottle/etc/suricata/rules
```
---

 <p style="font-size:24px;">3 Pega dentro del local.rules este contenido (las 3 reglas):</p>

 ## Brute Force

```bash

alert tcp any any -> $HOME_NET 22 (
  msg:"SOC-LAB: SSH brute force - multiple SYNs";
  flow:to_server,established;
  flags:S;
  detection_filter:track by_dst, count 15, seconds 60;
  threshold:type limit, track by_src, count 1, seconds 300;
  classtype:attempted-recon;
  sid:1000001; rev:1;
)
```
## Port Scan NULL
```bash
alert tcp any any -> $HOME_NET any (
  msg:"SOC-LAB: Port scan - NULL flags";
  flags:0;
  flow:stateless;
  detection_filter:track by_src, count 30, seconds 60;
  classtype:attempted-recon;
  sid:1000002; rev:1;
)

```
## DNS Exfiltration
```bash
alert dns any any -> any 53 (
  msg:"SOC-LAB: DNS exfil suspected - long labels";
  dns.query;
  pcre:"/([A-Za-z0-9]{40,}\\.){2,}/";
  detection_filter:track by_src, count 30, seconds 60;
  classtype:exfiltration;
  sid:1000003; rev:1;
)
```

---
# 3 Activación de local.rules y Verificación de Configuración 

Ahora vamos al siguiente paso concreto: hacer que Suricata cargue local.rules, validar la config y arrancarlo en la interfaz correcta.

## Paso A 
Respaldar ```suricata.yaml```

``` bash
sudo cp /opt/homebrew/Cellar/suricata/8.0.0/.bottle/etc/suricata/suricata.yaml \
  /opt/homebrew/Cellar/suricata/8.0.0/.bottle/etc/suricata/suricata.yaml.bak.$(date +%F_%H%M)
  ```
 ## Paso B
 Asegurar ```default-rule-path``` y añadir ```local.rules```

 Primero comprueba el ```default-rule-path``` y la lista ```rule-files```:

``` bash
javier@Javiers-MacBook-Air ~ % grep -E "default-rule-path|rule-files" -n /opt/homebrew/Cellar/suricata/8.0.0/.bottle/etc/suricata/suricata.yaml

2299:default-rule-path: /opt/homebrew/var/lib/suricata/rules
2301:rule-files:
2325:  #rule-files:
```

## ¿Qué significa?

Línea 2299 → tu ```suricata.yaml``` está configurado para buscar reglas en:

``` /opt/homebrew/var/lib/suricata/rules```


👉 O sea, no está apuntando al directorio donde creamos ```local.rules (/opt/homebrew/Cellar/.../etc/suricata/rules)```.

Línea 2301: ```rule-files```:
Está vacío, o sea no se están listando archivos de reglas activos ahí.

Línea 2325: ```#rule-files```:
Esa es una línea comentada (empieza con #), no tiene efecto.

## Cual es el siguiente paso?

1. Mueve tu local.rules al directorio estándar
``` bash
sudo mv /opt/homebrew/Cellar/suricata/8.0.0/.bottle/etc/suricata/rules/local.rules \
        /opt/homebrew/var/lib/suricata/rules/local.rules
```
2. Edita ```suricata.yaml``` para cargarlo
### Abre el archivo:
```
sudo nano /opt/homebrew/Cellar/suricata/8.0.0/.bottle/etc/suricata/suricata.yaml
```

### Abrir desde Finder

En la terminal, abre la carpeta en Finder:

```open /opt/homebrew/Cellar/suricata/8.0.0/.bottle/etc/suricata/```


### Te abrirá la carpeta en Finder.

Desde ahí arrastra ```suricata.yaml``` y suéltalo en la ventana de VS Code.