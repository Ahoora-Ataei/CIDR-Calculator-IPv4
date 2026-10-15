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

raw = input("Enter the IP address along with the prefix : " ,).strip()


add = ip.ip_network(raw , strict=False)


print(f"\nNetwork address : {add.network_address}")
print(f"Broadcast addres : {add.broadcast_address}")
print(f"First usable IP : {next(add.hosts())}")
print(f"Last usable IP : {last_ip(add)}")
print(f"Usable hosts : {usable_hosts(add)}")