import pyfiglet
import sys
import socket
from datetime import datetime
import threading

# Using pyfiglet to make the ASCII art of the port scanner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# Target variable is a string in user input
target = input(str("Target IP : "))

# Banner
print("_" * 50)
print("Scanning Target: " + target)
print("Scanning started at : " + str(datetime.now()))
print("_" * 50)

# Function to scan a single port
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[*] Port {port} is open")
        s.close()
    except socket.error:
        print(f"[!] Couldn't connect to port {port}")

# Threaded scanner
def threaded_scanner(start_port, end_port):
    for port in range(start_port, end_port):
        thread = threading.Thread(target=scan_port, args=(port,))
        thread.start()

# Main script
try:
    # Define the port range
    start_port = 1
    end_port = 65535
    max_threads = 100  # Limit the number of threads to avoid resource exhaustion

    # Launch threads in chunks
    for i in range(start_port, end_port, max_threads):
        end_range = min(i + max_threads, end_port)
        threaded_scanner(i, end_range)

except KeyboardInterrupt:
    print("\n Exiting Application :")
    sys.exit()

except socket.error:
    print("\n Host not responding :")
    sys.exit()
