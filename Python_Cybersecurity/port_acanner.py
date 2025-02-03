import socket
import threading

open_ports = []  # List to store open ports

def scan_port(host, port):
    """Scan a specific port on the given host."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)  
        if s.connect_ex((host, port)) == 0:
            open_ports.append(port)  # add open port to list
            print(f"✔ Port {port} is open.")

def port_scanner():
    """Main function to request IP and scan ports."""
    global open_ports
    host = input("Enter the IP address: ")
    ports = range(1, 1025)  # Commun ports

    print(f"\nScanning {host}...\n")

    threads = []  # List to manage threads
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(host, port))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Show message if no ports are open
    if not open_ports:
        print("\n❌ No open ports found.")
    else:
        print(f"\n✅ Scan completed. Found {len(open_ports)} open ports.")

if __name__ == "__main__":
    port_scanner()


### for excute run: python3 port_scanner.py ###
