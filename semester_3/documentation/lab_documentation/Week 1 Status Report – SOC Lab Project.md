# Week 1 Status Report – SOC Lab Project

## Summary

Installed UTM as the virtualization platform to run Parrot OS.

Parrot OS is a Debian-based Linux distribution designed for cybersecurity professionals, ethical hackers, and developers. It comes preloaded with tools for penetration testing, digital forensics, cryptography, and privacy protection. Lightweight and secure, it supports anonymity tools like Tor and is optimized for both security and performance.

Defined tech stack:
- Windows 10 (Victim)
- Parrot OS (Attacker) — I spent time familiarizing myself with its tools and environment.
- Ubuntu Server (SIEM host)

* We also worked on preparing a brief **malware analysis report**. I reviewed the behavior of a flagged malware sample from ***MalwareBazaar*** (FSP-0991.exe), focusing on its evasion tactics, indicators of compromise, and potential risks — a useful exercise to understand real-world threats.

* Created a shared project folder for documentation and screenshots.

## Screenshots

- ![Parrot OS Screenshot](https://raw.githubusercontent.com/Jnapfx/Javier-6-months-projects/refs/heads/main/semester_3/documentation/lab_documentation/Parrot_OS.png)
- ![SEToolkit Screenshot](https://github.com/Jnapfx/Javier-6-months-projects/blob/main/semester_3/documentation/lab_documentation/SEToolkit.png?raw=true)


## Additional Progress

As a test, we prepared a phishing page template by cloning google.com using a terminal command in Parrot OS:

`wget --mirror --convert-links --adjust-extension --page-requisites --no-parent https://google.com`


This exercise was purely for practice to understand how resource downloading and HTML mirroring work — it helped me get comfortable with the terminal and some of Parrot OS’s capabilities.

## Currently Working On

- Creating the network diagram
- Configuring internal or bridged networking between VMs

## Next Focus: Week 2

- Finalize networking setup to enable communication between machines
- Prepare for upcoming attack simulations and Phase 1 testing

## Overall Status

- Foundations are in place, and progress is on track
