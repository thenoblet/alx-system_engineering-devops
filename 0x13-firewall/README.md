# Firewall Configuration Tasks

This repository contains solutions for configuring firewall settings on servers using the `ufw` (Uncomplicated Firewall) tool.

## Task 0: Block all incoming traffic but mandatory

### Description
The goal is to configure the `ufw` firewall on the `web-01` server to block all incoming traffic except for specific TCP ports.

### Requirements
- Configure `ufw` to block all incoming traffic except for ports 22 (SSH), 443 (HTTPS SSL), and 80 (HTTP).
- Provide the `ufw` commands used to achieve this configuration.

### Instructions
1. Install the `ufw` firewall if not already installed.
2. Configure `ufw` to block all incoming traffic by default: `sudo ufw default deny incoming`.
3. Allow incoming traffic on ports 22, 443, and 80: 
4. Enable the `ufw` firewall: `sudo ufw enable`.
5. Verify the `ufw` status to ensure the correct rules are applied: `sudo ufw status`.

### File Contents
```bash
# ufw configuration to block all incoming traffic except SSH, HTTPS, and HTTP
# Execute these commands on web-01 server

# Set default policies
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Allow SSH (port 22)
sudo ufw allow 22/tcp

# Allow HTTPS (port 443)
sudo ufw allow 443/tcp

# Allow HTTP (port 80)
sudo ufw allow 80/tcp

# Enable ufw
sudo ufw enable

# Check status
sudo ufw status
```

## Task 1: Port Forwarding

## Description
This task involves configuring port forwarding on the `web-01` server to redirect traffic from port 8080/TCP to port 80/TCP.

## Requirements
- Configure the firewall on `web-01` to forward incoming traffic from port 8080/TCP to port 80/TCP.
- Provide the modified `ufw` configuration file that achieves this.

## Instructions
1. Modify the `ufw` configuration to enable port forwarding from 8080 to 80.
2. Verify the changes by checking the `ufw` status.
3. Ensure that the web server (nginx) is listening on port 80.

## Terminal Output (web-01)
```bash
# Modified ufw configuration to enable port forwarding from 8080 to 80
# Execute these commands on web-01 server

# Edit the ufw configuration file
sudo nano /etc/default/ufw

# Add the following lines to enable port forwarding
DEFAULT_FORWARD_POLICY="ACCEPT"

