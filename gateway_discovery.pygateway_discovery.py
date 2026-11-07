import subprocess
import ipaddress

def get_default_gateway():
    try:
       
        result = subprocess.check_output("ip route show default", shell=True).decode()
        parts = result.split()
        if "via" in parts:
            return parts[parts.index("via") + 1]
    except Exception as e:
        print(f"Error fetching gateway: {e}")
    return None

def get_ip_class(ip_str):
    try:
        ip_obj = ipaddress.ip_address(ip_str)
        if ip_obj.version == 4:
            first_octet = int(ip_str.split('.')[0])
            if 1 <= first_octet <= 126:
                return "Class A"
            elif 128 <= first_octet <= 191:
                return "Class B"
            elif 192 <= first_octet <= 223:
                return "Class C"
            elif 224 <= first_octet <= 239:
                return "Class D (Multicast)"
            elif 240 <= first_octet <= 255:
                return "Class E (Experimental)"
            elif first_octet == 127:
                return "Loopback"
        return "IPv6 or Non-Standard"
    except ValueError:
        return "Invalid IP Address"

if __name__ == "__main__":
    gateway = get_default_gateway()
    
    if gateway:
        ip_class = get_ip_class(gateway)
        print(f"Gateway IP : {gateway}")
        print(f"IP Class   : {ip_class}")
    else:
        print("Could not automatically detect the default gateway.")
