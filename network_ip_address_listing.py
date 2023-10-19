# List of IP addresses
ip_addresses = [
    "192.168.80.20",
    "192.168.60.1",
    "192.168.91.23",
    "192.168.60.43",
    "192.168.60.22",
    "192.168.61.50",
    "192.168.60.98",
    "192.168.1.24",
    "192.168.60.13",
    "192.168.60.47",
    ]

# Filter IP addresses out that don't belong in .60 subnet
filtered_ip_addresses = [ip for ip in ip_addresses if ip.split('.')[2] == '60']

for ip in filtered_ip_addresses:
    print(ip)