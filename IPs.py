import ipaddress


ip = '192.168.0.1'

end = ipaddress.ip_address(ip)
print(end + 257)