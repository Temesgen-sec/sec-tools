# Network Security & Port Scanning Toolkit

A collection of Python and Bash scripts developed for network discovery, port scanning, and automated reconnaissance tasks.

## Tools Included

1. **`custom_port_scanner.py`**
   * **Description:** A lightweight TCP port scanner built from scratch using Python's built-in `socket` library without external dependencies.
   * **Usage:** `python3 custom_port_scanner.py`

2. **`nmap_module_scanner.py`**
   * **Description:** A comprehensive port scanner utilizing the `python-nmap` wrapper library to query detailed port states and services.
   * **Usage:** `python3 nmap_module_scanner.py`

3. **`gateway_discovery.py`**
   * **Description:** A network routing utility that parses the system routing table to find the default gateway IP and determine its IPv4 class.
   * **Usage:** `python3 gateway_discovery.py`

4. **`nmap_nse_runner.sh`**
   * **Description:** A Bash automation script that accepts a target IP and an Nmap Scripting Engine (NSE) script name to execute targeted vulnerability scans.
   * **Usage:** `./nmap_nse_runner.sh <target-ip> <nse-script-name>`
