import ipaddress as ip

def usable_hosts(net):
    if net.prefixlen == 32:
        return 1
    elif net.prefixlen == 31:
        return 2
    else:
        return net.num_addresses-2

def last_ip (last):
    if last.prefixlen<=30:
       return last.broadcast_address-1
    elif last.prefixlen == 31:
        return last.broadcast_address
    else:
        return last.network_address
    

print("""
    ╔══════════════════════════════════════╗
    ║        CIDR Calculator  •  IPv4      ║
    ╚══════════════════════════════════════╝

    ▸ Enter an IPv4 address with a prefix.
    ▸ Format : <IP>/<prefix>     Example : 192.168.1.0/24
    ▸ Prefix : 0 – 32

""")



while True:

    raw = input("Enter the IP address along with the prefix : " ,).strip()

    try:
        add = ip.IPv4Network(raw , strict=False)

        print(f"\nNetwork address : {add.network_address}")
        print(f"Broadcast addres : {add.broadcast_address}")
        print(f"First usable IP : {next(add.hosts())}")
        print(f"Last usable IP : {last_ip(add)}")
        print(f"Usable hosts : {usable_hosts(add)}")

    except (ip.AddressValueError , EOFError):
        print("\nInvalid input. Enter an IPv4 address with a prefix, example: 192.168.1.0/24\n")

    try:
        user_choice = input("\nDo you want to continue? (Y)  or  (N) :\n").strip()

    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!\n")
        break
    
    if user_choice.lower() == "n" or user_choice.lower() == "no":
        print("\nGoodbye!\n")
        break