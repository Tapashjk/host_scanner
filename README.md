# Network Scanner

## Overview
This program scans a given network to identify all connected devices. It provides detailed information, including **IP addresses**, **MAC addresses**, and, when possible, **device names**. Designed for simplicity, it works effectively on any local network.

---

## Features
- Scans for devices connected to a given network.
- Provides the **IP address**, **MAC address**, and **device name** (if resolvable).
- Lightweight and efficient.

---

## Requirements
- **Python 3.x** installed on your system.
- The following Python libraries:
  - `scapy` (for network scanning)
  - `socket` (for hostname resolution)

Install dependencies with:
```bash
pip install scapy
```

---

## How to Use
1. Clone or download this repository.
2. Run the program with administrator/root privileges:
   ```bash
   python network_scanner.py
   ```
3. Enter the router's IP address when prompted (e.g., `192.168.1.1`).
4. The program will scan the network and display:
   - Connected device count.
   - **IP address**, **MAC address**, and **device name** of each device.

### Example Input:
```
Enter your router's IP address (e.g., 192.168.1.1): 192.168.1.1
```

### Example Output:
```
Scanning devices connected to the router with IP: 192.168.1.1...

Found 3 devices connected:

IP Address         MAC Address         Device Name
-----------------------------------------------
192.168.1.1        00:1A:2B:3C:4D:5E  MyRouter
192.168.1.100      00:1B:2C:3D:4E:5F  John-PC
192.168.1.101      00:1C:2D:3E:4F:5G  Unknown
```

---

## Limitations
- This program works only on **local networks**.
- It must be run on a device **connected to the target network**.
- Device names may show as `Unknown` if the hostname cannot be resolved.



## Notes
- Use this program ethically and responsibly.
- Ensure you have permission to scan the network.

