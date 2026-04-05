# VenomIntel

Advanced OSINT Automation Tool

**VenomIntel** is a terminal-based automation tool that consolidates username, email, website, and image-based open-source intelligence (OSINT) operations under a single menu interface. It aims to accelerate the information gathering process by centrally managing multiple popular OSINT tools and services.

<img width="1904" height="937" alt="Screenshot 2026-01-08 000056" src="https://github.com/user-attachments/assets/a9388bde-9dc3-43f7-ab2f-340eedb868b1" />

---

## General Features

- Menu-driven, interactive terminal interface
- Silent (background) automatic Python package update support
- Multiple OSINT tool integration
- Automatic web-based service launcher capability
- Root privilege verification
- ASCII banner and loading animation

---

## Supported Tools and Services

- Sherlock (Username reconnaissance)
- Holehe (Email account verification)
- SocialScan (Username / Email scanning)
- BlackBird (Email OSINT)
- WhatsMyName
- Photon (Web crawler)
- SpiderFoot
- Shodan
- Maltego
- PimEyes / Yandex Images / Mega
- OSINT Framework
- Wayback Machine
- ExifTool (image metadata analysis)

---

## Requirements

- Python 3.x
- Linux-based system
- Root privileges (sudo)
- Installation of the following tools on the system is recommended:
  • holehe
  • socialscan
  • photon
  • spiderfoot
  • exiftool
  • maltego
  • shodan CLI

---

## Installation
```bash
git clone https://github.com/osmnabyram/venomintel.git
cd venomintel
chmod +x venomintel.py
sudo python3 venomintel.py
```

## Usage

Root privileges are required to execute the tool:
```bash
sudo python3 venomintel.py
```

## Menu Options

- **1) Username Scanning**
Username reconnaissance via Sherlock

- **2) Email Verification (Holehe)**
Checks which platforms have registered accounts for a given email address

- **3) SocialScan Reconnaissance**
Username or email scanning

- **4) BlackBird**
Email OSINT analysis

- **5) GHunt (Passive)**
Google account analysis (requires manual configuration)

- **6) WhatsMyName**
Username verification via web interface

- **7) Photon Web Scanning**
Target website scanning

- **8) SpiderFoot**
Launches local web interface (`127.0.0.1:5001`)

- **9) Shodan**
Opens Shodan website

- **10) Maltego**
Launches Maltego application

- **11) PYM / Image OSINT**
Opens PimEyes, Yandex Images, and Mega

- **12) ExifTool**
Image file metadata analysis

- **13) Wayback Machine**
Displays archive records of target URLs

- **0) Exit**
Secure exit from program

---

## Workflow

- System loading animation is displayed
- Silent package updates are performed
- ASCII banner is printed
- Menu is displayed
- User makes a selection
- Selected OSINT tool is executed
- Returns to main menu upon completion

---

## Technical Details

### Automatic Updates

- Package versions are checked via PyPI
- Updates are performed in silent mode
- No output is provided to the user

### System Controls

- Root privilege verification (`os.getuid()`)
- Terminal clearing and animations
- Secure exit on error conditions

---

## Security Notes

- This tool is designed exclusively for **educational, lab, and CTF environments**
- Usage against unauthorized individuals or systems is **unethical and illegal**
- Users are **fully responsible** for all actions performed with this tool
