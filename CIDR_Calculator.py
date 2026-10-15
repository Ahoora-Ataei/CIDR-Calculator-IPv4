import ipaddress as ip

def usable_hosts(net):
    if net.prefixlen == 32:
        return 1
    elif net.prefixlen == 31:
        return 2
    else:
        return net.num_addresses-2


raw = input("Enter the IP address along with the prefix : " ,).strip()

add = ip.ip_network(raw , strict=False)

print(f"\nNetwork address : {add.network_address}")
print(f"Broadcast addres : {add.broadcast_address}")
print(f"First usable IP : {next(add.hosts())}")
print(f"Last usable IP : {add.broadcast_address-1}")
print(f"Usable hosts : {usable_hosts(add)}")
