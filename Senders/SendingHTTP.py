from scapy.all import *

bytes = 400
ip = "192.168.1.102"
num_of_packages = 7200
interval = 0.05

http_packet = IP(dst=ip)/TCP(dport=80)/Raw(RandString(size=bytes))
send(http_packet, inter=interval, loop=True, count=num_of_packages)