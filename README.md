# Network Subnet Calculator

# A lightweight, interactive Python utility designed for network administrators and students to quickly analyze IPv4 subnets, calculate host ranges, and verify IP address memberships.

## Features

- **Subnet Analysis:** Instantly calculates the Network Address, Broadcast Address, Standard Subnet Mask, and Cisco-style Wildcard Mask.
- **Host Range Calculation:** Automatically determines the usable host range and total host count, with built-in safety handling for point-to-point (`/31` or `/32`) links.
- **IP Version & Type Detection:** Identifies whether the network is IPv4 and flags it as a Private or Public address block.
- **Interactive IP Checker:** Allows you to test multiple specific IP addresses against the calculated subnet without re-typing the network range.
- **Error Handling:** Validates CIDR notation formatting and catches invalid IP inputs.

## Getting Started

## Prerequisites
### Make sure you have **Python 3.x** installed on your machine. You can verify your installation by running:
```bash
python --version
```

- Clone or download this repository to your local machine.
- Open your terminal or command prompt inside the project folder.
- Run the script:
```bash
python Main.py
```

Follow the interactive prompts on the screen! 
Type new to switch subnets or exit to close the program.
