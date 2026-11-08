
import socket
import time
import ipaddress

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))

            if result == 0:
                return port

    except OSError:
        pass

    return None


def main():
    ip = input("Enter the IP to scan: ")

    
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print("Invalid IP address!")
        return

    open_ports = []

    print(f"\nScanning {ip}...")
    start_time = time.time()

    try:
        for port in range(1, 65536):
            result = scan_port(ip, port)

            if result is not None:
                print(f"[+] Port {result} is OPEN")
                open_ports.append(result)

    except KeyboardInterrupt:
        print("\nScan interrupted by user.")

    end_time = time.time()

    
    print("\n========== SCAN SUMMARY ==========")
    print(f"Target: {ip}")
    print(f"Open ports found: {len(open_ports)}")
    print(f"Open ports: {open_ports}")
    print(f"Scan duration: {end_time - start_time:.2f} seconds")
    print("==================================")


if __name__ == "__main__":
    main()
