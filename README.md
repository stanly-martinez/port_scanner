# port_scanner
Port Scanner

Description

This is a simple port scanner written in Python that scans the first 1024 ports of a given IP address to identify open ports. The script utilizes multithreading to improve scanning efficiency and provides real-time output of open ports.

How It Works

The script prompts the user to enter an IP address.

It then scans ports from 1 to 1024 using the socket library.

Each port is scanned using a separate thread to speed up the process.

If a port is open, it is added to the open_ports list and displayed in the console.

After scanning, the script outputs the number of open ports found.

Installation

This script requires Python 3.x.

Dependencies

No external dependencies are required.

Usage

Run the script using Python:

python3 port_scanner.py

Example Output

Enter the IP address: 192.168.1.1

Scanning 192.168.1.1...

✔ Port 22 is open.
✔ Port 80 is open.
✔ Port 443 is open.

✅ Scan completed. Found 3 open ports.

Notes

The scanner only checks ports 1-1024, which are commonly used.

The timeout for each port check is set to 0.5 seconds to balance speed and accuracy.

Requires user input for the target IP address.

License

This project is open-source and available for modification and distribution.
