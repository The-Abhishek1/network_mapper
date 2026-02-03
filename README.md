# Network Mapper 🕸️

A Python-based **network discovery and visualization tool** that scans your subnet, identifies active hosts, resolves MAC addresses and hostnames, and visualizes the network in a **gateway-centric logical map**.

This project is designed for **learning networking, cybersecurity, and reconnaissance fundamentals**, inspired by how real scanners work internally.

---

## ✨ Features

### ✅ Implemented Features
- 🔍 **Automatic or manual subnet detection**
- 📡 **Active host discovery** (ICMP ping sweep)
- 🧭 **MAC address resolution** (ARP-based)
- 🏷️ **Hostname resolution** using:
  - Reverse DNS (PTR)
  - NetBIOS (Windows LAN)
  - mDNS / Avahi (Linux, IoT)
- 📊 **Tabular CLI output**
- 🕸️ **Logical network map visualization**
  - Gateway-centric
  - Non-overlapping nodes
  - Device metadata shown per node

---

## 🖼️ Sample Output

### CLI Output

```text
Enter network (e.g. 192.168.1.0/24) or press Enter for auto-detect: 192.168.7.1/24

Scanning network: 192.168.7.0/255.255.255.0

[+] Host 192.168.7.3 is UP
[+] Host 192.168.7.1 is UP

No. of Active hosts: 2

+--------------+-------------------+------------+
| IP Address   | MAC Address       | Hostname   |
+==============+===================+============+
| 192.168.7.3  | 46:a6:49:60:28:3d |            |
+--------------+-------------------+------------+
| 192.168.7.1  | 78:8c:b5:a6:7b:40 |            |
+--------------+-------------------+------------+

A graphical network map window is displayed showing the gateway at the center and all active hosts connected to it.

---

## 🏗️ Project Structure

NetworkScanner/
│
├── network_info.py      # Network detection & host discovery
├── device_details.py   # MAC & hostname enumeration
├── network_map.py      # Network visualization logic
└── README.md

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
    git clone https://github.com/The-Abhishek1/network-mapper.git 
    cd network-mapper

2️⃣ Create a virtual environment (recommended)

    python3 -m venv virtenv
    source virtenv/bin/activate

3️⃣ Install Python dependencies

    pip install -r requirements.txt

📦 Dependencies
  Python Libraries

    1.  scapy

    2.  networkx

    3.  matplotlib

    4.  tabulate

    5.  colorama (optional)

System Tools (Linux)

      nmblookup – NetBIOS hostname resolution

      avahi-resolve-address – mDNS hostname resolution

Install system tools:

      sudo apt install samba-common-bin avahi-utils

🚀 Usage

Run the scanner:

      python3 network_info.py

Network input options

    Press Enter → Auto-detect local /24 network

    Provide custom subnet:

      1.  192.168.1.0/24
      2.  10.0.0.0/24