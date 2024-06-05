#!/usr/bin/env python

import socket
import threading
from queue import Queue
import time
import sys

# Banner
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
    print("Let's scan for open ports on the target IP address.\n")

# Function to scan a single port
def scan_port(ip, port, open_ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    if result == 0:
        open_ports.append(port)
    sock.close()

# Function to handle threading
def threader(ip, open_ports):
    while True:
        worker = q.get()
        scan_port(ip, worker, open_ports)
        q.task_done()

# Loading bar
def loading_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if iteration == total:
        print()

# Main function
def main():
    display_banner()
    ip_address = input("Enter the IP address to scan: ")
    open_ports = []
    num_threads = 100
    ports = range(1, 1025)  # Scan ports 1 to 1024

    global q
    q = Queue()

    print("\nScanning in progress, please wait...")
    
    # Start threading
    for _ in range(num_threads):
        t = threading.Thread(target=threader, args=(ip_address, open_ports))
        t.daemon = True
        t.start()

    # Load the queue
    for worker in ports:
        q.put(worker)

    total_ports = len(ports)
    for i in range(total_ports):
        loading_bar(i + 1, total_ports, prefix='Progress:', suffix='Complete', length=50)
        time.sleep(0.01)  # Adjust if needed

    q.join()

    open_ports.sort()
    num_open_ports = len(open_ports)

    # Report results
    if num_open_ports > 0:
        print("\n\nScan complete!")
        print(f"Open ports found on {ip_address}: {open_ports}")
        print(f"Number of open ports: {num_open_ports}")
        print("Type of open doors:")
        for port in open_ports:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            print(f"Port {port}: {service}")
    else:
        print("\n\nNo open ports found on", ip_address)

if __name__ == "__main__":
    main()

