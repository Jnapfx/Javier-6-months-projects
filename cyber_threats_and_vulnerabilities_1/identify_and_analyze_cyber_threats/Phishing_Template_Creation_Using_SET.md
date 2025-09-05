# Phishing Template Creation Using Social-Engineer Toolkit (SET) on Parrot OS

This tutorial walks through the process of creating a phishing page using the Social-Engineer Toolkit (SET) on Parrot OS. It demonstrates how to clone a login page and capture user credentials in a controlled environment.

> ⚠️ This guide is intended **strictly for educational purposes** and **authorized penetration testing** only.

---

## Table of Contents

- [Overview](#overview)  
- [Requirements](#requirements)  
- [Step-by-Step Guide](#step-by-step-guide)  
- [Disclaimer](#disclaimer)

---

## Overview

SET allows ethical hackers and cybersecurity professionals to simulate social engineering attacks. In this tutorial, we’ll use:

- **Credential Harvester Attack Method**
- **Site Cloner**  

This combination allows cloning real websites and capturing login credentials locally for testing purposes.

---

## Requirements

- Parrot OS or Kali Linux with SET installed  
- Sudo/root access  
- The following image files saved in the same directory as this README:

  - `1_Launching SET.png`  
  - `2_SET_main_menu.png`  
  - `3_website_attack vectors.png`  
  - `4_credential_harvester.png`  
  - `5_Site_Cloner.png`  
  - `6_phishing_page_ready.png`  
  - `7_captured_credentials.png`  

---

## Step-by-Step Guide

### Step 1: Launch SET

Open a terminal and run:

```bash
sudo setoolkit
```

This launches the SET main interface.

![Launching SET](1_Launching_SET.png)

---

### Step 2: Select "Social-Engineering Attacks"

From the main menu, choose:

```
1) Social-Engineering Attacks
```

![SET Main Menu](2_SET_main_menu.png)

---

### Step 3: Select "Website Attack Vectors"

Next, select:

```
2) Website Attack Vectors
```

![Website Attack Vectors](3_website_attack vectors.png)

---

### Step 4: Choose "Credential Harvester Attack Method"

Then, choose:

```
3) Credential Harvester Attack Method
```

![Credential Harvester](4_credential_harvester.png)

---

### Step 5: Choose "Site Cloner"

Now choose:

```
2) Site Cloner
```

You’ll be prompted to enter the URL of the website to clone. For example:

```
https://accounts.google.com
```

![Site Cloner](5_Site_Cloner.png)

---

### Step 6: Configure Local Hosting

SET will ask for your local IP address (e.g., `192.168.1.100`) to host the cloned site. After entering it, SET will serve the cloned login page.

![Phishing Page Ready](6_phishing_page_ready.png)

---

### Step 7: Test and Capture Credentials

Using another device on the same network, visit the IP address provided by SET in a browser. When someone enters credentials on the cloned page, they’ll be logged in your terminal in real time.

![Captured Credentials](7_captured_credentials.png)

---

## Disclaimer

This tutorial is provided for **educational** and **authorized testing** only.  
Using these techniques in real-world environments **without proper consent** is illegal and unethical.  
Always obtain **explicit permission** before conducting any form of penetration testing.

---
