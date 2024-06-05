import socket

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
    for port in range(1, 1001):  # Scan ports 1 to 1000
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout for connection attempt
        result = sock.connect_ex((ip_address, port))  # Attempt to connect to the port
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def print_results(ip_address, open_ports):
    num_open_ports = len(open_ports)
    if num_open_ports > 0:
        print("\nOpen ports found on {}: {}".format(ip_address, open_ports))
        print("Number of open ports:", num_open_ports)
    else:
        print("\nNo open ports found on", ip_address)

def main():
    display_banner()
    ip_address = input("Enter the IP address to scan: ")
    open_ports = scan_ports(ip_address)
    print_results(ip_address, open_ports)

if __name__ == "__main__":
    main()
