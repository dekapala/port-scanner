# Port Scanner (Python)

This is a simple TCP port scanner written in Python. It allows the user to specify a target host (IP address or domain name) and a port range to identify open ports on the target.

## Features

- Basic TCP socket scanning
- Customizable port range
- Fast timeout-based connection attempts
- Command-line input prompts

## Use Case

This project is designed for educational and demonstration purposes, particularly for those interested in cybersecurity and network fundamentals. It can be used to understand how basic scanning tools like Nmap operate under the hood.

## Requirements

- Python 3.x

No external libraries are required.

## How to Use

1. Clone the repository:

```bash
git clone https://github.com/your-username/port-scanner.git
cd port-scanner

Run the script:

python scanner.py

Follow the on-screen instructions:

Enter target IP or domain: scanme.nmap.org
Start port: 20
End port: 80

Example Output

Port 22 is OPEN
Port 80 is OPEN

Author
Gabriel palazzini

Disclaimer
This tool is intended for educational purposes only. Do not use it to scan networks or hosts without explicit permission.
