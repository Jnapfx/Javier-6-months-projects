# DualSense Left Stick Drift Repair

This document details the **diagnosis and repair of left stick drift** on a DualSense controller, performed without replacing any parts. The guide includes verification steps, cleaning, and mechanical adjustments to ensure a safe and effective fix.

**Author:** Javier Napoles  
**Date:** August 22, 2025  
**Time:** 10:30 PM EDT  
**Project:** DualSense Left Stick Drift Repair

---

## 🔎 Diagnosis

### 1. Windows Verification
- Connect the DualSense via USB or Bluetooth.  
- Press `Win + R`, type `joy.cpl`, and press Enter.  
- Select the controller → `Properties` → `Test` tab.  
- Observe stick movement.  

**Observation:** Only the **left stick X-axis** had drift. However, as this was my first time performing this repair, I did not notice initially and ended up cleaning the Y-axis potentiometer instead.

### 2. macOS Verification
- Connect the DualSense.  
- Open an online tester, e.g., [Gamepad Tester](https://gamepad-tester.com).  
- Monitor real-time stick input.  

**Result:** Confirms that only the X-axis shows unintended movement.

---

## 🛠️ Cleaning & Repair Procedure

### 1. Preparation
- Required tools:
  - Precision screwdriver
  - Cotton swabs
  - 90%+ isopropyl alcohol
- Work on a clean, well-lit surface.  
- **Caution:** Avoid touching electronics with bare hands to prevent ESD damage.

### 2. Disassembly
- Carefully remove the DualSense shell (clips + screws).  
- Locate the left stick module.  
- Visually inspect for dust or debris.

### 3. Potentiometer Cleaning
- Identify the **green potentiometers** (X and Y axes).  
- **Note:** The actual drift was only on the X-axis, but I cleaned the Y-axis potentiometer by mistake.  
- Moisten a swab with isopropyl alcohol and clean the contact area.  
- Apply a small drop of alcohol inside the potentiometer slit and move the stick multiple times to spread it.  
- This cleans the **graphite tracks**, removing debris that can cause drift.

### 4. Wiper Adjustment
- Each potentiometer has a small metal contact (wiper) that touches the graphite track.  
- Carefully adjust the wiper to ensure consistent contact with the track.  
- This restores proper stick reading even if the wrong axis was cleaned initially.

### 5. Reassembly
- Reattach the shell and screws.  
- Test the controller again on Windows (`joy.cpl`) or macOS (Gamepad Tester).  
- Verify the stick returns to center and shows no drift.

---

## ✅ Results

- Left stick drift **fully eliminated**.  
- Stick returns to center correctly.  
- No lubricants or replacement parts required.  
- Controller ready for normal use.  
- **Lesson Learned:** Clean the correct axis next time to avoid unnecessary work.

---

## ⚠️ Recommendations & Notes

- Potentiometers use **graphite tracks** that wear over time.  
- This repair is **temporary but effective**; periodic cleaning can prolong stick life.  
- **Do not use pencil graphite** — clay content may permanently damage the tracks.  
- Keep the controller in a clean, dust-free environment.  
- If drift persists → consider **replacing the potentiometer** (standard ALPS 10kΩ).

---

## 📅 Final Status

| Component       | Status      | Method Used                          | Cost  |
|-----------------|------------|--------------------------------------|-------|
| Left Stick      | ✅ Repaired | Isopropyl alcohol cleaning + wiper adjustment (cleaned wrong axis by mistake) | $0    |

---

### 🔧 Technical Notes

- **Isopropyl alcohol:** removes dirt and residue without damaging graphite or plastic.  
- **Wiper:** metal contact translating physical movement into electrical signal; adjusting it improves stick accuracy.  
- **Drift:** occurs when potentiometer reads false movement due to dirt, wear, or poor contact.
