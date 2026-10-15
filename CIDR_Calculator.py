import ipaddress as ip

raw = input("Enter the IP address along with the prefix : ").strip()

add = ip.ip_network(raw)

print(f"Network address : {add.network_address}")
print(f"Broadcast addres : {add.broadcast_address}")
