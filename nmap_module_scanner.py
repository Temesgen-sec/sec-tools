
import nmap
import sys
import time

nm = nmap.PortScanner()
target = input("Enter the IP to scan: ")


open_ports = 0
closed_ports = 0
filtered_ports = 0

try:
    print(f"\nScanning all ports (1-65535) on {target} ")

    
    start_time = time.time()


    nm.scan(
        target,
        arguments="-p 1-65535 -sV -T4"
    )

    
    end_time = time.time()

    print(f"\nScan completed in {end_time - start_time:.2f} seconds.")

    
    for host in nm.all_hosts():
        print(f"\nHost: {host}")

        for protocol in nm[host].all_protocols():
            print(f"Protocol: {protocol}")

            for port in sorted(nm[host][protocol].keys()):

                details = nm[host][protocol][port]
                state = details['state']

                
                if state == 'open':
                    open_ports += 1
                elif state == 'closed':
                    closed_ports += 1
                elif state == 'filtered':
                    filtered_ports += 1

                
                print(
                    f"Port: {port} "
                    f"State: {state} "
                    f"Service: {details.get('name', 'unknown')} "
                    f"Version: {details.get('version', 'unknown')}"
                )

    
    print("\n========== SCAN SUMMARY ==========")
    print(f"Target: {target}")
    print(f"Scan duration: {end_time - start_time:.2f} seconds")
    print(f"Open ports: {open_ports}")
    print(f"Closed ports: {closed_ports}")
    print(f"Filtered ports: {filtered_ports}")
    print("==================================")

except nmap.PortScannerError as error:
    print(f"Nmap error: {error}")

except KeyboardInterrupt:
    print("\nScan interrupted by user. Exiting.")
    sys.exit()

except Exception as error:
    print(f"An unexpected error occurred: {error}")
