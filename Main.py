import ipaddress
import sys

# Always use CIDR notation i.e 192.168.1.0/24
def calc_subnet(cidr_input):
    try:
        #Check input and turn a host address into a network address
        network = ipaddress.ip_network(cidr_input, strict=False)

        #Print the given address and show the Network Address,Broadcast Address,Subnet Mask,Wildcard Mask and Total IP addresses
        print("\n" + "-"*50)
        print(f"  SUBNET ANALYSIS FOR: {network}")
        print("-"*50)
        print(f"Network Address:    {network.network_address}")
        print(f"Broadcast Address:  {network.broadcast_address}")
        print(f"Subnet Mask:        {network.netmask}")
        print(f"Wildcard Mask:      {network.hostmask}")
        print(f"Total IP Addresses: {network.num_addresses}")
        print("-"*50)

        #shows what address can be used or how many hosts can be assigned without the network and broadcast in it and also catches if its a point to point
        # Calculate usable host range
        if network.num_addresses > 2:
            hosts = list(network.hosts())
            print(f"Usable Host Range:  {hosts[0]} to {hosts[-1]}")
            print(f"Usable Host Count:  {len(hosts)}")
        else:
            #tell user its a Point to Point so no range available
            print("Usable Host Range:  N/A (Point-to-Point / Single Host)")
            
        print(f"IP Version:         IPv{network.version}")
        print(f"Address Type:       {'Private' if network.is_private else 'Public'}")
        print("-"*50)

        # Check if a specific IP belongs to this calculated subnet
        check_ip = input("\nWould you like to check if a specific IP address is in this subnet? (y/n): ").strip().lower()
        if check_ip == 'y':
            test_ip_str = input("Enter IP address to check: ").strip()
            try:
                test_ip = ipaddress.ip_address(test_ip_str)
                if test_ip in network:
                    print(f"SUCCESS: {test_ip} IS inside the subnet {network}.")
                else:
                    print(f"NO MATCH: {test_ip} IS NOT inside the subnet {network}.")
            except ValueError:
                print(f"ERROR: '{test_ip_str}' is not a valid IP address.")
                
    except ValueError as e:
        print(f"\n[ERROR] Invalid CIDR notation: {e}", file=sys.stderr)

if __name__ == "__main__":
    print("\n--- Network Admin Subnet Calculator ---")
    user_input = input("Enter a CIDR notation network (e.g., 10.0.0.0/16 or 192.168.1.50/24): ").strip()
    calc_subnet(user_input)