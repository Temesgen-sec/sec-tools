import socket
ip = input("enter the ip to scan : ")
try:
    for port in range(1, 65536):
     with   socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
       sock.settimeout(5)
       result = sock.connect_ex((ip, port))
    if result == 0:
       print(f"port {port} is open ")
    else:
         print(f"port {port} is closed")
except (socket.error, ValueError) as error:
   print(f"error: {error}")
