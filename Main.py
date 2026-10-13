import ipaddress
import sys

# Always use CIDR notation i.e 192.168.1.0/24 but checks if done so
def subnet_calc():
    print("\n--- Network Admin Subnet Calculator ---")
    print("Type 'exit' at any time to close the program.\n")
    
    # Outer loop: Handles entering/changing the main subnet
    while True:
        user_input = input("Enter a CIDR notation network (e.g., 10.0.0.0/16 or 192.168.1.50/24) or exit to leave: ").strip()
        
        # Global exit from the outer loop
        if user_input.lower() in ['exit']:
            print("\nExiting Subnet Calculator. Have a great day!")
            break
            
        try:
            # Check if the user forgot to include the CIDR notation (the slash)
            if '/' not in user_input:
                raise ValueError("Missing CIDR notation. Please include a subnet mask (e.g., /24).")

            # Check input and turn a host address into a network address
            network = ipaddress.ip_network(user_input, strict=False)

            # Print the given address and show the Network Address, Broadcast Address, Subnet Mask, Wildcard Mask and Total IP addresses
            print("\n" + "-"*50)
            print(f"  SUBNET ANALYSIS FOR: {network}")
            print("-"*50)
            print(f"Network Address:    {network.network_address}")
            print(f"Broadcast Address:  {network.broadcast_address}")
            print(f"Subnet Mask:        {network.netmask}")
            print(f"Wildcard Mask:      {network.hostmask}")
            print(f"Total IP Addresses: {network.num_addresses}")
            print("-"*50)

            # Shows what address can be used or how many hosts can be assigned without the network and broadcast in it, and catches point-to-point links
            if network.num_addresses > 2:
                hosts = list(network.hosts())
                print(f"Usable Host Range:  {hosts[0]} to {hosts[-1]}")
                print(f"Usable Host Count:  {len(hosts)}")
            else:
                # Tell user it's a Point-to-Point so no range available
                print("Usable Host Range:  N/A (Point-to-Point / Single Host)")
                
            print(f"IP Version:         IPv{network.version}")
            print(f"Address Type:       {'Private' if network.is_private else 'Public'}")
            print("-"*50)

            # Inner loop: Allows checking multiple IPs in THIS specific subnet without re-typing the CIDR
            while True:
                test_ip_str = input("\nEnter an IP to check in this subnet (or type 'new' for a different subnet or 'exit' to quit): ").strip()
                
                if test_ip_str.lower() in ['exit']:
                    print("\nExiting Subnet Calculator. Have a great day!")
                    sys.exit(0)
                elif test_ip_str.lower() in ['new']:
                    print("\n" + "="*30 + " SWITCHING SUBNET " + "="*30)
                    break # Breaks out of the inner loop and goes back to asking for a new CIDR
                    
                try:
                    test_ip = ipaddress.ip_address(test_ip_str)
                    if test_ip in network:
                        print(f"  -> SUCCESS: {test_ip} IS inside the subnet {network}.")
                    else:
                        print(f"  -> NO MATCH: {test_ip} IS NOT inside the subnet {network}.")
                except ValueError:
                    print(f"ERROR: '{test_ip_str}' is not a valid IP address.")
                
        except ValueError as e:
            print(f"\n[ERROR] Invalid input: {e}\n", file=sys.stderr)

if __name__ == "__main__":
    subnet_calc()