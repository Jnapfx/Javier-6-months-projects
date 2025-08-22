# 🛠️ Reparar el Arranque UEFI de Windows 10 en el SSD

## 📋 Descripción

Si después de instalar Windows 10 notas que el sistema solo arranca cuando el USB de instalación está conectado y desaparece una partición llamada `UEFI_NTFS` al retirar el USB, es probable que el instalador haya colocado los archivos de arranque en el USB en lugar del SSD.

Esta guía te ayudará a reparar el arranque de Windows en el SSD creando correctamente la partición EFI.

---

## 🔧 Requisitos

- Un USB booteable con el instalador de Windows 10
- El SSD con Windows 10 ya instalado
- Acceso al entorno de recuperación de Windows

---

## 🧭 Paso 1: Iniciar desde el USB de instalación

1. Conecta el USB de instalación.
2. Inicia tu PC y entra al menú de arranque (F12, F10, Esc, etc.).
3. Selecciona el USB para iniciar.
4. En la pantalla de instalación, **haz clic en "Reparar el equipo"** (abajo a la izquierda).
5. Luego entra a:  
   `Solucionar problemas` → `Símbolo del sistema`.

---

## 📌 Paso 2: Verificar si ya existe una partición EFI

Escribe los siguientes comandos:

```cmd
diskpart
list disk
select disk 0   (reemplaza 0 con el número de tu SSD si es diferente)
list partition
```

Busca una partición de ~100MB con tipo "Sistema".  
Si **ya existe**, anota su número y sal de `diskpart` escribiendo `exit`.  
Si **no existe**, sigue al paso siguiente.

---

## ⚙️ Paso 3: Crear una nueva partición EFI (si no existe)

Dentro de `diskpart`:

```cmd
create partition efi size=100
format quick fs=fat32
assign letter=s
exit
```

Esto crea la partición de arranque y la monta como `S:`.

---

## 🔄 Paso 4: Copiar el cargador de arranque de Windows

En el mismo símbolo del sistema, ejecuta:

```cmd
bcdboot C:\Windows /s S: /f UEFI
```

- Asegúrate de que `C:\Windows` sea la letra correcta de tu instalación de Windows.  
  Si no estás seguro, usa `diskpart → list volume` para identificarla.

Este comando copia los archivos de arranque de Windows a la partición EFI y registra el sistema en el firmware UEFI.

---

## ✅ Paso 5: Reiniciar y verificar

1. Cierra el símbolo del sistema.
2. Apaga el PC.
3. **Desconecta el USB.**
4. Inicia el equipo.
5. Entra al BIOS (F2, Supr, etc.) y asegúrate de que el SSD esté en primer lugar en el orden de arranque.

---

## 🧼 (Opcional) Eliminar partición UEFI_NTFS del USB

Una vez que todo funcione correctamente, puedes formatear el USB o eliminar manualmente la partición `UEFI_NTFS` si lo deseas.

---

## ⚠️ Preguntas Frecuentes (FAQ)

### ¿Puedo copiar la partición UEFI_NTFS del USB al SSD?
**No.** Esa partición no es una partición EFI válida para arranque de Windows. Fue creada por herramientas como Rufus para permitir arranque desde USBs formateados con NTFS, pero no es compatible con el arranque del sistema desde disco interno.

### ¿Esto borrará mi instalación de Windows?
**No.** Solo estás creando una nueva partición de arranque y registrando Windows en el firmware UEFI.

### ¿Qué pasa si no veo la letra `C:` como partición principal?
Usa `diskpart`, luego `list volume`, y localiza la partición que contiene la carpeta `Windows`. Usa esa letra en lugar de `C:` en el comando `bcdboot`.

---

## 📅 Última actualización

Agosto 2025

---
