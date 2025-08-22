# Windows Downgrade Journey (For Wazuh Setup)

**Date**: August 6, 2025

## Introduction

Today, during class, we were working on setting up Wazuh but encountered multiple errors throughout the process. After troubleshooting, I discovered that the main issue is related to system architecture. I am currently using Parrot OS with an ARM64 architecture, which is not compatible with Wazuh. The most appropriate solution would be to set up a new virtual machine with an x86_64 architecture, which is fully supported.

I will proceed with testing this approach and will share an update once I confirm whether it resolves the issue.

---

## Additional Context

The virtual machines I tried to run using UTM gave many errors, which further complicated the installation and configuration process of Wazuh.

For that reason, I decided to use a native Windows machine for installation. However, the Windows installed on that laptop started experiencing connection and stability issues, which led me to decide to downgrade from Windows 11 to Windows 10 to improve compatibility and performance.

---

## Goal

The purpose of this process is to successfully install and configure Wazuh — a powerful security monitoring platform. However, before reaching that point, several issues with the operating system led to an unexpected detour.

---

## Why I Downgraded: Windows 11 to Windows 10

After experiencing persistent connection issues and SSL errors with Windows 11 — problems I never had on Windows 10 — I decided to perform a system downgrade.

---

## Creating the USB Installer

I used Rufus to create a bootable Windows 10 USB installer with the following settings:

- Partition scheme: GPT  
- Target system: UEFI (non-CSM)  
- File system: FAT32

My initial attempt was with a microSD card and a USB adapter. Although Windows recognized it and the ISO was successfully flashed, the USB device did not appear in the system’s boot menu. Only "Windows Boot Manager" was listed.

---

## BIOS Adjustment

I enabled Legacy Boot in the BIOS settings. This made the USB device appear in the boot menu.

However, during installation I encountered the following error:

`Windows cannot be installed on this disk. The selected disk is of the GPT partition style.`

This happens because Legacy Boot only supports MBR partition schemes, while the disk was formatted as GPT.

---

## Returning to UEFI Mode

To continue installing on a GPT disk, I had to revert to UEFI boot mode.

Steps taken:

- Reflashed the ISO using Rufus with UEFI-compatible settings  
- Re-enabled UEFI in BIOS  
- Tried to boot again, but the USB with the microSD adapter was not detected in UEFI mode

It seems some adapters are not fully compatible with UEFI boot requirements.

---

## Next Step

I plan to test using a real USB flash drive I have at work. If it works, it should allow booting in UEFI mode and continue the Windows 10 installation.

---

## Upcoming Challenge

Once the downgrade is complete, the main objective will be:

Installing and configuring Wazuh on Windows 10.  
To be continued.

---
![I'm tired boss](https://www.meme-arsenal.com/memes/8d07373af86531363dea578a85d3417b.jpg)
---
---

---

---
# Version en Espanol
---


# Proceso de Downgrade de Windows (Para la instalación de Wazuh)

**Fecha**: 6 de agosto de 2025

## Introducción

Hoy, durante la clase, estuvimos trabajando en la configuración de Wazuh, pero encontramos múltiples errores durante el proceso. Tras realizar la resolución de problemas, descubrí que el problema principal está relacionado con la arquitectura del sistema. Actualmente estoy usando Parrot OS con arquitectura ARM64, que no es compatible con Wazuh. La solución más adecuada sería configurar una nueva máquina virtual con arquitectura x86_64, que es totalmente compatible.

Procederé a probar este enfoque y compartiré una actualización una vez que confirme si resuelve el problema.

---

## Contexto Adicional

Las máquinas virtuales que intenté correr con UTM me daban muchos errores, lo que complicaba aún más el proceso de instalación y configuración de Wazuh.

Por esa razón decidí usar un soporte nativo para la instalación, es decir, una laptop con Windows. Sin embargo, el Windows instalado en esa laptop comenzó a presentar problemas de conexión y estabilidad, lo que me llevó a tomar la decisión de hacer un downgrade de Windows 11 a Windows 10 para mejorar la compatibilidad y el rendimiento.

---

## Objetivo

El propósito de este proceso es instalar y configurar con éxito Wazuh — una plataforma avanzada de monitoreo de seguridad. Sin embargo, antes de llegar a ese punto, varios problemas con el sistema operativo provocaron un desvío inesperado.

---

## Por qué hice el downgrade: De Windows 11 a Windows 10

Tras experimentar problemas persistentes de conexión y errores SSL en Windows 11 — problemas que nunca tuve en Windows 10 — decidí realizar un downgrade del sistema.

---

## Creación del USB de instalación

Utilicé Rufus para crear un USB booteable con Windows 10 con la siguiente configuración:

- Esquema de partición: GPT  
- Sistema objetivo: UEFI (sin CSM)  
- Sistema de archivos: FAT32

Mi primer intento fue con una tarjeta microSD y un adaptador USB. Aunque Windows la reconoció y la ISO se grabó correctamente, el dispositivo USB no apareció en el menú de arranque del sistema. Solo aparecía "Windows Boot Manager".

---

## Ajuste en la BIOS

Activé el arranque Legacy en la configuración de la BIOS. Esto hizo que el USB apareciera en el menú de arranque.

Sin embargo, durante la instalación apareció el siguiente error:

`Windows no se puede instalar en este disco. El disco seleccionado es del estilo de partición GPT.`

Esto sucede porque el arranque Legacy solo soporta esquemas de partición MBR, mientras que el disco estaba formateado como GPT.

---

## Volviendo al modo UEFI

Para continuar con la instalación en un disco GPT, tuve que volver al modo de arranque UEFI.

Pasos realizados:

- Volví a grabar la ISO con Rufus usando configuración compatible con UEFI  
- Reactivé UEFI en la BIOS  
- Intenté arrancar nuevamente, pero el USB con el adaptador microSD no fue detectado en modo UEFI

Parece que algunos adaptadores no son completamente compatibles con los requisitos de arranque UEFI.

---

## Próximo paso

Planeo probar con un USB flash real que tengo en el trabajo. Si funciona, debería permitir arrancar en modo UEFI y continuar con la instalación de Windows 10.

---

## Desafío siguiente

Una vez completado el downgrade, el objetivo principal será:

Instalar y configurar Wazuh en Windows 10.  
Continuará.

![Estoy cansado jefe](https://slm-assets.secondlife.com/assets/33973239/lightbox/image.jpg?1695056043)

