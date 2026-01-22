from importlib.util import source_hash
from itertools import count

from ping3 import *
subnet_1 = 192
subnet_2 = 168
subnet_3 = 1
subnet_4 = 0
entity = "192.168.3.11"
status = True


def ip_to_str():
    ip_str = str(subnet_1) + "." + str(subnet_2) + "." + str(subnet_3) + "." + str(subnet_4)
    return(ip_str)


def entire_scan(subnet_4):
    running_ips = 0

    while subnet_4 <= 255:
        if (subnet_4 <= 255):
            print(ip_to_str() + " detected")
            running_ips += 1
            subnet_4 += 1
        else:
            print( ip_to_str()+ "... not found")
            subnet_4 += 1
    print(running_ips)

print("------------Welcome to SKARPER -----------")

verbose_ping ('google.com', count= 10)







entire_scan(subnet_4)
'''while status:
    ip_str = str(subnet_1) + "." + str(subnet_2) +"."+ str(subnet_3) +"." +  str(subnet_4)
    verbose_ping (ip_to_str(), timeout= 1)
    subnet_4 = subnet_4 + 1
'''