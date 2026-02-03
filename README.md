# Network Mapper 🕸️

A Python-based **local network discovery and visualization tool** that scans your subnet, identifies active hosts, resolves MAC addresses and hostnames, and visualizes the network in a **gateway-centric logical map**.

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