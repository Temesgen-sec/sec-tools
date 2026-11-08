import nmap
import sys


nm = nmap.PortScanner()
target = input("enter the ip to scan : ")

try:
    print(f"Scanning all ports (1-65535) on {target}..:")
    nm.scan(target, arguments="-p 1-65535 -sV -T4")

    for host in nm.all_hosts():
        print(f"\nHost: {host}")
        for protocol in nm[host].all_protocols():
            print(f"Protocol: {protocol}")
            for port in sorted(nm[host][protocol].keys()):
                details = nm[host][protocol][port]
                print(
                    f"Port: {port} "
                    f"state: {details['state']} "
                    f"service: {details.get('name', 'unknown')}"
                )
                
except nmap.PortScannerError as error:
    print(f"Nmap error: {error}")
except KeyboardInterrupt:
    print("\nScan interrupted by user. Exiting.")
    sys.exit()
except Exception as error:
    print(f"An unexpected error occurred: {error}")
