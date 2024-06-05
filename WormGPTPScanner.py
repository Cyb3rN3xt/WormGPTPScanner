#!/usr/bin/env python

import socket
import time
from progress.bar import Bar

def display_banner():
    print("\033[92m")  # ANSI color code for green
    print(r"""

 #     #                       #####               ######  
 #  #  #  ####  #####  #    # #     # #####  ##### #     # 
 #  #  # #    # #    # ##  ## #       #    #   #   #     # 
 #  #  # #    # #    # # ## # #  #### #    #   #   ######  
 #  #  # #    # #####  #    # #     # #####    #   #       
 #  #  # #    # #   #  #    # #     # #        #   #       
  ## ##   ####  #    # #    #  #####  #        #   #       

                                                                                             
    """)
    print("\033[0m")  # Reset color
    print("Welcome to WormGPTProject by Cyb3rN3xt Pentesting Tool")
    print("Let's scan for open ports on the target IP address.")

def scan_ports(ip_address):
    open_ports = []
    port_types = {
        20: 'FTP Data', 21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 53: 'DNS',
        80: 'HTTP', 110: 'POP3', 143: 'IMAP', 443: 'HTTPS', 3306: 'MySQL', 3389: 'RDP'
    }
    
    with Bar('Scanning', max=1000) as bar:
        for port in range(1, 1001):  # Scan ports 1 to 1000
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set timeout for connection attempt
            result = sock.connect_ex((ip_address, port))  # Attempt to connect to the port
            if result == 0:
                open_ports.append((port, port_types.get(port, 'Unknown Service')))
            sock.close()
            bar.next()
            time.sleep(0.01)  # Simulate a delay for the loading bar
    return open_ports

def print_results(ip_address, open_ports):
    num_open_ports = len(open_ports)
    if num_open_ports > 0:
        print(f"\nOpen ports found on {ip_address}:")
        for port, service in open_ports:
            print(f"Port {port}: {service}")
        print(f"Number of open ports: {num_open_ports}")
    else:
        print(f"\nNo open ports found on {ip_address}")

def main():
    display_banner()
    ip_address = input("Enter the IP address to scan: ")
    open_ports = scan_ports(ip_address)
    print_results(ip_address, open_ports)

if __name__ == "__main__":
    main()
