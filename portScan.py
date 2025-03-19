import socket

def scan_ports(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

# Example usage
target = "192.168.1.1"  # Replace with your target IP
ports = range(1, 1025)  # Scans ports 1 to 1024
scan_ports(target, ports)
